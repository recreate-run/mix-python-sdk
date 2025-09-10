# Permissions
(*permissions*)

## Overview

### Available Operations

* [deny](#deny) - Deny permission
* [grant](#grant) - Grant permission

## deny

Deny a specific permission

### Example Usage

<!-- UsageSnippet language="python" operationID="denyPermission" method="post" path="/api/permissions/{id}/deny" -->
```python
from mix_python_sdk import Mix


with Mix() as mix:

    res = mix.permissions.deny(id="<id>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `id`                                                                | *str*                                                               | :heavy_check_mark:                                                  | Permission ID                                                       |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.DenyPermissionResponse](../../models/denypermissionresponse.md)**

### Errors

| Error Type               | Status Code              | Content Type             |
| ------------------------ | ------------------------ | ------------------------ |
| errors.RESTResponseError | 401, 404                 | application/json         |
| errors.RESTResponseError | 500                      | application/json         |
| errors.MixDefaultError   | 4XX, 5XX                 | \*/\*                    |

## grant

Grant a specific permission

### Example Usage

<!-- UsageSnippet language="python" operationID="grantPermission" method="post" path="/api/permissions/{id}/grant" -->
```python
from mix_python_sdk import Mix


with Mix() as mix:

    res = mix.permissions.grant(id="<id>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `id`                                                                | *str*                                                               | :heavy_check_mark:                                                  | Permission ID                                                       |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.GrantPermissionResponse](../../models/grantpermissionresponse.md)**

### Errors

| Error Type               | Status Code              | Content Type             |
| ------------------------ | ------------------------ | ------------------------ |
| errors.RESTResponseError | 401, 404                 | application/json         |
| errors.RESTResponseError | 500                      | application/json         |
| errors.MixDefaultError   | 4XX, 5XX                 | \*/\*                    |