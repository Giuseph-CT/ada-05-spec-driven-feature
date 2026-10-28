# Repository Map

## Entry Points & Architecture
- `src/cli.py` - CLI Interface Layer (user input/output, argparse formatting).
- `src/service.py` - Domain Service Layer (business validation, search orchestration).
- `src/repository.py` - In-Memory Repository Layer (data storage, substring matching logic).
- `src/models.py` - Data structures (`Customer` dataclass).
- `src/exceptions.py` - Custom application errors (`ValidationError`).

## Tests
- `tests/` - Contains all unit and integration tests (using pytest).

## Change Guide
If changing search or validation behavior:
1. Check `REQUIREMENTS.md` and `SPEC.md` for business rules.
2. Update `src/service.py` if adding business validations (e.g., length, formatting).
3. Update `src/repository.py` if changing text matching or filtering logic.
4. Update `src/cli.py` ONLY if the terminal input/output interface needs to change.
5. Add or modify tests in `tests/`.
6. Run `./scripts/verify_repo.sh` to validate.

## Do Not Edit Directly
- `.venv/` (Virtual environment binaries and libraries)
- `__pycache__/` and `.pytest_cache/`
- `requirements.txt` (unless explicitly requested to add a new dependency)