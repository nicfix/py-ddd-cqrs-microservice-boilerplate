# Use pre-commit hooks for code-quality tooling

## Status

accepted

## Context

Adding some tools to the chain might cause developers to forget to run
them at every commit.

## Decision

To prevent this from happening we set-up pre-commit hooks using
python `pre-commit`: https://pre-commit.com/.

This will give us a way to specify our pre-commit hooks as a `.yaml`
 file and version them in the repo without the need of installing hooks in every machine.

## Consequences

As soon as the repository is cloned and the dependencies are installed 
a developer will have to run `pre-commit install` to set up correctly the pre-commit hooks.