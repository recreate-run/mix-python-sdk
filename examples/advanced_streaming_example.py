#!/usr/bin/env python3
"""
Advanced Streaming Example for Mix Python SDK

Documentation Reference: docs/sdks/streaming/README.md

This example demonstrates comprehensive streaming functionality with production-ready patterns:
- Persistent SSE state management with connection lifecycle tracking
- Advanced event processing for all event types (thinking, content, tool, permission, complete, error)
- Timeline tracking for real-time processing visualization
- Tool execution monitoring with lifecycle management
- Permission handling workflows with grant/deny operations
- Cancellation support and error recovery
- Rate limiting and reconnection handling
- Thread-safe operations and resource cleanup

This implementation mirrors sophisticated client-side streaming patterns for enterprise applications.
"""

from mix_python_sdk import Mix
import os
from dotenv import load_dotenv
import time
import threading
from dataclasses import dataclass, field
from typing import List, Dict, Optional, Any, Callable
from enum import Enum
import json
import uuid


class StreamingState(Enum):
    DISCONNECTED = "disconnected"
    CONNECTING = "connecting"
    CONNECTED = "connected"
    PROCESSING = "processing"
    PAUSED = "paused"
    CANCELLED = "cancelled"
    ERROR = "error"
    COMPLETED = "completed"


class TimelineEntryType(Enum):
    THINKING = "thinking"
    CONTENT = "content"
    TOOL = "tool"
    PERMISSION = "permission"
    ERROR = "error"


class ToolStatus(Enum):
    PENDING = "pending"
    RUNNING = "running"
    COMPLETED = "completed"
    ERROR = "error"


@dataclass
class TimelineEntry:
    id: str
    type: TimelineEntryType
    timestamp: float
    content: Any
    metadata: Dict[str, Any] = field(default_factory=dict)


@dataclass
class ToolCall:
    id: str
    name: str
    description: str
    status: ToolStatus
    parameters: Dict[str, Any]
    result: Optional[str] = None
    error: Optional[str] = None
    start_time: Optional[float] = None
    end_time: Optional[float] = None

    @property
    def duration(self) -> Optional[float]:
        if self.start_time and self.end_time:
            return self.end_time - self.start_time
        return None


@dataclass
class PermissionRequest:
    id: str
    session_id: str
    tool_name: str
    description: str
    action: str
    path: str = ""
    params: Dict[str, Any] = field(default_factory=dict)


@dataclass
class RateLimit:
    retry_after: int
    attempt: int
    max_attempts: int


@dataclass
class StreamingStats:
    messages_sent: int = 0
    events_received: int = 0
    tools_executed: int = 0
    permissions_requested: int = 0
    connection_time: Optional[float] = None
    total_processing_time: float = 0


