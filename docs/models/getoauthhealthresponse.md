# GetOAuthHealthResponse

OAuth health status


## Fields

| Field                                                                             | Type                                                                              | Required                                                                          | Description                                                                       | Example                                                                           |
| --------------------------------------------------------------------------------- | --------------------------------------------------------------------------------- | --------------------------------------------------------------------------------- | --------------------------------------------------------------------------------- | --------------------------------------------------------------------------------- |
| `providers`                                                                       | Dict[str, [models.GetOAuthHealthProviders](../models/getoauthhealthproviders.md)] | :heavy_check_mark:                                                                | Map of provider OAuth health status                                               |                                                                                   |
| `status`                                                                          | [models.Status](../models/status.md)                                              | :heavy_check_mark:                                                                | Overall health status                                                             | healthy                                                                           |
| `timestamp`                                                                       | [date](https://docs.python.org/3/library/datetime.html#date-objects)              | :heavy_check_mark:                                                                | Health check timestamp                                                            |                                                                                   |