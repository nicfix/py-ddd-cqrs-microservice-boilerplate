from uuid import UUID

from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware

from pet_store.infrastructure.bootstrap import bootstrap
from pet_store.services import queries, commands
from pet_store.services.commands import AddPetCommand
from pet_store.services.dtos import PetDTO, PetsPageDTO
from pet_store.services.queries import NoPetFoundError
from pet_store.services.unit_of_work import uow_provider

app = FastAPI()

origins = ["http://localhost:3000"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
    expose_headers=["Access-Control-Allow-Origin"],
)

# Initialize infrastructure (SQLAlchemy mappings, session provider, etc)
bootstrap()


@app.get("/pets", response_model=PetsPageDTO)
def get_pets(limit: int = 10, offset: int = 0) -> PetsPageDTO:
    """
    Get a list of pets.

    :return:
    """
    uow = uow_provider()
    response = queries.get_pets(uow, limit, offset)
    return response


@app.get("/pets/{pet_id}", response_model=PetDTO)
def get_pet(pet_id: UUID) -> PetDTO:
    """
    Get a pet by id.

    :param pet_id:
    :return:
    """
    uow = uow_provider()
    try:
        return queries.get_pet(pet_id, uow)
    except NoPetFoundError as e:
        raise HTTPException(status_code=404, detail=f"No pet found for id {str(pet_id)}") from e


@app.post("/pets", response_model=PetDTO)
def add_pet(pet_body: AddPetCommand) -> PetDTO:
    """
    Get a pet by id.

    :param pet_body:PetDTO
    :return:
    """
    uow = uow_provider()
    return commands.add_pet(pet_body, uow)


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
