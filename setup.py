from setuptools import setup, find_packages
import os
import re

# Read version from __init__.py
with open("ai_cmd/__init__.py", "r", encoding="utf-8") as f:
    version_match = re.search(r'__version__\s*=\s*["\']([^"\']+)["\']', f.read())
    version = version_match.group(1) if version_match else "0.1.0"

# Read the long description from README.md
with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="mia-terminal",
    version=version,
    author="Ronny Bruknapp",
    author_email="ronny.bruknapp@digitaltrend.no",
    description="A CLI tool that converts natural language to shell commands using OpenAI's API",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/ronnybru/ai-cmd",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
    install_requires=[
        "openai>=1.0.0",
    ],
    entry_points={
        "console_scripts": [
            "mia=ai_cmd.cli:main",
        ],
    },
)
