# Tools
(*tools*)

## Overview

### Available Operations

* [get_tools_status](#get_tools_status) - Get tools status

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