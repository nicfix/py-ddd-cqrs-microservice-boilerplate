from typing import Iterable
from uuid import UUID

from cookiecutter_project_name.command.adapters.repository import Repository
from cookiecutter_project_name.command.domain.models import Pet
from sqlalchemy import orm


class SQLAlchemyRepository(Repository):
    """A Pets Repository that uses SQLAlchemy"""

    def __init__(self, session: orm.Session):
        """
        Initialize the repository using an sqlalchemy session.

        :param session:
        """
        self.session = session

    def all(self, limit: int = 10, offset: int = 0) -> Iterable[Pet]:
        """
        Get all the pets in an iterator.

        :param limit:
        :param offset:
        :return:
        """
        return self.session.query(Pet).filter().limit(limit).offset(offset)

    def count(self) -> int:
        """
        Count the pets in the store.

        :return:
        """
        return self.session.query(Pet).count()

    def get_by_id(self, pet_id: UUID) -> Pet:
        """
        Get a Pet by id.

        :param pet_id: the pet's identifier
        :return: the pet
        """
        return self.session.query(Pet).filter_by(id=str(pet_id)).one()

    def add(self, pet: Pet) -> UUID:
        """
        Add a Pet to the store.

        :param pet: Pet the pet to add
        :return: the id of the added pet.
        """
        self.session.add(pet)
        return pet.id
