# StreamMessageResponse

Response from streaming message endpoint indicating broadcast status


## Fields

| Field                                | Type                                 | Required                             | Description                          |
| ------------------------------------ | ------------------------------------ | ------------------------------------ | ------------------------------------ |
| `session_id`                         | *str*                                | :heavy_check_mark:                   | Session identifier                   |
| `status`                             | [models.Status](../models/status.md) | :heavy_check_mark:                   | Broadcast status                     |