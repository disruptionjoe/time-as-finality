# T72: Physical Provenance Protocol

## Question

Under what physically modeled conditions can detector provenance metadata remain
trustworthy enough to fix D1 independence classes before finality scoring?

## Motivation

T68 showed that copied archives and independent overlapping readout chains can
be separated when intervention-sensitive provenance metadata are available.
T70 stress-tested that result with Boolean degradation flags. T72 replaces
those flags with interval/probability-valued protocol parameters.

## Protocol Parameters

T72 models:

- clock uncertainty distributions via timestamp error bounds and archive
  batching windows;
- signature/authentication failure probabilities, tag retention, forgery, and
  spoofed independent tags;
- archive batching and declared copy-latency intervals;
- trust boundaries between detector, archive, and transport subsystems;
- perturbation back-action matrices through dependent-change, independent-change,
  and back-action probabilities;
- partial provenance-DAG observability through signed-edge, truncation, and
  false-shared-edge probabilities.

## Pre-Registered Rule

Each channel emits a confidence and false-risk estimate. A channel is accepted
only if:

```text
confidence >= confidence_floor
false_risk <= max_false_risk
threshold_source = declared_physical_protocol
```

The confidence floor and false-risk ceiling are protocol declarations, not D1
outcome-tuned thresholds. If the only available threshold is ad hoc, D1 is
withheld.

If accepted dependence evidence exists, the records are assigned to the same
independence class. If accepted independence evidence exists, they are assigned
to distinct classes. If accepted evidence conflicts or no channel clears the
declared protocol bounds, D1 is withheld.

## Regime Outcomes

T72 includes regimes for:

- robust provenance recovery;
- batched-clock recovery using cryptographic/DAG evidence;
- lossy-tag recovery using clean intervention and DAG evidence;
- ambiguous withhold under low trust;
- ad hoc partial-DAG threshold withhold;
- false independence risk from forged independent-looking tags;
- false dependence risk from perturbation back-action.

## Current Result

T72 is a conditional and bounded success.

It shows that detector provenance recovery is possible under explicit physical
protocol assumptions, but also that the protocol can fail in two different
ways:

- conservative failure: D1 is withheld because provenance cannot be fixed;
- unsafe failure: the protocol accepts false independence or false dependence.

The unsafe failures are more damaging than T70's Boolean abstention cases. They
show why authentication and back-action limits are not optional.

## Claim Impact

Q1 remains partially supported only as a detector-record provenance accounting
framework under explicit physical protocol assumptions. T72 does not support
detector-level provenance recovery from calibrated outcomes or passive
statistics alone.

## Artifacts

- Model: `models/physical_provenance_protocol.py`
- Runner: `models/run_t72.py`
- Test: `tests/test_physical_provenance_protocol.py`
- Technical report: `TECHNICAL-REPORT-physical-provenance-protocol-v0.1.md`
- Results: `results/physical-provenance-protocol-v0.1.json`
- Result note: `results/physical-provenance-protocol-v0.1-results.md`
