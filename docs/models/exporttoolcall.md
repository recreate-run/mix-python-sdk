# ExportToolCall

Complete tool call information for export


## Fields

| Field                                                     | Type                                                      | Required                                                  | Description                                               |
| --------------------------------------------------------- | --------------------------------------------------------- | --------------------------------------------------------- | --------------------------------------------------------- |
| `finished`                                                | *bool*                                                    | :heavy_check_mark:                                        | Whether tool execution finished                           |
| `id`                                                      | *str*                                                     | :heavy_check_mark:                                        | Tool call identifier                                      |
| `input`                                                   | *str*                                                     | :heavy_check_mark:                                        | Tool input as JSON string                                 |
| `input_json`                                              | [Optional[models.InputJSON]](../models/inputjson.md)      | :heavy_minus_sign:                                        | Parsed tool input (optional)                              |
| `name`                                                    | *str*                                                     | :heavy_check_mark:                                        | Tool name                                                 |
| `result`                                                  | *Optional[str]*                                           | :heavy_minus_sign:                                        | Tool execution result (optional)                          |
| `screenshot_urls`                                         | List[*str*]                                               | :heavy_minus_sign:                                        | Screenshot URLs captured during tool execution (optional) |
| `type`                                                    | *str*                                                     | :heavy_check_mark:                                        | Tool type                                                 |