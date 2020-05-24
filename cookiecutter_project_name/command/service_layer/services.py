from typing import List

from pydantic.main import BaseModel
from sqlalchemy import orm

from cookiecutter_project_name.command.adapters.sql_alchemy.repository import (
    SQLAlchemyRepository,
)


class PetDTO(BaseModel):
    id: str
    name: str
    age: int


class PetsPageDTO(BaseModel):
    pets: List[PetDTO]
    total: int
    limit: int
    offset: int


def get_pets(session: orm.Session, limit: int = 10, offset: int = 0) -> PetsPageDTO:
    repo = SQLAlchemyRepository(session)
    pets = list(repo.all(limit, offset))
    total = repo.count()
    return PetsPageDTO(
        pets=[PetDTO(id=pet.id, name=pet.name, age=pet.age) for pet in pets],
        total=total,
        limit=limit,
        offset=offset,
    )
