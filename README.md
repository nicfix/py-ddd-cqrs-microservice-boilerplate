# py-ddd-microservice-boilerplate
A boilerplate for a Domain Driven Design(ed) Microservice in Python


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

# Install the pre-commit hooks, check .pre-commit-config.yaml
$ pre-commit install
```

## Tooling

### Run tests
```bash
$ pytest --cov-config=.coveragerc --cov=. batch_allocation/
```

### Format code
```bash
$ black ./batch_allocation
```

### Linter
```bash
$ flake8 ./batch_allocation
```



## Useful links:

* http://michal.karzynski.pl/blog/2019/05/26/python-project-maturity-checklist/
* http://cosmicpython.com



## Documentation

Please refer to the following pages (included in each module):
* [Architecture](./docs/Architecture.md)
* [Testing](tests/README.md)