class AdvancedStreamingManager:
    """Advanced streaming manager with persistent state and comprehensive event handling"""

    def __init__(self, mix_client: Mix, session_id: str):
        self.mix = mix_client
        self.session_id = session_id

        # Connection state
        self.state = StreamingState.DISCONNECTED
        self.error: Optional[str] = None
        self.last_event_id: Optional[str] = None

        # Processing state
        self.is_processing = False
        self.is_cancelling = False
        self.reasoning: str = ""
        self.reasoning_duration: Optional[float] = None
        self.final_content: str = ""
        self.completed = False

        # Collections
        self.timeline: List[TimelineEntry] = []
        self.tool_calls: Dict[str, ToolCall] = {}
        self.permission_requests: Dict[str, PermissionRequest] = {}

        # Rate limiting
        self.rate_limit: Optional[RateLimit] = None

        # Threading
        self.stream_thread: Optional[threading.Thread] = None
        self.abort_event = threading.Event()
        self.state_lock = threading.Lock()

        # Statistics
        self.stats = StreamingStats()

        # Callbacks
        self.on_state_change: Optional[Callable[[StreamingState], None]] = None
        self.on_content_delta: Optional[Callable[[str], None]] = None
        self.on_tool_update: Optional[Callable[[ToolCall], None]] = None
        self.on_permission_request: Optional[Callable[[PermissionRequest], None]] = None

    def _update_state(self, new_state: StreamingState, error: Optional[str] = None):
        """Thread-safe state update with callback notification"""
        with self.state_lock:
            old_state = self.state
            self.state = new_state
            self.error = error

            if self.on_state_change and old_state != new_state:
                self.on_state_change(new_state)

    def _add_timeline_entry(self, entry_type: TimelineEntryType, content: Any, metadata: Optional[Dict[str, Any]] = None):
        """Add entry to timeline with thread safety"""
        entry = TimelineEntry(
            id=str(uuid.uuid4()),
            type=entry_type,
            timestamp=time.time(),
            content=content,
            metadata=metadata or {}
        )

        with self.state_lock:
            self.timeline.append(entry)

        return entry

    def start_streaming(self):
        """Start the persistent SSE connection"""
        if self.state in [StreamingState.CONNECTING, StreamingState.CONNECTED]:
            print("Streaming already active")
            return

        self._update_state(StreamingState.CONNECTING)
        self.abort_event.clear()

        # Clear previous state
        with self.state_lock:
            self.timeline.clear()
            self.tool_calls.clear()
            self.permission_requests.clear()
            self.reasoning = ""
            self.final_content = ""
            self.completed = False
            self.stats.connection_time = time.time()

        # Start streaming thread
        self.stream_thread = threading.Thread(target=self._stream_processor, daemon=True)
        self.stream_thread.start()
        print("Streaming connection initiated")

    def _stream_processor(self):
        """Main SSE event processing loop"""
        try:
            print(f"Establishing SSE connection for session: {self.session_id}")
            stream_response = self.mix.streaming.stream_events(
                session_id=self.session_id,
                last_event_id=self.last_event_id
            )

            self._update_state(StreamingState.CONNECTED)
            print("SSE connection established successfully")

            for event in stream_response:
                if self.abort_event.is_set():
                    break

                # Track event ID for reconnection
                if hasattr(event, 'id') and event.id:
                    self.last_event_id = event.id

                self.stats.events_received += 1
                self._process_event(event)

        except Exception as e:
            error_msg = f"Stream processing error: {str(e)}"
            print(error_msg)
            self._update_state(StreamingState.ERROR, error_msg)
            self._add_timeline_entry(TimelineEntryType.ERROR, error_msg)

    def _process_event(self, event):
        """Process individual SSE events with comprehensive handling"""
        event_type = event.event if hasattr(event, 'event') else event['event']
        event_data = event.data if hasattr(event, 'data') else event['data']

        print(f"Processing event: {event_type}")

        if event_type == "connected":
            self._add_timeline_entry(
                TimelineEntryType.CONTENT,
                "SSE connection established",
                {"event_type": "connected"}
            )

        elif event_type == "heartbeat":
            # Heartbeat events keep connection alive
            pass

        elif event_type == "thinking":
            content = event_data.get('content') or event_data['content'] if 'content' in event_data else ''
            if content:
                with self.state_lock:
                    self.reasoning += content

                self._add_timeline_entry(
                    TimelineEntryType.THINKING,
                    content,
                    {"reasoning_total_length": len(self.reasoning)}
                )

                if not self.is_processing:
                    self.is_processing = True
                    self._update_state(StreamingState.PROCESSING)

        elif event_type == "content":
            content = event_data.get('content') or event_data['content'] if 'content' in event_data else ''
            if content:
                with self.state_lock:
                    self.final_content += content

                self._add_timeline_entry(
                    TimelineEntryType.CONTENT,
                    content,
                    {"content_total_length": len(self.final_content)}
                )

                if self.on_content_delta:
                    self.on_content_delta(content)

        elif event_type == "tool":
            self._handle_tool_event(event_data)

        elif event_type == "tool_execution_start":
            self._handle_tool_execution_start(event_data)

        elif event_type == "tool_execution_complete":
            self._handle_tool_execution_complete(event_data)

        elif event_type == "permission":
            self._handle_permission_event(event_data)

        elif event_type == "complete":
            self._handle_completion_event(event_data)

        elif event_type == "error":
            self._handle_error_event(event_data)

        else:
            print(f"Unhandled event type: {event_type}")

    def _handle_tool_event(self, event_data):
        """Handle tool execution events"""
        tool_id = event_data['id'] if 'id' in event_data else str(uuid.uuid4())
        tool_name = event_data['name']
        tool_status = event_data['status']
        tool_input = event_data.get('input', {})

        # Parse input if it's a string
        if isinstance(tool_input, str):
            tool_input = json.loads(tool_input)

        tool_call = ToolCall(
            id=tool_id,
            name=tool_name,
            description=f"Executing {tool_name}",
            status=ToolStatus(tool_status),
            parameters=tool_input,
            start_time=time.time() if tool_status == "running" else None
        )

        with self.state_lock:
            self.tool_calls[tool_id] = tool_call

        self._add_timeline_entry(
            TimelineEntryType.TOOL,
            tool_call,
            {"tool_status": tool_status}
        )

        if self.on_tool_update:
            self.on_tool_update(tool_call)

        print(f"Tool {tool_name} [{tool_id}]: {tool_status}")

    def _handle_tool_execution_start(self, event_data):
        """Handle tool execution start events"""
        tool_call_id = event_data['tool_call_id']
        progress = event_data['progress']

        if tool_call_id and tool_call_id in self.tool_calls:
            tool_call = self.tool_calls[tool_call_id]
            tool_call.status = ToolStatus.RUNNING
            tool_call.description = progress
            tool_call.start_time = time.time()

            self._add_timeline_entry(
                TimelineEntryType.TOOL,
                f"Tool execution started: {progress}",
                {"tool_id": tool_call_id, "progress": progress}
            )

            if self.on_tool_update:
                self.on_tool_update(tool_call)

    def _handle_tool_execution_complete(self, event_data):
        """Handle tool execution completion events"""
        tool_call_id = event_data['tool_call_id']
        progress = event_data['progress']
        success = event_data.get('success', True)

        if tool_call_id and tool_call_id in self.tool_calls:
            tool_call = self.tool_calls[tool_call_id]
            tool_call.status = ToolStatus.COMPLETED if success else ToolStatus.ERROR
            tool_call.end_time = time.time()

            if success:
                tool_call.result = progress
            else:
                tool_call.error = progress

            self.stats.tools_executed += 1

            self._add_timeline_entry(
                TimelineEntryType.TOOL,
                f"Tool execution {'completed' if success else 'failed'}: {progress}",
                {"tool_id": tool_call_id, "success": success, "duration": tool_call.duration}
            )

            if self.on_tool_update:
                self.on_tool_update(tool_call)

    def _handle_permission_event(self, event_data):
        """Handle permission request events"""
        permission = PermissionRequest(
            id=event_data.get('id', str(uuid.uuid4())),
            session_id=event_data.get('session_id', self.session_id),
            tool_name=event_data['tool_name'],
            description=event_data['description'],
            action=event_data['action'],
            path=event_data.get('path', ''),
            params=event_data.get('params', {})
        )

        with self.state_lock:
            self.permission_requests[permission.id] = permission

        self.stats.permissions_requested += 1

        self._add_timeline_entry(
            TimelineEntryType.PERMISSION,
            permission,
            {"permission_id": permission.id, "tool_name": permission.tool_name}
        )

        if self.on_permission_request:
            self.on_permission_request(permission)

        print(f"Permission requested: {permission.description}")

    def _handle_completion_event(self, event_data):
        """Handle message processing completion"""
        self.reasoning = event_data.get('reasoning', '') or self.reasoning
        self.reasoning_duration = event_data.get('reasoning_duration', None)

        with self.state_lock:
            self.completed = True
            self.is_processing = False

        if self.stats.connection_time:
            self.stats.total_processing_time = time.time() - self.stats.connection_time

        self._update_state(StreamingState.COMPLETED)

        self._add_timeline_entry(
            TimelineEntryType.CONTENT,
            "Message processing completed",
            {
                "reasoning_duration": self.reasoning_duration,
                "total_processing_time": self.stats.total_processing_time,
                "final_content_length": len(self.final_content)
            }
        )

        print("Message processing completed!")

    def _handle_error_event(self, event_data):
        """Handle error events with rate limiting support"""
        error_msg = event_data.get('error', 'Unknown error')
        retry_after = event_data.get('retry_after', None)
        attempt = event_data.get('attempt', 1)
        max_attempts = event_data.get('max_attempts', 8)

        if retry_after:
            self.rate_limit = RateLimit(
                retry_after=retry_after,
                attempt=attempt,
                max_attempts=max_attempts
            )

        self._update_state(StreamingState.ERROR, error_msg)

        self._add_timeline_entry(
            TimelineEntryType.ERROR,
            error_msg,
            {
                "retry_after": retry_after,
                "attempt": attempt,
                "max_attempts": max_attempts
            }
        )

        print(f"Error: {error_msg}")
        if retry_after:
            print(f"Rate limited - retry after {retry_after}ms (attempt {attempt}/{max_attempts})")

    def send_message(self, content: str) -> bool:
        """Send a streaming message with state management"""
        if self.state != StreamingState.CONNECTED:
            print(f"Cannot send message - not connected (state: {self.state})")
            return False

        try:
            # Reset processing state
            with self.state_lock:
                self.final_content = ""
                self.reasoning = ""
                self.completed = False
                self.is_processing = False
                self.is_cancelling = False
                self.tool_calls.clear()
                self.timeline.clear()

            self._update_state(StreamingState.PROCESSING)

            print(f"Sending message: {content}")
            response = self.mix.streaming.send_streaming_message(
                id=self.session_id,
                content=content
            )

            self.stats.messages_sent += 1

            self._add_timeline_entry(
                TimelineEntryType.CONTENT,
                f"Message sent: {content}",
                {"message_length": len(content)}
            )

            print(f"Message sent successfully: {response.status if hasattr(response, 'status') else 'Response received'}")
            return True

        except Exception as e:
            error_msg = f"Failed to send message: {str(e)}"
            self._update_state(StreamingState.ERROR, error_msg)
            raise

    def cancel_message(self) -> bool:
        """Cancel current message processing"""
        if not self.is_processing:
            print("No message currently processing")
            return False

        try:
            self.is_cancelling = True
            self._update_state(StreamingState.PAUSED)

            # Use sessions API to cancel processing
            self.mix.sessions.cancel_processing(id=self.session_id)

            with self.state_lock:
                self.is_processing = False
                self.is_cancelling = False

            self._update_state(StreamingState.CANCELLED)

            self._add_timeline_entry(
                TimelineEntryType.CONTENT,
                "Message processing cancelled",
                {"cancelled_at": time.time()}
            )

            print("Message processing cancelled")
            return True

        except Exception as e:
            error_msg = f"Failed to cancel message: {str(e)}"
            self._update_state(StreamingState.ERROR, error_msg)
            raise

    def grant_permission(self, permission_id: str) -> bool:
        """Grant a permission request"""
        if permission_id not in self.permission_requests:
            print(f"Permission request {permission_id} not found")
            return False

        try:
            self.mix.permissions.grant(id=permission_id)

            with self.state_lock:
                permission = self.permission_requests.pop(permission_id)

            self._add_timeline_entry(
                TimelineEntryType.PERMISSION,
                f"Permission granted: {permission.description}",
                {"permission_id": permission_id, "action": "granted"}
            )

            print(f"Permission granted: {permission.description}")
            return True

        except Exception as e:
            error_msg = f"Failed to grant permission: {str(e)}"
            raise Exception(error_msg) from e

    def deny_permission(self, permission_id: str) -> bool:
        """Deny a permission request"""
        if permission_id not in self.permission_requests:
            print(f"Permission request {permission_id} not found")
            return False

        try:
            self.mix.permissions.deny(id=permission_id)

            with self.state_lock:
                permission = self.permission_requests.pop(permission_id)

            self._add_timeline_entry(
                TimelineEntryType.PERMISSION,
                f"Permission denied: {permission.description}",
                {"permission_id": permission_id, "action": "denied"}
            )

            print(f"Permission denied: {permission.description}")
            return True

        except Exception as e:
            error_msg = f"Failed to deny permission: {str(e)}"
            raise Exception(error_msg) from e

    def get_timeline_summary(self) -> str:
        """Get a formatted summary of the timeline"""
        if not self.timeline:
            return "No timeline entries"

        summary = ["\n=== TIMELINE SUMMARY ==="]

        for entry in self.timeline:
            timestamp = time.strftime("%H:%M:%S", time.localtime(entry.timestamp))

            if entry.type == TimelineEntryType.THINKING:
                content_preview = str(entry.content)[:100] + ("..." if len(str(entry.content)) > 100 else "")
                summary.append(f"[{timestamp}] THINKING: {content_preview}")

            elif entry.type == TimelineEntryType.CONTENT:
                if isinstance(entry.content, str) and entry.content.startswith("Message") or entry.content.startswith("SSE"):
                    summary.append(f"[{timestamp}] EVENT: {entry.content}")
                else:
                    content_preview = str(entry.content)[:100] + ("..." if len(str(entry.content)) > 100 else "")
                    summary.append(f"[{timestamp}] CONTENT: {content_preview}")

            elif entry.type == TimelineEntryType.TOOL:
                if isinstance(entry.content, ToolCall):
                    tool = entry.content
                    summary.append(f"[{timestamp}] TOOL: {tool.name} [{tool.status.value}] - {tool.description}")
                else:
                    summary.append(f"[{timestamp}] TOOL: {entry.content}")

            elif entry.type == TimelineEntryType.PERMISSION:
                if isinstance(entry.content, PermissionRequest):
                    perm = entry.content
                    summary.append(f"[{timestamp}] PERMISSION: {perm.tool_name} - {perm.description}")
                else:
                    summary.append(f"[{timestamp}] PERMISSION: {entry.content}")

            elif entry.type == TimelineEntryType.ERROR:
                summary.append(f"[{timestamp}] ERROR: {entry.content}")

        return "\n".join(summary)

    def get_stats_summary(self) -> str:
        """Get a formatted summary of statistics"""
        return f"""
=== STREAMING STATISTICS ===
State: {self.state.value}
Messages Sent: {self.stats.messages_sent}
Events Received: {self.stats.events_received}
Tools Executed: {self.stats.tools_executed}
Permissions Requested: {self.stats.permissions_requested}
Total Processing Time: {self.stats.total_processing_time:.2f}s
Timeline Entries: {len(self.timeline)}
Active Tool Calls: {len([t for t in self.tool_calls.values() if t.status == ToolStatus.RUNNING])}
Pending Permissions: {len(self.permission_requests)}
Final Content Length: {len(self.final_content)}
Reasoning Length: {len(self.reasoning)}
"""

    def stop_streaming(self):
        """Stop the streaming connection and cleanup resources"""
        print("Stopping streaming connection...")

        # Signal abort to stream processor
        self.abort_event.set()

        # Wait for stream thread to finish
        if self.stream_thread and self.stream_thread.is_alive():
            self.stream_thread.join(timeout=5)

        self._update_state(StreamingState.DISCONNECTED)
        print("Streaming connection stopped")


