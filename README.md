# Tech News Aggregator

> **Full-stack AI agent built with Claude Code**

AI-powered tech news aggregation system demonstrating professional Claude Code workflows.

---

## 🚀 Quick Start

### Prerequisites
- Python 3.11 
- Node.js 18+
- AWS account with Bedrock access
- AWS credentials configured (`claudecodelabcampparticipants` profile)

### Installation

```bash
# Clone and setup
git clone https://github.com/StormAIDE/ClaudeCodeLabCamp.git
cd ClaudeCodeLabCamp
git checkout test/workshop-news-aggregator

# Backend setup (Python 3.13 required)
python3.13 -m venv claudecodeenv
source claudecodeenv/bin/activate
pip install -r requirements.txt
cp .env.example .env

# Frontend setup
cd frontend && npm install && cd ..
```

### AWS Credentials Setup

**IMPORTANT:** Export AWS credentials to environment **before** starting backend:

```bash
# Export credentials from your AWS profile
export AWS_ACCESS_KEY_ID=$(aws configure get aws_access_key_id --profile claudecodelabcampparticipants)
export AWS_SECRET_ACCESS_KEY=$(aws configure get aws_secret_access_key --profile claudecodelabcampparticipants)
export AWS_SESSION_TOKEN=$(aws configure get aws_session_token --profile claudecodelabcampparticipants)
export AWS_DEFAULT_REGION=eu-central-1

# Verify credentials
aws sts get-caller-identity
```

### Run the App

**Option A: Manual (2 terminals)**

Terminal 1 - Backend:
```bash
# Export AWS credentials first (see above)
source claudecodeenv/bin/activate
python -m backend.main
```

Terminal 2 - Frontend:
```bash
cd frontend
npm run dev
```

**Option B: Quick Start Script**
```bash
# Export AWS credentials first (see above)
./start.sh
```

### Access Points
- **Frontend:** http://localhost:5173
- **Backend API:** http://localhost:8000
- **API Docs:** http://localhost:8000/docs

### Usage
1. Open http://localhost:5173
2. Ask: "What are the latest AI developments?"
3. Agent searches RSS feeds (TechCrunch, The Verge, Hacker News, AWS)
4. Sources appear on right side
5. Click URLs to visit articles

---

## 📋 What This App Does

**Tech News Aggregator** - AI-powered news discovery:

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

## 🎓 Claude Code Features

This project demonstrates ALL major Claude Code features:

| Feature | Implementation | Location |
|---------|---------------|----------|
| **CLAUDE.md** | Project instructions for AI | `/CLAUDE.md` |
| **Hooks** | Automated workflows & safety | `.claude/hooks/` + `.claude/settings.json` |
| **Plugins** | LSP, GitHub integration | Install via `/plugin` command |
| **Commands** | `/component` generator | `.claude/commands/` |
| **Skills** | `/start-dev` workflow | `.claude/skills/` |
| **Agents** | Backend, frontend, reviewer | `.claude/agents/` |
| **MCP Servers** | Browser tools, diagrams | `.mcp.json` |
| **settings.json** | Central config | `.claude/settings.json` |

### Active Hooks

**1. Block Dangerous Commands** (PreToolUse)
- Prevents: `rm -rf /`, `dd`, fork bombs, pipe-to-shell
- Script: `.claude/hooks/block-dangerous.sh`

**2. Protect Sensitive Files** (PreToolUse)
- Protects: `.env`, lock files, `.git/`, `venv/`
- Script: `.claude/hooks/protect-files.sh`

**3. Auto-Run Tests** (PostToolUse)
- Runs pytest after `.py` edits
- Runs Vitest after `.ts`/`.tsx` edits
- Script: `.claude/hooks/run-tests.sh`

**4. Project Context Injection** (SessionStart)
- Loads project rules on startup
- File: `.claude/hooks/project-context.txt`

**Prerequisite:** All hooks require `jq`:
```bash
brew install jq
```

### Custom Agents

**1. backend-maintainer** - FastAPI, Strands SDK, Python  
**2. code-reviewer** - Quality analysis before commits  
**3. frontend-improver** - React, UI/UX improvements  
**4. frontend-visual-inspector** - Screenshot-based testing

