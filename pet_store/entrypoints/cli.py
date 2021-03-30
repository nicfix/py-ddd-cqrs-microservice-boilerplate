import invoke
import uvicorn
from invoke import UnexpectedExit


class CLI(object):
    def test_coverage(self):
        """
        Runs the tests and calculates the coverage.
        """
        try:
            invoke.run("coverage run --source=food_planner,account,api -m pytest -qq")
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
            host="0.0.0.0",
            port=8081,
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


cli = CLI()
