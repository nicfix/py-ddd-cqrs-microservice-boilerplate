from typing import List
from uuid import UUID

from pydantic import BaseModel


class PetDTO(BaseModel):
    """The Data Transfer object for a pet."""

    id: UUID
    name: str
    age: int


class PetsPageDTO(BaseModel):
    """The Data Transfer Object for a page of pets."""

    pets: List[PetDTO]
    total: int
    limit: int
    offset: int
