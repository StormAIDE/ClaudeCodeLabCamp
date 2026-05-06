# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This is the **ClaudeCode Labcamp Project** - a full-stack AI agent application built with FastAPI and React. It demonstrates clean architecture patterns for building AI agent systems with Strands SDK and Claude 4 via Amazon Bedrock.

## Development Commands

### Backend Development

**Setup:**
```bash
# IMPORTANT: Python 3.13 required (3.14 breaks pydantic-core)
python3.13 -m venv claudecodeenv
source claudecodeenv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Create .env from template (first time only)
cp .env.example .env
```

**AWS Credentials (REQUIRED before starting backend):**
```bash
# Export credentials from AWS profile to environment
export AWS_ACCESS_KEY_ID=$(aws configure get aws_access_key_id --profile claudecodelabcampparticipants)
export AWS_SECRET_ACCESS_KEY=$(aws configure get aws_secret_access_key --profile claudecodelabcampparticipants)
export AWS_SESSION_TOKEN=$(aws configure get aws_session_token --profile claudecodelabcampparticipants)
export AWS_DEFAULT_REGION=eu-central-1

# Verify
aws sts get-caller-identity
```

**Run backend server:**
```bash
# AFTER exporting AWS credentials
source claudecodeenv/bin/activate
python -m backend.main

# Or with uvicorn directly
uvicorn backend.main:app --reload --host 0.0.0.0 --port 8000
```

**Backend will be available at:**
- API: http://localhost:8000
- Swagger docs: http://localhost:8000/docs
- Health check: http://localhost:8000/health

### Frontend Development

**Setup:**
```bash
cd frontend

# Install dependencies (first time only)
npm install
```

**Run frontend server:**
```bash
npm run dev          # Start dev server (http://localhost:5173)
npm run build        # Build for production
npm run preview      # Preview production build
npm run lint         # Run ESLint
npm test             # Run unit tests with Vitest
npm run test:ui      # Run tests with UI
npm run test:coverage # Run tests with coverage report
```

### Running Both Services

**Quick start (both services):**
```bash
./start.sh
```

**Manual (separate terminals):**
```bash
# Terminal 1
source claudecodeenv/bin/activate && python -m backend.main

# Terminal 2
cd frontend && npm run dev
```

### Starting the App on Windows (via Claude Code)

When the user says "start the app", do the following steps in order:

1. **Check/create venv** — venv is at `claudecodeenv/` in project root; activation script is `claudecodeenv/Scripts/activate` (not `bin/activate`)
2. **Install backend deps if needed:** `source claudecodeenv/Scripts/activate && pip install -r requirements.txt`
3. **Start backend in background:** `source claudecodeenv/Scripts/activate && uvicorn backend.main:app --reload --host 0.0.0.0 --port 8000 > /tmp/backend.log 2>&1 &`
4. **Start frontend in background:** `cd frontend && npm run dev > /tmp/frontend.log 2>&1 &`
5. **Verify** both started by checking `/tmp/backend.log` and `/tmp/frontend.log`

URLs once running:
- Frontend: http://localhost:5173
- Backend API: http://localhost:8000
- API Docs: http://localhost:8000/docs

> AWS credentials must be configured in the environment for Bedrock/agent calls to work.

## Testing

### Backend Testing

**Test suite includes:**
- Configuration tests (`test_config.py`) - Settings validation and parsing
- Dependency tests (`test_dependencies.py`) - Verify all packages are importable
- Agent service tests (`test_agent_service.py`) - Agent logic and tool functions
- API endpoint tests (`test_endpoints.py`) - FastAPI routes and error handling

**Run backend tests:**
```bash
# Activate virtual environment first
source claudecodeenv/bin/activate

# Run all tests
python -m pytest backend/tests/ -v

# Run specific test file
python -m pytest backend/tests/test_config.py -v

# Run with coverage
python -m pytest backend/tests/ --cov=backend --cov-report=html

# Run tests in watch mode (requires pytest-watch)
ptw backend/tests/
```

**Current coverage:** 62 tests total (43 backend + 19 frontend) covering config, dependencies, agent service, endpoints, API client, store, and React components

**Run all tests:**
```bash
./run-all-tests.sh
```

### Testing Requirements

