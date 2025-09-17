# UpdatePreferencesResponse

Updated preferences


## Fields

| Field                           | Type                            | Required                        | Description                     |
| ------------------------------- | ------------------------------- | ------------------------------- | ------------------------------- |
| `created_at`                    | *Optional[int]*                 | :heavy_minus_sign:              | Creation timestamp              |
| `main_agent_max_tokens`         | *Optional[int]*                 | :heavy_minus_sign:              | Maximum tokens for main agent   |
| `main_agent_model`              | *Optional[str]*                 | :heavy_minus_sign:              | Main agent model ID             |
| `main_agent_reasoning_effort`   | *Optional[str]*                 | :heavy_minus_sign:              | Reasoning effort for main agent |
| `preferred_provider`            | *Optional[str]*                 | :heavy_minus_sign:              | Preferred AI provider           |
| `sub_agent_max_tokens`          | *Optional[int]*                 | :heavy_minus_sign:              | Maximum tokens for sub agent    |
| `sub_agent_model`               | *Optional[str]*                 | :heavy_minus_sign:              | Sub agent model ID              |
| `sub_agent_reasoning_effort`    | *Optional[str]*                 | :heavy_minus_sign:              | Reasoning effort for sub agent  |
| `updated_at`                    | *Optional[int]*                 | :heavy_minus_sign:              | Last update timestamp           |