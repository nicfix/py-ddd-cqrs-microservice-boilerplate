# py-ddd-cqrs-microservice-boilerplate

[![API Quality](https://github.com/nicfix/py-ddd-cqrs-microservice-boilerplate/actions/workflows/qualityChecks.yml/badge.svg)](https://github.com/nicfix/py-ddd-cqrs-microservice-boilerplate/actions/workflows/qualityChecks.yml)

A boilerplate for a Domain Driven Design(ed), CQRS based, Microservice in Python

## Installation

### In Docker or to run the microservice

```
# Install the necessary dev commands
$ pip install -r requirements.txt
```

### Development

```
# Install the necessary dev commands
$ pip install -r requirements-dev.txt
$ pre-commit install
```

## Start development server

```bash
$ python run.py watch
```

## Run tests

```bash
$ python run.py test
```

## Other commands

Check out the help manual

```bash
$ python run.py --help
```

## Useful links:

* http://michal.karzynski.pl/blog/2019/05/26/python-project-maturity-checklist/
* http://cosmicpython.com

## Documentation

Please refer to the following pages (included in each module):

* [Architecture](./docs/Architecture.md)
* [Testing](tests/tests.md)
