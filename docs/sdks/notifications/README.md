# Notifications

## Overview

### Available Operations

* [respond_to_notification](#respond_to_notification) - Respond to notification

## respond_to_notification

Send user's response to a notification request

### Example Usage

<!-- UsageSnippet language="python" operationID="respondToNotification" method="post" path="/api/notifications/{id}/respond" -->
```python
from mix_python_sdk import Mix


with Mix(
    server_url="https://api.example.com",
) as mix:

    mix.notifications.respond_to_notification(id="<id>", type_="acknowledge")

    # Use the SDK ...

```

### Parameters

| Parameter                                                                     | Type                                                                          | Required                                                                      | Description                                                                   |
| ----------------------------------------------------------------------------- | ----------------------------------------------------------------------------- | ----------------------------------------------------------------------------- | ----------------------------------------------------------------------------- |
| `id`                                                                          | *str*                                                                         | :heavy_check_mark:                                                            | Notification ID                                                               |
| `type`                                                                        | [models.RespondToNotificationType](../../models/respondtonotificationtype.md) | :heavy_check_mark:                                                            | Response type                                                                 |
| `value`                                                                       | *Optional[str]*                                                               | :heavy_minus_sign:                                                            | User's text input or selected choice (optional for acknowledge type)          |
| `retries`                                                                     | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)              | :heavy_minus_sign:                                                            | Configuration to override the default retry behavior of the client.           |

### Errors

| Error Type             | Status Code            | Content Type           |
| ---------------------- | ---------------------- | ---------------------- |
| errors.ErrorResponse   | 401, 404               | application/json       |
| errors.ErrorResponse   | 500                    | application/json       |
| errors.MixDefaultError | 4XX, 5XX               | \*/\*                  |