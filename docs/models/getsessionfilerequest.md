# GetSessionFileRequest


## Fields

| Field                                                                 | Type                                                                  | Required                                                              | Description                                                           |
| --------------------------------------------------------------------- | --------------------------------------------------------------------- | --------------------------------------------------------------------- | --------------------------------------------------------------------- |
| `id`                                                                  | *str*                                                                 | :heavy_check_mark:                                                    | Session ID                                                            |
| `filename`                                                            | *str*                                                                 | :heavy_check_mark:                                                    | Filename to retrieve                                                  |
| `thumb`                                                               | *Optional[str]*                                                       | :heavy_minus_sign:                                                    | Thumbnail specification: '100' (box), 'w100' (width), 'h100' (height) |
| `time`                                                                | *Optional[float]*                                                     | :heavy_minus_sign:                                                    | Time offset in seconds for video thumbnails (default: 1.0)            |