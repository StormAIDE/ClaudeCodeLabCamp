# ClaudeCode LabCamp Workshop Guide

**Welcome to the hands-on ClaudeCode workshop!** 

In this lab, you'll build your own AI-powered personal assistant from scratch, learning professional development workflows with Claude Code. By the end, you'll have a working full-stack application and understand how to use Claude Code plugins, hooks, and AI agent patterns.

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

---

## 📋 Prerequisites

Before starting, ensure you have:
- [ ] Claude Code installed (CLI, desktop, or web)
- [ ] Python 3.9+ installed
- [ ] Node.js 18+ and npm installed
- [ ] AWS credentials configured (for Bedrock access)
- [ ] Git installed
- [ ] A code editor (VS Code recommended)

**Check your setup:**
```bash
python --version    # Should be 3.9+
node --version      # Should be 18+
npm --version
aws configure list  # Should show configured credentials
```

---

## 🚀 Lab 1: Project Setup & Claude Code Basics

### Step 1.1: Create Your Project

**Ask Claude Code:**
```
Create a new directory called "my-ai-assistant" with the following structure:
- backend/ folder for Python API
- frontend/ folder for React app
- .gitignore file (Python, Node, and env files)
- README.md with a brief project description
```

**Verify:** You should see the directory structure created.

### Step 1.2: Initialize Git Repository

**Ask Claude Code:**
```
Initialize this as a git repository and create an initial commit
```

**Claude Code Feature Learned:** Basic file creation and git integration

### Step 1.3: Set Up Backend

**Ask Claude Code:**
```
Set up a Python FastAPI backend in the backend/ directory:
1. Create requirements.txt with: fastapi, uvicorn, strands-agents, pydantic-settings
2. Create backend/main.py with a basic FastAPI app
3. Add a /health endpoint that returns {"status": "healthy"}
4. Create a virtual environment called "venv"
```

**Try it yourself:**
```bash
source venv/bin/activate
pip install -r requirements.txt
python -m uvicorn backend.main:app --reload --port 8000
```

Visit http://localhost:8000/health - you should see the health status!

**Claude Code Feature Learned:** Multi-step task execution

---

## 🧪 Lab 2: Testing & Best Practices

### Step 2.1: Add Your First Test

**Ask Claude Code:**
```
Create a backend/tests/ directory and add test_main.py with a test for the health endpoint using pytest
```

**Try it yourself:**
```bash
pip install pytest httpx
pytest backend/tests/ -v
```

**Checkpoint:** Test should pass ✅

### Step 2.2: Set Up Automated Testing Hook

**Ask Claude Code:**
```
Configure a Claude Code hook that runs tests before every commit
```

**Claude Code Feature Learned:** Hooks for workflow automation

### Step 2.3: Create CLAUDE.md

**Ask Claude Code:**
```
Create a CLAUDE.md file documenting:
- How to run the backend
- How to run tests
- Project architecture
- Tech stack
Use the /init skill if available
```

**Claude Code Feature Learned:** Project documentation with `/init` skill

---

## 🤖 Lab 3: Build Your AI Agent

### Step 3.1: Configure Environment

**Ask Claude Code:**
```
Create .env.example and .env files with:
- CLAUDE_MODEL_ID (use eu.anthropic.claude-sonnet-4-5-20250929-v1:0)
- APP_NAME=MyAIAssistant
- API_PORT=8000
Add .env to .gitignore
```

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

**Try it yourself:**
```bash
# In one terminal
python -m uvicorn backend.main:app --reload --port 8000

# In another terminal
curl -X POST http://localhost:8000/api/v1/chat \
  -H "Content-Type: application/json" \
  -d '{"message": "Tell me a joke"}'
```

**Checkpoint:** You should get a joke back from Claude! 🎉

### Step 3.4: Add a Calculator Tool

**Ask Claude Code:**
```
Add a new tool to agent_service.py called calculate() that:
- Takes a math expression as string
- Uses ast.literal_eval() for safe evaluation (no eval!)
- Returns the result
Test it by asking the agent to calculate 42 * 37
```

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

**Try it yourself:**
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

**Checkpoint:** You should be able to chat with your AI assistant! 🤖

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

