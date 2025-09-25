# ForkSessionRequestBody


## Fields

| Field                                                                | Type                                                                 | Required                                                             | Description                                                          |
| -------------------------------------------------------------------- | -------------------------------------------------------------------- | -------------------------------------------------------------------- | -------------------------------------------------------------------- |
| `message_index`                                                      | *int*                                                                | :heavy_check_mark:                                                   | Index of the last message to include in the fork (0-based)           |
| `title`                                                              | *Optional[str]*                                                      | :heavy_minus_sign:                                                   | Optional title for the forked session (defaults to 'Forked Session') |