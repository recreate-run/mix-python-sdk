# Tools
(*tools*)

## Overview

### Available Operations

* [store_tool_credentials](#store_tool_credentials) - Store tool API key
* [delete_tool_credentials](#delete_tool_credentials) - Delete tool API key
* [get_tools_status](#get_tools_status) - Get tools status

## store_tool_credentials

Store API key for a specific tool provider

### Example Usage

<!-- UsageSnippet language="python" operationID="storeToolCredentials" method="post" path="/api/tools/credentials" -->
```python
from mix_python_sdk import Mix


with Mix() as mix:

    res = mix.tools.store_tool_credentials(api_key="<value>", provider="<value>", tool_type="multimodal_analyzer")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `api_key`                                                           | *str*                                                               | :heavy_check_mark:                                                  | API key for authentication                                          |
| `provider`                                                          | *str*                                                               | :heavy_check_mark:                                                  | Tool provider name (e.g., brave, gemini)                            |
| `tool_type`                                                         | [models.ToolType](../../models/tooltype.md)                         | :heavy_check_mark:                                                  | Tool category type                                                  |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.StoreToolCredentialsResponse](../../models/storetoolcredentialsresponse.md)**

### Errors

| Error Type             | Status Code            | Content Type           |
| ---------------------- | ---------------------- | ---------------------- |
| errors.ErrorResponse   | 400                    | application/json       |
| errors.ErrorResponse   | 500                    | application/json       |
| errors.MixDefaultError | 4XX, 5XX               | \*/\*                  |

## delete_tool_credentials

Delete stored API key for a specific tool provider

### Example Usage

<!-- UsageSnippet language="python" operationID="deleteToolCredentials" method="delete" path="/api/tools/credentials/{tool_type}/{provider}" -->
```python
from mix_python_sdk import Mix


with Mix() as mix:

    res = mix.tools.delete_tool_credentials(tool_type="<value>", provider="<value>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `tool_type`                                                         | *str*                                                               | :heavy_check_mark:                                                  | Tool category type (web_search, multimodal_analyzer)                |
| `provider`                                                          | *str*                                                               | :heavy_check_mark:                                                  | Tool provider name (e.g., brave, gemini)                            |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.DeleteToolCredentialsResponse](../../models/deletetoolcredentialsresponse.md)**

### Errors

| Error Type             | Status Code            | Content Type           |
| ---------------------- | ---------------------- | ---------------------- |
| errors.ErrorResponse   | 400, 404               | application/json       |
| errors.ErrorResponse   | 500                    | application/json       |
| errors.MixDefaultError | 4XX, 5XX               | \*/\*                  |

## get_tools_status

Get status and authentication information for all available tools and categories

### Example Usage

<!-- UsageSnippet language="python" operationID="getToolsStatus" method="get" path="/api/tools/status" -->
```python
from mix_python_sdk import Mix


with Mix() as mix:

    res = mix.tools.get_tools_status()

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.GetToolsStatusResponse](../../models/gettoolsstatusresponse.md)**

### Errors

| Error Type             | Status Code            | Content Type           |
| ---------------------- | ---------------------- | ---------------------- |
| errors.ErrorResponse   | 500                    | application/json       |
| errors.MixDefaultError | 4XX, 5XX               | \*/\*                  |