def demonstrate_basic_streaming(manager: AdvancedStreamingManager):
    """Demonstrate basic streaming with content accumulation"""
    print("\n" + "="*60)
    print("BASIC STREAMING DEMONSTRATION")
    print("="*60)

    # Setup callbacks for real-time updates
    def on_content(delta: str):
        print(f"CONTENT DELTA: {delta}", end="", flush=True)

    def on_state_change(state: StreamingState):
        print(f"\nSTATE CHANGED: {state.value}")

    manager.on_content_delta = on_content
    manager.on_state_change = on_state_change

    # Start streaming and send message
    manager.start_streaming()

    # Wait for connection
    timeout = 10
    start_time = time.time()
    while manager.state != StreamingState.CONNECTED and time.time() - start_time < timeout:
        time.sleep(0.1)

    if manager.state != StreamingState.CONNECTED:
        print("Failed to establish connection")
        return

    # Send a message that will generate thinking and content
    manager.send_message("Say hi")

    # Wait for completion
    timeout = 60
    start_time = time.time()
    while not manager.completed and time.time() - start_time < timeout:
        if manager.state == StreamingState.ERROR:
            print(f"\nError occurred: {manager.error}")
            break
        time.sleep(0.5)

    print("\n" + manager.get_timeline_summary())
    print(manager.get_stats_summary())


