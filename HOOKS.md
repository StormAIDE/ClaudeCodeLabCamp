# Claude Code Hooks Guide

This guide demonstrates how to use hooks to automate workflows in the ClaudeCode Labcamp project. Hooks are shell commands that run automatically at specific points in Claude Code's lifecycle.

## What Are Hooks?

Hooks let you:
- **Auto-format** code after every file edit
- **Block** dangerous commands before they run
- **Get notified** when Claude needs your input
- **Inject context** into Claude's conversation
- **Validate** changes before they're committed
- **Automate** repetitive tasks

Think of hooks as event listeners that trigger shell scripts at key moments.

---

## Quick Start: Your First Hook

Let's add a desktop notification hook so you know when Claude is waiting for you.

### 1. Create the hook configuration

Edit `~/.claude/settings.json` (create it if it doesn't exist):

```json
{
  "hooks": {
    "Notification": [
      {
        "matcher": "",
        "hooks": [
          {
            "type": "command",
            "command": "osascript -e 'display notification \"Claude Code needs your attention\" with title \"Claude Code\"'"
          }
        ]
      }
    ]
  }
}
```

**For Linux users:**
```json
{
  "hooks": {
    "Notification": [
      {
        "matcher": "",
        "hooks": [
          {
            "type": "command",
            "command": "notify-send 'Claude Code' 'Claude Code needs your attention'"
          }
        ]
      }
    ]
  }
}
```

### 2. Test it

Run Claude Code and ask it to do something that requires permission. Switch to another window. You should get a notification!

### 3. View your hooks

Type `/hooks` in Claude Code to see all configured hooks.

---

## Hook Lifecycle Events

Hooks trigger at specific points in Claude Code's workflow:

| Event | When It Fires | Common Use Cases |
|-------|---------------|------------------|
| `SessionStart` | Session begins or resumes | Load environment, inject context |
| `UserPromptSubmit` | Before Claude processes your prompt | Validate input, add context |
| `PreToolUse` | Before a tool executes | Block dangerous commands, validate |
| `PostToolUse` | After a tool succeeds | Format code, run tests, log activity |
| `PermissionRequest` | Permission dialog appears | Auto-approve safe commands |
| `Stop` | Claude finishes responding | Verify completeness, run checks |
| `CwdChanged` | Directory changes | Reload environment (direnv) |
| `FileChanged` | Watched file changes | React to .env or config changes |
| `ConfigChange` | Settings file modified | Audit configuration changes |
| `SessionEnd` | Session terminates | Clean up temp files |

Full list: https://code.claude.com/docs/en/hooks#hook-lifecycle

---

## Recommended Hooks for This Project

### 1. Auto-Format Code After Edits

Automatically run Prettier on every file Claude edits.

**File:** `.claude/settings.json` (project-level)

```json
{
  "hooks": {
    "PostToolUse": [
      {
        "matcher": "Edit|Write",
        "hooks": [
          {
            "type": "command",
            "command": "jq -r '.tool_input.file_path' | xargs npx prettier --write"
          }
        ]
      }
    ]
  }
}
```

**What it does:**
- Triggers after `Edit` or `Write` tool calls
- Extracts the file path from the hook input
- Runs Prettier on that file
- Ensures consistent code formatting automatically

**Educational value:**
- Shows post-processing automation
- Demonstrates JSON parsing with `jq`
- Teaches pipe-based command composition

---

### 2. Run Tests After Code Changes

Automatically run tests after Claude modifies Python or TypeScript files.

**File:** `.claude/settings.json`

```json
{
  "hooks": {
    "PostToolUse": [
      {
        "matcher": "Edit|Write",
        "hooks": [
          {
            "type": "command",
            "command": "\"$CLAUDE_PROJECT_DIR\"/.claude/hooks/run-tests.sh"
          }
        ]
      }
    ]
  }
}
```

**Create the script:** `.claude/hooks/run-tests.sh`

```bash
#!/bin/bash
set -e

INPUT=$(cat)
FILE_PATH=$(echo "$INPUT" | jq -r '.tool_input.file_path // empty')

# Only run tests for Python or TypeScript files
if [[ "$FILE_PATH" =~ \.(py|ts|tsx)$ ]]; then
  echo "Running tests after modifying $FILE_PATH..." >&2
  
  # Backend tests for Python files
  if [[ "$FILE_PATH" =~ \.py$ ]]; then
    cd "$CLAUDE_PROJECT_DIR"
    source claudecodeenv/bin/activate
    python -m pytest backend/tests/ -v --tb=short || echo "Tests failed" >&2
  fi
  
  # Frontend tests for TypeScript files
  if [[ "$FILE_PATH" =~ \.(ts|tsx)$ ]]; then
    cd "$CLAUDE_PROJECT_DIR/frontend"
    npm test -- --run || echo "Tests failed" >&2
  fi
fi

exit 0
```

**Make it executable:**
```bash
chmod +x .claude/hooks/run-tests.sh
```

**Educational value:**
- Continuous testing workflow
- File extension filtering with regex
- Conditional test execution

---

### 3. Block Dangerous Commands

Prevent Claude from running potentially destructive commands.

**File:** `.claude/settings.json`

```json
{
  "hooks": {
    "PreToolUse": [
      {
        "matcher": "Bash",
        "hooks": [
          {
            "type": "command",
            "command": "\"$CLAUDE_PROJECT_DIR\"/.claude/hooks/block-dangerous.sh"
          }
        ]
      }
    ]
  }
}
```

**Create the script:** `.claude/hooks/block-dangerous.sh`

```bash
#!/bin/bash

INPUT=$(cat)
COMMAND=$(echo "$INPUT" | jq -r '.tool_input.command // empty')

# List of dangerous patterns
DANGEROUS_PATTERNS=(
  "rm -rf /"
  "rm -rf ~"
  "dd if="
  "> /dev/sda"
  "mkfs"
  ":(){ :|:& };:"  # Fork bomb
  "curl.*|.*bash"  # Pipe to bash
  "wget.*|.*sh"    # Pipe to shell
)

for pattern in "${DANGEROUS_PATTERNS[@]}"; do
  if echo "$COMMAND" | grep -qE "$pattern"; then
    echo "BLOCKED: Command matches dangerous pattern '$pattern'" >&2
    echo "Command was: $COMMAND" >&2
    exit 2  # Exit 2 = block the command
  fi
done

exit 0  # Exit 0 = allow the command
```

**Make it executable:**
```bash
chmod +x .claude/hooks/block-dangerous.sh
```

**Educational value:**
- Security-first development
- Pattern matching for validation
- Exit codes for control flow (0=allow, 2=block)

---

### 4. Protect Sensitive Files

Prevent Claude from editing `.env` files, lock files, and git internals.

**File:** `.claude/settings.json`

```json
{
  "hooks": {
    "PreToolUse": [
      {
        "matcher": "Edit|Write",
        "hooks": [
          {
            "type": "command",
            "command": "\"$CLAUDE_PROJECT_DIR\"/.claude/hooks/protect-files.sh"
          }
        ]
      }
    ]
  }
}
```

**Create the script:** `.claude/hooks/protect-files.sh`

```bash
#!/bin/bash

INPUT=$(cat)
FILE_PATH=$(echo "$INPUT" | jq -r '.tool_input.file_path // empty')

# Protected file patterns
PROTECTED_PATTERNS=(
  ".env"
  ".env.local"
  "package-lock.json"
  "yarn.lock"
  "poetry.lock"
  ".git/"
  "node_modules/"
  "claudecodeenv/"
)

for pattern in "${PROTECTED_PATTERNS[@]}"; do
  if [[ "$FILE_PATH" == *"$pattern"* ]]; then
    echo "BLOCKED: $FILE_PATH is protected (matches pattern: $pattern)" >&2
    echo "This file should not be modified by automation." >&2
    exit 2  # Block the edit
  fi
done

exit 0  # Allow the edit
```

**Make it executable:**
```bash
chmod +x .claude/hooks/protect-files.sh
```

**Educational value:**
- Demonstrates file protection strategies
- Shows how to safeguard sensitive files
- Teaches pattern matching on file paths

---

### 5. Log All Commands

Keep a record of every command Claude runs for auditing.

**File:** `.claude/settings.json`

```json
{
  "hooks": {
    "PostToolUse": [
      {
        "matcher": "Bash",
        "hooks": [
          {
            "type": "command",
            "command": "jq -r '{timestamp: now | todate, cwd: .cwd, command: .tool_input.command}' >> ~/.claude/command-log.jsonl"
          }
        ]
      }
    ]
  }
}
```

**What it does:**
- Logs every Bash command with timestamp and working directory
- Uses JSONL format (JSON Lines) for easy parsing
- Stores in `~/.claude/command-log.jsonl`

**View the log:**
```bash
# Show last 10 commands
tail -10 ~/.claude/command-log.jsonl | jq .

# Filter by directory
grep "ClaudeCodeTest" ~/.claude/command-log.jsonl | jq .
```

**Educational value:**
- Audit trails for security and debugging
- JSONL format for streaming logs
- `jq` for JSON transformation

---

### 6. Inject Project Context on Session Start

Remind Claude of project-specific rules every time a session starts.

**File:** `.claude/settings.json`

```json
{
  "hooks": {
    "SessionStart": [
      {
        "matcher": "",
        "hooks": [
          {
            "type": "command",
            "command": "cat \"$CLAUDE_PROJECT_DIR\"/.claude/hooks/project-context.txt"
          }
        ]
      }
    ]
  }
}
```

**Create the context file:** `.claude/hooks/project-context.txt`

```text
📋 Project Context Reminder:

1. **Always run tests before committing:**
   - Backend: source claudecodeenv/bin/activate && python -m pytest backend/tests/
   - Frontend: cd frontend && npm test -- --run

2. **Ports are fixed:**
   - Backend: 8000 (never change)
   - Frontend: 5173 (never change)

3. **Commit format:**
   - Use conventional commits: feat:, fix:, chore:, docs:, test:
   - Example: "feat: add user authentication endpoint"

4. **Files to never modify:**
   - .env (credentials)
   - package-lock.json, poetry.lock (managed by package managers)
   - claudecodeenv/ (Python virtual environment)

5. **Current focus:**
   - Implementing plugin system for educational demo
   - All changes must have test coverage
```

**Educational value:**
- Context injection for consistency
- Project-specific best practices
- Reminds AI of important constraints

---

### 7. Verify All Tests Pass Before Stopping

Ensure Claude doesn't finish until all tests pass.

**File:** `.claude/settings.json`

```json
{
  "hooks": {
    "Stop": [
      {
        "hooks": [
          {
            "type": "agent",
            "prompt": "Verify that all tests pass before stopping. Run: 'source claudecodeenv/bin/activate && python -m pytest backend/tests/ -v' for backend and 'cd frontend && npm test -- --run' for frontend. If any tests fail, respond with {\"ok\": false, \"reason\": \"Tests are failing: <details>\"}. If all pass, respond with {\"ok\": true}.",
            "timeout": 120
          }
        ]
      }
    ]
  }
}
```

**What it does:**
- Uses an agent hook (can run commands and read files)
- Runs full test suite
- Blocks Claude from stopping if tests fail
- Continues working to fix the failures

**Educational value:**
- Quality gates in automation
- Agent-based verification (not just simple scripts)
- Test-driven development enforcement

---

## Hook Configuration Examples

### Project-Level Hooks (Shared with Team)

**File:** `.claude/settings.json`

```json
{
  "hooks": {
    "PostToolUse": [
      {
        "matcher": "Edit|Write",
        "hooks": [
          {
            "type": "command",
            "command": "jq -r '.tool_input.file_path' | xargs npx prettier --write"
          }
        ]
      }
    ],
    "PreToolUse": [
      {
        "matcher": "Bash",
        "hooks": [
          {
            "type": "command",
            "command": "\"$CLAUDE_PROJECT_DIR\"/.claude/hooks/block-dangerous.sh"
          }
        ]
      },
      {
        "matcher": "Edit|Write",
        "hooks": [
          {
            "type": "command",
            "command": "\"$CLAUDE_PROJECT_DIR\"/.claude/hooks/protect-files.sh"
          }
        ]
      }
    ]
  }
}
```

### User-Level Hooks (Personal Preferences)

**File:** `~/.claude/settings.json`

```json
{
  "hooks": {
    "Notification": [
      {
        "matcher": "",
        "hooks": [
          {
            "type": "command",
            "command": "osascript -e 'display notification \"Claude Code needs your attention\" with title \"Claude Code\"'"
          }
        ]
      }
    ],
    "PostToolUse": [
      {
        "matcher": "Bash",
        "hooks": [
          {
            "type": "command",
            "command": "jq -r '{timestamp: now | todate, cwd: .cwd, command: .tool_input.command}' >> ~/.claude/command-log.jsonl"
          }
        ]
      }
    ]
  }
}
```

---

## Understanding Hook Input/Output

### Input Format (stdin)

Every hook receives JSON on stdin with event-specific data:

```json
{
  "session_id": "abc123",
  "cwd": "/Users/student/ClaudeCodeTest",
  "hook_event_name": "PreToolUse",
  "tool_name": "Bash",
  "tool_input": {
    "command": "npm test"
  }
}
```

**Parse it with `jq`:**
```bash
INPUT=$(cat)
COMMAND=$(echo "$INPUT" | jq -r '.tool_input.command')
FILE_PATH=$(echo "$INPUT" | jq -r '.tool_input.file_path')
```

### Output Format (exit codes)

Your script's exit code determines what happens next:

| Exit Code | Meaning | Use Case |
|-----------|---------|----------|
| `0` | Allow/Proceed | Command is safe, let it run |
| `2` | Block/Deny | Command is dangerous, block it |
| Other | Error (but proceed) | Hook failed, but allow action |

**Write feedback to stderr:**
```bash
echo "BLOCKED: This command is not allowed" >&2
exit 2
```

**Inject context (stdout):**
```bash
echo "Remember to run tests before committing"
exit 0
```

### Structured JSON Output

For more control, output JSON instead of using exit codes:

```bash
#!/bin/bash
INPUT=$(cat)
COMMAND=$(echo "$INPUT" | jq -r '.tool_input.command')

if echo "$COMMAND" | grep -q "rm -rf"; then
  cat <<EOF
{
  "hookSpecificOutput": {
    "hookEventName": "PreToolUse",
    "permissionDecision": "deny",
    "permissionDecisionReason": "Dangerous command detected: $COMMAND"
  }
}
EOF
  exit 0
fi

exit 0
```

---

## Hook Matchers

Matchers filter when hooks run. Without a matcher, the hook fires on every event.

### Tool Name Matchers

```json
{
  "matcher": "Bash",           // Only Bash commands
  "matcher": "Edit|Write",     // Edit OR Write tools
  "matcher": "mcp__.*",        // All MCP tools
  "matcher": ".*"              // All tools (use sparingly)
}
```

### Event-Specific Matchers

| Event | Matcher Field | Example Values |
|-------|---------------|----------------|
| `SessionStart` | Session source | `startup`, `resume`, `clear`, `compact` |
| `SessionEnd` | End reason | `clear`, `logout`, `prompt_input_exit` |
| `Notification` | Notification type | `permission_prompt`, `idle_prompt` |
| `ConfigChange` | Config source | `user_settings`, `project_settings` |
| `FileChanged` | Filename | `.envrc\|.env` (literal filenames) |

---

## Advanced: The `if` Field

Filter by tool name AND arguments together:

```json
{
  "hooks": {
    "PreToolUse": [
      {
        "matcher": "Bash",
        "hooks": [
          {
            "type": "command",
            "if": "Bash(git *)",
            "command": "./check-git-policy.sh"
          }
        ]
      }
    ]
  }
}
```

**Only runs for `git` commands, not all Bash commands.**

---

## Managing Hooks

### View All Hooks

```bash
/hooks
```

Navigate with Tab, view details by selecting a hook.

### Reload Hooks

Hooks are reloaded automatically when you edit settings files. To force a reload:

```bash
# Restart Claude Code session
/clear
```

### Disable All Hooks

Add to settings file:

```json
{
  "disableAllHooks": true
}
```

### Debug Hooks

Start Claude Code with debug logging:

```bash
claude --debug-file /tmp/claude.log
```

Then tail the log in another terminal:

```bash
tail -f /tmp/claude.log | grep -i hook
```

---

## Troubleshooting

### Hook Not Firing

1. **Check hook is configured:** Run `/hooks` and verify it appears
2. **Verify matcher:** Matchers are case-sensitive (`bash` ≠ `Bash`)
3. **Test manually:**
   ```bash
   echo '{"tool_name":"Bash","tool_input":{"command":"ls"}}' | ./my-hook.sh
   echo $?  # Check exit code
   ```

### Permission Denied

Make scripts executable:

```bash
chmod +x .claude/hooks/my-hook.sh
```

### JSON Parsing Error

Your shell profile might be printing to stdout. Wrap echo statements:

```bash
# In ~/.zshrc or ~/.bashrc
if [[ $- == *i* ]]; then
  echo "Shell ready"  # Only in interactive mode
fi
```

### jq Not Found

Install `jq` for JSON parsing:

```bash
# macOS
brew install jq

# Ubuntu/Debian
sudo apt-get install jq
```

### Hook Runs Forever (Stop Hook)

Check if hook already triggered:

```bash
#!/bin/bash
INPUT=$(cat)
if [ "$(echo "$INPUT" | jq -r '.stop_hook_active')" = "true" ]; then
  exit 0  # Already ran, allow stop
fi
# ... rest of logic
```

---

## Student Exercises

### Exercise 1: Desktop Notifications

**Goal:** Get notified when Claude needs input

**Tasks:**
1. Add a `Notification` hook to `~/.claude/settings.json`
2. Test it by asking Claude to do something requiring permission
3. Switch windows and verify you get a notification

**Success:** You receive notifications without watching the terminal

---

### Exercise 2: Auto-Format Code

**Goal:** Automatically format code after edits

**Tasks:**
1. Install Prettier: `npm install -g prettier`
2. Add a `PostToolUse` hook for `Edit|Write` tools
3. Ask Claude to edit a frontend file
4. Verify Prettier runs automatically

**Success:** Files are formatted without manual `prettier` commands

---

### Exercise 3: Block Dangerous Commands

**Goal:** Prevent destructive operations

**Tasks:**
1. Create `.claude/hooks/block-dangerous.sh`
2. Add patterns like `rm -rf /`, `dd if=`, fork bombs
3. Register a `PreToolUse` hook for `Bash` tools
4. Test by asking Claude to run a dangerous command

**Success:** Dangerous commands are blocked with clear feedback

---

### Exercise 4: Protect Sensitive Files

**Goal:** Prevent edits to `.env` and lock files

**Tasks:**
1. Create `.claude/hooks/protect-files.sh`
2. Add patterns for `.env`, `package-lock.json`, `.git/`
3. Register a `PreToolUse` hook for `Edit|Write` tools
4. Test by asking Claude to edit `.env`

**Success:** Sensitive files are protected from modification

---

### Exercise 5: Command Auditing

**Goal:** Log all commands for security review

**Tasks:**
1. Add a `PostToolUse` hook for `Bash` tools
2. Log commands with timestamps to `~/.claude/command-log.jsonl`
3. Run several commands
4. View the log with `jq`

**Success:** All commands are logged in structured format

---

## Hook Cheat Sheet

### Common Patterns

**Extract command from hook input:**
```bash
COMMAND=$(echo "$INPUT" | jq -r '.tool_input.command')
```

**Extract file path from hook input:**
```bash
FILE_PATH=$(echo "$INPUT" | jq -r '.tool_input.file_path')
```

**Block with feedback:**
```bash
echo "Reason for blocking" >&2
exit 2
```

**Allow with context injection:**
```bash
echo "Additional context for Claude"
exit 0
```

**Check if file matches pattern:**
```bash
if [[ "$FILE_PATH" =~ \.py$ ]]; then
  # Python file
fi
```

**Get project directory:**
```bash
cd "$CLAUDE_PROJECT_DIR"
```

---

## Best Practices

1. **Start with simple hooks** - Desktop notifications, command logging
2. **Test hooks manually** - Pipe JSON to your script before adding to config
3. **Use exit codes correctly** - 0=allow, 2=block, others=error
4. **Write to stderr for feedback** - Stdout is for context/JSON output
5. **Keep hooks fast** - Slow hooks block Claude's workflow
6. **Make scripts executable** - `chmod +x` before registering
7. **Use project-relative paths** - `$CLAUDE_PROJECT_DIR` for portability
8. **Document your hooks** - Add comments explaining what they do
9. **Version control project hooks** - Commit `.claude/settings.json`
10. **Keep user hooks personal** - Don't commit `~/.claude/settings.json`

---

## Additional Resources

- **Official Hooks Guide:** https://code.claude.com/docs/en/hooks-guide
- **Hooks Reference:** https://code.claude.com/docs/en/hooks
- **Example Hooks:** https://github.com/anthropics/claude-code/tree/main/examples/hooks
- **jq Manual:** https://jqlang.github.io/jq/manual/

---

## Summary

**Essential hooks for this project:**
- ✅ **Auto-format code** - Prettier on every edit
- ✅ **Block dangerous commands** - Security safety net
- ✅ **Protect sensitive files** - Prevent `.env` modifications
- ✅ **Run tests after changes** - Continuous testing
- ✅ **Desktop notifications** - Never miss Claude waiting

Install all project hooks with:
```bash
# 1. Create hooks directory
mkdir -p .claude/hooks

# 2. Copy hook scripts from this guide to .claude/hooks/
# 3. Make them executable
chmod +x .claude/hooks/*.sh

# 4. Add hook configuration to .claude/settings.json
# 5. Test with /hooks command
```
