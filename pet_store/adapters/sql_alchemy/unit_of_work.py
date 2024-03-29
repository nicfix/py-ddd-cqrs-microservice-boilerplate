from typing import Callable, Optional

from sqlalchemy.orm import Session

from pet_store.adapters.sql_alchemy.repository import SQLAlchemyRepository
from pet_store.services.unit_of_work import UnitOfWork


class SQLAlchemyUnitOfWork(UnitOfWork):
    """An implementation of Unit of Work using context managers and postgres/mongodb repositories."""

    def __init__(
        self,
        session_factory: Callable[[], Session],
    ):
        self.sql_alchemy_session_factory: Callable[[], Session] = session_factory
        self.sql_alchemy_session: Optional[Session] = None

    def __enter__(self):
        """Initialize postgresql session and mongodb client, create the survey and reviews repositories."""
        self.sql_alchemy_session = self.sql_alchemy_session_factory()
        self.pets = SQLAlchemyRepository(self.sql_alchemy_session)

    def __exit__(self, *args, **kwargs):
        """Exit the context manager and close the postgres session."""
        super().__exit__(*args, **kwargs)
        self.sql_alchemy_session.close()

    def commit(self):
        """Commit the changes in the postgresql session."""
        self.sql_alchemy_session.commit()

    def rollback(self):
        """Rollback the changes in postgresql session."""
        self.sql_alchemy_session.rollback()
