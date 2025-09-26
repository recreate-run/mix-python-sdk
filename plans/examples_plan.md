# Mix Python SDK Example creation guidelines

## Overview

Use only the openrouter LLM provider, with the OPENROUTER_API_KEY. Don't use any other provider

## Implementation Standards

### Code Structure Template

Based on the structure of `authentication_example.py`, all example files must follow this exact pattern:

#### 1. File Header Format

```python
#!/usr/bin/env python3
"""
[Module Name] Example for Mix Python SDK

Documentation Reference: docs/sdks/[module]/README.md

This example demonstrates comprehensive [module] functionality including:
- [Feature 1 description]
- [Feature 2 description]
- [Feature 3 description]
...

Run this example to see all [module] methods in action.
"""

from mix_python_sdk import Mix
import os
```

#### 2. Environment Variable Setup (MANDATORY)

**All examples MUST follow this pattern:**

```python
from dotenv import load_dotenv

def main():
    # Load environment variables from .env file
    load_dotenv()

    # Get required API key from environment
    api_key = os.getenv("PROVIDER_API_KEY")
    if not api_key:
        raise ValueError("PROVIDER_API_KEY not found in environment variables. Please add it to your .env file.")
```

**Requirements:**

- Add `python-dotenv` dependency: `uv add python-dotenv`
- Load `.env` from workspace root with `load_dotenv()`
- Validate required environment variables exist
- Raise immediate error if API keys missing
- Use real API keys, never demo/placeholder keys

#### 3. Function Organization Pattern

- **One function per feature group**: Each major functionality gets its own dedicated function
- **Naming convention**: `demonstrate_[feature_name](mix, api_key)` (pass API key when needed)
- **Function docstrings**: Clear description of what each function demonstrates
- **Parameter**: All functions take `mix` client as parameter, plus API keys as needed
- **NO ERROR HANDLING**: Functions must NOT have try-catch blocks - let ALL errors crash immediately
- **Informative output**: Print statements showing operation flow and results

Example function structure:

```python
def demonstrate_feature_name(mix):
    """Demonstrate [specific functionality description]"""
    print("\n=== [Feature Name] Demo ===")

    print("Step description...")
    result = mix.module.operation()
    print(f"Result: {result}")

    # Additional processing if needed
    print("\nDetailed breakdown:")
    for key, value in result.__dict__.items():
        print(f"  {key}: {value}")
```

#### 7. Main Function Template

```python
def main():
    """Main function demonstrating Mix SDK [module] functionality"""
    # Load environment variables from .env file
    load_dotenv()

    # Get required API key from environment
    api_key = os.getenv("PROVIDER_API_KEY")
    if not api_key:
        raise ValueError("PROVIDER_API_KEY not found in environment variables. Please add it to your .env file.")

    server_url = os.getenv("MIX_SERVER_URL", "http://localhost:8088")

    print("="*60)
    print("MIX PYTHON SDK - [MODULE] EXAMPLE")
    print("="*60)
    print(f"Server URL: {server_url}")
    print("This example demonstrates all [module] functionality")
    print("Using real [PROVIDER] API key from .env file")
    print("="*60)

    with Mix(server_url=server_url) as mix:
        # Always start with system health check
        health = mix.system.get_health()
        print(f"System health: {health}")

        # Call each demonstration function in logical order
        demonstrate_feature1(mix, api_key)
        demonstrate_feature2(mix, api_key)
        demonstrate_feature3(mix)
        # ...


if __name__ == "__main__":
    main()
```

#### 4. Error Handling Requirements (CRITICAL)

**ZERO ERROR HANDLING POLICY:**

- **NO try/except blocks**: Remove ALL exception handling from code
- **Immediate crash**: Let all errors bubble up and crash the application
- **No graceful fallbacks**: Never suppress errors or provide default values
- **No silent failures**: Never catch and log errors - let them crash
- **Fail fast principle**: Stop execution on first error to surface problems immediately
- **No error recovery**: Never attempt to continue after failures
- **NO defensive programming**: Never use `hasattr` or other defensive patterns - let code fail fast with AttributeError when API contracts change

**Example of what NOT to do:**

```python
# WRONG - No error handling allowed
try:
    result = mix.authentication.store_api_key(api_key, provider)
except Exception as e:
    print(f"Error: {e}")
    return
```

**Correct approach:**

```python
# CORRECT - Let it crash
result = mix.authentication.store_api_key(api_key, provider)
```

#### 5. Output Formatting Standards

- **Section headers**: Use `=== [Section Name] Demo ===` format
- **Numbered steps**: Use "1. Step description...", "2. Next step..." within sections
- **Response display**: Always print operation results
- **Detailed breakdowns**: Access object attributes directly without defensive checks
- **Clear separation**: Empty lines between major sections
- **Status indicators**: Use visual indicators (✅, ❌) when appropriate

#### 6. Import and Environment Conventions

**Required imports for ALL examples:**

```python
#!/usr/bin/env python3
from mix_python_sdk import Mix
import os
from dotenv import load_dotenv
```

**Environment setup pattern:**

- **Always load .env**: `load_dotenv()` at start of main()
- **Validate API keys**: Raise error if required keys missing
- **Server URL**: `os.getenv("MIX_SERVER_URL", "http://localhost:8088")`
- **Context manager**: `with Mix(server_url=server_url) as mix:`
- **Dependency**: All examples require `python-dotenv` dependency

#### 7. Documentation Requirements

- **Module docstring**: Must include documentation reference and feature list
- **Function docstrings**: Every function must have a clear docstring
- **Inline comments**: Use comments to explain complex operations
- **Parameter documentation**: Explain demo parameters and real-world usage
- **Example notes**: Include notes about demo vs production usage

### Common Patterns

Each example file will follow these established patterns:

- **Environment Loading**: `load_dotenv()` and API key validation at start
- **Real Credentials**: Load actual API keys from `.env`, never use demo keys
- **Context Manager Usage**: `with Mix(server_url=server_url) as mix:`
- **Zero Error Handling**: NO try/catch blocks - let ALL errors crash immediately
- **Resource Cleanup**: Actual cleanup operations (not commented out)
- **System Health Check**: Always start with health verification
- **Modular Design**: Separate functions for each feature group
- **Immediate Failure**: Stop execution on first error

## File Organization

All examples will be placed in the existing `examples/` directory:
