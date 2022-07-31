from pet_store.adapters.sql_alchemy.db import get_session_factory
from pet_store.adapters.sql_alchemy.unit_of_work import SQLAlchemyUnitOfWork
from pet_store.config import SQLALCHEMY_DATABASE_URL, ORIGINS
from pet_store.entrypoints.api import build_app

# Initialize a Unit Of Work using the SQLAlchemy session
uow = SQLAlchemyUnitOfWork(session_factory=get_session_factory(SQLALCHEMY_DATABASE_URL))

# Initialize the app that can be used in any asgi compatible webserver (gunicorn, uvicorn etc)
app = build_app(
    uow=uow,
    origins=ORIGINS
)
