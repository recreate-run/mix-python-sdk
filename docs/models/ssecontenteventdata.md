# SSEContentEventData


## Fields

| Field                                                                     | Type                                                                      | Required                                                                  | Description                                                               |
| ------------------------------------------------------------------------- | ------------------------------------------------------------------------- | ------------------------------------------------------------------------- | ------------------------------------------------------------------------- |
| `assistant_message_id`                                                    | *Optional[str]*                                                           | :heavy_minus_sign:                                                        | ID of the assistant message this content belongs to                       |
| `content`                                                                 | *str*                                                                     | :heavy_check_mark:                                                        | Streaming content delta                                                   |
| `parent_tool_call_id`                                                     | *Optional[str]*                                                           | :heavy_minus_sign:                                                        | ID of the parent tool call that spawned this subagent (for nested events) |
| `type`                                                                    | *str*                                                                     | :heavy_check_mark:                                                        | Content event type                                                        |