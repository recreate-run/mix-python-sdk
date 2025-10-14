# SSEToolParameterDeltaEventData


## Fields

| Field                                                              | Type                                                               | Required                                                           | Description                                                        |
| ------------------------------------------------------------------ | ------------------------------------------------------------------ | ------------------------------------------------------------------ | ------------------------------------------------------------------ |
| `input`                                                            | *str*                                                              | :heavy_check_mark:                                                 | Partial JSON parameter delta - may not be parseable until complete |
| `tool_call_id`                                                     | *str*                                                              | :heavy_check_mark:                                                 | Tool call identifier for correlation                               |
| `type`                                                             | *str*                                                              | :heavy_check_mark:                                                 | Tool parameter delta event type                                    |