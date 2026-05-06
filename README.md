# ClaudeCode Labcamp

> **Learn Claude Code by building a full-stack AI agent**

Educational workshop project demonstrating professional Claude Code workflows.

---

## 🎓 For Participants

### Quick Start (Test the Completed App)

**1. Clone and setup:**
```bash
git clone https://github.com/StormAIDE/ClaudeCodeLabCamp.git
cd ClaudeCodeLabCamp

# Backend setup (Python 3.13 required)
python3.13 -m venv claudecodeenv
source claudecodeenv/bin/activate
pip install -r requirements.txt
cp .env.example .env

# Frontend setup
cd frontend && npm install && cd ..
```

**2. Export AWS credentials:**
```bash
export AWS_ACCESS_KEY_ID=<YOUR_ACCESS_KEY>
export AWS_SECRET_ACCESS_KEY=<YOUR_SECRET_KEY>
export AWS_DEFAULT_REGION=eu-central-1

# Verify
aws sts get-caller-identity
```

**3. Run the app:**
```bash
./start.sh
```

**4. Test it:**
- Frontend: http://localhost:5173
- Backend API: http://localhost:8000/docs
- Try asking: "What are the latest AI developments?"

---

### Workshop (Build From Scratch)

**After testing the completed app above:**

**1. Create new branch:**
```bash
git checkout -b workshop/<your-name>
```

**2. Follow the workshop guide:**

👉 **[WORKSHOP.md](./WORKSHOP.md)** — Complete hands-on guide covering:
- Lab 0-1: Setup & Connect Claude Code
- Lab 2: Build app with Plan Mode
- Lab 3: Plugins & TDD
- Lab 4: Commands, Skills & Hooks
- Lab 5: Agents & MCP
- Lab 6: Add custom news digest feature

Time: ~2-3 hours | Difficulty: Intermediate

**3. What you'll learn:**
- Core Claude Code workflows
- Agent development with Strands SDK
- Full-stack FastAPI + React architecture
- Testing, plugins, hooks, agents, MCP servers
- Building production-ready AI applications

---

## Prerequisites

**Must have installed:**
- Python 3.13
- Node.js 18+
- Git
- AWS account with Bedrock access
- AWS credentials configured (`claudecodelabcampparticipants` profile)

**Claude Code will install:**
- Python packages (FastAPI, Strands SDK, pytest, etc.)
- npm dependencies (React, Vite, TypeScript, etc.)
- Virtual environment setup

---

## 📋 What You'll Build

**Tech News Aggregator** - AI-powered news discovery app with:

- 🔍 **Real-Time Search**: Natural language queries search live RSS feeds
- 📊 **Auto-Categorize**: Articles tagged by domain (AI/ML, Cloud, Security, etc.)
- 💾 **Smart Caching**: SQLite stores articles to avoid re-fetching
- 💬 **Chat Interface**: Ask questions, get instant answers
- 📰 **Source Attribution**: Right panel shows articles used in response
- 🔗 **Real URLs**: Links to actual tech news sites
- 🎨 **Modern UI**: Dark glassmorphism with vibrant gradients

---

## 🛠️ Tech Stack

**Backend:**
- FastAPI + Strands Agents SDK + Pydantic
- SQLite database
- Claude 4 via Amazon Bedrock
- Python 3.11+

**Frontend:**
- React 19 + TypeScript + Vite
- Zustand (client state) + TanStack Query (server state)
- Tailwind CSS

**Testing:**
- Pytest: 43 backend tests
- Vitest: 19 frontend tests
- Total: 62 tests

---

## 🎓 Claude Code Features You'll Learn

This workshop covers ALL major Claude Code features:

| Feature | What You'll Build | When |
|---------|------------------|------|
| **CLAUDE.md** | Project instructions for AI | Lab 0 setup |
| **Plan Mode** | Design before coding | Lab 2 |
| **Plugins** | TypeScript/Pyright LSP | Lab 3 |
| **Commands** | `/component` generator | Lab 4 |
| **Skills** | `/start-dev` workflow | Lab 4 |
| **Hooks** | Safety & auto-testing | Lab 4 |
| **Agents** | Backend, frontend, reviewer | Lab 5 |
| **MCP Servers** | Browser automation | Lab 5 |
| **Full Feature** | RSS digest + keyword search | Lab 6 |

👉 All implementations are already in this repo on `main` branch — reference them anytime during the workshop!

### Example Implementations (on `main` branch)

**Hooks:**
- Block dangerous commands (`.claude/hooks/block-dangerous.sh`)
- Protect sensitive files (`.claude/hooks/protect-files.sh`)
- Auto-run tests on save (`.claude/hooks/run-tests.sh`)
- Project context injection (`.claude/hooks/project-context.txt`)

**Agents:**
- `backend-maintainer` - FastAPI, Strands SDK, Python
- `code-reviewer` - Quality analysis before commits
- `frontend-improver` - React, UI/UX improvements
- `frontend-visual-inspector` - Screenshot-based testing

**MCP Servers:**
- `drawio` - Architecture diagrams
- `chrome-devtools` - Browser automation, screenshots

**Commands & Skills:**
- `/component <Name> <description>` - Generate React component
- `/start-dev` - Start backend + frontend servers

