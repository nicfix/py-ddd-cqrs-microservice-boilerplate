# py-ddd-cqrs-microservice-boilerplate
[![Actions Status](https://github.com/nicfix/py-ddd-cqrs-microservice-boilerplate/workflows/quality/badge.svg)](https://github.com/nicfix/py-ddd-cqrs-microservice-boilerplate/actions)
[![Actions Status](https://github.com/nicfix/py-ddd-cqrs-microservice-boilerplate/workflows/tests/badge.svg)](https://github.com/nicfix/py-ddd-cqrs-microservice-boilerplate/actions)


A boilerplate for a Domain Driven Design(ed), CQRS based, Microservice in Python

## Documentation

Please refer to the following pages:
* [Architecture](./docs/Architecture.md)
* [Testing](tests/README.md)

## Help
```bash
$ make help
```

## Installation

### In Docker or to run the microservice
```bash
# Install the necessary dev commands
$ make requirements
```

### Development
```bash
# Install the necessary dev commands
$ make pre-commit
```

## Tests
```bash
# Run all the tests
$ make test
```

## Run

### Production
```bash
# Run the server
$ make run
```

### Development
```bash
# Run the server in watch source mode
$ make watch
```

## Useful links:

* http://michal.karzynski.pl/blog/2019/05/26/python-project-maturity-checklist/
* http://cosmicpython.com
