import uuid

from pet_store.domain.models import Pet
from pet_store.services import queries
from pet_store.services.dtos import PetsPageDTO
from tests.integration.utils import testing_infrastructure
from tests.integration.utils.local_db_test_case import LocalDBTestCase


class GetPetsTestCase(LocalDBTestCase):

    def setUp(self) -> None:
        super().setUp()

        self.pets = [
            Pet(
                id=uuid.uuid4(),
                name="Pimi",
                age=2
            ),
            Pet(
                id=uuid.uuid4(),
                name="Milu",
                age=12
            ),
        ]

        self.session.add_all(self.pets)
        self.session.commit()

    def test_get_pet(self):
        uow = testing_infrastructure.uow_factory()
        pets_dto = queries.get_pets(uow=uow)

        self.assertIsInstance(pets_dto, PetsPageDTO)
        pets_in_dto = pets_dto.pets
        for idx, pet in enumerate(self.pets):
            self.assertEqual(pet.id, pets_in_dto[idx].id)
            self.assertEqual(pet.name, pets_in_dto[idx].name)
            self.assertEqual(pet.age, pets_in_dto[idx].age)
