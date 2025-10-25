# SSEThinkingEventData


## Fields

| Field                                                                     | Type                                                                      | Required                                                                  | Description                                                               |
| ------------------------------------------------------------------------- | ------------------------------------------------------------------------- | ------------------------------------------------------------------------- | ------------------------------------------------------------------------- |
| `assistant_message_id`                                                    | *Optional[str]*                                                           | :heavy_minus_sign:                                                        | ID of the assistant message this thinking belongs to                      |
| `content`                                                                 | *str*                                                                     | :heavy_check_mark:                                                        | Thinking or reasoning content                                             |
| `parent_tool_call_id`                                                     | *Optional[str]*                                                           | :heavy_minus_sign:                                                        | ID of the parent tool call that spawned this subagent (for nested events) |
| `type`                                                                    | *str*                                                                     | :heavy_check_mark:                                                        | Thinking event type                                                       |