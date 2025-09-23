# Mix Python SDK Examples Plan

This document outlines the comprehensive plan for creating minimal examples for each SDK module directory in `docs/sdks/`. Each example will showcase all functionality available in that specific module.

## Overview

Based on analysis of the SDK documentation and existing examples, we will create **8 separate test files** in the `examples/` directory, each demonstrating the complete functionality of one SDK module. Use only the openrouter LLM provider, with the OPENROUTER_API_KEY. Don't use any other provider

## Example Files to Create

### 1. `examples/authentication_example.py`

**Documentation Reference**: `docs/sdks/authentication/README.md`

**Purpose**: Demonstrate comprehensive authentication management

**Functionality to showcase:**

- OAuth flow initiation and callback handling (Anthropic provider only)
- Authentication status checking across all providers
- Preferred provider validation
- Credential deletion and cleanup operations

**Key operations demonstrated:**

- `store_api_key()` - Provider-specific API key storage
- `start_o_auth_flow()` - Provider-specific OAuth flow (Anthropic only)
- `handle_o_auth_callback()` - OAuth callback processing
- `get_auth_status()` - Authentication status checking
- `validate_preferred_provider()` - Preferred provider validation
- `delete_credentials()` - Credential cleanup

### 2. `examples/files_example.py`

**Documentation Reference**: `docs/sdks/files/README.md`

**Purpose**: Demonstrate comprehensive file management within sessions

**Functionality to showcase:**

- File upload operations with different content types (text, image, binary)
- File listing with metadata display and filtering
- Thumbnail generation and retrieval for images
- File download with various options and error handling
- Session-based file isolation and management
- File deletion and cleanup operations

**Key operations demonstrated:**

- `upload()` - Upload files to sessions with content type handling
- `list()` - List session files with metadata
- `get()` - Retrieve specific file details and download
- `delete()` - Remove files from sessions
- Thumbnail generation workflows
- Error handling for file operations

**Sample Files Required:**

- Uses real sample files from `examples/sample_files/` directory
- Required files: `sample.txt` (any text content) and `sample.jpg/png` (any image file)
- Example raises `FileNotFoundError` if sample files are missing

### 3. `examples/messages_example.py`

**Documentation Reference**: `docs/sdks/messages/README.md`

**Purpose**: Demonstrate comprehensive messaging functionality

**Functionality to showcase:**

- Global message history retrieval with pagination support
- Session-specific message listing and filtering
- Interactive message sending with AI response handling
- Tool integration during conversations
- Message metadata analysis (reasoning, tool calls, tokens)
- Conversation continuity and context management

**Key operations demonstrated:**

- `get_history()` - Global message history with pagination
- `list_session()` - Session-specific message retrieval
- `send()` - Message sending with response handling
- Message structure analysis (roles, tool calls, reasoning)
- Conversation flow management

### 4. `examples/permissions_example.py`

**Documentation Reference**: `docs/sdks/permissions/README.md`

**Purpose**: Demonstrate permission management operations

**Functionality to showcase:**

- Permission granting operations with ID-based management
- Permission denial operations with proper response handling
- Error handling for invalid permission IDs and authentication
- Both synchronous and asynchronous operation patterns
- Response validation and status checking

**Key operations demonstrated:**

- `grant()` - Grant specific permissions by ID
- `deny()` - Deny specific permissions by ID
- `grant_async()` - Asynchronous permission granting
- `deny_async()` - Asynchronous permission denial
- Error handling for 401, 404, and 500 responses

### 5. `examples/preferences_example.py` (Enhanced)

**Documentation Reference**: `docs/sdks/preferencessdk/README.md`

**Purpose**: Demonstrate comprehensive preference management

**Functionality to showcase:**

- Available provider and model discovery
- Current preference retrieval and analysis
- Dual-agent configuration (main agent vs sub agent)
- Model selection, token limits, and reasoning effort settings
- Preference reset functionality
- Provider switching workflows and validation

**Key operations demonstrated:**

- `get_available_providers()` - Provider and model discovery
- `get_preferences()` - Current preference retrieval
- `update_preferences()` - Comprehensive preference configuration
- `reset_preferences()` - Reset to default settings
- Dual-agent architecture configuration

### 6. `examples/sessions_example.py` (Enhanced)

**Documentation Reference**: `docs/sdks/sessions/README.md`

**Purpose**: Demonstrate comprehensive session lifecycle management

