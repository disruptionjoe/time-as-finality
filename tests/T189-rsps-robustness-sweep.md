# T189: RSPS Robustness Sweep

## Status

Executed finite robustness sweep.

## Target Claims

- [RSPS: Record-Stability Pointer Selection](../claims/RSPS-record-stability-pointer-selection.md)
- [Q1A: Access-Boundary Record Accounting](../claims/Q1A-access-boundary-record-accounting.md)
- [N10: Q1A Spectrum Broadcast Structure Absorber](../literature/N10-q1a-spectrum-broadcast-structure-absorber.md)

## Purpose

Test the modest RSPS boundary after the record-fidelity toy model:

```text
record-fidelity terms may select the coupling/einselected pointer basis;
Born weights remain external trace-rule data.
```

This is a flat-QM null-model test. It is not a Temporal Issuance source-side
claim, a GU section-selector claim, a collapse model, or a Born-rule
derivation.

## Model

Script:

```text
models/rsps_robustness_sweep.py
```

Result artifacts:

```text
results/rsps-robustness-sweep-v0.1.json
results/rsps-robustness-sweep-v0.1-results.md
```

The script sweeps:

- baseline GHZ-style copying;
- environment fragment count;
- branch weights;
- imperfect copying;
- observer fragment access;
- nonorthogonal record states;
- monitored-axis rotation;
- provenance/audited redundancy;
- weakened agreement terms.

## Verdict

`supported_with_boundaries`

The finite sweep supports RSPS as a modest fixed-H basis/objectivity selector
across the tested perturbations. It does not derive Born probabilities. It
also preserves the TaF Q1A warning that raw fragment count is not objectivity
when provenance roots are shared.

## Boundary

Any proposed TI or GU physics bridge using this lane must first pass the
fixed-H null gate:

```text
decoherence / Quantum Darwinism / SBS for basis and objectivity
+ trace rule for probabilities
```

If that fixed-H package absorbs the case, no source-side issuance or GU
section-selection credit is earned.
