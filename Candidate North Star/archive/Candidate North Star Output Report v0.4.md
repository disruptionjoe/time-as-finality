# Candidate North Star Output Report v0.4

## Status

Output report for:

```text
Candidate North Star v0.4.md
```

This is not canon.
It does not promote the candidate.
It does not replace `NORTH-STAR.md`.

## What Changed From v0.3

v0.4 turns v0.3's broad synthesis into a compact audit specification.

Major changes:

- added exact capability-sufficiency and capability-insufficiency definitions;
- added the factorization iff fiber-constancy lemma;
- added minimal capability-preserving quotient;
- added trivial enrichment theorem;
- added capability spread over projection fibers;
- added `projection_underdescribed`;
- sharpened `canonical_residue` versus `formal_residue`;
- added success and failure criteria;
- added a compact reviewer checklist;
- added no-free-physics rule, physical access-profile requirement, and
  gauge/relabeling invariance audit;
- moved long domain inventories into companion-report posture.

## Main Decision

v0.4 is intentionally shorter and more reviewable than v0.3.

The main note now asks:

```text
What is K?
What equivalence is being used?
Does Cap factor through pi?
Which prior art absorbs the result?
What residue, if any, remains?
```

## Fresh-Eyes Review Integration

A fresh-eye review accepted the compression and posture, and recommended one
important mathematical cleanup:

```text
visible-state equivalence ~=_X must be carried through factorization,
fiber-constancy, spread, and quotient language.
```

Final v0.4 now factors through:

```text
X / ~=_X
```

and requires `~=_K` to be an equivalence relation, or else requires the audit
to declare the induced equivalence used for quotienting.

The review also added a blunt physics warning:

```text
strictly local observers cannot be credited with global/purifier/environment
capability unless the access profile grants a physical route to it.
```

## Bottom Line

The candidate is now strongest as:

```text
projection sufficiency for typed capability objects
```

with physics constrained to:

```text
known physics -> induced Cap -> projection sufficiency audit
```
