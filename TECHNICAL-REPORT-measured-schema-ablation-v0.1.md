# Technical Report: Measured Schema Ablation v0.1

## Claim Under Test

T76 introduced a broad measured evidence schema for detector-provenance
audits. T81 asks whether the current executable model earns that breadth.

## Artifact

T81 performs single-category ablations on the signed T76 fixture. One evidence
category at a time is replaced by degraded control values, and the T74 audit
is rerun without changing any other category.

## Current Strongest Claim

The current executable detector-provenance audit does not justify treating
every T76 evidence field as equally load-bearing. In the present witness
family, trust-boundary evidence fully removes robust recovery, and incomplete
pre-registration demotes the result to a threshold-dependent one. The other
declared categories do not independently change the verdict under
single-category ablation.

## What This Improved

T81 makes the detector branch more honest. It separates categories that are
actually decisive in the current executable audit from categories that are only
motivated at the prose level.

## What This Weakened

T81 weakens the broader detector-branch packaging in T76-T79. As currently
implemented, the route behaves mostly like a trust-boundary plus
pre-registration gate. Spoof, perturbation, and DAG evidence are not yet
independently load-bearing in the canonical witness family.

## Falsification Condition

T81 fails if every declared T76 evidence category independently changes the
signed fixture's verdict under single-category ablation, or if the trust and
pre-registration ablations stop changing the verdict.

## Claim Ledger Update

Q1 should remain `partially_supported`, but with a sharper detector-branch
boundary:

```text
The current executable detector route is narrower than the full measured
schema suggests. Trust-boundary evidence and pre-registration are presently
load-bearing; other evidence channels are argued for but not yet independently
decisive in the witness family.
```

## Open Blocker

The witness family does not yet contain cases where spoof evidence,
perturbation response, or DAG observability alone determine a false
independence or false dependence verdict.

## Next Work

Either simplify the measured schema to the categories the audit really uses, or
extend the witness family and classifier until each declared evidence channel
controls at least one boundary case on its own.

## Reproduction

```bash
python -m unittest tests.test_measured_schema_ablation -v
python -m models.run_t81
```
