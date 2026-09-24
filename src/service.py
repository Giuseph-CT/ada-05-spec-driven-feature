from src.exceptions import ValidationError
from src.models import Customer
from src.repository import CustomerRepository


class CustomerService:
    """Service layer orchestrating customer search validation and execution."""

    def __init__(self, repository: CustomerRepository | None = None) -> None:
        self._repository = repository if repository is not None else CustomerRepository()

    def search(self, query: str) -> list[Customer]:
        """Validate query and search customers through repository."""
        if query is None:
            raise ValidationError("Search query cannot be empty.")

        trimmed_query = query.strip()

        if not trimmed_query:
            raise ValidationError("Search query cannot be empty.")

        if len(trimmed_query) < 2:
            raise ValidationError("Search query must be at least 2 characters long.")

        return self._repository.search_by_text(trimmed_query)
