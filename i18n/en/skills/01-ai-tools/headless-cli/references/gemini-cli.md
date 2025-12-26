Here's the English translation of the provided Markdown document:

# Gemini CLI Parameter Reference

> Source: [Official Documentation](https://geminicli.com/docs/get-started/configuration/)

## Installation

```bash
npm install -g @anthropic-ai/gemini-cli
```

## Authentication

The first run will guide you through Google account login, or you can set environment variables:
```bash
export GEMINI_API_KEY="YOUR_API_KEY"
```

## Core Command Line Parameters

| Parameter | Description | Example |
|:---|:---|:---|
| `--model <model>` | Specify model | `--model gemini-2.5-flash` |
| `--yolo` | YOLO mode, automatically approve all tool calls | `gemini --yolo` |
| `--approval-mode <mode>` | Approval mode: `default`/`auto_edit`/`yolo` | `--approval-mode auto_edit` |
| `--allowed-tools <tools>` | List of allowed tools (comma separated) | `--allowed-tools ''` (disable all) |
| `--output-format <format>` | Output format: `text`/`json`/`stream-json` | `--output-format text` |
| `--sandbox` / `-s` | Enable sandbox mode | `gemini -s` |
| `--prompt <prompt>` / `-p` | Non-interactive mode, pass prompt directly | `gemini -p "query"` |
| `--prompt-interactive <prompt>` / `-i` | Interactive mode with initial prompt | `gemini -i "explain"` |
| `--debug` / `-d` | Enable debug mode | `gemini -d` |

## Available Models

- `gemini-2.5-flash` - Fast model
- `gemini-2.5-pro` - Advanced model
- `gemini-3-flash-preview` - Latest Flash
- `gemini-3-pro-preview` - Latest Pro

## Headless Mode Usage

```bash
# Basic headless call (piped input)
cat input.txt | gemini -p "Your prompt" --output-format text

# Disable tool calls (plain text output)
cat input.txt | gemini -p "Your prompt" --output-format text --allowed-tools ''

# YOLO mode (skip all confirmations)
gemini --yolo "Your prompt"

# Or use approval-mode
gemini --approval-mode yolo "Your prompt"
```

## Configuration File

Configuration is stored in `~/.gemini/settings.json` or project `.gemini/settings.json`:

```json
{
  "security": {
    "disableYoloMode": false
  },
  "model": {
    "name": "gemini-2.5-flash"
  }
}
```

## Proxy Configuration

```bash
export http_proxy=http://127.0.0.1:9910
export https_proxy=http://127.0.0.1:9910
```

## Frequently Asked Questions

1.  **MCP initialization is slow**: Use `--allowed-tools ''` to skip.
2.  **Timeout**: Use the `timeout` command wrapper.
3.  **Output includes logs**: Redirect stderr `2>/dev/null`.
