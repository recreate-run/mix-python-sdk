#!/usr/bin/env python3
"""
Streaming Minimal Example for Mix Python SDK

Documentation Reference: docs/sdks/streaming/README.md

This example demonstrates minimal streaming functionality including:
- Server-Sent Events (SSE) connection establishment for real-time updates
- Message sending via streaming pipeline with real-time event broadcasting
- Basic event stream processing and response handling
- Persistent streaming connections with proper response capture

Run this example to see essential streaming methods in action.
"""

from mix_python_sdk import Mix
from mix_python_sdk.models import MessageData
import os
from dotenv import load_dotenv
import json


def demonstrate_basic_sse_connection(mix, session_id):
    """Demonstrate basic Server-Sent Events connection establishment"""
    print("\n=== Basic SSE Connection Demo ===")

    print("1. Establishing SSE connection for real-time updates...")
    stream_response = mix.streaming.stream_events(session_id=session_id)
    print(f"Stream response: {stream_response}")

    if hasattr(stream_response, '__dict__'):
        print("\nSSE Connection details:")
        for key, value in stream_response.__dict__.items():
            print(f"  {key}: {value}")

    return stream_response


def demonstrate_basic_streaming_message(mix, session_id):
    """Demonstrate basic message sending via streaming pipeline"""
    print("\n=== Basic Streaming Message Demo ===")

    print("1. Setting up SSE connection to capture response...")
    stream_response = mix.streaming.stream_events(session_id=session_id)

    # Give SSE connection time to establish
    import time
    time.sleep(2)
    print("SSE connection established, ready to send message...")

    print("2. Sending message via streaming pipeline...")
    message_text = "Hello! Please explain what you are and what you can do in 20 words . think about your capabilities."
    print(f"Sending message: '{message_text}'")

    # Use proper MessageData model from SDK
    message_data = MessageData(
        text=message_text,
        media=[],
        apps=[],
        plan_mode=False
    )
    message_content = json.dumps(message_data.model_dump())

    message_response = mix.streaming.send_streaming_message(
        id=session_id,
        content=message_content
    )

    print(f"Message response: {message_response}")

    if hasattr(message_response, '__dict__'):
        print("\nMessage response details:")
        for key, value in message_response.__dict__.items():
            print(f"  {key}: {value}")

    print("3. Processing SSE events for response...")
    response_content = []
    thinking_content = []
    tool_calls = []

    with stream_response.result as event_stream:
        for event in event_stream:
            print(f"Event: {event.event}")

            if event.event == "connected":
                print("✅ SSE connection established")

            elif event.event == "heartbeat":
                print("💓 Heartbeat - connection alive")

            elif event.event == "thinking" and hasattr(event, 'data') and hasattr(event.data, 'content'):
                thinking_chunk = event.data.content
                if thinking_chunk:
                    thinking_content.append(thinking_chunk)
                    print(f"🤔 Thinking: {thinking_chunk[:100]}...")

            elif event.event == "content" and hasattr(event, 'data') and hasattr(event.data, 'content'):
                content_chunk = event.data.content
                if content_chunk:
                    response_content.append(content_chunk)
                    print(f"📝 Content chunk: {content_chunk}")

            elif event.event == "tool" and hasattr(event, 'data'):
                tool_data = event.data
                tool_info = {
                    'id': getattr(tool_data, 'id', 'unknown'),
                    'name': getattr(tool_data, 'name', 'unknown'),
                    'status': getattr(tool_data, 'status', 'unknown'),
                    'input': getattr(tool_data, 'input', None)
                }
                tool_calls.append(tool_info)
                print(f"🔧 Tool: {tool_info['name']} - {tool_info['status']}")
                if tool_info['input']:
                    print(f"   Input: {str(tool_info['input'])[:100]}...")

            elif event.event == "tool_execution_start" and hasattr(event, 'data'):
                tool_id = getattr(event.data, 'toolCallId', 'unknown')
                progress = getattr(event.data, 'progress', '')
                print(f"🚀 Tool execution started: {tool_id}")
                if progress:
                    print(f"   Progress: {progress}")

            elif event.event == "tool_execution_complete" and hasattr(event, 'data'):
                tool_id = getattr(event.data, 'toolCallId', 'unknown')
                success = getattr(event.data, 'success', False)
                progress = getattr(event.data, 'progress', '')
                status = "✅ Success" if success else "❌ Failed"
                print(f"{status} Tool execution completed: {tool_id}")
                if progress:
                    print(f"   Result: {progress[:100]}...")

            elif event.event == "error" and hasattr(event, 'data'):
                error_msg = getattr(event.data, 'error', 'Unknown error')
                print(f"❌ Error: {error_msg}")

            elif event.event == "permission" and hasattr(event, 'data'):
                perm_data = event.data
                tool_name = getattr(perm_data, 'toolName', 'unknown')
                description = getattr(perm_data, 'description', '')
                print(f"🔐 Permission requested for: {tool_name}")
                if description:
                    print(f"   Description: {description}")

            elif event.event == "complete":
                print("✅ Message processing completed!")

                # Show final reasoning if available
                if hasattr(event, 'data'):
                    reasoning = getattr(event.data, 'reasoning', None)
                    reasoning_duration = getattr(event.data, 'reasoningDuration', None)
                    if reasoning:
                        print(f"🧠 Final reasoning: {reasoning[:200]}...")
                    if reasoning_duration:
                        print(f"⏱️  Reasoning duration: {reasoning_duration}ms")
                break

            else:
                # Log any unhandled event types
                print(f"❓ Unhandled event type: {event.event}")

    # Print comprehensive results
    print(f"\n=== STREAMING SESSION SUMMARY ===")

    if thinking_content:
        complete_thinking = ''.join(thinking_content)
        print(f"🤔 Agent Thinking Process:")
        print(f"   {complete_thinking[:300]}...")

    if tool_calls:
        print(f"🔧 Tool Calls ({len(tool_calls)} total):")
        for tool in tool_calls:
            print(f"   - {tool['name']} ({tool['status']})")

    if response_content:
        complete_response = ''.join(response_content)
        print(f"📝 Complete Agent Response:")
        print(f"   {complete_response}")
    else:
        print("❌ No content received from stream")

    return message_response




