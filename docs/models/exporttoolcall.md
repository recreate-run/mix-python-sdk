# ExportToolCall

Complete tool call information for export


## Fields

| Field                                                | Type                                                 | Required                                             | Description                                          |
| ---------------------------------------------------- | ---------------------------------------------------- | ---------------------------------------------------- | ---------------------------------------------------- |
| `finished`                                           | *bool*                                               | :heavy_check_mark:                                   | Whether tool execution finished                      |
| `id`                                                 | *str*                                                | :heavy_check_mark:                                   | Tool call identifier                                 |
| `input`                                              | *str*                                                | :heavy_check_mark:                                   | Tool input as JSON string                            |
| `input_json`                                         | [Optional[models.InputJSON]](../models/inputjson.md) | :heavy_minus_sign:                                   | Parsed tool input (optional)                         |
| `is_error`                                           | *Optional[bool]*                                     | :heavy_minus_sign:                                   | Whether execution resulted in error (optional)       |
| `metadata`                                           | *Optional[str]*                                      | :heavy_minus_sign:                                   | Additional tool metadata (optional)                  |
| `name`                                               | *str*                                                | :heavy_check_mark:                                   | Tool name                                            |
| `result`                                             | *Optional[str]*                                      | :heavy_minus_sign:                                   | Tool execution result (optional)                     |
| `type`                                               | *str*                                                | :heavy_check_mark:                                   | Tool type                                            |