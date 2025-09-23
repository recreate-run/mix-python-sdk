# StoreToolCredentialsRequest


## Fields

| Field                                    | Type                                     | Required                                 | Description                              |
| ---------------------------------------- | ---------------------------------------- | ---------------------------------------- | ---------------------------------------- |
| `api_key`                                | *str*                                    | :heavy_check_mark:                       | API key for authentication               |
| `provider`                               | *str*                                    | :heavy_check_mark:                       | Tool provider name (e.g., brave, gemini) |
| `tool_type`                              | [models.ToolType](../models/tooltype.md) | :heavy_check_mark:                       | Tool category type                       |