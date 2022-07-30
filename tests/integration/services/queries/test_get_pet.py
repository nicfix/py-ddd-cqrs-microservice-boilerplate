import uuid

from pet_store.domain.models import Pet
from pet_store.services import queries
from pet_store.services.dtos import PetDTO
from pet_store.services.queries import NoPetFoundError
from tests.integration.utils import testing_infrastructure
from tests.integration.utils.local_db_test_case import LocalDBTestCase


class GetPetTestCase(LocalDBTestCase):

    def setUp(self) -> None:
        super().setUp()

        self.pet = Pet(
            id=uuid.uuid4(),
            name="Pimi",
            age=2
        )

        self.session.add(self.pet)
        self.session.commit()

    def test_get_pet(self):
        uow = testing_infrastructure.uow_factory()
        pet_dto = queries.get_pet(self.pet.id, uow)

        self.assertIsInstance(pet_dto, PetDTO)
        self.assertEqual(self.pet.id, pet_dto.id)
        self.assertEqual(self.pet.name, pet_dto.name)
        self.assertEqual(self.pet.age, pet_dto.age)

    def test_get_wrong_pet_id_fails(self):
        uow = testing_infrastructure.uow_factory()
        with self.assertRaises(NoPetFoundError):
            queries.get_pet(uuid.uuid4(), uow)
