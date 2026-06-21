# Technical Report: Detector Provenance Robustness v0.1

## Claim Under Test

T68 showed that intervention-sensitive provenance metadata can separate a
copied archive from an independent overlapping readout even when passive
detector statistics are identical. T70 tests whether that separation survives
realistic provenance degradation.

The question is not whether passive correlations or calibrated POVMs suffice.
T66 and T67 already say no. The question is whether D1 detector finality remains
operational when the metadata required by T68 are noisy, delayed, lossy,
forgeable, incomplete, or perturbed by the intervention.

## Model

T70 starts from the T68 hostile pair:

- dependent copied archive;
- independent overlapping readout.

Both witnesses keep the same passive detector statistics:

```text
agreement = 0.92
phi       = 0.84
```

The model then applies degradation regimes over six provenance channels:

1. clock uncertainty;
2. tag loss;
3. tag forgery or spoofing;
4. hidden archive latency;
5. perturbation back-action;
6. incomplete provenance DAGs.

It also includes an explicit partial-DAG threshold regime to test whether the
rule collapses back into arbitrary thresholding.

## Conservative Partition Rule

The T70 rule is conservative:

- use authenticated dependence evidence to put records in the same class;
- use authenticated independence evidence to put records in distinct classes;
- if no authenticated channel remains, abstain;
- if classification requires a partial-DAG threshold or unaudited semantic
  label, mark the regime threshold-dependent;
- compute D1 only after a partition is determined.

This is important. T70 does not allow passive similarity to substitute for
missing provenance.

## Robustness Result

T70 gives a mixed result.

The rule survives moderate single-channel degradation:

- clock uncertainty alone;
- tag loss when clean perturbation response and complete DAG remain;
- tag spoofing when unauthenticated tags are ignored and DAG/intervention
  evidence remain;
- perturbation back-action when authenticated tags and complete DAG remain;
- hidden archive latency when signed provenance metadata remain.

In these regimes, the copied archive is assigned one independence class:

```text
local_log -> P0
archive   -> P0
D1        = (2, 1, 1, 0)
finalized = false
```

The independent readout is assigned two independence classes:

```text
local_log -> P0
archive   -> P1
D1        = (2, 2, 1, 1)
finalized = true
```

The rule fails cleanly when all strong channels are missing or contaminated:

- tags are lost or unauthenticated;
- archive latency hides timing;
- perturbation is back-action contaminated;
- the provenance DAG is incomplete.

In this regime the partition is undetermined and D1 is not evaluated.

The rule also fails in the partial-DAG-only regime: if only a partial ancestry
score remains, classification requires an arbitrary threshold. T70 marks this
as threshold-dependent and withholds D1.

## Minimal Metadata Requirement

D1 detector finality is non-arbitrary only when the provenance partition is
fixed before scoring by at least one authenticated dependence channel for
copied records and at least one authenticated independence channel for
independent records.

In the T70 witness family, usable channels are:

- clean perturbation response;
- authenticated origin tags;
- complete signed ancestry;
- timing only when paired with ancestry and clock bounds.

Passive similarity, calibrated outcome statistics, and partial-DAG thresholds
are insufficient.

## Current Strongest Claim

T68 survives moderate single-channel degradation when redundant authenticated
provenance channels remain. The D1 partition can still be fixed before finality
scoring without inspecting the desired D1 verdict.

## What This Improved

T70 turns T68 from an ideal-metadata witness into a robustness map. The detector
branch now has a clearer operational condition: D1 detector finality is only
available after a provenance partition is fixed by trusted causal/provenance
instrumentation.

## What This Weakened

T70 weakens the detector branch of Q1 further. If clock, tag, intervention, and
DAG evidence are jointly missing, forgeable, thresholded, or back-action
contaminated, D1 adds no detector-level content beyond externally supplied
classes.

This is not a small caveat. It means TaF should not claim detector-level
provenance recovery from detector outcomes alone.

## Falsification Criterion

T70 fails if degraded copied and independent witnesses with identical passive
statistics can be classified non-arbitrarily without authenticated provenance
channels.

It also fails if a physical implementation shows that the required provenance
channels cannot be made independent of the desired D1 outcome.

## Q1 Recommendation

Keep Q1 `partially_supported`, but narrow its detector branch:

```text
D1 is an intervention-sensitive provenance/accounting predicate over detector
records whose independence partition has already been fixed by trusted
provenance instrumentation.
```

Do not claim calibration-free detector finality.

## Next Work

Replace the boolean degradation flags with a physical protocol model:

- clock distributions;
- signature failure probabilities;
- archive batching;
- intervention back-action matrices;
- detector subsystem trust boundaries.

The next hostile test should ask whether the minimal metadata requirement
survives probabilistic failure rates without becoming another threshold-tuned
rule.

## Reproduction

```bash
python -m unittest tests.test_detector_provenance_robustness -v
python -m models.run_t70
```


