from starlette.testclient import TestClient

from pet_store.entrypoints.api import app
from tests.e2e.utils.e2e_test_case import E2ETestCase


class PetTestCase(E2ETestCase):

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
