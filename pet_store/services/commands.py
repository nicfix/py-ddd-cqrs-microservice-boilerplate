import uuid

from pydantic import BaseModel

from pet_store.domain.models import Pet
from pet_store.services.dtos import PetDTO
from pet_store.services.unit_of_work import AbstractUnitOfWork


class AddPetCommand(BaseModel):
    name: str
    age: int


def add_pet(
        dto: AddPetCommand,
        uow: AbstractUnitOfWork
) -> PetDTO:
    """
    Adds a pet to the system.

    :param dto: the data needed to execute this command
    :type dto: AddPetCommand
    :param uow: the unit of work for this transaction
    :type uow: AbstractUnitOfWork
    :return: a data transferable representation of the Pet
    :rtype: PetDTO
    """

    with uow:
        repo = uow.pets
        pet_id = uuid.uuid4()
        pet = Pet(id=pet_id, **dto.dict())
        pet.id = repo.add(pet)
        uow.commit()

        return PetDTO(id=pet.id, name=pet.name, age=pet.age)
