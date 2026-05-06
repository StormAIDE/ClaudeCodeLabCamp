# Backend - ClaudeCode Lab Agent

Python FastAPI backend with Strands Agents SDK for AI-powered chat using Claude 4 via Amazon Bedrock. 

## Setup

1. **Activate virtual environment:**
   ```bash
   source ../claudecodeenv/bin/activate
   ```

2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Configure environment:**
   - Copy `../.env.example` to `../.env`
   - Ensure AWS credentials are configured in your terminal session
   - Update `CLAUDE_MODEL_ID` if needed (default: eu.anthropic.claude-sonnet-4-5-20250929-v1:0)

4. **Run the server:**
   ```bash
   python -m backend.main
   # OR
   uvicorn backend.main:app --reload --host 0.0.0.0 --port 8000
   ```

## API Endpoints

- `GET /health` - Health check
- `GET /api/v1/agent/status` - Agent status
- `POST /api/v1/agent/chat` - Chat with agent (supports streaming and non-streaming)

### Example Request

```bash
curl -X POST http://localhost:8000/api/v1/agent/chat \
  -H "Content-Type: application/json" \
  -d '{"message":"What is 25 * 4 + 10?","stream":false}'
```

## Architecture

- **FastAPI** - Async web framework
- **Strands SDK** - Agent orchestration with Claude 4
- **Pydantic** - Data validation and settings
- **Dependency Injection** - Singleton AgentService for performance
- **Safe Tool Execution** - AST-based math parser (no eval!)

## Project Structure

```
backend/
├── main.py              # FastAPI app entry point
├── config.py            # Pydantic Settings (loads from .env)
├── api/
│   ├── routes.py       # Route aggregation
│   ├── dependencies.py # Dependency injection (singleton AgentService)
│   └── endpoints/
│       └── agent.py    # Agent chat endpoints
├── services/
│   └── agent_service.py # Strands SDK agent service
└── tests/               # Test suite (43 tests)
    ├── test_config.py
    ├── test_dependencies.py
    ├── test_agent_service.py
    └── test_endpoints.py
```

## Key Features

### Security
- **Safe Math Evaluation:** Uses AST parsing instead of eval() to prevent code injection
- **Input Validation:** Rejects empty/whitespace messages
- **CORS Protection:** Configured for specific origins only

### Performance
- **Singleton Pattern:** AgentService instantiated once and reused across requests
- **Async Operations:** Full async/await support throughout
- **Dependency Injection:** FastAPI's Depends() for clean separation

### Tools Available

1. **get_weather(location)** - Mock weather information
2. **calculate(expression)** - Safe mathematical expression evaluator
   - Only allows: +, -, *, /, ** (power), unary +/-
   - Rejects: function calls, imports, variable assignments

## Testing

Run all tests:
```bash
source ../claudecodeenv/bin/activate
python -m pytest backend/tests/ -v
```

Run specific test file:
```bash
python -m pytest backend/tests/test_agent_service.py -v
```

Run with coverage:
```bash
python -m pytest backend/tests/ --cov=backend --cov-report=html
```

**Current coverage:** 43 tests covering config, dependencies, agent service, and endpoints

## Adding New Tools

1. Define tool in `services/agent_service.py`:

```python
@tool
def my_new_tool(param: str) -> str:
    """Tool description shown to Claude."""
    # Your implementation
    return result
```

2. Add to Agent initialization:

```python
self.agent = Agent(
    name="lab-assistant",
    model=settings.CLAUDE_MODEL_ID,
    system_prompt="...",
    tools=[get_weather, calculate, my_new_tool]  # Add here
)
```

## Strands SDK Usage

**Correct method names:**
- `agent.invoke_async(message)` - Single response (NOT run_async)
- `agent.stream_async(message)` - Streaming response

**Response handling:**
```python
response = await self.agent.invoke_async(message)
result_dict = response.to_dict()
text = result_dict['message']['content'][0]['text']
```

## Environment Variables

Required in `.env`:
- `APP_NAME` - Application name
- `API_HOST` - Host (default: 0.0.0.0)
- `API_PORT` - Port (default: 8000)
- `CORS_ORIGINS` - Comma-separated allowed origins
- `CLAUDE_MODEL_ID` - Bedrock model ID

## Development

- Hot reload enabled with `--reload` flag
- API docs available at `http://localhost:8000/docs`
- Logs use Python logging module (not print statements)

## Important Notes

- **AWS Credentials:** Must be configured in terminal session (not in .env)
- **Legacy Code:** The `backend/app/` directory is legacy - DO NOT USE
- **Active Implementation:** Use `backend/main.py` as entry point
