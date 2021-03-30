import invoke
import uvicorn
from invoke import UnexpectedExit


def test_coverage():
    invoke.run("coverage run --source=food_planner,account,api -m pytest -qq")
    invoke.run("coverage report --fail-under=70")


def test():
    try:
        invoke.run("pytest")
    except UnexpectedExit as e:
        print("Tests failed.")
        exit(e.result.exited)


def lint():
    try:
        invoke.run("flake8")
        print("Done.")
    except UnexpectedExit as e:
        print("Flake 8 failed.")
        exit(e.result.exited)


def watch():
    uvicorn.run(
        "pet_store.entrypoints.api:app",
        host="0.0.0.0",
        port=8081,
        log_level="debug",
        reload=True,
    )


def format():
    invoke.run("black food_planner")


def dev_setup():
    invoke.run("pip install -r requirements-dev.txt")
    invoke.run("pre-commit install")
