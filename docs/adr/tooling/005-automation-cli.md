# Automate all the commands through a unique CLI

## Status

proposed

## Context

It might be challenging to document and rememeber all teh commands
needed for tooling.

Continuous Integration toolchains require entrypoints that are
reliable for executing the different steps in the pipeline.

Many languages offer a CLI definition mechanism, often integrated in the
package manager, as example `npm` through `package.json` files for NodeJS/Typescript.

Sadly in python the scenario is more rarefied.

Promising options are tool like:
* `tox` - https://tox.readthedocs.io/
* `poetry` - https://python-poetry.org/docs/

However they don't allow (natively) to expose commands for running your application
and for administrative commands.

Following the [12 Factors](https://12factor.net/admin-processes) it would be beneficial to have a single cli interface
including all the needed command. 

## Decision

1. Use a single automation tool to expose a consistent CLI for your service
2. In lack of a better option, use `make`

Make is really popular and relatively simply.
However `make` is not Windows friendly and is another dependency needed in the 
developer's machine.


## Consequences

* Define and document the commands the application exposes in a single CLI
* Implement every new command adding it in the CLI
* Make sure that the Continuous Integration pipeline uses the very same commands