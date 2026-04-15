---
name: start-dev
description: Start both backend (FastAPI) and frontend (Vite) development servers
invocation: user
---

# Start Development Servers

Starts both backend (FastAPI) and frontend (Vite) development servers.

## Instructions

When this skill is invoked:

1. **Start the backend server:**
   - Navigate to project root
   - Activate virtual environment: `source claudecodeenv/bin/activate`
   - Run: `uvicorn backend.main:app --reload --host 0.0.0.0 --port 8000`
   - Run this in the background

2. **Start the frontend server:**
   - Navigate to frontend directory
   - Run: `npm run dev`
   - Run this in the background

3. **Report to user:**
   - Backend API: http://localhost:8000
   - Backend Docs: http://localhost:8000/docs
   - Frontend: http://localhost:5173
   - Let them know both servers are starting in the background

## Notes

- Both processes run in the background
- Check the output files to see if servers started successfully
- Backend requires AWS credentials to be configured in the environment
- Frontend proxies `/api` requests to the backend
