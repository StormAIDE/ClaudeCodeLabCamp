# Full-Stack AI Agent Application

A production-ready full-stack application demonstrating clean architecture patterns for building AI agent systems. This project serves as a hands-on learning environment for the **ClaudeCode Labcamp** - focused on repeatable workflows, verification patterns, and practical productivity enhancements for daily software engineering tasks.

## 🎯 Project Overview

This application showcases how to build a modern, scalable AI agent platform with:
- **Interactive chat interface** for conversing with AI agents
- **Real-time streaming responses** using Server-Sent Events (SSE)
- **Extensible tool and agent system** using registry patterns
- **Type-safe API communication** across the full stack
- **Clean architecture** with clear separation of concerns

## ✨ Features

- 🤖 **AI Agent System** - Intelligent agent powered by Claude 4 via Amazon Bedrock
- 🔧 **Safe Custom Tools** - Extensible tool system with security built-in (AST-based calculator, weather)
- 💬 **Real-Time Streaming** - Watch AI responses generate in real-time with SSE
- 🎨 **Modern UI** - React 19 + TypeScript with Tailwind CSS
- 🚀 **FastAPI Backend** - High-performance async Python backend with dependency injection
- 🧠 **Claude 4 Integration** - Powered by Strands Agents SDK and Amazon Bedrock
- 🔒 **Security First** - Input validation, safe tool execution, no eval()
- 📦 **Clean Architecture** - Dependency injection, clear separation of concerns
- ✅ **Comprehensive Tests** - 73 tests (43 backend + 30 frontend) all passing
- 🔌 **Claude Code Plugins** - Professional IDE features (TypeScript/Python LSP, GitHub, Git workflows)
- 🪝 **Claude Code Hooks** - Automated workflows (auto-format, safety checks, context injection)

## 📊 Current Status

### ✅ Implemented & Verified
- ✅ Backend FastAPI server with Strands SDK integration
- ✅ Frontend React 19 + TypeScript application with Vite
- ✅ Agent service with safe custom tools (weather, AST-based calculator)
- ✅ API endpoints: `/health`, `/api/v1/agent/chat`, `/api/v1/agent/status`
- ✅ **Dependency Injection** - Singleton AgentService pattern for performance
- ✅ **Input Validation** - Pydantic validators reject empty/whitespace messages
- ✅ **Security Hardening** - Safe AST parser (no eval()), prevents code injection
- ✅ Configuration management with Pydantic Settings
- ✅ CORS configuration for local development
- ✅ Environment-based configuration (.env)
- ✅ **Comprehensive Test Suite** - 73 tests (43 backend + 30 frontend) all passing
- ✅ Virtual environment setup (Python 3.14.0)
- ✅ Git repository with main and feature/lab-work branches
- ✅ Complete documentation (README, SETUP, CLAUDE.md, per-directory READMEs)
- ✅ Quick start script (`start.sh`)
- ✅ **Code Review Complete** - All critical issues resolved

### 📋 Planned Enhancements
- 📋 Frontend streaming UI support for token-by-token responses
- 📋 Message history persistence (localStorage or database)
- 📋 Authentication and authorization
- 📋 Multi-agent switching in UI
- 📋 Tool usage visualization
- 📋 Enhanced error boundaries
- 📋 Docker containerization
- 📋 CI/CD pipeline with GitHub Actions

## 🛠️ Tech Stack

### Backend
- **FastAPI** - Modern, fast Python web framework
- **Strands Agents SDK** - AI agent orchestration
- **Pydantic** - Data validation and settings management
- **Python 3.14.0** - Latest Python features

### Frontend
- **React 19** - Latest UI library with improved hooks
- **TypeScript** - Full type safety
- **Vite** - Fast build tool with HMR
- **TanStack Query** - Server state management and caching
- **Zustand** - Client state management
- **Tailwind CSS** - Utility-first styling
- **Vitest** - Fast unit testing framework
- **Testing Library** - Component testing utilities

### AI Layer
- **Claude 4** - Via Amazon Bedrock
- **Strands Agents SDK** - Custom tools and streaming support

## 🚀 Quick Start

### Prerequisites

