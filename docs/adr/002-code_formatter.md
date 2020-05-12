# Use an automated code formatter

## Status

accepted

## Context

When joining a new team, people coming from different environments might be
used to different styles in writing code. 
This might seem trivial and also irrelevant but it actually affects a lot 
the productivity of a team in at least two ways:
1. A developer might write the code in its own style
2. A developer might discuss the code style of another developer  

## Decision

In order to avoid this confusion and to promote a consistent style I propose
to use an automatic code formatter, in this case `black`: https://black.readthedocs.io/

## Consequences

Each developer will write code in its own style with the help of its own 
favourite tool.

Before committing (or integrating black in the tool) the developer will have
to format the code using the `black` command so that the style will be kept consistent.

This can be further enforced using black as a commit pre-hook.