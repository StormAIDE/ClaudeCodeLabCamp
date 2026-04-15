# Claude Code Plugins Setup Guide

This guide demonstrates how to use Claude Code plugins to enhance your development workflow. These plugins are educational examples for students learning full-stack AI development.

## Quick Start

```bash
# Install all recommended plugins at once
/plugin install typescript-lsp@claude-plugins-official
/plugin install pyright-lsp@claude-plugins-official
/plugin install github@claude-plugins-official
/plugin install commit-commands@anthropics-claude-code
/reload-plugins
```

## Recommended Plugins for This Project

### 1. TypeScript LSP (Code Intelligence)

**What it does:** Provides real-time type checking, auto-completion, and error detection for TypeScript/React code.

**Installation:**
```bash
# Step 1: Install the language server binary (if not already installed)
npm install -g typescript-language-server typescript

# Step 2: Install the plugin
/plugin install typescript-lsp@claude-plugins-official
/reload-plugins
```

**Benefits for students:**
- See type errors immediately after code changes
- Learn TypeScript best practices through real-time feedback
- Understand how professional IDEs work under the hood

**Try it:**
1. Make a type error in `frontend/src/components/ChatInterface.tsx`
2. Claude will automatically detect and fix it
3. Press **Ctrl+O** to see inline diagnostics

---

### 2. Python LSP (Pyright)

**What it does:** Provides type checking and IntelliSense for Python backend code.

**Installation:**
```bash
# Step 1: Install the language server binary
pip install pyright

# Step 2: Install the plugin
/plugin install pyright-lsp@claude-plugins-official
/reload-plugins
```

**Benefits for students:**
- Catch type errors in FastAPI routes and Pydantic models
- Learn Python type hints through immediate feedback
- Understand async/await patterns better with type checking

**Try it:**
1. Make a type error in `backend/services/agent_service.py`
2. Claude will see the diagnostic and suggest fixes
3. Learn proper type annotation patterns

---

### 3. GitHub Integration

**What it does:** Allows Claude to interact with GitHub - create PRs, manage issues, review code.

**Installation:**
```bash
# Install the plugin
/plugin install github@claude-plugins-official
/reload-plugins

# Authenticate (follow prompts)
# Claude will guide you through GitHub authentication
```

**Benefits for students:**
- Learn professional GitHub workflows
- Understand pull request best practices
- See how teams collaborate on code

**Try it:**
```bash
# View current repository info
Tell Claude: "Show me the open issues on this repo"

# Create a pull request
Tell Claude: "Create a PR for the current branch"

# Review a PR
Tell Claude: "Review PR #123"
```

---

### 4. Commit Commands

**What it does:** Automates git workflows with conventional commit messages.

**Installation:**
```bash
# Step 1: Add the demo marketplace (if not already added)
/plugin marketplace add anthropics/claude-code

# Step 2: Install the plugin
/plugin install commit-commands@anthropics-claude-code
/reload-plugins
```

**Benefits for students:**
- Learn conventional commit format (feat:, fix:, chore:, etc.)
- Automate repetitive git tasks
- Understand professional commit practices

**Try it:**
```bash
# Make changes to a file, then:
/commit-commands:commit

# Claude will:
# 1. Stage your changes
# 2. Generate a conventional commit message
# 3. Create the commit
```

---

### 5. Slack Integration (Optional - Advanced)

**What it does:** Send messages, read channels, and integrate AI with team communication.

**Installation:**
```bash
/plugin install slack@claude-plugins-official
/reload-plugins
```

**Benefits for students:**
- See real-world business integration
- Learn how AI can automate communication
- Understand OAuth and API integration patterns

**Try it:**
```bash
# Send a deployment notification
Tell Claude: "Send a message to #deployments that the backend is deployed"

# Get team updates
Tell Claude: "Check #engineering for any mentions of bugs"
```

**Setup requirements:**
- Slack workspace admin access
- Create a Slack app with proper scopes
- Configure OAuth tokens

---

## Managing Plugins

### View installed plugins
```bash
/plugin
# Navigate to "Installed" tab with Tab key
```

### Update marketplaces
```bash
/plugin marketplace update claude-plugins-official
/plugin marketplace update anthropics-claude-code
```

### Disable a plugin temporarily
```bash
/plugin disable typescript-lsp@claude-plugins-official
/reload-plugins
```

### Uninstall a plugin
```bash
/plugin uninstall typescript-lsp@claude-plugins-official
```

---

## Educational Use Cases

### Use Case 1: Type-Safe Development
**Plugins:** TypeScript LSP + Pyright LSP

**Demonstration:**
1. Ask Claude to add a new API endpoint
2. Show how Claude detects type mismatches automatically
3. Demonstrate fixing errors without running the code

**Learning outcomes:**
- Importance of type safety in production systems
- How LSP powers modern IDEs
- TypeScript and Python type systems

---

### Use Case 2: Professional Git Workflow
**Plugins:** Commit Commands + GitHub

**Demonstration:**
1. Implement a feature on a new branch
2. Use `/commit-commands:commit` for proper commits
3. Create a PR with `/review-pr` or through GitHub plugin
4. Show code review process

**Learning outcomes:**
- Conventional commit messages
- Pull request workflow
- Code review best practices

---

