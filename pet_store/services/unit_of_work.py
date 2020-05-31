import abc
from typing import Callable

from dependency_injector import providers

from pet_store.adapters.repository import Repository
from pet_store.adapters.sql_alchemy.repository import SQLAlchemyRepository
from pet_store.infrastructure.db import get_session


class AbstractUnitOfWork(abc.ABC):
    """A ContextManager based interface for the UnitOfWork pattern."""

    pets = Repository

    @abc.abstractmethod
    def __enter__(self):
        """Enter the context manager."""
        raise NotImplementedError

    @abc.abstractmethod
    def __exit__(self, *args, **kwargs):
        """Exit from the context manager."""
        self.rollback()

    @abc.abstractmethod
    def commit(self):
        """Commit the changes happened in this Unit of Work."""
        raise NotImplementedError

    @abc.abstractmethod
    def rollback(self):
        """Rollback the changes happened in this Unit of Work."""
        raise NotImplementedError


DEFAULT_REPOSITORY_FACTORY = get_session


class UnitOfWork(AbstractUnitOfWork):
    """An implementation of Unit of Work using context managers and postgres/mongodb repositories."""

    def __init__(
        self, session_factory: Callable = DEFAULT_REPOSITORY_FACTORY,
    ):
        self.sql_alchemy_session_factory = session_factory

        self.sql_alchemy_session = None

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


uow_provider = providers.Factory(UnitOfWork)
