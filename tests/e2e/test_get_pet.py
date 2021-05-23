import uuid

from fastapi.testclient import TestClient

from pet_store.domain import models
from pet_store.entrypoints.api import app
from tests.e2e.utils.e2e_test_case import E2ETestCase
from tests.e2e.utils.testing_infrastructure import (
    get_session,
)

pre_populated_pet_id = uuid.uuid4()
pet_data = {"id": str(pre_populated_pet_id), "name": "Pimienta", "age": 1}


class PetTestCase(E2ETestCase):

    @classmethod
    def setUpClass(cls) -> None:
        super().setUpClass()
        session = get_session()
        pet = models.Pet(**pet_data)  # type: ignore
        session.add(pet)
        session.commit()
        session.close()

    def test_get_pets(self):
        client = TestClient(app)

        response = client.get("/pets")
        self.assertEqual(200, response.status_code)
        response_data = response.json()
        self.assertEqual(
            response_data.get("pets", [])[0],
            pet_data,
        )

    def test_get_pet(self):
        client = TestClient(app)

        response = client.get(f"/pets/{pre_populated_pet_id}")
        self.assertEqual(200, response.status_code)
        self.assertEqual(
            response.json(),
            pet_data,
        )
