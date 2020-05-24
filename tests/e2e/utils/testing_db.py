import os

from sqlalchemy import create_engine, orm
from sqlalchemy.orm import sessionmaker

from pet_store.command.adapters.sql_alchemy.orm import create_tables, drop_tables

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


def create_testing_db():
    # This has to happen in Alembic
    create_tables(engine)


def destroy_testing_db():
    drop_tables(engine)
    os.remove(SQLITE_FILE_PATH)
