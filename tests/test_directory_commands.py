#!/usr/bin/env python3
"""
Test script for directory commands in mia-terminal.

This script tests the enhanced system prompt's ability to handle
standard user directory references correctly.
"""

import sys
import os
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent.parent))

from ai_cmd.cli import get_os_type, ask_openai

def test_directory_commands():
    """Test various directory commands to ensure they use absolute paths."""
    os_type = get_os_type()
    home_dir = str(Path.home())
    
    print(f"Testing on {os_type} with home directory: {home_dir}")
    print(f"Current working directory: {os.getcwd()}")
    print("\nTesting directory commands...")
    
    test_commands = [
        "open downloads",
        "open documents folder",
        "show me my desktop",
        "list files in downloads",
    ]
    
    for cmd in test_commands:
        print(f"\nTesting: '{cmd}'")
        try:
            result = ask_openai(cmd)
            print(f"Result: '{result}'")
            
            # Check if the result contains an absolute path or tilde reference
            if "~/" in result or home_dir in result:
                print("✅ Command uses absolute path or tilde reference")
            else:
                print("❌ Command does not use absolute path")
        except Exception as e:
            print(f"Error: {e}")

if __name__ == "__main__":
    test_directory_commands()
