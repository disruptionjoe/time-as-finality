# Technical Report: Detector Stack Export Map v0.1

## Claim Under Test

T94 made detector provenance the active Q1 route because weak measurement has
no real independent-axis platform. T87 already states the event-level raw-log
contract a detector deployment must satisfy. The highest-value next question is
whether the named T75 stack can be mapped to that contract without silently
adding post hoc structure.

## Artifact

T95 adds an executable export-map audit for this stack:

```text
HydraHarp time tags
  + White Rabbit synchronization
  + signed hash-chain archive
  + pre-registered control/provenance middleware
```

The audit reuses the T87 table and column requirements directly. It separates
five cases:

- native HydraHarp/White Rabbit timing export;
- signed archive without control packet;
- augmented pre-registered deployment plan;
- post hoc augmented packet;
- dashboard-summary export.

## Result

The T75 stack is feasible only as an augmented pre-registered deployment
packet. Native timing export is not enough. A signed archive is not enough. The
T87 controls, perturbation trial log, ancestry edge export, trust-boundary
audit, and demotion decision log must be engineered before data collection.

The one positive case is intentionally weak:

```text
admissible_as_preregistered_deployment_plan_only
```

It is not empirical support, because no real event rows are present.

## Current Strongest Claim

Detector-side Q1 remains alive only as a pre-registered detector-record
admissibility protocol. The named photon time-tagging route can be made
auditable in principle, but most of the load-bearing structure is
provenance/control middleware rather than native detector physics.

## What This Improved

T95 turns the T87 next step into an instrument-level checklist. A serious
reader can now ask for a deployment packet with exact tables, event-id joins,
manifest hashes, immutable exports, and checksums, instead of accepting a
narrative claim that the lab stack has "the logs."

It also prevents an over-reading of T75. Picosecond timing and synchronized
clocks are only the timing table. They do not supply copied/independent control
pairs, tag ambiguity challenges, perturbation controls, signed raw ancestry
edges, trust-boundary audits, or demotion decisions.

## What This Weakened Or Falsified

This weakens the source-anchored detector route. The stack does not natively
satisfy the raw-log contract. It requires custom middleware that must be
pre-registered before data collection.

It also blocks another false upgrade path: a signed archive without the T87
control packet still withholds detector-side Q1.

## Falsification Condition

T95 fails if native instrument exports alone can supply every T87 table and
required column before data collection.

It also fails in the opposite direction if an augmented deployment packet with
real rows cannot preserve the T86 signed recovery, all-ambiguous withhold,
perturbation/DAG rescue, and contaminated-control withhold separations under
the locked schema.

## Claim Ledger Update

Q1 should remain `partially_supported`, with the detector branch stated more
narrowly:

```text
Detector-side Q1 has an executable deployment path only through an augmented,
pre-registered T87 raw-log packet. Native time-tagging hardware and signed
archive summaries are insufficient; the route does not gain empirical support
until real event rows populate the locked T76/T86 audit without schema changes.
```

## Open Blocker

No real event rows exist for the augmented T95 map. Passing T95 is only a
deployment-plan admission, not a D1 verdict and not empirical evidence.

## Next Work

Build the augmented packet for one dry-run dataset:

- publish the row schemas;
- prove event-id joins across tables;
- freeze manifest, policy, analysis-code, and demotion hashes;
- export immutable checksums;
- run T87 before populating T76/T86 counts.

## Reproduction

```bash
python -m unittest tests.test_detector_stack_export_map -v
python -m models.run_t95
```
