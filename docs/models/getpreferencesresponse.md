# GetPreferencesResponse

User preferences and available providers


## Fields

| Field                                                                                        | Type                                                                                         | Required                                                                                     | Description                                                                                  |
| -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- |
| `available_providers`                                                                        | Dict[str, [models.AvailableProviders](../models/availableproviders.md)]                      | :heavy_check_mark:                                                                           | Map of available AI providers and their models                                               |
| `preferences`                                                                                | [OptionalNullable[models.GetPreferencesPreferences]](../models/getpreferencespreferences.md) | :heavy_minus_sign:                                                                           | User preferences (null if no preferences exist)                                              |