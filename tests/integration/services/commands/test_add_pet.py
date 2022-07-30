from pet_store.services import commands
from pet_store.services.commands import AddPetCommand
from pet_store.services.dtos import PetDTO
from tests.integration.utils import testing_infrastructure
from tests.integration.utils.local_db_test_case import LocalDBTestCase


class AddPetTestCase(LocalDBTestCase):

    def test_add_pet(self):
        add_pet_command = AddPetCommand(
            name="Pimi",
            age=2
        )

        uow = testing_infrastructure.uow_factory()
        result = commands.add_pet(dto=add_pet_command, uow=uow)

        self.assertIsInstance(result, PetDTO)
        self.assertEqual(add_pet_command.name, result.name)
        self.assertEqual(add_pet_command.age, result.age)
