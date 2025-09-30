# Sessions
(*sessions*)

## Overview

### Available Operations

* [list](#list) - List all sessions
* [create](#create) - Create a new session
* [delete](#delete) - Delete a session
* [get](#get) - Get a specific session
* [export_session](#export_session) - Export session transcript
* [fork](#fork) - Fork a session
* [rewind_session](#rewind_session) - Rewind a session
* [cancel_processing](#cancel_processing) - Cancel agent processing

## list

Retrieve a list of all available sessions with their metadata

### Example Usage

<!-- UsageSnippet language="python" operationID="listSessions" method="get" path="/api/sessions" -->
```python
from mix_python_sdk import Mix


with Mix() as mix:

    res = mix.sessions.list()

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[List[models.SessionData]](../../models/.md)**

### Errors

| Error Type             | Status Code            | Content Type           |
| ---------------------- | ---------------------- | ---------------------- |
| errors.ErrorResponse   | 401                    | application/json       |
| errors.ErrorResponse   | 500                    | application/json       |
| errors.MixDefaultError | 4XX, 5XX               | \*/\*                  |

## create

Create a new session with required title and optional custom system prompt. Session automatically gets isolated storage directory.

### Example Usage

<!-- UsageSnippet language="python" operationID="createSession" method="post" path="/api/sessions" -->
```python
from mix_python_sdk import Mix


with Mix() as mix:

    res = mix.sessions.create(title="<value>", custom_system_prompt="You are a helpful assistant specialized in $<domain>. Always be concise and accurate.", prompt_mode="append")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                                                                                                                                                 | Type                                                                                                                                                                                                                                                      | Required                                                                                                                                                                                                                                                  | Description                                                                                                                                                                                                                                               | Example                                                                                                                                                                                                                                                   |
| --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `title`                                                                                                                                                                                                                                                   | *str*                                                                                                                                                                                                                                                     | :heavy_check_mark:                                                                                                                                                                                                                                        | Title for the session                                                                                                                                                                                                                                     |                                                                                                                                                                                                                                                           |
| `custom_system_prompt`                                                                                                                                                                                                                                    | *Optional[str]*                                                                                                                                                                                                                                           | :heavy_minus_sign:                                                                                                                                                                                                                                        | Custom system prompt content. Size limits apply based on promptMode: 100KB (102,400 bytes) for replace mode, 50KB (51,200 bytes) for append mode. Ignored in default mode. Supports environment variable substitution with $<variable> syntax.            | You are a helpful assistant specialized in $<domain>. Always be concise and accurate.                                                                                                                                                                     |
| `prompt_mode`                                                                                                                                                                                                                                             | [Optional[models.PromptMode]](../../models/promptmode.md)                                                                                                                                                                                                 | :heavy_minus_sign:                                                                                                                                                                                                                                        | Custom prompt handling mode:<br/>- 'default': Use base system prompt only (customSystemPrompt ignored)<br/>- 'append': Append customSystemPrompt to base system prompt (50KB limit)<br/>- 'replace': Replace base system prompt with customSystemPrompt (100KB limit) | append                                                                                                                                                                                                                                                    |
| `retries`                                                                                                                                                                                                                                                 | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                                                                                                          | :heavy_minus_sign:                                                                                                                                                                                                                                        | Configuration to override the default retry behavior of the client.                                                                                                                                                                                       |                                                                                                                                                                                                                                                           |

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


with Mix() as mix:

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


with Mix() as mix:

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

## export_session

Export complete session transcript with all messages, tool calls, reasoning, and metadata as JSON

### Example Usage

<!-- UsageSnippet language="python" operationID="exportSession" method="get" path="/api/sessions/{id}/export" -->
```python
from mix_python_sdk import Mix


with Mix() as mix:

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

## fork

Create a new session based on an existing session, copying messages up to a specified index

### Example Usage

<!-- UsageSnippet language="python" operationID="forkSession" method="post" path="/api/sessions/{id}/fork" -->
```python
from mix_python_sdk import Mix


with Mix() as mix:

    res = mix.sessions.fork(id="<id>", message_index=385832)

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                            | Type                                                                 | Required                                                             | Description                                                          |
| -------------------------------------------------------------------- | -------------------------------------------------------------------- | -------------------------------------------------------------------- | -------------------------------------------------------------------- |
| `id`                                                                 | *str*                                                                | :heavy_check_mark:                                                   | Source session ID to fork from                                       |
| `message_index`                                                      | *int*                                                                | :heavy_check_mark:                                                   | Index of the last message to include in the fork (0-based)           |
| `title`                                                              | *Optional[str]*                                                      | :heavy_minus_sign:                                                   | Optional title for the forked session (defaults to 'Forked Session') |
| `retries`                                                            | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)     | :heavy_minus_sign:                                                   | Configuration to override the default retry behavior of the client.  |

### Response

**[models.SessionData](../../models/sessiondata.md)**

### Errors

| Error Type             | Status Code            | Content Type           |
| ---------------------- | ---------------------- | ---------------------- |
| errors.ErrorResponse   | 400, 404               | application/json       |
| errors.MixDefaultError | 4XX, 5XX               | \*/\*                  |

## rewind_session

Delete messages after a specified message in the current session, optionally cleaning up media files created after that point

### Example Usage

<!-- UsageSnippet language="python" operationID="rewindSession" method="post" path="/api/sessions/{id}/rewind" -->
```python
from mix_python_sdk import Mix


with Mix() as mix:

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


with Mix() as mix:

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