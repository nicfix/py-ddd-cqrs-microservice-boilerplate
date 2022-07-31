# Implement liveliness, readiness and startup probes

## Status

approved

## Context

Cloud providers often rely on the usage of Orchestration systems
over a containerization technology.

The orchestration system needs to know at least 2 things about any service:

* If the service started correctly after a deployment
* If the service is still healthy at any moment in time

## Decision

When implementing an API that has to be deployed on the cloud,
implement the following endpoints:

* `/ready` an endpoint that returns a 200 - OK if the service is ready to
  accept requests after a new deployment
* `/health` an endpoint that returns a 200 - OK if the service is still alive
  and functioning correctly

## Consequences

Thanks to this 2 endpoints is possible to deterministically and automatically
detect problems both after a new deployment and during the normal operation
of the service directly into the orchestration service.

Check out this page for more info regarding how `kubernetes` can be configured
for
this https://kubernetes.io/docs/tasks/configure-pod-container/configure-liveness-readiness-startup-probes/#define-a-liveness-http-request
