from uuid import UUID

from fastapi import FastAPI

from cookiecutter_project_name.command.adapters.sql_alchemy.orm import start_mappers
from cookiecutter_project_name.command.adapters.sql_alchemy.repository import (
    SQLAlchemyRepository,
)
from cookiecutter_project_name.infrastructure.db import get_session

app = FastAPI()
session = get_session()
mappers = start_mappers()


@app.get("/pets/{pet_id}")
def get_pet(pet_id: UUID):
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
