#!/usr/bin/env python3
"""Shared utilities for Mix Python SDK examples."""

import threading
import time
from mix_python_sdk.models import (
    SSEThinkingEvent,
    SSEContentEvent,
    SSEToolEvent,
    SSEErrorEvent,
    SSEEventStream,
    SSECompleteEvent,
)


def stream_message(mix, session_id: str, message: str) -> None:
    """Send message and process SSE events using CQRS pattern.

    Write path: REST API (POST /api/sessions/{id}/messages)
    Read path: SSE (GET /stream?sessionId={id})
    """
    stream_response = mix.streaming.stream_events(session_id=session_id)
    time.sleep(0.5)  # Allow SSE connection to establish

    # Send message in separate thread to avoid blocking SSE event processing
    send_thread = threading.Thread(
        target=lambda: mix.messages.send(id=session_id, text=message),
        daemon=True
    )
    send_thread.start()

    thinking_started = content_started = False

    try:
        with stream_response.result as event_stream:
            event: SSEEventStream
            for event in event_stream:
                if isinstance(event, SSEThinkingEvent):
                    if not thinking_started:
                        print("🤔 Thinking: ", end="", flush=True)
                        thinking_started = True
                    print(event.data.content, end="", flush=True)
                elif isinstance(event, SSEContentEvent):
                    if not content_started:
                        if thinking_started:
                            print("\n📝 Response: ", end="", flush=True)
                        else:
                            print("📝 Response: ", end="", flush=True)
                        content_started = True
                    print(event.data.content, end="", flush=True)
                elif isinstance(event, SSEToolEvent):
                    print(f"\n🔧 Tool: {event.data.name} - {event.data.status}")
                    if event.data.input:
                        print(f"   Parameters: {event.data.input}")
                elif isinstance(event, SSEErrorEvent):
                    print(f"\n❌ Error: {event.data.error}")
                    break
                elif isinstance(event, SSECompleteEvent):
                    break
    finally:
        # Give send thread a moment to complete
        send_thread.join(timeout=1.0)