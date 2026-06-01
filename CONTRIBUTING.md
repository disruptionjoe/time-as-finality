# Contributing

Time as Finality is designed to be broken, clarified, or formalized claim by claim.

## Best Ways To Help

- Open an issue challenging a claim.
- Add a toy model under `tests/`.
- Add a literature note under `literature/`.
- Tighten definitions in `GLOSSARY.md`.
- Add failure conditions to a claim file.
- Propose a weaker but more defensible version of a claim.

## Contribution Standards

Good contributions:

- distinguish core claims from speculation;
- preserve known physics constraints;
- name what would falsify or weaken a claim;
- cite prior work when possible;
- avoid claiming that human belief creates physical reality;
- avoid treating analogy as proof.

## Claim File Shape

```md
# ID: Claim Title

## Claim

## Class

## Status

## What This Does Not Claim

## Why It Might Be True

## How It Could Fail

## Tests

## Known Neighbors

## Contribution Needed
```

## Test File Shape

```md
# T#: Test Name

## Target Claims

## Setup

## Success Criteria

## Failure Criteria

## Known Physics Constraints

## Contribution Needed
```
