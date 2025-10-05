# Streaming
(*streaming*)

## Overview

### Available Operations

* [stream_events](#stream_events) - Server-Sent Events stream for real-time updates

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