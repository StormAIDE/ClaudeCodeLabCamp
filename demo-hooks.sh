#!/bin/bash
# Hooks Demo Script for ClaudeCode Labcamp
# This script demonstrates hook functionality

set -e

echo "=========================================="
echo "Claude Code Hooks Demo"
echo "=========================================="
echo ""

# Check if jq is installed
if ! command -v jq &> /dev/null; then
    echo "⚠️  Warning: jq is not installed"
    echo "   Hooks use jq for JSON parsing"
    echo "   Install with: brew install jq (macOS) or apt-get install jq (Linux)"
    echo ""
fi

echo "📁 Hooks Directory Structure:"
echo ""
tree -L 2 .claude/hooks/ 2>/dev/null || {
    echo ".claude/hooks/"
    ls -la .claude/hooks/ | awk '{print "  " $0}'
}
echo ""

echo "=========================================="
echo "Installed Hooks"
echo "=========================================="
echo ""

if [ -f ".claude/settings.json" ]; then
    echo "✅ Project hooks configured in .claude/settings.json"
    echo ""
    echo "Configured hooks:"
    echo ""

    # Parse and display hooks
    if command -v jq &> /dev/null; then
        echo "1. PostToolUse (Edit|Write):"
        echo "   → Auto-format with Prettier"
        echo ""

        echo "2. PreToolUse (Bash):"
        echo "   → Block dangerous commands"
        echo ""

        echo "3. PreToolUse (Edit|Write):"
        echo "   → Protect sensitive files"
        echo ""

        echo "4. SessionStart:"
        echo "   → Inject project context"
        echo ""
    fi
else
    echo "⚠️  No .claude/settings.json found"
    echo "   Hooks have been created but not registered yet"
fi

echo "=========================================="
echo "Testing Hooks"
echo "=========================================="
echo ""

echo "Test 1: Block Dangerous Commands"
echo "---------------------------------"
TEST_INPUT='{"tool_name":"Bash","tool_input":{"command":"rm -rf /"}}'
echo "Input: $TEST_INPUT"
echo "$TEST_INPUT" | .claude/hooks/block-dangerous.sh 2>&1 && {
    echo "❌ Test failed: Dangerous command was not blocked"
} || {
    echo "✅ Test passed: Dangerous command blocked"
}
echo ""

echo "Test 2: Protect Sensitive Files"
echo "---------------------------------"
TEST_INPUT='{"tool_name":"Edit","tool_input":{"file_path":".env"}}'
echo "Input: $TEST_INPUT"
echo "$TEST_INPUT" | .claude/hooks/protect-files.sh 2>&1 && {
    echo "❌ Test failed: .env file was not protected"
} || {
    echo "✅ Test passed: .env file protected"
}
echo ""

echo "Test 3: Allow Safe Commands"
echo "---------------------------------"
TEST_INPUT='{"tool_name":"Bash","tool_input":{"command":"ls -la"}}'
echo "Input: $TEST_INPUT"
echo "$TEST_INPUT" | .claude/hooks/block-dangerous.sh 2>&1 && {
    echo "✅ Test passed: Safe command allowed"
} || {
    echo "❌ Test failed: Safe command was blocked"
}
echo ""

echo "=========================================="
echo "Hook Scripts"
echo "=========================================="
echo ""
echo "Available hook scripts in .claude/hooks/:"
echo ""
for script in .claude/hooks/*.sh; do
    if [ -f "$script" ]; then
        name=$(basename "$script")
        if [ -x "$script" ]; then
            echo "  ✅ $name (executable)"
        else
            echo "  ❌ $name (not executable - run: chmod +x $script)"
        fi
    fi
done
echo ""

echo "=========================================="
echo "How to Use Hooks in Claude Code"
echo "=========================================="
echo ""
echo "1. View all hooks:"
echo "   /hooks"
echo ""
echo "2. The following hooks are active:"
echo "   • Auto-format code after edits (Prettier)"
echo "   • Block dangerous commands (rm -rf, dd, etc.)"
echo "   • Protect sensitive files (.env, lock files)"
echo "   • Inject project context on session start"
echo ""
echo "3. Test them by asking Claude to:"
echo "   • Edit a TypeScript file (→ auto-format)"
echo "   • Run 'rm -rf /' (→ blocked)"
echo "   • Edit .env file (→ blocked)"
echo ""
echo "4. Debug hooks with:"
echo "   claude --debug-file /tmp/claude.log"
echo "   tail -f /tmp/claude.log | grep -i hook"
echo ""

echo "=========================================="
echo "For complete documentation, see HOOKS.md"
echo "=========================================="
