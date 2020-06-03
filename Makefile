.PHONY: help requirements requirements-dev lint test run security licenses image

APP := pet_store
WORKON_HOME ?= .venv
VENV_BASE := $(WORKON_HOME)/${APP}
VENV_ACTIVATE := $(VENV_BASE)/bin/activate
PYTHON := ${VENV_BASE}/bin/python3

CONTAINER_CMD?=docker

IMAGE_NAME ?= nicfix/$(APP)
IMAGE_VERSION ?= latest

.DEFAULT: help
help:
	@fgrep -h "##" $(MAKEFILE_LIST) | fgrep -v fgrep | sed -e 's/\\$$//' | sed -e 's/##/\n\t/'

venv:	## create virtualenv
	@if [ ! -d "$(VENV_BASE)" ]; then \
		virtualenv -p python3 $(VENV_BASE); \
	fi

requirements:	## install requirements
requirements: venv
	@echo Install requirements
	@${PYTHON} -m pip install -r requirements.txt > /dev/null

requirements-dev:   ## install dev requirements
requirements-dev: venv
	@echo Install dev requirements
	@${PYTHON} -m pip install -r requirements-dev.txt

pre-commit:	## install the pre-commit hooks, check .pre-commit-config.yaml
pre-commit: requirements-dev
	@pre-commit install

format-code:	## use black to format code
	@${PYTHON} -m black ${APP}

lint:	## run pycodestyle
lint: requirements-dev
	@echo Running linter
	@${PYTHON} -m pycodestyle .
	@${PYTHON} -m flake8 ${APP}
	@${PYTHON} -m mypy --ignore-missing-imports ${APP} tests

security:	## run bandit
security: requirements-dev
	@echo Running security checks
	@${PYTHON} -m bandit ${APP}

licenses:   ## run pip-licenses
licenses: requirements-dev
	@echo Running pip-licenses
	@pip-licenses --summary --from=classifier --with-system --order=count

test:	## run tests and show report
test: lint
	@echo Running tests
	@LOG_LEVEL=DEBUG ${PYTHON} -m coverage run -m pytest tests
	@${PYTHON} -m coverage report -m

watch:	## run project in live reload
watch: requirements
	@${PYTHON} -m uvicorn ${APP}.entrypoints.api:app --reload

run:	## run project
run: requirements
	@${PYTHON} -m uvicorn ${APP}.entrypoints.api:app

image:	## build docker image
image:
	$(CONTAINER_CMD) build -t $(IMAGE_NAME):$(IMAGE_VERSION) .
