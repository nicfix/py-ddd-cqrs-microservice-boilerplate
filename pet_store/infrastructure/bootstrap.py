from dependency_injector import providers

from pet_store.command.adapters.sql_alchemy.orm import start_mappers
from pet_store.command.adapters.sql_alchemy.repository import session
from pet_store.infrastructure.db import get_session


def bootstrap():
    """
    Initialize all the infrastructure for the app.

    :return:
    """
    # Initialize the ORM
    start_mappers()

    # Configuring the provider for the session
    session.provided_by(providers.Callable(get_session))
