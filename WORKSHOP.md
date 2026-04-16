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
- **Draw.io**: Architecture diagram generation
- **Custom MCPs**: Build your own integrations

### 🧠 Memory (Lab 11)
- **Persistent Context**: Claude remembers preferences across sessions
- **Project Memory**: Store project-specific knowledge
- **Memory Management**: View and update stored information

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

You should see the Claude Code version number!

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

**Why do this first?** You need an existing folder with git initialized so Claude Code can work with it.

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

**Why?** Python dependencies will be isolated to this project.

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

**Why?** Claude Code needs AWS Bedrock access to use Claude AI models.

**📋 Setup Complete - Verify Your Environment:**

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

**Note:** If VS Code prompts "Do you trust the authors of the files in this folder?" - click "Yes, I trust the authors"

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

### Step 1.2: Share Strands Agents Documentation

**Give Claude the official Strands SDK documentation link:**

```
I want to build this project using Strands Agents SDK for the backend agent functionality.
Here's the official documentation: https://strandsagents.com/docs/user-guide/quickstart/python/

Please reference this documentation when building the agent service.
```

**Why?** This ensures Claude uses the correct Strands SDK patterns and APIs.

### Step 1.3: Connect GitHub CLI (gh) for Automated Git Operations

**Ask Claude Code to help you set up GitHub CLI:**

```
How do I connect GitHub CLI so you can automatically commit and push changes for me?
```

**Claude will help you:**
1. Install `gh` if not present (via homebrew/apt/etc)
2. Provide the authentication command: `gh auth login`

**Follow the prompts:**
```bash
# Run this in the terminal
gh auth login

# Select:
# - GitHub.com
# - HTTPS
# - Yes (authenticate Git)
# - Login with a web browser

# You'll get a code & url
# opne url in browser - enter the code
# Authorize GitHub CLI
# back in terminal press enter
```

**✅ Test It:**
```bash
gh auth status
# Should show: "Logged in to github.com"
```

**Why?** This allows Claude Code to automatically push commits to GitHub for you.

### Step 1.4: Reopen Claude Code with GitHub Access

**Important:** Close and reopen Claude Code so it can use the GitHub credentials:

```bash
# Exit Claude Code (Ctrl+C or type /exit)

# Reopen it
claudecode
```

Now Claude Code has GitHub CLI access in the same terminal session!

### Step 1.5: Give Claude Your GitHub Repository URL

**Tell Claude about your repository and workflow preferences:**

```
Remember this for future sessions:
- My GitHub repository is: https://github.com/yourusername/my-ai-assistant.git
- After every feature or fix, please commit with a descriptive message and push to GitHub
- Use conventional commit format: feat:, fix:, chore:, docs:, test:
- Always run tests before committing
```

**Claude will remember** these preferences!

### Step 1.6: Initialize CLAUDE.md for Project Memory

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
"What ports should this project use?"
```

**Claude should reference CLAUDE.md** and know the project setup!

---

## 🎨 Lab 2: Share UI Design Ideas with Image Pasting

### Step 2.1: Paste Your Design Inspiration

**Welcome!** Now that Claude Code is set up, let's start with something visual and fun - designing your chat interface!

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
Can you help me build a frontend that looks like this?
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
2. Suggest a tech stack to achieve the look
3. Generate React components matching the design
4. Recommend CSS/Tailwind classes for styling

**🎯 What This Improves:**
- ✨ **Before**: Try to describe design in words ("make it purple-ish with round bubbles...")
- ✨ **With Image**: Show exactly what you want - Claude sees it visually
- ✨ **Benefit**: Start with clear design goals, save hours of design iteration
- ✨ **Time Saved**: Skip the guesswork - Claude understands your vision immediately

**Example interaction:**
```
You: [Paste image of LeadBot chat interface]
"I love this chat design with the purple theme and bubble-style messages. 
Can you help me create something similar?"

Claude: "I can see this is a modern chat interface with:
- Purple-themed header with bot avatar and 'Online' status
- Clean message bubbles with rounded corners
- Interactive button options for user responses
- Smooth animations and good spacing

