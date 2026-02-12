# Sessions

## Overview

### Available Operations

* [list](#list) - List all sessions
* [create](#create) - Create a new session
* [delete](#delete) - Delete a session
* [get](#get) - Get a specific session
* [update_session_callbacks](#update_session_callbacks) - Update session callbacks
* [export_session](#export_session) - Export session transcript
* [rewind_session](#rewind_session) - Rewind a session
* [cancel_processing](#cancel_processing) - Cancel agent processing

## list

Retrieve a list of all available sessions with their metadata

### Example Usage

<!-- UsageSnippet language="python" operationID="listSessions" method="get" path="/api/sessions" -->
```python
from mix_python_sdk import Mix


with Mix(
    server_url="https://api.example.com",
) as mix:

    res = mix.sessions.list(include_subagents=False)

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                            | Type                                                                                 | Required                                                                             | Description                                                                          |
| ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ |
| `include_subagents`                                                                  | *Optional[bool]*                                                                     | :heavy_minus_sign:                                                                   | Include subagent sessions in response (default: false, subagent sessions are hidden) |
| `retries`                                                                            | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                     | :heavy_minus_sign:                                                                   | Configuration to override the default retry behavior of the client.                  |

### Response

**[List[models.SessionData]](../../models/.md)**

### Errors

| Error Type             | Status Code            | Content Type           |
| ---------------------- | ---------------------- | ---------------------- |
| errors.ErrorResponse   | 401                    | application/json       |
| errors.ErrorResponse   | 500                    | application/json       |
| errors.MixDefaultError | 4XX, 5XX               | \*/\*                  |

## create

Create a new session with required title and optional custom system prompt. Session automatically gets isolated storage directory. Supports session-level callbacks for automated actions after tool execution.

### Example Usage: invalid_prompt_mode

<!-- UsageSnippet language="python" operationID="createSession" method="post" path="/api/sessions" example="invalid_prompt_mode" -->
```python
from mix_python_sdk import Mix


with Mix(
    server_url="https://api.example.com",
) as mix:

    res = mix.sessions.create(browser_mode="local-browser-service", title="<value>", callbacks=[
        {
            "message_content": "Please review the changes and run tests",
            "name": "Log Output",
            "tool_name": "*",
            "type": "send_message",
        },
    ], cdp_url="wss://connect.browserbase.com/v1/sessions/abc123", custom_system_prompt="You are a helpful assistant specialized in $<domain>. Always be concise and accurate.", prompt_mode="append", session_type="main", subagent_type="")

    # Handle response
    print(res)

```
### Example Usage: invalid_session_type

<!-- UsageSnippet language="python" operationID="createSession" method="post" path="/api/sessions" example="invalid_session_type" -->
```python
from mix_python_sdk import Mix


with Mix(
    server_url="https://api.example.com",
) as mix:

    res = mix.sessions.create(browser_mode="local-browser-service", title="<value>", callbacks=[
        {
            "message_content": "Please review the changes and run tests",
            "name": "Log Output",
            "tool_name": "*",
            "type": "send_message",
        },
    ], cdp_url="wss://connect.browserbase.com/v1/sessions/abc123", custom_system_prompt="You are a helpful assistant specialized in $<domain>. Always be concise and accurate.", prompt_mode="append", session_type="main", subagent_type="")

    # Handle response
    print(res)

```
### Example Usage: missing_title

<!-- UsageSnippet language="python" operationID="createSession" method="post" path="/api/sessions" example="missing_title" -->
```python
from mix_python_sdk import Mix


with Mix(
    server_url="https://api.example.com",
) as mix:

    res = mix.sessions.create(browser_mode="local-browser-service", title="<value>", callbacks=[
        {
            "message_content": "Please review the changes and run tests",
            "name": "Log Output",
            "tool_name": "*",
            "type": "send_message",
        },
    ], cdp_url="wss://connect.browserbase.com/v1/sessions/abc123", custom_system_prompt="You are a helpful assistant specialized in $<domain>. Always be concise and accurate.", prompt_mode="append", session_type="main", subagent_type="")

    # Handle response
    print(res)

```
### Example Usage: prompt_size_exceeded_append

<!-- UsageSnippet language="python" operationID="createSession" method="post" path="/api/sessions" example="prompt_size_exceeded_append" -->
```python
from mix_python_sdk import Mix


with Mix(
    server_url="https://api.example.com",
) as mix:

    res = mix.sessions.create(browser_mode="local-browser-service", title="<value>", callbacks=[
        {
            "message_content": "Please review the changes and run tests",
            "name": "Log Output",
            "tool_name": "*",
            "type": "send_message",
        },
    ], cdp_url="wss://connect.browserbase.com/v1/sessions/abc123", custom_system_prompt="You are a helpful assistant specialized in $<domain>. Always be concise and accurate.", prompt_mode="append", session_type="main", subagent_type="")

    # Handle response
    print(res)

```
### Example Usage: prompt_size_exceeded_replace

<!-- UsageSnippet language="python" operationID="createSession" method="post" path="/api/sessions" example="prompt_size_exceeded_replace" -->
```python
from mix_python_sdk import Mix


with Mix(
    server_url="https://api.example.com",
) as mix:

    res = mix.sessions.create(browser_mode="local-browser-service", title="<value>", callbacks=[
        {
            "message_content": "Please review the changes and run tests",
            "name": "Log Output",
            "tool_name": "*",
            "type": "send_message",
        },
    ], cdp_url="wss://connect.browserbase.com/v1/sessions/abc123", custom_system_prompt="You are a helpful assistant specialized in $<domain>. Always be concise and accurate.", prompt_mode="append", session_type="main", subagent_type="")

    # Handle response
    print(res)

```
### Example Usage: subagent_type_not_allowed

<!-- UsageSnippet language="python" operationID="createSession" method="post" path="/api/sessions" example="subagent_type_not_allowed" -->
```python
from mix_python_sdk import Mix


with Mix(
    server_url="https://api.example.com",
) as mix:

    res = mix.sessions.create(browser_mode="local-browser-service", title="<value>", callbacks=[
        {
            "message_content": "Please review the changes and run tests",
            "name": "Log Output",
            "tool_name": "*",
            "type": "send_message",
        },
    ], cdp_url="wss://connect.browserbase.com/v1/sessions/abc123", custom_system_prompt="You are a helpful assistant specialized in $<domain>. Always be concise and accurate.", prompt_mode="append", session_type="main", subagent_type="")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                                                                                                                                                  | Type                                                                                                                                                                                                                                                       | Required                                                                                                                                                                                                                                                   | Description                                                                                                                                                                                                                                                | Example                                                                                                                                                                                                                                                    |
| ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `browser_mode`                                                                                                                                                                                                                                             | [models.CreateSessionBrowserMode](../../models/createsessionbrowsermode.md)                                                                                                                                                                                | :heavy_check_mark:                                                                                                                                                                                                                                         | Browser automation mode (required):<br/>- 'electron-embedded-browser': Electron app with embedded Chromium browser<br/>- 'local-browser-service': Local browser-service (GoRod-based)<br/>- 'remote-cdp-websocket': Remote CDP WebSocket URL (cloud browser providers) | local-browser-service                                                                                                                                                                                                                                      |
| `title`                                                                                                                                                                                                                                                    | *str*                                                                                                                                                                                                                                                      | :heavy_check_mark:                                                                                                                                                                                                                                         | Title for the session                                                                                                                                                                                                                                      |                                                                                                                                                                                                                                                            |
| `callbacks`                                                                                                                                                                                                                                                | List[[models.Callback](../../models/callback.md)]                                                                                                                                                                                                          | :heavy_minus_sign:                                                                                                                                                                                                                                         | Session-level callbacks that execute after tool completion. Environment variables available: CALLBACK_TOOL_RESULT, CALLBACK_TOOL_NAME, CALLBACK_TOOL_ID, CALLBACK_SESSION_ID                                                                               |                                                                                                                                                                                                                                                            |
| `cdp_url`                                                                                                                                                                                                                                                  | *Optional[str]*                                                                                                                                                                                                                                            | :heavy_minus_sign:                                                                                                                                                                                                                                         | CDP WebSocket URL for remote browser connections. Required when browserMode is 'remote-cdp-websocket'. Must start with 'ws://' or 'wss://'.                                                                                                                | wss://connect.browserbase.com/v1/sessions/abc123                                                                                                                                                                                                           |
| `custom_system_prompt`                                                                                                                                                                                                                                     | *Optional[str]*                                                                                                                                                                                                                                            | :heavy_minus_sign:                                                                                                                                                                                                                                         | Custom system prompt content. Size limits apply based on promptMode: 100KB (102,400 bytes) for replace mode, 50KB (51,200 bytes) for append mode. Ignored in default mode. Supports environment variable substitution with $<variable> syntax.             | You are a helpful assistant specialized in $<domain>. Always be concise and accurate.                                                                                                                                                                      |
| `prompt_mode`                                                                                                                                                                                                                                              | [Optional[models.PromptMode]](../../models/promptmode.md)                                                                                                                                                                                                  | :heavy_minus_sign:                                                                                                                                                                                                                                         | Custom prompt handling mode:<br/>- 'default': Use base system prompt only (customSystemPrompt ignored)<br/>- 'append': Append customSystemPrompt to base system prompt (50KB limit)<br/>- 'replace': Replace base system prompt with customSystemPrompt (100KB limit) | append                                                                                                                                                                                                                                                     |
| `session_type`                                                                                                                                                                                                                                             | [Optional[models.CreateSessionSessionType]](../../models/createsessionsessiontype.md)                                                                                                                                                                      | :heavy_minus_sign:                                                                                                                                                                                                                                         | Session type. API can only create 'main' sessions. Subagent sessions are created automatically by the task delegation system.                                                                                                                              | main                                                                                                                                                                                                                                                       |
| `subagent_type`                                                                                                                                                                                                                                            | *Optional[str]*                                                                                                                                                                                                                                            | :heavy_minus_sign:                                                                                                                                                                                                                                         | Subagent type - must not be set for API-created sessions. This field is reserved for programmatic subagent creation.                                                                                                                                       |                                                                                                                                                                                                                                                            |
| `retries`                                                                                                                                                                                                                                                  | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                                                                                                           | :heavy_minus_sign:                                                                                                                                                                                                                                         | Configuration to override the default retry behavior of the client.                                                                                                                                                                                        |                                                                                                                                                                                                                                                            |

### Response

**[models.SessionData](../../models/sessiondata.md)**

### Errors

| Error Type             | Status Code            | Content Type           |
| ---------------------- | ---------------------- | ---------------------- |
| errors.ErrorResponse   | 400                    | application/json       |
| errors.MixDefaultError | 4XX, 5XX               | \*/\*                  |

## delete

Permanently delete a session and all its data

### Example Usage

<!-- UsageSnippet language="python" operationID="deleteSession" method="delete" path="/api/sessions/{id}" -->
```python
from mix_python_sdk import Mix


with Mix(
    server_url="https://api.example.com",
) as mix:

    mix.sessions.delete(id="<id>")

    # Use the SDK ...

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `id`                                                                | *str*                                                               | :heavy_check_mark:                                                  | Session ID                                                          |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Errors

| Error Type             | Status Code            | Content Type           |
| ---------------------- | ---------------------- | ---------------------- |
| errors.ErrorResponse   | 404                    | application/json       |
| errors.MixDefaultError | 4XX, 5XX               | \*/\*                  |

## get

Retrieve detailed information about a specific session

### Example Usage

<!-- UsageSnippet language="python" operationID="getSession" method="get" path="/api/sessions/{id}" -->
```python
from mix_python_sdk import Mix


with Mix(
    server_url="https://api.example.com",
) as mix:

    res = mix.sessions.get(id="<id>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `id`                                                                | *str*                                                               | :heavy_check_mark:                                                  | Session ID                                                          |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.SessionData](../../models/sessiondata.md)**

### Errors

| Error Type             | Status Code            | Content Type           |
| ---------------------- | ---------------------- | ---------------------- |
| errors.ErrorResponse   | 404                    | application/json       |
| errors.MixDefaultError | 4XX, 5XX               | \*/\*                  |

## update_session_callbacks

Update the callback configurations for a session. Callbacks execute automatically after tool completion. Pass an empty array to clear all callbacks.

### Example Usage

<!-- UsageSnippet language="python" operationID="updateSessionCallbacks" method="patch" path="/api/sessions/{id}/callbacks" -->
```python
from mix_python_sdk import Mix


with Mix(
    server_url="https://api.example.com",
) as mix:

    res = mix.sessions.update_session_callbacks(id="<id>", callbacks=[])

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                                                                    | Type                                                                                                                                                                         | Required                                                                                                                                                                     | Description                                                                                                                                                                  |
| ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `id`                                                                                                                                                                         | *str*                                                                                                                                                                        | :heavy_check_mark:                                                                                                                                                           | Session ID to update                                                                                                                                                         |
| `callbacks`                                                                                                                                                                  | List[[models.Callback](../../models/callback.md)]                                                                                                                            | :heavy_check_mark:                                                                                                                                                           | Session-level callbacks that execute after tool completion. Environment variables available: CALLBACK_TOOL_RESULT, CALLBACK_TOOL_NAME, CALLBACK_TOOL_ID, CALLBACK_SESSION_ID |
| `retries`                                                                                                                                                                    | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                             | :heavy_minus_sign:                                                                                                                                                           | Configuration to override the default retry behavior of the client.                                                                                                          |

### Response

**[models.SessionData](../../models/sessiondata.md)**

### Errors

| Error Type             | Status Code            | Content Type           |
| ---------------------- | ---------------------- | ---------------------- |
| errors.ErrorResponse   | 400, 404               | application/json       |
| errors.MixDefaultError | 4XX, 5XX               | \*/\*                  |

## export_session

Export complete session transcript with all messages, tool calls, reasoning, and metadata as JSON

### Example Usage

<!-- UsageSnippet language="python" operationID="exportSession" method="get" path="/api/sessions/{id}/export" -->
```python
from mix_python_sdk import Mix


with Mix(
    server_url="https://api.example.com",
) as mix:

    res = mix.sessions.export_session(id="<id>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `id`                                                                | *str*                                                               | :heavy_check_mark:                                                  | Session ID to export                                                |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.ExportSessionResponse](../../models/exportsessionresponse.md)**

### Errors

| Error Type             | Status Code            | Content Type           |
| ---------------------- | ---------------------- | ---------------------- |
| errors.ErrorResponse   | 404                    | application/json       |
| errors.ErrorResponse   | 500                    | application/json       |
| errors.MixDefaultError | 4XX, 5XX               | \*/\*                  |

## rewind_session

Delete messages after a specified message in the current session, optionally cleaning up media files created after that point

### Example Usage

<!-- UsageSnippet language="python" operationID="rewindSession" method="post" path="/api/sessions/{id}/rewind" -->
```python
from mix_python_sdk import Mix


with Mix(
    server_url="https://api.example.com",
) as mix:

    res = mix.sessions.rewind_session(id="<id>", message_id="<id>", cleanup_media=True)

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                | Type                                                                                     | Required                                                                                 | Description                                                                              |
| ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- |
| `id`                                                                                     | *str*                                                                                    | :heavy_check_mark:                                                                       | Session ID to rewind                                                                     |
| `message_id`                                                                             | *str*                                                                                    | :heavy_check_mark:                                                                       | ID of the last message to keep. All messages after this message will be deleted.         |
| `cleanup_media`                                                                          | *Optional[bool]*                                                                         | :heavy_minus_sign:                                                                       | Whether to clean up media files created after the rewind point (based on file timestamp) |
| `retries`                                                                                | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                         | :heavy_minus_sign:                                                                       | Configuration to override the default retry behavior of the client.                      |

### Response

**[models.SessionData](../../models/sessiondata.md)**

### Errors

| Error Type             | Status Code            | Content Type           |
| ---------------------- | ---------------------- | ---------------------- |
| errors.ErrorResponse   | 400, 404               | application/json       |
| errors.MixDefaultError | 4XX, 5XX               | \*/\*                  |

## cancel_processing

Cancel any ongoing agent processing in the specified session

### Example Usage

<!-- UsageSnippet language="python" operationID="cancelSessionProcessing" method="post" path="/api/sessions/{id}/cancel" -->
```python
from mix_python_sdk import Mix


with Mix(
    server_url="https://api.example.com",
) as mix:

    res = mix.sessions.cancel_processing(id="<id>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `id`                                                                | *str*                                                               | :heavy_check_mark:                                                  | Session ID                                                          |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.CancelSessionProcessingResponse](../../models/cancelsessionprocessingresponse.md)**

### Errors

| Error Type             | Status Code            | Content Type           |
| ---------------------- | ---------------------- | ---------------------- |
| errors.ErrorResponse   | 404                    | application/json       |
| errors.MixDefaultError | 4XX, 5XX               | \*/\*                  |