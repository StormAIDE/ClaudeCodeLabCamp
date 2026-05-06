#!/bin/bash
# Protect sensitive files from modification
# Prevents Claude from editing credentials, lock files, and system directories

INPUT=$(cat)
FILE_PATH=$(echo "$INPUT" | jq -r '.tool_input.file_path // empty')

# Protected file patterns
PROTECTED_PATTERNS=(
  ".env"
  ".env.local"
  ".env.production"
  "package-lock.json"
  "yarn.lock"
  "poetry.lock"
  "Pipfile.lock"
  ".git/"
  "node_modules/"
  "claudecodeenv/"
  "venv/"
  ".venv/"
  "__pycache__/"
)

for pattern in "${PROTECTED_PATTERNS[@]}"; do
  if [[ "$FILE_PATH" == *"$pattern"* ]]; then
    echo "🔒 BLOCKED: $FILE_PATH is protected" >&2
    echo "   Pattern: $pattern" >&2
    echo "   This file should not be modified by automation." >&2
    echo "   If you need to modify it, edit manually." >&2
    exit 2  # Block the edit
  fi
done

exit 0  # Allow the edit
