from cookiecutter_project_name.command.adapters.sql_alchemy.orm import start_mappers


def bootstrap():
    """
    Initialize all the infrastructure for the app.

    :return:
    """
    # Initialize the ORM
    start_mappers()
