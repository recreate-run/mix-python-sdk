# SSECompleteEventData


## Fields

| Field                                         | Type                                          | Required                                      | Description                                   |
| --------------------------------------------- | --------------------------------------------- | --------------------------------------------- | --------------------------------------------- |
| `content`                                     | *Optional[str]*                               | :heavy_minus_sign:                            | Final response content                        |
| `done`                                        | *bool*                                        | :heavy_check_mark:                            | Indicates message processing completion       |
| `message_id`                                  | *Optional[str]*                               | :heavy_minus_sign:                            | Completed message identifier                  |
| `reasoning`                                   | *Optional[str]*                               | :heavy_minus_sign:                            | Optional reasoning content                    |
| `reasoning_duration`                          | *Optional[int]*                               | :heavy_minus_sign:                            | Duration of reasoning process in milliseconds |
| `type`                                        | *str*                                         | :heavy_check_mark:                            | Completion type                               |