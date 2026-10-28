# Repository Readiness Audit

## BEFORE

| Dimension | Score 0-5 | Weighted | Evidence | Main Gap |
|---|---:|---:|---|---|
| 1. Entry Point & Navigation | 4 | 12.0/15 | `README.md` details structure (`src/cli.py`, `service.py`) and execution. | Agent must infer that `README.md` contains commands, as `AGENTS.md` does not link to it as an entry point. |
| 2. Agent Instructions | 3 | 9.0/15 | `AGENTS.md` defines logical rules but lacks exact operative commands. | Lacks explicit execution commands; orders running `pytest` but omits virtual environment setup. |
| 3. Build / Run / Test | 4 | 12.0/15 | `README.md` lists explicit commands for venv, dependencies, and CLI. | Virtual environment activation often fails for agents if not automated or strictly enforced in instructions. |
| 4. Architecture Boundaries | 5 | 10.0/10 | `ARCHITECTURE.md` assigns exact responsibilities per file and layer. | N/A. Boundaries are clear and discoverable. |
| 5. Requirements & Traceability | 4 | 8.0/10 | `SPEC.md` contains explicit IDs (FR-01, AC-01) and clear rules. | Instructions do not explicitly force the agent to inject the Change ID in commits or PRs. |
| 6. Automation & Guardrails | 1 | 2.0/10 | `pytest` and `pytest-cov` are configured. | No preventive automation (pre-commit hooks, CI, linters). If the agent skips tests, nothing blocks it. |
| 7. Testability & Evidence | 4 | 12.0/15 | `README.md` defines `pytest --cov=src` with a 100% expectation. | Lacks a consolidated script (e.g., `test.sh`) to automatically capture output evidence for Definition of Done. |
| 8. Safety & Permissions | 3 | 6.0/10 | In-memory operations present low risk of data destruction. | No explicit limits on modifying configuration files (`pyproject.toml`) or git workflows. |

TOTAL BEFORE: 71.0 / 100

Top 3 friction points:
1. Lack of automation (Guardrails): The agent relies entirely on obedience to AGENTS.md to run tests; the repository does not actively block unverified changes.
2. Environment friction (Virtual Env): Execution requires venv activation and sys.path handling (`python -m src.cli`), which frequently breaks isolated agent terminals.
3. Disconnect between AGENTS.md and execution: Agent instructions omit exact coverage and test commands, forcing the agent to make a logical jump to find them in the README.

## AFTER

| Dimension | Score 0-5 | Weighted | Evidence | Improvement |
|---|---:|---:|---|---|
| 1. Entry Point & Navigation | 5 | 15.0/15 | `REPO_MAP.md` explicitly links boundaries and files. | Agent no longer guesses architectural layers. |
| 2. Agent Instructions | 5 | 15.0/15 | `AGENTS.md` acts as a strict operational contract. | Added exact Standard Commands and Stop Conditions. |
| 3. Build / Run / Test | 5 | 15.0/15 | `./scripts/verify_repo.sh` handles environment setup automatically. | Removed the implicit need for `source .venv/bin/activate`. |
| 4. Architecture Boundaries | 5 | 10.0/10 | `ARCHITECTURE.md` + `REPO_MAP.md` enforce limits. | Discoverability enhanced without rewriting docs. |
| 5. Requirements & Traceability | 5 | 10.0/10 | `SPEC.md` + Definition of Done in `AGENTS.md`. | Enforced verifiable behavior explicitly. |
| 6. Automation & Guardrails | 4 | 8.0/10 | `check_repo_contract.py` and pre-commit hook active. | Commits with broken tests are deterministically blocked. |
| 7. Testability & Evidence | 5 | 15.0/15 | `verify_repo.sh` unifies tests, coverage, and contract checks. | Agent provides standard script output as DoD evidence. |
| 8. Safety & Permissions | 4 | 8.0/10 | `AGENTS.md` and repo contract protect critical files. | Agent instructed to stop if destructive actions arise. |

**TOTAL AFTER: 96.0 / 100**
**DELTA: AFTER - BEFORE = +25 points (71 -> 96)**