def main():
    """Main function demonstrating Mix SDK streaming functionality"""
    # Load environment variables from .env file
    load_dotenv()

    # Get required API key from environment
    api_key = os.getenv("OPENROUTER_API_KEY")
    if not api_key:
        raise ValueError("OPENROUTER_API_KEY not found in environment variables. Please add it to your .env file.")

    server_url = os.getenv("MIX_SERVER_URL", "http://localhost:8088")

    print("="*60)
    print("MIX PYTHON SDK - STREAMING MINIMAL EXAMPLE")
    print("="*60)
    print(f"Server URL: {server_url}")
    print("This example demonstrates minimal streaming functionality")
    print("Using real OpenRouter API key from .env file")
    print("="*60)

    with Mix(server_url=server_url) as mix:
        # Always start with system health check
        health = mix.system.get_health()
        print(f"System health: {health}")

        # Store API key for OpenRouter
        print("\nStoring OpenRouter API key...")
        auth_response = mix.authentication.store_api_key(api_key=api_key, provider="openrouter")
        print(f"Authentication stored: {auth_response}")

        # Create a session for streaming
        print("\nCreating session for streaming demo...")
        session = mix.sessions.create(title="Streaming Minimal Demo")
        print(f"Created session: {session.id}")

        # Call each demonstration function in logical order
        demonstrate_basic_sse_connection(mix, session.id)
        demonstrate_basic_streaming_message(mix, session.id)

        # Clean up
        print(f"\nCleaning up session: {session.id}")
        mix.sessions.delete(id=session.id)
        print("Session deleted successfully")


if __name__ == "__main__":
    main()