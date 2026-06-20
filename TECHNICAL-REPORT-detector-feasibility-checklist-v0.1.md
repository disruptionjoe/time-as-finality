# Technical Report: Detector Feasibility Checklist v0.1

## Claim Under Test

T87 stated the raw-log contract and T95 mapped the named T75 time-tagging
stack into that contract. The highest-value next question is not another
synthetic detector witness. It is whether the surviving detector-side Q1 route
still looks like detector physics once its requirements are split into native
exports, provenance middleware, custom controls, and pre-data governance.

## Result

The route survives, but only narrowly:

```text
The current detector-side Q1 path is feasible only as a governance-heavy
dry-run protocol. The decisive bottlenecks are copied/independent controls,
ambiguity challenges, perturbation controls, and pre-data demotion rules, not
native detector timing.
```

Only one T87 table is native to the named time-tagging hardware:

- `event_time_tag_stream`

Two required tables are provenance/logging middleware:

- `signature_verification_log`
- `ancestry_dag_edge_export`

Three required tables are custom experiment-control infrastructure:

- `control_pair_manifest`
- `tag_ambiguity_challenge_log`
- `perturbation_trial_log`

Three required tables are governance locks:

- `preregistration_manifest`
- `trust_boundary_audit_log`
- `demotion_decision_log`

## Current Strongest Claim

Detector-side Q1 is no longer best described as an emerging detector
discriminator. It is a dry-run admissibility program over classical record
governance, with one native timing stream embedded inside a larger
provenance/control packet.

## What This Improved

T96 converts "instrument-facing feasibility" into an explicit burden split. A
serious reader can now inspect the route table-by-table and ask whether the
non-native blocker packet can be frozen before the first event.

This makes the detector branch easier to falsify. A lab does not need to argue
abstractly about provenance any longer. It can simply fail to instantiate the
blocker tables before data collection, which should demote the route.

## What This Weakened Or Falsified

This weakens the detector route again. The named hardware does not even come
close to carrying the route by itself. Timing is necessary, but it is not the
load-bearing object.

It also blocks another over-reading: a signed archive plus synchronized clocks
is still not close to a Q1 upgrade unless copied/independent controls,
ambiguity challenges, perturbation trials, trust audits, and demotion logs are
all locked pre-data.

## Falsification Condition

T96 fails if either of the following occurs:

1. a realistic detector stack natively exports most of the T87
   control/provenance/governance packet without custom middleware; or
2. a dry run that lacks the blocker tables still legitimately upgrades Q1.

Absent either outcome, the route should be treated as a narrow dry-run
governance program rather than detector physics.

## Claim Ledger Update

Q1 should remain `partially_supported`, but the detector branch should now be
stated more narrowly:

```text
Detector-side Q1 survives only as a governance-heavy dry-run admissibility
program over classical records. Native timing export is necessary but not
sufficient; the load-bearing packet is copied/independent controls, ambiguity
challenges, perturbation trials, signed raw ancestry edges, trust audits, and
pre-data demotion rules.
```

## Open Blocker

The repo still has no locked dry-run packet with real rows. The open blocker is
not timing resolution. It is whether a lab can freeze the non-native control
and governance tables before data collection without post hoc leakage.

## Next Work

Build one detector dry-run packet skeleton and try to fill it before any data
analysis:

- file names and immutable export points;
- copied/independent control manifest;
- ambiguity challenge rows;
- perturbation trial rows;
- signed DAG edge rows;
- trust-boundary audit rows;
- demotion decision rows;
- preregistration hashes.

If a realistic lab workflow cannot populate that packet pre-data, demote the
detector branch below the current Q1 frontier.

## Reproduction

```bash
python -m unittest tests.test_detector_feasibility_checklist -v
python -m models.run_t96
```
