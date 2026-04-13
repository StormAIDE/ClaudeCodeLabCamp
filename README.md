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

- 🤖 **Multi-Agent Support** - Switch between different AI agents with specialized capabilities
- 🔧 **Custom Tools** - Extensible tool system for agents (web search, calculator, and more)
- 💬 **Real-Time Streaming** - Watch AI responses generate in real-time
- 🎨 **Modern UI** - React + TypeScript with Tailwind CSS
- 🚀 **FastAPI Backend** - High-performance async Python backend
- 🧠 **Claude 4 Integration** - Powered by Anthropic's Claude 4 via Amazon Bedrock
- 📦 **Modular Architecture** - Easy to extend with new agents and tools

## 📊 Current Status

### ✅ Implemented
- ✅ Backend FastAPI server with Strands SDK integration
- ✅ Frontend React + TypeScript application with Vite
- ✅ Agent service with custom tools (weather, calculator)
- ✅ API endpoints: `/health`, `/api/v1/agent/chat`, `/api/v1/agent/status`
- ✅ Configuration management with Pydantic Settings
- ✅ CORS configuration for local development
- ✅ Environment-based configuration (.env)
- ✅ Virtual environment setup (Python 3.14.0)
- ✅ Git repository initialized with main and feature branches
- ✅ Comprehensive documentation (README, SETUP, CLAUDE.md)
- ✅ Quick start script (`start.sh`)

### 🚧 In Progress
- 🚧 Frontend streaming support for real-time responses
- 🚧 Message history persistence
- 🚧 Enhanced UI with message timestamps and user indicators
- 🚧 Additional custom tools and agent capabilities

### 📋 Planned
- 📋 Authentication and authorization
- 📋 Multi-agent switching in UI
- 📋 Conversation history management
- 📋 Tool usage visualization
- 📋 Error boundary and better error handling
- 📋 Unit and integration tests
- 📋 Docker containerization
- 📋 CI/CD pipeline

## 🛠️ Tech Stack

### Backend
- **FastAPI** - Modern, fast Python web framework
- **Strands Agents SDK** - AI agent orchestration
- **Pydantic** - Data validation and settings management
- **Python 3.14.0** - Latest Python features

### Frontend
- **React 18+** - UI library
- **TypeScript** - Type safety
- **Vite** - Fast build tool
- **TanStack Query** - Server state management
- **Zustand** - Client state management
- **Tailwind CSS** - Utility-first styling

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
├── backend/                      # Python FastAPI backend
│   ├── main.py                  # FastAPI application entry point
│   ├── config.py                # Configuration management (Pydantic Settings)
│   ├── api/                     # API layer
│   │   ├── routes.py           # Route aggregation
│   │   └── endpoints/          # API endpoints
│   │       └── agent.py        # Agent chat endpoints
│   └── services/                # Business logic
│       └── agent_service.py    # Agent service with Strands SDK
│
├── frontend/                    # React TypeScript frontend
│   ├── src/
│   │   ├── components/         # React components
│   │   │   ├── ChatInterface.tsx    # Main chat interface
│   │   │   ├── MessageList.tsx      # Message display
│   │   │   └── MessageInput.tsx     # Input component
│   │   ├── api/                # API client
│   │   │   └── agent.ts        # Agent API calls
│   │   ├── store/              # Zustand state management
│   │   │   └── agentStore.ts   # Agent state
│   │   ├── App.tsx             # Main App component
│   │   └── main.tsx            # React entry point
│   ├── package.json            # Node.js dependencies
│   └── vite.config.ts          # Vite configuration
│
├── claudecodeenv/              # Python virtual environment (gitignored)
├── requirements.txt            # Python dependencies
├── .env                        # Environment variables (create from .env.example)
├── .env.example                # Environment variables template
├── start.sh                    # Quick start script
├── SETUP.md                    # Detailed setup instructions
├── README.md                   # This file
└── CLAUDE.md                   # Claude Code workflow documentation
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

## 🧪 Try It Out

Once both services are running, try these example queries in the UI:

1. **Weather Query:**
   ```
   What's the weather in San Francisco?
   ```

2. **Calculator:**
   ```
   Calculate 25 * 4 + 10
   ```

3. **General Chat:**
   ```
   Hello! What can you help me with?
   ```

4. **Tool Testing:**
   ```
   Can you search the web for latest AI news?
   ```

## 🛠️ Extending the Application

### Adding New Tools

Edit `backend/services/agent_service.py` and add new tools with the `@tool` decorator:

```python
from strands import tool

@tool
def my_new_tool(param: str) -> str:
    """
    Description of what this tool does.
    
    Args:
        param: Parameter description
    
    Returns:
        Result description
    """
    # Implementation here
    return f"Result for {param}"
```

Then add the tool to the Agent initialization:

```python
self.agent = Agent(
    name="lab-assistant",
    instructions="...",
    tools=[get_weather, calculate, my_new_tool]  # Add your tool here
)
```

### Customizing the Agent

Modify the agent's behavior in `backend/services/agent_service.py`:

- **Change instructions:** Edit the `instructions` parameter
- **Add/remove tools:** Modify the `tools` list
- **Change model:** Update the Agent configuration (defaults to Claude 4 via Bedrock)

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

## 📚 Additional Resources

- [FastAPI Documentation](https://fastapi.tiangolo.com/)
- [Strands Agents SDK](https://strandsagents.com/docs/)
- [React Documentation](https://react.dev/)
- [Tailwind CSS](https://tailwindcss.com/)
- [Claude API Documentation](https://docs.anthropic.com/)
- [Amazon Bedrock Documentation](https://docs.aws.amazon.com/bedrock/)

## 📄 License

This project is part of the ClaudeCode Labcamp learning environment.

