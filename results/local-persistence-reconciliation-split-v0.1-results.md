# Local Persistence and Reconciliation Split v0.1 Results

**Test:** T42 - Local Persistence and Reconciliation Split Audit
**Date:** 2026-06-18
**Status:** Implemented

---

## Witness Summary

| Witness | Classification | Accumulation difference | Reconciliation lag | Pass |
| --- | --- | --- | --- | --- |
| delay_without_dilation | delay_without_dilation | 0 | 4 | Yes |
| dilation_like_without_delay | dilation_like_accumulation_without_extra_delay | 4 | 0 | Yes |
| both_effects | both_effects | 4 | 3 | Yes |
| null_case | null_case | 0 | 0 | Yes |

All witnesses pass: **True**

Independence witnessed: **True**

---

## Scenario Details

### Delay Without Dilation

```text
source accumulation = 10
target accumulation = 10
source visible index = 6
hidden source accumulation due to delay = 4
reconciliation lag = 4
local accumulation difference = 0
```

Interpretation: delayed record access appears without local accumulation
difference.

### Dilation-Like Accumulation Without Extra Delay

```text
source accumulation = 10
target accumulation = 6
source visible index = 10
hidden source accumulation due to delay = 0
reconciliation lag = 0
local accumulation difference = 4
```

Interpretation: local accumulation difference appears without extra
reconciliation delay.

### Both Effects

```text
source accumulation = 10
target accumulation = 6
source visible index = 7
hidden source accumulation due to delay = 3
reconciliation lag = 3
local accumulation difference = 4
```

Interpretation: the comparison has both local accumulation difference and
record-access lag.

### Null Case

```text
source accumulation = 10
target accumulation = 10
source visible index = 10
hidden source accumulation due to delay = 0
reconciliation lag = 0
local accumulation difference = 0
```

Interpretation: the model does not manufacture a rate difference.

---

## Hypothesis Verdicts

| Hypothesis | Status |
| --- | --- |
| H0 | retained_guardrail |
| H1 | partially_supported |
| H2 | best_supported |
| H3 | not_earned |
| H4 | rejected_for_finite_split |

Best supported: **H2**.

---

## Theorem

Finite Accumulation/Reconciliation Independence Theorem:

```text
local accumulation difference
and
reconciliation lag
```

are independent finite observables in `LocalPersistenceReconciliationSystem`.

The result is a finite model theorem only. It is not a physical derivation of
proper time.

---

## Machine-Readable Output

Full structured output:

```text
results/local-persistence-reconciliation-split-v0.1.json
```
