# Tasks

## T-01 Project setup
- Goal: Create project directory structure, initial files, and pytest setup.
- Files: `src/__init__.py`, `tests/__init__.py`, `pyproject.toml` or `requirements.txt`.
- Acceptance: `pytest` runs without errors.
- Verification: Execute `pytest` via terminal.

## T-02 Domain model
- Goal: Define `Customer` dataclass and custom `ValidationError` exception.
- Files: `src/models.py`, `src/exceptions.py`, `tests/test_models.py`.
- Acceptance: `Customer` object instantiates correctly with id, name, email.
- Verification: Run `pytest tests/test_models.py`.

## T-03 Search logic
- Goal: Implement `CustomerRepository` and search filtering logic.
- Files: `src/repository.py`, `tests/test_repository.py`.
- Acceptance: Repository filters records by partial name and email (case-insensitive).
- Verification: Run `pytest tests/test_repository.py`.

## T-04 Validation and errors
- Goal: Implement `CustomerService` with query validation rules (FR-03, FR-06).
- Files: `src/service.py`, `tests/test_service.py`.
- Acceptance: Raises `ValidationError` when query length < 2 or whitespace.
- Verification: Run `pytest tests/test_service.py`.

## T-05 Tests
- Goal: Ensure comprehensive test suite execution and high test coverage.
- Files: `tests/test_service.py`, `tests/test_repository.py`.
- Acceptance: Test coverage >= 90%.
- Verification: Run `pytest --cov=src`.

## T-06 Documentation
- Goal: Create `README.md` explaining CLI execution and updates to `AI_USAGE_LOG.md`.
- Files: `README.md`, `AI_USAGE_LOG.md`.
- Acceptance: Clear usage instructions and completed AI interaction log.
- Verification: Manual review of documentation.