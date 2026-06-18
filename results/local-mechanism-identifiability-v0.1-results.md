# Local Mechanism Identifiability v0.1 Results

**Test:** T44 - Local Mechanism Identifiability Audit
**Date:** 2026-06-18
**Status:** Implemented

---

## Probe Summary

| Probe | Separates all | Separated pairs | Unresolved pairs |
| --- | --- | --- | --- |
| baseline | No | 0 | 3 |
| event_count_scaling | No | 0 | 3 |
| demand_drop | No | 2 | 1 |
| resource_shock | No | 2 | 1 |
| coupling_rewire | No | 2 | 1 |
| load_recovery | No | 0 | 3 |

---

## Minimal Basis

```text
demand_drop
coupling_rewire
```

This two-probe basis separates all three T43 mechanism families:

- intrinsic rate;
- resource budget;
- interaction density.

---

## Unresolved Equivalences Preserved

The following probes preserve the T43 ambiguity:

```text
baseline
event_count_scaling
load_recovery
```

These are not failures. They show that local accumulation traces alone are not
enough to identify mechanism.

---

## Hypothesis Verdicts

| Hypothesis | Status |
| --- | --- |
| H0 | rejected |
| H1 | partially_supported |
| H2 | supported |
| H3 | supported |
| H4 | best_supported |
| H5 | rejected_for_t43_family |

Best supported: **H4**.

---

## Theorem

Finite Probe Identifiability Theorem:

```text
T43-equivalent mechanisms are not identifiable from baseline local accumulation
alone, but demand_drop plus coupling_rewire separates intrinsic rate, resource
budget, and interaction density.
```

---

## Machine-Readable Output

```text
results/local-mechanism-identifiability-v0.1.json
```
