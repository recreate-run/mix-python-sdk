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
from mix_python_sdk.models import SendMessageRequestBody
import os
from dotenv import load_dotenv
import json


def demonstrate_basic_sse_connection(mix, session_id):
    """Demonstrate basic Server-Sent Events connection establishment"""
    print("\n=== Basic SSE Connection Demo ===")

    print("1. Establishing SSE connection for real-time updates...")
    stream_response = mix.streaming.stream_events(session_id=session_id)
    print(f"Stream response: {stream_response}")

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

    message_data = SendMessageRequestBody(
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

            elif event.event == "thinking":
                thinking_chunk = event.data.content
                thinking_content.append(thinking_chunk)
                print(f"🤔 Thinking: {thinking_chunk[:100]}...")

            elif event.event == "content":
                content_chunk = event.data.content
                response_content.append(content_chunk)
                print(f"📝 Content chunk: {content_chunk}")

            elif event.event == "tool":
                tool_data = event.data
                tool_info = {
                    'id': tool_data.id,
                    'name': tool_data.name,
                    'status': tool_data.status,
                    'input': tool_data.input
                }
                tool_calls.append(tool_info)
                print(f"🔧 Tool: {tool_info['name']} - {tool_info['status']}")
                print(f"   Input: {str(tool_info['input'])[:100]}...")

            elif event.event == "tool_execution_start":
                tool_id = event.data.toolCallId
                progress = event.data.progress
                print(f"🚀 Tool execution started: {tool_id}")
                print(f"   Progress: {progress}")

            elif event.event == "tool_execution_complete":
                tool_id = event.data.toolCallId
                success = event.data.success
                progress = event.data.progress
                status = "✅ Success" if success else "❌ Failed"
                print(f"{status} Tool execution completed: {tool_id}")
                print(f"   Result: {progress[:100]}...")

            elif event.event == "error":
                error_msg = event.data.error
                print(f"❌ Error: {error_msg}")

            elif event.event == "permission":
                perm_data = event.data
                tool_name = perm_data.toolName
                description = perm_data.description
                print(f"🔐 Permission requested for: {tool_name}")
                print(f"   Description: {description}")

            elif event.event == "complete":
                print("✅ Message processing completed!")

                # Show final reasoning
                reasoning = event.data.reasoning
                reasoning_duration = event.data.reasoning_duration
                print(f"🧠 Final reasoning: {reasoning[:200]}...")
                print(f"⏱️  Reasoning duration: {reasoning_duration}ms")
                break

            else:
                # Log any unhandled event types
                print(f"❓ Unhandled event type: {event.event}")

    # Print comprehensive results
    print(f"\n=== STREAMING SESSION SUMMARY ===")

    complete_thinking = ''.join(thinking_content)
    print(f"🤔 Agent Thinking Process:")
    print(f"   {complete_thinking[:300]}...")

    print(f"🔧 Tool Calls ({len(tool_calls)} total):")
    for tool in tool_calls:
        print(f"   - {tool['name']} ({tool['status']})")

    complete_response = ''.join(response_content)
    print(f"📝 Complete Agent Response:")
    print(f"   {complete_response}")

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