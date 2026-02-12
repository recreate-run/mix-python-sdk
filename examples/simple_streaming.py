#!/usr/bin/env python3
"""Simple streaming example using high-level helper functions.

This example demonstrates the easiest way to use Mix streaming with
callback-based event handling.
"""

import asyncio
import os
from dotenv import load_dotenv
from mix_python_sdk import Mix
from mix_python_sdk.helpers import send_with_callbacks


async def main():
    load_dotenv()
    api_key = os.getenv("OPENROUTER_API_KEY")
    if not api_key:
        raise ValueError("OPENROUTER_API_KEY not found in environment variables")

    async with Mix(
        server_url=os.getenv("MIX_SERVER_URL", "http://localhost:8088")
    ) as mix:
        mix.authentication.store_api_key(api_key=api_key, provider="openrouter")
        session = mix.sessions.create(
            title="Simple Streaming Demo",
            browser_mode="local-browser-service"
        )

        # Simple callback-based streaming - just 10 lines instead of 50!
        await send_with_callbacks(
            mix,
            session_id=session.id,
            message="What's your working directory?",
            on_thinking=lambda text: print(f"🤔 {text}", end="", flush=True),
            on_content=lambda text: print(f"\n💬 {text}", end="", flush=True),
            on_tool_execution_start=lambda tool: print(f"\n🔧 Tool execution started: {tool}"),
            on_complete=lambda: print("\n✅ Complete!"),
        )

        mix.sessions.delete(id=session.id)


if __name__ == "__main__":
    asyncio.run(main())
