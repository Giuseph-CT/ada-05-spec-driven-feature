# AGENTS.md

## Read First
1. REQUIREMENTS.md
2. SPEC.md
3. ARCHITECTURE.md
4. TASKS.md

## Sources of Truth
- Business rules and constraints live ONLY in `REQUIREMENTS.md`.
- Verifiable behaviors and test scenarios live in `SPEC.md`.
- Do not change requirements or specs merely to make tests pass.
- Do not invent business requirements.

## Repository Map
- `src/` - Core implementation (CLI, Service, Repository, Models).
- `tests/` - Automated unit and integration tests (pytest).
- `docs/` - Architecture and traceability context.
- `scripts/` - Deterministic operational checks.

## Standard Commands
**CRITICAL:** This project uses a local virtual environment. Do not use global `pytest` or `python` commands. Always use the `.venv/bin/` paths or the provided scripts.

- **Install:** `python3 -m venv .venv && source .venv/bin/activate && pip install -r requirements.txt`
- **Run CLI:** `.venv/bin/python -m src.cli "<query>"`
- **Test:** `.venv/bin/pytest`
- **Verify Coverage:** `.venv/bin/pytest --cov=src`
- **Full Verification:** `./scripts/verify_repo.sh`

## Change Rules
- Keep changes strictly scoped to the requested task.
- Follow the 3-layer architecture defined in `ARCHITECTURE.md` (e.g., validation goes in `service.py`, not `cli.py`).
- Do not weaken or delete existing tests.
- Do not introduce new external dependencies without explicit justification.

## Stop Conditions
Stop execution and ask for human input when:
- Requirements in `REQUIREMENTS.md` conflict with the requested task.
- An architecture boundary must change.
- A required modification affects files outside `src/` and `tests/`.

## Definition of Done
- All relevant new behavior has dedicated unit tests.
- Execution of `./scripts/verify_repo.sh` passes without errors.
- Test coverage remains at or above 90%.
- Acceptance criteria mapped in the task are fully covered.