### Use Case 3: Real-Time Error Detection
**Plugins:** TypeScript LSP + Pyright LSP

**Demonstration:**
1. Intentionally introduce a bug (e.g., wrong parameter type)
2. Show Claude catching it immediately via diagnostics
3. Watch Claude fix it in the same turn

**Learning outcomes:**
- Shift-left testing philosophy
- Benefits of static analysis
- How to read compiler errors

---

### Use Case 4: Team Collaboration
**Plugins:** GitHub + Slack

**Demonstration:**
1. Create a feature branch
2. Make commits with proper messages
3. Create PR through Claude
4. Send notification to Slack channel

**Learning outcomes:**
- Full development lifecycle
- Cross-tool automation
- Team communication patterns

---

## Troubleshooting

### Plugin not found
```bash
# Update the marketplace
/plugin marketplace update claude-plugins-official
/plugin marketplace update anthropics-claude-code

# Try installing again
/plugin install <plugin-name>@<marketplace-name>
```

### Language server not starting
```bash
# Check if binary is installed
which typescript-language-server
which pyright

# Install if missing
npm install -g typescript-language-server typescript
pip install pyright

# Reinstall plugin
/plugin uninstall typescript-lsp@claude-plugins-official
/plugin install typescript-lsp@claude-plugins-official
/reload-plugins
```

### Skills not showing up
```bash
# Clear plugin cache
rm -rf ~/.claude/plugins/cache

# Restart Claude Code and reinstall
/plugin install <plugin-name>
/reload-plugins
```

---

## Student Exercises

### Exercise 1: Setup All Plugins
**Goal:** Install and configure all recommended plugins

**Tasks:**
1. Install TypeScript LSP and verify it detects errors
2. Install Pyright LSP and test with backend code
3. Install commit-commands and make a proper commit
4. Install GitHub plugin and view repository info

**Success criteria:**
- All plugins show as "Installed" in `/plugin` UI
- TypeScript errors appear inline (Ctrl+O)
- Commits use conventional format

---

### Exercise 2: Build with Intelligence
**Goal:** Use LSP plugins while developing a feature

**Tasks:**
1. Add a new React component with intentional type error
2. Let Claude detect and fix it automatically
3. Add type hints to a Python function
4. Verify both frontend and backend have no type errors

**Success criteria:**
- Type errors caught before runtime
- Proper TypeScript interfaces used
- Python type hints follow mypy standards

---

### Exercise 3: Professional Workflow
**Goal:** Complete feature → commit → PR flow

**Tasks:**
1. Create a feature branch
2. Implement a small feature (e.g., add a timestamp to messages)
3. Use `/commit-commands:commit` for each logical change
4. Create a PR using GitHub plugin

**Success criteria:**
- Branch follows naming convention (feature/*, fix/*)
- Commits use conventional format
- PR has proper description

---

## Plugin Architecture (For Advanced Students)

### How Plugins Work

**Plugin Types:**
1. **Skills** - New slash commands (e.g., `/commit-commands:commit`)
2. **Agents** - Specialized AI agents for specific tasks
3. **Hooks** - Automated actions triggered by events
4. **MCP Servers** - External service integrations (GitHub, Slack)
5. **LSP Servers** - Language intelligence (TypeScript, Python)

**Example Plugin Structure:**
```
.claude-plugin/
├── manifest.json      # Plugin metadata
├── skills/           # Slash command definitions
├── agents/           # Specialized agent prompts
├── hooks/            # Event-triggered scripts
└── mcp-servers/      # External integrations
```

### Creating Your Own Plugin (Advanced)

See official documentation:
- [Plugins Guide](https://code.claude.com/docs/en/plugins)
- [Plugin Marketplaces](https://code.claude.com/docs/en/plugin-marketplaces)
- [Plugins Reference](https://code.claude.com/docs/en/plugins-reference)

---

## Best Practices

1. **Always reload after installing:** `/reload-plugins` applies changes immediately
2. **Update marketplaces regularly:** Get latest plugin versions
3. **Use project scope for team plugins:** Adds to `.claude/settings.json` for sharing
4. **Check plugin errors:** `/plugin` → Errors tab shows issues
5. **Trust before installing:** Only install from official or verified sources

---

## Additional Resources

- **Official Marketplace:** [claude.com/plugins](https://claude.com/plugins)
- **Demo Plugins:** [github.com/anthropics/claude-code/tree/main/plugins](https://github.com/anthropics/claude-code/tree/main/plugins)
- **Documentation:** [code.claude.com/docs/en/discover-plugins](https://code.claude.com/docs/en/discover-plugins)

---

## Summary

**Essential plugins for this project:**
- ✅ TypeScript LSP - Real-time frontend type checking
- ✅ Pyright LSP - Backend Python type safety
- ✅ GitHub - Professional version control workflows
- ✅ Commit Commands - Automated git best practices

**Optional for advanced demos:**
- Slack - Business communication integration
- Sentry - Error monitoring and tracking
- Linear - Project management integration

Install all essentials with:
```bash
/plugin install typescript-lsp@claude-plugins-official && \
/plugin install pyright-lsp@claude-plugins-official && \
/plugin install github@claude-plugins-official && \
/plugin marketplace add anthropics/claude-code && \
/plugin install commit-commands@anthropics-claude-code && \
/reload-plugins
```
