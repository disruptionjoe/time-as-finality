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

## Agent-Driven Exploration Protocol

Use this protocol for underexplored open problems, long-horizon hypotheses,
and cross-cutting research patterns that are too broad for one linear pass.
It is especially appropriate when the repo needs to convert intuition into
candidate tests, audits, or clean demotions without promoting claims.

1. Launch one read-only subagent per goal. Each goal should name the relevant
   claim, hypothesis, open problem, and existing tests or reports.
2. Require each subagent to return only:
   - a refined goal statement;
   - a best-next-artifact proposal with a working title and candidate filename;
   - key tests with success, failure, and demotion criteria;
   - links to relevant existing repo artifacts;
   - immediate blockers or negative results.
3. Run one synthesis pass after the independent outputs. The synthesis should
   identify the strongest executable next artifacts, guardrails, priority
   order, and any numbering or registry conflicts.
4. Route outcomes conservatively:
   - `tests/` for executable artifacts;
   - `open-problems/` for theorem targets not yet earned;
   - `explorations/` or technical reports for synthesis and audits;
   - `ROADMAP.md` for priority sequence only;
   - `CLAIM-LEDGER.md` only after an artifact runs and earns a claim update.
5. Treat proposed T-numbers as placeholders until checked against `TESTS.md`
   and `tests/`. Do not reuse an existing number.

Promotion gates:

- No new claim from subagent synthesis alone.
- No physics, geometry, consciousness, or novelty upgrade until the proposed
  artifact runs and yields a narrow theorem, separation, or falsifying result.
- Preserve negative results and demotions as first-class progress.
- Keep the recurring-structure map active: separate known mechanisms from the
  repo's possible contribution before naming novelty.
- Promotion is agent-owned once these gates are met — it does not pause for Joe.
  A hard promotion (raising a claim into the `theorem_backed` tier of the Canon
  Index, or asserting a top-line claim as proven/resolved) files an evidence-trail
  awareness note in `CapacityOS/mailboxes/joeops/` using
  `templates/hard-promotion-joeops-notice.md`: what was promoted, the case FOR, the
  steelmanned case AGAINST, how the call was made, risks, supporting
  artifacts/certificates, and how to reverse. Awareness, not approval.
- The one hard barrier is external publication: nothing enters `papers/published/`
  until Joe publishes externally.

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