## 🎓 Lab 6: Professional Workflows with Plugins

### Step 6.1: Understanding Claude Code Plugins

**What are plugins?**
Plugins extend Claude Code with additional capabilities like language servers, external integrations, and specialized tools.

**Try these commands:**
```
/plugin list                  # See installed plugins
/plugin marketplace list      # Browse available plugins
```

### Step 6.2: Install Language Server Plugins (LSPs)

**LSPs provide real-time type checking and code intelligence:**

```
/plugin install typescript-lsp@claude-plugins-official
/plugin install pyright-lsp@claude-plugins-official
/reload-plugins
```

**Ask Claude Code:**
```
Run type checking on my TypeScript and Python code. Fix any type errors found.
```

**Watch:** Claude will use LSP to identify type errors before running your code!

**Claude Code Feature Learned:** LSP plugins for code quality

### Step 6.3: Install GitHub Plugin

**Connect Claude Code to GitHub for PR reviews and issue management:**

```
/plugin install github@claude-plugins-official
/reload-plugins
```

**Ask Claude Code:**
```
Show me all open pull requests in this repository
```

**Claude Code Feature Learned:** GitHub integration plugin

---

## 🛠️ Lab 7: Custom Commands & Skills

### Step 7.1: Use the Component Command

**This project includes a custom `/component` command for rapid React development.**

**Try it:**
```
/component ErrorBoundary A component that catches React errors
```

**Watch:** Claude generates a fully-typed React component with:
- TypeScript interface
- Tailwind CSS styling
- Proper project structure
- Best practices

**Create more components:**
```
/component LoadingSpinner Shows loading state
/component UserAvatar Displays user profile picture
```

**Claude Code Feature Learned:** Custom commands for code generation

### Step 7.2: Create Your Own Custom Command

**Commands are reusable prompt templates in `.claude/commands/`.**

**Ask Claude Code:**
```
Create a custom command called /test-all in .claude/commands/ that:
1. Runs backend tests with coverage
2. Runs frontend tests
3. Reports pass/fail status
4. Shows code coverage percentage
```

**Command structure:**
```markdown
---
name: test-all
description: Run all tests with coverage
usage: /test-all
---

# Test All

Run both backend and frontend test suites...
```

**Try it:**
```
/test-all
```

**Claude Code Feature Learned:** Custom command creation

### Step 7.2: Use the Start-Dev Skill

**This project includes a custom `/start-dev` skill to start both servers.**

**Try it:**
```
/start-dev
```

**Watch Claude:**
1. Activate Python virtual environment
2. Start FastAPI backend (port 8000)
3. Start Vite frontend (port 5173)
4. Report server status
5. Show URLs to visit

**Claude Code Feature Learned:** Custom skills for project workflows

### Step 7.3: Use Built-in Skills

**Skills are specialized multi-step workflows. Try the commit skill:**

```
/commit
```

**Watch Claude:**
1. Check git status
2. Review changes  
3. Generate a conventional commit message
4. Run pre-commit hooks (tests!)
5. Create the commit

**Try other built-in skills:**
```
/init          # Initialize CLAUDE.md documentation
/review        # Review a pull request
/simplify      # Refactor code for simplicity
```

**Claude Code Feature Learned:** Built-in skills for git workflows

### Step 7.4: Create Your Own Custom Skill

**Skills live in `.claude/skills/` and can have complex logic.**

**Ask Claude Code:**
```
Create a custom skill called /check-health that:
1. Checks if backend server is running (port 8000)
2. Checks if frontend server is running (port 5173)  
3. Tests /health endpoint
4. Reports status with colored output
Create it in .claude/skills/check-health/
```

**Skill structure:**
```
.claude/skills/check-health/
├── SKILL.md          # Skill prompt and logic
└── skill.json        # Metadata (optional)
```

**Try it:**
```
/check-health
```

**Claude Code Feature Learned:** Custom skill development

---

## 🪝 Lab 8: Hooks for Workflow Automation

### Step 8.1: Understanding Hooks

**Hooks automatically run actions at specific points in Claude Code's workflow:**
- `PreToolUse` - Before Claude uses a tool
- `PostToolUse` - After Claude uses a tool  
- `SessionStart` - When starting a new session

