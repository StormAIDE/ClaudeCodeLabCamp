#!/bin/bash
# Plugin Demo Script for ClaudeCode Labcamp
# This script demonstrates plugin installation and usage

set -e  # Exit on error

echo "=========================================="
echo "Claude Code Plugins Demo"
echo "=========================================="
echo ""

# Function to check if a command exists
command_exists() {
    command -v "$1" >/dev/null 2>&1
}

# Check prerequisites
echo "Checking prerequisites..."

if ! command_exists npm; then
    echo "❌ npm not found. Please install Node.js first."
    exit 1
fi

if ! command_exists pip; then
    echo "❌ pip not found. Please install Python first."
    exit 1
fi

echo "✅ Prerequisites satisfied"
echo ""

# Install language server binaries
echo "=========================================="
echo "Step 1: Installing Language Server Binaries"
echo "=========================================="
echo ""

echo "Installing TypeScript language server..."
npm install -g typescript-language-server typescript 2>/dev/null || true

echo "Installing Pyright for Python..."
pip install pyright 2>/dev/null || true

echo "✅ Language servers installed"
echo ""

# Instructions for plugin installation
echo "=========================================="
echo "Step 2: Install Claude Code Plugins"
echo "=========================================="
echo ""
echo "Run the following commands in Claude Code:"
echo ""
echo "1. Install TypeScript LSP:"
echo "   /plugin install typescript-lsp@claude-plugins-official"
echo ""
echo "2. Install Python LSP:"
echo "   /plugin install pyright-lsp@claude-plugins-official"
echo ""
echo "3. Install GitHub integration:"
echo "   /plugin install github@claude-plugins-official"
echo ""
echo "4. Add demo marketplace:"
echo "   /plugin marketplace add anthropics/claude-code"
echo ""
echo "5. Install Commit Commands:"
echo "   /plugin install commit-commands@anthropics-claude-code"
echo ""
echo "6. Reload plugins:"
echo "   /reload-plugins"
echo ""

# Demo scenarios
echo "=========================================="
echo "Step 3: Demo Scenarios"
echo "=========================================="
echo ""
echo "Scenario 1: Type-Safe Development"
echo "---------------------------------"
echo "1. Open frontend/src/components/ChatInterface.tsx"
echo "2. Change a prop type to something invalid"
echo "3. Press Ctrl+O to see TypeScript diagnostics"
echo "4. Ask Claude to fix the type error"
echo ""
echo "Scenario 2: Git Workflow"
echo "---------------------------------"
echo "1. Make a change to any file"
echo "2. Run: /commit-commands:commit"
echo "3. Claude will stage, write commit message, and commit"
echo ""
echo "Scenario 3: GitHub Integration"
echo "---------------------------------"
echo "1. Ask Claude: 'Show me the open issues'"
echo "2. Ask Claude: 'Create a PR for this branch'"
echo ""
echo "Scenario 4: Real-time Error Detection"
echo "---------------------------------"
echo "1. Open backend/services/agent_service.py"
echo "2. Remove a type hint from a function"
echo "3. Watch Claude detect missing type annotation"
echo "4. Ask Claude to add proper type hints"
echo ""

echo "=========================================="
echo "For complete documentation, see PLUGINS.md"
echo "=========================================="
