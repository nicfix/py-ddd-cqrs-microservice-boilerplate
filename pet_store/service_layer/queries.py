from typing import List
from uuid import UUID

from pydantic.main import BaseModel

from pet_store.service_layer.unit_of_work import uow_provider


class PetDTO(BaseModel):
    """The Data Transfer object for a pet."""

    id: str
    name: str
    age: int


class PetsPageDTO(BaseModel):
    """The Data Transfer Object for a page of pets."""

    pets: List[PetDTO]
    total: int
    limit: int
    offset: int


def get_pets(limit: int = 10, offset: int = 0) -> PetsPageDTO:
    """
    Get a paginated list of pets.

    :param limit: int, how many pets per page
    :param offset: int, how many pets you've already downloaded
    :return: PetsPageDTO, the pets page Data Transfer Object
    """
    uow = uow_provider()
    with uow:
        repo = uow.pets
        pets = list(repo.all(limit, offset))
        total = repo.count()

        return PetsPageDTO(
            pets=[PetDTO(id=pet.id, name=pet.name, age=pet.age) for pet in pets],
            total=total,
            limit=limit,
            offset=offset,
        )


def get_pet(pet_id: UUID) -> PetDTO:
    """
    Get a pet by id.

    :param pet_id: UUID, the unique id of a pet
    :return: PetsDTO, the pet's Data Transfer Object
    """
    uow = uow_provider()
    with uow:
        repo = uow.pets
        pet = repo.get_by_id(pet_id)
        return PetDTO(id=pet.id, name=pet.name, age=pet.age)