I'll help you build this! Let's start by setting up the project..."
```

**💡 Pro Tip:** You can paste multiple design references to show different aspects:
- One image for overall layout
- Another for specific components (buttons, inputs)
- A third showing color palette or animations

**No design image?** No problem! You can skip this step and Claude will help you create a clean, modern design from scratch. But if you have visual inspiration, sharing it upfront helps Claude align the entire build to your vision!

---

## 🏗️ Lab 3: Let Claude Code Build Your Project

### Step 3.1: Ask Claude to Create Project Structure

**Now that setup is complete, let Claude Code do the heavy lifting!**

**Ask Claude Code:**
```
Create the following project structure:
- backend/ folder for Python FastAPI API
- frontend/ folder for React + TypeScript app
- .gitignore file (include: venv/, node_modules/, .env, __pycache/, .DS_Store)
- Update README.md with project overview and tech stack
```

**✅ Test It:**
```bash
ls -la
cat README.md
```

**🎯 What This Improves:**
- ✨ **Before Claude Code**: Manually create each directory and file
- ✨ **With Claude Code**: Entire project structure in one command
- ✨ **Time Saved**: 5-10 minutes → 30 seconds

**Claude Code Feature Learned:** Multi-step project scaffolding

### Step 3.2: Set Up Backend with Strands SDK

**Ask Claude Code:**
```
Set up a Python FastAPI backend in the backend/ directory:
1. Create requirements.txt with: fastapi, uvicorn, strands-agents, pydantic-settings
2. Create backend/main.py with a basic FastAPI app
3. Add a /health endpoint that returns {"status": "healthy"}
Note: We already have a venv created in Lab 0
```

**✅ Test It Yourself:**
```bash
source venv/bin/activate
pip install -r requirements.txt
python -m uvicorn backend.main:app --reload --port 8000
```

Visit http://localhost:8000/health - you should see the health status!

**🎯 What This Improves:**
- ✨ **Before**: Write boilerplate code manually
- ✨ **With Claude**: Full backend setup in one prompt
- ✨ **Time Saved**: 20-30 minutes → 2 minutes

**Claude Code Feature Learned:** Multi-step task execution

---

## 🧪 Lab 2: Testing & CLAUDE.md Configuration

### Step 2.1: Add Your First Test

**Ask Claude Code:**
```
Create a backend/tests/ directory and add test_main.py with a test for the health endpoint using pytest
```

**✅ Test It:**
```bash
pip install pytest httpx
pytest backend/tests/ -v
```

**Checkpoint:** Test should pass ✅

**🎯 What This Improves:**
- ✨ **With Tests**: Confidence your code works
- ✨ **Without Tests**: Manual testing every time
- ✨ **Benefit**: Catch bugs before deployment

### Step 2.2: Create CLAUDE.md (Project Documentation)

**CLAUDE.md tells Claude Code about your project's rules and architecture.**

**Ask Claude Code:**
```
Create a CLAUDE.md file documenting:
- How to run the backend
- How to run tests
- Project architecture overview
- Tech stack (FastAPI, Strands SDK, React, Vite)
- Important rules (e.g., "Always run tests before committing")
Use the /init skill if available
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

### Step 2.3: Set Up Automated Testing Hook

**Ask Claude Code:**
```
Create a PreToolUse hook in .claude/settings.json that runs tests before every commit
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

**Claude Code Feature Learned:** Hooks for workflow automation (we'll explore more in Lab 8)

---

## 🤖 Lab 3: Build Your AI Agent

### Step 3.1: Configure Environment (.env file)

**Ask Claude Code:**
```
Create .env.example and .env files with:
- CLAUDE_MODEL_ID (use eu.anthropic.claude-sonnet-4-5-20250929-v1:0)
- APP_NAME=MyAIAssistant
- API_PORT=8000
Add .env to .gitignore
```

**✅ Test It:**
```bash
cat .env
cat .env.example
git status  # .env should not appear (ignored)
```

**🎯 What This Improves:**
- ✨ **Benefit**: Secrets stay out of git
- ✨ **Benefit**: Easy configuration management

### Step 3.2: Create Agent Service

**Ask Claude Code:**
```
Create backend/services/agent_service.py with:
1. Import Strands SDK (Agent, tool)
2. Create an AgentService class
3. Add a simple tool called get_joke() that returns a random joke
4. Initialize the Agent with Claude model from .env
5. Add a chat() method that takes a message and returns agent response
```

**Hint:** Look at the reference project's `agent_service.py` for inspiration!

### Step 3.3: Create Chat Endpoint

**Ask Claude Code:**
```
Create backend/api/endpoints/chat.py with:
1. POST /chat endpoint that accepts {"message": "string"}
2. Uses AgentService to process the message
3. Returns {"response": "string"}
Add it to main.py with /api/v1 prefix
```

**✅ Test It:**
```bash
# In one terminal
python -m uvicorn backend.main:app --reload --port 8000

