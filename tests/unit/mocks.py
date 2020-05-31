from typing import Iterable
from uuid import UUID

from pet_store.adapters.repository import Repository
from pet_store.domain.models import Pet


class MockRepository(Repository):
    """A Mocked Repository implementation, to be used in tests"""

    def count(self) -> int:
        return len(self.pets)

    def all(self, limit: int = 10, offset: int = 0) -> Iterable[Pet]:
        return list(self.pets)

    def __init__(self, pets: Iterable[Pet] = ()):
        self.pets = set(pets)

    def get_by_id(self, pet_id: UUID) -> Pet:
        return next(pet for pet in self.pets if pet.id == pet_id)

    def add(self, pet: Pet) -> UUID:
        self.pets.add(pet)
        return pet.id
