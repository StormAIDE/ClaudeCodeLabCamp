# Setup Instructions

This guide will help you set up and run the ClaudeCode Lab Agent application.

## Prerequisites

- Python 3.14.0 (already configured with virtual environment)
- Node.js 18+ and npm
- AWS CLI configured with Bedrock access
- AWS credentials in terminal session

## Backend Setup

### 1. Activate Python Virtual Environment

```bash
source claudecodeenv/bin/activate
```

### 2. Install Python Dependencies

```bash
pip install -r requirements.txt
```

### 3. Create .env File

```bash
cp .env.example .env
```

**Note:** AWS credentials should already be configured in your terminal session via `aws configure` or environment variables. The backend will use those credentials automatically.

### 4. Start the Backend Server

```bash
python backend/main.py
```

Or use uvicorn directly:

```bash
uvicorn backend.main:app --reload --host 0.0.0.0 --port 8000
```

The backend will be available at `http://localhost:8000`

API documentation: `http://localhost:8000/docs`

## Frontend Setup

### 1. Navigate to Frontend Directory

```bash
cd frontend
```

### 2. Install Node Dependencies

```bash
npm install
```

### 3. Start the Development Server

```bash
npm run dev
```

The frontend will be available at `http://localhost:5173`

## Running Both Services

You can use the provided startup script to run both services:

```bash
./start.sh
```

Or manually in separate terminals:

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

## Running Tests

### Backend Tests (43 tests)

```bash
source claudecodeenv/bin/activate
python -m pytest backend/tests/ -v
```

### Frontend Tests (30 tests)

```bash
cd frontend
npm test
```

### Run All Tests

```bash
source claudecodeenv/bin/activate && \
python -m pytest backend/tests/ -v && \
cd frontend && npm test -- --run
```

## Testing the Application

1. Open your browser to `http://localhost:5173`
2. You should see the ClaudeCode Lab Agent interface
3. Try asking questions like:
   - "What's the weather in San Francisco?"
   - "Calculate 25 * 4 + 10" (uses safe AST parser, no eval!)
   - "Hello, how can you help me?"

### Security Features

- **Safe Math Evaluation:** The calculate tool uses AST parsing instead of `eval()` to prevent code injection
- **Input Validation:** Empty or whitespace-only messages are rejected with a 422 error
- **Dependency Injection:** AgentService is a singleton to improve performance and reduce Bedrock connections

## Troubleshooting

### AWS Credentials Error

If you get AWS credentials errors, ensure your terminal session has AWS credentials configured:

```bash
aws configure
# OR
export AWS_ACCESS_KEY_ID=your_key
export AWS_SECRET_ACCESS_KEY=your_secret
export AWS_SESSION_TOKEN=your_token  # if using temporary credentials
```

### Port Already in Use

If port 8000 or 5173 is already in use, you can change them:

**Backend:** Edit `.env` and change `API_PORT`

**Frontend:** Edit `frontend/vite.config.ts` and change the port in server settings

### Import Errors

Make sure your virtual environment is activated before running the backend:

```bash
source claudecodeenv/bin/activate
```

## Architecture

- **Backend:** FastAPI + Strands Agents SDK
- **Frontend:** React + TypeScript + Vite + TanStack Query + Zustand
- **AI:** Claude 4 via Amazon Bedrock (Strands SDK)
- **API:** RESTful with streaming support

## Development Workflow

1. Make changes to backend code in `backend/`
2. Make changes to frontend code in `frontend/src/`
3. Both services support hot reload during development
4. Commit changes to `feature/lab-work` branch
5. Push to GitHub when ready

## Next Steps

- Add more custom tools to the agent (see `backend/services/agent_service.py`)
- Customize the UI (see `frontend/src/components/`)
- Add streaming support to the frontend
- Implement message history persistence
- Add authentication if needed
