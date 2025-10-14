# GetAuthStatusProviders


## Fields

| Field                                                                            | Type                                                                             | Required                                                                         | Description                                                                      |
| -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- |
| `auth_method`                                                                    | [Optional[models.GetAuthStatusAuthMethod]](../models/getauthstatusauthmethod.md) | :heavy_minus_sign:                                                               | Authentication method (oauth, api_key, none)                                     |
| `authenticated`                                                                  | *Optional[bool]*                                                                 | :heavy_minus_sign:                                                               | Whether provider is authenticated                                                |
| `display_name`                                                                   | *Optional[str]*                                                                  | :heavy_minus_sign:                                                               | User-friendly provider name                                                      |