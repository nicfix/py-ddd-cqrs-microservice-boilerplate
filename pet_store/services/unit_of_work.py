import abc

from pet_store.adapters.repository import Repository


class UnitOfWork(abc.ABC):
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
