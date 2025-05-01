#!/usr/bin/env python3
"""
Basic test for the mia-terminal package.

This script demonstrates how to use the mia-terminal package programmatically.
"""

import sys
import os

# Add the parent directory to the path so we can import the package
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from ai_cmd.cli import ask_openai

def test_ask_openai():
    """Test the ask_openai function."""
    print("Testing ask_openai function...")
    
    # This will prompt for an API key if not already configured
    prompt = "list all files in the current directory"
    
    try:
        command = ask_openai(prompt)
        print(f"Prompt: {prompt}")
        print(f"Generated command: {command}")
        print("Test successful!")
        return True
    except Exception as e:
        print(f"Test failed: {e}")
        return False

if __name__ == "__main__":
    print("Running basic test for mia-terminal package...")
    success = test_ask_openai()
    
    if success:
        print("\nAll tests passed!")
        sys.exit(0)
    else:
        print("\nTests failed!")
        sys.exit(1)
