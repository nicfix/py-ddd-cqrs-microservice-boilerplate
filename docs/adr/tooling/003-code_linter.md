# Use an automated code linter

## Status

accepted

## Context

When joining a new team, people coming from different environments might be
used to different styles in writing code. 
This might seem trivial and also irrelevant but it actually affects a lot 
the productivity of a team in at least two ways:
1. A developer might write the code in its own style
2. A developer might discuss the code style of another developer  

Furthermore, some practices might be considered good in one team while being
considered bad in another team.

This creates an awkward situation in which some developers try to correct these bad
practices in PRs without really succeding but increasing the level of frustration of 
their colleagues.

## Decision

Proceed as follows:
* define a set of rules that are considered good or bad practices,
* discuss and agree on the minimum amount of rules at team level, 
* let an automatic linter block every commit in a pre-commit hook

Use `flake8`: https://flake8.pycqa.org/ for python.

## Consequences

The linter will act as a cold rules checker,
no more developers and hard feelings in enforcing the rules.
At the same time, running it at a pre-commit-hook will make sure
that code that is not compliant will not reach the repo at all.

# References
* https://adr.github.io/
* https://github.com/joelparkerhenderson/architecture_decision_record