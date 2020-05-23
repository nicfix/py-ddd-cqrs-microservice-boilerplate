import uuid
from unittest import TestCase

from cookiecutter_project_name.command.domain.models import Pet
from tests.unit.mocks import MockRepository


class PetModelTestCase(TestCase):
    def setUp(self) -> None:
        self.pet_id = uuid.uuid4()
        self.pet = Pet(id=self.pet_id, name="Pimienta", age=1)
        self.repo = MockRepository([self.pet])

    def test_get_pet(self) -> None:
        pet = self.repo.get_by_id(self.pet_id)
        self.assertEqual(self.pet, pet)

    def test_add_pet(self) -> None:
        new_pet_id = uuid.uuid4()
        pet = Pet(id=new_pet_id, name="Milù", age=9)

        pet_id = self.repo.add(pet)

        self.assertEqual(new_pet_id, pet_id)

        self.assertTrue(pet in self.repo.pets)
