# Health

## Overview

### Available Operations

* [get_o_auth_health](#get_o_auth_health) - Get OAuth authentication health

## get_o_auth_health

Get health status of all OAuth credentials. Background service refreshes tokens 35 minutes before expiry. API calls mark tokens expired 5 minutes before expiry. Health statuses: 'healthy' (tokens valid, >5min remaining), 'degraded' (some tokens within 5min of expiry but refreshable), 'unhealthy' (tokens expired without refresh capability)

### Example Usage

<!-- UsageSnippet language="python" operationID="getOAuthHealth" method="get" path="/health/auth" -->
```python
from mix_python_sdk import Mix


with Mix(
    server_url="https://api.example.com",
) as mix:

    res = mix.health.get_o_auth_health()

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.GetOAuthHealthResponse](../../models/getoauthhealthresponse.md)**

### Errors

| Error Type             | Status Code            | Content Type           |
| ---------------------- | ---------------------- | ---------------------- |
| errors.ErrorResponse   | 500                    | application/json       |
| errors.MixDefaultError | 4XX, 5XX               | \*/\*                  |