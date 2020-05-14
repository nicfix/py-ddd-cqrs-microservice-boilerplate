# Responsibilities
This page contains a brief description of each main class from this architecture

#### ValueObject `domain`
A domain model object that doesn't have an identity.

#### Entity `domain`
A domain model object that has an identity.

#### Aggregate `domain`
A domain model object that:
* has an entity
* defines a consistency boundary
* aggregates all the other domain entities for this bounded context

Only one Repository per Aggregate exists.

#### Event `domain`
A domain object that represents an event happened or going to happen on a domain object.

#### Command `domain`
A special kind of event that represents a request for a modification on a domain object.

#### Repository `adapters`
Retrieves and stores aggregates from and to the persistence technology.

#### Event Handlers `service_layer`
Handle one specific event as part of a single distinct unit of work.

#### Unit of Work `service_layer`
Creates a session/consistency context for modification operations on domain aggregates.

#### Message Bus `service_layer`
Dispatches events to events handlers, collects new events and returns results

#### Entry Point `entrypoints`
A client of the message bus. Receives external inputs and converts them into Events or 
Commands to be handled by the message bus.