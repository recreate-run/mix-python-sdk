# SSEErrorEventData


## Fields

| Field                             | Type                              | Required                          | Description                       |
| --------------------------------- | --------------------------------- | --------------------------------- | --------------------------------- |
| `attempt`                         | *Optional[int]*                   | :heavy_minus_sign:                | Current retry attempt number      |
| `error`                           | *str*                             | :heavy_check_mark:                | Error message description         |
| `max_attempts`                    | *Optional[int]*                   | :heavy_minus_sign:                | Maximum number of retry attempts  |
| `retry_after`                     | *Optional[int]*                   | :heavy_minus_sign:                | Milliseconds to wait before retry |
| `type`                            | *Optional[str]*                   | :heavy_minus_sign:                | Error type classification         |