# HandleOAuthCallbackRequest


## Fields

| Field                                  | Type                                   | Required                               | Description                            |
| -------------------------------------- | -------------------------------------- | -------------------------------------- | -------------------------------------- |
| `code`                                 | *str*                                  | :heavy_check_mark:                     | Authorization code from OAuth provider |
| `provider`                             | *str*                                  | :heavy_check_mark:                     | Provider name (anthropic)              |
| `state`                                | *str*                                  | :heavy_check_mark:                     | OAuth state for verification           |