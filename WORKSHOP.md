# Tech News Aggregator Workshop Guide

**Welcome to the hands-on ClaudeCode workshop!** 

In this lab, you'll build your own Tech News Aggregator from scratch, learning professional development workflows with Claude Code. By the end, you'll have a working full-stack application that aggregates and analyzes tech news using AI.

**Workshop Philosophy: "Add Feature → Test Feature → See The Improvement"**

After adding each Claude Code service (plugins, commands, hooks, skills, agents, MCP), you'll immediately test it and see how it improves your development workflow!

---

## What You'll Build

**Project:** A Tech News Aggregator that:
- Searches for recent tech news articles (AI, Cloud, DevOps, Web Dev, etc.)
- Categorizes articles by technology domain  
- Summarizes article content
- Shows trending tech topics
- Stores article history in SQLite database
- Provides a chat interface + visual news feed

**Tech Stack:**
- Backend: Python + FastAPI + Strands SDK
- Frontend: React + TypeScript + Vite
- Database: SQLite for article storage
- AI: Claude via Amazon Bedrock

---

## Prerequisites

**Must be installed BEFORE workshop:**

These cannot be installed by Claude Code - you need them first:

- [ ] **Python 3.11+** (you should already have this)
- [ ] **Node.js 18+** (download from [nodejs.org](https://nodejs.org))
- [ ] **Git** (download from [git-scm.com](https://git-scm.com))
- [ ] **VS Code or terminal** (any terminal works)
- [ ] **AWS account with Bedrock access**
- [ ] **AWS credentials** (Access Key ID, Secret Key, Session Token)

**Check your setup:**
```bash
python --version    # Must show 3.11+
node --version      # Must show 18+
git --version       # Any recent version
```

**Claude Code will install for you:**
- ✅ Python packages (FastAPI, Strands SDK, pytest, etc.)
- ✅ npm dependencies (React, Vite, TypeScript, etc.)
- ✅ GitHub CLI (optional, for PR workflows)
- ✅ Virtual environment setup

---

## Getting Started: Setup Before Workshop

### Step 1: Install Claude Code CLI

#### Option 1: Install in VS Code Terminal (Mac - Recommended)

```bash
# Install Claude Code CLI
curl -fsSL https://claude.ai/install.sh | bash
```

**Verify installation:**
```bash
claude --version
# Should display: Claude Code v[version number]
```

**If command not found:**
- Close and reopen terminal (shell needs to reload PATH)
- Or run: `source ~/.zshrc` (Mac/Linux) or `source ~/.bashrc` (Linux)

#### Option 2: Install for Other Operating Systems

**Follow the official installation guide:**

👉 **[https://code.claude.com/docs/en/quickstart](https://code.claude.com/docs/en/quickstart)**

This guide covers Windows, Linux, macOS, Desktop App, and VS Code Extension.

---

### Step 2: Configure AWS Profile (BEFORE Starting Claude Code)

**Create AWS profile with credentials provided by instructor:**

```bash
# Create named profile
aws configure --profile claudecodeprofile
```

**When prompted, enter these values:**

```
AWS Access Key ID [None]: [paste your access key]
AWS Secret Access Key [None]: [paste your secret key]
Default region name [None]: eu-central-1
Default output format [None]: json
```

**Set session token (if not asked in previous step):**

```bash
aws configure set aws_session_token [your-session-token] --profile claudecodeprofile
```

**Verify profile configured correctly:**

```bash
aws sts get-caller-identity --profile claudecodeprofile
# Should return your AWS account details
```

**Export profile to environment (important!):**

```bash
export AWS_PROFILE=claudecodeprofile
```

**Note:** You'll connect Claude Code to your project in Lab 1 after creating the project folder.

---

## Lab 0: Initial Setup

**Prerequisites completed:**
- ✅ Claude Code CLI installed and verified
- ✅ AWS profile configured (`claudecodeprofile`)

**Now let's prepare the project environment:**

### Step 0.1: Create Project Folder and Setup Version Control

**Do this BEFORE starting Claude Code:**

```bash
# 1. Create your project folder
mkdir tech-news-aggregator
cd tech-news-aggregator

# 2. Create README.md (so you have something to commit)
echo "# Tech News Aggregator" > README.md
echo "AI-powered tech news aggregation system built with Claude Code" >> README.md

# 3. Initialize git repository
git init
git add README.md
git commit -m "Initial commit"
```

**Why do this first?** You need an existing folder with git initialized so Claude Code can work with it.

### Step 0.2: Create Python Virtual Environment

```bash
# Create Python virtual environment
python -m venv venv

# Activate it (you'll need this activated later)
# On Mac/Linux:
source venv/bin/activate
# On Windows:
# venv\Scripts\activate
```

**Why?** Python dependencies will be isolated to this project.

### Step 0.3: Create GitHub Repository and Push

**Create the remote repository:**

1. Go to GitHub.com and create a new repository (e.g., "tech-news-aggregator")
2. Don't initialize with README (you already have one)
3. Copy the HTTPS URL (e.g., `https://github.com/yourusername/tech-news-aggregator.git`)

**Connect and push:**

```bash
# Add remote repository
git remote add origin https://github.com/yourusername/tech-news-aggregator.git

# Push to GitHub
git branch -M main
git push -u origin main
```

Success! Your repository is now on GitHub.

**Checklist before proceeding to Lab 1:**
- [ ] Claude Code CLI installed and verified (`claude --version`)
- [ ] AWS profile configured (`claudecodeprofile`) with `export AWS_PROFILE=claudecodeprofile`
- [ ] Project folder created (`tech-news-aggregator/`)
- [ ] Git initialized and pushed to GitHub
- [ ] Python virtual environment created (`venv/`)

---

## Lab 1: Connect Claude Code to Your Project

### Step 1.1: Start Claude Code in Project Directory

**Navigate to your project and start Claude:**

```bash
# Make sure AWS profile is exported
export AWS_PROFILE=claudecodeprofile

# Navigate to project
cd tech-news-aggregator

# Start Claude Code (first time)
claude
```

**When you run `claude` for the first time, you'll see this setup prompt:**

1. **Select authentication method**: Choose **AWS Bedrock SSO**
2. **Enter AWS SSO profile name**: Type `claudecodeprofile`
3. **Enter AWS region**: Type `eu-central-1`
4. **Follow remaining prompts** to complete setup
5. **Press Enter** to restart Claude
6. **Type `claude` again** - Connection established

**What you'll see after setup:**
```
Claude Code v[version]
Connected to: tech-news-aggregator/
Ready to assist!
```

**Success!** Claude Code is now connected to your project and can read/write files, run commands, and assist with development.

### Step 1.2: Test Basic Commands

**Try these commands:**

```bash
# Check current directory
/pwd

# List files
/ls

# Check git status  
/git status
```

Claude Code should respond with directory info and git status!

### Step 1.3: Connect GitHub CLI (Optional but Recommended)

**Install GitHub CLI if not installed:**

```bash
# Mac
brew install gh

# Windows (via Chocolatey)
choco install gh

# Linux
# See: https://github.com/cli/cli#installation
```

**Authenticate:**

```bash
gh auth login
# Follow prompts to authenticate via browser
```

**Test:**
```bash
gh repo view
# Should show your repository info
```

**What This Enables:**
- Create PRs from Claude Code
- Manage issues directly
- View PR reviews and checks

---

## Lab 2: Build App + Tests with Plan Mode

### Step 2.1: Use Plan Mode to Design the App

**Enter Plan Mode:**
```
Press Shift+Tab before hitting Enter on your prompt
```

**Ask Claude Code:**
```
Create a full-stack Tech News Aggregator application with:

Backend (Python + FastAPI + Strands SDK):
- Agent with 4 tools:
  - search_news(topic: str, days: int = 7) - Find recent tech articles
  - categorize_article(text: str) - Auto-categorize by tech domain
  - summarize_article(url: str) - Generate article summaries
  - get_trending_topics() - Show trending tech topics
- SQLite database for article storage (articles table with id, title, url, summary, topic, published_date, fetched_at)
- API endpoints:
  - POST /api/v1/agent/chat - Chat with agent
  - GET /api/v1/news?topic=AI&days=7 - Get news articles
  - GET /api/v1/trending - Get trending topics
- Configuration: APP_NAME = "Tech News Aggregator", DATABASE_PATH = "./data/articles.db"

Frontend (React + TypeScript + Vite):
- ChatInterface component for agent interaction
- NewsFeed component - Display article cards with loading states
- ArticleCard component - Shows title, summary, topic badge, dates, clickable URL
- TopicFilter component - Filter buttons (All, AI/ML, Cloud/DevOps, Web Development, Mobile, Security, Data Science)
- Two-column responsive layout: Chat interface (left) + News feed (right)
- App title: "Tech News Aggregator"
- Subtitle: "Stay updated with the latest tech news - AI, Cloud, DevOps, and more"

Include full test coverage:

Backend tests (backend/tests/):
- test_news_tools.py:
  - test_search_news_returns_articles() - Verify 3 articles returned
  - test_search_news_filters_by_days() - Verify days parameter works
  - test_categorize_article_ai_ml() - Test AI/ML categorization
  - test_categorize_article_cloud_devops() - Test Cloud/DevOps categorization
  - test_summarize_article_returns_summary() - Verify summary generation
  - test_get_trending_topics_returns_list() - Verify 5 topics returned
- test_news_endpoints.py:
  - test_get_news_endpoint() - Test GET /api/v1/news
  - test_get_news_with_topic_filter() - Test ?topic=AI parameter
  - test_get_trending_endpoint() - Test GET /api/v1/trending
  - test_post_chat_endpoint() - Test POST /api/v1/agent/chat
- test_database.py:
  - test_database_initialization() - Verify articles table created
  - test_add_article() - Test article insertion
  - test_get_articles_by_topic() - Test topic filtering
  - test_get_trending_topics() - Test trending aggregation

Frontend tests (frontend/src/components/__tests__/):
- NewsFeed.test.tsx - renders topic filter buttons, calls API when topic changes, displays loading state, shows "no articles" message when empty, renders article cards when data available
- ArticleCard.test.tsx - renders article title as clickable link, displays summary text, shows topic badge, formats dates correctly
- TopicFilter.test.tsx - renders all topic buttons, highlights selected topic, calls onChange when clicked

Use mock data for articles initially (real API integration can be added later).
Follow FastAPI + React + Strands SDK architecture patterns.
Backend port: 8000, Frontend port: 5173
```

**Review the plan**, approve it, and let Claude generate the project structure with tests.

### Step 2.2: Start the App

**Ask Claude Code:**
```
Start the app
```

Claude will:
1. Activate virtual environment
2. Install dependencies (FastAPI, Strands SDK, React, etc.)
3. Start FastAPI backend on port 8000
4. Start Vite frontend on port 5173

### Step 2.3: Test the Tech News Agent

**Open:** http://localhost:5173

**You should see:**
- Header: "Tech News Aggregator"
- Two-column layout: Chat (left) + News Feed (right)
- Topic filter buttons: All, AI/ML, Cloud/DevOps, etc.
- Empty news feed (database is empty)

**Test queries in the chat:**

**Query 1:**
```
What's the latest AI news this week?
```

**Expected:** Agent calls `search_news("AI", 7)` and returns 3 mock articles with titles, dates, summaries, URLs

**Query 2:**
```
What are the trending tech topics?
```

**Expected:** Agent calls `get_trending_topics()` and returns list like:
- AI - 156 articles
- Cloud Computing - 89 articles  
- Web3 - 67 articles
- Cybersecurity - 54 articles
- DevOps - 43 articles

**Query 3:**
```
Categorize this: "New Kubernetes update improves container orchestration"
```

**Expected:** Agent calls `categorize_article()` and returns "Category: Cloud/DevOps"

### Step 2.4: Run Tests

**Backend tests:**
```bash
source venv/bin/activate
python -m pytest backend/tests/ -v
```

**Frontend tests:**
```bash
cd frontend
npm test
```

**Expected:** All tests pass

**What You Just Built:**
- Full-stack app with tests in minutes!
- Agent with 4 custom tools
- React frontend with TypeScript
- FastAPI backend with Strands SDK
- SQLite database ready for articles
- Complete test coverage (backend + frontend)

---

## Lab 3: Plugins & TDD

### Step 3.1: Install TypeScript LSP Plugin

**In Claude Code:**
```
/plugin marketplace add claude-plugins-official
/plugin install typescript-lsp@claude-plugins-official
/reload-plugins
```

**Test it:**

**Ask Claude Code:**
```
In frontend/src/components/NewsFeed.tsx, intentionally add a type error:

const articles: Article[] = "not an array";  // Should error!

Check if LSP catches this.
```

**Expected:** TypeScript LSP shows error: `Type 'string' is not assignable to type 'Article[]'`

### Step 3.2: Install Pyright LSP Plugin

**In Claude Code:**
```
/plugin install pyright-lsp@claude-plugins-official
/reload-plugins
```

**Test it:**

**Ask Claude Code:**
```
In backend/services/agent_service.py, add a type error:

def chat(self, message: str) -> int:  # Says int but returns str!
    return "this is wrong"

Check if Pyright catches this.
```

**Expected:** Pyright LSP shows error: `Expression of type 'str' cannot be assigned to return type 'int'`

**What This Teaches:**
- LSP for real-time type checking
- Plugin marketplace usage
- Developer productivity tools

### Step 3.3: Add a Simple Feature with TDD

**Feature to add:** Topic filter in news feed

**Ask Claude Code:**
```
Add topic filtering using TDD:

1. Write these failing tests:
   Frontend test (TopicFilter.test.tsx):
   - test_filter_by_ai() - Click "AI/ML" and verify only AI articles shown
   - test_filter_shows_count() - Each filter button shows article count
   
   Backend test (test_news_endpoints.py):
   - test_get_news_filters_correctly() - API filters by topic parameter

2. Run tests - they should fail

3. Implement the feature:
   - Update TopicFilter component to emit topic changes
   - Update NewsFeed to filter by selected topic
   - Update backend endpoint to filter database queries

4. Run tests again - they should pass
```

**Test your new feature:**

**In the app:**
1. Get some articles: "Show me AI news"
2. Click "Cloud/DevOps" filter
3. See articles filtered correctly

**What This Teaches:**
- TDD workflow: Tests first, then implementation
- LSP catches errors before running tests
- Simple feature addition with test coverage

---

## Lab 4: Commands, Skills & Hooks

### Step 4.1: Create the /component Command

**Ask Claude Code:**
```
Create a custom slash command called /component following the official Claude Code documentation at https://code.claude.com/docs/en/agent-sdk/slash-commands

The command should:
1. Accept arguments: /component <ComponentName> <description>
2. Generate a fully-typed React + TypeScript component with:
   - Proper TypeScript interfaces
   - Tailwind CSS styling
   - Clean, readable code
   - Best practices (exported component, proper types)
3. Save it to frontend/src/components/<ComponentName>.tsx
4. Follow the project's existing component structure

Example usage: /component LoadingSpinner Shows a loading indicator while content is loading

Use the official docs format for the command file in .claude/commands/
```

**Claude will create** `.claude/commands/component.md` with proper frontmatter and prompt template.

**Test It - Generate Your First Component:**

```
/component LoadingSpinner Shows a loading indicator while content is loading
```

**Expected:**
- File created: `frontend/src/components/LoadingSpinner.tsx`
- Component has TypeScript interface
- Tailwind CSS for styling
- Fully functional!

**Use it:**

**Ask Claude:** "Use the LoadingSpinner component in NewsFeed while fetching articles"

**What This Teaches:**
- Custom command creation using official SDK
- Reusable code generation templates
- Component scaffolding automation
- Time saved: 10 minutes → 30 seconds per component

### Step 4.2: Create the /start-dev Skill

**Skills are multi-step automated workflows. Let's create one to start both servers!**

**Ask Claude Code:**
```
Create a custom skill called /start-dev that automates starting the development environment.

Reference the official documentation: https://code.claude.com/docs/en/agent-sdk/skills

The skill should:
1. Check if Python virtual environment exists (venv/)
2. Activate the virtual environment
3. Start FastAPI backend in background on port 8000
4. Navigate to frontend directory
5. Start Vite dev server on port 5173
6. Report server status with colored output
7. Show URLs to visit (backend and frontend)
8. Handle errors gracefully (missing dependencies, ports in use)

Create the skill in .claude/skills/start-dev/ with proper SKILL.md structure.
```

**Test It:**
```
/start-dev
```

**Expected:**
```
Virtual environment activated
Starting backend on port 8000...
Backend running at http://localhost:8000
Starting frontend on port 5173...
Frontend running at http://localhost:5173
Both servers are ready!
```

**What This Teaches:**
- Multi-step skill creation
- Background process management
- Error handling in skills
- Time saved: Manual steps → One command

### Step 4.3: Add PreToolUse Hook - Block Dangerous Commands

**Ask Claude Code:**
```
Create a PreToolUse hook that blocks dangerous commands before execution.

Reference: https://code.claude.com/docs/en/hooks/examples

Add to .claude/settings.json:
{
  "hooks": {
    "PreToolUse:Bash": {
      "command": ".claude/hooks/block-dangerous.sh"
    }
  }
}

The hook script (.claude/hooks/block-dangerous.sh) should:
1. Check if command contains: rm -rf, dd, mkfs, :(){ :|:& };:
2. If dangerous, return non-zero exit code with error message
3. If safe, return 0 (allow execution)

Test: Try "rm -rf /" - should be blocked!
```

**Test It:**

**Ask Claude:** "Delete all files with rm -rf /"

**Expected:** Hook blocks it with error: "BLOCKED: Dangerous command detected"

### Step 4.4: Add PreToolUse Hook - Protect Database and Config Files

**Ask Claude Code:**
```
Add a hook that protects sensitive files from being edited or deleted.

Reference the official docs: https://code.claude.com/docs/en/hooks/reference

Create .claude/hooks/protect-files.sh that:
1. Blocks edits to: data/articles.db, .env, venv/, .git/
2. Returns error message explaining why
3. Suggests safe alternatives (use API for database, use .env.example for config)

Add to .claude/settings.json:
{
  "hooks": {
    "PreToolUse:Edit": {
      "command": ".claude/hooks/protect-files.sh"
    },
    "PreToolUse:Write": {
      "command": ".claude/hooks/protect-files.sh"
    }
  }
}
```

**Test:** Try editing `.env` - should be blocked!

**What This Teaches:**
- PreToolUse hooks prevent mistakes
- File protection for sensitive data
- Automation without manual checks

---

## Lab 5: Agents & MCP

### Step 5.1: Understand MCP

**Read the docs:**
```
https://code.claude.com/docs/en/mcp
```

**Key concepts:**
- **MCP (Model Context Protocol)** connects external tools to Claude
- **MCP Servers** expose tools via standard protocol
- **Examples**: Chrome DevTools, Draw.io, Database clients

### Step 5.2: Install Chrome DevTools MCP

**Check if .mcp.json exists:**
```bash
cat .mcp.json
```

**If not, create it:**

**Ask Claude Code:**
```
Create .mcp.json file to configure Chrome DevTools MCP server:

{
  "mcpServers": {
    "chrome-devtools": {
      "command": "npx",
      "args": [
        "-y",
        "@executeautomation/chrome-devtools-mcp-server"
      ]
    }
  }
}
```

**Reload Claude Code:**
```bash
# Exit and restart claudecode
# Or use /reload-plugins if available
```

**Verify MCP tools loaded:**

**Ask Claude:** "What MCP tools do you have access to?"

**Expected:** Should list chrome-devtools tools (navigate_page, take_screenshot, etc.)

### Step 5.3: Create Visual News Feed Inspector Agent

**Ask Claude Code:**
```
Create an agent that uses Chrome DevTools MCP to test the news feed visually.

Create .claude/agents/visual-inspector.md:

---
name: visual-inspector
description: Tests news feed UI using Chrome DevTools (screenshots, console, interaction)
model: sonnet
---

# System Prompt
You are a frontend QA engineer testing the Tech News Aggregator UI. Use Chrome DevTools MCP tools to:

1. **Navigate to app**: http://localhost:5173
2. **Take screenshots** at key states (initial load, topic filtered, articles loaded)
3. **Check console** for errors or warnings
4. **Test interactions**:
   - Click topic filter buttons
   - Verify articles render
   - Check responsive layout
5. **Report issues**: Visual bugs, console errors, broken functionality

# Available MCP Tools
- new_page(url) - Open browser to URL
- take_screenshot(filePath) - Capture screenshot
- click(selector) - Click element
- get_console_messages() - Check console logs
- wait_for(text) - Wait for text to appear

# Workflow
1. Open http://localhost:5173
2. Screenshot: "initial-load.png"
3. Click "AI/ML" filter
4. Screenshot: "ai-filtered.png"
5. Check console for errors
6. Report findings
```

**Test it:**

**Ask Claude:** "Use visual-inspector agent to test the news feed and take screenshots"

**Expected:**
- Browser opens automatically
- Screenshots saved to project directory
- Console errors reported
- Visual analysis provided

### Step 5.4: Test Article Card Rendering

**Ask Claude:** 
```
Use visual-inspector to verify:
1. Article cards render with all fields (title, summary, topic, date)
2. Topic badges have correct colors
3. Links are clickable
4. Layout is responsive
Take screenshots of any issues found.
```

**What This Teaches:**
- MCP server configuration
- Browser automation with Chrome DevTools
- Visual testing with screenshots
- Agent delegation for specialized tasks
- External tool integration

---

## Lab 6: Documentation

### Step 6.1: Update CLAUDE.md

**CLAUDE.md provides project-specific instructions to Claude Code.**

**Ask Claude Code:**
```
Update CLAUDE.md to document the Tech News Aggregator:

## Project Overview
This is a Tech News Aggregator built with FastAPI, React, and Claude AI. It searches, categorizes, and analyzes tech news articles.

## Architecture
- Backend: Python + FastAPI + Strands SDK (port 8000)
- Frontend: React + TypeScript + Vite (port 5173)
- Database: SQLite at data/articles.db
- AI: Claude via Amazon Bedrock

## Agent Tools
1. search_news(topic, days=7) - Returns mock articles for a topic
2. categorize_article(text) - Returns category (AI/ML, Cloud/DevOps, etc.)
3. summarize_article(url) - Returns article summary
4. get_trending_topics() - Returns top 5 trending topics

## API Endpoints
- POST /api/v1/agent/chat - Chat with agent
- GET /api/v1/news?topic=AI&days=7 - Get news articles
- GET /api/v1/trending - Get trending topics

## Database Schema
```sql
CREATE TABLE articles (
  id INTEGER PRIMARY KEY,
  title TEXT NOT NULL,
  url TEXT NOT NULL,
  summary TEXT,
  topic TEXT,
  published_date TEXT,
  fetched_at TEXT DEFAULT CURRENT_TIMESTAMP
)
```

## Development Commands
- Start app: /start-dev
- Generate component: /component <name> <description>

## Important Files
- backend/tools/news_tools.py - Agent tool implementations
- backend/database/db.py - SQLite wrapper
- frontend/src/components/NewsFeed.tsx - Main news feed UI
- .claude/agents/visual-inspector.md - UI testing agent

## Rules
- Database should only be modified via API (protected by PreToolUse hook)
- All tests must pass before committing
- Use TypeScript strict mode in frontend
- Agent tools should return formatted markdown
```

### Step 6.2: Review Configuration Files

**Check your hooks configuration:**

```bash
cat .claude/settings.json
```

**Should contain:**
```json
{
  "hooks": {
    "PreToolUse:Bash": {
      "command": ".claude/hooks/block-dangerous.sh"
    },
    "PreToolUse:Edit": {
      "command": ".claude/hooks/protect-files.sh"
    },
    "PreToolUse:Write": {
      "command": ".claude/hooks/protect-files.sh"
    }
  }
}
```

**Check MCP servers:**

```bash
cat .mcp.json
```

**Should contain:**
```json
{
  "mcpServers": {
    "chrome-devtools": {
      "command": "npx",
      "args": ["-y", "@executeautomation/chrome-devtools-mcp-server"]
    }
  }
}
```

**What This Teaches:**
- Project documentation for AI collaboration
- Hook configuration management
- MCP server setup
- Best practices for team projects

---

## Final Verification Checklist

**Before you're done, verify everything works:**

### Backend Checklist
- [ ] All 4 news tools working (`search_news`, `categorize_article`, `summarize_article`, `get_trending_topics`)
- [ ] Database initializes at `data/articles.db`
- [ ] `/api/v1/news` endpoint returns articles
- [ ] `/api/v1/trending` endpoint returns topics
- [ ] `/api/v1/agent/chat` endpoint works
- [ ] Agent responds to news queries
- [ ] Backend tests pass: `python -m pytest backend/tests/ -v`

### Frontend Checklist
- [ ] NewsFeed displays with topic filters
- [ ] ArticleCard shows title, summary, topic, dates
- [ ] TopicFilter highlights selected topic
- [ ] Chat interface sends/receives messages
- [ ] Two-column layout renders correctly
- [ ] Frontend tests pass: `cd frontend && npm test`

### Features Checklist
- [ ] TypeScript LSP active (shows type errors in real-time)
- [ ] Pyright LSP active (shows Python type errors)
- [ ] Custom command working (`/component`)
- [ ] Custom skill working (`/start-dev`)
- [ ] Hooks protecting database and config files
- [ ] Agent available (visual-inspector)
- [ ] MCP Chrome DevTools working (can take screenshots)

### Documentation Checklist
- [ ] CLAUDE.md updated for news project
- [ ] README.md explains the Tech News Aggregator
- [ ] .claude/settings.json has all hooks
- [ ] .mcp.json has MCP servers configured

**Test the complete workflow:**

1. Start the app: `/start-dev`
2. Open: http://localhost:5173
3. Ask: "What's the latest AI news this week?"
4. Click topic filter: "Cloud/DevOps"
5. Run tests: `python -m pytest backend/tests/ -v && cd frontend && npm test`
6. Take screenshot: "Use visual-inspector to screenshot the news feed"

**If all works:** Congratulations! Your Tech News Aggregator is complete!

---

## Lab 12: Add Your Own News Digest Page

Now that the base app is running, you will extend it with a fully personalised news digest — a dedicated page that scrapes RSS feeds on a schedule, caches articles in the shared SQLite database, and lets users filter by sub-topic.

The digest page and the chatbot share the same database: the page scrapes specialist feeds every 60 seconds, and the chatbot reads from that cache to answer questions like *"What has SpaceX launched lately?"* — instantly, because the data is already there.

---

### Step 12.1: Browse the Agent Marketplace

Before writing a line of code, browse **[https://app.aitmpl.com](https://app.aitmpl.com)** — a community marketplace of pre-built Claude Code components.

| Category | What you will find |
|----------|--------------------|
| **Skills** | Slash commands — session savers, security reviews, test runners |
| **Agents** | Specialised sub-agents — backend developer, code reviewer, debugger |
| **Hooks** | Event-triggered automations — run tests on save, block dangerous commands |
| **Settings** | Best-practice `.claude/settings.json` presets |

> **Skills vs Agents — what is the difference?**
>
> **Agents** work autonomously in the background — Claude spawns them to do a task (write code, review, debug). You see the result, not every intermediate step.
>
> **Skills** are slash commands you invoke yourself — they guide Claude through a workflow step by step inside your session, staying fully visible the whole time.

**Workshop activity:**
1. Search for something relevant to your digest topic (e.g. `rss`, `news`, `web scraping`, `code review`, `security`)
2. Look for agents that could help you — for example a `backend-developer` agent or a `security-reviewer` agent
3. Install a skill by copying its `.md` file into `.claude/skills/<name>/SKILL.md` and invoke it with `/<name>`
4. Install an agent by copying its `.md` file into `.claude/agents/<name>.md`

**Useful agents for this lab:**
- A **backend-maintainer** or **python-pro** agent to write FastAPI and database code
- A **code-reviewer** agent to check security of each layer
- A **frontend-improver** agent to build the React page

The `/save-to-claude-md` skill is already installed in this project. Run it at the end of every session to persist what you built into `CLAUDE.md` so the next session picks up where you left off.

---

### Step 12.2: Choose Your Topic and Sub-topics

Pick a news topic. Some ideas: `Space & Aerospace`, `Cybersecurity`, `DevOps`, `Quantum Computing`, `Green Tech`, `Gaming`, `Web3`, `Fintech`, `AR/VR`, `Open Source`

For your topic, define:
- **4 to 6 sub-topics** (e.g. for Cybersecurity: `vulnerabilities`, `ransomware`, `privacy`, `cloud-security`, `appsec`, `threat-intel`)
- **RSS feeds** for each sub-topic — you can ask Claude: *"Find me 2 good RSS feeds for [subtopic] news"*

---

### Step 12.3: Enter Plan Mode

Enter Plan Mode before writing any code:

```
Press: Shift + Tab + Tab
```

Then paste this prompt, filling in your topic and sub-topics:

```
I want to add a "[YOUR TOPIC]" news digest page to this project.

Topic: [YOUR TOPIC]
Sub-topics: [LIST YOUR SUBTOPICS]
RSS feeds: [LIST 1-2 FEED URLS PER SUBTOPIC — ask Claude to suggest some if unsure]

This is a FastAPI + React project with a SQLite database and an AI chatbot.
I want to add a full-stack news digest feature that works like this:

1. A background scraper runs on a schedule and fetches articles from RSS feeds,
   storing them in the SQLite database. Deduplicate so the same article is
   never stored twice.

2. A dedicated page in the navigation shows the articles with sub-topic filter
   chips. If the DB has no articles yet for a sub-topic, fetch from RSS on
   demand and cache the result. Auto-refresh the page every 60 seconds.

3. The AI chatbot gets a new tool that lets it answer questions about this
   topic. The tool must read ONLY from the database — it never fetches from
   RSS directly. If the DB has no articles it returns "no articles found".
   This is the key rule: the digest page fills the cache, the chatbot reads
   from it.

Security requirements:
- Validate all sub-topic inputs against an allowlist at every layer
  (the agent tool, the API endpoint, and the DB insert)
- Parameterised SQL queries only — no string interpolation in SQL
- Only store articles with http or https URLs

Explore the existing codebase first to understand its structure and conventions
before planning anything. Use a code-reviewer agent to check the security of
the plan. Produce a detailed step-by-step implementation plan.
```

Review the plan saved to `.claude/plans/`. Read it, ask questions, and adjust anything before approving.

---

### Step 12.4: Approve and Implement

Once you are happy with the plan:

```
The plan looks good. Implement it — backend first (tools file,
DB migration, endpoint, route registration, scraper loop, agent service),
then frontend (types, API client, hook, page component, App.tsx nav).
Run the full test suite after each major step and fix any failures before
moving on.
```

Watch Claude spawn sub-agents to handle each layer.

---

### Step 12.5: Run Tests

```bash
source venv/bin/activate
python -m pytest backend/tests/ -v
```

All original tests must still pass, plus the new tests for your topic.

If there are failures:

```
The test suite has failures. Read the output and fix them.
```

---

### Step 12.6: Verify in the Browser

1. Restart the backend: `python -m backend.main`
2. Open [http://localhost:5173](http://localhost:5173)
3. Click your new tab in the nav bar
4. Articles should load from RSS feeds
5. Click each sub-topic filter — articles should re-fetch and display

If a filter shows no articles:

```
The [subtopic] filter shows no articles. Trace why and fix it.
```

---

### Step 12.7: Chat With Your Digest

The chatbot and your digest page share the same SQLite database. Once your page has scraped some articles, the chatbot can answer questions from that cache.

Try these in the chat:

```
What is the latest news about [your topic]?
What has [specific company] released this week?
Show me the most recent [subtopic] news.
```

**What This Teaches:**
- Full-stack feature development with Plan Mode
- Security-first design: allowlists, parameterised SQL, URL validation
- Shared DB architecture: pages scrape, chatbot reads from cache
- Using backend-maintainer and frontend-improver agents in parallel
- Code-reviewer agent validates security before implementation

---

### Step 12.8: Save the Session

At the end of every session, run:

```
/save-to-claude-md
```

Claude will review the conversation and append a dated summary to `CLAUDE.md` covering decisions made, patterns established, files changed, and bugs fixed. The next session starts with full context already loaded.

---

### How This Digest Differs From RAG — and When to Use Each

The digest you just built uses **SQL keyword search** (`LIKE '%query%'`) to match articles. It works immediately, requires no extra infrastructure, and handles the most common queries well. Understanding its limits — and when RAG is the right upgrade — is useful context.

**How the current search works:**

The agent picks the right tool automatically:
- Broad topic question → calls `search_news` against general RSS feeds
- Specific keyword query (e.g. "Boston Dynamics") → calls `search_all_news`, a `SQL LIKE '%query%'` scan across all cached article titles and summaries
- Your custom topic → calls `search_[topic]_news`, a DB-only read from the cache your digest page pre-scraped

**Why pre-scrape instead of fetching live on every question?**

| | Fetch live on every question | Pre-scraped DB cache |
|--|------------------------------|----------------------|
| **Response time** | 3–8 s (network + parsing) | < 1 s |
| **RSS feed load** | Every question hits the feed servers | Feeds polled on a schedule |
| **Duplicate work** | 10 users ask the same thing = 10 fetches | 10 users = 1 cached result |
| **Offline resilience** | Fails if the feed is down | Still answers from cache |

The digest page acts as a background scraper that continuously warms the cache. The chatbot is a reader — it benefits from everything the page already fetched.

**The limit of keyword search:**

```
"Boston Dynamics"        — finds articles mentioning those exact words ✅
"bipedal robot company"  — no match, even if the article is clearly about Boston Dynamics ❌
"Atlas latest news"      — only matches if "Atlas" literally appears in title or summary ❌
```

**What RAG (Retrieval-Augmented Generation) adds:**

RAG understands meaning, not just words. Here is how it works:

1. **Embed articles on save** — when an article is stored, generate a vector embedding (a list of ~1500 numbers encoding the semantic meaning) using a model like `text-embedding-3-small` or Anthropic's embeddings API
2. **Store the embeddings** — save those vectors alongside the article in SQLite with the `sqlite-vec` extension, or in a dedicated vector DB like pgvector, Chroma, or Qdrant
3. **Embed the query** — at question time, embed the user's question using the same model
4. **Similarity search** — find the articles whose vectors are mathematically closest to the query vector (cosine similarity). Closest = most similar in meaning, not wording
5. **Ground Claude's answer** — inject the retrieved articles into the prompt; Claude reads them and answers based on real content

```
User asks: "bipedal robot company news"
  → embed query → [0.23, -0.87, 0.45, ...]
  → similarity search → Boston Dynamics articles score highest
  → Claude answers grounded in those articles ✅
```

**Keyword search vs RAG — when to use which:**

| | Keyword search (what we built) | Real RAG |
|--|-------------------------------|----------|
| Finds exact words / names | Yes | Yes |
| Finds synonyms | No | Yes |
| Finds by meaning / concept | No | Yes |
| Setup complexity | None — plain SQL | Embedding model + vector store |
| Extra cost | Free | Small cost per article embedded |
| Best for | Company names, direct keywords | Open-ended natural language questions |

For this workshop, keyword search is the right tradeoff — zero extra infrastructure, works immediately, and handles the most common queries well. RAG is the natural next step if you want to turn this into a production product.

**To add RAG to this project, tell Claude Code:**

```
Add semantic search to the news chatbot using Anthropic's embeddings API.
When articles are saved to the DB, generate embeddings and store them in a
sqlite-vec table. Replace the LIKE search in search_all_news with a vector
similarity search. Keep the LIKE search as a fallback if no embeddings exist.
```

---

## Congratulations!

You've successfully built a Tech News Aggregator and mastered all major Claude Code features!

**What You Learned:**

1. Core Claude Code - File operations, terminal integration, git workflows
2. Agent Development - Created 4 custom tools with Strands SDK
3. Full-Stack Architecture - FastAPI backend + React frontend
4. Database Integration - SQLite for article storage
5. Testing - TDD with pytest and Vitest
6. Plugins - TypeScript LSP, Pyright LSP for real-time type checking
7. Custom Commands - `/component` for rapid development
8. Skills - `/start-dev` workflow automation
9. Hooks - PreToolUse for safety and file protection
10. Specialized Agents - visual-inspector for UI testing
11. MCP Servers - Chrome DevTools for browser automation

**What You Built:**

- News Search - Find articles by topic and timeframe
- Categorization - Auto-categorize by tech domain
- Summarization - Generate article summaries
- Trending Topics - See what's hot in tech
- Article History - SQLite database
- Chat Interface - AI-powered news assistant
- Visual Feed - Two-column layout with filters
- Complete Test Coverage - Backend + Frontend tests

**Next Steps:**

1. **Add Real News API Integration**
   - NewsAPI.org (https://newsapi.org/)
   - RSS feeds (TechCrunch, Hacker News, The Verge)
   - Reddit API (r/technology, r/programming)

2. **Deploy to Production**
   - Backend: AWS Lambda + API Gateway or EC2
   - Frontend: Vercel, Netlify, or AWS S3 + CloudFront
   - Database: AWS RDS (PostgreSQL) or keep SQLite

3. **Add User Authentication**
   - JWT tokens or OAuth
   - User-specific bookmarks and preferences
   - Personalized news recommendations

4. **Implement Article Recommendations**
   - Collaborative filtering
   - Content-based filtering with Claude
   - Trending algorithm based on user activity

5. **Add More Features**
   - Email digest subscriptions
   - Slack/Discord notifications
   - Article comments and ratings
   - Multi-language support

**Share Your Work:**

- Push to GitHub and share the repo
- Write a blog post about what you learned
- Create a demo video
- Deploy live and share the URL

**Keep Learning:**

- Explore more Claude Code plugins
- Build custom MCP servers
- Create more specialized agents
- Contribute to open source

---

## Resources

**Official Documentation:**
- Claude Code: https://code.claude.com/docs
- Strands SDK: https://strandsagents.com/docs
- FastAPI: https://fastapi.tiangolo.com/
- React: https://react.dev/
- Vite: https://vitejs.dev/

**Community:**
- Claude Code Discord: https://discord.gg/claude-code
- GitHub Discussions: https://github.com/anthropics/claude-code/discussions

**Example Projects:**
- This repository: Full Tech News Aggregator implementation
- Claude Code Examples: https://github.com/anthropics/claude-code-examples

---

**You're now a Claude Code expert! Go build something amazing!**
