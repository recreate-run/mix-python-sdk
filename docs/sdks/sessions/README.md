# Sessions
(*sessions*)

## Overview

### Available Operations

* [list](#list) - List all sessions
* [create](#create) - Create a new session
* [delete](#delete) - Delete a session
* [get](#get) - Get a specific session
* [fork](#fork) - Fork a session
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

**[models.ListSessionsResponse](../../models/listsessionsresponse.md)**

### Errors

| Error Type               | Status Code              | Content Type             |
| ------------------------ | ------------------------ | ------------------------ |
| errors.RESTResponseError | 401                      | application/json         |
| errors.RESTResponseError | 500                      | application/json         |
| errors.MixDefaultError   | 4XX, 5XX                 | \*/\*                    |

## create

Create a new session with optional title and working directory

### Example Usage

<!-- UsageSnippet language="python" operationID="createSession" method="post" path="/api/sessions" -->
```python
from mix_python_sdk import Mix


with Mix() as mix:

    res = mix.sessions.create()

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `title`                                                             | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | Optional title for the session                                      |
| `working_directory`                                                 | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | Optional working directory path                                     |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.CreateSessionResponse](../../models/createsessionresponse.md)**

### Errors

| Error Type               | Status Code              | Content Type             |
| ------------------------ | ------------------------ | ------------------------ |
| errors.RESTResponseError | 400                      | application/json         |
| errors.MixDefaultError   | 4XX, 5XX                 | \*/\*                    |

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

| Error Type               | Status Code              | Content Type             |
| ------------------------ | ------------------------ | ------------------------ |
| errors.RESTResponseError | 404                      | application/json         |
| errors.MixDefaultError   | 4XX, 5XX                 | \*/\*                    |

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

**[models.GetSessionResponse](../../models/getsessionresponse.md)**

### Errors

| Error Type               | Status Code              | Content Type             |
| ------------------------ | ------------------------ | ------------------------ |
| errors.RESTResponseError | 404                      | application/json         |
| errors.MixDefaultError   | 4XX, 5XX                 | \*/\*                    |

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
| `message_index`                                                      | *int*                                                                | :heavy_check_mark:                                                   | Index of the last message to include in the fork (1-based)           |
| `title`                                                              | *Optional[str]*                                                      | :heavy_minus_sign:                                                   | Optional title for the forked session (defaults to 'Forked Session') |
| `retries`                                                            | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)     | :heavy_minus_sign:                                                   | Configuration to override the default retry behavior of the client.  |

### Response

**[models.ForkSessionResponse](../../models/forksessionresponse.md)**

### Errors

| Error Type               | Status Code              | Content Type             |
| ------------------------ | ------------------------ | ------------------------ |
| errors.RESTResponseError | 400, 404                 | application/json         |
| errors.MixDefaultError   | 4XX, 5XX                 | \*/\*                    |

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

| Error Type               | Status Code              | Content Type             |
| ------------------------ | ------------------------ | ------------------------ |
| errors.RESTResponseError | 404                      | application/json         |
| errors.MixDefaultError   | 4XX, 5XX                 | \*/\*                    |