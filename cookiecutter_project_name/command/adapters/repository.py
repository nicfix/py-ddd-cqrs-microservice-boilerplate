import abc
from typing import Iterable
from uuid import UUID

from cookiecutter_project_name.command.domain.models import Pet


class Repository(abc.ABC):
    """The repository interface for the Pet aggregate"""

    @abc.abstractmethod
    def all(self, limit: int = 10, offset: int = 0) -> Iterable[Pet]:
        """
        Get all the pets in an iterator.

        :param limit:
        :param offset:
        :return:
        """
        raise NotImplementedError

    @abc.abstractmethod
    def count(self) -> int:
        """
        Count the pets in the store.

        :return:
        """
        raise NotImplementedError

    @abc.abstractmethod
    def get_by_id(self, pet_id: UUID) -> Pet:
        """
        Get a Pet by id.

        :param pet_id: the pet's identifier
        :return: the pet
        """
        raise NotImplementedError

    @abc.abstractmethod
    def add(self, pet: Pet) -> UUID:
        """
        Add a Pet to the store.

        :param pet: Pet the pet to add
        :return: the id of the added pet.
        """
        raise NotImplementedError
