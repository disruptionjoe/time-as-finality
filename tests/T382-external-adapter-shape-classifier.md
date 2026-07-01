# T382: External Adapter Shape Classifier

## Target Claims

R1, S1, D1, PO1, and the T381 next object:

```text
Which external adapter shape can couple into the shared compatibility substrate
without importing global time?
```

## Setup

Classify declared adapter shapes:

- absolute clock,
- scalar source action,
- one signal channel,
- two null channels,
- overcomplete multi-channel interface,
- gauge-like local adapter.

Criteria:

- no global time import,
- local substrate coupling,
- two independent null directions,
- minimal not overcomplete,
- reciprocal observer scaling support.

## Success Criteria

- Two-null-channel adapter is the uniquely clean survivor.
- Absolute clock is rejected for global-time import.
- Scalar source action is rejected for lacking signal geometry.
- One-channel adapter is rejected as undercomplete.
- Overcomplete multi-channel adapter is demoted.
- Gauge-like local adapter is partial unless it supplies observer calibration.

## Failure Criteria

- Absolute clock survives.
- Scalar or one-channel coupling is treated as enough for observer relativity.
- Overcomplete primitive directions are promoted as clean.
- Catalog evidence is mistaken for origin/derivation evidence.

## Known Constraints

The classifier is not exhaustive over all mathematically possible adapters. It
only ranks declared shapes that matter for the current TaF/GU-style question.

## Contribution Needed

Stress the clean survivor by perturbing its assumptions: anisotropy,
nonreciprocity, delay/noise, missing channels, and overcomplete channels.
