# RewindSessionRequestBody


## Fields

| Field                                                                                    | Type                                                                                     | Required                                                                                 | Description                                                                              |
| ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- |
| `cleanup_media`                                                                          | *Optional[bool]*                                                                         | :heavy_minus_sign:                                                                       | Whether to clean up media files created after the rewind point (based on file timestamp) |
| `message_id`                                                                             | *str*                                                                                    | :heavy_check_mark:                                                                       | ID of the last message to keep. All messages after this message will be deleted.         |