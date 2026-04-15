# Plugin Examples & Use Cases

This document provides concrete examples of how to use plugins in the ClaudeCode Labcamp project.

## Example 1: TypeScript Type Error Detection

### Without Plugin
```typescript
// frontend/src/components/ChatInterface.tsx
interface Message {
  id: string;
  role: 'user' | 'assistant';
  content: string;
  timestamp: Date;
}

// This compiles but could cause runtime errors
const message = {
  id: '123',
  role: 'admin',  // ❌ Wrong role type - not caught until runtime
  content: 'Hello',
  timestamp: new Date()
};
```

### With TypeScript LSP Plugin
1. Claude detects the error immediately after you type it
2. Diagnostic appears: "Type '"admin"' is not assignable to type '"user" | "assistant"'"
3. Claude automatically suggests: "Change 'admin' to 'user' or 'assistant'"
4. **No need to run the app to find the bug!**

**Educational value:** Students learn that type systems catch bugs at compile-time, not runtime.

---

## Example 2: Python Type Safety

### Without Plugin
```python
# backend/services/agent_service.py
def process_message(message):  # ❌ No type hints
    if len(message) > 0:
        return message.upper()
    return None
```

### With Pyright LSP Plugin
```python
def process_message(message: str) -> str | None:  # ✅ Proper type hints
    if len(message) > 0:
        return message.upper()
    return None
```

**What Claude sees:**
- "Missing type annotation for function parameter"
- "Return type should be specified"
- Claude automatically adds proper type hints

**Educational value:** Students learn Python type hints improve code maintainability and IDE support.

---

## Example 3: Conventional Commits

### Without Plugin
```bash
git add .
git commit -m "fixed stuff"  # ❌ Poor commit message
```

### With Commit Commands Plugin
```bash
/commit-commands:commit
```

**Claude automatically:**
1. Runs `git status` and `git diff`
2. Analyzes what changed
3. Generates: `fix: resolve type error in ChatInterface component`
4. Adds conventional prefix (feat:, fix:, chore:, etc.)
5. Creates commit with proper format

**Educational value:** Students learn industry-standard commit conventions used in professional teams.

---

## Example 4: Pull Request Creation

### Without Plugin
```bash
# Manual process:
git push origin feature/my-branch
# Open browser
# Navigate to GitHub
# Click "New Pull Request"
# Fill out title and description
# Submit PR
```

### With GitHub Plugin
```bash
# Just tell Claude:
"Create a PR for this branch"
```

**Claude automatically:**
1. Runs `git log main..HEAD` to see all commits
2. Runs `git diff main...HEAD` to see all changes
3. Generates PR title: "Add real-time chat streaming support"
4. Generates PR body with:
   - Summary of changes
   - Test plan
   - Related issues
5. Creates PR using `gh pr create`

**Educational value:** Students learn professional PR workflow without manual overhead.

---

## Example 5: Cross-File Type Checking

### Scenario: Adding a new API endpoint

**File 1: `backend/api/endpoints/agent.py`**
```python
from pydantic import BaseModel

class ChatRequest(BaseModel):
    message: str
    conversation_id: str  # Added new field

@router.post("/chat")
async def chat(request: ChatRequest):
    return {"response": "Hello"}
```

**File 2: `frontend/src/api/agent.ts`**
```typescript
export async function sendMessage(message: string) {
  return axios.post('/api/v1/agent/chat', {
    message: message
    // ❌ Missing conversation_id!
  });
}
```

**What happens:**

### Without Plugins
- Backend change works fine
- Frontend sends request
- **Runtime error:** 422 Unprocessable Entity
- Student must debug by checking network tab, reading error messages, etc.

### With TypeScript LSP + Pyright LSP
1. **Backend side:** Pyright validates the Pydantic model
2. **Frontend side:** TypeScript LSP doesn't know about backend changes yet
3. Student runs the frontend
4. Gets 422 error
5. Claude sees the error in console logs
6. **With type checking:** Claude suggests updating the TypeScript API client

