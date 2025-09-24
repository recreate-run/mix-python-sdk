# SSEContentEvent

Base SSE event with standard fields


## Fields

| Field                                                            | Type                                                             | Required                                                         | Description                                                      | Example                                                          |
| ---------------------------------------------------------------- | ---------------------------------------------------------------- | ---------------------------------------------------------------- | ---------------------------------------------------------------- | ---------------------------------------------------------------- |
| `event`                                                          | [models.SSEContentEventEvent](../models/ssecontenteventevent.md) | :heavy_check_mark:                                               | Event type identifier                                            |                                                                  |
| `id`                                                             | *str*                                                            | :heavy_check_mark:                                               | Unique sequential event identifier for ordering and reconnection | 1234567890                                                       |
| `retry`                                                          | *Optional[int]*                                                  | :heavy_minus_sign:                                               | Client retry interval in milliseconds                            | 30000                                                            |
| `data`                                                           | [models.SSEContentEventData](../models/ssecontenteventdata.md)   | :heavy_check_mark:                                               | N/A                                                              |                                                                  |