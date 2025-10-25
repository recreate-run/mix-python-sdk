# Tools
(*tools*)

## Overview

### Available Operations

* [list_llm_tools](#list_llm_tools) - List LLM tools
* [get_tool_credentials_status](#get_tool_credentials_status) - Get tool credentials status
* [get_tools_status](#get_tools_status) - Get tools status

## list_llm_tools

Returns the list of all LLM tools that Claude can invoke. The list is dynamically extracted from the actual tools registered in CoderAgentTools() (agent/tools.go), ensuring it always reflects the current tool availability. Typical tools include: Bash, Edit, Read, Write, Grep, Glob, WebFetch, WebSearch, ReadMedia, TodoWrite, ExitPlanMode, and Task. This endpoint is useful for creating tool callbacks or understanding available agent capabilities.

### Example Usage

<!-- UsageSnippet language="python" operationID="listLLMTools" method="get" path="/api/tools" -->
```python
from mix_python_sdk import Mix


with Mix() as mix:

    res = mix.tools.list_llm_tools()

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.ListLLMToolsResponse](../../models/listllmtoolsresponse.md)**

### Errors

| Error Type             | Status Code            | Content Type           |
| ---------------------- | ---------------------- | ---------------------- |
| errors.ErrorResponse   | 500                    | application/json       |
| errors.MixDefaultError | 4XX, 5XX               | \*/\*                  |

## get_tool_credentials_status

Returns authentication/credential status for external tool integrations (Brave Search, Gemini Vision, etc.). This endpoint checks if API keys are configured for tools that require external service credentials.

### Example Usage

<!-- UsageSnippet language="python" operationID="getToolCredentialsStatus" method="get" path="/api/tools/credentials-status" -->
```python
from mix_python_sdk import Mix


with Mix() as mix:

    res = mix.tools.get_tool_credentials_status()

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.GetToolCredentialsStatusResponse](../../models/gettoolcredentialsstatusresponse.md)**

### Errors

| Error Type             | Status Code            | Content Type           |
| ---------------------- | ---------------------- | ---------------------- |
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