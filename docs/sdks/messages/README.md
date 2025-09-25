# Messages
(*messages*)

## Overview

### Available Operations

* [get_history](#get_history) - Get global message history
* [list_session](#list_session) - List session messages
* [send](#send) - Send a message to session

## get_history

Retrieve message history across all sessions with optional pagination

### Example Usage

<!-- UsageSnippet language="python" operationID="getMessageHistory" method="get" path="/api/messages/history" -->
```python
from mix_python_sdk import Mix


with Mix() as mix:

    res = mix.messages.get_history(limit=50, offset=0)

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `limit`                                                             | *Optional[int]*                                                     | :heavy_minus_sign:                                                  | Maximum number of messages to return                                |
| `offset`                                                            | *Optional[int]*                                                     | :heavy_minus_sign:                                                  | Number of messages to skip                                          |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[List[models.BackendMessage]](../../models/.md)**

### Errors

| Error Type             | Status Code            | Content Type           |
| ---------------------- | ---------------------- | ---------------------- |
| errors.ErrorResponse   | 401                    | application/json       |
| errors.ErrorResponse   | 500                    | application/json       |
| errors.MixDefaultError | 4XX, 5XX               | \*/\*                  |

## list_session

Retrieve all messages from a specific session

### Example Usage

<!-- UsageSnippet language="python" operationID="getSessionMessages" method="get" path="/api/sessions/{id}/messages" -->
```python
from mix_python_sdk import Mix


with Mix() as mix:

    res = mix.messages.list_session(id="<id>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `id`                                                                | *str*                                                               | :heavy_check_mark:                                                  | Session ID                                                          |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[List[models.BackendMessage]](../../models/.md)**

### Errors

| Error Type             | Status Code            | Content Type           |
| ---------------------- | ---------------------- | ---------------------- |
| errors.ErrorResponse   | 404                    | application/json       |
| errors.MixDefaultError | 4XX, 5XX               | \*/\*                  |

## send

Send a user message to a specific session for AI processing

### Example Usage

<!-- UsageSnippet language="python" operationID="sendMessage" method="post" path="/api/sessions/{id}/messages" -->
```python
from mix_python_sdk import Mix


with Mix() as mix:

    res = mix.messages.send(id="<id>", apps=[
        "<value 1>",
    ], media=[
        "<value 1>",
        "<value 2>",
    ], plan_mode=False, text="<value>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `id`                                                                | *str*                                                               | :heavy_check_mark:                                                  | Session ID                                                          |
| `apps`                                                              | List[*str*]                                                         | :heavy_check_mark:                                                  | Array of app identifiers or references                              |
| `media`                                                             | List[*str*]                                                         | :heavy_check_mark:                                                  | Array of media file references or URLs                              |
| `plan_mode`                                                         | *bool*                                                              | :heavy_check_mark:                                                  | Whether the message is in planning mode                             |
| `text`                                                              | *str*                                                               | :heavy_check_mark:                                                  | The text content of the message                                     |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.BackendMessage](../../models/backendmessage.md)**

### Errors

| Error Type             | Status Code            | Content Type           |
| ---------------------- | ---------------------- | ---------------------- |
| errors.ErrorResponse   | 400, 404               | application/json       |
| errors.MixDefaultError | 4XX, 5XX               | \*/\*                  |