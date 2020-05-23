from unittest import TestCase

from fastapi.testclient import TestClient

from cookiecutter_project_name.entrypoints.api import app


class HealthyTestCase(TestCase):
    def test_get_healthy(self):
        client = TestClient(app)

        response = client.get("/healthy")
        self.assertEqual(200, response.status_code)
        self.assertEqual(response.json(), {"status": "ok"})


class ReadyTestCase(TestCase):
    def test_get_ready(self):
        client = TestClient(app)

        response = client.get("/ready")
        self.assertEqual(200, response.status_code)
        self.assertEqual(response.json(), {"status": "ready"})
