# SendMessageRequestBody


## Fields

| Field                                   | Type                                    | Required                                | Description                             |
| --------------------------------------- | --------------------------------------- | --------------------------------------- | --------------------------------------- |
| `apps`                                  | List[*str*]                             | :heavy_check_mark:                      | Array of app identifiers or references  |
| `media`                                 | List[*str*]                             | :heavy_check_mark:                      | Array of media file references or URLs  |
| `plan_mode`                             | *bool*                                  | :heavy_check_mark:                      | Whether the message is in planning mode |
| `text`                                  | *str*                                   | :heavy_check_mark:                      | The text content of the message         |