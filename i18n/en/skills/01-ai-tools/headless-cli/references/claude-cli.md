Here is the English translation of the Markdown document:

# Claude Code CLI Parameter Reference

> Source: [Official Documentation](https://docs.anthropic.com/en/docs/claude-code/cli-reference)

## Installation

```bash
npm install -g @anthropic-ai/claude-code
```

## Authentication

Requires an Anthropic API Key or Claude Pro/Max subscription:
```bash
export ANTHROPIC_API_KEY="YOUR_API_KEY"
```

## Core Commands

| Command | Description | Example |
|:---|:---|:---|
| `claude` | Starts an interactive REPL | `claude` |
| `claude "query"` | Starts with an initial prompt | `claude "explain this"` |
| `claude -p "query"` | Print mode, exits after execution | `claude -p "review code"` |
| `claude -c` | Continues the most recent conversation | `claude -c` |
| `claude -c -p "query"` | Continues conversation (Print mode) | `claude -c -p "run tests"` |
| `claude -r "id" "query"` | Resumes a specified session | `claude -r "abc123" "continue"` |
| `claude update` | Updates to the latest version | `claude update` |
| `claude mcp` | Configures the MCP server | `claude mcp add server` |

## CLI Parameters

| Parameter | Description | Example |
|:---|:---|:---|
| `--model` | Specifies the model | `--model claude-sonnet-4` |
| `--output-format` | Output format: `text`/`json`/`stream-json` | `--output-format json` |
| `--max-turns` | Limits the number of conversation turns | `--max-turns 3` |
| `--dangerously-skip-permissions` | Skips all permission confirmations (YOLO) | See below |
| `--allowedTools` | List of allowed tools | `--allowedTools "Write" "Bash(git *)"` |
| `--disallowedTools` | List of disallowed tools | `--disallowedTools "Bash(rm *)"` |
| `--add-dir` | Adds additional working directories | `--add-dir ./apps ./lib` |
| `--verbose` | Enables detailed logs | `--verbose` |
| `--continue` | Continues the recent conversation | `--continue` |
| `--resume` | Resumes a specified session | `--resume abc123` |

## Available Models

- `claude-sonnet-4` - Balanced model (default)
- `claude-opus-4` - Most powerful model
- `claude-opus-4.5` - Latest and most powerful

## Headless Mode Usage

```bash
# Print mode (non-interactive, exits after execution)
claude -p "review this code" --output-format text

# Piped input
cat input.txt | claude -p "explain these errors"

# YOLO mode (skips all permission confirmations)
claude --dangerously-skip-permissions "Your prompt"

# Alias setup
alias cc='claude --dangerously-skip-permissions'

# Continue conversation + Print mode (suitable for scripts)
claude -c -p "show progress"
```

## Interactive Commands (Slash Commands)

| Command | Description |
|:---|:---|
| `/help` | Displays all commands |
| `/config` | Configures settings |
| `/allowed-tools` | Configures tool permissions |
| `/mcp` | Manages MCP servers |
| `/vim` | Enables vim editing mode |

## Configuration Files

- User settings: `~/.claude/settings.json`
- Project settings: `.claude/settings.json`
- Local settings: `.claude/settings.local.json`

```json
{
  "model": "claude-sonnet-4",
  "permissions": {
    "allowedTools": ["Read", "Write", "Bash(git *)"],
    "deny": ["Read(./.env)", "Bash(rm *)"]
  }
}
```

## Context Files (CLAUDE.md)

- Global: `~/.claude/CLAUDE.md`
- Project: `./CLAUDE.md`
- Subdirectory: Component-specific instructions

## Deep Thinking Trigger Words

Increasing intensity:
- `think` - Basic thinking
- `think hard` - Deep thinking
- `think harder` - Deeper thinking
- `ultrathink` - Deepest thinking

## Common Issues

1.  **Permission pop-ups**: Use `--dangerously-skip-permissions`
2.  **Context too long**: Use `/compact` or `/clear`
3.  **Reverting changes**: Use `/rewind`
