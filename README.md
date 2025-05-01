# MIA Terminal

A simple, powerful CLI tool that converts natural language to shell commands using OpenAI's API.

## Author

Created by Ronny Bruknapp (ronny.bruknapp@digitaltrend.no)

## Features

- 🧠 Convert natural language to shell commands
- 🔑 Secure API key storage
- ⚡ Simple, intuitive interface
- 🚀 Cross-platform compatibility (Linux, macOS, Windows)

## Installation

You can install `mia-terminal` directly from PyPI:

```bash
pip install mia-terminal
```

Or install from source:

```bash
git clone https://github.com/ronnybru/ai-cmd.git
cd ai-cmd
pip install .
```

## Usage

Using `mia` is simple:

```bash
mia <your natural language prompt>
```

For example:

```bash
mia list all files in the current directory sorted by size
```

The tool will:

1. Convert your natural language to a shell command using OpenAI
2. Display the suggested command
3. Execute the command when you press ENTER (or cancel with Ctrl+C)

### First-time Setup

On first use, you'll be prompted to enter your OpenAI API key. This key is stored securely in your home directory and used for all future requests.

## Examples

Here are some examples of what you can do with `mia`:

```bash
# Find large files
mia find files larger than 100MB in my home directory

# Process text
mia count the number of lines in all python files recursively

# System maintenance
mia show me system resource usage sorted by CPU

# Network operations
mia scan open ports on localhost
```

## Configuration

Your OpenAI API key is stored in:

- Linux/macOS: `~/.mia-terminal/config.json`
- Windows: `C:\Users\<username>\.mia-terminal\config.json`

## Requirements

- Python 3.6+
- OpenAI API key (get one at https://platform.openai.com/api-keys)

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request
