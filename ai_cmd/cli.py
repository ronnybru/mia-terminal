#!/usr/bin/env python3
"""
MIA Terminal

This module provides the main CLI functionality for the mia command.
"""

import os
import subprocess
import sys
from pathlib import Path
import getpass
import json

try:
    import openai
except ImportError:
    print("OpenAI package not found. Installing...")
    subprocess.check_call([sys.executable, "-m", "pip", "install", "openai"])
    import openai

# Configuration paths
CONFIG_DIR = Path.home() / ".mia-terminal"
CONFIG_FILE = CONFIG_DIR / "config.json"

def ensure_config_dir():
    """Ensure the configuration directory exists."""
    CONFIG_DIR.mkdir(parents=True, exist_ok=True)

def load_config():
    """Load configuration from file."""
    if not CONFIG_FILE.exists():
        return {}
    
    try:
        with open(CONFIG_FILE, 'r') as f:
            return json.load(f)
    except (json.JSONDecodeError, IOError):
        print("Warning: Config file is corrupted. Creating a new one.")
        return {}

def save_config(config):
    """Save configuration to file."""
    ensure_config_dir()
    with open(CONFIG_FILE, 'w') as f:
        json.dump(config, f)

def get_api_key():
    """Get the OpenAI API key, prompting the user if necessary."""
    config = load_config()
    
    if 'api_key' not in config or not config['api_key']:
        print("\n🔑 OpenAI API Key Setup")
        print("An OpenAI API key is required to use this tool.")
        print("You can get one at: https://platform.openai.com/api-keys")
        print("Your API key will be stored locally at:", CONFIG_FILE)
        
        api_key = getpass.getpass("Enter your OpenAI API key: ").strip()
        
        if not api_key:
            print("❌ No API key provided. Exiting.")
            sys.exit(1)
        
        config['api_key'] = api_key
        save_config(config)
        print("✅ API key saved successfully!")
    
    return config['api_key']

def get_os_type():
    """Determine the operating system type."""
    if sys.platform.startswith('darwin'):
        return "macOS"
    elif sys.platform.startswith('win'):
        return "Windows"
    elif sys.platform.startswith('linux'):
        return "Linux"
    else:
        return "Unknown"

def ask_openai(prompt):
    """Convert natural language to a shell command using OpenAI."""
    api_key = get_api_key()
    client = openai.OpenAI(api_key=api_key)
    
    os_type = get_os_type()
    home_dir = str(Path.home())
    current_dir = os.getcwd()
    
    system_prompt = f"""You are a helpful assistant that converts natural language into shell commands for {os_type}.
Provide ONLY the command with no explanation or markdown formatting.

Important guidelines:
1. When references to standard user directories like 'downloads', 'documents', 'desktop', etc. are made:
   - On macOS: Use '/Users/username/Downloads', '/Users/username/Documents', etc. or '~/Downloads', '~/Documents', etc.
   - On Windows: Use appropriate Windows paths like 'C:\\Users\\username\\Downloads'
   - On Linux: Use '/home/username/Downloads' or '~/Downloads'

2. The user's home directory is: {home_dir}

3. The current working directory is: {current_dir}

4. Always use absolute paths for standard user directories rather than assuming they're relative to the current directory.

5. Ensure the command is appropriate for {os_type} and follows its command syntax.

6. For commands like "open downloads", "open documents", etc., use:
   - On macOS: 'open ~/Downloads', 'open ~/Documents', etc.
   - On Windows: 'start %USERPROFILE%\\Downloads', 'start %USERPROFILE%\\Documents', etc.
   - On Linux: 'xdg-open ~/Downloads', 'xdg-open ~/Documents', etc.
"""
    
    try:
        response = client.chat.completions.create(
            model="gpt-4o",
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": f"Convert this to a shell command: {prompt}"}
            ],
            temperature=0.7,
        )
        return response.choices[0].message.content.strip()
    except Exception as e:
        print(f"❌ Error communicating with OpenAI: {e}")
        sys.exit(1)

def main():
    """Main entry point for the CLI."""
    if len(sys.argv) < 2:
        print("Usage: mia <natural language prompt>")
        print("Example: mia list all files in the current directory sorted by size")
        sys.exit(1)
    
    # Check for --version flag
    if sys.argv[1] == "--version":
        from ai_cmd import __version__
        print(f"mia-terminal version {__version__}")
        sys.exit(0)
    
    prompt = " ".join(sys.argv[1:])
    print(f"🧠 Converting to shell command: {prompt}")
    
    try:
        cmd = ask_openai(prompt)
        print(f"\n💡 Suggested command:\n{cmd}")
        
        confirm = input("\n⚡ Press ENTER to run it, or Ctrl+C to cancel...")
        
        # Execute the command
        subprocess.run(cmd, shell=True)
        
    except KeyboardInterrupt:
        print("\n🛑 Operation cancelled.")
        sys.exit(0)

if __name__ == "__main__":
    main()
