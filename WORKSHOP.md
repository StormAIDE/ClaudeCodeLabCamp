# Tech News Aggregator Workshop Guide

**Welcome to the hands-on ClaudeCode workshop!** 

In this lab, you'll build your own Tech News Aggregator from scratch, learning professional development workflows with Claude Code. By the end, you'll have a working full-stack application that aggregates and analyzes tech news using AI.

**🎯 Workshop Philosophy: "Add Feature → Test Feature → See The Improvement"**

After adding each Claude Code service (plugins, commands, hooks, skills, agents, MCP), you'll immediately test it and see how it improves your development workflow!

---

## 🎯 What You'll Build

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

## 🎓 Claude Code Features You'll Master

This workshop covers **all major Claude Code features** through hands-on practice:

### 🔧 Core Features
- **File Operations**: Read, write, edit, search code
- **Terminal Integration**: Run commands, manage processes
- **Git Workflows**: Commit, branch, PR creation

### 🔌 Plugins (Lab 6)
- **Language Servers (LSP)**: Real-time type checking for TypeScript & Python
- **GitHub Integration**: PR reviews, issue management
- **Plugin Marketplace**: Browse and install community plugins

### 📝 Commands & Skills (Lab 7)
- **Commands**: Reusable prompt templates (`/news-search`, `/fetch-trending`)
- **Skills**: Multi-step workflows (`/commit`, `/review`, `/init`)
- **Custom Creation**: Build your own commands and skills

### 🪝 Hooks (Lab 8)
- **PreToolUse**: Run checks before actions (file protection, database safety)
- **PostToolUse**: Automate after actions (test runs, database backups)
- **SessionStart**: Initialize project context on startup

### 🤖 Agents (Lab 9)
- **Specialized Agents**: News analysts, data quality checkers, content reviewers
- **Agent Delegation**: Assign tasks to expert agents
- **Agent Memory**: Persistent learning across invocations

### 🔌 MCP Servers (Lab 10)
- **Chrome DevTools**: Browser automation, screenshots, UI testing
- **Visual Inspector Agent**: Agent that uses MCP to "see" the news feed
- **Draw.io**: Architecture diagram generation

### ⚙️ Settings & Configuration (Throughout)
- **CLAUDE.md**: Project-specific instructions for Claude
- **settings.json**: Hook configuration and automation
- **.mcp.json**: MCP server configuration

---

## 📋 Prerequisites

Before starting, ensure you have:
- [ ] Python 3.9+ installed
- [ ] Node.js 18+ and npm installed
- [ ] Git installed
- [ ] AWS account with Bedrock access (for Claude AI models)
- [ ] AWS credentials (Access Key ID & Secret Access Key)
- [ ] GitHub account (for version control and CI/CD)
- [ ] VS Code or preferred code editor

**Check your setup:**
```bash
python --version    # Should be 3.9+
node --version      # Should be 18+
npm --version
git --version
aws --version       # AWS CLI should be installed
```

**Note:** We'll install Claude Code in the first step below!

---

## 🚀 Getting Started: Install Claude Code

### Before Lab 0: Install Claude Code CLI

**You need to install Claude Code first!**

#### Option 1: Install in VS Code Terminal (Mac - Recommended)

**Open VS Code terminal and run:**

```bash
# Install Claude Code CLI
curl -fsSL https://claude.ai/install.sh | bash
```

**After installation, start Claude:**
```bash
claude
```

**🔐 First-Time Setup - AWS Bedrock SSO Configuration:**

When you type `claude` for the first time, you'll see a prompt to configure authentication:

1. **Select authentication method**: Choose **AWS Bedrock SSO**
2. **Enter AWS SSO profile name**: Type your profile name (e.g., `default` or your custom profile)
3. **Enter AWS region**: Type `eu-central-1` (or your preferred region)
4. **Follow remaining prompts** to complete setup
5. **Press Enter to restart Claude**
6. **Type `claude` again** - Connection will be established

**✅ You should now be connected and ready to chat!**

#### Option 2: Install for Other Operating Systems

**Follow the official installation guide:**

