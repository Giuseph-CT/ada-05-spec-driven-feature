# BEFORE Agent Run

## Run Context
Agent: Google Antigravity
Model: Gemini Argon 4 Medium
Tools: File System, Bash/Terminal
Permissions: Local workspace access
Baseline commit/tag: ada08-baseline

## Clarification Questions
- None. The agent proceeded based on the initial prompt.

## Repository Exploration
- Read `TASK_UNDER_TEST.md`
- Read `REQUIREMENTS.md`
- Read `SPEC.md`
- Inspected `src/service.py`
- Inspected `tests/test_service.py`

## Incorrect Assumptions
- The agent initially assumed that the global `pytest` command was available and configured in the terminal session environment.

## Failed / Unknown Commands
- Command: `pytest`
  - Result: Failed on the first attempt.
  - Resolution: The agent inferred the need to bypass the global path and directly invoked the virtual environment binary instead (`.venv/bin/pytest || python3 -m pytest`).

## Out-of-Scope Changes
- None. The agent strictly modified the necessary domain logic (`src/service.py`) and test files (`tests/test_service.py`).

## Validation Evidence
- Added `test_service_query_exceeding_max_length_raises_validation_error` (51 chars).
- Added `test_service_query_at_max_length_is_valid` (50 chars).
- Executed `.venv/bin/pytest -v --cov=src`.
- 34 tests passed successfully with 99% coverage, exceeding the NFR-02 requirement.

## Final Result
PASS (The agent successfully completed the task, but experienced measurable friction with environment execution).

---

# Implicit Knowledge Found

## IK-01
What:
Testing requires explicit invocation of the virtual environment binaries (e.g., `.venv/bin/pytest`) rather than standard global commands (`pytest`).
How was it discovered:
The agent attempted to run `pytest` directly, which resulted in a failed command execution, forcing a fallback strategy.
Should this remain implicit?
NO
Where should it become explicit?
In `AGENTS.md` (via a standard commands section) and encapsulated in an executable script like `scripts/run_tests.sh`.

---

## Changes Made

### Improvement I-01
Category: Context
Problem: The agent had to infer the exact test execution commands and environment paths (virtual environment).
Change: Updated `AGENTS.md` to act as an operational contract, explicitly listing the `Standard Commands` using `.venv/bin/...` binaries.
Evidence: The agent will rely on the documented commands rather than global fallbacks.

### Improvement I-02
Category: Executable Knowledge
Problem: Complex or multi-step validation logic (like checking tests + coverage) relies on the agent remembering flags.
Change: Created `scripts/verify_repo.sh` to run tests and coverage deterministically.
Evidence: `AGENTS.md` points to this script as the Definition of Done verifier.

### Improvement I-03
Category: Context
Problem: The agent starts executing commands and writing code without a structured plan, increasing the risk of architectural mistakes.
Change: Created `GEMINI.md` as a tool-specific adapter to enforce a planning phase and point to `AGENTS.md`.
Evidence: The agent will output a short plan before applying modifications.

### Improvement I-04
Category: Navigation
Problem: The agent had to read the source code of multiple files (`cli.py`, `service.py`) just to understand where validation logic lives.
Change: Created `docs/REPO_MAP.md` to explicitly map architectural boundaries (CLI vs Service vs Repository).
Evidence: The agent can directly target `src/service.py` for validation tasks without scanning the entire `src/` folder.

### Improvement I-05
Category: Executable Knowledge & Automation
Problem: Validation required the agent to remember and string together multiple test and coverage commands.
Change: Created `scripts/verify_repo.sh` to centralize environment setup, testing, and contract verification in a single, deterministic command.
Evidence: The agent only needs to call `./scripts/verify_repo.sh` to prove Definition of Done.

### Improvement I-06
Category: Guardrail & CI Check
Problem: The agent could theoretically bypass tests or delete critical markdown files without immediate failure.
Change: 
1. Added `scripts/check_repo_contract.py` to ensure structural integrity (blocking deletion of `AGENTS.md`, `SPEC.md`, etc.).
2. Integrated a git `pre-commit` hook and `.github/workflows/verify.yml` to automatically execute `verify_repo.sh` outside the agent's direct control.
Evidence: Any commit with failing tests or missing contract files is deterministically rejected.