All these are pre-configured on `main` — you'll build your own versions in the workshop!

---

## 📂 Completed App Structure (on `main`)

```
ClaudeCodeLabCamp/
├── backend/                 ← FastAPI + Strands SDK
│   ├── main.py              ← Entry point
│   ├── config.py            ← Settings
│   ├── api/endpoints/       ← Routes
│   ├── services/            ← Agent logic
│   └── tests/               ← 43 pytest tests
│
├── frontend/                ← React + TypeScript
│   ├── src/
│   │   ├── components/      ← UI components
│   │   ├── api/             ← API client
│   │   └── test/            ← 19 Vitest tests
│   └── package.json
│
├── .claude/                 ← Claude Code config
│   ├── settings.json        ← Hooks, permissions
│   ├── hooks/               ← Shell scripts
│   ├── agents/              ← 4 custom agents
│   ├── commands/            ← /component
│   └── skills/              ← /start-dev
│
├── CLAUDE.md                ← Instructions for AI
├── WORKSHOP.md              ← Your guide to rebuild
└── README.md                ← This file
```

---

## 🧪 Testing the Completed App

**Before starting workshop, verify everything works:**

```bash
# Backend tests (43 tests)
source claudecodeenv/bin/activate
python -m pytest backend/tests/ -v

# Frontend tests (19 tests)
cd frontend
npm test

# All tests
./run-all-tests.sh
```

**Expected:** All 62 tests pass ✅

If tests fail, check AWS credentials exported and dependencies installed.

---

## 📂 Repository Structure

**For participants:**

```
main branch           ← Completed app (test this first)
  ├── backend/        ← Full FastAPI implementation
  ├── frontend/       ← Complete React app
  ├── .claude/        ← All hooks, agents, skills, commands
  ├── WORKSHOP.md     ← Your guide to rebuild from scratch
  └── README.md       ← This file

Your workshop branch  ← Create this, follow WORKSHOP.md
  ├── <start empty>   ← Build incrementally with Claude Code
  └── WORKSHOP.md     ← Follow labs 0-6
```

**Workflow:**
1. Test completed app on `main` branch
2. Create `workshop/<your-name>` branch
3. Follow [WORKSHOP.md](./WORKSHOP.md) to rebuild from scratch
4. Compare your implementation with `main` branch when stuck

---

## 🔧 Troubleshooting

**Common issues when testing the completed app:**

| Problem | Fix |
|---------|-----|
| Port in use | `lsof -ti:8000 \| xargs kill -9` (backend)<br>`lsof -ti:5173 \| xargs kill -9` (frontend) |
| AWS error | Export credentials: `export AWS_ACCESS_KEY_ID=<YOUR_KEY>`<br>Verify: `aws sts get-caller-identity` |
| `use_bedrock: false` | AWS credentials not exported to environment before starting backend |
| Module not found | `source claudecodeenv/bin/activate` |
| Hooks not working | `brew install jq` |
| Python 3.14 error | Must use Python 3.13: `python3.13 -m venv claudecodeenv` |

**During workshop:**
- Stuck? Compare your code with `main` branch
- Tests failing? Run `git diff main` to see what's different
- Ask Claude Code: "Compare my implementation with main branch for [file]"

---

## 📚 Resources

**Official Documentation:**
- **Claude Code:** [code.claude.com/docs](https://code.claude.com/docs)
- **Strands SDK:** [strandsagents.com/docs](https://strandsagents.com/docs)
- **FastAPI:** [fastapi.tiangolo.com](https://fastapi.tiangolo.com)
- **React:** [react.dev](https://react.dev)

**Community:**
- **Claude Code Discord:** [discord.gg/claude-code](https://discord.gg/claude-code)
- **GitHub Discussions:** [github.com/anthropics/claude-code/discussions](https://github.com/anthropics/claude-code/discussions)

---

## 🎯 For Instructors

**Using this repo for workshops:**

1. **Preparation:**
   - Ensure all participants have prerequisites installed
   - Test AWS credentials work (`aws sts get-caller-identity`)
   - Clone repo and verify tests pass on `main` branch

2. **Session structure:**
   - **10 min:** Overview + test completed app
   - **15 min:** Lab 0-1 (Setup, connect Claude Code)
   - **30 min:** Lab 2 (Plan Mode, build initial app)
   - **20 min:** Lab 3 (Plugins, TDD)
   - **25 min:** Lab 4 (Commands, skills, hooks)
   - **20 min:** Lab 5 (Agents, MCP)
   - **40 min:** Lab 6 (Full feature: keyword search)
   - **10 min:** Wrap-up, share results

3. **Support:**
   - Main branch = reference implementation
   - Participants create `workshop/<name>` branches
   - Stuck? `git diff main` shows differences
   - Tests failing? Check AWS credentials exported

---

## 📄 License

Educational project for ClaudeCode Labcamp workshops.

---

## 🙏 Built With

- [Claude 4](https://www.anthropic.com/claude) via Amazon Bedrock
- [Strands Agents SDK](https://strandsagents.com/)
- [FastAPI](https://fastapi.tiangolo.com/) + [React](https://react.dev/)
- [Claude Code](https://claude.ai/code)

---

**Ready to learn? Start with [WORKSHOP.md](./WORKSHOP.md)! 🚀**
