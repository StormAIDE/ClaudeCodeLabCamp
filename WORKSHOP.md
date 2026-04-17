# ClaudeCode LabCamp Workshop Guide

**Welcome to the hands-on ClaudeCode workshop!** 

In this lab, you'll build your own AI-powered personal assistant from scratch, learning professional development workflows with Claude Code. By the end, you'll have a working full-stack application and understand how to use Claude Code plugins, hooks, and AI agent patterns.

**🎯 Workshop Philosophy: "Add Feature → Test Feature → See The Improvement"**

After adding each Claude Code service (plugins, commands, hooks, skills, agents, MCP), you'll immediately test it and see how it improves your development workflow!

---

## 🎯 What You'll Build

**Project:** A personal AI assistant that can:
- Answer questions about your favorite topics (movies, books, sports, etc.)
- Perform calculations
- Tell jokes
- Remember conversation context
- Stream responses in real-time

**Tech Stack:**
- Backend: Python + FastAPI + Strands SDK
- Frontend: React + TypeScript + Vite
- AI: Claude via Amazon Bedrock

---

## 🎓 Claude Code Features You'll Master

This workshop covers **all major Claude Code features** through hands-on practice:

### 🔧 Core Features
- **File Operations**: Read, write, edit, search code
- **Terminal Integration**: Run commands, manage processes
- **Git Workflows**: Commit, branch, PR creation

### 🔌 Plugins (Lab 6)
- **Language Servers (LSP)**: Real-time type checking for TypeScript & Python
- **GitHub Integration**: PR reviews, issue management
- **Plugin Marketplace**: Browse and install community plugins

### 📝 Commands & Skills (Lab 7)
- **Commands**: Reusable prompt templates (`/test-all`, `/component`)
- **Skills**: Multi-step workflows (`/commit`, `/review`, `/init`)
- **Custom Creation**: Build your own commands and skills

### 🪝 Hooks (Lab 8)
- **PreToolUse**: Run checks before actions (file protection, safety)
- **PostToolUse**: Automate after actions (test runs, linting)
- **SessionStart**: Initialize project context on startup

### 🤖 Agents (Lab 9)
- **Specialized Agents**: Code reviewers, testers, frontend specialists
- **Agent Delegation**: Assign tasks to expert agents
- **Agent Memory**: Persistent learning across invocations

### 🔌 MCP Servers (Lab 10)
- **Chrome DevTools**: Browser automation, screenshots, debugging
- **Visual Inspector Agent**: Agent that uses MCP to "see" the frontend
- **Draw.io**: Architecture diagram generation

### ⚙️ Settings & Configuration (Throughout)
- **CLAUDE.md**: Project-specific instructions for Claude
- **settings.json**: Hook configuration and automation
- **.mcp.json**: MCP server configuration

---

## 📋 Prerequisites

Before starting, ensure you have:
- [ ] Python 3.9+ installed
- [ ] Node.js 18+ and npm installed
- [ ] Git installed
- [ ] AWS account with Bedrock access (for Claude AI models)
- [ ] AWS credentials (Access Key ID & Secret Access Key)
- [ ] GitHub account (for version control and CI/CD)
- [ ] VS Code or preferred code editor

**Check your setup:**
```bash
python --version    # Should be 3.9+
node --version      # Should be 18+
npm --version
git --version
aws --version       # AWS CLI should be installed
```

**Note:** We'll install Claude Code in the first step below!

---

## 🚀 Getting Started: Install Claude Code

### Before Lab 0: Install Claude Code CLI

**You need to install Claude Code first!**

#### Option 1: Install in VS Code (Mac - Recommended)

**Open VS Code terminal and run:**

```bash
# Install Claude Code CLI
curl -fsSL https://claude.ai/install.sh | bash
```

**After installation:**
```bash
# Verify installation
claudecode --version
```

✅ You should see the Claude Code version number!

#### Option 2: Install for Other Operating Systems

**Follow the official installation guide:**

