from fastapi.testclient import TestClient

from tests.integration.utils.local_db_test_case import LocalDBTestCase


class HealthyTestCase(LocalDBTestCase):
    def test_get_healthy(self):
        client = TestClient(self.app)

        response = client.get("/healthy")
        self.assertEqual(200, response.status_code)
        self.assertEqual(response.json(), {"status": "ok"})


class ReadyTestCase(LocalDBTestCase):
    def test_get_ready(self):
        client = TestClient(self.app)

        response = client.get("/ready")
        self.assertEqual(200, response.status_code)
        self.assertEqual(response.json(), {"status": "ready"})
