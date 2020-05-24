from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

SQLALCHEMY_DATABASE_URL = "sqlite:///./sql_app.db"
# SQLALCHEMY_DATABASE_URL = "postgresql://user:password@postgresserver/db"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)
session_factory = sessionmaker(autocommit=False, autoflush=False, bind=engine)


def get_engine():
    """
    Return the SQLAlchemy db engine.

    :return:
    """
    return engine


def get_session():
    """
    Return the SQLAlchemy session.

    :return:
    """
    return session_factory()
