# MessageData


## Fields

| Field                                                  | Type                                                   | Required                                               | Description                                            |
| ------------------------------------------------------ | ------------------------------------------------------ | ------------------------------------------------------ | ------------------------------------------------------ |
| `assistant_response`                                   | *Optional[str]*                                        | :heavy_minus_sign:                                     | Assistant's response message (optional)                |
| `id`                                                   | *str*                                                  | :heavy_check_mark:                                     | Unique message identifier                              |
| `reasoning`                                            | *Optional[str]*                                        | :heavy_minus_sign:                                     | Reasoning process (optional)                           |
| `reasoning_duration`                                   | *Optional[int]*                                        | :heavy_minus_sign:                                     | Reasoning duration in milliseconds (optional)          |
| `role`                                                 | [models.MessageRole](../models/messagerole.md)         | :heavy_check_mark:                                     | Message role                                           |
| `session_id`                                           | *str*                                                  | :heavy_check_mark:                                     | Session identifier                                     |
| `tool_calls`                                           | List[[models.ToolCallData](../models/toolcalldata.md)] | :heavy_minus_sign:                                     | Tool calls made during message processing              |
| `user_input`                                           | *str*                                                  | :heavy_check_mark:                                     | User's input message                                   |