### Step 8.2: Create a Pre-Commit Hook

**Ask Claude Code:**
```
Create a PreToolUse hook in .claude/settings.json that:
1. Runs on any git commit operations
2. Checks that all tests pass
3. Blocks the commit if tests fail
4. Shows test output
```

**Try it:**
```
Make a small change and try to commit it with failing tests
```

**Claude Code Feature Learned:** Pre-commit hooks for quality gates

### Step 8.3: Create a File Protection Hook

**Ask Claude Code:**
```
Create a PreToolUse hook that prevents editing:
- .env files (secrets)
- package-lock.json (managed by npm)
- poetry.lock (managed by poetry)
- Files in claudecodeenv/ (virtual environment)
```

**Test it:**
```
Ask Claude to modify your .env file - it should be blocked!
```

**Claude Code Feature Learned:** File protection hooks

### Step 8.4: Create a SessionStart Hook

**Ask Claude Code:**
```
Create a SessionStart hook that displays:
- Current git branch
- Number of uncommitted changes
- Last commit message
- Project tech stack reminder
```

**Test it:**
```
Restart your Claude Code session to see the welcome message
```

**Claude Code Feature Learned:** Session initialization hooks

---

## 🤖 Lab 9: Custom Agents

### Step 9.1: Understanding Agents

**Agents are specialized Claude instances with specific roles, expertise, and tools.**

**This project includes 4 pre-built agents:**
- `code-reviewer` - Comprehensive code quality analysis
- `frontend-improver` - React/UI/UX specialist
- `frontend-visual-inspector` - Browser testing & screenshots
- `backend-maintainer` - FastAPI/Python backend expert

### Step 9.2: Use the Code Review Agent

**The code-reviewer agent specializes in quality analysis.**

**Ask Claude Code:**
```
Use the code-reviewer agent to review my agent_service.py file
```

**Watch the agent:**
1. Analyze code structure and patterns
2. Check for security vulnerabilities
3. Validate type safety
4. Review error handling
5. Suggest improvements with examples

**Review results will include:**
- Security issues
- Type safety problems
- Performance concerns
- Best practice violations
- Actionable fixes

**Claude Code Feature Learned:** Using specialized agents

### Step 9.3: Use the Frontend Improver Agent

**The frontend-improver agent specializes in React and UI/UX.**

**Ask Claude Code:**
```
Use the frontend-improver agent to enhance the ChatInterface component with better loading states
```

**The agent will:**
1. Read existing component code
2. Analyze UI/UX patterns
3. Suggest improvements
4. Implement changes with React best practices

**Claude Code Feature Learned:** Frontend-focused agent delegation

### Step 9.4: Use the Visual Inspector Agent

**The frontend-visual-inspector works with Chrome DevTools MCP.**

**Ask Claude Code:**
```
Use the frontend-visual-inspector agent to take screenshots of the chat interface and suggest UI improvements
```

**The agent will:**
1. Start the frontend server if needed
2. Navigate to http://localhost:5173
3. Take screenshots
4. Analyze visual design
5. Provide specific improvement suggestions

**Claude Code Feature Learned:** Visual testing with agents + MCP

### Step 9.5: Create Your Own Custom Agent

**Create a specialized agent for your domain.**

**Ask Claude Code:**
```
Create a custom agent called test-engineer in .claude/agents/ that:
1. Generates comprehensive test cases
2. Identifies edge cases
3. Writes pytest and vitest tests
4. Achieves 90%+ coverage
5. Follows TDD principles
```

**Agent structure:**
```markdown
---
name: test-engineer
description: Test automation specialist
model: sonnet
---

# Test Engineer Agent

You are a test automation expert...
```

**Use it:**
```
Ask Claude: "Use the test-engineer agent to create tests for my new feature"
```

**Claude Code Feature Learned:** Custom agent creation

### Step 9.6: Agent Memory

**Agents can have persistent memory in `.claude/agent-memory/`.**

**Check existing agent memory:**
```
Ask Claude: "Show me what the frontend-improver agent remembers about this project"
```

