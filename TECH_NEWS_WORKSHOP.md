# Tech News Aggregator Workshop - Adapted from ClaudeCode LabCamp

**Welcome!** This workshop adapts the [main WORKSHOP.md](./WORKSHOP.md) to build a **Tech News Aggregator** instead of a personal assistant. Follow the same Claude Code features, but with a practical news-focused app.

**🎯 Purpose:** Validate that participants can adapt the workshop to build different applications while learning the same Claude Code features.

---

## 🎯 What You'll Build

**Project:** A Tech News Aggregator that:
- Searches for recent tech news articles (AI, Cloud, DevOps, Web Dev, etc.)
- Categorizes articles by technology domain
- Summarizes article content
- Shows trending tech topics
- Stores article history in SQLite
- Provides a chat interface + visual news feed

**Tech Stack:**
- Backend: Python + FastAPI + Strands SDK
- Frontend: React + TypeScript + Vite
- Database: SQLite for article storage
- AI: Claude via Amazon Bedrock

---

## 📋 Prerequisites

Same as main workshop - see [WORKSHOP.md Prerequisites section](./WORKSHOP.md#📋-prerequisites)

**Additional for this project:**
- Understanding of REST APIs
- Basic SQL knowledge (we use SQLite)

---

## 🚀 Lab 0: Repository & Environment Setup

Follow [Lab 0 from main workshop](./WORKSHOP.md#-lab-0-repository-setup-and-environment) exactly - same steps for:
- Git initialization
- Virtual environment creation
- AWS credentials configuration
- GitHub repository connection

**No changes needed** - infrastructure setup is identical.

---

## 🔌 Lab 1: Connect Claude Code

Follow [Lab 1 from main workshop](./WORKSHOP.md#-lab-1-connect-claude-code) exactly:
- Install Claude Code CLI
- Connect to GitHub
- Verify permissions

**No changes needed** - CLI setup is identical.

---

## 🏗️ Lab 2: Build the Tech News Aggregator Project

**This lab adapts Lab 2 from the main workshop** - same structure, different tools!

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
- SQLite database for article storage (articles table)
- API endpoints:
  - POST /api/v1/agent/chat - Chat with agent
  - GET /api/v1/news?topic=AI&days=7 - Get news articles
  - GET /api/v1/trending - Get trending topics

Frontend (React + TypeScript + Vite):
- ChatInterface component (reuse from base architecture)
- NewsFeed component - Display article cards
- ArticleCard component - Individual article display
- TopicFilter component - Filter by tech category (AI, Cloud, DevOps, etc.)
- Two-column layout: Chat interface + News feed side-by-side

Database Schema:
CREATE TABLE articles (
  id INTEGER PRIMARY KEY,
  title TEXT NOT NULL,
  url TEXT NOT NULL,
  summary TEXT,
  topic TEXT,
  published_date TEXT,
  fetched_at TEXT DEFAULT CURRENT_TIMESTAMP
)

Configuration:
- APP_NAME = "Tech News Aggregator"
- NEWS_API_KEY (optional, for production)
- DATABASE_PATH = "./data/articles.db"

Use mock data for articles initially (real API integration can be added later).
Follow the same architecture patterns as the main workshop project.
```

**Review the plan**, approve it, and let Claude generate the project structure.

### Step 2.2: Start the App

**Ask Claude Code:**
```
Start the app
```

Claude will:
1. Activate virtual environment
2. Start FastAPI backend on port 8000
3. Start Vite frontend on port 5173

### Step 2.3: Test the Tech News Agent

**Open:** http://localhost:5173

**Test queries:**
- "What's the latest AI news this week?"
- "Show me Cloud Computing articles"
- "What are the trending tech topics?"
- "Summarize the article at https://example.com/article-1"

**Expected behavior:**
- Agent uses `search_news()` tool to find articles
- Returns formatted article list with titles, dates, summaries
- NewsFeed component displays articles visually
- Topic filter allows filtering by category

---

## 🧪 Lab 3: Test-Driven Development

**Adapts Lab 3 from main workshop** - same TDD approach, different tests.

### Step 3.1: Write Backend Tests

**Ask Claude Code:**
```
Create pytest tests for the Tech News Aggregator:

backend/tests/test_news_tools.py:
- test_search_news_returns_articles()
- test_search_news_filters_by_days()
- test_categorize_article_ai_ml()
- test_categorize_article_cloud_devops()
- test_summarize_article_returns_summary()
- test_get_trending_topics_returns_list()

backend/tests/test_news_endpoints.py:
- test_get_news_endpoint()
- test_get_news_with_topic_filter()
- test_get_trending_endpoint()

backend/tests/test_database.py:
- test_database_initialization()
- test_add_article()
- test_get_articles_by_topic()
- test_get_trending_topics()
```

### Step 3.2: Run Tests

```bash
source claudecodeenv/bin/activate
python -m pytest backend/tests/ -v
```

**Expected:** All tests pass ✅

### Step 3.3: Write Frontend Tests

**Ask Claude Code:**
```
Create Vitest tests for frontend components:

frontend/src/components/__tests__/NewsFeed.test.tsx
frontend/src/components/__tests__/ArticleCard.test.tsx
frontend/src/components/__tests__/TopicFilter.test.tsx
```

---

## 🔍 Lab 4: Add a New Feature with TDD

**Adapts Lab 4** - same TDD workflow, news-specific feature.

**Feature to add:** Article bookmarking

**Ask Claude Code:**
```
Add a bookmark feature to the Tech News Aggregator using TDD:

1. Write failing tests first:
   - Backend: test_bookmark_article(), test_get_bookmarked_articles()
   - Frontend: test_bookmark_button_renders(), test_bookmark_click_saves()

2. Implement the feature:
   - Add bookmarked column to articles table
   - Add bookmark_article() tool
   - Add BookmarkButton component
   - Add GET /api/v1/bookmarks endpoint

3. Run tests to verify they pass
```

---

## 🔧 Lab 5: Add Real-Time Updates

**Adapts Lab 5** - same streaming concepts, news context.

**Ask Claude Code:**
```
Enhance the news feed with real-time updates:

1. Add Server-Sent Events (SSE) for live news updates
2. Update NewsFeed component to show loading states
3. Test streaming: "Keep me updated on AI news as they come in"
```

---

## 🔌 Lab 6: Plugins (TypeScript & Python LSP)

**Follow Lab 6 from main workshop exactly** - LSP setup is identical for both projects.

- Install TypeScript LSP for frontend type checking
- Install Pyright LSP for backend type checking
- Test with intentional type errors in both codebases

**No adaptation needed** - plugin installation is project-agnostic.

---

## 📝 Lab 7: Commands & Skills for Rapid Development

**Adapts Lab 7** - same custom command/skill creation, news-themed examples.

### Step 7.1: Create the /news-search Command

**Ask Claude Code:**
```
Create a custom slash command called /news-search following the official Claude Code documentation.

The command should:
1. Accept arguments: /news-search <topic> <days>
2. Call the search_news tool
3. Format results in a readable markdown table
4. Save to .claude/commands/news-search.md

Example usage: /news-search AI 7
```

### Step 7.2: Create the /fetch-trending Skill

**Ask Claude Code:**
```
Create a custom skill called /fetch-trending that automates:
1. Call get_trending_topics()
2. For each trending topic, call search_news(topic, 7)
3. Save results to data/trending_report.md
4. Display summary with article counts

Create in .claude/skills/fetch-trending/SKILL.md
```

**Test it:**
```
/fetch-trending
```

### Step 7.3: Create Your Own News Command

**Try creating:**
- `/news-digest` - Daily summary of all categories
- `/compare-topics` - Compare article counts between two topics
- `/archive-news` - Export news to JSON/CSV

---

## 🪝 Lab 8: Hooks for Automation

**Follow Lab 8 from main workshop** with these adaptations:

### Step 8.1: Add PreToolUse Hook - Protect Database

**Ask Claude Code:**
```
Add a PreToolUse hook that blocks direct edits to the SQLite database file:

File: .claude/settings.json
Block edits to: data/articles.db
Reason: Database should only be modified via API
```

### Step 8.2: Add PostToolUse Hook - Auto-backup News Data

**Ask Claude Code:**
```
Add a PostToolUse hook that automatically backs up the database after article additions:

Trigger: After Write/Edit to backend/database/
Action: Copy data/articles.db to data/backups/articles-{timestamp}.db
```

### Step 8.3: Add SessionStart Hook - Show News Stats

**Ask Claude Code:**
```
Add SessionStart hook that displays:
- Total articles in database
- Trending topics (top 5)
- Last update timestamp
```

---

## 🤖 Lab 9: Specialized Agents

**Adapts Lab 9** - same agent patterns, news-focused tasks.

### Step 9.1: Create News Content Agent

**Ask Claude Code:**
```
Create a specialized agent for news content analysis:

Agent: news-analyst
Purpose: Deep-dive analysis of news trends
Tools: analyze_sentiment(), detect_duplicates(), compare_sources()
Prompt: "Analyze sentiment trends in Cloud Computing news from the past week"
```

### Step 9.2: Create Data Quality Agent

**Ask Claude Code:**
```
Create an agent that validates news data quality:

Agent: data-quality-checker
Purpose: Check for broken URLs, missing summaries, invalid dates
Prompt: "Audit the database for data quality issues"
```

### Step 9.3: Test Multiple Agents Together

**Ask Claude Code:**
```
Analyze AI news quality and sentiment trends together using both agents
```

---

## 🔌 Lab 10: MCP Servers (Visual News Feed Inspector)

**Adapts Lab 10** - same MCP concepts, news UI testing.

### Step 10.1: Install Chrome DevTools MCP

Follow [Lab 10 steps from main workshop](./WORKSHOP.md#-lab-10-mcp-servers) for MCP installation.

### Step 10.2: Create Visual News Inspector Agent

**Ask Claude Code:**
```
Create an agent that uses Chrome DevTools MCP to visually test the news feed:

Agent: news-feed-inspector
MCP Tools: chrome-devtools (screenshots, console logs)
Purpose: Take screenshots of NewsFeed with different topics

Test:
1. Navigate to http://localhost:5173
2. Take screenshot of initial state
3. Click "AI/ML" topic filter
4. Take screenshot of filtered results
5. Report any visual issues or console errors
```

### Step 10.3: Test Article Card Rendering

**Ask Claude Code:**
```
Use the news-feed-inspector agent to verify:
- Article cards render correctly
- Topic badges display proper colors
- Links are clickable
- Dates format correctly
```

---

## 🎓 Lab 11: Configuration & Best Practices

**Follow Lab 11 from main workshop** - same CLAUDE.md and settings patterns.

**Adaptations for news project:**

### Update CLAUDE.md

**Ask Claude Code:**
```
Update CLAUDE.md to document the Tech News Aggregator:
- Change project description
- Document news tools (search_news, categorize_article, etc.)
- Explain database schema
- Add /news and /trending endpoint docs
```

---

## ✅ Final Verification Checklist

**Backend:**
- [ ] All 4 news tools working (search, categorize, summarize, trending)
- [ ] Database stores articles correctly
- [ ] `/api/v1/news` endpoint returns articles
- [ ] `/api/v1/trending` endpoint returns topics
- [ ] Agent responds to news queries

**Frontend:**
- [ ] NewsFeed displays articles
- [ ] ArticleCard shows title, summary, topic, dates
- [ ] TopicFilter filters by category
- [ ] Chat interface communicates with agent
- [ ] Two-column layout renders correctly

**Tests:**
- [ ] Backend tests pass (news tools, endpoints, database)
- [ ] Frontend tests pass (components, interactions)

**Features:**
- [ ] TypeScript LSP active (frontend type checking)
- [ ] Pyright LSP active (backend type checking)
- [ ] Custom commands working (/news-search)
- [ ] Custom skills working (/fetch-trending)
- [ ] Hooks enforcing database protection
- [ ] Agents performing specialized tasks

**Documentation:**
- [ ] CLAUDE.md updated for news project
- [ ] README.md explains the Tech News Aggregator

---

## 🎉 Congratulations!

You've successfully adapted the ClaudeCode workshop to build a Tech News Aggregator! 

**Key takeaways:**
1. ✅ Workshop structure is **flexible** - same Claude Code features work for any application
2. ✅ Architecture patterns are **reusable** - FastAPI + React + Strands SDK adapts easily
3. ✅ TDD, plugins, hooks, agents, MCP all apply regardless of domain
4. ✅ You validated the workshop is **followable** for different use cases

**Next steps:**
- Add real News API integration (NewsAPI.org, RSS feeds)
- Deploy to production
- Add user authentication
- Implement article recommendations
- Share your learnings!

---

## 📚 Differences from Main Workshop

**What changed:**
- **Agent tools**: weather/calculator/jokes → news/categorize/summarize/trending
- **Database**: Added SQLite for article storage
- **Frontend components**: Added NewsFeed, ArticleCard, TopicFilter
- **API endpoints**: Added /news and /trending
- **System prompt**: Personal assistant → Tech news analyst

**What stayed the same:**
- Lab structure and progression
- Claude Code features (plugins, hooks, agents, MCP)
- Testing approach (TDD with pytest + Vitest)
- Architecture (FastAPI + React + Strands SDK)
- Ports (8000 backend, 5173 frontend)

**Validation result:** ✅ Workshop instructions are adaptable to different domains while teaching the same Claude Code skills.
