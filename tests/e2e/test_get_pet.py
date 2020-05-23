from unittest import TestCase

from cookiecutter_project_name.command.adapters.sql_alchemy.orm import (
    create_tables,
    drop_tables,
)
from cookiecutter_project_name.command.domain import models
from cookiecutter_project_name.entrypoints.api import app
from cookiecutter_project_name.infrastructure.db import get_engine, get_session
from fastapi.testclient import TestClient

engine = get_engine()
pre_populated_pet_id = "7e33cedf-56ee-4706-ac16-944cef1c9930"
pet_data = {"id": "7e33cedf-56ee-4706-ac16-944cef1c9930", "name": "pimi", "age": 1}


class PetTestCase(TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        # This has to happen in Alembic

        create_tables(engine)

        session = get_session()

        pet = models.Pet(**pet_data)
        session.add(pet)
        session.commit()

    @classmethod
    def tearDownClass(cls) -> None:
        drop_tables(engine)

    def test_get_pet(self):
        client = TestClient(app)

        response = client.get("/pets/7e33cedf-56ee-4706-ac16-944cef1c9930")
        self.assertEqual(200, response.status_code)
        self.assertEqual(
            response.json(), pet_data,
        )
