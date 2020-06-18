import uuid
from unittest import TestCase

from dependency_injector import providers
from fastapi.testclient import TestClient

from pet_store.domain import models
from pet_store.entrypoints.api import app
from pet_store.services.unit_of_work import uow_provider
from tests.e2e.utils.testing_infrastructure import (
    get_session,
    destroy_testing_db,
    create_testing_db,
    uow_factory,
)

# Changing the UnitOfWorkFactory using the dependency_injector library
uow_provider.override(providers.Callable(uow_factory))

pre_populated_pet_id = uuid.uuid4()
pet_data = {"id": str(pre_populated_pet_id), "name": "Pimienta", "age": 1}


class PetTestCase(TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        # This has to happen in Alembic
        create_testing_db()
        session = get_session()
        pet = models.Pet(**pet_data)  # type: ignore
        session.add(pet)
        session.commit()
        session.close()

    @classmethod
    def tearDownClass(cls) -> None:
        destroy_testing_db()

    def test_get_pets(self):
        client = TestClient(app)

        response = client.get("/pets")
        self.assertEqual(200, response.status_code)
        response_data = response.json()
        self.assertEqual(
            response_data.get("pets", [])[0], pet_data,
        )

    def test_get_pet(self):
        client = TestClient(app)

        response = client.get(f"/pets/{pre_populated_pet_id}")
        self.assertEqual(200, response.status_code)
        self.assertEqual(
            response.json(), pet_data,
        )
