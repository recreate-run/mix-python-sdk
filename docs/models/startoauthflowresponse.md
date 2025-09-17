# StartOAuthFlowResponse

OAuth authorization information


## Fields

| Field                                  | Type                                   | Required                               | Description                            |
| -------------------------------------- | -------------------------------------- | -------------------------------------- | -------------------------------------- |
| `auth_url`                             | *Optional[str]*                        | :heavy_minus_sign:                     | OAuth authorization URL to redirect to |
| `message`                              | *Optional[str]*                        | :heavy_minus_sign:                     | Instructions for completing OAuth flow |
| `state`                                | *Optional[str]*                        | :heavy_minus_sign:                     | OAuth state token for verification     |