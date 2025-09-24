# SSEToolExecutionCompleteEventData


## Fields

| Field                                 | Type                                  | Required                              | Description                           |
| ------------------------------------- | ------------------------------------- | ------------------------------------- | ------------------------------------- |
| `progress`                            | *str*                                 | :heavy_check_mark:                    | Final execution progress description  |
| `success`                             | *bool*                                | :heavy_check_mark:                    | Indicates if tool execution succeeded |
| `tool_call_id`                        | *str*                                 | :heavy_check_mark:                    | Tool call identifier                  |
| `tool_name`                           | *str*                                 | :heavy_check_mark:                    | Name of the completed tool            |
| `type`                                | *str*                                 | :heavy_check_mark:                    | Tool execution complete event type    |