**Educational value:** Shows the importance of API contracts and type safety across frontend/backend boundaries.

---

## Example 6: Refactoring with Confidence

### Scenario: Rename a function across multiple files

**Starting point:**
```typescript
// frontend/src/api/agent.ts
export async function sendChatMessage(message: string) { /* ... */ }

// frontend/src/components/MessageInput.tsx
import { sendChatMessage } from '../api/agent';
sendChatMessage(input);

// frontend/src/components/ChatInterface.tsx  
import { sendChatMessage } from '../api/agent';
sendChatMessage(userMessage);
```

**Task:** Rename `sendChatMessage` to `sendMessage`

### Without LSP Plugin
Tell Claude: "Rename sendChatMessage to sendMessage"

**Claude's approach:**
1. Uses `grep` to find all occurrences
2. Manually edits each file
3. **Might miss some references** or break things

### With TypeScript LSP Plugin
Tell Claude: "Rename sendChatMessage to sendMessage"

**Claude's approach:**
1. Uses LSP "Find References" to get **exact** locations
2. Performs rename operation
3. LSP validates that no references are broken
4. **Catches errors immediately** if something is missed

**Educational value:** Shows how professional IDEs enable safe refactoring at scale.

---

## Example 7: Learning from Diagnostics

### Scenario: Common React mistake

```typescript
// frontend/src/components/MessageList.tsx
import React, { useEffect } from 'react';

function MessageList({ messages }) {  // ❌ No type for props
  useEffect(() => {
    console.log(messages);
  });  // ❌ Missing dependency array
  
  return (
    <div>
      {messages.map(msg => (  // ❌ Missing key prop
        <div>{msg.content}</div>
      ))}
    </div>
  );
}
```

### With TypeScript LSP Plugin

**Claude sees these diagnostics automatically:**
1. "Parameter 'messages' implicitly has an 'any' type"
2. "React Hook useEffect has a missing dependency: 'messages'"
3. "Each child in a list should have a unique 'key' prop"

**Claude fixes all three issues in one turn:**
```typescript
interface MessageListProps {
  messages: Message[];
}

function MessageList({ messages }: MessageListProps) {
  useEffect(() => {
    console.log(messages);
  }, [messages]);  // ✅ Dependency array added
  
  return (
    <div>
      {messages.map(msg => (
        <div key={msg.id}>{msg.content}</div>  // ✅ Key prop added
      ))}
    </div>
  );
}
```

**Educational value:** Students learn React best practices through real-time feedback.

---

## Example 8: Integration Testing with GitHub Actions

### Scenario: Setting up CI/CD

**Without GitHub Plugin:**
- Manually create `.github/workflows/test.yml`
- Copy/paste workflow from documentation
- Push and hope it works
- Debug YAML syntax errors

**With GitHub Plugin:**
Tell Claude: "Set up GitHub Actions to run tests on every PR"

**Claude can:**
1. Check existing workflows: `gh api repos/{owner}/{repo}/actions/workflows`
2. Create workflow file with proper syntax
3. Verify the workflow: `gh workflow view test.yml`
4. Test it: `gh workflow run test.yml`
5. Monitor results: `gh run list`

**Educational value:** Students learn CI/CD setup without manual YAML debugging.

---

## Example 9: Code Navigation

### Scenario: Understanding agent architecture

**Student asks:** "How does the agent process messages?"

### Without LSP Plugin
**Claude's approach:**
1. Uses `grep` to find "process_message"
2. Reads multiple files
3. Tries to trace execution flow manually

### With Pyright LSP Plugin
**Claude's approach:**
1. Uses "Go to Definition" on `process_message`
2. Uses "Find References" to see all callers
3. Uses "Type Hierarchy" to understand inheritance
4. Traces the exact execution path with 100% accuracy

**Educational value:** Shows how to navigate large codebases professionally.

---

## Example 10: Multi-Plugin Workflow

### Scenario: Complete feature development

**Task:** Add a "clear chat" button to the UI

**Full workflow with plugins:**

