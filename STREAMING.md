# Streaming Guide

The Mix Python SDK provides high-level helper functions that make streaming interactions simple and ergonomic. This guide explains the three patterns available and when to use each.

## Quick Start (Recommended)

For most use cases, use the **callback-based** `send_with_callbacks()` function:

```python
import asyncio
from mix_python_sdk import Mix
from mix_python_sdk.helpers import send_with_callbacks

async def main():
    async with Mix(server_url="http://localhost:8088") as mix:
        session = mix.sessions.create(title="Demo")

        await send_with_callbacks(
            mix,
            session_id=session.id,
            message="What's the weather like?",
            on_content=lambda text: print(text, end="", flush=True),
            on_complete=lambda: print("\nDone!")
        )

asyncio.run(main())
```

## The Three Patterns

### 1. `send_with_callbacks()` - Callback-based ⭐ RECOMMENDED

**Use this 90% of the time** - simplest and most ergonomic.

```python
await send_with_callbacks(
    mix,
    session_id=session.id,
    message="Tell me a joke",
    on_thinking=lambda text: print(f"🤔 {text}", end="", flush=True),
    on_content=lambda text: print(f"💬 {text}", end="", flush=True),
    on_tool=lambda tool: print(f"\n🔧 Using {tool.name}"),
    on_error=lambda error: print(f"\n❌ {error}"),
    on_complete=lambda: print("\n✅ Done!")
)
```

**Available callbacks:**

- `on_thinking` - Called when AI is thinking (receives text)
- `on_content` - Called for response content (receives text)
- `on_tool` - Called when a tool is used (receives tool data)
- `on_tool_execution_start` - Called when tool execution starts
- `on_tool_execution_complete` - Called when tool execution completes
- `on_error` - Called on errors (receives error message)
- `on_permission` - Called when permission is requested
- `on_complete` - Called when streaming completes

**Pros:**

- ✅ Simplest API
- ✅ All complexity hidden
- ✅ Just provide callbacks for events you care about

**Cons:**

- ❌ Can't control event flow (can't skip/stop conditionally)

---

### 2. `query()` - Async Iterator

Use when you need **more control** over event processing.

```python
from mix_python_sdk import Mix
from mix_python_sdk.helpers import query

async for event in query(mix, session.id, "Hello!"):
    if event.type == "content":
        print(event.content, end="", flush=True)

    elif event.type == "thinking":
        print(f"[Thinking: {event.thinking}]")

    elif event.type == "tool":
        print(f"\nTool: {event.tool_name}")
        if some_condition:
            break  # Can stop processing early!
```

**Event types:**

- `"thinking"` - AI thinking
- `"content"` - Response content
- `"tool"` - Tool usage
- `"tool_execution_start"` - Tool execution started
- `"tool_execution_complete"` - Tool execution completed
- `"error"` - Error occurred
- `"permission"` - Permission requested
- `"complete"` - Stream completed

**Event properties:**

- `event.type` - Event type string
- `event.data` - Raw event data
- `event.content` - Content text (if type is "content")
- `event.thinking` - Thinking text (if type is "thinking")
- `event.tool_name` - Tool name (if type is "tool")

**Pros:**

- ✅ Can control loop flow (break, continue)
- ✅ Can inspect events before processing
- ✅ Familiar Python pattern

**Cons:**

- ❌ More verbose than callbacks
- ❌ Must manually check event types

---

### 3. `StreamingSession` - Context Manager

Use when you need **automatic session lifecycle management**.

```python
from mix_python_sdk import Mix
from mix_python_sdk.helpers import StreamingSession

async with Mix(server_url="http://localhost:8088") as mix:
    mix.authentication.store_api_key(api_key=api_key, provider="openrouter")

    # Session created automatically
    async with StreamingSession(mix, title="Chat") as session:
        # Send multiple messages to same session
        await session.send(
            "Hello!",
            on_content=lambda t: print(t, end="", flush=True)
        )

        await session.send(
            "Tell me more",
            on_content=lambda t: print(t, end="", flush=True)
        )

        # Can also use query pattern
        async for event in session.query("Goodbye!"):
            if event.type == "content":
                print(event.content, end="", flush=True)

    # Session deleted automatically on exit
```

**Pros:**

- ✅ Automatic session creation/cleanup
- ✅ Multiple messages to same session
- ✅ Clean resource management

**Cons:**

- ❌ More overhead for single messages

---

## Complete Example: All Event Types

Here's a comprehensive example showing all available callbacks:

```python
import asyncio
from mix_python_sdk import Mix
from mix_python_sdk.helpers import send_with_callbacks

async def main():
    async with Mix(server_url="http://localhost:8088") as mix:
        mix.authentication.store_api_key(api_key="your-key", provider="openrouter")
        session = mix.sessions.create(title="Demo")

        thinking_started = False
        content_started = False

        def handle_thinking(text: str):
            nonlocal thinking_started
            if not thinking_started:
                print("🤔 Thinking: ", end="", flush=True)
                thinking_started = True
            print(text, end="", flush=True)

        def handle_content(text: str):
            nonlocal content_started
            if not content_started:
                print("\n💬 Response: ", end="", flush=True)
                content_started = True
            print(text, end="", flush=True)

        def handle_tool(tool):
            print(f"\n🔧 Tool: {tool.name} - {tool.status}")
            if hasattr(tool, "input") and tool.input:
                print(f"   Input: {tool.input}")

        def handle_error(error):
            print(f"\n❌ Error: {error}")

        def handle_complete():
            print("\n✅ Complete!")

        await send_with_callbacks(
            mix,
            session_id=session.id,
            message="What's your working directory?",
            on_thinking=handle_thinking,
            on_content=handle_content,
            on_tool=handle_tool,
            on_error=handle_error,
            on_complete=handle_complete,
        )

        mix.sessions.delete(id=session.id)

asyncio.run(main())
```

## When to Use Each Pattern

| Use Case | Recommended Pattern |
|----------|-------------------|
| Simple chat bot | `send_with_callbacks()` |
| Display streaming responses | `send_with_callbacks()` |
| Need to stop on condition | `query()` |
| Need event inspection | `query()` |
| Multi-turn conversation | `StreamingSession` |
| Auto session cleanup | `StreamingSession` |
| Maximum control | Low-level API (see examples/streaming_example.py) |

## Examples

See the `examples/` directory for complete working examples:

- **examples/simple_streaming.py** - Basic callback-based streaming
- **examples/query_streaming.py** - Async iterator pattern
- **examples/session_context_streaming.py** - Context manager pattern
- **examples/streaming_example.py** - Comprehensive example with all event types
- **examples/example_template.py** - Minimal template

## Migration from v0.5.0

If you were using the low-level API before, you can simplify your code:

**Before (v0.5.0):**

```python
stream_response = await mix.streaming.stream_events_async(session_id=session_id)
await asyncio.sleep(0.5)

async with stream_response.result as event_stream:
    async def process_events():
        async for event in event_stream:
            if isinstance(event, SSEContentEvent):
                print(event.data.content, end="", flush=True)
            # ... more event handling

    await asyncio.gather(
        mix.messages.send_async(id=session_id, text=message),
        process_events(),
    )
```

**After (v0.6.0+):**

```python
await send_with_callbacks(
    mix,
    session_id=session.id,
    message=message,
    on_content=lambda text: print(text, end="", flush=True),
)
```

The low-level API is still available if you need it!
