# SendMessageResponse

Message accepted for processing. Agent runs asynchronously and streams results via SSE.


## Fields

| Field                              | Type                               | Required                           | Description                        | Example                            |
| ---------------------------------- | ---------------------------------- | ---------------------------------- | ---------------------------------- | ---------------------------------- |
| `session_id`                       | *str*                              | :heavy_check_mark:                 | Session ID for the processing task |                                    |
| `status`                           | *str*                              | :heavy_check_mark:                 | Processing status                  | processing                         |