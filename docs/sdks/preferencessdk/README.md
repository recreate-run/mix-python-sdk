# Preferences

## Overview

### Available Operations

* [get_preferences](#get_preferences) - Get user preferences
* [update_preferences](#update_preferences) - Update user preferences
* [get_available_providers](#get_available_providers) - Get available providers
* [reset_preferences](#reset_preferences) - Reset preferences

## get_preferences

Retrieve current user preferences including model and provider settings

### Example Usage

<!-- UsageSnippet language="python" operationID="getPreferences" method="get" path="/api/preferences" -->
```python
from mix_python_sdk import Mix


with Mix(
    server_url="https://api.example.com",
) as mix:

    res = mix.preferences.get_preferences()

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.GetPreferencesResponse](../../models/getpreferencesresponse.md)**

### Errors

| Error Type             | Status Code            | Content Type           |
| ---------------------- | ---------------------- | ---------------------- |
| errors.ErrorResponse   | 500                    | application/json       |
| errors.MixDefaultError | 4XX, 5XX               | \*/\*                  |

## update_preferences

Update user preferences including model and provider settings

### Example Usage

<!-- UsageSnippet language="python" operationID="updatePreferences" method="post" path="/api/preferences" -->
```python
from mix_python_sdk import Mix


with Mix(
    server_url="https://api.example.com",
) as mix:

    res = mix.preferences.update_preferences()

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `main_agent_max_tokens`                                             | *Optional[int]*                                                     | :heavy_minus_sign:                                                  | Maximum tokens for main agent responses                             |
| `main_agent_model`                                                  | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | Main agent model ID                                                 |
| `main_agent_reasoning_effort`                                       | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | Reasoning effort setting for main agent                             |
| `preferred_provider`                                                | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | Preferred AI provider (anthropic, openai, openrouter)               |
| `sub_agent_max_tokens`                                              | *Optional[int]*                                                     | :heavy_minus_sign:                                                  | Maximum tokens for sub agent responses                              |
| `sub_agent_model`                                                   | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | Sub agent model ID                                                  |
| `sub_agent_reasoning_effort`                                        | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | Reasoning effort setting for sub agent                              |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.UpdatePreferencesResponse](../../models/updatepreferencesresponse.md)**

### Errors

| Error Type             | Status Code            | Content Type           |
| ---------------------- | ---------------------- | ---------------------- |
| errors.ErrorResponse   | 400                    | application/json       |
| errors.ErrorResponse   | 500                    | application/json       |
| errors.MixDefaultError | 4XX, 5XX               | \*/\*                  |

## get_available_providers

Retrieve list of available AI providers and their supported models

### Example Usage

<!-- UsageSnippet language="python" operationID="getAvailableProviders" method="get" path="/api/preferences/providers" -->
```python
from mix_python_sdk import Mix


with Mix(
    server_url="https://api.example.com",
) as mix:

    res = mix.preferences.get_available_providers()

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[Dict[str, models.GetAvailableProvidersResponse]](../../models/.md)**

### Errors

| Error Type             | Status Code            | Content Type           |
| ---------------------- | ---------------------- | ---------------------- |
| errors.ErrorResponse   | 500                    | application/json       |
| errors.MixDefaultError | 4XX, 5XX               | \*/\*                  |

## reset_preferences

Reset user preferences to default values

### Example Usage

<!-- UsageSnippet language="python" operationID="resetPreferences" method="post" path="/api/preferences/reset" -->
```python
from mix_python_sdk import Mix


with Mix(
    server_url="https://api.example.com",
) as mix:

    res = mix.preferences.reset_preferences()

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.ResetPreferencesResponse](../../models/resetpreferencesresponse.md)**

### Errors

| Error Type             | Status Code            | Content Type           |
| ---------------------- | ---------------------- | ---------------------- |
| errors.ErrorResponse   | 500                    | application/json       |
| errors.MixDefaultError | 4XX, 5XX               | \*/\*                  |