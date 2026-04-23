# Workshop: Build Your Own Tech News Digest with Claude Code

> **Branch:** `test/workshop-news-aggregator`
> **Slides:** [`Claude_Code_Workshop.pptx`](./Claude_Code_Workshop.pptx)
> **Template Marketplace:** [https://app.aitmpl.com](https://app.aitmpl.com)

In this workshop you will use **Claude Code** to build a personalised tech news aggregator — a **News Digest** around a topic of your choice (AI, Robotics, Cybersecurity, Web3, Gaming, etc.).

The digest page and the chatbot **share the same database**: the page scrapes specialist RSS feeds every 60 seconds, and the chatbot reads from that cache to answer questions like *"What has Boston Dynamics released lately?"* — instantly, because the data is already there.

You will experience every major Claude Code feature hands-on:
Plan Mode → Sub-Agents → Skills → CLAUDE.md → `/save-to-claude-md`

---

## Prerequisites

Before the workshop, make sure you have:

| Requirement | How to get it |
|-------------|--------------|
| **Claude Code** | [claude.ai/code](https://claude.ai/code) — download and install |
| **Anthropic API Key** | [console.anthropic.com](https://console.anthropic.com) — create an account, generate a key |
| **Python 3.11+** | [python.org](https://python.org) |
| **Node.js 18+** | [nodejs.org](https://nodejs.org) |
| **Git** | [git-scm.com](https://git-scm.com) |

---

## Step 0 — Get the Project Running

```bash
# 1. Clone the repo and switch to the workshop branch
git clone https://github.com/StormAIDE/ClaudeCodeLabCamp.git
cd ClaudeCodeLabCamp
git checkout test/workshop-news-aggregator

# 2. Create and activate a Python virtual environment
python -m venv claudecodeenv
source claudecodeenv/bin/activate        # Mac/Linux
# claudecodeenv\Scripts\activate         # Windows

# 3. Install backend dependencies
pip install -r backend/requirements.txt

# 4. Set up your environment file
cp .env.example .env
# Open .env and fill in your ANTHROPIC_API_KEY

# 5. Install frontend dependencies
cd frontend && npm install && cd ..

# 6. Start both servers
source claudecodeenv/bin/activate
python -m backend.main &                 # Backend on http://localhost:8000
cd frontend && npm run dev               # Frontend on http://localhost:5173
```

Open [http://localhost:5173](http://localhost:5173) — you should see the Tech News Aggregator with a chat interface and a Robotics tab.

**Verify everything works:**
```bash
python -m pytest backend/tests/ -q      # Should show: 54 passed
```

---

## Step 1 — Open the Project in Claude Code

```bash
claude .
```

Ask Claude Code to familiarise itself with the project:

```
Familiarise yourself with this project. Explain:
- What the app does
- How the AI agent works
- How a new news topic could be added
- What files I would need to touch
```

Claude will read the codebase and map the architecture for you.

---

## Step 2 — Explore the Agent Marketplace

Browse **[https://app.aitmpl.com](https://app.aitmpl.com)** together as a group.

This is a community marketplace of pre-built Claude Code components:

| Category | What you will find |
|----------|--------------------|
| **Skills** | Slash commands — session savers, security reviews, test runners |
| **Agents** | Specialised sub-agents — backend developer, code reviewer, debugger |
| **Hooks** | Event-triggered automations — run tests on save, block dangerous commands |
| **Settings** | Best-practice `.claude/settings.json` presets |

> **Skills vs Agents — what is the difference?**
>
> **Agents** work autonomously in the background — Claude spawns them to do something (write code, review, debug). You see the result, not every step.
>
> **Skills** are slash commands you invoke yourself — they guide Claude through a workflow step by step inside your session, staying fully visible.

**Workshop activity:**
1. Search for something relevant to your topic (e.g. `web scraping`, `rss`, `news`, `code review`)
2. Find a skill you want to use
3. Install it by copying the `.md` file into `.claude/commands/` and invoke it with `/skill-name`

The `/save-to-claude-md` skill is already installed in this project — you will use it at the end of every session.

---

## Step 3 — Choose Your Topic

Pick your news digest topic. This is what your new page will be about.

Some ideas: `Cybersecurity`, `Web3`, `Gaming`, `Quantum Computing`, `Green Tech`, `Space`, `DevTools`, `Fintech`, `AR/VR`, `Open Source`

For your topic, think about:
- **4 to 6 subtopics** (e.g. for Cybersecurity: Vulnerabilities, Ransomware, Privacy, Cloud Security, AppSec, Threat Intel)
- **RSS feeds** that cover those subtopics — you can ask Claude to help find good ones

---

## Step 4 — Enter Plan Mode

Enter Plan Mode — this keeps Claude in architect mode without touching any files:

```
Press: Shift + Tab + Tab
```

### Option A — Use the Robotics page as a template (recommended for beginners)

The Robotics page is a complete, working example. Claude can replicate its exact pattern for your topic. Paste this prompt, replacing YOUR TOPIC and SUBTOPICS:

```
I want to add a "[YOUR TOPIC]" news digest page to this project.
Model it exactly after the existing Robotics page:
- Sub-topic filters: [SUBTOPICS]
- RSS feeds per subtopic
- Auto-fetch from feeds when the DB is empty
- A new tab in the navigation
- 60-second refresh interval

Use robotics_tools.py, robotics.py, and RoboticsPage.tsx as
the direct pattern to follow.

Security requirements:
- Allowlist-validate all subtopic inputs
- Parameterised queries only
- No user-controlled strings in SQL

Use a code-reviewer agent to check the security of the plan
and an Explore agent to map which files need to change.
Produce a detailed step-by-step implementation plan.
```

### Option B — Design it from scratch (for participants who want more control)

```
I want to build a "[YOUR TOPIC]" news digest page from scratch.
The project already has a FastAPI backend, SQLite database,
and React 19 frontend. I want:
- Sub-topic filters: [SUBTOPICS]
- RSS feed fetching with SQLite caching
- A dedicated API endpoint
- A React page with filter chips and article cards

Don't copy any existing pattern — design the best approach.

Use a code-reviewer agent to review the security of the plan.
Produce a detailed step-by-step implementation plan.
```

Review the plan saved to `.claude/plans/`. Read it, ask questions, and edit anything you disagree with before proceeding.

---

## Step 5 — Approve and Let the Agents Work

Once you are happy with the plan:

```
The plan looks good. Start implementation — backend first (tools file,
DB migration, endpoint, route registration), then frontend
(types, API client, hook, page component, App.tsx nav toggle).
Run the full test suite after each major step and fix any failures.
```

Watch Claude spawn sub-agents in the terminal:

- **Explore agent** — maps existing patterns in the codebase
- **python-pro agent** — writes type-safe FastAPI and pytest code
- **fullstack-developer agent** — wires DB to API to frontend
- **code-reviewer agent** — checks each layer before moving on

You don't need to do anything — just watch and ask questions.

---

## Step 6 — Run Tests and Fix Failures

```bash
python -m pytest backend/tests/ -q
```

If there are failures:

```
The test suite has failures. Read the output and fix them.
```

Claude will diagnose, patch, and re-run until all tests pass.

Target: all original 54 tests still pass, plus new tests for your topic.

---

## Step 7 — Verify in the Browser

1. Restart the backend:
   ```bash
   source claudecodeenv/bin/activate && python -m backend.main
   ```
2. Open [http://localhost:5173](http://localhost:5173)
3. Click your new tab in the nav bar
4. You should see articles loading from RSS feeds
5. Click each sub-topic filter — articles should re-fetch

If a filter shows no articles:
```
The [subtopic] filter shows no articles. Trace why and fix it.
```

---

## Step 8 — Save the Session to CLAUDE.md

At the end of every session, run:

```
/save-to-claude-md
```

Claude will review the conversation and append a dated summary to `CLAUDE.md` covering decisions made, patterns established, files changed, and bugs fixed. The next session starts with full context already loaded.

```bash
tail -50 CLAUDE.md
```

---

## Step 9 — Chat With Your Digest

The chatbot and your digest page share the same SQLite database. Once your page has scraped some articles, the chatbot can answer questions directly from that cache — no extra fetching needed.

Try these in the chat:

```
What is the latest news about [your topic]?
What has [specific company] released this week?
Show me trending topics
```

**How the search works under the hood:**

The agent picks the right tool automatically:

- Broad topic (e.g. "AI news") — calls `search_news` against general RSS feeds
- Specific query (e.g. "Boston Dynamics") — calls `search_all_news`, a keyword search using `SQL LIKE '%query%'` across all cached article titles and summaries
- Robotics questions — calls `search_robotics_news` against specialist feeds (The Robot Report, IEEE Spectrum, etc.)

**Why pre-scrape instead of fetching live on every question?**

When the chatbot gets a question it could either hit the RSS feeds right now or read from what the digest page already scraped. Fetching live every time has real costs:

| | Fetch live on every question | Pre-scraped DB cache |
|--|------------------------------|----------------------|
| **Response time** | 3 to 8 seconds (network + parsing) | 1 to 2 seconds |
| **RSS feed load** | Every question hits the feed servers | Feeds polled on a schedule |
| **Duplicate work** | 10 users ask the same thing = 10 fetches | 10 users = 1 cached result |
| **Offline resilience** | Fails if the feed is down | Still answers from cache |
| **Cost** | Network + processing on every chat turn | Fetch cost paid once, shared across all queries |

The digest page acts as a background scraper that continuously warms the cache. The chatbot is just a reader — it benefits from everything the page already fetched without doing any of the work itself.

If the DB has nothing for a query, the chatbot falls back to a live fetch automatically and caches the result for next time.

Sources appear on the right side of the screen showing the actual articles used.

---

## Future Work — Making the Search Smarter with Real RAG

The current search uses SQL keyword matching (`LIKE '%query%'`). It works well for exact names and terms, but it can only find articles that contain the exact words you typed:

```
"Boston Dynamics"        — finds articles mentioning those exact words
"bipedal robot company"  — no match, even if the article is clearly about Boston Dynamics
"Atlas latest news"      — only matches if "Atlas" literally appears in title or summary
```

**What RAG (Retrieval Augmented Generation) is:**

RAG means the system understands meaning, not just keywords. Instead of matching words, it matches concepts. Here is how it works:

1. **Embed articles on save** — when an article is stored, generate a vector embedding: a list of around 1500 numbers that encode the semantic meaning of the text, using a model like `text-embedding-3-small` or Anthropic's embeddings API
2. **Store the embeddings** — save those vectors in SQLite with the `sqlite-vec` extension, or in a dedicated vector database like pgvector, Chroma, or Qdrant
3. **Embed the query** — at question time, embed the user's question using the same model
4. **Similarity search** — find the articles whose vectors are mathematically closest to the query vector (cosine similarity). Closest means most similar in meaning, not in wording
5. **Ground Claude's answer** — inject the retrieved articles into Claude's prompt as context. Claude reads them and answers based on real content

```
User asks: "bipedal robot company news"
  → embed query → [0.23, -0.87, 0.45, ...]
  → similarity search → Boston Dynamics articles score highest
  → Claude answers grounded in those articles
```

**Keyword search vs RAG:**

| | Keyword search (what we built) | Real RAG |
|--|-------------------------------|----------|
| Finds exact words | Yes | Yes |
| Finds synonyms | No | Yes |
| Finds by meaning and concept | No | Yes |
| Setup complexity | None — plain SQL | Embedding model + vector store |
| Extra cost | Free | Small cost per article embedded |
| Best for | Company names, direct keywords | Open-ended natural language questions |

For this workshop, keyword search is the right tradeoff — zero extra infrastructure, works immediately, and handles the most common use cases well. RAG is the natural next step if you want to turn this into a production product.

To extend this project with RAG, tell Claude Code:

```
Add semantic search to the news chatbot using Anthropic's embeddings API.
When articles are saved to the DB, generate embeddings and store them in a
sqlite-vec table. Replace the LIKE search in search_all_news with a vector
similarity search. Keep the LIKE search as a fallback if no embeddings exist.
```

---

## What You Have Used

| Feature | Where you used it |
|---------|------------------|
| **Plan Mode** | Step 4 — architecture before code |
| **Sub-Agents** | Step 5 — Explore, python-pro, code-reviewer, fullstack |
| **Skills** | Step 2 — install from aitmpl.com; Step 8 — `/save-to-claude-md` |
| **CLAUDE.md** | Step 8 — persistent session memory |
| **Agentic loop** | Step 5 — Claude auto-dispatches tools and iterates |
| **Shared DB cache** | Step 9 — pages scrape, chatbot reads from the same cache |

---

## Project Structure

```
ClaudeCodeLabCamp/
├── backend/
│   ├── services/agent_service.py     <- AI agent (Bedrock or Anthropic)
│   │                                    reads from shared DB via ALL_TOOL_SCHEMAS
│   ├── tools/news_tools.py           <- General RSS + search_all_news (keyword DB search)
│   ├── tools/robotics_tools.py       <- Robotics feeds (optional template)
│   ├── api/endpoints/robotics.py     <- GET /robotics (optional template)
│   └── database/db.py                <- Shared SQLite — pages write, chatbot reads
├── frontend/src/
│   ├── pages/RoboticsPage.tsx        <- Robotics page (optional template)
│   ├── hooks/useRoboticsNews.ts      <- TanStack Query hook (optional template)
│   ├── api/robotics.ts               <- Axios client (optional template)
│   └── App.tsx                       <- View toggle nav
├── .claude/
│   └── commands/
│       └── save-to-claude-md.md      <- /save-to-claude-md skill
├── .env.example                      <- Copy to .env, add your API key
├── Claude_Code_Workshop.pptx         <- Workshop slides
└── CLAUDE.md                         <- Claude's persistent memory
```

The Robotics implementation is an optional reference. Use it as a template (Option A) or ignore it and design from scratch (Option B).

---

## AI Provider Setup

**Option A — Anthropic API Key (default, no AWS needed):**
```env
ANTHROPIC_API_KEY=sk-ant-...
CLAUDE_MODEL_ID=claude-sonnet-4-6
```

**Option B — AWS Bedrock (if you have AWS credentials):**
```env
AWS_ACCESS_KEY_ID=AKIA...
AWS_SECRET_ACCESS_KEY=...
AWS_DEFAULT_REGION=eu-west-1
CLAUDE_MODEL_ID=eu.anthropic.claude-sonnet-4-5-20250929-v1:0
```

The backend auto-detects which to use. Bedrock takes priority when both AWS keys are set.

---

## Useful Links

| Resource | URL |
|----------|-----|
| Claude Code docs | [docs.anthropic.com/claude-code](https://docs.anthropic.com/claude-code) |
| Agent and skill marketplace | [app.aitmpl.com](https://app.aitmpl.com) |
| Anthropic console | [console.anthropic.com](https://console.anthropic.com) |
| API docs (local) | [localhost:8000/docs](http://localhost:8000/docs) |

---

## Troubleshooting

| Problem | Fix |
|---------|-----|
| `ANTHROPIC_API_KEY` not picked up | Check `.env` exists in project root and restart the backend |
| Port already in use | `lsof -ti:8000 \| xargs kill -9` (backend) or `:5173` (frontend) |
| Module not found | `source claudecodeenv/bin/activate` |
| No articles on new tab | Tell Claude: "the [topic] page shows no articles, trace and fix" |
| Tests failing | Tell Claude: "read the test output and fix all failures" |
| Starlette version conflict | `pip install "starlette>=0.37.2,<0.42.0"` |

---

*Workshop materials by Ana-Maria Lacatusu · Built with Claude Code · Powered by Anthropic*
