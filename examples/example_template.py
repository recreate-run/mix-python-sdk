#!/usr/bin/env python3
"""Minimal streaming example demonstrating SSE connection, message sending, and event processing."""

import asyncio
import os
from dotenv import load_dotenv
from mix_python_sdk import Mix
from mix_python_sdk.models import (
    SSEThinkingEvent,
    SSEContentEvent,
    SSEToolEvent,
    SSEErrorEvent,
    SSECompleteEvent,
)


async def main():
    load_dotenv()

    async with Mix(server_url=os.getenv("MIX_SERVER_URL")) as mix:
        mix.authentication.store_api_key(
            api_key=os.getenv("OPENROUTER_API_KEY"), provider="openrouter"
        )

        session = mix.sessions.create(title="Streaming Demo")
        stream_response = await mix.streaming.stream_events_async(session_id=session.id)
        await asyncio.sleep(0.5)

        async with stream_response.result as event_stream:

            async def process_events():
                async for event in event_stream:
                    if isinstance(event, SSEThinkingEvent):
                        print(event.data.content, end="", flush=True)
                    elif isinstance(event, SSEContentEvent):
                        print(event.data.content, end="", flush=True)
                    elif isinstance(event, SSEToolEvent):
                        print(f"\n🔧 {event.data.name}: {event.data.status}")
                    elif isinstance(event, SSEErrorEvent):
                        print(f"\n❌ {event.data.error}")
                        break
                    elif isinstance(event, SSECompleteEvent):
                        break

            await asyncio.gather(
                mix.messages.send_async(
                    id=session.id,
                    text="write a detailed 50 word essay about the history of cats",
                ),
                process_events(),
            )


if __name__ == "__main__":
    asyncio.run(main())
