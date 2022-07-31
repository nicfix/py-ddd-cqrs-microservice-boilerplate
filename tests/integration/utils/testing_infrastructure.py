import os

from sqlalchemy import create_engine, orm
from sqlalchemy.orm import sessionmaker

from pet_store.adapters.sql_alchemy.orm import metadata
from pet_store.adapters.sql_alchemy.unit_of_work import SQLAlchemyUnitOfWork
from pet_store.services.unit_of_work import UnitOfWork

SQLITE_FILE_PATH = "./testing_sql_app.db"

SQLALCHEMY_DATABASE_URL = f"sqlite:///{SQLITE_FILE_PATH}"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)
session_factory = sessionmaker(autocommit=False, autoflush=False, bind=engine)


def get_session() -> orm.Session:
    """
    Return the SQLAlchemy session.

    :return:
    """
    return session_factory()


def get_engine():
    """
    Return the SQLAlchemy db engine.

    :return:
    """
    return engine


def create_tables(engine):
    """
    Create the tables in the database!

    :param engine:
    :return:
    """
    metadata.create_all(engine)


def drop_tables(engine):
    """
    Drop the tables in the database!

    :param engine:
    :return:
    """
    metadata.drop_all(engine)


def create_testing_db():
    # This has to happen in Alembic
    create_tables(engine)


def destroy_testing_db():
    drop_tables(engine)
    os.remove(SQLITE_FILE_PATH)


def uow_factory() -> UnitOfWork:
    return SQLAlchemyUnitOfWork(get_session)
