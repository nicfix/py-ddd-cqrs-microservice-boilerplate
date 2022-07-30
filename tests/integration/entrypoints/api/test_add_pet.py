from fastapi.testclient import TestClient

from pet_store.entrypoints.api import app
from tests.integration.utils.local_db_test_case import LocalDBTestCase


class PetTestCase(LocalDBTestCase):

    def test_add_pet(self):
        client = TestClient(app)

        body = {
            'age': 12,
            'name': 'Milú'
        }

        response = client.post('/pets', json=body)

        pet_json = response.json()

        self.assertEqual({
            'age': pet_json.get('age', None),
            'name': pet_json.get('name', None)
        }, body)

        self.assertIsNotNone(pet_json.get('id', None))
