# Use Dependency Inversion

## Status

approved

## Context

Implementing a rest api often involves integrating external services such as databases or caches.
In some cases it's necessary to call other apis to fetch data.
The external dependencies might make unit-testing challenging. In such cases the natural solution is to provide mocks
that simulate the behavior of the external service even without calling it.

There are several approaches to provide the mocks (and the real implementations) to the services, some of the most
used are:

* Direct import and monkey patching
* Dependency injection
* Dependency inversion

Monkey patching is an approach that I don't recommend, please check the [README.md](../../../tests/tests.md) in the
tests folder for more info on that.

Dependency injection requires the use of some technology that provides the dependencies in a "transparent" way and can
be customized so that during testing the mocks are passed instead of the real dependencies. However, sometimes these
technologies can feel like "magic" and hide the way they pass the dependencies to the actual code.

Dependency inversion is a design approach in which the dependencies are explicitly passed from who constructs or invokes
the unit to run/test.

## Decision

I will use the dependency inversion approach, moving away to the previously used dependency injection approach.

## Consequences

The `dependency-injector` package will be removed, the app will be built using a `build_app` function instead of being a
module variable.