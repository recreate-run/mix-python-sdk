# ListMcpServersResponse


## Fields

| Field                                                                       | Type                                                                        | Required                                                                    | Description                                                                 |
| --------------------------------------------------------------------------- | --------------------------------------------------------------------------- | --------------------------------------------------------------------------- | --------------------------------------------------------------------------- |
| `connected`                                                                 | *bool*                                                                      | :heavy_check_mark:                                                          | Whether the MCP server is currently connected                               |
| `name`                                                                      | *str*                                                                       | :heavy_check_mark:                                                          | MCP server name                                                             |
| `status`                                                                    | *str*                                                                       | :heavy_check_mark:                                                          | Server connection status (e.g., 'connected', 'failed', 'disconnected')      |
| `tools`                                                                     | List[[models.Tool](../models/tool.md)]                                      | :heavy_minus_sign:                                                          | List of tools provided by this MCP server (null if server is not connected) |