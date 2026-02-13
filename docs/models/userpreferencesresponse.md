# UserPreferencesResponse

User preferences configuration


## Fields

| Field                                                 | Type                                                  | Required                                              | Description                                           |
| ----------------------------------------------------- | ----------------------------------------------------- | ----------------------------------------------------- | ----------------------------------------------------- |
| `created_at`                                          | *Optional[int]*                                       | :heavy_minus_sign:                                    | Unix timestamp when preferences were created          |
| `main_agent_max_tokens`                               | *Optional[int]*                                       | :heavy_minus_sign:                                    | Maximum tokens for main agent responses               |
| `main_agent_model`                                    | *Optional[str]*                                       | :heavy_minus_sign:                                    | Main agent model ID                                   |
| `main_agent_reasoning_effort`                         | *Optional[str]*                                       | :heavy_minus_sign:                                    | Reasoning effort setting for main agent               |
| `preferred_provider`                                  | *Optional[str]*                                       | :heavy_minus_sign:                                    | Preferred AI provider (anthropic, openai, openrouter) |
| `sub_agent_max_tokens`                                | *Optional[int]*                                       | :heavy_minus_sign:                                    | Maximum tokens for sub agent responses                |
| `sub_agent_model`                                     | *Optional[str]*                                       | :heavy_minus_sign:                                    | Sub agent model ID                                    |
| `sub_agent_reasoning_effort`                          | *Optional[str]*                                       | :heavy_minus_sign:                                    | Reasoning effort setting for sub agent                |
| `updated_at`                                          | *Optional[int]*                                       | :heavy_minus_sign:                                    | Unix timestamp of last update                         |