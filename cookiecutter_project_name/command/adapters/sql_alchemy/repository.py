from uuid import UUID

from cookiecutter_project_name.command.adapters.repository import Repository
from cookiecutter_project_name.command.domain.models import Pet
from sqlalchemy import orm


class SQLAlchemyRepository(Repository):
    def __init__(self, session: orm.Session):
        self.session = session

    def get_by_id(self, id: UUID) -> Pet:
        return self.session.query(Pet).filter_by(id=str(id)).one()

    def add(self, pet: Pet) -> UUID:
        self.session.add(pet)
        return pet.id
