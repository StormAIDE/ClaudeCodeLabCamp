#!/bin/bash
# Block dangerous commands before they execute
# This hook prevents destructive operations that could harm the system

INPUT=$(cat)
COMMAND=$(echo "$INPUT" | jq -r '.tool_input.command // empty')

# List of dangerous patterns
DANGEROUS_PATTERNS=(
  "rm -rf /"
  "rm -rf ~"
  "rm -rf \$HOME"
  "dd if="
  "> /dev/sda"
  "mkfs"
  ":\(\)\{ :\|:& \};"  # Fork bomb
  "curl.*\|.*bash"     # Pipe to bash
  "curl.*\|.*sh"       # Pipe to sh
  "wget.*\|.*bash"     # Pipe to bash
  "wget.*\|.*sh"       # Pipe to sh
  "chmod 777"          # Overly permissive
  "sudo rm"            # Dangerous sudo
)

for pattern in "${DANGEROUS_PATTERNS[@]}"; do
  if echo "$COMMAND" | grep -qE "$pattern"; then
    echo "🚫 BLOCKED: Command matches dangerous pattern '$pattern'" >&2
    echo "   Command: $COMMAND" >&2
    echo "   This operation is not allowed for safety reasons." >&2
    exit 2  # Exit 2 = block the command
  fi
done

exit 0  # Exit 0 = allow the command
