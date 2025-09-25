# ToolCallData


## Fields

| Field                                          | Type                                           | Required                                       | Description                                    |
| ---------------------------------------------- | ---------------------------------------------- | ---------------------------------------------- | ---------------------------------------------- |
| `finished`                                     | *bool*                                         | :heavy_check_mark:                             | Whether tool call has finished                 |
| `id`                                           | *str*                                          | :heavy_check_mark:                             | Unique tool call identifier                    |
| `input`                                        | *str*                                          | :heavy_check_mark:                             | Tool input parameters                          |
| `is_error`                                     | *Optional[bool]*                               | :heavy_minus_sign:                             | Whether tool call resulted in error (optional) |
| `name`                                         | *str*                                          | :heavy_check_mark:                             | Tool name                                      |
| `result`                                       | *Optional[str]*                                | :heavy_minus_sign:                             | Tool execution result (optional)               |
| `type`                                         | *str*                                          | :heavy_check_mark:                             | Tool type                                      |