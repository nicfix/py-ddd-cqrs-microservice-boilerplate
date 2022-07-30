from unittest import TestCase

from pet_store.adapters.sql_alchemy.orm import auto_start_mappers
from pet_store.entrypoints.api import build_app
from pet_store.adapters.sql_alchemy.unit_of_work import SQLAlchemyUnitOfWork
from tests.integration.utils.testing_infrastructure import (
    get_session,
    destroy_testing_db,
    create_testing_db,
)


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
        self.uow = SQLAlchemyUnitOfWork(get_session)
        self.app = build_app(uow=self.uow)
