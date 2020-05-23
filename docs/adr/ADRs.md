# Architectural Decision Record

## Status

approved

## Context

Design decisions tend to be forgotten during the course of a project.
At any point in time new developers will need a place to describe problems, 
propose solutions, take decisions and evaluate consequences.

Technical decisions evolve over time due to many reasons. Change of requirements,
deprecation of technologies, new approaches are only some of the drivers for a technical
change.

Wherever a change is needed or not the first thing to asses 
is the status quo to understand how to move from the current 
situation to the new one.

Is not unusual for software project to have technologies and design decisions that have
been forgotten and cannot be explained.

## Decision

For every relevant design decision create an Architectural Decision Record, 
add it to the code repository, and version it using the same version control
system utilized by the codebase.

## Consequences

This approach has several advantages:
* The documentation is always close to the code
* Anyone can create an ADR without the need of particular tooling
* The ADRs can be implemented using the `markdown` syntax with all the advantages connected
(rendering in github, possibility to generate websites etc.)
* The ADRs are versioned together with the code so it's possible to track back when a decision
has been added/modified/removed.