**CRITICAL - Run tests before every change:**
1. **Before making any code changes:** Run the full test suite
2. **After making changes:** Re-run tests to ensure nothing broke
3. **Before committing:** All tests must pass (62 tests total (43 backend + 19 frontend))
4. **When adding new features:** Write tests for new functionality
5. **When fixing bugs:** Add tests that reproduce the bug, then fix it

## Architecture Overview

### Backend Structure

```
backend/
├── main.py              # FastAPI app entry point
├── config.py            # Pydantic Settings for env vars
├── api/                 # API layer
│   ├── routes.py       # Route aggregation
│   ├── dependencies.py # Dependency injection (singleton AgentService)
│   └── endpoints/
│       └── agent.py    # Agent chat endpoints with input validation
├── services/            # Business logic
│   └── agent_service.py # Strands SDK agent service with safe tools
└── tests/               # Test suite (35 tests)
    ├── test_config.py
    ├── test_dependencies.py
    ├── test_agent_service.py
    └── test_endpoints.py
```

**Key architectural decisions:**
- Configuration via Pydantic Settings (`backend/config.py`) loads from `.env` AND shell environment vars
- **AWS Credentials**: Must be exported to environment before starting backend (pydantic reads from shell vars)
- Agent logic isolated in `agent_service.py` using **Strands SDK only** (no anthropic SDK fallback)
- **Dependency injection** (`api/dependencies.py`) - Singleton AgentService pattern for performance
- **Input validation** - Pydantic validators reject empty/whitespace messages
- **Security** - Tools use safe implementations (AST parser for math, no eval())
- API routes aggregated in `api/routes.py` and mounted with `/api/v1` prefix
- CORS configured to allow frontend on localhost:5173 and localhost:3000

### Frontend Structure

```
frontend/src/
├── App.tsx                    # Main app with agent status header
├── main.tsx                   # Entry point with QueryClientProvider
├── components/
│   ├── ChatInterface.tsx      # Main chat UI component
│   ├── MessageList.tsx        # Displays message history
│   └── MessageInput.tsx       # Input field with send button
├── api/
│   └── agent.ts              # Axios API client for backend
└── store/
    └── agentStore.ts         # Zustand store for messages & status
```

**State management:**
- **Zustand** (`agentStore.ts`) - Client state (messages, agent status)
- **TanStack Query** (`main.tsx`) - Server state, caching, mutations
- Messages stored with `{ id, role, content, timestamp }`

### Strands SDK Integration

**Location:** `backend/services/agent_service.py`

**How it works:**
1. Import: `from strands import Agent, tool`
2. Define tools with `@tool` decorator - these become callable by the agent
3. **Agent initialized with `model`, `system_prompt`, and `tools` list**
4. Model ID configured in `.env` as `CLAUDE_MODEL_ID`
5. **Agent methods: `invoke_async()` for single response, `stream_async()` for streaming**
6. **Response handling: Extract text from `AgentResult.to_dict()['message']['content']`**

**Security Note:**
- The `calculate` tool uses safe AST parsing (not `eval()`)
- Only allows mathematical operators: +, -, *, /, ** (power), unary +/-
- Rejects any code execution attempts (e.g., `__import__`, function calls)

**Adding new tools:**
```python
@tool
def your_tool_name(param: str) -> str:
    """Docstring is shown to Claude as tool description."""
    # Implementation
    return result

# Then add to Agent initialization:
self.agent = Agent(
    name="lab-assistant",
    model=settings.CLAUDE_MODEL_ID,
    system_prompt="...",  # Use system_prompt, not instructions
    tools=[get_weather, calculate, your_tool_name]  # Add here
)

# Calling the agent:
response = await self.agent.invoke_async(message)  # Use invoke_async, not run_async
result_dict = response.to_dict()
text = result_dict['message']['content'][0]['text']  # Extract text from response
```

## Configuration Management

**Environment variables** (`.env`):
- `APP_NAME` - Application name
- `API_HOST` / `API_PORT` - Backend server config
- `CORS_ORIGINS` - Comma-separated list of allowed origins
- `CLAUDE_MODEL_ID` - Bedrock model ID (currently: `eu.anthropic.claude-sonnet-4-5-20250929-v1:0`)

