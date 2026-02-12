# SSEToolUseParameterDeltaEventData


## Fields

| Field                                                                     | Type                                                                      | Required                                                                  | Description                                                               |
| ------------------------------------------------------------------------- | ------------------------------------------------------------------------- | ------------------------------------------------------------------------- | ------------------------------------------------------------------------- |
| `assistant_message_id`                                                    | *Optional[str]*                                                           | :heavy_minus_sign:                                                        | ID of the assistant message this tool parameter delta belongs to          |
| `input`                                                                   | *str*                                                                     | :heavy_check_mark:                                                        | Partial JSON parameter delta - may not be parseable until complete        |
| `parent_tool_call_id`                                                     | *Optional[str]*                                                           | :heavy_minus_sign:                                                        | ID of the parent tool call that spawned this subagent (for nested events) |
| `tool_call_id`                                                            | *str*                                                                     | :heavy_check_mark:                                                        | Tool call identifier for correlation                                      |
| `type`                                                                    | *str*                                                                     | :heavy_check_mark:                                                        | Tool use parameter delta event type                                       |