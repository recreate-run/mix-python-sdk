#!/usr/bin/env python3
"""Comprehensive streaming example using high-level helper functions.

This example shows all available streaming event types and how to handle them
using the callback-based send_with_callbacks helper function.
"""

import asyncio
import os
from dotenv import load_dotenv
from mix_python_sdk import Mix
from mix_python_sdk.helpers import send_with_callbacks


async def stream_message(mix, session_id: str, message: str) -> None:
    """Send message via streaming and process events with callbacks."""
    thinking_started = content_started = False

    def handle_thinking(text: str):
        nonlocal thinking_started
        if not thinking_started:
            print("🤔 Thinking: ", end="", flush=True)
            thinking_started = True
        print(text, end="", flush=True)

    def handle_content(text: str):
        nonlocal content_started, thinking_started
        if not content_started:
            if thinking_started:
                print("\n📝 Response: ", end="", flush=True)
            else:
                print("📝 Response: ", end="", flush=True)
            content_started = True
        print(text, end="", flush=True)

    def handle_tool(tool):
        print(f"\n🔧 Tool: {tool.name} - {tool.status}")
        if hasattr(tool, "input") and tool.input:
            print(f"   Parameters: {tool.input}")

    def handle_tool_execution_start(data):
        if hasattr(data, "progress") and data.progress:
            print(f"   Progress: {data.progress}")

    def handle_tool_execution_complete(data):
        if hasattr(data, "progress") and data.progress:
            if hasattr(data, "success") and data.success:
                print(f"📄 Result:\n{data.progress}")
            else:
                print(f"❌ Error:\n{data.progress}")

    def handle_permission(data):
        print(f"\n🔐 Permission: {data.tool_name}")

    def handle_complete():
        nonlocal content_started
        if content_started:
            print("\n")
        print("✅ Complete!")

    await send_with_callbacks(
        mix,
        session_id=session_id,
        message=message,
        on_thinking=handle_thinking,
        on_content=handle_content,
        on_tool=handle_tool,
        on_tool_execution_start=handle_tool_execution_start,
        on_tool_execution_complete=handle_tool_execution_complete,
        on_error=lambda error: print(f"\n❌ Error: {error}"),
        on_permission=handle_permission,
        on_complete=handle_complete,
    )


async def main():
    load_dotenv()
    api_key = os.getenv("OPENROUTER_API_KEY")
    if not api_key:
        raise ValueError("OPENROUTER_API_KEY not found in environment variables")

    user_msg = "what's your working dir?"

    async with Mix(
        server_url=os.getenv("MIX_SERVER_URL", "http://localhost:8088")
    ) as mix:
        mix.system.get_health()
        mix.authentication.store_api_key(api_key=api_key, provider="openrouter")
        session = mix.sessions.create(title="Streaming Demo")
        await stream_message(mix, session.id, user_msg)
        mix.sessions.delete(id=session.id)


if __name__ == "__main__":
    asyncio.run(main())
