from pet_store.domain import models
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
    """
    Initialize the mapping between tables and models.

    :return:
    """
    pets_mapper = orm.mapper(models.Pet, pets)
    return [pets_mapper]


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
