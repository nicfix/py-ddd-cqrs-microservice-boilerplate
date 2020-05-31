# Fast API as Rest API framework

# Status

approved

# Context

Python provides several frameworks to develop RESTful APIs.
All of them have their pro and cons and fit different scenarios.

In this project we have the following functional requirements:
* we want to build a REST API
* we don't need templating or HTML rendering features
* we need an OpenAPI specification exposed from the API
* we need a validation framework for input data
* we need a serialization framework for output data
* **OPT** we need an automated mechanism to keep in sync the OpenAPI spec with
the implementation

In this project we have the following non-functional requirements:
* we need a small memory consumption, in this way we can replicate
the api in several containers
* **OPT** we need support for asynchronous handling of HTTP requests,
in this way we can reduce the number of replicas in high I/O bound 
performance scenarios 



# Solution

Use FastAPI as a REST framework.
> FastAPI is a modern, fast (high-performance), 
> web framework for building APIs with Python 3.6+ 
> based on standard Python type hints.
> - [Pydantic Website](https://fastapi.tiangolo.com/)

It checks all the functional and non-functional requirements. 

Furthermore:
* uses the python `typing` module to implement validation
* supports the Pydantic Models to implement validation
* supports the Pydantic Models to implement serialization
* uses the pythondocs and the Pydantic models to automatically generate
the OpenAPI specification and the Swagger-UI/Redoc sites. 

Is developed on top of Starlette which is developed from the creators
of `django-rest-framework` and adds the support for a `typing` based
web development leveraging on `pydantic` Models.

# Consequences

FastAPI is based on the ASGI (Asynchronous Standard Gateway Interface).
FastAPI provides an application object that can be used by any ASGI compatible
webservers. An ASGI compatible webserver has to be choosen to run FastAPI apps.

Another consequence of choosing FastAPI is the suggestion to use `pydantic` as 
Data Transfer Objects framework so that the integration will be natural and will
also generate documentation that will be up-to-date with the current implementation.