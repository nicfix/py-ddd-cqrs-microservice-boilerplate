from cookiecutter_project_name.command.domain import models
from sqlalchemy import Column, Integer, MetaData, String, Table, orm

metadata = MetaData()

pets = Table(
    "pets",
    metadata,
    Column("id", String(255), primary_key=True),
    Column("name", String(255)),
    Column("age", Integer, nullable=False),
)


def start_mappers():
    pets_mapper = orm.mapper(models.Pet, pets)
    return [pets_mapper]


def create_tables(engine):
    metadata.create_all(engine)


def drop_tables(engine):
    metadata.drop_all(engine)
