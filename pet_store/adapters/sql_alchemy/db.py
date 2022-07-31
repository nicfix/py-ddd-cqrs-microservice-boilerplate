from typing import Callable

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session


def get_session_factory(database_uri: str) -> Callable[[], Session]:
    """
    Builds a session factory for the database uri passed as parameter
    :param database_uri: the uri of the database
    :type database_uri: str
    :return: A function that returns a orm session when invoked
    :rtype: Callable[[], Session]
    """
    engine = create_engine(
        database_uri, connect_args={"check_same_thread": False}
    )
    return sessionmaker(autocommit=False, autoflush=False, bind=engine)
