[architecture.layers]: architecture.layers.jpg "architecture.layers Architecture Layers"
# Architecture

This application follows the architecture suggested in 
the Cosmic Python book: https://www.cosmicpython.com/

The Cosmic Python book provides guidelines to implement
a good DDD architecture in python.

The architecture of this project is **NOT** based on:
* the Active Record pattern (Django like)
* Exagonal Architecture (even though similarities can be found)
* Clean Architecture (even though similarities can be found)

Please refer to the book's [preface](https://www.cosmicpython.com/book/preface.html) 
to check how this architecture relates to the ones I mentioned before.

## Architecture Decision Record

This project includes a folder of [Architecture Decision Records](https://adr.github.io/),
check it out [here](./adr/000-ADR.md).

## Layers
![Architecture Layers][architecture.layers]

The responsibilities in this API can be assigned to layers:
* Domain (`domain` module)
* Adapters (`adapters` module)
* Service Layer (`service_layer` module)
* Entrypoints (`entrypoints` module)


### Domain
This layer implements the Ubiquitous Language specific to our Domain.
In this module are included only Pure python classes and functions that aim to have
no infrastructure dependencies (frameworks, persistence, data transfer etc).

This layer has to remain portable to any other python project and testable as 
a unit.

The layer is further divided in 2 modules:
* `models`, including the classes that implement DDD's Entities and ValueObjects
* `service_functions`, including the functional implementation of Domain relative operations.

Please check the paragraph "Not Everything Has to Be an Object: A Domain Service Function" from the
[Cosmic Python's 1st chapter](https://www.cosmicpython.com/book/chapter_01_domain_model.html)

Best quote:
> Sometimes, it just isn’t a thing. — Eric Evans, Domain-Driven Design

Please check the [Domain](../domain/docs/README.md) documentation page for more details. 


# Adapters
The Adapters implement the "adaptation" to the foundation/backing services.
As a pattern they implement the following:
* An interface that has to be used by all the clients, unaware of technological details
* A concrete implementation on top of a specific technology

The goal is to provide an easy to swap set of adaptation objects to protect
the code from changes in technological choices.
 
The Adapters layer includes the Repository classes. 
A Repository is a simplifying abstraction over data storage, 
allowing us to decouple our model layer from the data layer.

The repositories in this layer are implemented using the Adapter pattern.

Please check the paragraph "Repository Pattern" from the
[Cosmic Python's 2nd chapter](https://www.cosmicpython.com/book/chapter_02_repository.html)



# Service Layer
The Service Layer uses the Adapters and the Domain to implement services used outside.
The Services functions/classes implement a contract with external clients. Potentially only
tests against the ServiceLayer surface (interface) should be granted since the internal implementation
details of the domain model should remain hidden to external clients.

You can consider the services at the same level of the UseCases of the Exagonal Architecture/Clean Architecture.

Their interface should never expose domain objects outside and should not accept them as parameters.
Their interface should allow the injection of Repositories using the Dependency Inversion principle (SOLID).

For this reason all the services implemented in this project accept/expose DTOs (Data Transfer Objects) that
are not the domain objects, the structure of these objects is part of the "contract" of the service layer.


# Entrypoints

> Entrypoints are the places we drive our application from. In the official ports and adapters terminology, 
> these are adapters too, and are referred to as primary, driving, or outward-facing adapters.

The Entrypoints is the layer (and the only one) that is dependent from technological choices related
to the web technology one might want to choose.
In a well implemented DDD architecture, all the technological choices are taken in the adapters/entrypoints
layers.

Some technologies might be used in the service layer to facilitate serialization/deserialization and
validation (pydantinc to implement the DTOs in our case).

No technological dependencies are added to the domain layer. Pure classes/functions implemented
using language functionalities as much as possible

In this project we provide one entrypoint in the form of a web application server implemented 
with FastAPI.
