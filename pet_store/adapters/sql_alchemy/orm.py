import logging
import uuid

from sqlalchemy import Column, Integer, MetaData, String, Table, orm
from sqlalchemy.exc import ArgumentError

from pet_store.adapters.sql_alchemy.BinaryUUID import BinaryUUID
from pet_store.domain import models

metadata = MetaData()

pets = Table(
    "pets",
    metadata,
    Column("id", BinaryUUID(255), primary_key=True, default=uuid.uuid4),
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


def auto_start_mappers():
    try:
        start_mappers()
        logging.debug("Mappers initialized")
    except ArgumentError:
        logging.debug("Mappers already initialized")


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