**Functionality to showcase:**

- Complete session lifecycle (create, get, list, delete)
- Session forking with message index specification
- Processing cancellation for long-running operations
- Session metadata and usage statistics analysis
- Working directory management and isolation
- Session cleanup and resource management

**Key operations demonstrated:**

- `list()` - List all sessions with metadata
- `create()` - Create new sessions with configuration
- `get()` - Retrieve specific session details
- `delete()` - Session deletion and cleanup
- `fork()` - Session branching with message history
- `cancel_processing()` - Cancel ongoing operations

### 7. `examples/system_example.py`

**Documentation Reference**: `docs/sdks/system/README.md`

**Purpose**: Demonstrate system operations and health monitoring

**Functionality to showcase:**

- Health check and system status monitoring
- Command discovery and detailed command inspection
- MCP (Model Context Protocol) server listing and tool ecosystem status
- Integration readiness verification
- System introspection and capability discovery

**Key operations demonstrated:**

- `get_health()` - System health monitoring
- `list_commands()` - Available command discovery
- `get_command()` - Detailed command inspection
- `list_mcp_servers()` - MCP server and tool ecosystem status
- System integration verification workflows

### 8. `examples/tools_example.py`

**Documentation Reference**: `docs/sdks/tools/README.md`

**Purpose**: Demonstrate tools management and credential handling

**Functionality to showcase:**

- Tools status discovery and authentication checking
- Tool credential storage for different providers (Brave, Gemini)
- Tool type management (web_search, multimodal_analyzer)
- Credential deletion and cleanup operations
- Authentication verification workflows

**Key operations demonstrated:**

- `get_tools_status()` - Tool availability and authentication status
- `store_tool_credentials()` - Provider credential storage
- `delete_tool_credentials()` - Credential cleanup
- Tool authentication verification and management

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
    if hasattr(result, '__dict__'):
        print("\nDetailed breakdown:")
        for key, value in result.__dict__.items():
            print(f"  {key}: {value}")
```

#### 7. Main Function Template (UPDATED)

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
- **Detailed breakdowns**: Use `hasattr(result, '__dict__')` to show object details
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

### Common Patterns (UPDATED)

Each example file will follow these established patterns:

- **Environment Loading**: `load_dotenv()` and API key validation at start
- **Real Credentials**: Load actual API keys from `.env`, never use demo keys
- **Context Manager Usage**: `with Mix(server_url=server_url) as mix:`
- **Zero Error Handling**: NO try/catch blocks - let ALL errors crash immediately
- **Resource Cleanup**: Actual cleanup operations (not commented out)
- **System Health Check**: Always start with health verification
- **Modular Design**: Separate functions for each feature group
- **Immediate Failure**: Stop execution on first error

## Usage Scenarios

### For Developers

- **Learning Tool**: Progressive complexity from basic to advanced operations
- **Reference Implementation**: Production-ready patterns and best practices
- **Integration Guide**: Complete examples for each SDK module

### For Testing

- **Functionality Verification**: Ensure all SDK operations work correctly
- **Integration Testing**: Validate SDK behavior with the Mix platform
- **Regression Testing**: Detect issues when SDK or platform changes

### For Documentation

- **API Examples**: Complete, runnable code snippets
- **Feature Coverage**: Demonstrate all available functionality
- **Best Practices**: Show recommended usage patterns

## File Organization

All examples will be placed in the existing `examples/` directory:

```
examples/
├── authentication_example.py    # Authentication & credential management
├── files_example.py            # File operations within sessions
├── messages_example.py         # Messaging and conversation management
├── permissions_example.py      # Permission granting and denial
├── preferences_example.py      # User preference configuration
├── sessions_example.py         # Session lifecycle management
├── system_example.py          # System health and command discovery
└── tools_example.py           # Tools management and credentials
```

## Success Criteria (UPDATED)

Each example file should:

- ✅ Demonstrate ALL operations available in its respective SDK module
- ✅ **NO error handling** - let all errors crash immediately
- ✅ Load real credentials from environment variables using `python-dotenv`
- ✅ Validate environment setup before execution
- ✅ Follow established SDK patterns and conventions
- ✅ Provide clear, informative output
- ✅ Use actual API operations, not demo/placeholder calls
- ✅ Serve as both learning tool and reference implementation

This plan ensures complete coverage of the Mix Python SDK functionality while maintaining consistency and providing valuable learning resources for developers.
