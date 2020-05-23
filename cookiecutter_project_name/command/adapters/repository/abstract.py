import abc

from cookiecutter_project_name.command.domain.models import Pet


class Repository(abc.ABC):
    """The repository interface for the Pet aggregate"""

    def get_by_id(self, id: str) -> Pet:
        """
        Get a Pet by id.

        :param id: the pet's identifier
        :return: the pet
        """
        raise NotImplementedError("Method get_by_id not implemented")

    def add(self, pet: Pet) -> str:
        """
        Add a Pet to the repository.

        :param pet: Pet the pet to add
        :return: the id of the added pet.
        """
        raise NotImplementedError("Method add not implemented")
