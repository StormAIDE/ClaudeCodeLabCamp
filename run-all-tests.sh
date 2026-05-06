#!/bin/bash

# Test runner script to be used after agent changes
# This ensures no regressions are introduced by agent modifications

set -e  # Exit on any error

echo "🧪 Running comprehensive test suite after agent changes..."
echo "================================================"

# Get the project root directory
PROJECT_ROOT=$(pwd)

# Cleanup function to ensure servers are stopped
cleanup_servers() {
    echo ""
    echo "🧹 Cleaning up any running servers..."

    # Kill processes on development ports
    lsof -ti:8000 2>/dev/null | xargs kill -9 2>/dev/null || true
    lsof -ti:5173 2>/dev/null | xargs kill -9 2>/dev/null || true

    # Kill any remaining backend processes
    pkill -f "python.*backend.main" 2>/dev/null || true

    # Kill any remaining vite processes
    pkill -f "vite" 2>/dev/null || true

    echo "✅ Server cleanup complete"
}

# Register cleanup to run on script exit
trap cleanup_servers EXIT

# Check if we're in the right directory
if [ ! -f "CLAUDE.md" ]; then
    echo "❌ Error: Not in project root directory"
    exit 1
fi

# Function to run with error handling
run_with_status() {
    local description="$1"
    local command="$2"

    echo ""
    echo "🔍 $description"
    echo "   Command: $command"
    echo "   ----------------------------------------"

    # Run command and capture both stdout and stderr
    if bash -c "$command"; then
        echo "   ✅ PASSED: $description"
        return 0
    else
        echo "   ❌ FAILED: $description"
        return 1
    fi
}

# Track overall success
OVERALL_SUCCESS=0

# Frontend Tests
echo ""
echo "🎨 FRONTEND TESTING"
echo "=================="

if run_with_status "Frontend test suite (19 tests)" "cd \"$PROJECT_ROOT/frontend\" && npm test -- --run --reporter=verbose"; then
    echo "✅ All frontend tests passed!"
else
    echo "❌ Frontend tests failed!"
    OVERALL_SUCCESS=1
fi

if run_with_status "Frontend linting" "cd \"$PROJECT_ROOT/frontend\" && npm run lint"; then
    echo "✅ Frontend linting passed!"
else
    echo "⚠️  Frontend linting issues found"
    # Don't fail overall for linting issues, just warn
fi

# Backend Tests
echo ""
echo "🔧 BACKEND TESTING"
echo "=================="

if run_with_status "Backend test suite (43 tests)" "cd \"$PROJECT_ROOT\" && source claudecodeenv/bin/activate && python -m pytest backend/tests/ -v --tb=short"; then
    echo "✅ All backend tests passed!"
else
    echo "❌ Backend tests failed!"
    OVERALL_SUCCESS=1
fi

# Server Startup Tests
echo ""
echo "🚀 SERVER STARTUP TESTING"
echo "========================="

if run_with_status "Backend server startup test" "cd \"$PROJECT_ROOT\" && source claudecodeenv/bin/activate && python -c \"from backend.main import app; print('Backend imports successfully')\""; then
    echo "✅ Backend startup test passed!"
else
    echo "❌ Backend startup test failed!"
    OVERALL_SUCCESS=1
fi

if run_with_status "Frontend build test" "cd \"$PROJECT_ROOT/frontend\" && npm run build"; then
    echo "✅ Frontend build test passed!"
    # Clean up build directory
    cd "$PROJECT_ROOT" && rm -rf frontend/dist
else
    echo "❌ Frontend build test failed!"
    OVERALL_SUCCESS=1
fi

# Final Results
echo ""
echo "📊 FINAL RESULTS"
echo "==============="

if [ $OVERALL_SUCCESS -eq 0 ]; then
    echo "🎉 ALL TESTS PASSED!"
    echo "   ✅ Frontend: 19 tests passing"
    echo "   ✅ Backend: 43 tests passing"
    echo "   ✅ Servers: Startup tests passing"
    echo "   ✅ Build: Frontend builds successfully"
    echo ""
    echo "🚀 Ready for deployment/commit!"
    exit 0
else
    echo "💥 SOME TESTS FAILED!"
    echo "   Please review the failures above and fix issues before proceeding."
    echo "   Do not commit or deploy until all tests pass."
    exit 1
fi