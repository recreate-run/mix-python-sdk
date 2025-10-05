#!/usr/bin/env python3
"""Minimal streaming example using high-level helper functions."""

import asyncio
import os
from dotenv import load_dotenv
from mix_python_sdk import Mix
from mix_python_sdk.helpers import send_with_callbacks


async def main():
    load_dotenv()

    async with Mix(server_url=os.getenv("MIX_SERVER_URL")) as mix:
        mix.authentication.store_api_key(
            api_key=os.getenv("OPENROUTER_API_KEY"), provider="openrouter"
        )

        session = mix.sessions.create(title="Streaming Demo")

        await send_with_callbacks(
            mix,
            session_id=session.id,
            message="write a detailed 50 word essay about the history of cats",
            on_thinking=lambda text: print(text, end="", flush=True),
            on_content=lambda text: print(text, end="", flush=True),
            on_tool=lambda tool: print(f"\n🔧 {tool.name}: {tool.status}"),
            on_error=lambda error: print(f"\n❌ {error}"),
        )


if __name__ == "__main__":
    asyncio.run(main())
