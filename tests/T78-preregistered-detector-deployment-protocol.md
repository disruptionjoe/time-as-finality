# T78: Pre-registered Detector Deployment Protocol

## Question

What must be fixed before a real detector run for T76/T77 to count as an
empirical test rather than a post hoc fixture analysis?

## Motivation

T76 replaced narrative detector posteriors with an evidence schema, and T77
showed that the signed result only matters inside a policy corridor that keeps
the timing-only unsigned control from leaking false positives. Both are still
fixture-level. T78 adds a pre-data gate for a real deployment.

## Contract

A detector run is admissible for a Q1 detector-branch upgrade only if it fixes,
before the first event:

- all T76 evidence fields;
- a T77-safe confidence and false-risk policy corridor;
- a timing-matched unsigned negative control;
- spoof, uniqueness, perturbation, and DAG replay/truncation challenges;
- raw log sources for time tags, signatures, archive receipts, trust-boundary
  checks, perturbation trials, and ancestry DAG export;
- a demotion rule if controls leak or threshold fields are incomplete.

## Success Criteria

- A complete pre-data plan is admitted for the locked T76/T77 real-log audit.
- Post hoc policy choice is rejected even when evidence fields are complete.
- Missing unsigned timing controls are rejected.
- Fixture-only counts are rejected.
- The T77 permissive corridor is rejected because it already leaked unsigned
  false positives.

## Failure Criteria

- A post hoc or fixture-only plan is allowed to upgrade Q1.
- A plan without timing-matched unsigned controls is allowed to upgrade Q1.
- A permissive policy corridor is treated as equivalent to the baseline or
  stricter corridor.

## Claim Impact

If T78 passes, Q1 remains `partially_supported` only as a pre-registered,
real-log detector-provenance protocol claim. Synthetic fixture counts and post
hoc policy selection cannot upgrade the detector branch.

If T78 fails, the detector branch should be demoted because the current audit
would not distinguish a real empirical discriminator from threshold or policy
selection.

## Reproduction

```bash
python -m unittest tests.test_preregistered_detector_deployment_protocol -v
python -m models.run_t78
```
