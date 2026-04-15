#!/bin/bash

# ClaudeCode Lab Agent Stop Script
# This script stops both backend and frontend services

echo "🛑 Stopping ClaudeCode Lab Agent services..."

# Function to kill process on port
kill_port() {
    local port=$1
    local service=$2

    local pids=$(lsof -ti:$port 2>/dev/null)
    if [ -n "$pids" ]; then
        echo "   Stopping $service (port $port)..."
        kill $pids 2>/dev/null
        sleep 1
        # Force kill if still running
        if lsof -ti:$port >/dev/null 2>&1; then
            echo "   Force stopping $service..."
            kill -9 $pids 2>/dev/null
        fi
        echo "   ✅ $service stopped"
    else
        echo "   ℹ️  $service not running (port $port)"
    fi
}

# Stop backend (port 8000)
kill_port 8000 "Backend"

# Stop frontend (port 5173)
kill_port 5173 "Frontend"

# Also kill any python backend.main processes
BACKEND_PIDS=$(ps aux | grep "python.*backend.main" | grep -v grep | awk '{print $2}')
if [ -n "$BACKEND_PIDS" ]; then
    echo "   Cleaning up remaining backend processes..."
    kill $BACKEND_PIDS 2>/dev/null
    echo "   ✅ Backend processes cleaned up"
fi

# Kill any npm vite processes
VITE_PIDS=$(ps aux | grep "vite" | grep -v grep | awk '{print $2}')
if [ -n "$VITE_PIDS" ]; then
    echo "   Cleaning up remaining Vite processes..."
    kill $VITE_PIDS 2>/dev/null
    echo "   ✅ Vite processes cleaned up"
fi

echo ""
echo "✅ All services stopped!"
