# Testing Guide: Tech News Aggregator

**Branch:** `test/workshop-news-aggregator`

This guide shows how to test the Tech News Aggregator implementation.

---

## 🚀 Quick Test (5 minutes)

### Step 1: Switch to the Branch

```bash
git checkout test/workshop-news-aggregator
```

### Step 2: Start the Application

**Option A: Let Claude Code start it**
```
Ask Claude: "Start the app"
```

**Option B: Manual start**

Terminal 1 (Backend):
```bash
source claudecodeenv/bin/activate
python -m backend.main
```

Terminal 2 (Frontend):
```bash
cd frontend
npm run dev
```

### Step 3: Open the Application

Visit: **http://localhost:5173**

You should see:
- Header: "Tech News Aggregator"
- Two-column layout:
  - Left: Chat interface
  - Right: News feed with topic filters

### Step 4: Test the Chat Interface

Try these queries:

**Query 1: Search for AI news**
```
What's the latest AI news this week?
```

**Expected:** Agent responds with 3 mock articles about AI (titles, dates, summaries, URLs)

**Query 2: Check trending topics**
```
What are the trending tech topics?
```

**Expected:** Agent shows trending list (AI, Cloud Computing, Web3, Cybersecurity, DevOps)

**Query 3: Categorize an article**
```
Categorize this: "New Kubernetes update improves container orchestration"
```

**Expected:** Agent responds with "Category: Cloud/DevOps"

### Step 5: Test the News Feed

1. **Initial state:** News feed is empty (database is empty)
2. **Topic filter:** Click different topics (AI/ML, Cloud/DevOps, Web Development)
3. **Expected:** Filter buttons change color when selected

---

## 🧪 Full Test Suite (15 minutes)

### Backend API Tests

```bash
# Activate environment
source claudecodeenv/bin/activate

# Test health endpoint
curl http://localhost:8000/health

# Expected: {"status":"healthy","app":"ClaudeCode Lab Agent"}

# Test news endpoint (empty database)
curl "http://localhost:8000/api/v1/news?topic=AI&days=7"

# Expected: []

# Test trending endpoint (empty database)
curl "http://localhost:8000/api/v1/trending"

# Expected: []

# Test agent chat endpoint
curl -X POST http://localhost:8000/api/v1/agent/chat \
  -H "Content-Type: application/json" \
  -d '{"message": "What are the latest AI news?"}'

# Expected: JSON with agent response containing 3 AI articles
```

### Frontend Component Tests

```bash
cd frontend

# Run unit tests (if created)
npm test

# Build production bundle
npm run build

# Preview production build
npm run preview
```

---

## 🔍 Verification Checklist

### ✅ Backend

- [ ] **Server starts** on port 8000
- [ ] **Health endpoint** returns healthy status
- [ ] **Agent responds** to news queries with mock articles
- [ ] **News tools work**: `search_news()`, `categorize_article()`, `summarize_article()`, `get_trending_topics()`
- [ ] **Database initializes** at `data/articles.db`
- [ ] **API endpoints exist**: `/api/v1/news`, `/api/v1/trending`

### ✅ Frontend

- [ ] **Server starts** on port 5173
- [ ] **Title displays**: "Tech News Aggregator"
- [ ] **Two-column layout** renders correctly
- [ ] **Chat interface** accepts input and sends messages
- [ ] **News feed** displays with topic filters
- [ ] **Topic filter buttons** change color when clicked
- [ ] **Article cards** would render if database had data

### ✅ Integration

- [ ] **Chat queries trigger agent tools**
- [ ] **Agent returns formatted news articles**
- [ ] **Frontend receives and displays agent responses**
- [ ] **No console errors** in browser DevTools
- [ ] **No backend errors** in terminal

---

## 🐛 Common Issues

### Issue: "ModuleNotFoundError: No module named 'requests'"

**Cause:** `requests` was imported but not installed (fixed in commit eb5cbe0)

**Fix:** Already fixed - the import was removed since we use mock data

### Issue: News feed shows no articles

**Expected behavior** - the database is empty because:
1. Mock data in tools doesn't persist to database
2. In production, tools would store articles via `db.add_article()`

**To populate database manually:**
```python
from backend.database.db import db

db.add_article(
    title="Test Article",
    url="https://example.com",
    summary="This is a test",
    topic="AI",
    published_date="2026-04-17"
)
```

### Issue: Frontend shows CORS errors

**Check:** Backend must be running on port 8000

**Check:** Frontend must be running on port 5173

**CORS is configured** in `backend/config.py`:
```python
CORS_ORIGINS: Union[List[str], str] = "http://localhost:5173,http://localhost:3000"
```

### Issue: Agent doesn't call tools

**Check system prompt** in `backend/services/agent_service.py`:
- Should mention "always use the search_news tool"
- Agent name should be "tech-news-agent"

---

## 📊 Expected vs. Actual Comparison

### Main Workshop (feature/lab-work)

**Agent Tools:**
- `get_weather(location: str)`
- `calculate(expression: str)`
- `tell_joke()`

**System Prompt:**
- "You are a helpful AI assistant"
- "Help with calculations and weather information"

**Frontend:**
- Single ChatInterface
- "ClaudeCode Lab Agent" title

### Tech News Branch (test/workshop-news-aggregator)

**Agent Tools:**
- `search_news(topic: str, days: int = 7)`
- `categorize_article(text: str)`
- `summarize_article(url: str)`
- `get_trending_topics()`

**System Prompt:**
- "You are a Tech News Aggregator AI assistant"
- "When users ask about a topic, always use the search_news tool"

**Frontend:**
- ChatInterface + NewsFeed side-by-side
- "Tech News Aggregator" title
- Article cards with topic filters

**Database:**
- SQLite at `data/articles.db`
- Schema: articles(id, title, url, summary, topic, published_date, fetched_at)

---

## 🎯 Validation Results

### Question: Can participants follow the main workshop to build this news app?

**Answer:** ✅ **YES** - with adaptations documented in TECH_NEWS_WORKSHOP.md

### What changed:
- Tool implementations (news vs. weather/calculator)
- System prompt (news analyst vs. generic assistant)
- Database addition (SQLite for articles)
- Frontend components (NewsFeed, ArticleCard, TopicFilter)
- API endpoints (GET /news, GET /trending)

### What stayed the same:
- Lab structure (0-11)
- Architecture (FastAPI + React + Strands SDK)
- Claude Code features (plugins, hooks, agents, MCP)
- Testing approach (TDD with pytest + Vitest)
- Ports (8000, 5173)

### Conclusion:
The workshop is **flexible and adaptable** to different application domains. Participants can follow the same structure to build:
- News aggregators
- E-commerce assistants
- Project management tools
- Any domain-specific AI agent

---

## 📸 Screenshots to Verify

1. **Homepage:** Two-column layout with chat on left, news feed on right
2. **Chat response:** Agent listing 3 AI articles with titles, dates, summaries
3. **Topic filter:** Buttons showing AI/ML, Cloud/DevOps, Web Development, etc.
4. **Backend logs:** Agent tool calls visible in terminal
5. **Browser DevTools:** No console errors

---

## 🎓 Learning Outcomes

By testing this implementation, you validated:

1. ✅ **Workshop structure is reusable** across different domains
2. ✅ **Agent tools are swappable** while keeping Strands SDK patterns
3. ✅ **Architecture scales** to more complex use cases (database, multiple endpoints)
4. ✅ **Claude Code features work** regardless of application type
5. ✅ **Documentation adapts** easily to new contexts

**Next:** Try building your own variation! Follow TECH_NEWS_WORKSHOP.md or adapt it further.
