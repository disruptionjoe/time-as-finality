# T134: Detector Dry-Run Tier Gate

## Route

Quantum measurement / classical records, with experimental-discriminator
pressure on detector evidence infrastructure.

## Question

Can the T97 dry-run packet emit the T133 packet tiers honestly, or does the
raw-log scaffold still need a separate T121/T133 wrapper before any detector
deployment can claim provisional admission or claim-review readiness?

## Motivation

T133 showed that detector packet requirements are tiered, not flat. The next
risk is overclaiming T97: a lab could freeze and fill the raw-log tables, then
treat that as enough for detector-branch admission. T134 tests that shortcut.

## Setup

The audit composes:

- the T97 raw-log scaffold;
- a row-filled T97 variant;
- the T121/T123 packet wrapper;
- the T133 raw/provisional/claim-review tier split.

## Success Criteria

- The locked pre-data T97 scaffold remains non-evidence.
- Filled T97 raw-log rows alone do not clear provisional admission.
- Filled T97 rows plus a complete T121/T123 wrapper clear all three tiers.
- Missing provenance blocks provisional admission.
- Missing witnesses or an open challenge preserve provisional intake but block
  claim-review readiness.
- The result does not upgrade Q1B or claim detector physics.

## Failure Criteria

- Real T97 rows alone are treated as sufficient for provisional admission.
- T97-native fields are described as covering T121/T133 wrapper fields that
  they do not actually cover.
- Missing witnesses or open disputes are flattened into the same failure tier
  as missing provenance/signature/authority fields.

## Claim Impact

No Q1B promotion. T134 makes detector evidence harder to overstate: T97 is
necessary but not sufficient. A real deployment must pre-register both the
T97 raw-log packet and the T121/T133 wrapper, then state which tier is being
claimed before event collection.

## Reproduction

```bash
python -m unittest tests.test_detector_dry_run_tier_gate -v
python -m models.run_t134
```
