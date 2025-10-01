# SSESessionCreatedEventData


## Fields

| Field                                       | Type                                        | Required                                    | Description                                 | Example                                     |
| ------------------------------------------- | ------------------------------------------- | ------------------------------------------- | ------------------------------------------- | ------------------------------------------- |
| `created_at`                                | *int*                                       | :heavy_check_mark:                          | Unix timestamp when the session was created |                                             |
| `session_id`                                | *str*                                       | :heavy_check_mark:                          | ID of the newly created session             |                                             |
| `title`                                     | *str*                                       | :heavy_check_mark:                          | Title of the newly created session          |                                             |
| `type`                                      | *str*                                       | :heavy_check_mark:                          | Event type                                  | session_created                             |