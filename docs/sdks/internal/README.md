# Internal

## Overview

### Available Operations

* [refresh_o_auth_tokens](#refresh_o_auth_tokens) - Manually refresh OAuth tokens

## refresh_o_auth_tokens

Manually trigger OAuth token refresh for all expired tokens. Normally tokens are refreshed automatically by the background service every 30 minutes.

### Example Usage

<!-- UsageSnippet language="python" operationID="refreshOAuthTokens" method="post" path="/internal/auth/refresh-tokens" -->
```python
from mix_python_sdk import Mix


with Mix(
    server_url="https://api.example.com",
) as mix:

    res = mix.internal.refresh_o_auth_tokens()

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.RefreshOAuthTokensResponse](../../models/refreshoauthtokensresponse.md)**

### Errors

| Error Type             | Status Code            | Content Type           |
| ---------------------- | ---------------------- | ---------------------- |
| errors.ErrorResponse   | 500                    | application/json       |
| errors.MixDefaultError | 4XX, 5XX               | \*/\*                  |