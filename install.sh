#!/bin/bash
# Installation script for mia-terminal

set -e  # Exit immediately if a command exits with a non-zero status

echo "Installing MIA Terminal..."

# Check if Python is installed
if ! command -v python3 &> /dev/null; then
    echo "Error: Python 3 is required but not installed."
    echo "Please install Python 3 and try again."
    exit 1
fi

# Check Python version
PYTHON_VERSION=$(python3 -c 'import sys; print(f"{sys.version_info.major}.{sys.version_info.minor}")')
REQUIRED_VERSION="3.6"

if [ "$(printf '%s\n' "$REQUIRED_VERSION" "$PYTHON_VERSION" | sort -V | head -n1)" != "$REQUIRED_VERSION" ]; then
    echo "Error: Python $REQUIRED_VERSION or higher is required."
    echo "Current version: $PYTHON_VERSION"
    exit 1
fi

# Check if pip is installed
if ! command -v pip3 &> /dev/null; then
    echo "Error: pip3 is required but not installed."
    echo "Please install pip3 and try again."
    exit 1
fi

# Get the directory of the script
SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" &> /dev/null && pwd )"

echo "Installing from directory: $SCRIPT_DIR"

# Install the package
echo "Installing package..."
pip3 install -e "$SCRIPT_DIR"

# Check if installation was successful
if [ $? -eq 0 ]; then
    echo ""
    echo "✅ Installation successful!"
    echo ""
    echo "You can now use mia by running:"
    echo "  mia <your natural language prompt>"
    echo ""
    echo "Example:"
    echo "  mia list all files in the current directory sorted by size"
    echo ""
    echo "On first use, you'll be prompted to enter your OpenAI API key."
else
    echo "❌ Installation failed."
    exit 1
fi