# In another terminal
curl -X POST http://localhost:8000/api/v1/chat \
  -H "Content-Type: application/json" \
  -d '{"message": "Tell me a joke"}'
```

**Checkpoint:** You should get a joke back from Claude! 🎉

**🎯 What This Improves:**
- ✨ **Achievement**: You just built an AI agent with tool calling!
- ✨ **Benefit**: Backend can now use Claude's intelligence

### Step 3.4: Add a Calculator Tool

**Ask Claude Code:**
```
Add a new tool to agent_service.py called calculate() that:
- Takes a math expression as string
- Uses ast.literal_eval() for safe evaluation (no eval!)
- Returns the result
Test it by asking the agent to calculate 42 * 37
```

**✅ Test It:**
```bash
curl -X POST http://localhost:8000/api/v1/chat \
  -H "Content-Type: application/json" \
  -d '{"message": "Calculate 42 times 37"}'
```

**🎯 What This Improves:**
- ✨ **Before**: Agent can only chat
- ✨ **With Tools**: Agent can perform calculations
- ✨ **Benefit**: Agent becomes more capable

**Claude Code Feature Learned:** Iterative development, code modification

---

## 🎨 Lab 4: Build the Frontend

### Step 4.1: Initialize React App

**Ask Claude Code:**
```
Set up a React + TypeScript + Vite app in frontend/:
1. Use npm create vite@latest
2. Install dependencies: axios, @tanstack/react-query
3. Configure Vite to proxy /api to http://localhost:8000
4. Create a basic App.tsx with "AI Assistant" title
```

**✅ Test It:**
```bash
cd frontend
npm install
npm run dev
```

Visit http://localhost:5173 - you should see your app!

### Step 4.2: Create Chat Interface

**Ask Claude Code:**
```
Create a ChatInterface component with:
1. Message list showing conversation history
2. Input field for user messages
3. Send button
4. Use TanStack Query to call the backend /chat endpoint
Style it with Tailwind CSS
```

**Claude Code Feature Learned:** Frontend component generation, API integration

### Step 4.3: Add Message History

**Ask Claude Code:**
```
Add state management to store messages:
1. Each message has: id, role (user/assistant), content, timestamp
2. Display messages in chronological order
3. Auto-scroll to newest message
4. Show loading state while waiting for response
```

**✅ Test It - Full System:**
```
1. Start backend: python -m uvicorn backend.main:app --reload --port 8000
2. Start frontend: cd frontend && npm run dev
3. Open browser: http://localhost:5173
4. Send message: "Tell me a joke"
5. Send message: "Calculate 15 + 27"
```

**Checkpoint:** You should be able to chat with your AI assistant! 🤖

**🎯 What This Improves:**
- ✨ **Achievement**: Full-stack AI chat application working!
- ✨ **Benefit**: Users can interact with your AI agent

---

## 🔧 Lab 5: Advanced Features

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

### Step 5.2: Add Tool for Your Interest

**Challenge:** Add a custom tool based on your interests:
- Movie buff? Add `search_movies()` tool
- Sports fan? Add `get_team_stats()` tool
- Weather enthusiast? Add `get_forecast()` tool

**Ask Claude Code:**
```
Add a new tool called [your_tool_name] to the agent that [describe functionality]
```

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

**LSPs provide real-time type checking and code intelligence:**

```
/plugin install typescript-lsp@claude-plugins-official
/plugin install pyright-lsp@claude-plugins-official
/reload-plugins
```

**✅ Test It - Introduce a Type Error:**

1. **Add a type error to frontend:**
```typescript
// In ChatInterface.tsx, change:
const [message, setMessage] = useState<string>('')
// To:
const [message, setMessage] = useState<number>('')  // Wrong! Should be string
```

2. **Ask Claude Code:**
```
Run type checking on my TypeScript files. Find and fix any type errors.
```

**Watch:** Claude will use LSP to detect the type mismatch and fix it!

3. **Now test Python:**
```python
# In agent_service.py, add:
def test_function(x: int) -> str:
    return x  # Wrong! Should return string, not int
