# Authentication
(*authentication*)

## Overview

### Available Operations

* [store_api_key](#store_api_key) - Store API key
* [set_api_key](#set_api_key) - Set API key
* [initiate_o_auth_login](#initiate_o_auth_login) - OAuth authentication
* [handle_o_auth_callback](#handle_o_auth_callback) - Handle OAuth callback
* [start_o_auth_flow](#start_o_auth_flow) - Start OAuth authentication
* [get_auth_status](#get_auth_status) - Get authentication status
* [validate_preferred_provider](#validate_preferred_provider) - Validate preferred provider
* [delete_credentials](#delete_credentials) - Delete provider credentials

## store_api_key

Store API key for direct authentication with a specific provider

### Example Usage

<!-- UsageSnippet language="python" operationID="storeApiKey" method="post" path="/api/auth/api-key" -->
```python
from mix_python_sdk import Mix


with Mix() as mix:

    res = mix.authentication.store_api_key(api_key="<value>", provider="openrouter")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `api_key`                                                           | *str*                                                               | :heavy_check_mark:                                                  | API key for authentication                                          |
| `provider`                                                          | [models.Provider](../../models/provider.md)                         | :heavy_check_mark:                                                  | Provider name (anthropic, openai, openrouter)                       |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.StoreAPIKeyResponse](../../models/storeapikeyresponse.md)**

### Errors

| Error Type             | Status Code            | Content Type           |
| ---------------------- | ---------------------- | ---------------------- |
| errors.ErrorResponse   | 400                    | application/json       |
| errors.ErrorResponse   | 500                    | application/json       |
| errors.MixDefaultError | 4XX, 5XX               | \*/\*                  |

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

| Error Type             | Status Code            | Content Type           |
| ---------------------- | ---------------------- | ---------------------- |
| errors.ErrorResponse   | 400, 401               | application/json       |
| errors.ErrorResponse   | 500                    | application/json       |
| errors.MixDefaultError | 4XX, 5XX               | \*/\*                  |

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

| Error Type             | Status Code            | Content Type           |
| ---------------------- | ---------------------- | ---------------------- |
| errors.ErrorResponse   | 401                    | application/json       |
| errors.ErrorResponse   | 500                    | application/json       |
| errors.MixDefaultError | 4XX, 5XX               | \*/\*                  |

## handle_o_auth_callback

Process OAuth callback and exchange code for access token

### Example Usage

<!-- UsageSnippet language="python" operationID="handleOAuthCallback" method="post" path="/api/auth/oauth-callback" -->
```python
from mix_python_sdk import Mix


with Mix() as mix:

    res = mix.authentication.handle_o_auth_callback(code="<value>", provider="<value>", state="Arizona")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `code`                                                              | *str*                                                               | :heavy_check_mark:                                                  | Authorization code from OAuth provider                              |
| `provider`                                                          | *str*                                                               | :heavy_check_mark:                                                  | Provider name (anthropic)                                           |
| `state`                                                             | *str*                                                               | :heavy_check_mark:                                                  | OAuth state for verification                                        |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.HandleOAuthCallbackResponse](../../models/handleoauthcallbackresponse.md)**

### Errors

| Error Type             | Status Code            | Content Type           |
| ---------------------- | ---------------------- | ---------------------- |
| errors.ErrorResponse   | 400                    | application/json       |
| errors.ErrorResponse   | 500                    | application/json       |
| errors.MixDefaultError | 4XX, 5XX               | \*/\*                  |

## start_o_auth_flow

Initiate OAuth authentication flow for a specific provider

### Example Usage

<!-- UsageSnippet language="python" operationID="startOAuthFlow" method="post" path="/api/auth/oauth/{provider}" -->
```python
from mix_python_sdk import Mix


with Mix() as mix:

    res = mix.authentication.start_o_auth_flow(provider="<value>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `provider`                                                          | *str*                                                               | :heavy_check_mark:                                                  | Provider name (currently only 'anthropic')                          |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.StartOAuthFlowResponse](../../models/startoauthflowresponse.md)**

### Errors

| Error Type             | Status Code            | Content Type           |
| ---------------------- | ---------------------- | ---------------------- |
| errors.ErrorResponse   | 400                    | application/json       |
| errors.ErrorResponse   | 500                    | application/json       |
| errors.MixDefaultError | 4XX, 5XX               | \*/\*                  |

## get_auth_status

Get authentication status for all supported providers

### Example Usage

<!-- UsageSnippet language="python" operationID="getAuthStatus" method="get" path="/api/auth/status" -->
```python
from mix_python_sdk import Mix


with Mix() as mix:

    res = mix.authentication.get_auth_status()

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.GetAuthStatusResponse](../../models/getauthstatusresponse.md)**

### Errors

| Error Type             | Status Code            | Content Type           |
| ---------------------- | ---------------------- | ---------------------- |
| errors.ErrorResponse   | 500                    | application/json       |
| errors.MixDefaultError | 4XX, 5XX               | \*/\*                  |

## validate_preferred_provider

Check if the user's preferred provider is authenticated

### Example Usage

<!-- UsageSnippet language="python" operationID="validatePreferredProvider" method="get" path="/api/auth/validate" -->
```python
from mix_python_sdk import Mix


with Mix() as mix:

    res = mix.authentication.validate_preferred_provider()

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.ValidatePreferredProviderResponse](../../models/validatepreferredproviderresponse.md)**

### Errors

| Error Type             | Status Code            | Content Type           |
| ---------------------- | ---------------------- | ---------------------- |
| errors.ErrorResponse   | 500                    | application/json       |
| errors.MixDefaultError | 4XX, 5XX               | \*/\*                  |

## delete_credentials

Delete stored API key and/or OAuth credentials for a provider

### Example Usage

<!-- UsageSnippet language="python" operationID="deleteCredentials" method="delete" path="/api/auth/{provider}" -->
```python
from mix_python_sdk import Mix


with Mix() as mix:

    res = mix.authentication.delete_credentials(provider="<value>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `provider`                                                          | *str*                                                               | :heavy_check_mark:                                                  | Provider name (anthropic, openai, openrouter)                       |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.DeleteCredentialsResponse](../../models/deletecredentialsresponse.md)**

### Errors

| Error Type             | Status Code            | Content Type           |
| ---------------------- | ---------------------- | ---------------------- |
| errors.ErrorResponse   | 400                    | application/json       |
| errors.ErrorResponse   | 500                    | application/json       |
| errors.MixDefaultError | 4XX, 5XX               | \*/\*                  |