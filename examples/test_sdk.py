#!/usr/bin/env python3
"""
Test script for mix-python-sdk
"""

import os
import sys
from mix_python_sdk import Mix
from mix_python_sdk import errors

def test_sdk():
    """Test basic SDK functionality"""
    print("Testing mix-python-sdk...")
    print(f"Python version: {sys.version}")
    
    # You can set a custom server URL if needed
    # server_url = os.getenv("MIX_SERVER_URL", "http://localhost:8088")
    # mix = Mix(server_url=server_url)
    
    try:
        with Mix() as mix:
            print("\n1. Testing system health")
            try:
                health = mix.system.get_health()
                print(f"✓ Health check successful: {health}")
            except errors.MixError as e:
                print(f"✗ Health check failed: {e.message} (Status: {e.status_code})")
            
            print("\n2. Testing authentication status")
            try:
                auth_status = mix.authentication.get_auth_status()
                print(f"✓ Auth status: {auth_status}")
            except errors.MixError as e:
                print(f"✗ Auth status check failed: {e.message} (Status: {e.status_code})")
            
            print("\n3. Testing available providers")
            try:
                providers = mix.preferences.get_available_providers()
                print(f"✓ Available providers: {providers}")
            except errors.MixError as e:
                print(f"✗ Failed to get providers: {e.message} (Status: {e.status_code})")
            
            print("\n4. Testing session creation")
            try:
                session = mix.sessions.create(title="SDK Test Session")
                print(f"✓ Created session: {session.id}")
                
                print("\n5. Testing message sending")
                try:
                    response = mix.messages.send(id=session.id, content="Hello from mix-python-sdk test!")
                    print(f"✓ Message sent, response: {response}")
                except errors.MixError as e:
                    print(f"✗ Failed to send message: {e.message} (Status: {e.status_code})")
                
                print("\n6. Testing session messages listing")
                try:
                    messages = mix.messages.list_session(id=session.id)
                    message_count = len(messages) if messages else 0
                    print(f"✓ Session has {message_count} messages")
                except errors.MixError as e:
                    print(f"✗ Failed to list messages: {e.message} (Status: {e.status_code})")
                
                print("\n7. Testing session deletion")
                try:
                    mix.sessions.delete(id=session.id)
                    print(f"✓ Deleted session: {session.id}")
                except errors.MixError as e:
                    print(f"✗ Failed to delete session: {e.message} (Status: {e.status_code})")
                    
            except errors.MixError as e:
                print(f"✗ Failed to create session: {e.message} (Status: {e.status_code})")
    
    except Exception as e:
        print(f"❌ Test failed with error: {str(e)}")
        return False
    
    print("\n✅ All tests completed")
    return True

if __name__ == "__main__":
    success = test_sdk()
    sys.exit(0 if success else 1)