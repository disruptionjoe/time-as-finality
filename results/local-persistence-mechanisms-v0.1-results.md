# Local Persistence Mechanisms v0.1 Results

**Test:** T43 - Local Persistence Accumulation Mechanism Audit
**Date:** 2026-06-18
**Status:** Implemented

---

## Mechanism Cases

| Case | Hypothesis | Accumulation difference | Reconciliation lag | Verdict |
| --- | --- | --- | --- | --- |
| intrinsic_rate_difference | H1 | 10 | 0 | supported |
| resource_budget_difference | H2 | 10 | 0 | supported |
| interaction_density_difference | H3 | 10 | 0 | supported |
| resource_difference_with_delay | H2 | 10 | 3 | combined_effects_witness |

---

## Propagation Control

```text
fixed intrinsic accumulation
vary propagation delay
```

Result:

```text
accumulation difference changed = False
reconciliation lag changed = True
```

Verdict: propagation changes lag, not local accumulation.

---

## Rejected Candidate

Propagation shadow:

```text
delta = base_rate - delay_penalty * propagation_delay
```

Result:

```text
fixed topology produces difference = False
varied topology produces difference = True
eliminated = True
```

Reason: the apparent accumulation difference appears only when propagation
parameters differ.

---

## Equivalence Classes

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

Trace-level equivalence supports H4.

---

## Hypothesis Verdicts

| Hypothesis | Status |
| --- | --- |
| H0 | rejected |
| H1 | partially_supported |
| H2 | partially_supported |
| H3 | partially_supported |
| H4 | best_supported |
| H5 | not_earned |

Best supported: **H4**.

---

## Theorem

Finite Local Mechanism Equivalence Theorem:

```text
multiple finite node-local mechanisms can change local persistence accumulation
with propagation held fixed
```

and

```text
distinct mechanism parameterizations can generate identical local delta traces
```

This is a finite trace-level theorem only.

---

## Machine-Readable Output

```text
results/local-persistence-mechanisms-v0.1.json
```
