# SSESummarizeEvent

Base SSE event with standard fields


## Fields

| Field                                                                | Type                                                                 | Required                                                             | Description                                                          | Example                                                              |
| -------------------------------------------------------------------- | -------------------------------------------------------------------- | -------------------------------------------------------------------- | -------------------------------------------------------------------- | -------------------------------------------------------------------- |
| `event`                                                              | [models.SSESummarizeEventEvent](../models/ssesummarizeeventevent.md) | :heavy_check_mark:                                                   | Event type identifier                                                |                                                                      |
| `id`                                                                 | *str*                                                                | :heavy_check_mark:                                                   | Unique sequential event identifier for ordering and reconnection     | 1234567890                                                           |
| `retry`                                                              | *Optional[int]*                                                      | :heavy_minus_sign:                                                   | Client retry interval in milliseconds                                | 30000                                                                |
| `data`                                                               | [models.SSESummarizeEventData](../models/ssesummarizeeventdata.md)   | :heavy_check_mark:                                                   | N/A                                                                  |                                                                      |