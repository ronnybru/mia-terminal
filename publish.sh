#!/bin/bash
# Script to build and publish the package to PyPI

set -e  # Exit immediately if a command exits with a non-zero status

echo "Building and publishing MIA Terminal (mia-terminal) to PyPI..."

# Check if twine is installed
if ! python3.11 -c "import twine" &> /dev/null; then
    echo "Error: twine is required but not installed."
    echo "Please install twine with: pip3.11 install twine"
    exit 1
fi

# Get the directory of the script
SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" &> /dev/null && pwd )"
cd "$SCRIPT_DIR"

# Clean up previous builds
echo "Cleaning up previous builds..."
rm -rf build/ dist/ *.egg-info/

# Build the package
echo "Building the package..."
python3.11 setup.py sdist bdist_wheel

# Check the package
echo "Checking the package..."
python3.11 -m twine check dist/*

# Ask for confirmation before uploading
echo ""
echo "Package is ready to be uploaded to PyPI."
read -p "Do you want to upload to PyPI? (y/n): " -n 1 -r
echo ""

if [[ $REPLY =~ ^[Yy]$ ]]; then
    # Upload to PyPI
    echo "Uploading to PyPI..."
    python3.11 -m twine upload dist/*
    
    echo ""
    echo "✅ Package successfully published to PyPI!"
    echo "You can now install it with: pip install mia-terminal"
else
    echo "Upload cancelled."
    echo "You can upload manually with: python3.11 -m twine upload dist/*"
fi
