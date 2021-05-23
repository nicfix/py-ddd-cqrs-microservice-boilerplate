from unittest import TestCase

from dependency_injector import providers

from pet_store.services.unit_of_work import uow_provider
from tests.e2e.utils.testing_infrastructure import (
    get_session,
    destroy_testing_db,
    create_testing_db,
    uow_factory,
)

# Changing the UnitOfWorkFactory using the dependency_injector library
uow_provider.override(providers.Callable(uow_factory))


class E2ETestCase(TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        # This has to happen in Alembic
        create_testing_db()

    @classmethod
    def tearDownClass(cls) -> None:
        destroy_testing_db()

    def setUp(self) -> None:
        self.session = get_session()
