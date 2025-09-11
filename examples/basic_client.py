#!/usr/bin/env python3
"""
Basic usage example for mix-python-sdk
"""

from mix_python_sdk import Mix
import os

def main():
    server_url = os.getenv("MIX_SERVER_URL", "http://localhost:8088")
    
    with Mix(server_url=server_url) as mix:
        try:
            # Check health
            health = mix.system.get_health()
            print(f"Health: {health}")

            # List sessions
            sessions = mix.sessions.list()
            print(f"Sessions: {len(sessions) if sessions else 0}")
            
            # Create new session
            session = mix.sessions.create(title="Test Session")
            print(f"Created session: {session.id if session else 'No session data'}")

            # Send hello message
            if session:
                response = mix.messages.send(id=session.id, content = "Hello")
                print(f"Message response: {response}")
                
                # Delete the session
                mix.sessions.delete(id=session.id)
                print(f"Deleted session: {session.id}")
            else:
                print("No session data available to send message")
            
        except Exception as e:
            print(f"Error: {e}")

if __name__ == "__main__":
    main()