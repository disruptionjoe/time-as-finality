# T70: Detector Provenance Robustness

## Question

Does the T68 intervention-sensitive provenance rule remain usable when detector
provenance metadata are noisy, delayed, lossy, forgeable, or perturbed by the
intervention itself?

## Motivation

T66 showed that calibrated POVM response matrices do not determine D1 detector
finality. T67 showed that passive pairwise correlations do not recover D1
independence classes. T68 gave a conditional-positive repair: copied archives
and independent overlapping readouts can have identical passive statistics, but
separate when intervention-sensitive provenance metadata are available before
D1 scoring.

T70 stress-tests that repair.

## Failure Modes

T70 applies controlled degradation regimes to the T68 copied-vs-independent
witness family:

- clock uncertainty;
- tag loss;
- tag forgery or spoofing;
- hidden archive latency;
- perturbation back-action;
- incomplete provenance DAGs;
- partial-DAG threshold dependence.

The passive statistics are held fixed:

```text
agreement = 0.92
phi       = 0.84
```

## Conservative Rule

D1 is computed only after the degraded provenance rule fixes the independence
partition. If no authenticated provenance channel remains, the rule abstains.
If classification would require a partial-DAG threshold or unaudited semantic
label, the rule marks the regime threshold-dependent and withholds D1.

## Current Result

T70 produces a mixed robustness result.

The T68 rule survives moderate single-channel degradation:

- clock uncertainty alone;
- tag loss when clean perturbation response and complete DAG remain;
- tag spoofing when unauthenticated tags are ignored and DAG/intervention
  evidence remain;
- perturbation back-action when authenticated tags and complete DAG remain;
- hidden archive latency when signed provenance metadata remain.

The rule fails cleanly when all strong channels are missing or contaminated:

- incomplete DAG;
- missing or unauthenticated tags;
- hidden latency and ambiguous timing;
- perturbation back-action.

It also fails when only a partial ancestry score remains and classification
would require an arbitrary threshold.

## Minimal Metadata Requirement

D1 detector finality is non-arbitrary only when the provenance partition is
fixed by at least one authenticated dependence channel for copied records and
at least one authenticated independence channel for independent records.

Usable channels in this witness family are:

- clean perturbation response;
- authenticated origin tags;
- complete signed ancestry;
- timing only when paired with ancestry and clock bounds.

Passive similarity and partial-DAG thresholds are insufficient.

## Claim Impact

Q1 remains partially supported, but only as an intervention-sensitive
provenance/accounting framework over detector records. T70 does not support a
claim that D1 detector finality can be recovered from calibrated detector
outcomes alone.

## Artifacts

- Model: `models/detector_provenance_robustness.py`
- Runner: `models/run_t70.py`
- Test: `tests/test_detector_provenance_robustness.py`
- Technical report: `TECHNICAL-REPORT-detector-provenance-robustness-v0.1.md`
- Results: `results/detector-provenance-robustness-v0.1.json`
- Result note: `results/detector-provenance-robustness-v0.1-results.md`


