# Use an automated license checker

## Status

proposed

## Context

Working with OpenSource software for commercial purposes requires
every developer to check the licenses of the packages that he uses.

Some licenses might be not-compatible with the project needs and
cause some legal issue if not properly handled.

Using open-source libraries speeds up development in a 
significant way but has a drawback, nested dependencies.

Each open-source library could depend on further open-source libraries
that could have different licenses for usage and re-distribution.

## Decision

Given the previous concerns I suggest to use an automated
licenses checker on the installed packages.

In python you can use `pip-licenses` (which is distributed with MIT license)


## Consequences

Anytime a new library is added to the project a developer
can verify if a new/conflicting license has been added with that
library or with a nested dependency.

This allows the developer to take counter measures that can vary
from mentioning the library in the list of open source technologies 
or deciding to not use that library at all.