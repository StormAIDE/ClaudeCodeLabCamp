#!/bin/bash
# Automatically run tests after code changes
# Runs Python tests for .py files, TypeScript tests for .ts/.tsx files

set -e

INPUT=$(cat)
FILE_PATH=$(echo "$INPUT" | jq -r '.tool_input.file_path // empty')

# Only run tests for Python or TypeScript files
if [[ ! "$FILE_PATH" =~ \.(py|ts|tsx)$ ]]; then
  exit 0  # Not a code file, skip tests
fi

echo "🧪 Running tests after modifying $FILE_PATH..." >&2

# Backend tests for Python files
if [[ "$FILE_PATH" =~ \.py$ ]]; then
  cd "$CLAUDE_PROJECT_DIR"
  if [ -d "claudecodeenv" ]; then
    echo "   → Running backend tests..." >&2
    source claudecodeenv/bin/activate
    python -m pytest backend/tests/ -v --tb=short 2>&1 | head -20 >&2 || {
      echo "   ❌ Backend tests failed!" >&2
      exit 0  # Don't block, just warn
    }
    echo "   ✅ Backend tests passed" >&2
  fi
fi

# Frontend tests for TypeScript files
if [[ "$FILE_PATH" =~ \.(ts|tsx)$ ]]; then
  cd "$CLAUDE_PROJECT_DIR/frontend"
  if [ -f "package.json" ]; then
    echo "   → Running frontend tests..." >&2
    npm test -- --run 2>&1 | tail -20 >&2 || {
      echo "   ❌ Frontend tests failed!" >&2
      exit 0  # Don't block, just warn
    }
    echo "   ✅ Frontend tests passed" >&2
  fi
fi

exit 0