```

4. **Ask Claude Code:**
```
Run type checking on my Python backend code.
```

**Watch:** Pyright LSP catches the return type mismatch!

**🎯 What This Improves:**
- ✨ **Before LSP**: Type errors only found at runtime or build time
- ✨ **With LSP**: Type errors caught instantly while coding
- ✨ **Benefit**: Fewer bugs, better code quality, faster development
- ✨ **Time Saved**: Hours of debugging → Instant detection

**Claude Code Feature Learned:** LSP plugins for code quality

### Step 6.3: Install GitHub Plugin

**Connect Claude Code to GitHub for PR reviews and issue management:**

```
/plugin install github@claude-plugins-official
/reload-plugins
```

**✅ Test It - GitHub Integration:**

1. **First, push your project to GitHub:**
```bash
git remote add origin https://github.com/yourusername/my-ai-assistant.git
git push -u origin main
```

2. **Ask Claude Code:**
```
Show me all open pull requests in this repository
```

3. **Ask Claude Code:**
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

### Step 7.1: Use the Component Command

**This project includes a custom `/component` command for rapid React development.**

**✅ Test It - Generate Components:**

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

**Claude Code Feature Learned:** Custom commands for code generation

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

### Step 7.3: Use the Start-Dev Skill

**Skills are multi-step automated workflows.**

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

### Step 7.5: Create Your Own Custom Skill

**Skills live in `.claude/skills/` and can have complex logic.**

**Ask Claude Code:**
```
Create a custom skill called /check-health in .claude/skills/check-health/ that:
1. Checks if backend server is running (curl localhost:8000/health)
2. Checks if frontend server is running (curl localhost:5173)
3. If backend is down, shows how to start it
4. If frontend is down, shows how to start it
5. Reports overall system status with colored output (✅ or ❌)
Create SKILL.md file with the full logic
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

**🎯 What This Improves:**
- ✨ **Benefit**: Quick system health checks
- ✨ **Benefit**: Helpful debugging when services are down

**Claude Code Feature Learned:** Custom skill development

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

### Step 8.2: Create a Pre-Commit Test Hook

