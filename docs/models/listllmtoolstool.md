# ListLLMToolsTool


## Fields

| Field                                                  | Type                                                   | Required                                               | Description                                            | Example                                                |
| ------------------------------------------------------ | ------------------------------------------------------ | ------------------------------------------------------ | ------------------------------------------------------ | ------------------------------------------------------ |
| `description`                                          | *Optional[str]*                                        | :heavy_minus_sign:                                     | Tool description                                       | Execute bash commands in a persistent shell session    |
| `name`                                                 | *Optional[str]*                                        | :heavy_minus_sign:                                     | Tool name                                              | Bash                                                   |
| `parameters`                                           | [Optional[models.Parameters]](../models/parameters.md) | :heavy_minus_sign:                                     | Tool parameter schema                                  |                                                        |
| `required`                                             | List[*str*]                                            | :heavy_minus_sign:                                     | Required parameters                                    |                                                        |