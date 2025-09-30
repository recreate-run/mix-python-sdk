# ExportMessage

Complete message information for export


## Fields

| Field                                                                | Type                                                                 | Required                                                             | Description                                                          |
| -------------------------------------------------------------------- | -------------------------------------------------------------------- | -------------------------------------------------------------------- | -------------------------------------------------------------------- |
| `content`                                                            | *str*                                                                | :heavy_check_mark:                                                   | Message content                                                      |
| `created_at`                                                         | [date](https://docs.python.org/3/library/datetime.html#date-objects) | :heavy_check_mark:                                                   | Message creation timestamp                                           |
| `finish_reason`                                                      | *Optional[str]*                                                      | :heavy_minus_sign:                                                   | Completion finish reason (optional)                                  |
| `id`                                                                 | *str*                                                                | :heavy_check_mark:                                                   | Message identifier                                                   |
| `model`                                                              | *Optional[str]*                                                      | :heavy_minus_sign:                                                   | Model used for this message (optional)                               |
| `reasoning`                                                          | *Optional[str]*                                                      | :heavy_minus_sign:                                                   | Reasoning content (optional)                                         |
| `reasoning_duration`                                                 | *Optional[int]*                                                      | :heavy_minus_sign:                                                   | Reasoning duration in milliseconds (optional)                        |
| `role`                                                               | *str*                                                                | :heavy_check_mark:                                                   | Message role (user, assistant, tool)                                 |
| `tool_calls`                                                         | List[[models.ExportToolCall](../models/exporttoolcall.md)]           | :heavy_minus_sign:                                                   | Tool calls with complete information                                 |
| `updated_at`                                                         | [date](https://docs.python.org/3/library/datetime.html#date-objects) | :heavy_check_mark:                                                   | Message update timestamp                                             |