def demonstrate_tool_execution_monitoring(manager: AdvancedStreamingManager):
    """Demonstrate tool execution monitoring"""
    print("\n" + "="*60)
    print("TOOL EXECUTION MONITORING DEMONSTRATION")
    print("="*60)

    # Setup tool monitoring callback
    def on_tool_update(tool: ToolCall):
        status_icon = {
            ToolStatus.PENDING: "⏳",
            ToolStatus.RUNNING: "🔄",
            ToolStatus.COMPLETED: "✅",
            ToolStatus.ERROR: "❌"
        }

        icon = status_icon.get(tool.status, "❓")
        duration_str = f" ({tool.duration:.2f}s)" if tool.duration else ""
        print(f"{icon} {tool.name}: {tool.description}{duration_str}")

    manager.on_tool_update = on_tool_update

    # Send a message that might trigger tool usage
    message = """
    I need you to help me analyze this codebase. Please:
    1. Search for Python files containing 'streaming' in their name
    2. Read one of those files and explain its main functionality
    3. Show me the current directory structure

    This should demonstrate tool execution monitoring.
    """

    success = manager.send_message(message.strip())
    if not success:
        print("Failed to send message")
        return

    # Monitor for completion or timeout
    timeout = 120  # Longer timeout for tool execution
    start_time = time.time()
    while not manager.completed and time.time() - start_time < timeout:
        if manager.state == StreamingState.ERROR:
            print(f"\nError occurred: {manager.error}")
            break
        time.sleep(1)

    print("\n" + manager.get_timeline_summary())
    print(manager.get_stats_summary())


