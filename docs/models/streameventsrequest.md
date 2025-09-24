# StreamEventsRequest


## Fields

| Field                                                    | Type                                                     | Required                                                 | Description                                              |
| -------------------------------------------------------- | -------------------------------------------------------- | -------------------------------------------------------- | -------------------------------------------------------- |
| `session_id`                                             | *str*                                                    | :heavy_check_mark:                                       | Session ID to stream events for                          |
| `last_event_id`                                          | *Optional[str]*                                          | :heavy_minus_sign:                                       | Last received event ID for reconnection and event replay |