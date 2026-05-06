#!/bin/bash

# ClaudeCode Lab Agent Startup Script
# This script starts both backend and frontend services

echo "🚀 Starting ClaudeCode Lab Agent..."
echo ""

# Check if virtual environment exists
if [ ! -d "claudecodeenv" ]; then
    echo "❌ Virtual environment not found. Please run: python -m venv claudecodeenv"
    exit 1
fi

# Check if node_modules exists in frontend
if [ ! -d "frontend/node_modules" ]; then
    echo "📦 Installing frontend dependencies..."
    cd frontend && npm install && cd ..
fi

# Check if requirements are installed
if ! source claudecodeenv/bin/activate && python -c "import fastapi" 2>/dev/null; then
    echo "📦 Installing backend dependencies..."
    source claudecodeenv/bin/activate
    pip install -r requirements.txt
fi

# Create .env if it doesn't exist
if [ ! -f ".env" ]; then
    echo "📝 Creating .env file from .env.example..."
    cp .env.example .env
fi

echo ""
echo "✅ Starting services..."
echo ""
echo "Backend: http://localhost:8000"
echo "Frontend: http://localhost:5173"
echo "API Docs: http://localhost:8000/docs"
echo ""
echo "Press Ctrl+C to stop all services"
echo ""

# Function to cleanup on exit
cleanup() {
    echo ""
    echo "🛑 Stopping services..."
    kill 0
    exit
}

trap cleanup SIGINT SIGTERM

# Start backend in background
source claudecodeenv/bin/activate
python -m backend.main &
BACKEND_PID=$!

# Give backend time to start
sleep 2

# Start frontend in background
cd frontend
npm run dev &
FRONTEND_PID=$!

# Wait for both processes
wait
