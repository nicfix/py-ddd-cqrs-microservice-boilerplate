from uuid import UUID

from fastapi import FastAPI

from cookiecutter_project_name.command.adapters.sql_alchemy.repository import (
    SQLAlchemyRepository,
)
from cookiecutter_project_name.infrastructure.bootstrap import bootstrap
from cookiecutter_project_name.infrastructure.db import get_session

app = FastAPI()
bootstrap()


@app.get("/pets")
def get_pets(limit: int = 10, offset: int = 0):
    """
    Get a list of pets.

    :return:
    """
    session = get_session()
    repo = SQLAlchemyRepository(session)
    pets = repo.all(limit, offset)
    total = repo.count()
    return {"pets": list(pets), "total": total, "limit": limit, "offset": offset}


@app.get("/pets/{pet_id}")
def get_pet(pet_id: UUID):
    """
    Get a pet by id.

    :param pet_id:
    :return:
    """
    session = get_session()
    repo = SQLAlchemyRepository(session)
    return repo.get_by_id(pet_id)


@app.get("/healthy")
def healthy_probe():
    """
    Check if the service is in a healthy state.

    :return:
    """
    return {"status": "ok"}


@app.get("/ready")
def ready_probe():
    """
    Check if the service is ready, used mainly after deployment.

    :return:
    """
    return {"status": "ready"}
