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

## 🎓 Lab 6: Professional Workflows

### Step 6.1: Set Up Plugins

**Try these commands:**
```
/plugin install typescript-lsp@claude-plugins-official
/plugin install pyright-lsp@claude-plugins-official
/plugin install github@claude-plugins-official
/reload-plugins
```

**Ask Claude Code:**
```
Run type checking on my TypeScript and Python code. Fix any type errors found.
```

**Claude Code Feature Learned:** LSP plugins for code quality

### Step 6.2: Add Comprehensive Tests

**Ask Claude Code:**
```
Create a full test suite:
1. Backend: test_agent_service.py with tests for all tools
2. Backend: test_chat_endpoint.py with API tests
3. Frontend: ChatInterface.test.tsx with React Testing Library
Goal: 80%+ code coverage
```

**Try it yourself:**
```bash
# Backend
pytest backend/tests/ --cov=backend --cov-report=term

# Frontend
cd frontend && npm test
```

### Step 6.3: Create a Start Script

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

### Step 6.4: Use Memory Feature

**Tell Claude Code:**
```
Remember that my preferred port for the backend is 8000 and frontend is 5173. Never suggest changing these.
```

**Then ask:**
```
What ports should I use for this project?
```

**Claude Code Feature Learned:** Persistent memory across sessions

### Step 6.5: Commit with Best Practices

**Try the commit skill:**
```
/commit
```

Watch Claude:
1. Check git status
2. Review changes
3. Generate a conventional commit message
4. Run pre-commit hooks (tests!)
5. Create the commit

**Claude Code Feature Learned:** Automated git workflows with skills

---

## 🏆 Lab 7: Deployment & Documentation

### Step 7.1: Add Deployment Config

**Ask Claude Code:**
```
Create Docker configuration:
1. Dockerfile for backend
2. Dockerfile for frontend
3. docker-compose.yml to run both services
4. Add health checks and proper environment variables
```

### Step 7.2: Complete Documentation

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

### Step 7.3: Create Demo Video Script

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

**Claude Code Features:**
- ✅ Multi-step task automation
- ✅ Git integration and commit automation
- ✅ Plugin system (LSP, GitHub)
- ✅ Hooks for workflow automation
- ✅ Skills for common tasks (/commit, /init)
- ✅ Memory for project preferences
- ✅ Testing integration
- ✅ Documentation generation

**Development Skills:**
- ✅ Full-stack application architecture
- ✅ AI agent development with Strands SDK
- ✅ API design and implementation
- ✅ Modern React patterns
- ✅ Test-driven development
- ✅ Professional git workflows
- ✅ Code quality automation

**Best Practices:**
- ✅ Conventional commits
- ✅ Automated testing
- ✅ Environment configuration
- ✅ Security (no eval, no secrets in code)
- ✅ Type safety
- ✅ Error handling
- ✅ Code documentation

---

## 🆘 Troubleshooting

### Agent not responding?
- Check AWS credentials: `aws sts get-caller-identity`
- Verify .env has correct CLAUDE_MODEL_ID
- Check backend logs for errors

### Frontend can't reach backend?
- Ensure backend is running on port 8000
- Check Vite proxy config in vite.config.ts
- Look for CORS errors in browser console

### Tests failing?
- Activate virtual environment first
- Install test dependencies: `pip install pytest httpx`
- Check test isolation (mock external APIs)

### Claude Code not using plugins?
- Run `/reload-plugins` after installation
- Check plugin status with `/plugin list`
- Restart Claude Code session

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

**🎉 Congratulations on completing the LabCamp workshop!**

You now have hands-on experience building AI agents with Claude Code. Keep experimenting, keep building, and most importantly - have fun coding with Claude! 🚀
