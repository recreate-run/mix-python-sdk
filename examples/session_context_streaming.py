#!/usr/bin/env python3
"""Streaming example using StreamingSession context manager.

This example shows the most convenient pattern for working with sessions
by automatically handling session creation and cleanup.
"""

import asyncio
import os
from dotenv import load_dotenv
from mix_python_sdk import Mix
from mix_python_sdk.helpers import StreamingSession


async def main():
    load_dotenv()
    api_key = os.getenv("OPENROUTER_API_KEY")
    if not api_key:
        raise ValueError("OPENROUTER_API_KEY not found in environment variables")

    async with Mix(server_url=os.getenv("MIX_SERVER_URL", "http://localhost:8088")) as mix:
        mix.authentication.store_api_key(api_key=api_key, provider="openrouter")

        # Session is automatically created and cleaned up
        async with StreamingSession(mix, title="Context Manager Demo") as session:
            print(f"Session ID: {session.id}\n")

            # First message using callbacks
            await session.send(
                "What's the capital of France?",
                on_content=lambda text: print(text, end="", flush=True),
                on_complete=lambda: print("\n"),
            )

            # Second message using query iterator
            print("\n---\n")
            async for event in session.query("And what about Italy?"):
                if event.type == "content":
                    print(event.content, end="", flush=True)
                elif event.type == "complete":
                    print("\n")


if __name__ == "__main__":
    asyncio.run(main())
