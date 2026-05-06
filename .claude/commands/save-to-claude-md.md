---
description: Summarise this session and persist key decisions to CLAUDE.md
---

You are a technical documentation assistant. Review this entire conversation and extract the following:

1. **Architectural decisions** — choices made and the reasoning behind them
2. **Patterns established** — coding conventions, security rules, design patterns
3. **Files created or significantly changed** — with one-line purpose summaries
4. **Bugs fixed** — root cause + fix approach
5. **User preferences** — how the user likes to work

Then append the following block to CLAUDE.md (create the file if it doesn't exist).
Place it under a `## Session Log` heading at the bottom. Do not overwrite existing content.

```
## Session — YYYY-MM-DD

### Decisions
- ...

### Patterns
- ...

### Files Changed
- `path/to/file.py` — one-line purpose

### Bugs Fixed
- Bug: ... | Root cause: ... | Fix: ...
```

Keep each bullet to one line. Focus on the WHY, not the WHAT.
Omit anything already documented elsewhere in CLAUDE.md.
