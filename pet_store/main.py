from pet_store.adapters.sql_alchemy.unit_of_work import SQLAlchemyUnitOfWork
from pet_store.entrypoints.api import build_app
from pet_store.infrastructure.db import get_session

# Initialize a Unit Of Work using the SQLAlchemy session
uow = SQLAlchemyUnitOfWork(get_session)
# Initialize the app that can be used in any asgi compatible webserver (gunicorn, uvicorn etc)
app = build_app(uow)