1. **Create feature branch**
   ```bash
   # Claude uses git
   git checkout -b feature/clear-chat-button
   ```

2. **Implement frontend (TypeScript LSP active)**
   - Add button to `MessageInput.tsx`
   - TypeScript LSP catches prop type errors immediately
   - Add handler to `agentStore.ts`
   - TypeScript LSP validates Zustand state types

3. **Add backend endpoint (Pyright LSP active)**
   - Add `/clear` endpoint to `agent.py`
   - Pyright validates FastAPI route types
   - Update service layer
   - Pyright checks async/await usage

4. **Write tests**
   - Frontend test: `MessageInput.test.tsx`
   - Backend test: `test_endpoints.py`
   - Run tests: all pass ✅

5. **Commit with conventional format**
   ```bash
   /commit-commands:commit
   # Claude generates: "feat: add clear chat button with confirmation dialog"
   ```

6. **Create pull request**
   ```bash
   # Tell Claude: "Create a PR"
   # Claude uses GitHub plugin to create PR with:
   # - Title: "Add clear chat functionality"
   # - Body: Summary, test plan, screenshots
   ```

7. **Code review**
   - Reviewer comments on PR
   - Claude sees comments via GitHub plugin
   - Makes requested changes
   - Pushes updates

**Educational value:** End-to-end professional development workflow using multiple tools together.

---

## Common Patterns Students Will Learn

### Pattern 1: Type-Driven Development
1. Define types first (interfaces, models)
2. Let LSP guide implementation
3. Compiler ensures correctness
4. Runtime errors reduced dramatically

### Pattern 2: Git Best Practices
1. Small, focused commits
2. Conventional commit messages
3. Feature branches
4. Pull request workflow with reviews

### Pattern 3: Test-Driven Development
1. Write failing test
2. Implement feature
3. Watch tests pass
4. LSP ensures no regressions

### Pattern 4: Continuous Integration
1. Every commit runs tests
2. Type checking on every file save
3. Automated PR checks
4. Deploy only if all checks pass

---

## Teaching Moments

### Moment 1: "Why did my app crash?"
**Without plugins:** "Let me add more console.logs..."
**With plugins:** "The type system caught that bug before you even ran the app!"

### Moment 2: "What files do I need to change?"
**Without plugins:** "Grep through the codebase and hope you found everything..."
**With plugins:** "LSP's 'Find References' shows you exactly every usage!"

### Moment 3: "Did I break anything?"
**Without plugins:** "Run the app and click through every feature..."
**With plugins:** "Type checker verified nothing broke + tests passed = confident!"

### Moment 4: "How do professionals work?"
**Without plugins:** "Manually do everything..."
**With plugins:** "This is how VS Code, JetBrains, and other IDEs work behind the scenes!"

---

## Assessment Ideas

### Quiz Questions:
1. What's the difference between compile-time and runtime errors?
2. How does LSP improve developer productivity?
3. Why are conventional commit messages important?
4. What is the benefit of type hints in Python?
5. How does TypeScript help prevent bugs?

### Practical Exercises:
1. **Exercise:** Intentionally break something and watch LSP catch it
2. **Exercise:** Refactor a function name across 5 files using LSP
3. **Exercise:** Create a feature branch → commit → PR using plugins
4. **Exercise:** Fix 3 type errors that LSP detects
5. **Exercise:** Set up a new language server for a different language

---

## Summary

**Key Learning Outcomes:**
- ✅ Type safety prevents bugs before runtime
- ✅ LSP powers modern IDE features
- ✅ Git best practices improve team collaboration  
- ✅ Automated tooling increases productivity
- ✅ Professional workflows scale to large teams

**Plugins Demonstrated:**
- TypeScript LSP → Frontend type safety
- Pyright LSP → Backend type safety
- Commit Commands → Git best practices
- GitHub → PR workflow automation
- (Optional) Slack → Team communication integration

**Next Steps:**
See [PLUGINS.md](PLUGINS.md) for installation instructions and [CLAUDE.md](CLAUDE.md) for full project documentation.