- **Python 3.14.0** (virtual environment already set up in `claudecodeenv/`)
- **Node.js 18+** and npm
- **AWS Account** with Bedrock access and Claude 4 enabled
- **AWS CLI** configured with credentials
- **Git**

### Setup

1. **Clone the repository:**
   ```bash
   git clone https://github.com/StormAIDE/ClaudeCodeLabCamp.git
   cd ClaudeCodeLabCamp
   ```

2. **Configure AWS credentials in terminal:**
   ```bash
   aws configure
   # OR export credentials directly:
   export AWS_ACCESS_KEY_ID=your_key
   export AWS_SECRET_ACCESS_KEY=your_secret
   export AWS_SESSION_TOKEN=your_token  # if using temporary credentials
   ```

3. **Create .env file:**
   ```bash
   cp .env.example .env
   ```
   
   **Note:** AWS credentials are NOT needed in .env since they're configured in your terminal session.

4. **Install backend dependencies:**
   ```bash
   source claudecodeenv/bin/activate
   pip install -r requirements.txt
   ```

5. **Install frontend dependencies:**
   ```bash
   cd frontend
   npm install
   cd ..
   ```

### Running the Application

#### Option 1: Quick Start Script (Recommended)

```bash
./start.sh
```

This will start both backend and frontend services automatically.

#### Option 2: Manual Start (Separate Terminals)

**Terminal 1 - Backend:**
```bash
source claudecodeenv/bin/activate
python backend/main.py
```

**Terminal 2 - Frontend:**
```bash
cd frontend
npm run dev
```

