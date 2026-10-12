# StudySync: project guide for agents

## What this is

StudySync is a small Streamlit study-session app and the shared project for the AI110 Tinkers 1B, 2B, and 3B. The app ships complete from Week 2. Each tinker is a ticket against the running app: one scoped feature, with one part left for the student to finish.

| Tab (`app.py`) | Modules | Tinker |
|---|---|---|
| Session Scorer | `scoring.py`, `scoring_helpers.py`, `test_scoring.py` | 1B, Split the Logic |
| Session Log | `sessions.py` | 2B, Wire It Up |
| Find a Study Spot | `ranking.py`, `data/study_spots.csv`, `diagram.mmd` | 3B, Rank & Explain |

The README has the student-facing setup. This file is for agents and for Danny returning to the project.

## Run and test

- Python 3.13 (`.python-version`). Use the `.venv` in the repo root (gitignored).
- Install: `pip install -r requirements.txt`
- App: `python -m streamlit run app.py`
- Tests: `python -m pytest`
- Demo: `python scoring.py` prints the streak-bonus demo for `run_demo()`.

## Status (snapshot, 2026-10-12)

- **1B:** `test_scoring.py` is complete, with 5 `session_rating` boundary tests (commit `79c952f`, 2026-10-12). `apply_streak_bonus` was moved from `scoring.py` to `scoring_helpers.py` in the working tree on 2026-10-12. That move was uncommitted at the time of this snapshot.
- **2B:** `sessions.py` still has `NotImplementedError` stubs and TODOs for Parts 1–4.
- **3B:** `ranking.py` still has `NotImplementedError` stubs and TODOs. `diagram.mmd` is still the placeholder comment.

This snapshot goes stale. `git log` and `git status` are the source of truth for current state.

## Rules for agents

- **Don't edit `REFLECTIONS.md` unless Danny explicitly asks.** When he does ask, proofread, edit, or organize only what he named. He types his own reflections there.
- **`ai_usage_log.yaml`:** add an entry only when Danny asks. Keep `entries` in chronological order. Record the mechanical fields (timestamp, `session_id`, `decision`). The reflection text is Danny's own words, so leave it blank unless he dictates it.
- **Stay in the ticket scope.** Don't finish a stubbed part unless asked. The docstrings at the top of `scoring.py` and `scoring_helpers.py` are assignment text, not current documentation.
- **Don't commit unless Danny asks.** Make the change, report what changed, and wait for a go-ahead.
- **Streamlit work:** use the `developing-with-streamlit` skill (symlinked under `.agents/` and `.claude/`).
- **Don't touch** `.venv/`, `__pycache__/`, `.pytest_cache/`, or `.DS_Store`.

## Commit messages

- Format: `<category>: <what changed>`. Existing history uses `add:`, e.g. `add: complete session_rating tests with additional boundary cases`.
- The body records what changed, why, and what was decided. Write it as a memory entry for a future agent, not a file list.
- Date and attribute claims in notes and docs, e.g. "Danny confirms (October 2026)…".
- If the session specifies a `Co-Authored-By` trailer, include it.