**Ask Claude Code:**
```
Create a PreToolUse hook in .claude/settings.json that:
1. Matches any git commit operations (matcher: "Bash" with command containing "git commit")
2. Runs: ./run-tests.sh script
3. Shows status message: "Running tests before commit..."
4. Blocks commit if tests fail

Also create the run-tests.sh script that:
- Activates venv
- Runs pytest backend/tests/
- Runs npm test in frontend/
- Exits with error code if any test fails
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

### Step 8.3: Create a File Protection Hook

**Ask Claude Code:**
```
Create a PreToolUse hook in .claude/settings.json that:
1. Matches Edit and Write operations
2. Blocks editing these files:
   - .env (contains secrets)
   - package-lock.json (managed by npm)
   - poetry.lock (managed by poetry)  
   - venv/** (virtual environment)
3. Shows error message explaining why file is protected
Create a shell script .claude/hooks/protect-files.sh for this
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

### Step 8.4: Create a SessionStart Context Hook

**Ask Claude Code:**
```
Create a SessionStart hook in .claude/settings.json that:
1. Runs when Claude Code starts
2. Displays:
   - Current git branch
   - Number of uncommitted changes (git status --short | wc -l)
   - Last commit message (git log -1 --oneline)
   - Server ports (Backend: 8000, Frontend: 5173)
   - Quick commands (/start-dev, /test-all, /component)
Create a script .claude/hooks/project-context.sh for this
```

**✅ Test It:**
```
Restart your Claude Code session
```

**Watch:** You'll see a welcome message with project context:
```
📋 Project Context:
├─ Branch: feature/add-auth
├─ Uncommitted changes: 3 files
├─ Last commit: feat: add user authentication endpoint
├─ Backend: http://localhost:8000
├─ Frontend: http://localhost:5173
└─ Quick commands: /start-dev /test-all /component
```

**🎯 What This Improves:**
- ✨ **Before**: Manually check git status, remember ports, recall commands
- ✨ **With Hook**: All context loaded automatically at session start
- ✨ **Benefit**: Get oriented immediately, no context switching
- ✨ **Time Saved**: 1-2 minutes every session

**Claude Code Feature Learned:** Session initialization hooks

### Step 8.5: Create a PostToolUse Formatting Hook

**Ask Claude Code:**
```
Create a PostToolUse hook that:
1. Runs after Edit or Write operations on .ts, .tsx, .py files
2. Formats the file with appropriate tool (prettier for TS, black for Python)
3. Shows message: "Auto-formatted <filename>"
```

**✅ Test It:**
```
Ask Claude: "Add a new function to agent_service.py with messy formatting"
```

**Watch:** Claude writes the code, then the hook auto-formats it!

**🎯 What This Improves:**
- ✨ **Before**: Manually run prettier/black after every change
- ✨ **With Hook**: Code formatted automatically
- ✨ **Benefit**: Consistent style, no formatting debates

**Claude Code Feature Learned:** PostToolUse hooks for automation

---

## 🤖 Lab 9: Specialized Agents for Expert Help

### Step 9.1: Understanding Agents

**Agents are specialized Claude instances with specific roles, expertise, and tools.**

**This reference project includes 4 pre-built agents:**
- `code-reviewer` - Comprehensive code quality analysis
- `frontend-improver` - React/UI/UX specialist
- `frontend-visual-inspector` - Browser testing & screenshots (uses Chrome MCP)
- `backend-maintainer` - FastAPI/Python backend expert

**✅ Test It - Explore Agents:**
```
Ask Claude: "What custom agents are available in .claude/agents/?"
```

### Step 9.2: Use the Code Review Agent

**The code-reviewer agent specializes in finding bugs and improving code quality.**

**✅ Test It - Get a Code Review:**

**Ask Claude Code:**
```
Use the code-reviewer agent to review my agent_service.py file. Focus on security, error handling, and best practices.
```

**Watch the agent analyze:**
1. Security vulnerabilities (SQL injection, eval usage, etc.)
2. Error handling (try/catch, validation)
3. Type safety (missing type hints)
4. Performance concerns (N+1 queries, memory leaks)
5. Best practice violations

**Example findings:**
```
🔍 Security Issues:
❌ Line 45: Using ast.literal_eval - consider safer alternatives
✅ Recommendation: Add input validation before evaluation

🔍 Type Safety:
❌ Line 23: Missing return type hint
✅ Fix: def chat(message: str) -> dict[str, Any]:

🔍 Error Handling:
❌ Line 67: No try/catch around API call
✅ Add: Wrap agent.invoke_async() in try/except
```

**🎯 What This Improves:**
- ✨ **Before**: Hope your code is good or wait for code review
- ✨ **With Agent**: Instant expert review with actionable feedback
- ✨ **Benefit**: Catch bugs before they reach production
- ✨ **Learning**: Understand best practices from feedback

**Claude Code Feature Learned:** Using specialized agents

### Step 9.3: Use the Frontend Improver Agent

**The frontend-improver agent specializes in React and UI/UX.**

**✅ Test It - Improve Your UI:**

**Ask Claude Code:**
```
Use the frontend-improver agent to enhance the ChatInterface component with:
1. Better loading states (skeleton screens)
2. Smooth message animations
3. Better error UI
4. Accessibility improvements
```

**Watch the agent:**
1. Read your existing component
2. Analyze UI/UX patterns
3. Suggest improvements with reasoning
4. Implement changes following React best practices

**🎯 What This Improves:**
- ✨ **Before**: Research UI patterns yourself
- ✨ **With Agent**: Get expert UI/UX improvements
- ✨ **Benefit**: Professional-looking interface, better UX

**Claude Code Feature Learned:** Frontend-focused agent delegation

### Step 9.4: Use the Visual Inspector Agent

**The frontend-visual-inspector works with Chrome DevTools MCP to test visually.**

**✅ Test It - Visual Testing:**

**Ask Claude Code:**
```
Use the frontend-visual-inspector agent to:
1. Take screenshots of the chat interface
2. Test at mobile (375px), tablet (768px), and desktop (1920px) sizes
3. Identify visual bugs or layout issues
4. Suggest specific improvements
```

**Watch the agent:**
1. Start frontend server if needed
2. Launch browser via Chrome DevTools MCP
3. Navigate to http://localhost:5173
4. Take screenshots at different sizes
5. Analyze visuals and provide feedback

**Example feedback:**
```
📸 Mobile (375px):
❌ Send button is cut off at bottom
❌ Messages overflow horizontally
✅ Fix: Add max-width: 100% and overflow-wrap: break-word

📸 Tablet (768px):
✅ Layout looks good!

📸 Desktop (1920px):
❌ Chat interface is too wide (stretches full screen)
✅ Fix: Add max-width: 800px and center with mx-auto
```

**🎯 What This Improves:**
- ✨ **Before**: Manually resize browser and check each size
- ✨ **With Agent**: Automated visual testing across devices
- ✨ **Benefit**: Catch UI bugs early, ensure responsiveness
- ✨ **Time Saved**: 15-20 minutes of manual testing → 2 minutes

**Claude Code Feature Learned:** Visual testing with agents + MCP

### Step 9.5: Use the Backend Maintainer Agent

**The backend-maintainer agent specializes in FastAPI and Python backend work.**

**✅ Test It - Optimize Backend:**

**Ask Claude Code:**
```
Use the backend-maintainer agent to:
1. Review agent_service.py for performance improvements
2. Add proper error handling to the chat endpoint
3. Implement request validation
4. Add logging for debugging
```

**🎯 What This Improves:**
- ✨ **Benefit**: Backend-specific expertise
- ✨ **Benefit**: Focus on API performance and reliability

**Claude Code Feature Learned:** Backend-focused agent delegation

### Step 9.6: Create Your Own Custom Agent

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

### Step 9.7: Agent Memory

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

## 🔌 Lab 10: MCP for Browser Testing & Diagrams

### Step 10.1: Understanding MCP

**MCP (Model Context Protocol) connects Claude Code to external tools.**

**This reference project has 2 MCP servers pre-configured:**
- `chrome-devtools` - Browser automation, screenshots, debugging
- `drawio` - Architecture diagram generation

**✅ Test It - Check MCP Configuration:**
```
Ask Claude: "Show me the MCP servers configured in .mcp.json"
```

**You should see:**
```json
{
  "mcpServers": {
    "drawio": {
      "command": "npx",
      "args": ["-y", "@drawio/mcp"]
    },
    "chrome-devtools": {
      "command": "npx",
      "args": ["-y", "chrome-devtools-mcp@latest"]
    }
  }
}
```

### Step 10.2: Use Chrome DevTools MCP

**Chrome DevTools MCP is already installed! Let's use it.**

**✅ Test It - Take Screenshots:**

**Ask Claude Code:**
```
Use Chrome DevTools MCP to:
1. Start the frontend if needed
2. Open http://localhost:5173 in a browser
3. Take a screenshot of the chat interface
4. Check browser console for any errors or warnings
```

**Watch Claude:**
1. Launch browser via MCP
2. Navigate to your app
3. Capture screenshot (you'll see it in the response!)
4. Read console logs
5. Report findings

**🎯 What This Improves:**
- ✨ **Before**: Manually open browser, take screenshots, check console
- ✨ **With MCP**: Automated browser testing and screenshots
- ✨ **Benefit**: Visual verification, catch console errors
- ✨ **Use Case**: Automated visual regression testing

**Claude Code Feature Learned:** Browser automation via MCP

### Step 10.3: Test Responsive Design with MCP

**✅ Test It - Multi-Device Testing:**

**Ask Claude Code:**
```
Use Chrome DevTools MCP to test the chat interface responsiveness:
1. Mobile (375px width) - iPhone SE size
2. Tablet (768px width) - iPad size
3. Desktop (1920px width) - Full HD
Take screenshots of each and identify any layout issues.
```

**Watch:** Claude captures 3 screenshots and analyzes them!

**Example analysis:**
```
📱 Mobile (375px):
✅ Messages stack vertically (good!)
❌ Input field is too wide, causes horizontal scroll
✅ Fix: Add max-width: 100% to input

📱 Tablet (768px):
✅ Layout looks great!

💻 Desktop (1920px):
❌ Chat interface stretches too wide
✅ Fix: Add max-width: 800px and mx-auto
```

**🎯 What This Improves:**
- ✨ **Before**: Manually resize browser, test each device
- ✨ **With MCP**: Automated responsive testing across sizes
- ✨ **Time Saved**: 20 minutes → 2 minutes
- ✨ **Benefit**: Ensure mobile users have great experience

**Claude Code Feature Learned:** Visual regression testing

### Step 10.4: Debug Network Issues with MCP

**✅ Test It - Monitor API Calls:**

**Ask Claude Code:**
```
Use Chrome DevTools MCP to:
1. Open the app and monitor network requests
2. Send a chat message "Tell me a joke"
3. Capture the API call to /api/v1/chat
4. Show request/response details
5. Measure response time
6. Identify any errors or slow requests
```

**Watch:** Claude monitors network and reports:
```
🌐 Network Analysis:
Request: POST http://localhost:8000/api/v1/chat
Status: 200 OK
Response Time: 1.2s
Request Body: {"message": "Tell me a joke"}
Response Body: {"response": "Why did the..."}

⚡ Performance:
- Response time is good (< 2s)
- No failed requests
- Consider adding request caching for common queries
```

**🎯 What This Improves:**
- ✨ **Before**: Open DevTools manually, check network tab
- ✨ **With MCP**: Automated network monitoring and analysis
- ✨ **Benefit**: Catch slow APIs, debug network issues
- ✨ **Use Case**: Performance testing and optimization

**Claude Code Feature Learned:** Network debugging via MCP

### Step 10.5: Generate Diagrams with Draw.io MCP

**Draw.io MCP is already installed for creating diagrams!**

**✅ Test It - Architecture Diagram:**

**Ask Claude Code:**
```
Use Draw.io MCP to create a system architecture diagram showing:
1. User (browser)
2. React Frontend (port 5173) - Vite dev server
3. FastAPI Backend (port 8000)
4. AgentService (using Strands SDK)
5. Claude AI (via Amazon Bedrock)
6. Show data flow: User → Frontend → Backend → Agent → Claude → Back
Use boxes for components and arrows for data flow.
```

**Watch:** Claude generates a professional diagram!

**The diagram will show:**
```
[User Browser]
      ↓
[React Frontend :5173]
      ↓ HTTP POST /api/v1/chat
[FastAPI Backend :8000]
      ↓
[AgentService (Strands SDK)]
      ↓ Bedrock API
[Claude AI Model]
      ↓ Response
[Back through stack]
```

**🎯 What This Improves:**
- ✨ **Before**: Manually create diagrams in Draw.io or Lucidchart
- ✨ **With MCP**: Generate diagrams from text description
- ✨ **Time Saved**: 30-60 minutes → 2 minutes
- ✨ **Benefit**: Keep architecture docs up to date

**Create more diagrams:**
```
Use Draw.io MCP to create a sequence diagram showing the chat message flow with timing
```

**Claude Code Feature Learned:** Architecture diagram generation

### Step 10.6: Advanced - Agent + MCP Integration

**Combine agents with MCP for powerful workflows.**

**✅ Test It - Automated Visual Testing:**

**Ask Claude Code:**
```
Use the frontend-visual-inspector agent to:
1. Test the entire user journey (load page, send message, receive response)
2. Take screenshots at each step
3. Check for UI bugs or inconsistencies
4. Test accessibility (check for proper ARIA labels)
5. Provide a comprehensive visual test report
```

**Watch:** The agent uses Chrome DevTools MCP internally!

**Example report:**
```
📋 Visual Test Report

✅ Step 1: Page Load
- Screenshot captured
- No console errors
- Page loads in 0.8s

✅ Step 2: User Types Message
- Input field is accessible (has aria-label)
- Character count shows correctly

❌ Step 3: Message Sent
- Loading spinner not visible (should show while waiting)
- Fix: Add LoadingSpinner component

✅ Step 4: Response Received
- Message appears correctly
- Timestamp is formatted properly

🎯 Accessibility Issues:
❌ Send button missing aria-label
✅ Fix: Add aria-label="Send message"
```

**🎯 What This Improves:**
- ✨ **Benefit**: Combines agent intelligence + MCP tools
- ✨ **Benefit**: Comprehensive automated testing
- ✨ **Use Case**: Pre-deployment visual QA

**Claude Code Feature Learned:** Agent + MCP integration

### Step 10.7: Create a Custom MCP Server (Advanced Challenge)

**Build your own MCP server for project-specific needs.**

**Ask Claude Code:**
```
Create a custom MCP server called "project-tools" that provides:
1. Database query interface (for SQLite)
2. Log file analyzer (parse backend logs for errors)
3. Performance metrics (calculate avg response time from logs)
4. Test coverage checker (parse pytest coverage reports)

Create:
- .mcp.json entry for "project-tools"
- Node.js MCP server at mcp-servers/project-tools.js
- Tools for each functionality above
```

**MCP server structure:**
```json
{
  "mcpServers": {
    "project-tools": {
      "command": "node",
      "args": ["./mcp-servers/project-tools.js"]
    }
  }
}
```

**✅ Test It:**
```
Ask Claude: "Use project-tools MCP to analyze backend logs and show error rate"
```

**🎯 What This Improves:**
- ✨ **Benefit**: Extend Claude Code with project-specific tools
- ✨ **Use Case**: Custom debugging, monitoring, analytics

**Claude Code Feature Learned:** Custom MCP server development

---

## 📝 Lab 11: Memory for Persistent Context

### Step 11.1: Use Claude Code Memory

**Claude Code can remember preferences across sessions.**

**✅ Test It - Save Preferences:**

**Tell Claude Code:**
```
Remember these project preferences:
- Backend port: 8000 (never change)
- Frontend port: 5173 (never change)
- We use conventional commits (feat:, fix:, chore:, docs:)
- Always run tests before committing
- Python virtual environment is "venv"
```

**Then in a NEW session (restart Claude Code), ask:**
```
What ports should I use for this project?
What commit format does this project use?
How do I activate the virtual environment?
```

**Watch:** Claude remembers all preferences!

**🎯 What This Improves:**
- ✨ **Before**: Explain project setup every session
- ✨ **With Memory**: Claude knows your preferences automatically
- ✨ **Benefit**: Consistent behavior, no repetition
- ✨ **Time Saved**: 5 minutes explanation every session

**Claude Code Feature Learned:** Persistent memory across sessions

### Step 11.2: Project-Specific Memory

**Tell Claude about your learning goals.**

**✅ Test It - Educational Context:**

**Tell Claude Code:**
```
Remember that this is an educational project for learning. Always:
- Explain concepts clearly with examples
- Prioritize readable code over clever optimizations
- Add helpful comments explaining "why", not just "what"
- Suggest gradual improvements rather than complex refactors
- Ask if I understand before moving to next step
```

**Then ask:**
```
Add caching to the agent service to improve performance
```

**Watch:** Claude's approach changes - more explanatory, step-by-step!

**Example response:**
```
I'll add caching to improve performance. Let me explain the approach:

1. **Why cache?** Agent responses for the same question don't change, so we can reuse them.

2. **Simple approach:** Use Python's @lru_cache decorator
   - Stores recent responses in memory
   - Automatically evicts old entries
   - No external dependencies needed

3. **Implementation:**
[Code with detailed comments explaining each line]

4. **Trade-offs to understand:**
   - Pro: Faster responses for repeated questions
   - Con: Uses memory (but limited by lru_cache size)
   - Con: Cached responses might become stale

Do you understand the caching strategy? Should I proceed?
```

**🎯 What This Improves:**
- ✨ **Benefit**: Claude adapts to your learning style
- ✨ **Benefit**: Better explanations, gradual learning
- ✨ **Use Case**: Teaching, onboarding, documentation

**Claude Code Feature Learned:** Project-specific memory

### Step 11.3: Check and Update Memory

**✅ Test It - Memory Inspection:**

**Check what Claude remembers:**
```
What do you remember about this project's preferences and standards?
```

**Update memory:**
```
Forget about the "gradual improvements" preference. Now prefer complete, production-ready implementations.
```

**Verify:**
```
What's your approach to adding new features now?
```

**🎯 What This Improves:**
- ✨ **Benefit**: Control Claude's behavior long-term
- ✨ **Benefit**: Update preferences as project evolves

**Claude Code Feature Learned:** Memory inspection and management

---

## 🧪 Lab 12: Comprehensive Testing & Quality Assurance

### Step 12.1: Add Full Test Suite

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

### Step 12.2: Create Unified Start Script

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

## 🏆 Lab 13: Deployment & Documentation

### Step 13.1: Add Deployment Config

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

### Step 13.2: Complete Documentation

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

### Step 13.3: Create Demo Presentation

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
