# Technical Report: Local Mechanism Identifiability Audit (T44)

**Version:** v0.1
**Date:** 2026-06-18
**Status:** Implemented

---

## Summary

T43 showed that distinct finite mechanisms can generate identical local
accumulation traces. T44 asks whether that ambiguity can be removed by finite
probe protocols.

Result: the T43 mechanisms are not identifiable from baseline accumulation
alone, but they are separable by a two-probe observable basis:

```text
demand_drop
coupling_rewire
```

Best-supported hypothesis: **H4**. A small finite observable basis separates the
T43 mechanism families.

This remains a finite identifiability result. It does not identify a physical
proper-time mechanism.

---

## Probe Results

| Probe | Separated pairs | Unresolved pairs | Verdict |
| --- | --- | --- | --- |
| baseline | 0 | 3 | preserves ambiguity |
| event_count_scaling | 0 | 3 | preserves ambiguity |
| demand_drop | 2 | 1 | separates resource budget |
| resource_shock | 2 | 1 | separates resource budget |
| coupling_rewire | 2 | 1 | separates interaction density |
| load_recovery | 0 | 3 | preserves ambiguity in this simple model |

The useful probes are not the ones that merely extend the trace. They perturb
specific local mechanism parameters.

---

## Minimal Observable Basis

The minimal separating basis found is:

```text
demand_drop
coupling_rewire
```

Response structure:

| Mechanism | Demand drop | Coupling rewire | Identification |
| --- | --- | --- | --- |
| intrinsic rate | stable | stable | intrinsic-like |
| resource budget | changes | stable | resource-like |
| interaction density | stable | changes | coupling-like |

This separates all three T43 baseline mechanisms.

Resource shock is redundant with demand drop in the simple trace model.

---

## Unresolved Equivalences

The following weaker probe sets leave the mechanisms unresolved:

```text
baseline
event_count_scaling
load_recovery
```

These unresolved cases are important. They preserve the T43 warning:

```text
same local accumulation curve does not identify its generating mechanism
```

---

## Hypothesis Verdicts

| Hypothesis | Verdict |
| --- | --- |
| H0 | rejected |
| H1 | partially_supported |
| H2 | supported |
| H3 | supported |
| H4 | best_supported |
| H5 | rejected_for_t43_family |

H0 is rejected because finite probes separate the T43 mechanisms.

H1 is partially supported because intrinsic rate is distinguishable as stable
under both demand and coupling perturbation, but stability under a single
irrelevant probe is not unique.

H2 is supported: resource budget responds to demand and resource probes.

H3 is supported: interaction density responds to coupling rewiring.

H4 is best supported: a small observable basis separates all three mechanisms.

H5 is rejected for the finite T43 mechanism family, but remains open for richer
future mechanisms.

---

## Theorem Earned

**Finite Probe Identifiability Theorem**

The T43 trace-equivalent mechanisms are not identifiable from baseline local
accumulation alone, but a two-probe finite observable basis, demand_drop plus
coupling_rewire, separates intrinsic rate, resource budget, and interaction
density.

---

## What T44 Does Not Claim

- It does not explain relativity.
- It does not derive proper time.
- It does not identify a physical clock mechanism.
- It does not introduce spacetime dynamics.
- It does not show that the T44 probes are physically realizable.

---

## Recommendation

Promote demand sensitivity and coupling sensitivity as the minimal next
observable basis for local accumulation studies.

Keep baseline trace equivalence as a live warning against overinterpreting
local accumulation curves.

The next question is no longer:

```text
Can finite mechanisms be distinguished at all?
```

It is:

```text
Which of these finite probes, if any, has an operational physical analogue?
```

---

## Evidence

Executable files:

- `models/local_mechanism_identifiability.py`
- `models/run_t44.py`
- `tests/test_local_mechanism_identifiability.py`

Result artifacts:

- `results/local-mechanism-identifiability-v0.1.json`
- `results/local-mechanism-identifiability-v0.1-results.md`

Run:

```bash
python -m pytest tests/test_local_mechanism_identifiability.py -q
python -m models.run_t44
```
