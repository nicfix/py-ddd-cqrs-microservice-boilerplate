from typing import Iterable
from uuid import UUID

from cookiecutter_project_name.command.adapters.repository import Repository
from cookiecutter_project_name.command.domain.models import Pet


class MockRepository(Repository):
    """A Mocked Repository implementation, to be used in tests"""

    def __init__(self, pets: Iterable[Pet] = ()):
        self.pets = set(pets)

    def get_by_id(self, id: UUID) -> Pet:
        return next(pet for pet in self.pets if pet.id == id)

    def add(self, pet: Pet) -> UUID:
        self.pets.add(pet)
        return pet.id
