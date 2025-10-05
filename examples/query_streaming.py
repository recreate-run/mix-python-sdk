#!/usr/bin/env python3
"""Streaming example using query() async iterator.

This example shows the query() pattern which is similar to Claude SDK's
simple async iteration pattern.
"""

import asyncio
import os
from dotenv import load_dotenv
from mix_python_sdk import Mix
from mix_python_sdk.helpers import query


async def main():
    load_dotenv()
    api_key = os.getenv("OPENROUTER_API_KEY")
    if not api_key:
        raise ValueError("OPENROUTER_API_KEY not found in environment variables")

    async with Mix(server_url=os.getenv("MIX_SERVER_URL", "http://localhost:8088")) as mix:
        mix.authentication.store_api_key(api_key=api_key, provider="openrouter")
        session = mix.sessions.create(title="Query Streaming Demo")

        # Simple async iteration over events
        async for event in query(mix, session.id, "What's 2+2?"):
            if event.type == "thinking":
                print(f"🤔 Thinking: {event.thinking}", end="", flush=True)
            elif event.type == "content":
                print(f"\n💬 Response: {event.content}", end="", flush=True)
            elif event.type == "tool":
                print(f"\n🔧 Tool: {event.tool_name}")
            elif event.type == "complete":
                print("\n✅ Complete!")

        mix.sessions.delete(id=session.id)


if __name__ == "__main__":
    asyncio.run(main())
