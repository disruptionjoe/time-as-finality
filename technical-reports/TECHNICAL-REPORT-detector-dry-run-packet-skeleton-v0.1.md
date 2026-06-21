# Technical Report: Detector Dry-Run Packet Skeleton v0.1

## Claim Under Test

T96 narrowed detector-side Q1 to a governance-heavy dry-run admissibility
program. The highest-value next question is whether that program can be
specified as a concrete pre-data packet, or whether the detector route remains
too vague to evaluate before a lab run.

## Artifact

T97 adds an executable dry-run packet skeleton for the T87 detector route. The
locked packet contains:

- every T87 table;
- exact required columns and no extras;
- deterministic file names;
- declared join keys;
- schema hashes;
- export checksums;
- all T86 hostile control roles;
- both channel-isolation tests;
- policy, analysis-code, evidence-schema, demotion-rule, and manifest hashes.

The model audits five packet shapes:

- locked schema-complete scaffold;
- placeholder population attempt;
- schema-drift packet;
- post hoc packet;
- packet missing hostile T86 controls.

## Result

The locked scaffold passes only as:

```text
schema_complete_predata_scaffold_only
```

Its evidence verdict is:

```text
withhold_detector_q1_upgrade
```

If the same packet is handed to T87 immediately, T87 rejects it because it has
no real raw deployment log. This is the desired boundary: the packet can be
frozen before data collection, but it is not empirical evidence.

All hostile controls fail:

- placeholder rows cannot populate T76/T86 counts;
- unregistered schema columns are rejected;
- post hoc packet locking is rejected;
- missing ambiguous-tag and DAG contamination controls are rejected.

## Current Strongest Claim

A detector-side Q1 dry-run packet can now be specified without schema
ambiguity, but it remains only a pre-data scaffold. T87 would still reject it
as evidence until real event rows replace template exports without changing
schema, policy, demotion rules, or control roles.

## What This Improved

T97 turns the T96 blocker into an executable artifact a lab or reviewer can
inspect before data collection. The route no longer depends on informal claims
that "the logs" can be produced later. The packet says exactly what files,
columns, joins, hashes, and controls must exist.

It also makes the next falsification easy: if the packet cannot be frozen
before the first event, the detector route should be demoted without running a
D1-style audit.

## What This Weakened Or Falsified

This weakens detector-side Q1 again. The current positive result is not a
detector effect and not an empirical discriminator. It is a pre-data governance
artifact over classical records.

It also falsifies a likely shortcut: a schema-complete packet is not enough if
it contains only templates. Placeholder rows, post hoc schema changes, and
missing hostile controls must withhold any Q1 upgrade.

## Falsification Condition

Demote the detector branch if a realistic lab workflow cannot freeze the T97
packet before event collection, or if the filled packet cannot pass T87 and
preserve the T86 signed-DAG, perturbation, ambiguous-control, and
contaminated-control separations under the locked schema.

## Claim Ledger Update

Q1 should remain `partially_supported`, but narrowed:

```text
Detector-side Q1 now has a schema-complete dry-run packet skeleton, not
evidence. Placeholder rows, schema drift, post hoc packet assembly, and missing
hostile controls falsify any attempted detector upgrade. A Q1 upgrade requires
real event rows collected under the locked packet and admitted by T87 before
T76/T86 scoring.
```

## Open Blocker

No actual detector event rows have been collected under the locked packet. The
live blocker is operational: freeze the packet before first event, then fill it
without schema changes.

## Next Work

Instantiate the T97 packet in a real lab dry run with empty files, signed
manifests, immutable export points, and operator handoff checks. If the lab
cannot do that pre-data, demote the detector route below the active Q1
frontier.

## Reproduction

```bash
python -m unittest tests.test_detector_dry_run_packet_skeleton -v
python -m models.run_t97
```
