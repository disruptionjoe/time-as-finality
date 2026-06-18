# Technical Report: Local Persistence Accumulation Mechanism Audit (T43)

**Version:** v0.1
**Date:** 2026-06-18
**Status:** Implemented

---

## Summary

T42 showed that local persistence accumulation and reconciliation lag are
distinct finite observables. T43 asks the next question:

```text
If reconciliation delay alone cannot explain local accumulation differences,
what finite mechanisms can?
```

Result: three node-local mechanisms produce local accumulation differences
while propagation is held fixed:

| Mechanism | Local difference | Reconciliation lag | Verdict |
| --- | --- | --- | --- |
| intrinsic stabilization rate | Yes | No | supported |
| finite resource budget | Yes | No | supported |
| interaction density | Yes | No | supported |

A fourth candidate, propagation shadow, is rejected. It produces apparent local
differences only when propagation parameters differ.

Best-supported hypothesis: **H4**. Several mechanisms are mathematically
equivalent at the finite trace level.

---

## Mechanism Model

T43 does not modify `D1RestrictionSystem`, `TypedTransportNetwork`, or T42.
It adds a small sidecar object:

```text
MechanismTrace:
  mechanism_type
  parameters
  local event deltas
  total accumulation
  propagation-dependence flag
```

Each trace generates local event deltas. T42 then measures the resulting
comparison.

---

## Candidate Mechanisms

### H1: Intrinsic Stabilization Rate

```text
delta_i = intrinsic_rate_i
```

Witness:

```text
source rate = 2
target rate = 1
propagation delay = 0
accumulation difference = 10
reconciliation lag = 0
```

This supports H1 as one finite mechanism. It does not prove that intrinsic
rate is the unique mechanism.

### H2: Finite Resource Budget

```text
delta_i = min(update_demand_i, stabilization_budget_i)
```

Witness:

```text
source demand = 2, budget = 2
target demand = 2, budget = 1
propagation delay = 0
accumulation difference = 10
reconciliation lag = 0
```

This is the most promising mechanistic interpretation, but T43 cannot identify
it uniquely because other mechanisms produce the same finite trace.

### H3: Interaction Density

```text
delta_i = base_rate_i + coupling_strength_i * interaction_count_i
```

Witness:

```text
source local interaction count = 1
target local interaction count = 0
propagation delay = 0
accumulation difference = 10
reconciliation lag = 0
```

This supports local interaction density as a candidate mechanism.

### Rejected Candidate: Propagation Shadow

The rejected mechanism defines:

```text
delta_i = base_rate_i - delay_penalty * propagation_delay_i
```

It produces no difference when topology is fixed. It produces a difference only
when propagation parameters differ.

Verdict: rejected as disguised propagation delay.

---

## Propagation Control

T43 repeats T42's key guardrail:

```text
fixed intrinsic traces
vary propagation delay
```

Result:

```text
local accumulation difference changed = False
reconciliation lag changed = True
```

This confirms that ordinary propagation variation changes record-access lag,
not local accumulation.

---

## Equivalence Search

T43 finds trace-level equivalence classes:

```text
(2,2,2,2,2,2,2,2,2,2)
  intrinsic_rate_2
  resource_demand_2_budget_2
  interaction_base_1_coupling_1_count_1

(1,1,1,1,1,1,1,1,1,1)
  intrinsic_rate_1
  resource_demand_2_budget_1
  interaction_base_1_coupling_1_count_0
```

Therefore, local accumulation traces alone cannot identify the underlying
mechanism. This is why H4 is best supported.

---

## Hypothesis Verdicts

| Hypothesis | Verdict |
| --- | --- |
| H0 | rejected |
| H1 | partially_supported |
| H2 | partially_supported |
| H3 | partially_supported |
| H4 | best_supported |
| H5 | not_earned |

T43 rejects H0 because finite mechanisms do produce local differences.

T43 supports H1-H3 as candidate mechanisms, but not uniquely.

T43 supports H4 most strongly because distinct mechanisms generate identical
finite traces.

H5 is not earned. The only additional mechanism found is a boundary case, and
that boundary case is rejected.

---

## Theorem Earned

**Finite Local Mechanism Equivalence Theorem**

Multiple finite node-local mechanisms can change local persistence accumulation
with propagation held fixed, and distinct mechanism parameterizations can
generate identical local delta traces.

This theorem is finite and trace-level only.

---

## Minimal Extension

The smallest supported extension is:

```text
node-local accumulation generator metadata
```

This can live around T42 local histories. It does not require modifying:

- `D1RestrictionSystem`
- `D1RestrictionMorphism`
- `TypedTransportNetwork`
- D1Cat

---

## What T43 Does Not Claim

- It does not explain relativity.
- It does not derive proper time.
- It does not identify a physical clock mechanism.
- It does not introduce spacetime dynamics.
- It does not promote local accumulation into a physical observable.

---

## Recommendation

Promote the local accumulation generator as a minimal mathematical sidecar for
future tests.

Do not choose a unique physical interpretation yet.

Resource budget and interaction density are the most promising interpretations,
but T43 shows they are observationally equivalent to simpler intrinsic-rate
traces unless richer observables are added.

The next recovery question is:

```text
What additional observable distinguishes local resource limits from local
interaction density while propagation remains fixed?
```

---

## Evidence

Executable files:

- `models/local_persistence_mechanisms.py`
- `models/run_t43.py`
- `tests/test_local_persistence_mechanisms.py`

Result artifacts:

- `results/local-persistence-mechanisms-v0.1.json`
- `results/local-persistence-mechanisms-v0.1-results.md`

Run:

```bash
python -m pytest tests/test_local_persistence_mechanisms.py -q
python -m models.run_t43
```