def demonstrate_permission_workflow(manager: AdvancedStreamingManager):
    """Demonstrate permission handling workflow"""
    print("\n" + "="*60)
    print("PERMISSION WORKFLOW DEMONSTRATION")
    print("="*60)

    # Setup permission handling
    def on_permission_request(permission: PermissionRequest):
        print(f"\n🔐 PERMISSION REQUESTED:")
        print(f"  Tool: {permission.tool_name}")
        print(f"  Action: {permission.action}")
        print(f"  Description: {permission.description}")
        print(f"  Path: {permission.path}")

        # Auto-grant permissions for demo (in real app, user would decide)
        time.sleep(1)  # Brief pause for demonstration
        print(f"  AUTO-GRANTING permission {permission.id}")
        manager.grant_permission(permission.id)

    manager.on_permission_request = on_permission_request

    # Send a message that might require permissions
    message = """
    Please create a simple test file called 'streaming_test.txt' with some sample content,
    then read it back and show me the contents. This might require file system permissions.
    """

    success = manager.send_message(message.strip())
    if not success:
        print("Failed to send message")
        return

    # Monitor for completion
    timeout = 60
    start_time = time.time()
    while not manager.completed and time.time() - start_time < timeout:
        if manager.state == StreamingState.ERROR:
            print(f"\nError occurred: {manager.error}")
            break
        time.sleep(1)

    print("\n" + manager.get_timeline_summary())
    print(manager.get_stats_summary())