**AWS Credentials:**
- **CRITICAL: NOT stored in .env** - must be exported to shell environment BEFORE starting backend
- **Required setup:**
  ```bash
  export AWS_ACCESS_KEY_ID=$(aws configure get aws_access_key_id --profile claudecodelabcampparticipants)
  export AWS_SECRET_ACCESS_KEY=$(aws configure get aws_secret_access_key --profile claudecodelabcampparticipants)
  export AWS_SESSION_TOKEN=$(aws configure get aws_session_token --profile claudecodelabcampparticipants)
  export AWS_DEFAULT_REGION=eu-central-1
  ```
- Pydantic Settings reads these from environment variables, not from AWS profile directly
- Strands SDK uses these credentials for Bedrock API access
- Verify with: `aws sts get-caller-identity`
- **If `use_bedrock: false`** → credentials not exported before starting backend

**Changing the Claude model:**
Edit `CLAUDE_MODEL_ID` in `.env` - Strands SDK supports any Bedrock Claude model ID.

## Git Workflow

- **Main Branch**: `main`
- **Feature Branch**: `feature/lab-work` (active development)
- Commit to `feature/lab-work` after meaningful changes
- Repository: https://github.com/StormAIDE/ClaudeCodeLabCamp.git

## Claude Code Plugins

This project uses Claude Code plugins to enhance development workflow and demonstrate professional tooling. See **[PLUGINS.md](PLUGINS.md)** for complete setup guide.

**Recommended plugins for students:**
- **TypeScript LSP** - Real-time type checking for React frontend
- **Pyright LSP** - Python type safety for FastAPI backend  
- **GitHub** - Professional version control workflows
- **Commit Commands** - Automated git best practices

**Quick install:**
```bash
/plugin install typescript-lsp@claude-plugins-official
/plugin install pyright-lsp@claude-plugins-official
/plugin install github@claude-plugins-official
/plugin marketplace add anthropics/claude-code
/plugin install commit-commands@anthropics-claude-code
/reload-plugins
```

## Claude Code Hooks

This project includes hooks to automate workflows and enforce best practices.

**Active hooks:**
- **Block dangerous commands** - Prevents destructive operations (rm -rf, dd, etc.)
- **Protect sensitive files** - Blocks edits to .env, lock files, git internals
- **Inject project context** - Reminds Claude of project rules on session start

**Hooks are configured in:** `.claude/settings.json`

**View hooks:** Type `/hooks` in Claude Code

**Note:** For code formatting, use Prettier manually when needed:
```bash
npx prettier --write <file>
```

## Important Notes

- **Python 3.13 required** - venv MUST use Python 3.13 (3.14 breaks pydantic-core build)
- **Do not read `claudecodeenv/` folder** - Python virtual env, wastes tokens
- **Always activate virtual environment** before running backend: `source claudecodeenv/bin/activate`
- **AWS credentials MUST be exported** - Export to environment before starting backend (see Configuration section)
- **Agent will fail without Bedrock access** - Check `use_bedrock: true` at `/api/v1/agent/status`
- **Frontend proxies API** - Vite proxies `/api` to `http://localhost:8000` (see `vite.config.ts`)
- **All tests must pass** - Run `./run-all-tests.sh` before committing

## Tech Stack Reference

**Backend:**
- FastAPI (async web framework)
- Strands Agents SDK only (no anthropic SDK) - https://strandsagents.com/docs/user-guide/quickstart/python/
- Pydantic Settings (configuration)
- Python 3.13 (⚠️ 3.14 not compatible)

**Frontend:**
- React 19 with TypeScript
- Vite (build tool)
- TanStack Query (server state)
- Zustand (client state)
- Tailwind CSS (styling)
- Axios (HTTP client)

**AI:**
- Claude model_id="eu.anthropic.claude-sonnet-4-5-20250929-v1:0" via Amazon Bedrock
- Strands Agents SDK handles agent orchestration, tool calling, and streaming


## Rules
- **ALWAYS run tests before and after making changes** - Use `./run-all-tests.sh`
- Always use conventional commits: feat:, fix:, chore:, docs:, test:
- After every change, run tests, then commit AND push to GitHub automatically
- Backend is in /backend — Python, FastAPI, Strands SDK
- Frontend is in /frontend — TypeScript, React, Vite
- Never use print() for logging — use Python logging module
- Never commit secrets or .env files
- All 35 tests must pass before committing
- When adding features, write tests for them
- When fixing bugs, add regression tests