👉 **[https://code.claude.com/docs/en/quickstart](https://code.claude.com/docs/en/quickstart)**

This guide covers:
- **Windows**: Installation via PowerShell
- **Linux**: Installation via bash script
- **macOS**: Alternative installation methods
- **Desktop App**: Download standalone app
- **VS Code Extension**: Install directly in VS Code

**✅ Test Installation:**
```bash
claudecode --version
# Should display: Claude Code v[version number]
```

**🎯 What This Enables:**
- ✨ Chat with Claude directly from your terminal
- ✨ Claude can read, write, and execute code
- ✨ Seamless integration with your development workflow
- ✨ Access to Claude 4 via Amazon Bedrock

---

## 🛠️ Lab 0: Initial Setup (Before Starting Claude Code)

**Now that Claude Code is installed, let's prepare the project environment:**

### Step 0.1: Create Project Folder and Setup Version Control

**Do this BEFORE starting Claude Code:**

```bash
# 1. Create your project folder
mkdir my-ai-assistant
cd my-ai-assistant

# 2. Create README.md (so you have something to commit)
echo "# My AI Assistant" > README.md
echo "AI-powered personal assistant built with Claude Code" >> README.md

# 3. Initialize git repository
git init
git add README.md
git commit -m "Initial commit"
```

**💡 Why do this first?** You need an existing folder with git initialized so Claude Code can work with it.

### Step 0.2: Create Python Virtual Environment

```bash
# Create Python virtual environment
python -m venv venv

# Activate it (you'll need this activated later)
# On Mac/Linux:
source venv/bin/activate
# On Windows:
# venv\Scripts\activate
```

**💡 Why?** Python dependencies will be isolated to this project.

### Step 0.3: Create GitHub Repository and Push

**Create the remote repository:**

1. Go to GitHub.com and create a new repository (e.g., "my-ai-assistant")
2. Don't initialize with README (you already have one)
3. Copy the HTTPS URL (e.g., `https://github.com/yourusername/my-ai-assistant.git`)

**Connect and push:**

```bash
# Add remote repository
git remote add origin https://github.com/yourusername/my-ai-assistant.git

# Push to GitHub
git branch -M main
git push -u origin main
```

**✅ Test It:** Visit your GitHub repo URL - you should see your README!

### Step 0.4: Configure AWS Profile (for Bedrock Access)

**Create AWS credentials file or configure profile:**

```bash
# Option 1: Use aws configure
aws configure --profile my-ai-assistant
# Enter your:
# - AWS Access Key ID
# - AWS Secret Access Key
# - Default region (e.g., us-east-1)
# - Output format (json)

# Option 2: Or manually create ~/.aws/credentials
# [my-ai-assistant]
# aws_access_key_id = YOUR_KEY
# aws_secret_access_key = YOUR_SECRET
# region = us-east-1
```

**✅ Test It:**
```bash
aws configure list --profile my-ai-assistant
# Should show your configured credentials
```

**💡 Why?** Claude Code needs AWS Bedrock access to use Claude AI models.

---

**📋 Setup Complete - Verify Your Environment**

At this point, you should have VS Code open in your project folder with a terminal ready.

**Checklist:**
- ✅ Project folder created
- ✅ Python virtual environment (venv/)
- ✅ Git initialized with initial commit
- ✅ GitHub remote repository connected
- ✅ AWS credentials configured
- ✅ VS Code open in project directory
- ✅ Terminal open in VS Code (View → Terminal)

**Quick verification commands:**
```bash
pwd                    # Should show path to my-ai-assistant
git status            # Should show clean working tree
git remote -v         # Should show your GitHub repo
ls -la                # Should see: venv/, .git/, README.md
```

**💡 Note:** If VS Code prompts "Do you trust the authors of the files in this folder?" - click "Yes, I trust the authors"

---

## 🚀 Lab 1: Connect Claude Code and Start Building

### Step 1.1: Start Claude Code

**In your VS Code terminal (or regular terminal in project directory):**

```bash
# Make sure you're in the project directory
cd my-ai-assistant

# Start Claude Code
claudecode
```

**First-time setup - You'll be prompted:**

1. **"How would you like to connect to Claude?"**
   - Select: **"Amazon Bedrock"**

2. **"Select AWS profile:"**
   - Select: **"my-ai-assistant"** (or whatever you named it)

3. **Connection established!** You'll see the Claude Code prompt.

**✅ Test It - Say Hi:**
```
Hi! Can you confirm you're connected and ready to help?
```

**Claude should respond** - connection successful! 🎉

---

### Step 1.2: Connect GitHub CLI for Automated Git Operations

**Ask Claude Code to help you set up GitHub CLI:**

```
How do I connect GitHub CLI so you can automatically commit and push changes for me?
```

**Claude will help you:**
1. Install `gh` if not present (via homebrew/apt/etc)
2. Provide the authentication command: `gh auth login`

**Follow the prompts:**
```bash
# Exit from Claude Code first
# Run this in the terminal
gh auth login

# Select:
# - GitHub.com
# - HTTPS
# - Yes (authenticate Git)
# - Login with a web browser

# You'll get a code & URL
# Open URL in browser - enter the code
# Authorize GitHub CLI
# Back in terminal, press Enter
```

**✅ Test It:**
```bash
gh auth status
# Should show: "Logged in to github.com"
```

**💡 Why?** This allows Claude Code to automatically push commits to GitHub for you.

---

### Step 1.3: Reopen Claude Code with GitHub Access

**Important:** Reopen Claude Code so it can use the GitHub credentials:

```bash
# Exit Claude Code (Ctrl+C or type /exit)

# Reopen it
claudecode
```

Now Claude Code has GitHub CLI access in the same terminal session!

### Step 1.4: Give Claude Your GitHub Repository URL

**Tell Claude about your repository and workflow preferences:**

```
Remember this for future sessions:
- My GitHub repository is: https://github.com/yourusername/my-ai-assistant.git
- After every feature or fix, please commit with a descriptive message and push to GitHub
- Use conventional commit format: feat:, fix:, chore:, docs:, test:
- Always run tests before committing
```

**Claude will remember** these preferences!

---

### Step 1.5: Initialize CLAUDE.md for Project Memory

**Ask Claude to create project documentation:**

```
/init
```

**OR manually ask:**
```
Create a CLAUDE.md file that documents:
- Project structure and tech stack
- How to run backend and frontend
- Testing commands
- Important rules (ports, commit format, etc.)
- AWS and GitHub setup
```

**✅ Test It - Restart Claude Code:**
```bash
# Exit and reopen
claudecode

# Ask:
"What this project is about?"
```

**Claude should reference CLAUDE.md** and know the project setup!

---

## 🏗️ Lab 2: Let Claude Code Build Your Project

### Step 2.1: Ask Claude to Create Project Structure

**Now that setup is complete, let Claude Code do the heavy lifting!**

**Let's use plan mode so Claude shows you what it will build before executing:**

**Type this prompt (but don't press Enter yet!):**
```
Create a complete, working full-stack AI assistant project using Strands Agents SDK.

Reference: https://strandsagents.com/docs/user-guide/quickstart/python/

Build a fully functional AI assistant with:

**Backend (Python + FastAPI + Strands SDK):**
- Agent service with Claude AI via Bedrock
- Tools: weather lookup, calculator, joke generator
- Chat API endpoint (POST /api/v1/chat)
- Health check endpoint
- Error handling and validation

**Frontend (React + TypeScript + Vite):**
- Chat interface with message history
- Input field and send button
- Display user/assistant messages
- Loading states
- Modern, clean UI

**Configuration & Setup:**
- .env.example and .env (CLAUDE_MODEL_ID, APP_NAME, API_PORT)
- .gitignore (exclude .env, venv/, node_modules/)
- requirements.txt and package.json
- Complete README with setup instructions

**Architecture:**
- Clean separation of concerns
- Modular code structure
- API-first design

Make it a complete, working project ready to run immediately.
```

**Before pressing Enter, press Shift+Tab to switch to Plan Mode!**

You'll see the mode indicator change to "Plan" at the bottom of the prompt.

**Now press Enter to submit.**

**Claude will show you a detailed plan:**
- What files will be created
- What the architecture will look like
- What dependencies will be installed

**Review the plan, then approve it to execute!**

**🎯 What This Improves:**
- ✨ **Before Claude Code**: Manually create each directory and file
- ✨ **With Claude Code**: Entire project structure in one command
- ✨ **With Plan Mode**: See what will happen before it executes
- ✨ **Time Saved**: 5-10 minutes → 30 seconds

**Claude Code Feature Learned:** Multi-step project scaffolding with plan mode

---

### Step 2.2: Start and Test the Application

**Now let's start the application! Ask Claude Code to do it:**

```
Start the application:
1. Activate the Python virtual environment
2. Install backend dependencies from requirements.txt
3. Start the FastAPI backend on port 8000 in the background
4. Install frontend dependencies
5. Start the Vite frontend on port 5173 in the background
6. Show me the URLs when both are running
```

**Watch Claude:**
- Activates venv
- Installs Python dependencies
- Starts backend server (background)
- Installs npm dependencies  
- Starts frontend server (background)
- Reports both are running

**✅ Verify Everything Works:**
- Backend health: http://localhost:8000/health
- API docs: http://localhost:8000/docs
- Frontend app: http://localhost:5173
- **Test the chat**: Send a message like "Tell me a joke" or "Calculate 42 * 37"

**🎯 What This Improves:**
- ✨ **Before Claude Code**: Days of manual coding
- ✨ **With Claude Code**: Complete working app in minutes
- ✨ **Time Saved**: 2-3 days → 10 minutes
- ✨ **Achievement**: Full-stack AI agent with tools, working end-to-end!

**Claude Code Feature Learned:** Complete project generation with one prompt

---

## 🎨 Lab 3: Share UI Design Ideas with Image Pasting

### Step 3.1: Paste Your Design Inspiration

**Now that you have a base project, let's make the UI look amazing!**

One of Claude Code's powerful features is that it can understand images - perfect for showing design inspiration!

**Do you have a chat interface design you like?** You can paste an image directly into the Claude Code chat!

**How to paste an image:**
1. Find an image of a chat interface you like (from Dribbble, Behance, or even a screenshot of your favorite app)
2. Copy the image to your clipboard
3. Press `Ctrl+V` in the Claude Code chat
4. Claude will see the image and understand the design!

**Ask Claude Code:**
```
Here's the design I want for my AI assistant chat interface. 
Can you update the frontend to look like this?
```

**What Claude can extract from your design image:**
- Color scheme and theme (purple, blue, dark mode, etc.)
- Layout structure (header, message list, input area)
- Message bubble styles (rounded, flat, shadows)
- Interactive elements (buttons, quick replies, typing indicators)
- Typography and spacing preferences
- Status indicators (online, typing, etc.)

**✅ Test It:**
After pasting your design image, Claude will analyze it and can:
1. Describe the design elements it sees
2. Update the React components to match the design
3. Apply appropriate CSS/Tailwind classes for styling
4. Adjust colors, spacing, and layout

**🎯 What This Improves:**
- ✨ **Before**: Try to describe design in words ("make it purple-ish with round bubbles...")
- ✨ **With Image**: Show exactly what you want - Claude sees it visually
- ✨ **Benefit**: Start with clear design goals, save hours of design iteration
- ✨ **Time Saved**: Skip the guesswork - Claude understands your vision immediately

**Example interaction:**
```
You: [Paste image of a modern chat interface]
"I love this chat design with the purple theme and bubble-style messages. 
Can you update our chat interface to look like this?"

Claude: "I can see this is a modern chat interface with:
- Purple-themed header with bot avatar and 'Online' status
- Clean message bubbles with rounded corners
- Interactive button options for user responses
- Smooth animations and good spacing

I'll update the ChatInterface component to match this design..."
```

**💡 Pro Tip:** You can paste multiple design references to show different aspects:
- One image for overall layout
- Another for specific components (buttons, inputs)
- A third showing color palette or animations

**No design image?** No problem! You can skip this step and Claude will help you create a clean, modern design from scratch. But if you have visual inspiration, sharing it after the base project helps Claude style the UI perfectly!

---

## 🧪 Lab 4: Testing & CLAUDE.md Configuration

### Step 4.1: Create Comprehensive Test Suite

**Ask Claude Code:**
```
Create a comprehensive test suite for both backend and frontend that covers:
- API endpoints and health checks
- Configuration loading
- All dependencies are correctly installed and importable
- Main components and functionality
```

**✅ Test It:**
```
Ask Claude: "Run all the tests you just created for both backend and frontend"
```

**Checkpoint:** All tests should pass ✅

**🎯 What This Improves:**
- ✨ **With Tests**: Confidence your code works (both backend AND frontend)
- ✨ **Dependency verification**: Catch missing packages early
- ✨ **Benefit**: Catch bugs before deployment, never commit broken code

### Step 4.2: Create CLAUDE.md (Project Documentation)

**CLAUDE.md tells Claude Code about your project's rules and architecture.**

**Ask Claude Code:**
Type in claudecode chat terminal
```
/init
```

**✅ Test It - See Claude Remember:**
```
Restart Claude Code session, then ask:
"How do I run the backend server?"
```

**Watch:** Claude will reference CLAUDE.md automatically!

**🎯 What This Improves:**
- ✨ **Before CLAUDE.md**: Explain project setup every session
- ✨ **With CLAUDE.md**: Claude knows your project automatically
- ✨ **Benefit**: Consistent behavior, less repetition

**Claude Code Feature Learned:** Project documentation with CLAUDE.md

---

### Step 4.3: Set Up Automated Testing Hook

**Ask Claude Code:**
```
Set up automated testing hooks that run tests before every commit:

1. Create .claude/hooks/ folder with a script that runs all tests (backend and frontend)
2. Configure .claude/settings.json to call this script as a PreToolUse hook before commits
3. The hook should block the commit if any tests fail
Here is official docs:
https://code.claude.com/docs/en/hooks-guide
```

**✅ Test It:**
```
Make a small change to README.md
Ask Claude: "Commit this change"
```

**Watch:** Tests run automatically before commit!

**🎯 What This Improves:**
- ✨ **Before Hooks**: Manually remember to run tests
- ✨ **With Hooks**: Tests run automatically before every commit
- ✨ **Benefit**: Never commit broken code

**Understanding hooks:**
- **settings.json** - Defines WHEN hooks run (PreToolUse, PostToolUse, SessionStart)
- **.claude/hooks/** folder - Contains the ACTUAL scripts that execute (.sh files, .txt files)

**Claude Code Feature Learned:** Hooks for workflow automation (we'll explore more in Lab 8)

---

## 🔧 Lab 5: Advanced Features (optional)

### Step 5.1: Add Streaming Responses

**Ask Claude Code:**
```
Implement streaming for real-time responses:
1. Update agent_service.py to use agent.stream_async()
2. Create a new /chat/stream endpoint with Server-Sent Events
3. Update frontend to handle streaming responses
```

**✅ Test It:**
```
Send a message and watch it appear word-by-word in real-time!
```

**🎯 What This Improves:**
- ✨ **Before**: Wait for entire response
- ✨ **With Streaming**: See response as it's generated
- ✨ **Benefit**: Better user experience, feels faster

**Claude Code Feature Learned:** Complex refactoring, async patterns

---

### Step 5.2: Add Tool for Your Interest

**Challenge:** Add a custom tool based on your interests:
- Movie buff? Add `search_movies()` tool
- Sports fan? Add `get_team_stats()` tool
- Weather enthusiast? Add `get_forecast()` tool

**Ask Claude Code:**
```
Add a new tool called [your_tool_name] to the agent that [describe functionality]
```

---

### Step 5.3: Improve UI/UX

**Ask Claude Code:**
```
Enhance the chat interface with:
1. Dark mode toggle
2. Copy button for assistant messages
3. Typing indicator animation
4. Error handling with user-friendly messages
```

---

## 🎓 Lab 6: Plugins for Code Quality

### Step 6.1: Understanding Claude Code Plugins

**What are plugins?**
Plugins extend Claude Code with additional capabilities like language servers, external integrations, and specialized tools.

**✅ Test It - Explore Available Plugins:**
```
/plugin marketplace list
```

**You'll see:**
- LSP plugins (TypeScript, Python, Go, Rust, etc.)
- Integration plugins (GitHub, Linear, etc.)
- Tool plugins

### Step 6.2: Install Language Server Plugins (LSPs)

**LSPs automatically check your code for errors as you work with Claude Code.**

**Install them:**
```
/plugin install typescript-lsp@claude-plugins-official
/plugin install pyright-lsp@claude-plugins-official
/reload-plugins
```

**✅ Test It - See LSP Catch Errors Automatically:**

**Ask Claude Code to make a change:**
```
Add a new feature to the chat interface: display the character count of the user's message below the input field
```

**What happens:**
- Claude will write the code
- **TypeScript LSP automatically checks** for type errors in the background
- If there are any type issues, Claude sees them instantly and fixes them
- You get correct code the first time!

**Try with backend:**
```
Add a new tool to the agent that gets the current time
```

**What happens:**
- Claude writes the Python code
- **Pyright LSP automatically checks** for type errors
- Claude ensures types are correct before showing you the code

**🎯 What This Improves:**
- ✨ **Before LSP**: Claude writes code → you run it → runtime errors → fix → repeat
- ✨ **With LSP**: Claude writes code → LSP validates instantly → you get working code
- ✨ **Benefit**: Fewer bugs, better code quality, no back-and-forth
- ✨ **Time Saved**: Hours of debugging → Prevention before it happens

**Key point:** You don't need to do anything - LSPs work automatically in the background!

**Claude Code Feature Learned:** LSP plugins for automatic code quality

---

### Step 6.3: Install GitHub Plugin (optional)

**Connect Claude Code to GitHub for PR reviews and issue management:**

```
/plugin install github@claude-plugins-official
/reload-plugins
```

**✅ Test It - GitHub Integration:**

1. **Ask Claude Code:**
```
Show me all open pull requests in this repository
```

2. **Ask Claude Code:**
```
Create an issue titled "Add user authentication" with description: "Implement JWT-based authentication for the chat API"
```

**🎯 What This Improves:**
- ✨ **Before**: Switch to GitHub web/CLI for PR/issue management
- ✨ **With Plugin**: Manage GitHub without leaving Claude Code
- ✨ **Benefit**: Seamless workflow, stay in context

**Claude Code Feature Learned:** GitHub integration plugin

---

## 🛠️ Lab 7: Commands & Skills for Rapid Development

### Step 7.1: Create the Component Command

**Let's create a custom `/component` command for rapid React development!**

**Ask Claude Code:**
```
Create a custom slash command called /component following the official Claude Code documentation at https://code.claude.com/docs/en/agent-sdk/slash-commands

The command should:
1. Accept arguments: /component <ComponentName> <description>
2. Generate a fully-typed React + TypeScript component with:
   - Proper TypeScript interfaces
   - Tailwind CSS styling
   - Clean, readable code
   - Best practices (exported component, proper types)
3. Save it to frontend/src/components/<ComponentName>.tsx
4. Follow the project's existing component structure

Example usage: /component LoadingSpinner Shows a loading indicator while content is loading

Use the official docs format for the command file in .claude/commands/
```

**Claude will create** `.claude/commands/component.md` with proper frontmatter and prompt template.

**✅ Test It - Generate Your First Component:**

**Try it:**
```
/component LoadingSpinner Shows a loading indicator
```

**Watch:** Claude generates a fully-typed React component with:
- TypeScript interface
- Tailwind CSS styling
- Proper project structure
- Best practices

**Create more components:**
```
/component ErrorBoundary Catches and displays React errors
/component UserAvatar Displays user profile picture with initials fallback
/component Toast Shows notification messages
```

**Now use a generated component:**
```
Ask Claude: "Use the LoadingSpinner component in ChatInterface while waiting for agent response"
```

**🎯 What This Improves:**
- ✨ **Before**: Manually write each component (10-15 minutes each)
- ✨ **With /component**: Generate in 30 seconds
- ✨ **Benefit**: Consistent code style, faster development
- ✨ **Time Saved**: 10 minutes → 30 seconds per component

**Claude Code Feature Learned:** Custom command creation using official SDK docs

---

### Step 7.2: Create Your Own Custom Command

**Commands are reusable prompt templates in `.claude/commands/`.**

**Ask Claude Code:**
```
Create a custom command called /test-all in .claude/commands/test-all.md that:
1. Activates the virtual environment
2. Runs backend tests with coverage (pytest backend/tests/ --cov=backend)
3. Runs frontend tests (cd frontend && npm test)
4. Reports pass/fail status with color
5. Shows code coverage percentage
```

**Command file structure:**
```markdown
---
name: test-all
description: Run all tests with coverage
usage: /test-all
---

# Run All Tests

Run both backend and frontend test suites with coverage reporting...
```

**✅ Test It:**
```
/test-all
```

**Watch:** All tests run in sequence with coverage reports!

**🎯 What This Improves:**
- ✨ **Before**: Type long test commands manually
- ✨ **With /test-all**: One command runs everything
- ✨ **Benefit**: No more forgotten test steps

**Claude Code Feature Learned:** Custom command creation

---

### Step 7.3: Create the Start-Dev Skill

**Skills are multi-step automated workflows. Let's create one to start both servers!**

**Ask Claude Code:**
```
Create a custom skill called /start-dev that automates starting the development environment.

Reference the official documentation: https://code.claude.com/docs/en/agent-sdk/skills

The skill should:
1. Check if Python virtual environment exists (venv/)
2. Activate the virtual environment
3. Start FastAPI backend in background on port 8000
4. Navigate to frontend directory
5. Start Vite dev server on port 5173
6. Report server status with colored output
7. Show URLs to visit (backend and frontend)
8. Handle errors gracefully (missing dependencies, ports in use)

Create the skill in .claude/skills/start-dev/ with proper SKILL.md structure.
```

**✅ Test It:**
```
/start-dev
```

**Watch Claude:**
1. Check if virtual environment exists
2. Activate Python virtual environment
3. Start FastAPI backend in background (port 8000)
4. Start Vite frontend (port 5173)
5. Report server status
6. Show URLs to visit

**🎯 What This Improves:**
- ✨ **Before**: Open 2 terminals, run 4-5 commands manually
- ✨ **With /start-dev**: One command starts everything
- ✨ **Time Saved**: 2-3 minutes → 10 seconds

**Claude Code Feature Learned:** Custom skills for project workflows

---

### Step 7.4: Use Built-in Skills

**Try the commit skill:**

**✅ Test It - Smart Git Commit:**

1. **Make some changes:**
```
Ask Claude: "Add error handling to the chat endpoint that returns 400 for empty messages"
```

2. **Commit with skill:**
```
/commit
```

**Watch Claude:**
1. Run `git status` to see changes
2. Run `git diff` to review what changed
3. Review git log for commit message style
4. Generate a conventional commit message: "fix: add validation for empty messages in chat endpoint"
5. Run pre-commit hooks (tests!)
6. Create the commit

**🎯 What This Improves:**
- ✨ **Before**: Manual git add, git commit, write message, hope tests pass
- ✨ **With /commit**: Automatic conventional commit with test verification
- ✨ **Benefit**: Consistent commit messages, never commit broken code

**Try other built-in skills:**
```
/init          # Initialize or update CLAUDE.md documentation
/review <PR#>  # Review a pull request
/simplify      # Refactor code for simplicity
```

**Claude Code Feature Learned:** Built-in skills for git workflows

---

### Step 7.5: Create Your Own Custom Skill (optional)

**Skills live in `.claude/skills/` and can have complex logic. Let's create one for system health checks!**

**Ask Claude Code:**
```
Create a custom skill called /check-health following the official Claude Code skills documentation.

Reference: https://code.claude.com/docs/en/agent-sdk/skills

The skill should:
1. Check if backend server is running (curl localhost:8000/health)
2. Check if frontend server is running (curl localhost:5173)
3. If backend is down, show how to start it (activation + python -m backend.main)
4. If frontend is down, show how to start it (cd frontend && npm run dev)
5. Report overall system status with colored output (✅ for running, ❌ for down)
6. Show response times for each service
7. Display the last 3 lines of logs if a service is down

Create the skill in .claude/skills/check-health/SKILL.md with proper frontmatter.
```

**Skill structure:**
```
.claude/skills/check-health/
└── SKILL.md          # Skill prompt and logic
```

**✅ Test It:**
```
Stop the backend server, then run:
/check-health
```

**Watch:** Skill detects backend is down and shows how to start it!

**Try again with both running:**
```
Start both servers, then run:
/check-health
```

**Watch:** See both services reporting healthy with response times!

**🎯 What This Improves:**
- ✨ **Benefit**: Quick system health checks
- ✨ **Benefit**: Helpful debugging when services are down
- ✨ **Time Saved**: Manual curl testing → One command health report

**Claude Code Feature Learned:** Custom skill development with complex logic

---

## 🪝 Lab 8: Hooks for Automated Quality Control

### Step 8.1: Understanding Hooks

**Hooks automatically run actions at specific points in Claude Code's workflow:**
- `PreToolUse` - Before Claude uses a tool (safety checks, validation)
- `PostToolUse` - After Claude uses a tool (tests, linting)
- `SessionStart` - When starting a new session (context loading)

**View current hooks:**
```
Ask Claude: "Show me what hooks are configured in .claude/settings.json"
```

---

### Step 8.2: Create a Pre-Commit Test Hook

**Let's create a hook that automatically runs tests before every commit!**

**Ask Claude Code:**
```
Create a hook that runs tests before every commit using the official hooks documentation: https://code.claude.com/docs/en/hooks-guide

The hook should:
1. Trigger before git commit commands (PreToolUse hook)
2. Run all backend and frontend tests
3. Block the commit if any tests fail
4. Show a clear message: "Running tests before commit..."

Create:
- A shell script in .claude/hooks/ folder that runs the tests
- Configuration in .claude/settings.json to trigger this hook before commits
```

**✅ Test It - Hook Blocks Bad Code:**

1. **Break a test:**
```python
# In backend/tests/test_main.py, change expected status:
def test_health_endpoint():
    response = client.get("/health")
    assert response.status_code == 500  # Wrong! Should be 200
```

2. **Try to commit:**
```
Ask Claude: "Commit all changes with message 'test hook'"
```

**Watch:** Hook runs tests, they fail, and commit is blocked! ❌

3. **Fix the test and try again:**
```python
assert response.status_code == 200  # Correct
```

**Watch:** Hook runs tests, they pass, commit succeeds! ✅

**🎯 What This Improves:**
- ✨ **Before**: Manually remember to run tests before every commit
- ✨ **With Hook**: Tests run automatically, broken code can't be committed
- ✨ **Benefit**: Never break the main branch
- ✨ **Team Benefit**: Entire team protected by automated quality gate

**Claude Code Feature Learned:** Pre-commit hooks for quality gates

---

### Step 8.3: Create a File Protection Hook

**Let's protect sensitive files from accidental edits!**

**Ask Claude Code:**
```
Create a hook that protects sensitive files from being edited using the official hooks documentation: https://code.claude.com/docs/en/hooks-guide

The hook should:
1. Trigger before Edit and Write operations (PreToolUse hook)
2. Block edits to these files:
   - .env (contains secrets - should be edited manually)
   - package-lock.json (managed by npm - use npm install instead)
3. Show helpful error messages explaining why each file is protected

Create:
- A shell script in .claude/hooks/ folder that checks the file path
- Configuration in .claude/settings.json to trigger this hook before Edit/Write
```

**✅ Test It - Hook Protects Secrets:**

**Try to edit .env:**
```
Ask Claude: "Add DEBUG=true to my .env file"
```

**Watch:** Hook blocks the edit with message:
```
❌ Cannot edit .env - this file contains secrets and should be edited manually
```

**Try to edit package-lock.json:**
```
Ask Claude: "Update React version in package-lock.json"
```

**Watch:** Hook blocks with message:
```
❌ Cannot edit package-lock.json - this file is managed by npm. Use 'npm install' instead.
```

**🎯 What This Improves:**
- ✨ **Before**: Accidentally commit secrets or break lock files
- ✨ **With Hook**: Critical files are protected automatically
- ✨ **Benefit**: Security and dependency management safety
- ✨ **Real-World Impact**: Prevented AWS keys being committed!

**Claude Code Feature Learned:** File protection hooks

---

## 🤖 Lab 9: Specialized Agents for Expert Help

### Step 9.1: Understanding Agent Creation

**Agents (subagents) are specialized Claude instances with specific roles, expertise, and tools.**

**Learn more:** https://code.claude.com/docs/en/sub-agents

**General steps to create any agent:**

1. **Open agent interface:** Type `/agents` in Claude Code
2. **Switch to "Library" tab** (shows all available agents)
3. **Click "Create new agent"**
4. **Choose location:** Select **"Personal"** (saves to `~/.claude/agents/` for all projects)
5. **Choose creation method:** Select **"Generate with Claude"**
6. **Describe the agent:** Paste the agent description (we'll provide for each agent)
7. **Select tools:** Choose which tools the agent can use
8. **Select model:** Choose **"Sonnet"** (balanced performance)
9. **Choose color:** Pick a color (helps identify agent in UI)
10. **Configure memory:** Select **"User scope"** (agent remembers across projects)
11. **Save:** Press `s` or `Enter`

**Now let's create 3 specialized agents!**

---

### Step 9.2: Create Code Reviewer Agent

**Agent Purpose:** Reviews code for quality, security, and best practices

**Description to use:**
```
You are a Code Reviewer Agent პასუხისმგ responsible for analyzing and improving the overall quality of the codebase.

## Scope
You review the entire project including:
- Backend (Python, FastAPI, Strands Agents)
- Frontend (React, TypeScript)
- Project structure and architecture
- Git practices and commit quality

## Responsibilities
- Identify bugs, inefficiencies, and code smells
- Suggest improvements for readability and maintainability
- Enforce best practices across frontend and backend
- Ensure consistency in coding standards
- Review API design and data flow
- Check for missing tests or edge cases
- Evaluate performance and scalability risks

## When to Use This Agent
Use this agent when:
- Reviewing new features or changes
- Before committing or merging code
- After major refactoring
- When debugging complex issues
- When improving code quality
- When preparing for production readiness

## Behavior Rules
- Do NOT directly modify code unless explicitly asked
- First analyze, then suggest improvements
- Prioritize critical issues over minor ones
- Provide actionable, specific feedback
- Be structured and clear in review

## Constraints
- Do NOT introduce new features
- Do NOT rewrite code unnecessarily
- Focus on improvement, not over-engineering

## Output Format
Structure your review as:
1. Critical Issues
2. Improvements
3. Suggestions
4. Optional Enhancements


## Output Expectations
- Be concise but thorough
- Reference specific files or sections
- Provide reasoning for each suggestion
```

**Tools to select:** Read-only tools only (Read, Grep, Glob, Bash)

**✅ Agent Created!**

---

### Step 9.3: Create Frontend Improver Agent

**Agent Purpose:** React/UI/UX specialist for frontend development

**Description to use:**

```
You are a Frontend Improver Agent responsible for enhancing the user interface, user experience, and frontend architecture of this project.

## Scope
You own all frontend-related code including:
- React + TypeScript components
- UI/UX design and layout
- API integration layer
- State management
- Styling and responsiveness

## Responsibilities
- Improve UI clarity, usability, and responsiveness
- Ensure consistent design patterns and component reuse
- Optimize frontend performance
- Improve API interaction (loading states, error handling, retries)
- Maintain clean and scalable component architecture
- Ensure accessibility and good UX practices
- Implement real-time or streaming UI when applicable

## When to Use This Agent
Use this agent when:
- Creating or improving UI components
- Enhancing user experience
- Fixing frontend bugs
- Connecting frontend to backend APIs
- Improving performance or responsiveness
- Refactoring frontend structure
- Adding new features to UI

## Behavior Rules
- Always understand the existing UI before making changes
- Maintain consistency in design and components
- Use TypeScript best practices
- Prefer reusable components over duplication
- Ensure proper separation of concerns (UI vs logic)

## Constraints
- Do NOT modify backend code
- Do NOT change API contracts without coordination
- Avoid unnecessary libraries unless justified

## Output Expectations
- Explain UI/UX improvements clearly
- Provide clean, readable React + TypeScript code
- Ensure components are reusable and maintainable
```

**Tools to select:** Read, Write, Edit, Grep, Glob

**✅ Agent Created!**

---

### Step 9.4: Create Backend Maintainer Agent

**Agent Purpose:** FastAPI/Python backend specialist

**Description to use:**

```
You are a Backend Maintainer Agent responsible for designing, improving, and maintaining the backend system of this project.

## Scope
You own all backend-related code including:
- FastAPI application
- API routes and schemas
- Business logic and services
- Integration with Strands Agents SDK
- Data validation and error handling
- Performance and scalability improvements

## Responsibilities
- Ensure backend follows clean architecture principles
- Keep code modular, readable, and well-structured
- Optimize API performance and response times
- Maintain clear separation between routes, services, and agent logic
- Improve and extend AI agent capabilities using Strands Agents SDK
- Ensure structured and consistent API responses (prefer JSON)
- Add logging, monitoring, and error handling where needed
- Ensure compatibility with frontend requirements

## When to Use This Agent
Use this agent when:
- Creating or modifying backend APIs
- Adding new agent capabilities
- Refactoring backend code
- Debugging backend errors
- Improving performance or scalability
- Adding middleware, authentication, or validation
- Integrating external services (via MCP or APIs)

## Behavior Rules
- Always analyze existing backend structure before making changes
- Avoid breaking existing APIs unless explicitly instructed
- Maintain backward compatibility when possible
- Write clean, production-ready Python code
- Prefer reusable services over duplicated logic
- Suggest improvements proactively

## Constraints
- Do NOT modify frontend code
- Do NOT change project-wide architecture without justification
- Do NOT introduce unnecessary dependencies

## Output Expectations
- Clearly explain changes before applying them
- Group related changes logically
- Ensure code is testable and maintainable
```

**Tools to select:** Read, Write, Edit, Grep, Glob, Bash

**✅ Agent Created!**

---

### Step 9.5: Test All Three Agents Together!

**Now that you've created 3 specialized agents, let's use them in a complete workflow!**

**Scenario:** Add a new chat history feature to your AI assistant

**Ask Claude Code:**
```
I want to add a chat history feature with these requirements:

1. Backend: Create a GET /api/v1/chat/history endpoint that returns the last 10 messages
2. Frontend: Add a "History" button in the ChatInterface that opens a modal showing message history
3. Code Review: Review all new code for quality, security, and best practices

Use the appropriate specialized agents for each step.
```

**Watch Claude orchestrate the agents:**

1. **backend-maintainer** creates the new API endpoint with proper error handling
2. **code-reviewer** analyzes the backend code for issues
3. **frontend-improver** builds the History button and modal component
4. **code-reviewer** checks the React component for best practices

**Expected workflow output:**
```
✅ Backend endpoint created at backend/api/endpoints/agent.py
✅ Code review: No critical issues, 2 suggestions implemented
✅ Frontend History component created at frontend/src/components/ChatHistory.tsx
✅ Code review: Added accessibility attributes, improved TypeScript types
```

**🎯 What This Improves:**
- ✨ **Before**: You build backend → build frontend → manually review → hope you didn't miss anything
- ✨ **With Agents**: Expert specialists handle each part with automatic quality checks
- ✨ **Benefit**: Production-ready code with comprehensive review
- ✨ **Time Saved**: 3-4 hours → 30-45 minutes with full expert review

**Try another workflow:**
```
Add input validation to the chat endpoint to reject empty messages, then review
the changes for security and best practices
```

**Claude Code Feature Learned:** Complete agent-powered development workflow

**💡 What's Missing?** We can't see how the UI actually looks! In Lab 10, we'll add MCP for browser testing and create a visual-inspector agent that can take screenshots.

---

### Step 9.6: (Optional) Create Your Own Custom Agent

**Create a specialized agent for testing.**

**Ask Claude Code:**
```
Create a custom agent called test-engineer in .claude/agents/test-engineer.md that:
1. Specializes in test automation
2. Generates comprehensive test cases for pytest and vitest
3. Identifies edge cases
4. Achieves 90%+ code coverage
5. Follows TDD (Test-Driven Development) principles
6. Writes descriptive test names and clear assertions
```

**Agent file structure:**
```markdown
---
name: test-engineer
description: Test automation specialist for pytest and vitest
model: sonnet
---

# Test Engineer Agent

You are a test automation expert specializing in Python (pytest) and TypeScript (vitest) testing...

## Your Responsibilities
1. Generate comprehensive test suites
2. Identify edge cases and error conditions
3. Write clear, maintainable tests
4. Achieve high code coverage
5. Follow testing best practices

## Testing Patterns
- Arrange-Act-Assert pattern
- Test isolation with mocks/fixtures
- Descriptive test names (test_should_<expected>_when_<condition>)
...
```

**✅ Test It:**
```
Ask Claude: "Use the test-engineer agent to create comprehensive tests for my calculator tool in agent_service.py"
```

**Watch the agent generate:**
```python
def test_calculate_should_return_sum_when_given_addition():
    result = calculate("2 + 2")
    assert result == 4

def test_calculate_should_return_product_when_given_multiplication():
    result = calculate("6 * 7")
    assert result == 42

def test_calculate_should_handle_float_precision():
    result = calculate("0.1 + 0.2")
    assert abs(result - 0.3) < 0.001

def test_calculate_should_raise_error_when_given_invalid_expression():
    with pytest.raises(ValueError):
        calculate("import os")

def test_calculate_should_handle_division_by_zero():
    with pytest.raises(ZeroDivisionError):
        calculate("1 / 0")
```

**🎯 What This Improves:**
- ✨ **Before**: Write tests yourself, might miss edge cases
- ✨ **With Agent**: Comprehensive test suite with edge cases
- ✨ **Benefit**: Higher quality, better coverage, catch bugs early
- ✨ **Time Saved**: 1-2 hours of test writing → 10 minutes

**Claude Code Feature Learned:** Custom agent creation

---

### Step 9.7: (Optional) Agent Memory

**Agents can remember preferences and learnings across invocations.**

**✅ Test It - Teach an Agent:**

**Tell the code-reviewer agent:**
```
Tell the code-reviewer agent to remember these project standards:
- We prefer async/await over .then() for promises
- All Python functions must have type hints
- Error messages should be user-friendly, not technical
- We use conventional commits (feat:, fix:, etc.)
- Backend port is 8000, frontend is 5173 (never change)
```

**Then later, ask:**
```
Use the code-reviewer agent to review this code:
def get_user(id):
    return db.query().then(lambda x: x)
```

**Watch:** Agent will remember your standards and flag both issues:
```
❌ Missing type hints (violates project standard)
❌ Using .then() instead of async/await (violates project standard)
```

**Check agent memory:**
```
Ask Claude: "Show me what the code-reviewer agent remembers about this project"
```

**🎯 What This Improves:**
- ✨ **Before**: Repeat preferences to agents every time
- ✨ **With Memory**: Agents learn and remember project standards
- ✨ **Benefit**: Consistent behavior, agents get smarter over time

**Claude Code Feature Learned:** Agent memory systems

---

## 🔌 Lab 10: MCP & Visual Testing Agent

### Step 10.1: The Problem - We Can't See the Frontend!

**In Lab 9, we created agents to improve our frontend, but there's a problem:**

Our agents are "blind" - they can read code, but they can't see how the UI actually looks!

```
❌ Frontend-improver can read ChatInterface.tsx
❌ But it can't see if buttons are cut off on mobile
❌ It can't detect visual bugs or layout issues
❌ It doesn't know if colors clash or text is unreadable
```

**The solution? MCP (Model Context Protocol) + A Visual Inspector Agent!**

---

### Step 10.2: Understanding MCP

**MCP (Model Context Protocol) connects Claude Code to external tools.**

Learn more: https://code.claude.com/docs/en/mcp

**What MCP enables:**
- Browser automation (screenshots, clicking, testing)
- External APIs (Slack, GitHub, databases)
- Custom tools specific to your project

**We'll use:** Chrome DevTools MCP for browser automation

---

### Step 10.3: Install Chrome DevTools MCP

**Let's install the MCP server that gives Claude browser automation powers!**

**Ask Claude Code:**
```
Install the Chrome DevTools MCP server so we can take screenshots and test the frontend visually.

Add it to .mcp.json configuration.
```

**Claude will create/update `.mcp.json`:**
```json
{
  "mcpServers": {
    "chrome-devtools": {
      "command": "npx",
      "args": ["-y", "chrome-devtools-mcp@latest"]
    }
  }
}
```

**Important: Restart Claude Code**
```
Exit Claude Code (Ctrl+C or type /exit)
Then restart: claudecode
```

**When you restart, Claude will ask permission to use the Chrome DevTools MCP server - approve it!**

---

**✅ Test It:**
```
Use Chrome DevTools MCP to open http://localhost:5173 and take a screenshot
```

**Watch Claude:**
1. Launch browser
2. Navigate to localhost:5173
3. Take a screenshot
4. You'll see the screenshot in Claude's response!

**✅ MCP is working!**

---

### Step 10.4: Create Visual Inspector Agent (Using MCP!)

**Now that we have MCP, let's create an agent that can "see" the frontend!**

**Type in Claude Code:**
```
/agents
```

**Create the agent:**

**Agent Purpose:** Visual testing specialist using Chrome DevTools MCP

**Description to use:**
```
A visual testing specialist that uses Chrome DevTools MCP to take screenshots, 
test responsive design across device sizes, check console errors, and provide 
visual feedback about the UI. Helps frontend-improver agent know what actually 
needs improvement.
```

**Tools to select:** Read, Write, Bash, Edit, **All MCP chrome-devtools tools**

**✅ Agent Created!**

---

### Step 10.5: Use Visual Inspector to Help Frontend Improver!

**Now let's see the power of combining agents + MCP!**

**Scenario:** Improve the chat interface based on visual testing

**Ask Claude Code:**
```
I want to improve the chat interface:

1. Use visual-inspector agent to take screenshots at mobile (375px), tablet (768px), 
   and desktop (1920px) sizes
2. Identify any visual bugs or layout issues
3. Use frontend-improver agent to fix the issues found

Work together to make the UI perfect across all devices!
```

**Watch the workflow:**
1. **visual-inspector** launches browser, takes 3 screenshots
2. **visual-inspector** analyzes: "Send button cut off on mobile, chat too wide on desktop"
3. **frontend-improver** reads the visual feedback
4. **frontend-improver** fixes ChatInterface.tsx with proper responsive styles
5. **visual-inspector** takes new screenshots to verify fixes

**This is the power of agents + MCP working together!**

**🎯 What This Improves:**
- ✨ **Before**: Frontend-improver is blind, can't see visual issues
- ✨ **With visual-inspector + MCP**: Frontend-improver gets eyes!
- ✨ **Benefit**: Fix real visual bugs, not just code issues
- ✨ **Time Saved**: Hours of manual testing → Automated visual QA

**Claude Code Feature Learned:** Agent + MCP integration for visual testing

---

### Step 10.6: Install Draw.io MCP for Architecture Diagrams

**Now let's add another MCP server for creating architecture diagrams!**

**Learn more:** https://www.drawio.com/doc/faq/ai-drawio-generation

**Ask Claude Code:**
```
Install the Draw.io MCP server so we can generate architecture diagrams.

Add the MCP server from: https://www.drawio.com/doc/faq/ai-drawio-generation

Add it to .mcp.json configuration.
```

**Claude will update `.mcp.json`:**
```json
{
  "mcpServers": {
    "chrome-devtools": {
      "command": "npx",
      "args": ["-y", "chrome-devtools-mcp@latest"]
    },
    "drawio": {
      "command": "npx",
      "args": ["-y", "@drawio/mcp"]
    }
  }
}
```

**Important: Restart Claude Code**
```
Exit Claude Code (Ctrl+C or type /exit)
Then restart: claudecode
```

**When you restart, Claude will ask permission to use the Draw.io MCP server - approve it!**

---

### Step 10.7: Generate Architecture Diagrams

**Now let's use Draw.io MCP to document our system!**

**Ask Claude Code:**
```
Use Draw.io MCP to create a system architecture diagram showing:
1. User (browser)
2. React Frontend (port 5173)
3. FastAPI Backend (port 8000)
4. AgentService (using Strands SDK)
5. Claude AI (via Amazon Bedrock)
6. Show data flow with arrows: User → Frontend → Backend → Agent → Claude → Response

Use boxes for components and arrows for data flow.
```

**Watch:** Claude generates a professional diagram!

**The diagram shows:**
```
[User Browser]
      ↓
[React Frontend :5173]
      ↓ POST /api/v1/chat
[FastAPI Backend :8000]
      ↓
[AgentService (Strands SDK)]
      ↓ Bedrock API
[Claude AI]
      ↓ Response
[Back to User]
```

**Try more diagrams:**
```
Create a sequence diagram showing the chat message flow with timing
```

**🎯 What This Improves:**
- ✨ **Before**: Manually create diagrams in Draw.io or Lucidchart (30-60 minutes)
- ✨ **With MCP**: Generate diagrams from text description (2 minutes)
- ✨ **Benefit**: Keep architecture docs up to date easily
- ✨ **Use Case**: Documentation, onboarding, design discussions

**Claude Code Feature Learned:** Architecture diagram generation with MCP

---

## 🧪 Lab 11: Comprehensive Testing & Quality Assurance

### Step 11.1: Add Full Test Suite

**Ask Claude Code:**
```
Create a comprehensive test suite with 80%+ coverage:

Backend tests (backend/tests/):
1. test_agent_service.py - Test all agent tools (get_joke, calculate)
2. test_chat_endpoint.py - API tests (success, validation, errors)
3. test_config.py - Configuration validation
4. test_integration.py - Full request-to-response flow

Frontend tests (frontend/src/__tests__/):
1. ChatInterface.test.tsx - Component behavior
2. api.test.ts - API client with mocked responses
3. App.test.tsx - Full app integration

Use pytest for backend, vitest for frontend.
```

**✅ Test It - Run Full Test Suite:**

```bash
# Backend tests with coverage
source venv/bin/activate
pytest backend/tests/ -v --cov=backend --cov-report=term --cov-report=html

# Frontend tests with coverage
cd frontend
npm test -- --coverage
```

**Check coverage reports:**
```bash
# Backend: open htmlcov/index.html
# Frontend: open coverage/index.html
```

**🎯 What This Improves:**
- ✨ **Before**: Hope code works, find bugs in production
- ✨ **With Tests**: Confidence that code works correctly
- ✨ **Benefit**: Catch regressions, safe refactoring
- ✨ **Coverage Goal**: 80%+ means most code is tested

---

### Step 11.2: Create Unified Start Script

**Ask Claude Code:**
```
Create start.sh script that:
1. Checks if venv exists, creates if missing
2. Activates virtual environment
3. Installs/updates dependencies (pip install -r requirements.txt)
4. Starts backend in background (port 8000)
5. Checks if frontend dependencies are installed
6. Starts frontend (port 5173)
7. Waits for both servers to be ready
8. Opens browser to http://localhost:5173
9. Shows colored status messages
10. Make it executable (chmod +x)
```

**✅ Test It:**
```bash
./start.sh
```

**Watch:** Entire project starts with one command!

**🎯 What This Improves:**
- ✨ **Before**: Multiple terminal windows, 5+ commands
- ✨ **With start.sh**: One command starts everything
- ✨ **Time Saved**: 3-5 minutes → 10 seconds
- ✨ **Team Benefit**: Easy onboarding for new developers

---

## 🏆 Lab 12: Deployment & Documentation

### Step 12.1: Add Deployment Config

**Ask Claude Code:**
```
Create Docker configuration for production:
1. backend/Dockerfile - Multi-stage build, optimized for FastAPI
2. frontend/Dockerfile - Build Vite for production, serve with nginx
3. docker-compose.yml - Run both services with networking
4. Add health checks and proper environment variables
5. Add .dockerignore files
```

**✅ Test It:**
```bash
docker-compose up --build
```

**Visit:** http://localhost:5173

**🎯 What This Improves:**
- ✨ **Benefit**: Production-ready deployment
- ✨ **Benefit**: Consistent environment (dev/prod parity)

---

### Step 12.2: Complete Documentation

**Ask Claude Code:**
```
Create comprehensive README.md with:
1. Project overview with demo GIF/screenshot
2. Features list with checkboxes
3. Architecture diagram (ASCII art)
4. Prerequisites and setup instructions
5. How to run (development and production)
6. API documentation (endpoints, request/response)
7. Testing instructions
8. Troubleshooting section
9. Contributing guidelines
10. License (MIT)
```

**✅ Test It:**
```
Ask a teammate or friend to set up the project using only your README
```

**🎯 What This Improves:**
- ✨ **Benefit**: Anyone can understand and run your project
- ✨ **Use Case**: Open source, team onboarding, portfolio

---

### Step 12.3: Create Demo Presentation

**Ask Claude Code:**
```
Write a 5-minute demo script for presenting this project:
1. Problem statement (why this matters)
2. Solution overview (what you built)
3. Live demo flow (step-by-step walkthrough)
4. Technical highlights (Claude Code features used)
5. Architecture overview
6. Future enhancements
7. Lessons learned

Format as speaker notes with timing.
```

---

## 🎯 Extension Challenges

Ready to level up? Try these advanced challenges:

### Challenge 1: Multi-Agent System
**Goal:** Multiple specialized agents working together.
```
Create:
- Research agent (searches web, summarizes)
- Coding agent (writes code)
- Review agent (reviews code quality)
- Router agent (delegates to appropriate agent)
Test: "Research REST API best practices and implement them in our API"
```

### Challenge 2: Persistent Conversation Memory
**Goal:** Agent remembers conversations across sessions.
```
Implement:
- SQLite database for conversation history
- Conversation summarization (for context window)
- User profile learning
- /history command to view past conversations
Test: Chat today, restart tomorrow, agent remembers!
```

### Challenge 3: Voice Interface
**Goal:** Talk to your agent.
```
Add:
- Speech-to-text input (Web Speech API)
- Text-to-speech output (browser synthesis)
- Voice activity detection
- Audio waveform visualization
Test: Have a voice conversation with your agent!
```

### Challenge 4: Plugin System for Tools
**Goal:** Users can enable/disable agent tools dynamically.
```
Create:
- Tool marketplace UI
- Enable/disable toggles for each tool
- Tool usage statistics
- Custom tool creator
Test: User enables "weather" tool, agent can now check weather!
```

### Challenge 5: Analytics Dashboard
**Goal:** Insights into agent usage.
```
Build:
- Usage stats (messages per day, popular tools)
- Response time graphs
- Error rate tracking
- User satisfaction ratings
- Export to CSV
Test: View analytics showing agent performance over time
```

---

## 📚 Complete Feature Summary

After this workshop, you've mastered:

### ✅ Claude Code Core Features
- Multi-step task automation
- File operations (read, write, edit, grep, glob)
- Git integration
- Terminal command execution

### ✅ CLAUDE.md Configuration
- **What**: Project-specific instructions
- **Tested**: Claude remembers project setup automatically
- **Impact**: No more repeating context every session

### ✅ settings.json Hooks
- **What**: Automated workflows at tool use points
- **Tested**: Pre-commit tests, file protection, session context
- **Impact**: Quality gates, security, automation

### ✅ Plugins
- **What**: Extend Claude Code capabilities
- **Tested**: TypeScript LSP (type checking), Pyright LSP, GitHub
- **Impact**: Catch bugs early, seamless GitHub integration

### ✅ Custom Commands
- **What**: Reusable prompt templates
- **Tested**: /component (generate React components), /test-all
- **Impact**: 10 minutes → 30 seconds per task

### ✅ Custom Skills
- **What**: Multi-step automated workflows
- **Tested**: /start-dev (start both servers), /check-health
- **Impact**: Complex workflows in one command

### ✅ Custom Agents
- **What**: Specialized Claude instances
- **Tested**: code-reviewer, frontend-improver, test-engineer
- **Impact**: Expert-level reviews, faster development

### ✅ Agent Memory
- **What**: Agents learn project preferences
- **Tested**: code-reviewer remembers standards
- **Impact**: Consistent behavior, agents get smarter

### ✅ MCP (Model Context Protocol)
- **What**: Connect to external tools
- **Tested**: Chrome DevTools (screenshots, console), Draw.io (diagrams)
- **Impact**: Visual testing, automated documentation

### ✅ Memory System
- **What**: Persistent preferences across sessions
- **Tested**: Ports, commit format, learning style
- **Impact**: No repetition, consistent workflow

### 📊 Impact Metrics

| Feature | Time Saved | Quality Impact |
|---------|-----------|----------------|
| LSP Plugins | Hours of debugging → Instant detection | ⬆️ Fewer type errors |
| Pre-commit Hooks | 0 → 100% test coverage enforcement | ⬆️ No broken commits |
| /component Command | 10 min → 30 sec per component | ⬆️ Consistent code style |
| /start-dev Skill | 3 min → 10 sec startup | ⬆️ Smooth workflow |
| Code Review Agent | No review → Expert review in 2 min | ⬆️ Catch bugs early |
| Visual Inspector + MCP | 20 min manual testing → 2 min automated | ⬆️ Better UX |
| Memory System | 5 min context every session → 0 | ⬆️ Less repetition |

**Total Time Saved Per Day:** 1-2 hours
**Code Quality Improvement:** 50-80% fewer bugs reach production

---

## 🆘 Troubleshooting

[Previous troubleshooting section remains the same...]

---

## 🚀 Quick Reference Card

[Previous reference card remains the same...]

---

**🎉 Congratulations on completing the LabCamp workshop!**

You now have hands-on experience with:
- ✅ Building full-stack AI agents with Strands SDK
- ✅ Using **ALL** Claude Code features (tested each one!)
- ✅ Professional development workflows
- ✅ Test-driven development with automated quality gates
- ✅ Custom tooling (commands, skills, agents, hooks)
- ✅ Visual testing and browser automation (MCP)
- ✅ Persistent memory and context management

**What makes this workshop special:**
- 🎯 **"Add → Test → See Benefit"** approach for every feature
- ⏱️ **Time savings measured** - you experienced the speed boost
- 🐛 **Bug prevention tested** - you saw hooks block bad code
- 🤖 **Agent expertise witnessed** - expert reviews in minutes

**Next steps:**
- 🚀 Build your own AI agent project
- 🛠️ Create custom commands/skills for your workflow
- 📢 Share your learnings with the community
- 📖 Explore advanced Claude Code documentation

Keep experimenting, keep building, and most importantly - **have fun coding with Claude!** 🚀
