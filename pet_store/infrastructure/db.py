from sqlalchemy import create_engine, orm
from sqlalchemy.orm import sessionmaker

from pet_store.infrastructure.config import SQLALCHEMY_DATABASE_URL

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