def demonstrate_cancellation_workflow(manager: AdvancedStreamingManager):
    """Demonstrate message cancellation"""
    print("\n" + "="*60)
    print("CANCELLATION WORKFLOW DEMONSTRATION")
    print("="*60)

    # Send a message that will take some time to process
    message = """
    Please write a comprehensive analysis of different software architectural patterns,
    including detailed comparisons between microservices, monolithic, and serverless architectures.
    Make it very detailed with examples and use cases for each pattern.
    This should be a long response that we can cancel partway through.
    """

    success = manager.send_message(message.strip())
    if not success:
        print("Failed to send message")
        return

    # Let it process for a bit, then cancel
    print("Letting message process for 10 seconds, then cancelling...")
    time.sleep(10)

    if manager.is_processing:
        print("Cancelling message...")
        cancel_success = manager.cancel_message()

        if cancel_success:
            print("Message cancelled successfully")
            print(f"Partial content received: {len(manager.final_content)} characters")
            if manager.final_content:
                preview = manager.final_content[:200] + ("..." if len(manager.final_content) > 200 else "")
                print(f"Content preview: {preview}")
        else:
            print("Failed to cancel message")
    else:
        print("Message completed before cancellation")

    print("\n" + manager.get_timeline_summary())
    print(manager.get_stats_summary())


