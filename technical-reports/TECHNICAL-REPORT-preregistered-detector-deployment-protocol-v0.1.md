# Technical Report: Pre-registered Detector Deployment Protocol v0.1

## Claim Under Test

The detector branch has reached a stricter boundary. T76 made deployment
evidence executable, and T77 exposed policy sensitivity. The next question is
whether a future detector run can be specified in advance strongly enough to
serve as an empirical discriminator rather than a fixture or post hoc policy
exercise.

## Artifact

T78 adds an executable pre-registration gate. A candidate deployment is
admissible for a Q1 detector-branch upgrade only if, before the first event, it
fixes:

- the full T76 evidence schema;
- the T77-safe confidence and false-risk corridor;
- timing-matched unsigned, spoof, uniqueness, perturbation, and DAG controls;
- raw log sources for time tags, signatures, archive receipts, trust-boundary
  audits, perturbation trials, and ancestry DAG exports;
- a demotion rule if controls leak or thresholds are incomplete.

## Current Strongest Claim

The detector branch now has a pre-data gate: a real deployment can only test Q1
if it fixes the evidence schema, controls, raw logs, policy corridor, and
demotion rule before data collection.

## What This Improved

T78 turns the next experiment into a falsifiable contract. It says exactly what
must exist before a detector run can be allowed into the T76/T77 audit, and it
separates real deployment logs from fixture counts.

## What This Weakened

T78 weakens the detector branch by making T76/T77 insufficient for any further
upgrade. Fixture counts, post hoc policy choices, missing unsigned controls,
and permissive corridors are rejected before D1 scoring.

## Falsification Condition

Demote detector-level Q1 if no real deployment can satisfy this pre-data
contract and still preserve signed recovery, unsigned withhold, and
incomplete-pre-registration failure under the locked T76/T77 audit.

## Claim Ledger Update

Q1 should remain `partially_supported`, but the detector-level claim narrows:

```text
Detector-level support requires a pre-registered, real-log provenance protocol.
Synthetic fixtures, post hoc policy selection, and permissive control-leaking
corridors cannot upgrade Q1.
```

## Next Work

Populate the T78 contract from an actual detector run, then run the locked
T76/T77 pipeline without changing evidence fields or policy corridor.

## Reproduction

```bash
python -m unittest tests.test_preregistered_detector_deployment_protocol -v
python -m models.run_t78
```
