import uuid

from pydantic import BaseModel

from pet_store.domain.models import Pet
from pet_store.services.dtos import PetDTO
from pet_store.services.unit_of_work import uow_provider


class AddPetCommand(BaseModel):
    name: str
    age: int


def add_pet(dto: AddPetCommand) -> PetDTO:
    """
    Adds a new pet.

    :param limit: int, how many pets per page
    :param offset: int, how many pets you've already downloaded
    :return: PetsPageDTO, the pets page Data Transfer Object
    """

    uow = uow_provider()
    with uow:
        repo = uow.pets
        id = uuid.uuid4()
        pet = Pet(id=id, **dto.dict())
        pet.id = repo.add(pet)
        uow.commit()

        return PetDTO(id=str(pet.id), name=pet.name, age=pet.age)
