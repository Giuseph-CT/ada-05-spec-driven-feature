# Task Under Test
Change ID: CR-001

## Goal
Add a maximum length validation to the search query input. The system must reject any search query that exceeds 50 characters.

## Requirements Covered
- FR-07 (New): The system MUST validate that the search query is 50 characters or less.
- AC-04 (New): Given a query string of 51 characters, when searching, then a ValidationError is raised with the message "Search query exceeds maximum length of 50 characters."

## Verification
- Run the test suite.
- A new unit test must be added to verify this specific validation rule. The test must pass.

## Constraints
- Use REQUIREMENTS.md and SPEC.md as the source of truth.
- Keep changes scoped to this task.
- Do not redefine existing requirements in this file.