# ClaudeCode Labcamp: Full-Stack AI Agent Project

> **Learn Claude Code: Boost Daily Productivity**
> 
> A hands-on project demonstrating ALL Claude Code features working together to enhance your daily software engineering tasks with repeatable workflows and verification patterns.

## 📋 What You'll Learn

This project showcases how Claude Code integrates 8 powerful features into a single development workflow:

1. **CLAUDE.md** - Project documentation that guides AI behavior
2. **Hooks** - Automated workflows (formatting, safety checks, testing)
3. **Plugins** - IDE features (type checking, GitHub integration)
4. **Custom Commands** - Reusable slash commands
5. **Skills** - Multi-step automated workflows
6. **Custom Agents** - Specialized AI agents for specific tasks
7. **MCP Servers** - External tool integration
8. **settings.json** - Centralized configuration

---

## 🚀 Quick Start

### Prerequisites

- **Python 3.14.0** (virtual environment included in `claudecodeenv/`)
- **Node.js 18+** and npm
- **AWS Account** with Bedrock access (Claude 4 enabled)
- **AWS CLI** configured with credentials
- **Git**
- **Claude Code** installed ([claude.ai/code](https://claude.ai/code))

### Installation

```bash
# 1. Clone the repository
git clone https://github.com/StormAIDE/ClaudeCodeLabCamp.git
cd ClaudeCodeLabCamp

# 2. Configure AWS credentials (terminal session)
aws configure
# OR export credentials directly:
export AWS_ACCESS_KEY_ID=your_key
export AWS_SECRET_ACCESS_KEY=your_secret
export AWS_SESSION_TOKEN=your_token  # if using temporary credentials

# 3. Create .env file
cp .env.example .env
# Note: AWS credentials are NOT in .env - they're in your terminal session

# 4. Install backend dependencies
source claudecodeenv/bin/activate
pip install -r requirements.txt

# 5. Install frontend dependencies
cd frontend
npm install
cd ..
```

### Running the Application

**Option 1: Quick Start Script**
```bash
./start.sh
```

**Option 2: Manual Start (2 terminals)**
```bash
# Terminal 1 - Backend
source claudecodeenv/bin/activate
python -m backend.main

# Terminal 2 - Frontend
cd frontend
npm run dev
```

**Access Points:**
- Frontend: http://localhost:5173
- Backend API: http://localhost:8000
- API Docs: http://localhost:8000/docs

---

## 🏗️ Project Architecture

```
┌─────────────────────────────────────────────────────────────┐
│                        Frontend                              │
│  React 19 + TypeScript + Vite + Tailwind CSS               │
│  - ChatInterface: Main UI                                   │
│  - Zustand: Client state management                         │
│  - TanStack Query: Server state & caching                   │
└────────────────┬────────────────────────────────────────────┘
                 │ HTTP/SSE
                 ↓
┌─────────────────────────────────────────────────────────────┐
│                         Backend                              │
│  FastAPI + Strands Agents SDK + Pydantic                    │
│  - Agent Service: Claude 4 via Amazon Bedrock               │
│  - Safe Tools: Weather, AST-based calculator                │
│  - Dependency Injection: Singleton pattern                  │
└────────────────┬────────────────────────────────────────────┘
                 │
                 ↓
┌─────────────────────────────────────────────────────────────┐
│              Claude 4 (Amazon Bedrock)                       │
│  model: eu.anthropic.claude-sonnet-4-5-20250929-v1:0       │
└─────────────────────────────────────────────────────────────┘
```

**Key Technologies:**
- **Backend:** FastAPI, Strands SDK, Pydantic, Python 3.14
- **Frontend:** React 19, TypeScript, Vite, Zustand, TanStack Query, Tailwind CSS
- **AI:** Claude 4 via Amazon Bedrock
- **Testing:** Pytest (backend: 43 tests), Vitest (frontend: 19 tests) - 62 tests total

---

## 🎓 Labcamp Learning Path: Claude Code Features in Action

### Step 1: CLAUDE.md - Project Documentation

**What it is:**
A markdown file that contains instructions for Claude Code about your project. It's like a project guide that tells Claude how to work with your codebase.

**Where to find it:**
- File: `/CLAUDE.md`
- [Official docs](https://code.claude.com/docs/en/memory)

**What it does:**
- Defines development commands (backend, frontend, testing)
- Specifies architecture patterns and project structure
- Sets rules (always run tests, use conventional commits, never modify .env)
- Documents tech stack and configuration

**Try it yourself:**
1. Open `CLAUDE.md` in your editor
2. Notice sections like "Development Commands", "Testing Requirements", "Architecture Overview"
3. In Claude Code, ask: "What are the development commands for this project?"
4. Claude will reference CLAUDE.md and give you the exact commands

**Example:**
```
You: "How do I run the backend?"
Claude: "According to CLAUDE.md, run: source claudecodeenv/bin/activate && python -m backend.main"
```

**Educational Value:**
- **Consistency:** All developers (human or AI) follow the same rules
- **Onboarding:** New team members read CLAUDE.md to understand the project
- **Documentation-as-code:** Project rules are version-controlled

---

### Step 2: Hooks - Automated Workflows

**What they are:**
Shell scripts that run automatically at specific points in Claude Code's lifecycle (before/after tool calls, session start/end, etc.)

**Where to find them:**
- Configuration: `.claude/settings.json`
- Scripts: `.claude/hooks/*.sh`
- Command: `/hooks` (shows all configured hooks)

**Active Hooks in This Project:**

#### Hook #1: Block Dangerous Commands
**Event:** `PreToolUse` (before Bash tool)
**Script:** `.claude/hooks/block-dangerous.sh`
**What it does:** Prevents destructive operations like `rm -rf /`, `dd`, fork bombs, pipe to shell
**Status:** ✅ **Working** (requires `jq` - install with `brew install jq`)

**Blocked patterns:**
- `rm -rf /`, `rm -rf ~`, `rm -rf $HOME`
- `dd if=` (disk destroyer)
- `> /dev/sda` (overwrite disk)
- `mkfs` (format filesystem)
- Fork bomb: `:(){ :|:& };:`
- Pipe to shell: `curl * | bash`, `wget * | sh`
- `chmod 777` (overly permissive)
- `sudo rm` (dangerous sudo)

**Try it:**
```
You: "Run the command: rm -rf /"
Claude: [BLOCKED] 🚫 Command matches dangerous pattern 'rm -rf /'
```

#### Hook #2: Protect Sensitive Files
**Event:** `PreToolUse` (before Edit/Write tools)
**Script:** `.claude/hooks/protect-files.sh`
**What it does:** Blocks edits to `.env`, lock files, `.git/`, `claudecodeenv/`
**Status:** ✅ **Working** (requires `jq` - install with `brew install jq`)

**Protected patterns:**
- `.env`, `.env.local`, `.env.production` (credentials)
- `package-lock.json`, `yarn.lock`, `poetry.lock`, `Pipfile.lock` (lock files)
- `.git/` (git internals)
- `node_modules/`, `claudecodeenv/`, `venv/`, `.venv/`, `__pycache__/` (dependencies)

**Try it:**
```
You: "Edit the .env file to add a new variable"
Claude: [BLOCKED] 🔒 .env is protected - this file should not be modified by automation
```

#### Hook #3: Run Tests After Code Changes
**Event:** `PostToolUse` (after Edit/Write tools)
**Script:** `.claude/hooks/run-tests.sh`
**What it does:** Automatically runs test suite after editing `.py`, `.ts`, or `.tsx` files
**Status:** ✅ **Working** (requires `jq` - install with `brew install jq`)

**How it works:**
- **Python files (`.py`)**: Runs `python -m pytest backend/tests/` in virtual environment
- **TypeScript files (`.ts`, `.tsx`)**: Runs `npm test -- --run` in frontend directory
- **Non-blocking**: Warns if tests fail but doesn't prevent the edit
- **Smart filtering**: Only runs for code files, skips config/docs

**Try it:**
1. Ask Claude to modify `backend/config.py`
2. Watch the test suite run automatically
3. See test results in real-time

#### Hook #4: Inject Project Context
**Event:** `SessionStart`
**File:** `.claude/hooks/project-context.txt`
**What it does:** Reminds Claude of project rules every session (ports, commit format, test requirements)
**Status:** ✅ **Working**

**Try it:**
1. Start a new Claude Code session
2. Ask Claude about the project
3. Notice it already knows the ports (8000, 5173) and commit format without you telling it

**Educational Value:**
- **Safety:** Prevents accidents (rm -rf, editing credentials)
- **Consistency:** Same rules apply every time, every session
- **Productivity:** Focus on features, not repetitive tasks
- **Quality:** Tests run automatically after every code change
- **Context:** Claude knows project rules on session start

**Prerequisites:**
All hooks require `jq` (JSON processor) to be installed:
```bash
brew install jq
```

**View all hooks:**
```bash
/hooks  # Interactive browser showing all configured hooks
```

---

### Step 3: Plugins - IDE Features

**What they are:**
Extensions that add IDE-like features to Claude Code (type checking, code navigation, GitHub integration)

**Where to configure them:**
- Command: `/plugin` (interactive plugin manager)
- Marketplace: `claude-plugins-official` (auto-added)

**Recommended Plugins for This Project:**

#### Plugin #1: TypeScript LSP
**What:** Real-time type checking for React/TypeScript code
**Install:** `/plugin install typescript-lsp@claude-plugins-official`
**Prerequisite:** `npm install -g typescript-language-server typescript`

**What it does:**
- Detects type errors immediately after edits
- Shows diagnostics without running the app
- Enables "Go to Definition", "Find References"

**Try it:**
1. Install the plugin: `/plugin install typescript-lsp@claude-plugins-official`
2. Reload: `/reload-plugins`
3. Ask Claude: "Add a new prop to ChatInterface.tsx with wrong type"
4. Watch the TypeScript LSP catch the error instantly (no need to run the app!)
5. Claude will see the diagnostic and can fix it immediately

**Verification command for participants:**
```
Ask Claude: "Add a maxMessages prop to ChatInterface with type string, then try to use it in math"
Expected: TypeScript LSP reports type error immediately
```

#### Plugin #2: Pyright LSP
**What:** Type checking for Python/FastAPI backend
**Install:** `/plugin install pyright-lsp@claude-plugins-official`
**Prerequisite:** `pip install pyright`

**What it does:**
- Validates type hints automatically
- Catches async/await errors
- Ensures Pydantic models are correct

**Try it:**
1. Install the plugin: `/plugin install pyright-lsp@claude-plugins-official`
2. Reload: `/reload-plugins`
3. Ask Claude: "Add a type annotation error to backend/config.py"
4. Pyright catches it before runtime

**Verification command for participants:**
```
Ask Claude: "Add a line to backend/config.py: test_port: int = '8000'"
Expected: Pyright LSP reports type mismatch (str assigned to int)
```

#### Plugin #3: GitHub Integration
**What:** PR creation, issue management, code review automation
**Install:** `/plugin install github@claude-plugins-official`

**What it does:**
- Create pull requests from Claude Code
- View/create/close issues
- Review PRs with AI assistance

**Try it:**
1. Install the plugin: `/plugin install github@claude-plugins-official`
2. Reload: `/reload-plugins`
3. Ask Claude: "Show me the PRs for this branch"

**Verification command for participants:**
```
Ask Claude: "Use the GitHub plugin to list all open PRs for the feature/lab-work branch"
Expected: Claude uses `gh pr list` command and shows PR details
```

#### Plugin #4: Commit Commands
**What:** Automated conventional commit messages
**Install:** 
```bash
/plugin marketplace add anthropics/claude-code
/plugin install commit-commands@anthropics-claude-code
```

**What it does:**
- Analyzes changes with `git diff`
- Generates conventional commit message (feat:, fix:, chore:)
- Commits automatically

**Try it:**
1. Install the plugin:
   ```bash
   /plugin marketplace add anthropics/claude-code
   /plugin install commit-commands@anthropics-claude-code
   /reload-plugins
   ```
2. Make a small change (edit any file)
3. Ask Claude: "Use the commit-commands skill to commit these changes"

**Verification command for participants:**
```
1. Make a change: Ask Claude to "Add a comment to backend/config.py"
2. Ask Claude: "Use the commit skill to create a commit"
Expected: Claude analyzes changes, generates conventional commit message, commits
```

**Educational Value:**
- **Professional tooling:** Same features as VS Code, JetBrains IDEs
- **Shift-left testing:** Catch bugs at compile-time, not runtime
- **Type-driven development:** Type system guides implementation
- **GitHub workflow:** Automate PR creation and reviews

**View/manage plugins:**
```bash
/plugin                    # Interactive plugin manager
/reload-plugins            # Apply plugin changes
```

---

### Step 4: Custom Commands - Slash Commands

**What they are:**
Reusable commands you create for common tasks, invoked with `/command-name`

**Where to find them:**
- File: `.claude/commands/component.md`
- Format: Markdown with frontmatter (YAML metadata)

**Example: Component Generator**

**Command:** `/component ComponentName [description]`

**What it does:**
1. Creates a new React TypeScript component
2. Generates proper file structure with TypeScript interfaces
3. Applies Tailwind CSS styling from project theme
4. Follows project conventions (functional components, type imports)

**Try it:**
```bash
/component LoadingSpinner Shows a loading indicator
```

**Claude will:**
1. Create `frontend/src/components/LoadingSpinner.tsx`
2. Generate component with proper TypeScript types
3. Apply project's Tailwind CSS color scheme
4. Add props interface (`LoadingSpinnerProps`)
5. Show you the code and suggest where to use it

**Example Output:**
```typescript
interface LoadingSpinnerProps {
  size?: 'sm' | 'md' | 'lg'
  className?: string
}

export default function LoadingSpinner({ 
  size = 'md', 
  className = '' 
}: LoadingSpinnerProps) {
  return (
    <div className="flex items-center justify-center">
      <div className="animate-spin rounded-full border-4 border-blue-600 border-t-transparent" />
    </div>
  )
}
```

**Educational Value:**
- **Code generation:** Automate repetitive component creation
- **Consistency:** All components follow the same structure
- **Productivity:** Create components in seconds, not minutes
- **Customization:** Define your own commands for your workflow

**Verification command for participants:**
```
Ask Claude: "Use the /component command to create TestButton with description 'A simple test button', then delete it"
Expected: Claude creates frontend/src/components/TestButton.tsx with proper TypeScript types and Tailwind styling, then removes it
What it proves: Custom command generates components following project conventions
```

**Create your own command:**
1. Create `.claude/commands/your-command.md`
2. Add YAML frontmatter (name, description, usage)
3. Write instructions for Claude
4. Use it with `/your-command`

---

### Step 5: Skills - Complex Workflows

**What they are:**
Multi-step automated workflows that orchestrate multiple commands

**Where to find them:**
- File: `.claude/skills/start-dev/SKILL.md`
- Format: Markdown with instructions for Claude

**Example: Start Development Servers**

**Skill:** `/start-dev` (or use the Skill tool)

**What it does:**
1. Activates Python virtual environment
2. Starts FastAPI backend on port 8000 (background process)
3. Starts Vite frontend on port 5173 (background process)
4. Reports status and URLs to you

**Try it:**
```bash
# Just run the skill
/start-dev

# Claude will:
# ✓ Activate claudecodeenv
# ✓ Start backend: uvicorn backend.main:app --reload
# ✓ Start frontend: npm run dev
# ✓ Report both URLs
```

**Educational Value:**
- **Workflow automation:** Complex tasks become one command
- **Consistency:** Same startup process every time
- **Error handling:** Skill handles environment setup
- **Background processes:** Both servers run simultaneously

**Verification command for participants:**
```
Ask Claude: "Use the start-dev skill to start both servers, then stop them"
Expected: Claude starts backend (port 8000) and frontend (port 5173) in background, confirms URLs, then stops both
What it proves: Multi-step workflow automation with background processes
```

**Create your own skill:**
1. Create `.claude/skills/your-skill/SKILL.md`
2. Write step-by-step instructions
3. Claude executes the workflow automatically
4. Use it by asking Claude to run the skill

**Difference between Commands vs Skills:**
- **Commands:** User-invocable with `/slash` syntax, simpler use case
- **Skills:** More complex, can have multiple steps, Claude invokes based on context

---

### Step 6: Custom Agents - Specialized AI

**What they are:**
Specialized AI agents trained for specific tasks (backend, frontend, code review, visual inspection)

**Where to find them:**
- Directory: `.claude/agents/`
- Files: 4 agent definitions (YAML frontmatter + markdown)

**Available Agents:**

#### Agent #1: backend-maintainer
**Purpose:** Backend development tasks (FastAPI, Strands SDK, Python)
**When to use:** API endpoints, service layer, agent tools, database work

**Try it:**
```
You: "Add a new endpoint to get user profile"
Claude: [Delegates to backend-maintainer agent]
Agent: [Creates endpoint, adds validation, writes tests]
```

#### Agent #2: code-reviewer
**Purpose:** Comprehensive code quality analysis
**When to use:** Before commits, after refactoring, debugging complex issues

**Try it:**
```
You: "Review the changes in this branch"
Claude: [Spawns code-reviewer agent]
Agent: [Analyzes backend + frontend, checks tests, reports issues]
```

#### Agent #3: frontend-improver
**Purpose:** UI/UX improvements, React components, frontend architecture
**When to use:** Component development, state management, client-side work

**Try it:**
```
You: "Improve the chat interface with better UX"
Claude: [Launches frontend-improver agent]
Agent: [Analyzes UI, proposes improvements, implements changes]
```

#### Agent #4: frontend-visual-inspector
**Purpose:** Visual analysis of UI (takes screenshots, checks layout)
**When to use:** Visual bugs, responsive design, UI/UX validation

**Try it:**
```
You: "Check if the chat interface looks good on mobile"
Claude: [Spawns frontend-visual-inspector agent]
Agent: [Takes screenshots, analyzes layout, suggests fixes]
```

**Educational Value:**
- **Specialization:** Each agent has deep expertise in its domain
- **Parallel work:** Multiple agents can work simultaneously
- **Context isolation:** Agents work in separate contexts (worktrees)
- **Multi-agent systems:** Shows how AI teams collaborate

**How agents work:**
1. You ask Claude to do something
2. Claude recognizes it matches an agent's specialty
3. Agent is spawned with specific instructions
4. Agent completes task and reports back
5. Claude integrates the results

---

### Step 7: MCP Servers - External Tools

**What they are:**
Model Context Protocol servers that connect Claude Code to external services (diagrams, browsers, databases, APIs)

**Where to find them:**
- File: `.mcp.json`
- Format: JSON configuration with server definitions

**Configured MCP Servers:**

#### MCP #1: drawio
**Purpose:** Create diagrams (flowcharts, architecture diagrams, UML)
**Command:** `npx -y @drawio/mcp`

**Try it:**
```
You: "Create an architecture diagram showing backend, frontend, and Bedrock"
Claude: [Uses drawio MCP server]
Result: Generates .drawio file with visual diagram
```

#### MCP #2: chrome-devtools
**Purpose:** Browser automation (screenshots, console logs, network requests)
**Command:** `npx -y chrome-devtools-mcp@latest`

**Try it:**
```
You: "Take a screenshot of the chat interface"
Claude: [Uses chrome-devtools MCP]
Result: Opens browser, navigates to localhost:5173, captures screenshot
```

**Educational Value:**
- **External integration:** Connect AI to any tool or service
- **Visual outputs:** Generate diagrams, take screenshots
- **Automation:** Browser testing, API calls, file operations
- **Extensibility:** Add any MCP server to extend capabilities

**How MCP works:**
1. MCP server runs as a subprocess
2. Claude sends requests to the server
3. Server performs action (create diagram, take screenshot, etc.)
4. Server returns results
5. Claude integrates results into conversation

**Add your own MCP server:**
```json
{
  "mcpServers": {
    "your-server": {
      "command": "npx",
      "args": ["-y", "your-mcp-package"]
    }
  }
}
```

**Popular MCP servers:**
- `@modelcontextprotocol/server-filesystem` - File operations
- `@modelcontextprotocol/server-postgres` - Database access
- `@modelcontextprotocol/server-slack` - Slack integration
- `@modelcontextprotocol/server-github` - GitHub API

---

### Step 8: settings.json - Configuration Hub

**What it is:**
Central configuration file that ties all Claude Code features together

**Where to find it:**
- Project: `.claude/settings.json` (shared with team)
- User: `~/.claude/settings.json` (personal preferences)
- Local: `.claude/settings.local.json` (gitignored, local overrides)

**What's Configured:**

**Hooks:**
```json
{
  "hooks": {
    "PreToolUse": [...],      // Block dangerous commands, protect files
    "SessionStart": [...]     // Inject project context
  }
}
```

**Permissions:**
```json
{
  "permissions": {
    "allowed": [
      "Bash(npm *)",          // Allow npm commands
      "Bash(git *)",          // Allow git commands
      "mcp__*"                // Allow all MCP tools
    ]
  }
}
```

**Educational Value:**
- **Centralization:** All configuration in one place
- **Version control:** Project settings committed to git
- **Scopes:** User settings (personal), project (team), local (gitignored)
- **Transparency:** Easy to see what's enabled/disabled

**View configuration:**
```bash
/hooks              # Browse all hooks
/plugin             # Manage plugins
cat .claude/settings.json  # View raw config
```

---

## 📂 Project Structure

```
ClaudeCodeLabCamp/
├── backend/                      # FastAPI backend
│   ├── main.py                  # Entry point (USE THIS)
│   ├── config.py                # Pydantic Settings
│   ├── api/                     # API layer
│   │   ├── routes.py           # Route aggregation
│   │   ├── dependencies.py     # Dependency injection
│   │   └── endpoints/
│   │       └── agent.py        # Agent chat endpoints
│   ├── services/                # Business logic
│   │   └── agent_service.py    # Strands SDK agent service
│   └── tests/                   # Test suite (35 tests)
│       ├── test_config.py      
│       ├── test_dependencies.py
│       ├── test_agent_service.py
│       └── test_endpoints.py
│
├── frontend/                     # React TypeScript frontend
│   ├── src/
│   │   ├── App.tsx              # Main app
│   │   ├── main.tsx             # Entry point
│   │   ├── components/          # React components
│   │   │   ├── ChatInterface.tsx
│   │   │   ├── MessageList.tsx
│   │   │   └── MessageInput.tsx
│   │   ├── api/
│   │   │   └── agent.ts         # API client
│   │   ├── store/
│   │   │   └── agentStore.ts    # Zustand store
│   │   └── test/                # Test files
│   ├── package.json
│   └── vite.config.ts
│
├── .claude/                      # Claude Code configuration
│   ├── settings.json            # Hooks, permissions
│   ├── hooks/                   # Hook scripts
│   │   └── project-context.txt  # Context injection
│   ├── agents/                  # Custom agents
│   │   ├── backend-maintainer.md
│   │   ├── code-reviewer.md
│   │   ├── frontend-improver.md
│   │   └── frontend-visual-inspector.md
│   ├── commands/                # Custom commands
│   │   └── component.md         # /component generator
│   └── skills/                  # Skills
│       └── start-dev/
│           └── SKILL.md         # Start dev servers
│
├── .mcp.json                    # MCP server config
├── .env.example                 # Environment template
├── CLAUDE.md                    # Project documentation for Claude Code
├── README.md                    # This file (labcamp guide)
├── start.sh                     # Quick start script
├── run-all-tests.sh            # Test orchestration
└── requirements.txt             # Python dependencies
```

---

## 🛠️ Complete Development Workflow Example

Let's walk through a real development session showing ALL features working together:

### Scenario: Add a "Clear Chat" Button

```
# 1. Start Claude Code session
→ SessionStart hook fires
→ Injects project context from .claude/hooks/project-context.txt
→ Claude knows: ports (8000, 5173), commit format, test requirements

# 2. You ask: "Add a clear chat button to the UI"
→ Claude delegates to frontend-improver agent (Step 6: Custom Agents)
→ Agent analyzes ChatInterface component

# 3. Generate button component
You: "/component ClearButton A button to clear chat messages"
→ Custom command fires (Step 4: Commands)
→ Creates frontend/src/components/ClearButton.tsx

# 4. Claude modifies ChatInterface.tsx
→ Adds import for ClearButton
→ Wires up onClick handler to clear messages
→ TypeScript LSP plugin runs (Step 3: Plugins)
→ No type errors detected ✓

# 5. Try dangerous command (accidentally)
You: "Remove all test files with rm -rf frontend/src/test"
→ PreToolUse hook fires (Step 2: Hooks)
→ Dangerous command detected
→ Command BLOCKED ✓

# 6. Commit changes
You: "/commit-commands:commit"
→ Plugin generates conventional commit (Step 3: Plugins)
→ Message: "feat: add clear chat button with confirmation"
→ Commit created ✓

# 7. Create pull request
You: "Create a PR for this feature"
→ GitHub plugin fires (Step 3: Plugins)
→ Generates PR title, description, test plan
→ Creates PR on GitHub ✓

# 8. Create architecture diagram
You: "Create a diagram showing the new button's data flow"
→ MCP drawio server fires (Step 7: MCP)
→ Generates .drawio file with visual diagram ✓
```

**What just happened:**
- ✅ **CLAUDE.md** guided the process (Step 1)
- ✅ **Hooks** blocked dangerous commands and protected files (Step 2)
- ✅ **Plugins** caught type errors and created PR (Step 3)
- ✅ **Custom Command** generated component (Step 4)
- ✅ **Custom Agent** handled frontend work (Step 6)
- ✅ **MCP Server** created diagram (Step 7)
- ✅ **settings.json** wired it all together (Step 8)

**Result:** Feature implemented, tested, committed, and PR'd - all with automated safety checks and quality verification.

---

## 🎯 Key Takeaways for Labcamp

### Productivity Gains

1. **Safety:** Hooks prevent destructive operations and protect sensitive files
2. **Quality:** Plugins catch type errors before runtime
3. **Speed:** Commands and skills reduce multi-step workflows to one command
4. **Collaboration:** Agents handle specialized tasks in parallel
5. **Integration:** MCP connects to any external tool or service
6. **Context:** Project rules and architecture documented in CLAUDE.md

### Best Practices

1. **Document everything** in CLAUDE.md (commands, rules, architecture)
2. **Use hooks** for automated formatting and safety checks
3. **Install plugins** for type checking and IDE features
4. **Create commands** for common repetitive tasks
5. **Define skills** for complex multi-step workflows
6. **Leverage agents** for specialized work (backend, frontend, review)
7. **Add MCP servers** for external tool integration
8. **Centralize config** in settings.json

### Common Pitfalls to Avoid

❌ **Don't skip CLAUDE.md** - It's the foundation of project understanding
❌ **Don't disable hooks** - They prevent accidents and ensure consistency
❌ **Don't ignore plugins** - Type checking saves hours of debugging
❌ **Don't commit secrets** - Hooks protect .env but always double-check
❌ **Don't bypass tests** - All tests must pass before committing

---

## 📚 Additional Resources

### Official Documentation
- **Claude Code:** [code.claude.com/docs](https://code.claude.com/docs)
- **CLAUDE.md Guide:** [code.claude.com/docs/en/memory](https://code.claude.com/docs/en/memory)
- **Hooks Reference:** [code.claude.com/docs/en/hooks](https://code.claude.com/docs/en/hooks)
- **Plugins Guide:** [code.claude.com/docs/en/discover-plugins](https://code.claude.com/docs/en/discover-plugins)
- **MCP Specification:** [modelcontextprotocol.io](https://modelcontextprotocol.io)

### Framework Documentation
- **FastAPI:** [fastapi.tiangolo.com](https://fastapi.tiangolo.com/)
- **Strands SDK:** [strandsagents.com/docs](https://strandsagents.com/docs/)
- **React:** [react.dev](https://react.dev/)
- **Tailwind CSS:** [tailwindcss.com](https://tailwindcss.com/)

### Community & Support
- **GitHub Issues:** [github.com/anthropics/claude-code/issues](https://github.com/anthropics/claude-code/issues)
- **Plugin Marketplace:** [claude.com/plugins](https://claude.com/plugins)
- **MCP Servers:** [github.com/modelcontextprotocol/servers](https://github.com/modelcontextprotocol/servers)

---

## 🎨 Real-World Example: Transforming the Grey UI

**Problem:** The frontend appeared grey and washed out despite having a dark glassmorphism design in the code.

**Solution:** Used multiple Claude Code features working together to diagnose and fix the issue.

### Step-by-Step Workflow

#### 1. Visual Inspection (MCP + Custom Agent)
```
User: "The frontend is just grey with no colors, why?"
Claude: [Launches frontend-visual-inspector agent]
```

**What happened:**
- Agent used **chrome-devtools MCP server** to take screenshots
- Analyzed the UI and identified the problem:
  - Low opacity colors (blue-500/10, purple-500/10)
  - Over-transparent glassmorphism (white/[0.02])
  - Dark slate backgrounds making accents invisible

**Screenshot captured:**
![Before: Grey, washed-out UI with minimal color]

#### 2. Visual Improvements (Custom Agent + Tool Use)
```
Claude: [Launches frontend-improver agent]
```

**What happened:**
- Agent modified 4 component files simultaneously:
  - `App.tsx` - Boosted gradient blob opacity (/10 → /20)
  - `ChatInterface.tsx` - Enhanced glassmorphism surfaces
  - `MessageList.tsx` - Purple-tinted assistant messages
  - `MessageInput.tsx` - More prominent input field

**Changes made:**
- Doubled background gradient opacity for vibrant blue/purple glow
- Brightened glassmorphism surfaces (white/[0.02] → white/[0.05])
- Bold gradients on icons (blue-500 to purple-600)
- Color-coded capability pills (blue for weather, purple for math)
- Enhanced focus states with glowing effects

#### 3. Problem Discovery (MCP Browser Tools)
```
Claude: [Takes screenshot after changes]
Result: Still showing grey/white!
```

**What happened:**
- Used **chrome-devtools MCP** to reload page and take fresh screenshot
- Used `evaluate_script` to inspect computed styles:
  ```javascript
  classList: ["bg-gradient-to-br", "from-slate-900", "via-slate-800"]
  backgroundImage: "none"  // ❌ Classes present but CSS not applied!
  ```

**Root cause identified:** Tailwind CSS v4 compatibility issue

#### 4. Fix Applied (Direct Tool Use)
```
Claude: [Reads package.json, identifies Tailwind v4]
```

**What happened:**
- Discovered project uses Tailwind v4 (`tailwindcss: ^4.2.2`)
- Tailwind v4 changed import syntax
- **Old (v3):** `@tailwind base; @tailwind components; @tailwind utilities;`
- **New (v4):** `@import "tailwindcss";`

**Fix:**
```diff
- @tailwind base;
- @tailwind components;
- @tailwind utilities;
+ @import "tailwindcss";
```

#### 5. Verification (MCP + Testing)
```
Claude: [Reloads page with cache clear, takes screenshot]
```

**Result:** ✅ **Success!**

**Screenshot captured:**
![After: Vibrant dark theme with blue/purple gradients, glassmorphism effects, color-coded elements]

**Visual improvements confirmed:**
- ✅ Dark gradient background visible (slate-900 to slate-800)
- ✅ Blue and purple ambient glows in corners
- ✅ Glassmorphism card with frosted glass effect
- ✅ Vibrant emerald status badge
- ✅ Color-coded capability pills (blue, purple, neutral)
- ✅ Bold gradient on empty state icon
- ✅ Enhanced input field with better contrast

#### 6. Quality Assurance (Hooks + Testing)
```
Claude: [Runs test suite before committing]
```

**What happened:**
- **Testing hook** automatically triggered
- Backend: 43 tests passed ✅
- Frontend: 19 tests passed ✅
- No regressions introduced

#### 7. Commit and Push (Plugin + Convention)
```
Claude: [Creates conventional commit and pushes]
```

**Commit message:**
```
feat: enhance UI with vibrant colors and fix Tailwind v4 compatibility

Visual improvements:
- Increase gradient blob opacity from /10 to /20
- Brighten glassmorphism surfaces
- Bold gradients on empty state icon
- Color-coded capability pills

Technical fix:
- Fix Tailwind CSS v4 compatibility
```

### Features Used in This Workflow

| Feature | How It Was Used |
|---------|----------------|
| **Custom Agents** | frontend-visual-inspector + frontend-improver agents |
| **MCP Servers** | chrome-devtools for screenshots, browser automation, script evaluation |
| **Direct Tools** | Read (inspect code), Edit (fix CSS), Bash (run tests) |
| **Hooks** | Testing hook verified no regressions |
| **Plugins** | TypeScript LSP caught any type errors in component changes |
| **CLAUDE.md** | Guided testing requirements and commit format |
| **settings.json** | Enabled MCP servers and configured hooks |

### Key Takeaways

1. **Multi-agent collaboration** - Visual-inspector diagnosed, frontend-improver fixed
2. **MCP integration** - Browser automation provided real-time visual feedback
3. **Root cause analysis** - DevTools revealed CSS wasn't applying despite correct classes
4. **Automated testing** - Hooks ensured quality throughout the workflow
5. **Professional workflow** - From diagnosis to fix to commit, all automated

**Time saved:** What would have taken 30+ minutes of manual debugging, browser refreshing, and trial-and-error was completed in minutes with Claude Code's integrated tooling.

**Result:** A production-ready, visually stunning dark theme with glassmorphism effects and vibrant color accents, all tested and committed with zero regressions.

---

## 🤝 Contributing

This project is for educational purposes (ClaudeCode Labcamp). To contribute:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'feat: add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

**Commit Format:** Use conventional commits (feat:, fix:, chore:, docs:, test:)

---

## 📄 License

This project is part of the ClaudeCode Labcamp learning environment.

---

## 🙏 Acknowledgments

- Built with [Claude 4](https://www.anthropic.com/claude) via Amazon Bedrock
- Powered by [Strands Agents SDK](https://strandsagents.com/)
- UI components styled with [Tailwind CSS](https://tailwindcss.com/)
- Development accelerated with [Claude Code](https://claude.ai/code)

---

**Happy coding! 🚀**

*This project demonstrates how Claude Code's 8 core features work together to boost daily productivity through automation, safety, and verification.*
