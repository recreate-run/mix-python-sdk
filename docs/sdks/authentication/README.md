# Authentication
(*authentication*)

## Overview

### Available Operations

* [set_api_key](#set_api_key) - Set API key
* [initiate_o_auth_login](#initiate_o_auth_login) - OAuth authentication

## set_api_key

Set API key for direct authentication

### Example Usage

<!-- UsageSnippet language="python" operationID="setApiKey" method="post" path="/api/auth/apikey" -->
```python
from mix_python_sdk import Mix


with Mix() as mix:

    res = mix.authentication.set_api_key(api_key="<value>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `api_key`                                                           | *str*                                                               | :heavy_check_mark:                                                  | API key for authentication                                          |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.SetAPIKeyResponse](../../models/setapikeyresponse.md)**

### Errors

| Error Type               | Status Code              | Content Type             |
| ------------------------ | ------------------------ | ------------------------ |
| errors.RESTResponseError | 400, 401                 | application/json         |
| errors.RESTResponseError | 500                      | application/json         |
| errors.MixDefaultError   | 4XX, 5XX                 | \*/\*                    |

## initiate_o_auth_login

Initiate OAuth authentication flow

### Example Usage

<!-- UsageSnippet language="python" operationID="initiateOAuthLogin" method="post" path="/api/auth/login" -->
```python
from mix_python_sdk import Mix


with Mix() as mix:

    res = mix.authentication.initiate_o_auth_login()

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.InitiateOAuthLoginResponse](../../models/initiateoauthloginresponse.md)**

### Errors

| Error Type               | Status Code              | Content Type             |
| ------------------------ | ------------------------ | ------------------------ |
| errors.RESTResponseError | 401                      | application/json         |
| errors.RESTResponseError | 500                      | application/json         |
| errors.MixDefaultError   | 4XX, 5XX                 | \*/\*                    |