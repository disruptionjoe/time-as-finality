# Technical Report: Detector Dry-Run Tier Gate v0.1

## Claim Under Test

T133 split the detector packet burden into raw evidence preservation,
provisional admission, and claim-review readiness. T134 asks whether T97 can
emit those tiers by itself, or whether the raw-log scaffold must be bound to
a separate T121/T133 packet wrapper.

## Result

T97 is necessary but not sufficient.

A locked T97 scaffold is still only a pre-data packet-freezing artifact. A
row-filled T97 raw-log packet is stronger, but still cannot clear T133
provisional admission by itself. It lacks or only partially covers key wrapper
fields:

- raw measurement payload;
- calibration reference;
- packet-level provenance chain;
- authority domains;
- publication status;
- revocation status;
- key state;
- admissibility tokens;
- reconstruction paths;
- challenge/dispute status.

The integration target is stricter:

```text
real T97 rows
  + complete T121/T123 wrapper
  -> raw evidence preserved
  -> provisionally admissible
  -> claim-review ready
```

## Tier Boundary

The finite witness family has three important controls:

- missing provenance blocks provisional admission;
- missing witnesses preserves provisional admission but blocks claim review;
- open challenge/dispute state preserves provisional admission but blocks
  claim review.

This preserves the T133 tier split and rejects a flat "all packet failures are
the same" reading.

## What This Improved

T134 turns the T133 recommendation into an executable integration gate. Future
detector packets now report three explicit outputs:

1. raw evidence preserved;
2. provisionally admissible;
3. claim-review ready.

That makes the detector branch easier to falsify before data collection. A lab
must now say exactly which tier it claims.

## What This Weakened

This weakens the apparent sufficiency of T97. A schema-complete raw-log packet,
even with real rows, is not detector evidence admission and is not a Q1B
upgrade. The T121/T133 wrapper is not paperwork after the fact; it is part of
the admissibility object.

## Current Strongest Claim

Q1B remains an externally blocked admissibility protocol. Its strongest current
form is:

```text
Detector records may enter review only through a pre-registered combined
packet: T97 raw logs plus T121/T133 wrapper fields, with the claimed tier
fixed before event collection.
```

This is detector evidence infrastructure, not detector physics.

## Falsification Condition

T134 fails if real T97 rows alone are enough for provisional admission under
the packet policy, or if a complete T121/T123 wrapper plus real T97 rows still
cannot clear the declared tiers without adding post hoc fields.

## Open Blocker

No real deployment has frozen the combined T97 raw-log packet and T121/T133
wrapper before data collection.

## Recommended Next

Build a single pre-registration manifest that binds T97 table hashes, T121
packet-wrapper fields, T100 authority-domain evidence, and the claimed tier
before the first detector event.

## Reproduction

```bash
python -m unittest tests.test_detector_dry_run_tier_gate -v
python -m models.run_t134
```