Open your browser to [http://localhost:5173](http://localhost:5173)

**Access Points:**
- Frontend: http://localhost:5173
- Backend API: http://localhost:8000
- API Docs: http://localhost:8000/docs

## 📂 Project Structure

```
ClaudeCodeTest/
├── backend/                         # Python FastAPI backend
│   ├── main.py                     # FastAPI application entry point
│   ├── config.py                   # Configuration management (Pydantic Settings)
│   ├── api/                        # API layer
│   │   ├── routes.py              # Route aggregation
│   │   ├── dependencies.py        # Dependency injection (singleton AgentService)
│   │   └── endpoints/             # API endpoints
│   │       └── agent.py           # Agent chat endpoints with validation
│   ├── services/                   # Business logic
│   │   └── agent_service.py       # Agent service with Strands SDK & safe tools
│   ├── tests/                      # Test suite (43 tests)
│   │   ├── test_config.py         # Configuration tests
│   │   ├── test_dependencies.py   # Package import tests
│   │   ├── test_agent_service.py  # Agent and tool tests
│   │   ├── test_endpoints.py      # API endpoint tests
│   │   └── conftest.py            # Test fixtures
│   ├── requirements.txt            # Python dependencies
│   └── README.md                   # Backend-specific documentation
│
├── frontend/                       # React 19 TypeScript frontend
│   ├── src/
│   │   ├── components/            # React components
│   │   │   ├── ChatInterface.tsx  # Main chat interface
│   │   │   ├── MessageList.tsx    # Message display
│   │   │   ├── MessageInput.tsx   # Input component
│   │   │   └── StatusBadge.tsx    # Agent status indicator
│   │   ├── api/                   # API client
│   │   │   └── agent.ts           # Agent API calls (Axios)
│   │   ├── store/                 # Zustand state management
│   │   │   └── agentStore.ts      # Agent state
│   │   ├── types/                 # TypeScript type definitions
│   │   ├── hooks/                 # Custom React hooks
│   │   ├── test/                  # Test files (30 tests)
│   │   ├── App.tsx                # Main App component
│   │   └── main.tsx               # React entry point with TanStack Query
│   ├── package.json               # Node.js dependencies & scripts
│   ├── vite.config.ts             # Vite configuration
│   ├── vitest.config.ts           # Vitest test configuration
│   └── README.md                  # Frontend-specific documentation
│
├── claudecodeenv/                 # Python virtual environment (gitignored)
├── .env                           # Environment variables (create from .env.example)
├── .env.example                   # Environment variables template
├── start.sh                       # Quick start script (both services)
├── demo-plugins.sh                # Plugin installation demo script
├── demo-hooks.sh                  # Hooks demonstration script
├── pytest.ini                     # Pytest configuration
├── SETUP.md                       # Detailed setup instructions
├── README.md                      # This file (project overview)
├── CLAUDE.md                      # Claude Code workflow documentation
├── PLUGINS.md                     # Claude Code plugins setup guide
├── PLUGIN-EXAMPLES.md             # Plugin use cases and examples
├── HOOKS.md                       # Claude Code hooks guide
└── .claude/                       # Claude Code configuration
    ├── settings.json              # Project hooks configuration
    └── hooks/                     # Hook scripts
        ├── block-dangerous.sh     # Block destructive commands
        ├── protect-files.sh       # Protect sensitive files
        ├── run-tests.sh           # Auto-run tests after changes
        └── project-context.txt    # Project context injection
```

## 🔌 API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| `GET` | `/health` | Health check endpoint |
| `POST` | `/api/v1/agent/chat` | Send message to agent (streaming supported) |
| `GET` | `/api/v1/agent/status` | Check agent service status |

### API Documentation

Once the backend is running, visit:
- **Swagger UI:** [http://localhost:8000/docs](http://localhost:8000/docs)
- **ReDoc:** [http://localhost:8000/redoc](http://localhost:8000/redoc)

## ✅ Testing & Verification

### Check if Services are Running

**1. Check Backend Health:**
```bash
# Health check endpoint
curl http://localhost:8000/health

# Expected response:
# {"status":"healthy","service":"ClaudeCode Lab Agent"}
```

**2. Check Agent Status:**
```bash
# Agent service status
curl http://localhost:8000/api/v1/agent/status

# Expected response:
# {"status":"Agent service is ready","agent_name":"lab-assistant"}
```

**3. Test Agent Chat (Non-Streaming):**
```bash
# Send a test message to the agent
curl -X POST http://localhost:8000/api/v1/agent/chat \
  -H "Content-Type: application/json" \
  -d '{"message": "Hello, who are you?"}'

# Expected: JSON response with agent reply
```

**4. Test Agent Chat (Streaming):**
```bash
# Stream agent response
curl -X POST http://localhost:8000/api/v1/agent/chat \
  -H "Content-Type: application/json" \
  -H "Accept: text/event-stream" \
  -d '{"message": "What is 2 + 2?", "stream": true}'

# Expected: Server-Sent Events stream
```

**5. Check Frontend:**
- Open browser to [http://localhost:5173](http://localhost:5173)
- You should see the chat interface with "ClaudeCode Lab Agent" header
- Status indicator should show "Ready" or agent name

**6. Verify API Documentation:**
```bash
# Open in browser
open http://localhost:8000/docs  # macOS
# or
xdg-open http://localhost:8000/docs  # Linux
```

### Check Process Status

```bash
# Check if backend is running
lsof -i :8000
# Should show Python process listening on port 8000

# Check if frontend is running
lsof -i :5173
# Should show Node/Vite process listening on port 5173

# Check AWS credentials
aws sts get-caller-identity
# Should return your AWS identity without errors
```

### Verify Logs

**Backend Logs:**
- Look for: `INFO: Application startup complete.`
- Look for: `INFO: Uvicorn running on http://0.0.0.0:8000`

**Frontend Logs:**
- Look for: `VITE v[version] ready in [time]ms`
- Look for: `➜ Local: http://localhost:5173/`

## 🧪 Testing

### Run Tests

**Backend Tests (43 tests):**
```bash
source claudecodeenv/bin/activate
python -m pytest backend/tests/ -v
```

**Frontend Tests (30 tests):**
```bash
cd frontend
npm test
```

**Run All Tests (73 total):**
```bash
source claudecodeenv/bin/activate && \
python -m pytest backend/tests/ -v && \
cd frontend && npm test -- --run
```

**Test Coverage:**
```bash
# Backend coverage
python -m pytest backend/tests/ --cov=backend --cov-report=html

# Frontend coverage
cd frontend && npm run test:coverage
```

### Try It Out

Once both services are running, try these example queries in the UI:

1. **Weather Query:**
   ```
   What's the weather in San Francisco?
   ```

2. **Safe Calculator (AST-based, no eval!):**
   ```
   Calculate 25 * 4 + 10
   ```
   Expected result: 110

3. **Complex Math:**
   ```
   What is (100 - 25) * 3 + 50?
   ```
   Expected result: 275

4. **General Chat:**
   ```
   Hello! What can you help me with?
   ```

5. **Security Test (should be rejected):**
   ```
   Calculate __import__('os').system('echo test')
   ```
   Expected: Error message about unsupported expression

## 🛠️ Extending the Application

### Adding New Tools

Edit `backend/services/agent_service.py` and add new tools with the `@tool` decorator:

```python
from strands import tool

@tool
def my_new_tool(param: str) -> str:
    """
    Description of what this tool does.
    The docstring is shown to Claude as the tool description.
    
    Args:
        param: Parameter description
    
    Returns:
        Result description
    """
    # Implementation here
    # IMPORTANT: Validate inputs and implement safely
    return f"Result for {param}"
```

Then add the tool to the Agent initialization:

```python
self.agent = Agent(
    name="lab-assistant",
    model=settings.CLAUDE_MODEL_ID,
    system_prompt="...",  # Use system_prompt, not instructions
    tools=[get_weather, calculate, my_new_tool]  # Add your tool here
)
```

**Important Security Notes:**
- Never use `eval()` or `exec()` in tools
- Validate all inputs
- Use type hints for parameters
- Handle errors gracefully
- Document security considerations

### Customizing the Agent

Modify the agent's behavior in `backend/services/agent_service.py`:

- **Change system prompt:** Edit the `system_prompt` parameter (not `instructions`)
- **Add/remove tools:** Modify the `tools` list
- **Change model:** Update `CLAUDE_MODEL_ID` in `.env` file
- **Call the agent:** Use `invoke_async(message)` (not `run_async`)
- **Extract response:** Parse `AgentResult.to_dict()['message']['content']`

## 🐛 Troubleshooting

### AWS Credentials Error
- Make sure AWS credentials are configured in your terminal session
- Run `aws configure` to set up credentials
- Or export them: `export AWS_ACCESS_KEY_ID=...`
- Credentials should NOT be in .env file

### Backend won't start
- Verify AWS credentials in terminal: `aws sts get-caller-identity`
- Check Python version: `python --version` (should be 3.14.0)
- Ensure virtual environment is activated: `source claudecodeenv/bin/activate`
- Try reinstalling dependencies: `pip install -r requirements.txt`

### Frontend build errors
- Clear node_modules: `rm -rf node_modules && npm install`
- Check Node version: `node --version` (should be 18+)
- Verify all dependencies installed: `npm install`

### Port Already in Use
- Backend (8000): Change `API_PORT` in `.env`
- Frontend (5173): Change port in `frontend/vite.config.ts`

### Import Errors
- Activate virtual environment before running backend
- Ensure all dependencies are installed

For more detailed troubleshooting, see [SETUP.md](SETUP.md)

## 📝 Git Workflow

- **Main branch:** `main`
- **Feature branch:** `feature/lab-work`

Commit changes to the feature branch:
```bash
git add .
git commit -m "Your commit message"
git push origin feature/lab-work
```

## 📋 Quick Reference Commands

### Development Commands

```bash
# Activate Python virtual environment
source claudecodeenv/bin/activate

# Start backend
python backend/main.py

# Start frontend (in separate terminal)
cd frontend && npm run dev

# Start both services
./start.sh

# Install backend dependencies
pip install -r requirements.txt

# Install frontend dependencies
cd frontend && npm install
```

### Testing Commands

```bash
# Test backend health
curl http://localhost:8000/health

# Test agent status
curl http://localhost:8000/api/v1/agent/status

# Test chat endpoint
curl -X POST http://localhost:8000/api/v1/agent/chat \
  -H "Content-Type: application/json" \
  -d '{"message": "Hello"}'

# Check running processes
lsof -i :8000  # Backend
lsof -i :5173  # Frontend

# Verify AWS credentials
aws sts get-caller-identity
```

### Git Commands

```bash
# Check status
git status

# Commit changes
git add .
git commit -m "feat: your message"

# Push to feature branch
git push origin feature/lab-work

# Pull latest changes
git pull origin feature/lab-work
```

### Troubleshooting Commands

```bash
# Check Python version
python --version

# Check Node version
node --version

# List installed Python packages
pip list

# Kill process on port
lsof -ti:8000 | xargs kill -9  # Backend
lsof -ti:5173 | xargs kill -9  # Frontend

# Clear frontend cache
cd frontend && rm -rf node_modules dist && npm install

# Reinstall backend dependencies
pip install --force-reinstall -r requirements.txt
```

## 🔌 Claude Code Plugins

This project includes Claude Code plugins to showcase professional development tooling. Plugins enhance the development experience with:

- **TypeScript LSP** - Real-time type checking for React components
- **Pyright LSP** - Python type safety for FastAPI backend
- **GitHub Integration** - PR creation, issue management, code review
- **Commit Commands** - Automated conventional commit messages

### Quick Plugin Setup

```bash
# Install all recommended plugins
/plugin install typescript-lsp@claude-plugins-official
/plugin install pyright-lsp@claude-plugins-official
/plugin install github@claude-plugins-official
/plugin marketplace add anthropics/claude-code
/plugin install commit-commands@anthropics-claude-code
/reload-plugins
```

### Demo Script

Run the plugin demo to install language server binaries and see usage examples:

```bash
./demo-plugins.sh
```

### Documentation

- **[PLUGINS.md](PLUGINS.md)** - Complete plugin setup guide with installation instructions
- **[PLUGIN-EXAMPLES.md](PLUGIN-EXAMPLES.md)** - Real-world use cases and educational examples
- **[Official Plugins](https://claude.com/plugins)** - Browse the official plugin marketplace

### Educational Benefits

Plugins demonstrate:
- How professional IDEs provide real-time type checking
- Language Server Protocol (LSP) architecture
- Git workflow automation and best practices
- Cross-tool integration (GitHub, Slack, etc.)
- Type-driven development patterns

## 🪝 Claude Code Hooks

This project includes hooks that automate workflows and enforce best practices. Hooks run shell commands automatically at key points in Claude Code's lifecycle.

### Active Hooks

**Configured in `.claude/settings.json`:**

- **Auto-format code** - Prettier runs after every file edit
- **Block dangerous commands** - Prevents destructive operations (rm -rf, dd, fork bombs)
- **Protect sensitive files** - Blocks edits to .env, lock files, git internals
- **Inject project context** - Reminds Claude of project rules on session start

### View Hooks

```bash
# In Claude Code, type:
/hooks
```

This shows all configured hooks, when they trigger, and their commands.

### Demo Script

Run the hooks demo to test safety features:

```bash
./demo-hooks.sh
```

**Example tests:**
- Attempts to run `rm -rf /` → Blocked ✅
- Attempts to edit `.env` → Blocked ✅  
- Safe commands like `ls -la` → Allowed ✅

### Documentation

- **[HOOKS.md](HOOKS.md)** - Complete hooks guide with examples and student exercises
- **[Hooks Reference](https://code.claude.com/docs/en/hooks)** - Official hooks documentation

### Educational Benefits

Hooks demonstrate:
- Automated code formatting (consistency without manual work)
- Security gates (prevent destructive operations)
- File protection strategies (safeguard credentials and configs)
- Context injection (maintain consistency across sessions)
- Event-driven automation (respond to tool calls, file changes, etc.)

## 📚 Additional Resources

- [FastAPI Documentation](https://fastapi.tiangolo.com/)
- [Strands Agents SDK](https://strandsagents.com/docs/)
- [React Documentation](https://react.dev/)
- [Tailwind CSS](https://tailwindcss.com/)
- [Claude API Documentation](https://docs.anthropic.com/)
- [Amazon Bedrock Documentation](https://docs.aws.amazon.com/bedrock/)
- [Claude Code Plugins](https://code.claude.com/docs/en/discover-plugins)

## 📄 License

This project is part of the ClaudeCode Labcamp learning environment.

