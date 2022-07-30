from unittest import TestCase

from dependency_injector import providers

from pet_store.adapters.sql_alchemy.orm import auto_start_mappers
from pet_store.services.unit_of_work import uow_provider
from tests.integration.utils.testing_infrastructure import (
    get_session,
    destroy_testing_db,
    create_testing_db,
    uow_factory,
)

# TODO: Remove together with dependency_injector
# Changing the UnitOfWorkFactory using the dependency_injector library
uow_provider.override(providers.Callable(uow_factory))


class LocalDBTestCase(TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        # This has to happen in Alembic
        create_testing_db()
        auto_start_mappers()

    @classmethod
    def tearDownClass(cls) -> None:
        destroy_testing_db()

    def setUp(self) -> None:
        self.session = get_session()
