#!/usr/bin/env python3
"""
Streaming Example for Mix Python SDK

Documentation Reference: docs/sdks/streaming/README.md

This example demonstrates comprehensive streaming functionality including:
- Server-Sent Events (SSE) connection establishment for real-time updates
- Persistent streaming connections with proper reconnection support
- Message sending via streaming pipeline with real-time event broadcasting
- Event stream processing and handling during message processing
- Last-Event-ID header support for reconnection and event replay
- Integration with active SSE connections for real-time processing events

Run this example to see all streaming methods in action.
"""

from mix_python_sdk import Mix
import os
from dotenv import load_dotenv
import time
import threading


def demonstrate_sse_connection(mix, session_id):
    """Demonstrate Server-Sent Events connection establishment"""
    print("\n=== SSE Connection Demo ===")

    print("1. Establishing SSE connection for real-time updates...")
    stream_response = mix.streaming.stream_events(session_id=session_id)
    print(f"Stream response: {stream_response}")

    if hasattr(stream_response, '__dict__'):
        print("\nSSE Connection details:")
        for key, value in stream_response.__dict__.items():
            print(f"  {key}: {value}")

    return stream_response


def demonstrate_streaming_message(mix, session_id):
    """Demonstrate message sending via streaming pipeline with real-time SSE capture"""
    print("\n=== Streaming Message Demo ===")

    print("1. Establishing SSE connection to capture real-time response...")
    stream_response = mix.streaming.stream_events(session_id=session_id)

    # Start SSE processing in background thread
    full_response_content = []
    agent_reasoning = []
    response_complete = False

    def capture_sse_events():
        nonlocal full_response_content, agent_reasoning, response_complete

        print("SSE: Listening for real-time events...")
        with stream_response.result as event_stream:
            for event in event_stream:
                print(f"SSE Event: {event.event}")

                if event.event == "connected":
                    print("SSE: Connection established")

                elif event.event == "thinking" and hasattr(event, 'data') and hasattr(event.data, 'content'):
                    reasoning_content = event.data.content
                    if reasoning_content:
                        agent_reasoning.append(reasoning_content)
                        print(f"SSE Thinking: {reasoning_content[:100]}...")

                elif event.event == "content" and hasattr(event, 'data') and hasattr(event.data, 'content'):
                    content_chunk = event.data.content
                    if content_chunk:
                        full_response_content.append(content_chunk)
                        print(f"SSE Content: {content_chunk}")

                elif event.event == "complete":
                    print("SSE: Message processing completed!")
                    response_complete = True
                    break

    # Start SSE capture in background
    sse_thread = threading.Thread(target=capture_sse_events)
    sse_thread.start()

    # Give SSE connection time to establish
    time.sleep(1)

    print("\n2. Sending message via streaming pipeline...")
    message_content = "Hello, streaming! Please explain how SSE works in simple terms."
    print(f"Sending message: '{message_content}'")

    message_response = mix.streaming.send_streaming_message(
        id=session_id,
        content=message_content
    )

    print(f"Message response: {message_response}")

    # Wait for SSE processing to complete
    print("\n3. Waiting for complete agent response via SSE...")
    sse_thread.join(timeout=60)  # Increased timeout for AI processing

    # Display captured response
    print("\n=== CAPTURED AGENT RESPONSE ===")

    if agent_reasoning:
        print("Agent Reasoning:")
        for reasoning in agent_reasoning:
            print(f"  {reasoning}")

    if full_response_content:
        print("\nAgent Response:")
        complete_response = ''.join(full_response_content)
        print(f"  {complete_response}")
    else:
        print("No content captured from SSE stream")

    print(f"Response Complete: {response_complete}")

    return message_response

def demonstrate_integrated_streaming_workflow(mix, session_id):
    """Demonstrate integrated streaming workflow with simultaneous SSE and messaging"""
    print("\n=== Integrated Streaming Workflow Demo ===")

    print("1. Setting up concurrent SSE connection and message sending...")

    # Start SSE connection in background
    def process_events():
        print("Background: Establishing SSE connection...")
        stream_response = mix.streaming.stream_events(session_id=session_id)

        print("Background: Processing events...")
        with stream_response.result as event_stream:
            for event in event_stream:
                print(f"Background Event: {event.event}")
                if event.event == "content" and hasattr(event, 'data') and hasattr(event.data, 'content'):
                    content = event.data.content
                    if content:
                        print(f"Background Content: {content[:50]}..." if len(str(content)) > 50 else f"Background Content: {content}")
                elif event.event == "complete":
                    print("Background: Message processing completed!")
                    break

    # Start event processing in background thread
    event_thread = threading.Thread(target=process_events)
    event_thread.start()

    # Give SSE connection time to establish
    time.sleep(1)

    print("2. Sending message via streaming pipeline...")
    message_response = mix.streaming.send_streaming_message(
        id=session_id,
        content="Explain the benefits of Server-Sent Events over traditional polling. Keep it concise."
    )

    print(f"Message sent successfully: {getattr(message_response, 'session_id', getattr(message_response, 'id', 'Unknown ID'))}")

    # Wait for event processing to complete
    event_thread.join(timeout=30)

    print("3. Integrated workflow completed!")


def main():
    """Main function demonstrating Mix SDK streaming functionality"""
    load_dotenv()

    api_key = os.getenv("OPENROUTER_API_KEY")
    if not api_key:
        raise ValueError("OPENROUTER_API_KEY not found in environment variables. Please add it to your .env file.")

    server_url = os.getenv("MIX_SERVER_URL", "http://localhost:8088")

    print("="*60)
    print("MIX PYTHON SDK - STREAMING EXAMPLE")
    print("="*60)
    print(f"Server URL: {server_url}")
    print("This example demonstrates all streaming functionality")
    print("Using real OpenRouter API key from .env file")
    print("="*60)

    with Mix(server_url=server_url) as mix:
        health = mix.system.get_health()
        print(f"System health: {health}")

        # Store API key for OpenRouter
        print("\nStoring OpenRouter API key...")
        auth_response = mix.authentication.store_api_key(api_key=api_key, provider="openrouter")
        print(f"Authentication stored: {auth_response}")

        # Check preferences to ensure AI processing is configured
        print("\nChecking preferences...")
        preferences = mix.preferences.get_preferences()
        print(f"Current preferences: {preferences}")

        # Create a session for streaming
        print("\nCreating session for streaming demo...")
        session = mix.sessions.create(title="Streaming Demo Session")
        print(f"Created session: {session.id}")

        # Demonstrate all streaming functionality
        # demonstrate_sse_connection(mix, session.id)
        # demonstrate_streaming_message(mix, session.id)
        demonstrate_integrated_streaming_workflow(mix, session.id)

        # Clean up
        print(f"\nCleaning up session: {session.id}")
        mix.sessions.delete(id=session.id)
        print("Session deleted successfully")


if __name__ == "__main__":
    main()