👉 **[https://code.claude.com/docs/en/quickstart](https://code.claude.com/docs/en/quickstart)**

This guide covers:
- **Windows**: Installation via PowerShell
- **Linux**: Installation via bash script
- **macOS**: Alternative installation methods
- **Desktop App**: Download standalone app
- **VS Code Extension**: Install directly in VS Code

**✅ After installation, start Claude and configure AWS Bedrock SSO as described above.**

**🎯 What This Enables:**
- ✨ Chat with Claude directly from your terminal
- ✨ Claude can read, write, and execute code
- ✨ Seamless integration with your development workflow
- ✨ Access to Claude 4 via Amazon Bedrock

---

## 🛠️ Lab 0: Initial Setup (Before Starting Claude Code)

**Now that Claude Code is installed, let's prepare the project environment:**

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

**💡 Why do this first?** You need an existing folder with git initialized so Claude Code can work with it.

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

**💡 Why?** Python dependencies will be isolated to this project.

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

✅ **Success!** Your repository is now on GitHub.

### Step 0.4: Configure AWS Credentials

**You need AWS credentials to access Claude AI via Bedrock:**

**Option A: AWS CLI Configure (Recommended)**

```bash
aws configure
# AWS Access Key ID: [your-access-key]
# AWS Secret Access Key: [your-secret-key]
# Default region: us-east-1
# Default output format: json
```

**Option B: Set Environment Variables**

```bash
export AWS_ACCESS_KEY_ID=your-access-key
export AWS_SECRET_ACCESS_KEY=your-secret-key
export AWS_SESSION_TOKEN=your-session-token  # If using temporary credentials
```

**✅ Test your AWS setup:**
```bash
aws sts get-caller-identity
# Should return your AWS account details
```

**Checklist before proceeding:**
- [ ] Project folder created (`tech-news-aggregator/`)
- [ ] Git initialized and pushed to GitHub
- [ ] Python virtual environment created (`venv/`)
- [ ] AWS credentials configured
- [ ] Claude Code CLI installed

---

## 🔌 Lab 1: Connect Claude Code

### Step 1.1: Start Claude Code

**In your project directory:**

```bash
# Navigate to project
cd tech-news-aggregator

# Start Claude Code
claude
```

**What you'll see:**
```
Claude Code v[version]
Connected to: tech-news-aggregator/
Ready to assist!
```

**Note:** If this is your first time running Claude, refer to the AWS Bedrock SSO configuration steps in the installation section above.

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

✅ Claude Code should respond with directory info and git status!

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

**✅ Test:**
```bash
gh repo view
# Should show your repository info
```

**🎯 What This Enables:**
- ✨ Create PRs from Claude Code
- ✨ Manage issues directly
- ✨ View PR reviews and checks

---

## 🏗️ Lab 2: Build the Tech News Aggregator Project

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

Use mock data for articles initially (real API integration can be added later).
Follow FastAPI + React + Strands SDK architecture patterns.
Backend port: 8000, Frontend port: 5173
```

**Review the plan**, approve it, and let Claude generate the project structure.

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

**🎯 What You Just Built:**
- ✨ Full-stack app in minutes!
- ✨ Agent with 4 custom tools
- ✨ React frontend with TypeScript
- ✨ FastAPI backend with Strands SDK
- ✨ SQLite database ready for articles
- ✨ Two API endpoints + chat endpoint

---

## 🧪 Lab 3: Test-Driven Development

### Step 3.1: Write Backend Tests

**Ask Claude Code:**
```
Create pytest tests for the Tech News Aggregator in backend/tests/:

test_news_tools.py:
- test_search_news_returns_articles() - Verify 3 articles returned
- test_search_news_filters_by_days() - Verify days parameter works
- test_categorize_article_ai_ml() - Test AI/ML categorization
- test_categorize_article_cloud_devops() - Test Cloud/DevOps categorization
- test_summarize_article_returns_summary() - Verify summary generation
- test_get_trending_topics_returns_list() - Verify 5 topics returned

test_news_endpoints.py:
- test_get_news_endpoint() - Test GET /api/v1/news
- test_get_news_with_topic_filter() - Test ?topic=AI parameter
- test_get_trending_endpoint() - Test GET /api/v1/trending
- test_post_chat_endpoint() - Test POST /api/v1/agent/chat

test_database.py:
- test_database_initialization() - Verify articles table created
- test_add_article() - Test article insertion
- test_get_articles_by_topic() - Test topic filtering
- test_get_trending_topics() - Test trending aggregation
```

### Step 3.2: Run Tests

```bash
source venv/bin/activate
python -m pytest backend/tests/ -v
```

**Expected:** All tests pass ✅

**🎯 What This Teaches:**
- ✨ TDD workflow with pytest
- ✨ Testing agent tools
- ✨ Testing API endpoints
- ✨ Testing database operations

### Step 3.3: Write Frontend Tests

**Ask Claude Code:**
```
Create Vitest tests for frontend components in frontend/src/components/__tests__/:

NewsFeed.test.tsx:
- renders topic filter buttons
- calls API when topic changes
- displays loading state
- shows "no articles" message when empty
- renders article cards when data available

ArticleCard.test.tsx:
- renders article title as clickable link
- displays summary text
- shows topic badge
- formats dates correctly

TopicFilter.test.tsx:
- renders all topic buttons
- highlights selected topic
- calls onChange when clicked
```

### Step 3.4: Run Frontend Tests

```bash
cd frontend
npm test
```

**Expected:** All tests pass ✅

---

## 🔍 Lab 4: Add a New Feature with TDD

**Feature to add:** Article bookmarking

### Step 4.1: Write Failing Tests First

**Ask Claude Code:**
```
Add bookmark feature using TDD:

1. Write these failing tests:
   Backend tests (test_bookmarks.py):
   - test_bookmark_article() - Mark article as bookmarked
   - test_unbookmark_article() - Remove bookmark
   - test_get_bookmarked_articles() - Retrieve bookmarked articles only
   
   Frontend tests (BookmarkButton.test.tsx):
   - test_bookmark_button_renders() - Button appears on article card
   - test_bookmark_click_toggles_state() - Click saves/removes bookmark
   - test_bookmarked_articles_have_filled_icon() - Visual indicator

2. Run tests - they should fail ❌

3. Implement the feature:
   - Add "bookmarked" BOOLEAN column to articles table
   - Create bookmark_article(article_id: int, bookmarked: bool) tool
   - Add POST /api/v1/articles/{id}/bookmark endpoint
   - Add GET /api/v1/bookmarks endpoint
   - Create BookmarkButton component with filled/unfilled heart icon
   - Integrate BookmarkButton into ArticleCard

4. Run tests again - they should pass ✅
```

### Step 4.2: Test Your New Feature

**In the app:**
1. Get some articles: "Show me AI news"
2. Click the heart icon on an article card
3. Filter by "Bookmarked" (new filter button)
4. See only bookmarked articles

**🎯 What This Teaches:**
- ✨ TDD: Tests first, then implementation
- ✨ Database schema migrations
- ✨ Adding new agent tools
- ✨ Creating new React components
- ✨ Full-stack feature development

---

## 🔧 Lab 5: Add Real-Time Updates

### Step 5.1: Implement Server-Sent Events (SSE)

**Ask Claude Code:**
```
Add real-time news updates using SSE:

1. Backend:
   - Create GET /api/v1/news/stream endpoint
   - Return Server-Sent Events stream
   - Send new articles as they're added to database
   - Format: data: {"article": {...}}\n\n

2. Frontend:
   - Update NewsFeed component to use EventSource
   - Connect to /api/v1/news/stream
   - Auto-append new articles to feed
   - Show toast notification: "New article: {title}"
   - Add "Live Updates" toggle switch

3. Test:
   - Enable live updates in UI
   - In another terminal: curl -X POST to add article to DB
   - Verify new article appears in feed automatically
```

### Step 5.2: Test Streaming Chat

**Ask Claude Code:**
```
Test the agent's streaming response:

In chat, type: "Keep me updated on AI news as they come in"

Agent should respond in streaming chunks showing progressive text.
```

**🎯 What This Teaches:**
- ✨ Server-Sent Events (SSE)
- ✨ Real-time data updates
- ✨ Streaming agent responses
- ✨ EventSource API in React

---

## 🔌 Lab 6: Plugins (TypeScript & Python LSP)

### Step 6.1: Install TypeScript LSP Plugin

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

### Step 6.2: Install Pyright LSP Plugin

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

### Step 6.3: Install GitHub Plugin (optional)

**In Claude Code:**
```
/plugin install github@claude-plugins-official
/reload-plugins
```

**Test it:**

**Ask Claude Code:**
```
Create an issue titled "Add RSS feed integration" with description: "Integrate real RSS feeds from TechCrunch, Hacker News, The Verge for live news updates"
```

**Expected:** Issue created on GitHub!

**🎯 What This Teaches:**
- ✨ LSP for real-time type checking
- ✨ Plugin marketplace usage
- ✨ GitHub integration for issues/PRs
- ✨ Developer productivity tools

---

## 📝 Lab 7: Commands & Skills for Rapid Development

### Step 7.1: Create the /component Command

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

**✅ Test It - Generate Your First Component:**

**Try it:**
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

**🎯 What This Teaches:**
- ✨ Custom command creation using official SDK
- ✨ Reusable code generation templates
- ✨ Component scaffolding automation
- ✨ Time saved: 10 minutes → 30 seconds per component

### Step 7.2: Create the /news-search Command

**Ask Claude Code:**
```
Create a /news-search command in .claude/commands/news-search.md that:
1. Accepts: /news-search <topic> <days>
2. Calls search_news tool with parameters
3. Formats results as markdown table with columns: Title | Date | Topic | URL
4. Saves to data/searches/<topic>-<timestamp>.md

Example: /news-search AI 7
```

**Test it:**
```
/news-search "Cloud Computing" 7
```

**Expected:** Creates `data/searches/cloud-computing-2026-04-17.md` with formatted table

### Step 7.3: Create the /start-dev Skill

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

**✅ Test It:**
```
/start-dev
```

**Expected:**
```
✅ Virtual environment activated
🚀 Starting backend on port 8000...
✅ Backend running at http://localhost:8000
🚀 Starting frontend on port 5173...
✅ Frontend running at http://localhost:5173
✨ Both servers are ready!
```

**🎯 What This Teaches:**
- ✨ Multi-step skill creation
- ✨ Background process management
- ✨ Error handling in skills
- ✨ Time saved: Manual steps → One command

### Step 7.4: Create the /test-all Skill

**Ask Claude Code:**
```
Create /test-all skill that:
1. Activates venv
2. Runs backend tests: python -m pytest backend/tests/ -v
3. Runs frontend tests: cd frontend && npm test -- --run
4. Generates combined coverage report
5. Shows summary: X/Y tests passed

Save in .claude/skills/test-all/SKILL.md
```

**Test it:**
```
/test-all
```

**Expected:** Both test suites run, coverage report generated

### Step 7.5: Create Your Own Custom Skill

**Skills live in `.claude/skills/` and can have complex logic. Let's create one for system health checks!**

**Ask Claude Code:**
```
Create a custom skill called /check-health following the official Claude Code skills documentation.

Reference: https://code.claude.com/docs/en/agent-sdk/slash-commands (skills section)

The skill should:
1. Check if backend server is running (curl localhost:8000/health)
2. Check if frontend server is running (curl localhost:5173)
3. If backend is down, show how to start it (activation + python -m backend.main)
4. If frontend is down, show how to start it (cd frontend && npm run dev)
5. Report overall system status with colored output (✅ for running, ❌ for down)
6. Show response times for each service
7. Display the last 3 lines of logs if a service is down

Create the skill in .claude/skills/check-health/SKILL.md with proper frontmatter.
```

**Skill structure:**
```markdown
---
name: check-health
description: Check system health (backend, frontend, database)
---

[Implementation instructions for Claude...]
```

**Test it:**
```
Stop the backend server, then run:
/check-health
```

**Watch:** Skill detects backend is down and shows how to start it!

**Try again with both running:**
```
Start both servers, then run:
/check-health
```

**Watch:** See both services reporting healthy with response times!

**🎯 What This Improves:**
- ✨ Quick system health checks
- ✨ Helpful debugging when services are down
- ✨ Time saved: Manual curl testing → One command health report
- ✨ Custom skill development with complex logic

---

## 🪝 Lab 8: Hooks for Automation

### Step 8.1: Add PreToolUse Hook - Block Dangerous Commands

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

**✅ Test It:**

**Ask Claude:** "Delete all files with rm -rf /"

**Expected:** Hook blocks it with error: "🔒 BLOCKED: Dangerous command detected"

### Step 8.2: Add PreToolUse Hook - Protect Database and Config Files

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

### Step 8.3: Add SessionStart Hook - Show Project Context

**This hook runs every time you start Claude Code!**

**Ask Claude Code:**
```
Create a SessionStart hook that shows project context on startup.

Create .claude/hooks/session-start.sh that displays:
1. Project name and branch
2. Last commit message
3. Total articles in database (sqlite3 query)
4. Trending topics (top 3)
5. Servers running? (check ports 8000, 5173)

Add to .claude/settings.json:
{
  "hooks": {
    "SessionStart": {
      "command": ".claude/hooks/session-start.sh"
    }
  }
}
```

**Test:** Restart Claude Code - you should see project context banner!

**🎯 What This Teaches:**
- ✨ PreToolUse hooks prevent mistakes
- ✨ File protection for sensitive data
- ✨ SessionStart hooks provide context
- ✨ Automation without manual checks

---

## 🤖 Lab 9: Specialized Agents

### Step 9.1: Understand Agent Types

**Read about agents:**
```
https://code.claude.com/docs/en/sub-agents
```

**Key concepts:**
- **Agents** run in separate context (isolated from main chat)
- **Results** are summarized back to you
- **Use cases**: Research, code review, testing, exploration

### Step 9.2: Create News Content Analyst Agent

**Ask Claude Code:**
```
Create a specialized agent for analyzing news content trends.

Create .claude/agents/news-analyst.md with:

---
name: news-analyst
description: Analyzes news trends, sentiment, and patterns across articles
model: sonnet
---

# System Prompt
You are a news content analyst specializing in technology news. You analyze:
- Sentiment trends (positive, negative, neutral coverage)
- Topic correlations (which topics appear together)
- Source credibility and bias
- Emerging trends and patterns

When given a set of articles, provide:
1. Overall sentiment distribution
2. Most discussed subtopics
3. Notable patterns or trends
4. Recommendations for further investigation

# Tools
You have access to:
- search_news() - Find articles by topic
- categorize_article() - Get article categories
- Database queries via SQLite

# Response Format
Always structure your analysis as:
## Sentiment Analysis
[breakdown]

## Topic Trends  
[patterns]

## Recommendations
[what to investigate next]
```

**Test it:**

**Ask Claude:** "Use the news-analyst agent to analyze AI news sentiment from this week"

**Expected:** Agent spawns, analyzes articles, returns summary of findings

### Step 9.3: Create Data Quality Checker Agent

**Ask Claude Code:**
```
Create an agent that audits news data quality.

Create .claude/agents/data-quality.md:

---
name: data-quality-checker
description: Audits database for quality issues (broken URLs, missing data, duplicates)
model: haiku
---

# System Prompt
You are a data quality auditor for a news aggregation system. Your job:

Check for:
1. **Broken URLs** - Try fetching each article URL, flag 404s
2. **Missing summaries** - Articles without summary field
3. **Duplicate articles** - Same title or URL appearing multiple times
4. **Invalid dates** - Dates in the future or before 2020
5. **Orphaned categories** - Articles with invalid topic values

# Output Format
Report findings as:
## Critical Issues (blocks functionality)
- [list with article IDs]

## Warnings (should fix soon)
- [list with article IDs]

## Statistics
- Total articles: X
- Quality score: Y%
```

**Test it:**

**Ask Claude:** "Use data-quality-checker agent to audit the database"

**Expected:** Agent reports quality metrics and issues found

### Step 9.4: Create Code Review Agent

**Ask Claude Code:**
```
Use the built-in code-reviewer agent to review news tools.

Prompt: "Review backend/tools/news_tools.py for:
- Code quality and best practices
- Error handling completeness
- Type hints accuracy
- Mock data realism
- Suggest improvements"
```

**Expected:** Detailed code review with specific suggestions

### Step 9.5: Test All Agents Together

**Ask Claude Code:**
```
Run a comprehensive analysis using multiple agents:

1. news-analyst: Analyze Cloud Computing news trends
2. data-quality-checker: Audit database health
3. code-reviewer: Review backend/api/endpoints/news.py

Run them in parallel and summarize findings across all three.
```

**Expected:** All 3 agents run, results combined into unified report

**🎯 What This Teaches:**
- ✨ Creating custom agents with specific expertise
- ✨ Agent isolation (separate context windows)
- ✨ Using multiple agents in parallel
- ✨ Delegating specialized tasks to expert agents

---

## 🔌 Lab 10: MCP Servers (Visual News Feed Inspector)

### Step 10.1: Understand MCP

**Read the docs:**
```
https://code.claude.com/docs/en/mcp
```

**Key concepts:**
- **MCP (Model Context Protocol)** connects external tools to Claude
- **MCP Servers** expose tools via standard protocol
- **Examples**: Chrome DevTools, Draw.io, Database clients

### Step 10.2: Install Chrome DevTools MCP

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

### Step 10.3: Create Visual News Feed Inspector Agent

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

### Step 10.4: Test Article Card Rendering

**Ask Claude:** 
```
Use visual-inspector to verify:
1. Article cards render with all fields (title, summary, topic, date)
2. Topic badges have correct colors
3. Links are clickable
4. Layout is responsive
Take screenshots of any issues found.
```

### Step 10.5: Install Draw.io MCP (Optional)

**Ask Claude Code:**
```
Add Draw.io MCP server to .mcp.json for architecture diagrams:

{
  "mcpServers": {
    "chrome-devtools": { ... },
    "drawio": {
      "command": "npx",
      "args": ["-y", "@keturiosakys/mcp-server-drawio"]
    }
  }
}

Restart Claude Code to load it.
```

**Test it:**

**Ask Claude:** "Create an architecture diagram of the Tech News Aggregator showing Backend (FastAPI + Strands + SQLite), Frontend (React + TypeScript), and AI (Claude via Bedrock)"

**Expected:** `.drawio` file created with architecture diagram!

**🎯 What This Teaches:**
- ✨ MCP server configuration
- ✨ Browser automation with Chrome DevTools
- ✨ Visual testing with screenshots
- ✨ Diagram generation with Draw.io
- ✨ External tool integration

---

## 🎓 Lab 11: Configuration & Best Practices

### Step 11.1: Update CLAUDE.md

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
  fetched_at TEXT DEFAULT CURRENT_TIMESTAMP,
  bookmarked BOOLEAN DEFAULT 0
)
```

## Development Commands
- Start app: /start-dev
- Run tests: /test-all
- Check health: /check-health
- Search news: /news-search <topic> <days>

## Important Files
- backend/tools/news_tools.py - Agent tool implementations
- backend/database/db.py - SQLite wrapper
- frontend/src/components/NewsFeed.tsx - Main news feed UI
- .claude/agents/news-analyst.md - News analysis agent
- .claude/agents/visual-inspector.md - UI testing agent

## Rules
- Database should only be modified via API (protected by PreToolUse hook)
- All tests must pass before committing
- Use TypeScript strict mode in frontend
- Agent tools should return formatted markdown
```

### Step 11.2: Review .claude/settings.json

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
    },
    "SessionStart": {
      "command": ".claude/hooks/session-start.sh"
    }
  }
}
```

### Step 11.3: Review .mcp.json

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
    },
    "drawio": {
      "command": "npx",
      "args": ["-y", "@keturiosakys/mcp-server-drawio"]
    }
  }
}
```

**🎯 What This Teaches:**
- ✨ Project documentation for AI collaboration
- ✨ Hook configuration management
- ✨ MCP server setup
- ✨ Best practices for team projects

---

## ✅ Final Verification Checklist

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
- [ ] Custom commands working (`/component`, `/news-search`)
- [ ] Custom skills working (`/start-dev`, `/test-all`, `/check-health`)
- [ ] Hooks protecting database and config files
- [ ] Agents available (news-analyst, data-quality-checker, visual-inspector)
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
5. Run health check: `/check-health`
6. Run tests: `/test-all`
7. Take screenshot: "Use visual-inspector to screenshot the news feed"

**If all works:** 🎉 **Congratulations! Your Tech News Aggregator is complete!**

---

## 🎉 Congratulations!

You've successfully built a Tech News Aggregator and mastered all major Claude Code features!

**What You Learned:**

1. ✅ **Core Claude Code** - File operations, terminal integration, git workflows
2. ✅ **Agent Development** - Created 4 custom tools with Strands SDK
3. ✅ **Full-Stack Architecture** - FastAPI backend + React frontend
4. ✅ **Database Integration** - SQLite for article storage
5. ✅ **Testing** - TDD with pytest and Vitest
6. ✅ **Plugins** - TypeScript LSP, Pyright LSP, GitHub integration
7. ✅ **Custom Commands** - `/component`, `/news-search` for rapid development
8. ✅ **Skills** - `/start-dev`, `/test-all`, `/check-health` workflows
9. ✅ **Hooks** - PreToolUse for safety, SessionStart for context
10. ✅ **Specialized Agents** - news-analyst, data-quality-checker, visual-inspector
11. ✅ **MCP Servers** - Chrome DevTools for UI testing, Draw.io for diagrams

**What You Built:**

- 🔍 **News Search** - Find articles by topic and timeframe
- 📊 **Categorization** - Auto-categorize by tech domain
- 📝 **Summarization** - Generate article summaries
- 🔥 **Trending Topics** - See what's hot in tech
- 💾 **Article History** - SQLite database
- 💬 **Chat Interface** - AI-powered news assistant
- 📰 **Visual Feed** - Two-column layout with filters
- 🔖 **Bookmarking** - Save favorite articles
- 🔴 **Live Updates** - Real-time SSE streaming

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

## 📚 Resources

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

**🎓 You're now a Claude Code expert! Go build something amazing!** 🚀
