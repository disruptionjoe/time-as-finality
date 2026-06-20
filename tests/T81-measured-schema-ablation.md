# T81: Measured Schema Ablation

## Question

Which T76 measured-evidence categories are actually load-bearing in the
current executable detector-provenance audit, and which are presently asserted
in prose but non-discriminating under single-category ablation?

## Motivation

T76-T79 built a stricter detector branch around measured evidence,
pre-registration, and raw logs. That route is only scientifically useful if
the required schema is honest about what the executable audit currently uses.
If some categories never affect the verdict, the branch is overclaimed and
should be narrowed.

## Setup

- Start from the T76 signed measured fixture.
- Replace one evidence category at a time with the corresponding degraded
  control values while keeping all other categories fixed.
- Re-run the T74 Monte Carlo audit after each single-category replacement.

Categories:

- timing;
- retention/signature pass rates;
- spoof-resistance counts;
- trust-boundary checks;
- perturbation-separation counts;
- DAG observability and signed-edge counts;
- pre-registration coverage.

## Success Criteria

- At least one category is shown to be load-bearing.
- At least one declared T76 category is shown to be non-load-bearing under the
  current witness family.
- The result sharpens Q1 by narrowing the current executable content instead
  of expanding it rhetorically.

## Failure Criteria

- Every category is load-bearing, making the current schema fully justified.
- No category is load-bearing, making the measured detector route collapse.
- The ablation result depends on changing multiple categories at once.

## Known Physics Constraints

- This is a protocol-audit ablation over already formed records, not a new
  detector-dynamics model.
- No conclusion here upgrades Q1 beyond measured provenance bookkeeping.
- A non-load-bearing category in T81 may still matter physically; the claim is
  only about the current executable audit.

## Contribution Needed

Either compress the detector schema to the categories that actually control the
verdict, or extend the witness family so spoof, perturbation, and DAG evidence
each become independently decisive.
