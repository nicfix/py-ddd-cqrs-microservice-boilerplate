import invoke
import uvicorn
from invoke import UnexpectedExit


class CLI(object):
    def test_coverage(self):
        """
        Runs the tests and calculates the coverage.
        """
        try:
            invoke.run("coverage run --source=pet_store -m pytest -qq")
            invoke.run("coverage report --fail-under=70")
        except UnexpectedExit as e:
            print("Coverage failed.")
            exit(e.result.exited)

    def test(self):
        """
        Runs the tests using pytest.
        """
        try:
            invoke.run("pytest")
        except UnexpectedExit as e:
            print("Tests failed.")
            exit(e.result.exited)

    def lint(self):
        """
        Checks the code for the correct style using flake8
        """
        try:
            invoke.run("flake8")
            print("Done.")
        except UnexpectedExit as e:
            print("Flake 8 failed.")
            exit(e.result.exited)

    def watch(self):
        """
        Runs your API using uvicorn in watch mode.
        USE ONLY IN DEVELOPMENT.
        """
        uvicorn.run(
            "pet_store.entrypoints.api:app",
            port=8000,
            host="0.0.0.0",  # nosec
            log_level="debug",
            reload=True,
        )

    def format(self):
        """
        Formats the code using black
        """
        invoke.run("black pet_store")

    def dev_setup(self):
        """
        Installs all the development dependencies and the pre-commit hooks.
        """
        invoke.run("pip install -r requirements-dev.txt")
        invoke.run("pre-commit install")

    def check_dependencies_vulnerabilities(self):
        """
        Checks all the dependencies for known vulnerabilities
        """
        invoke.run("pip install -r requirements-dev.txt")
        invoke.run("safety check")

    def check_vulnerabilities(self):
        """
        Checks all the dependencies for known vulnerabilities
        """
        invoke.run("pip install -r requirements-dev.txt")
        invoke.run("bandit -r pet_store")

    def migrate_database(self):
        invoke.run("pip install -r requirements-dev.txt")
        invoke.run("alembic upgrade head")

    def autogenerate_migrations(self, comment: str):
        invoke.run("pip install -r requirements-dev.txt")
        invoke.run(f'alembic revision --autogenerate -m "{comment}"')


cli = CLI()
