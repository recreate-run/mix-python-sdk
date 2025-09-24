# Streaming
(*streaming*)

## Overview

### Available Operations

* [stream_events](#stream_events) - Server-Sent Events stream for real-time updates
* [send_streaming_message](#send_streaming_message) - Send message via streaming pipeline

## stream_events

Establishes a persistent SSE connection for receiving real-time updates during message processing. Connection remains open for multiple messages and includes proper reconnection support with Last-Event-ID header.

### Example Usage

<!-- UsageSnippet language="python" operationID="streamEvents" method="get" path="/stream" -->
```python
from mix_python_sdk import Mix


with Mix() as mix:

    res = mix.streaming.stream_events(session_id="<id>")

    with res as event_stream:
        for event in event_stream:
            # handle event
            print(event, flush=True)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `session_id`                                                        | *str*                                                               | :heavy_check_mark:                                                  | Session ID to stream events for                                     |
| `last_event_id`                                                     | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | Last received event ID for reconnection and event replay            |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.StreamEventsResponse](../../models/streameventsresponse.md)**

### Errors

| Error Type             | Status Code            | Content Type           |
| ---------------------- | ---------------------- | ---------------------- |
| errors.ErrorResponse   | 404                    | application/json       |
| errors.ErrorResponse   | 500                    | application/json       |
| errors.MixDefaultError | 4XX, 5XX               | \*/\*                  |

## send_streaming_message

Send a message to a session via the streaming pipeline. This endpoint integrates with active SSE connections to broadcast real-time processing events including thinking, content, tool execution, and completion events.

### Example Usage

<!-- UsageSnippet language="python" operationID="sendStreamingMessage" method="post" path="/stream/{id}/message" -->
```python
from mix_python_sdk import Mix


with Mix() as mix:

    res = mix.streaming.send_streaming_message(id="<id>", content="<value>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `id`                                                                | *str*                                                               | :heavy_check_mark:                                                  | Session ID to send message to                                       |
| `content`                                                           | *str*                                                               | :heavy_check_mark:                                                  | Message content to send for processing                              |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.StreamMessageResponse](../../models/streammessageresponse.md)**

### Errors

| Error Type             | Status Code            | Content Type           |
| ---------------------- | ---------------------- | ---------------------- |
| errors.ErrorResponse   | 400, 404               | application/json       |
| errors.ErrorResponse   | 500                    | application/json       |
| errors.MixDefaultError | 4XX, 5XX               | \*/\*                  |