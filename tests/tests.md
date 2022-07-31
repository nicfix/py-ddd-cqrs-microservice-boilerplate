# Tests

## Organization
The tests are organized in 3 groups:
* E2E tests `tests.e2e`
* Integration tests `tests.integration`
* Unit tests `tests.unit`


### Context
Given the definition for the following as in the Cosmic Python book (see [Architecture](../docs/Architecture.md)):
* entrypoints  (Web Server, CLI Tool, Messaging Job)
* adapters (Database, caching system, external service mock)

We follow the guidelines of the [Cosmic Python book](https://www.cosmicpython.com/book/chapter_05_high_gear_low_gear.html#kinds_of_tests).

### E2E tests
**Definition**: We define an e2e test as a test that executes code from all the "ends".
In particular, requesting an operation from one entrypoint and reaching a concrete adapter.

We aim to test the critical paths of the system looking at it as a black box.

Example:

Test --HTTP--> Entrypoint (Webserver App) -- ... --> Adapter (Repository) --> Testing/Local Database

### Integration tests
**Definition**: We define an integration test a test that executes a unit integrated
in the system. In particular, invoking a method of a unit which uses one of the adapters.

Example: 

Test --Direct Invocation--> Class method/function --...--> Adapter (Repository) --> Testing/Local Database

### Unit tests
**Definition**: We define a unit test a test test executes a unit mocking all the 
other adapters (if needed).

Example: 

Test --Direct Invocation--> Class method/function --...--> MockedAdapter (MockedRepository)


## Mocks Versus Fakes; Classic-Style Versus London-School TDD
In this project we prefer the Classic-Style: 
> We like to build our tests around state both in setup and in assertions, 
> and we like to work at the highest level of abstraction possible rather 
> than doing checks on the behavior of intermediary collaborators.

Quoting the [Cosmic Python Book](https://www.cosmicpython.com/book/chapter_03_abstractions.html#_why_not_just_patch_it_out):
> We avoid using `mocks` in this book and in our production code too. 
> 
> We’re not going to enter into a Holy War, but our instinct is that mocking frameworks, particularly monkeypatching, are a code smell.
> 
> Instead, we like to clearly identify the responsibilities in our codebase, and to separate those responsibilities into small, 
> focused objectsrequirements that are easy to replace with a test double.