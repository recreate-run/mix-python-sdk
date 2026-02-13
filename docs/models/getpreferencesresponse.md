# GetPreferencesResponse

User preferences and available providers


## Fields

| Field                                                                            | Type                                                                             | Required                                                                         | Description                                                                      |
| -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- |
| `available_providers`                                                            | Dict[str, [models.AvailableProviders](../models/availableproviders.md)]          | :heavy_check_mark:                                                               | Map of available AI providers and their models                                   |
| `preferences`                                                                    | [Optional[models.UserPreferencesResponse]](../models/userpreferencesresponse.md) | :heavy_minus_sign:                                                               | User preferences configuration                                                   |