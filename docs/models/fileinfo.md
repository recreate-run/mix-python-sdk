# FileInfo


## Fields

| Field                               | Type                                | Required                            | Description                         |
| ----------------------------------- | ----------------------------------- | ----------------------------------- | ----------------------------------- |
| `is_dir`                            | *bool*                              | :heavy_check_mark:                  | Whether this is a directory         |
| `modified`                          | *int*                               | :heavy_check_mark:                  | Last modified timestamp (Unix time) |
| `name`                              | *str*                               | :heavy_check_mark:                  | File name                           |
| `size`                              | *int*                               | :heavy_check_mark:                  | File size in bytes                  |
| `url`                               | *str*                               | :heavy_check_mark:                  | Static URL to access the file       |