### MCP Servers

**1. drawio** - Architecture diagrams  
**2. chrome-devtools** - Browser automation, screenshots

View MCP config: `.mcp.json`

### Custom Commands & Skills

**Command:** `/component <Name> <description>` - Generate React component  
**Skill:** `/start-dev` - Start backend + frontend servers

---

## 📂 Project Structure

```
ClaudeCodeLabCamp/
├── backend/
│   ├── main.py              # FastAPI entry point
│   ├── config.py            # Pydantic Settings
│   ├── api/
│   │   └── endpoints/       # API routes
│   ├── services/
│   │   └── agent_service.py # Strands SDK agent
│   └── tests/               # 43 pytest tests
│
├── frontend/
│   ├── src/
│   │   ├── components/      # React components
│   │   ├── api/             # Axios client
│   │   ├── store/           # Zustand store
│   │   └── test/            # 19 Vitest tests
│   └── package.json
│
├── .claude/
│   ├── settings.json        # Hooks, permissions
│   ├── hooks/               # Shell scripts
│   ├── agents/              # 4 custom agents
│   ├── commands/            # /component
│   └── skills/              # /start-dev
│
├── .mcp.json                # MCP server config
├── CLAUDE.md                # Project docs for AI
├── WORKSHOP.md              # Workshop guide
└── requirements.txt
```

---

## 🧪 Testing

```bash
# Backend tests
source claudecodeenv/bin/activate
python -m pytest backend/tests/ -v

# Frontend tests
cd frontend
npm test

# All tests
./run-all-tests.sh
```

**Expected:** All 62 tests pass ✅

---

## 🎯 Workshop Guide

**Want to learn by building this project from scratch?**

See [WORKSHOP.md](./WORKSHOP.md) for complete hands-on guide covering:
- Lab 0-1: Setup & Connect Claude Code
- Lab 2: Build app with Plan Mode
- Lab 3: Plugins & TDD
- Lab 4: Commands, Skills & Hooks
- Lab 5: Agents & MCP
- Lab 6: Add custom news digest feature

Time: ~2-3 hours | Difficulty: Intermediate

---

## 🔧 Troubleshooting

| Problem | Fix |
|---------|-----|
| Port in use | `lsof -ti:8000 \| xargs kill -9` (backend)<br>`lsof -ti:5173 \| xargs kill -9` (frontend) |
| AWS error | Export credentials: `export AWS_ACCESS_KEY_ID=$(aws configure get aws_access_key_id)`<br>Verify: `aws sts get-caller-identity` |
| `use_bedrock: false` | AWS credentials not exported to environment before starting backend |
| Module not found | `source claudecodeenv/bin/activate` |
| Hooks not working | `brew install jq` |
| Python 3.14 pydantic error | Use Python 3.13: `python3.13 -m venv claudecodeenv` |

---

## 📚 Documentation

- **Claude Code:** [code.claude.com/docs](https://code.claude.com/docs)
- **Strands SDK:** [strandsagents.com/docs](https://strandsagents.com/docs)
- **FastAPI:** [fastapi.tiangolo.com](https://fastapi.tiangolo.com)
- **React:** [react.dev](https://react.dev)

---

## 🤝 Contributing

1. Fork repo
2. Create feature branch (`git checkout -b feature/name`)
3. Commit changes (`git commit -m 'feat: add feature'`)
4. Push branch (`git push origin feature/name`)
5. Open Pull Request

**Commit format:** Conventional commits (feat:, fix:, chore:, docs:, test:)

---

## 📄 License

Educational project for ClaudeCode Labcamp.

---

## 🙏 Acknowledgments

Built with:
- [Claude 4](https://www.anthropic.com/claude) via Amazon Bedrock
- [Strands Agents SDK](https://strandsagents.com/)
- [Tailwind CSS](https://tailwindcss.com/)
- [Claude Code](https://claude.ai/code)

---

**Happy coding! 🚀**

*Built to demonstrate Claude Code's automation, safety, and verification features.*
