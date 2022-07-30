from uuid import UUID

from pet_store.adapters import repository
from pet_store.services.dtos import PetDTO, PetsPageDTO
from pet_store.services.unit_of_work import AbstractUnitOfWork


def get_pets(uow: AbstractUnitOfWork, limit: int = 10, offset: int = 0) -> PetsPageDTO:
    """
    Get a paginated list of pets.

    :param uow: the unit of work for this transaction
    :type uow: AbstractUnitOfWork
    :param limit: how many pets per page
    :type limit: int
    :param offset: how many pets you've already downloaded
    :type offset: int
    :return: the pets page Data Transfer Object
    :rtype: PetsPageDTO
    """
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


class NoPetFoundError(Exception):
    pass


def get_pet(pet_id: UUID, uow: AbstractUnitOfWork) -> PetDTO:
    """
    Get a pet by id.
    :param pet_id: the unique id of an existing pet
    :type pet_id: UUID
    :param uow: the unit of work for this transaction
    :type uow: AbstractUnitOfWork
    :return: a data transferable representation of the pet
    :rtype: PetDTO
    :raises NoPetFound: when no pet is found for the requested id.
    """
    with uow:
        repo = uow.pets

        try:
            pet = repo.get_by_id(pet_id)
        except repository.NoPetFoundError as e:
            raise NoPetFoundError() from e

        return PetDTO(id=pet.id, name=pet.name, age=pet.age)