**Configure agent memory:**
```
Tell the code-reviewer agent to remember:
- Our coding standards prefer async/await over .then()
- We always add type hints to Python functions
- Error messages should be user-friendly
```

**Claude Code Feature Learned:** Agent memory systems

---

## 🔌 Lab 10: MCP (Model Context Protocol) Integration

### Step 10.1: Understanding MCP

**MCP (Model Context Protocol) connects Claude Code to external tools and services.**

**This project has 2 MCP servers pre-configured:**
- `chrome-devtools` - Browser automation and testing
- `drawio` - Diagram generation

**Check configuration:**
```
Ask Claude: "Show me the MCP servers configured in .mcp.json"
```

### Step 10.2: Use Chrome DevTools MCP

**Chrome DevTools MCP is already installed! Let's use it.**

**Ask Claude Code:**
```
Use Chrome DevTools MCP to:
1. Open http://localhost:5173 in a browser
2. Take a screenshot of the chat interface
3. Check for console errors or warnings
4. Analyze the page load performance
```

**Watch Claude:**
- Launch a browser instance
- Navigate to your app
- Capture a screenshot (you'll see it!)
- Inspect console logs
- Report findings

**Claude Code Feature Learned:** Browser automation via MCP

### Step 10.3: Test Responsive Design with MCP

**Ask Claude Code:**
```
Use Chrome DevTools MCP to test the chat interface at mobile, tablet, and desktop sizes. Take screenshots of each and suggest improvements.
```

**The MCP can:**
- Resize viewport (375px, 768px, 1920px)
- Take screenshots at each size
- Test mobile responsiveness
- Identify layout issues

**Claude Code Feature Learned:** Visual regression testing

### Step 10.4: Debug Network Issues with MCP

**Ask Claude Code:**
```
Use Chrome DevTools MCP to monitor network requests when I send a chat message. Check for errors or slow requests.
```

**The MCP will:**
1. Monitor network activity
2. Capture API calls to /api/v1/chat
3. Show response times
4. Identify failed requests
5. Suggest optimizations

**Claude Code Feature Learned:** Network debugging via MCP

### Step 10.5: Generate Diagrams with Draw.io MCP

**Draw.io MCP is already installed! Let's create diagrams.**

**Ask Claude Code:**
```
Use Draw.io MCP to create a system architecture diagram showing:
- React frontend (port 5173)
- FastAPI backend (port 8000)  
- Strands SDK agent
- Claude via Bedrock
- Data flow between components
```

**Watch Claude generate a professional diagram!**

**Create more diagrams:**
```
Use Draw.io MCP to create a sequence diagram of the chat message flow from user input to agent response
```

**Claude Code Feature Learned:** Architecture diagram generation

### Step 10.6: Advanced MCP Usage

**Combine MCP with agents for powerful workflows.**

**Ask Claude Code:**
```
Use the frontend-visual-inspector agent (which uses Chrome DevTools MCP) to:
1. Test the entire user journey
2. Take screenshots at each step
3. Check for accessibility issues
4. Provide a visual test report
```

**Claude Code Feature Learned:** Agent + MCP integration

### Step 10.7: Create a Custom MCP Server (Advanced)

**Challenge:** Build your own MCP server for project-specific needs.

**Ask Claude Code:**
```
Create a custom MCP server in .mcp.json that provides:
1. Database query interface (for SQLite)
2. Log file analyzer (parse backend logs)
3. Performance metrics (response times, error rates)
Call it "project-tools"
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

**Claude Code Feature Learned:** Custom MCP server development

---

## 📝 Lab 11: Memory & Context Management

### Step 11.1: Use Claude Code Memory

**Tell Claude Code:**
```
Remember that my preferred port for the backend is 8000 and frontend is 5173. Never suggest changing these.
```

**Then ask:**
```
What ports should I use for this project?
```

**Claude Code Feature Learned:** Persistent memory across sessions

### Step 11.2: Project-Specific Memory

**Tell Claude Code:**
```
Remember that this is an educational project for students. Always:
- Explain concepts clearly
- Prioritize readable code over clever code
- Add helpful comments for learning
- Suggest gradual improvements
```

**Then ask:**
```
Add a new feature to the agent
```

**Watch:** Claude's approach should be more educational now!

### Step 11.3: Check Memory

**Ask Claude Code:**
```
What do you remember about this project's preferences?
```

**Claude Code Feature Learned:** Memory inspection

---

## 🧪 Lab 12: Advanced Testing & Comprehensive Test Suite

### Step 12.1: Add Comprehensive Tests

**Ask Claude Code:**
```
Create a full test suite:
1. Backend: test_agent_service.py with tests for all tools
2. Backend: test_chat_endpoint.py with API tests  
3. Backend: test_config.py for configuration validation
4. Frontend: ChatInterface.test.tsx with React Testing Library
5. Frontend: API client tests
Goal: 80%+ code coverage
```

**Try it yourself:**
```bash
# Backend
pytest backend/tests/ --cov=backend --cov-report=term

# Frontend  
cd frontend && npm test
```

### Step 12.2: Create a Start Script

**Ask Claude Code:**
```
Create start.sh that:
1. Checks if virtual environment exists
2. Activates it
3. Starts backend in background
4. Starts frontend
5. Opens browser to localhost:5173
Make it executable
```

---

---

## 🏆 Lab 13: Deployment & Documentation

### Step 13.1: Add Deployment Config

**Ask Claude Code:**
```
Create Docker configuration:
1. Dockerfile for backend
2. Dockerfile for frontend
3. docker-compose.yml to run both services
4. Add health checks and proper environment variables
```

### Step 13.2: Complete Documentation

**Ask Claude Code:**
```
Update README.md with:
- Project overview
- Features list
- Setup instructions
- Architecture diagram (use text/ASCII)
- API documentation
- Troubleshooting section
```

### Step 13.3: Create Demo Video Script

**Ask Claude Code:**
```
Write a demo script for presenting this project that covers:
- Problem statement
- Solution overview
- Live demo flow
- Technical highlights
- Future enhancements
```

---

## 🎯 Extension Challenges

Ready for more? Try these advanced challenges:

### Challenge 1: Multi-Agent System
Create multiple specialized agents (research, coding, creative writing) and a router agent that delegates tasks.

### Challenge 2: Conversation Memory
Implement conversation summarization so the agent remembers context across sessions using a database.

### Challenge 3: Voice Interface
Add speech-to-text input and text-to-speech output for voice conversations.

### Challenge 4: Tool Marketplace
Build a plugin system where users can enable/disable different tools dynamically.

### Challenge 5: Analytics Dashboard
Add a dashboard showing agent usage stats, response times, and popular tools.

---

## 📚 Key Takeaways

After completing this workshop, you've learned:

**Claude Code Core Features:**
- ✅ Multi-step task automation
- ✅ Git integration and commit automation
- ✅ File operations (read, write, edit, grep, glob)
- ✅ Terminal command execution
- ✅ Testing integration

**Claude Code Plugins:**
- ✅ Language Server Protocol (LSP) integration
  - TypeScript LSP for React type checking
  - Pyright LSP for Python type safety
- ✅ GitHub plugin for PR reviews and issue management
- ✅ Plugin marketplace and installation
- ✅ Plugin configuration and reloading

**Claude Code Commands:**
- ✅ Built-in commands (/help, /commit, /init)
- ✅ Custom command creation (.claude/commands/)
- ✅ Command syntax and parameters
- ✅ Reusable prompt templates

**Claude Code Skills:**
- ✅ Built-in skills (/commit, /init, /review)
- ✅ Custom skill development (.claude/skills/)
- ✅ Skill parameters and workflows
- ✅ Multi-step automated processes

**Claude Code Hooks:**
- ✅ PreToolUse hooks (before actions)
- ✅ PostToolUse hooks (after actions)
- ✅ SessionStart hooks (session initialization)
- ✅ File protection hooks
- ✅ Test automation hooks
- ✅ Git workflow hooks
- ✅ Hook configuration in settings.json

**Claude Code Agents:**
- ✅ Custom agent creation (.claude/agents/)
- ✅ Specialized agent roles (code-reviewer, test-engineer)
- ✅ Agent delegation and collaboration
- ✅ Agent memory systems
- ✅ Agent tool configuration

**Claude Code MCP (Model Context Protocol):**
- ✅ MCP server installation and configuration
- ✅ Chrome DevTools MCP for browser automation
  - Screenshot capture
  - Console inspection
  - Network debugging
- ✅ Draw.io MCP for diagram generation
- ✅ Custom MCP server development
- ✅ .mcp.json configuration

**Claude Code Memory:**
- ✅ Persistent memory across sessions
- ✅ Project-specific preferences
- ✅ Memory inspection and management
- ✅ Context retention strategies

**Development Skills:**
- ✅ Full-stack application architecture
- ✅ AI agent development with Strands SDK
- ✅ API design and implementation
- ✅ Modern React patterns (hooks, context, query)
- ✅ Test-driven development (pytest, vitest)
- ✅ Professional git workflows
- ✅ Code quality automation
- ✅ Type safety (TypeScript, Python type hints)

**Best Practices:**
- ✅ Conventional commits (feat:, fix:, chore:)
- ✅ Automated testing with hooks
- ✅ Environment configuration (.env)
- ✅ Security (no eval, no secrets in code)
- ✅ Type safety and LSP integration
- ✅ Error handling and validation
- ✅ Code documentation (CLAUDE.md)
- ✅ Workflow automation with hooks
- ✅ Custom tooling (commands, skills, agents)

---

## 🆘 Troubleshooting

### Agent not responding?
- Check AWS credentials: `aws sts get-caller-identity`
- Verify .env has correct CLAUDE_MODEL_ID
- Check backend logs for errors
- Ensure Strands SDK is installed: `pip show strands-agents`

### Frontend can't reach backend?
- Ensure backend is running on port 8000
- Check Vite proxy config in vite.config.ts
- Look for CORS errors in browser console
- Verify backend health: `curl http://localhost:8000/health`

### Tests failing?
- Activate virtual environment first: `source venv/bin/activate`
- Install test dependencies: `pip install pytest httpx`
- Check test isolation (mock external APIs)
- Run tests individually to isolate failures

### Claude Code not using plugins?
- Run `/reload-plugins` after installation
- Check plugin status with `/plugin list`
- Restart Claude Code session
- Verify plugin installation: `/plugin marketplace list --installed`

### Custom commands not working?
- Check file location: `.claude/commands/command-name.md`
- Verify frontmatter format (name, description, usage)
- Command names must match filename (without .md)
- Restart Claude Code to reload commands

### Skills not appearing?
- Check directory structure: `.claude/skills/skill-name/SKILL.md`
- Skills require SKILL.md file (uppercase)
- Verify frontmatter in SKILL.md
- Skills show up with `/` prefix: `/skill-name`

### Hooks not firing?
- Check `.claude/settings.json` syntax (valid JSON)
- Verify hook matcher regex (Bash, Edit, Write, etc.)
- Check hook script permissions: `chmod +x .claude/hooks/*.sh`
- Test hook scripts manually first
- Check Claude Code console for hook errors

### Agents not available?
- Check `.claude/agents/agent-name.md` exists
- Verify agent frontmatter (name, description, model)
- Use exact agent name when invoking
- Agent files must have .md extension

### MCP servers not working?
- Check `.mcp.json` syntax (valid JSON)
- Verify npx is installed: `npx --version`
- Install MCP packages: `npx -y @drawio/mcp`
- Check MCP server status in Claude Code settings
- Restart Claude Code after MCP changes

### Memory not persisting?
- Check `.claude/memory/` directory exists
- Memory files must have .md extension
- Verify MEMORY.md index file
- Memory requires explicit save: "Remember that..."

### Chrome DevTools MCP issues?
- Ensure Chrome/Chromium is installed
- Check port conflicts (default: 9222)
- Try closing all Chrome instances first
- Install with: `npx -y chrome-devtools-mcp@latest`

### Type checking (LSP) not working?
- Install LSP plugins: `/plugin install typescript-lsp@claude-plugins-official`
- Reload plugins: `/reload-plugins`
- Check tsconfig.json / pyproject.toml exist
- Verify plugin status: `/plugin list`

---

## 🎓 What's Next?

**Share Your Project:**
- Push to GitHub
- Add screenshots to README
- Write a blog post about what you learned

**Continue Learning:**
- Explore Claude Code documentation: https://code.claude.com/docs
- Try the reference project in this repo
- Build your own custom Claude Code skills

**Join the Community:**
- Share your project on social media
- Help other participants
- Contribute to open-source Claude Code projects

---

## 📖 Resources

- **Reference Project:** See the main project in this repo for advanced patterns
- **Strands SDK Docs:** https://strandsagents.com/docs/
- **FastAPI Docs:** https://fastapi.tiangolo.com/
- **React Query Docs:** https://tanstack.com/query/latest
- **Claude Code Docs:** https://code.claude.com/docs
- **PLUGINS.md:** Detailed plugin setup guide
- **CLAUDE.md:** Best practices and architecture

---

## 🚀 Quick Reference Card

### Essential Commands
```bash
/help                    # Get help with Claude Code
/commit                  # Create a git commit with best practices
/init                    # Initialize CLAUDE.md documentation
/review                  # Review a pull request
/simplify                # Refactor code for simplicity
/start-dev               # Start backend + frontend servers (custom)
/component ComponentName # Generate React component (custom)
```

### Plugin Management
```bash
/plugin list                              # Show installed plugins
/plugin marketplace list                  # Browse available plugins
/plugin install <name>@<publisher>        # Install a plugin
/reload-plugins                           # Reload plugin configuration
```

### File Locations
```
.claude/
├── agents/              # Custom agents (*.md)
├── commands/            # Custom commands (*.md)
├── skills/              # Custom skills (*/SKILL.md)
├── hooks/               # Hook scripts (*.sh)
├── agent-memory/        # Agent persistent memory
└── settings.json        # Hook configuration

.mcp.json                # MCP server configuration
CLAUDE.md                # Project documentation for Claude
```

### Hook Types
- `PreToolUse` - Before Claude uses a tool (safety checks)
- `PostToolUse` - After Claude uses a tool (tests, linting)
- `SessionStart` - When starting a session (context)

### Agent Invocation
```
Use the <agent-name> agent to <task>

Examples:
- Use the code-reviewer agent to review my code
- Use the frontend-improver agent to enhance the UI
- Use the frontend-visual-inspector agent to test the design
- Use the backend-maintainer agent to optimize the API
```

### MCP Tools Available
- `chrome-devtools` - Browser automation, screenshots, debugging
- `drawio` - Generate architecture diagrams
- Custom MCP servers can be added to `.mcp.json`

### Memory Commands
```
Remember that <preference>              # Save to memory
What do you remember about <topic>?     # Recall from memory
Forget about <previous preference>      # Remove from memory
```

### Testing Commands
```bash
# Backend tests
source venv/bin/activate
pytest backend/tests/ -v --cov=backend

# Frontend tests
cd frontend && npm test

# All tests
./run-all-tests.sh
```

### Common Patterns

**Creating a feature end-to-end:**
1. Design with `/plan` or describe to Claude
2. Generate components with `/component`
3. Use LSP plugins for type safety
4. Run tests before committing
5. Commit with `/commit`
6. Create PR with GitHub plugin

**Debugging workflow:**
1. Use Chrome DevTools MCP to inspect frontend
2. Use backend-maintainer agent for API issues
3. Check logs and network requests
4. Fix and test
5. Use code-reviewer agent before committing

**UI improvement workflow:**
1. Use frontend-visual-inspector agent to screenshot
2. Use frontend-improver agent to implement changes
3. Test with Chrome DevTools MCP
4. Use LSP for type checking
5. Commit changes

---

**🎉 Congratulations on completing the LabCamp workshop!**

You now have hands-on experience with:
- Building full-stack AI agents with Strands SDK
- Using all major Claude Code features (plugins, commands, skills, hooks, agents, MCP)
- Professional development workflows
- Test-driven development
- Custom tooling and automation

**Next steps:**
- Build your own AI agent project
- Create custom commands and skills for your workflow
- Share your learnings with the community
- Explore the Claude Code documentation

Keep experimenting, keep building, and most importantly - have fun coding with Claude! 🚀