def main():
    """Main function demonstrating advanced Mix SDK streaming functionality"""
    load_dotenv()

    api_key = os.getenv("OPENROUTER_API_KEY")
    if not api_key:
        raise ValueError("OPENROUTER_API_KEY not found in environment variables. Please add it to your .env file.")

    server_url = os.getenv("MIX_SERVER_URL", "http://localhost:8088")

    print("="*60)
    print("MIX PYTHON SDK - ADVANCED STREAMING EXAMPLE")
    print("="*60)
    print(f"Server URL: {server_url}")
    print("This example demonstrates advanced streaming functionality with:")
    print("- Persistent state management")
    print("- Timeline tracking")
    print("- Tool execution monitoring")
    print("- Permission handling")
    print("- Cancellation support")
    print("="*60)

    with Mix(server_url=server_url) as mix:
        # System health check
        health = mix.system.get_health()
        print(f"System health: {health}")

        # Store API key
        print("\nStoring OpenRouter API key...")
        auth_response = mix.authentication.store_api_key(api_key=api_key, provider="openrouter")
        print(f"Authentication stored: {auth_response}")

        # Check preferences
        print("\nChecking preferences...")
        preferences = mix.preferences.get_preferences()
        print(f"Current preferences: {preferences}")

        # Create session for advanced streaming
        print("\nCreating session for advanced streaming demo...")
        session = mix.sessions.create(title="Advanced Streaming Demo Session")
        print(f"Created session: {session.id}")

        # Create advanced streaming manager
        manager = AdvancedStreamingManager(mix, session.id)

        try:
            # Run demonstrations
            demonstrate_basic_streaming(manager)

            # # Reset for next demo
            # manager.stop_streaming()
            # time.sleep(2)

            # demonstrate_tool_execution_monitoring(manager)

            # # Reset for next demo
            # manager.stop_streaming()
            # time.sleep(2)

            # demonstrate_permission_workflow(manager)

            # # Reset for next demo
            # manager.stop_streaming()
            # time.sleep(2)

            # demonstrate_cancellation_workflow(manager)

        finally:
            # Cleanup
            manager.stop_streaming()
            print(f"\nCleaning up session: {session.id}")
            mix.sessions.delete(id=session.id)
            print("Session deleted successfully")

            print("\nAdvanced streaming demonstration completed!")


if __name__ == "__main__":
    main()