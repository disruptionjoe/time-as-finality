# T34: Chained Projection Analysis — v0.1 Results

## Verdict

**Implemented: all three chain shapes confirmed.**

- Emergent obstruction (Spectre): CONFIRMED
- Stepwise propagation: CONFIRMED
- Absorbed obstruction: CONFIRMED

## Chain Results

### Spectre Chain (Emergent Obstruction)

`source_code → compiler_IR → assembly → machine_code → microarchitecture`

| Checkpoint pair | AC6 | PO1 instance |
| --- | --- | --- |
| source → compiler_IR | False | No |
| source → assembly | False | No |
| source → machine_code | False | No |
| source → microarchitecture (endpoint) | True | Yes |

- `emergent_obstruction = True`
- Endpoint verdict: `fully_admissible`
- Endpoint AC vector: AC1=T, AC2=T, AC3=T, AC4=T, AC5=T, AC6=T, AC7=T
- Obstruction first appears at: `microarchitecture`

The 3-patch gluing contradiction at microarchitecture:
```
access_level =  cache_state  (speculation fills cache with secret-dependent entries)
cache_state  =  timing       (hit vs miss latency)
access_level ≠  timing       (security policy: timing must not reveal access level)
```
A=B, B=C, A≠C — the same finite H¹ gluing obstruction pattern as
Nielsen-Ninomiya and CAP theorem.

### Stepwise Chain (Propagation)

`source_code → compiler_IR → assembly (obstructed) → machine_code (obstructed)`

| Checkpoint pair | AC6 | PO1 instance |
| --- | --- | --- |
| source → compiler_IR | False | No |
| source → assembly | True | Yes |
| source → machine_code (endpoint) | True | Yes |

- `stepwise_propagation = True`
- Endpoint verdict: `fully_admissible`
- Obstruction first appears at: `assembly`

### Absorbed Chain (Negative Control)

`source_code → unoptimized_IR (obstructed) → optimized_IR (clean) → assembly (clean)`

| Checkpoint pair | AC6 | PO1 instance |
| --- | --- | --- |
| source → unoptimized_IR | True | Yes |
| source → optimized_IR | False | No |
| source → assembly (endpoint) | False | No |

- `absorbed_obstruction = True`
- Endpoint verdict: `non_admissible_no_new_obstruction`
- Obstruction first appears at: `unoptimized_IR`

## PO1 Chain Theorem (T34)

A chained projection is a PO1 instance when its endpoint pair satisfies
AC1-AC7, independent of whether any source→intermediate pair in the chain is a
PO1 instance.

EMERGENT CASE: the obstruction at the endpoint can be invisible when projecting
from source to any strict intermediate level Li; only the full chain endpoint
reveals the PO1 instance.

ABSORBED CASE: a PO1 instance visible at an intermediate level can be resolved
before the endpoint; the chain theorem does not guarantee PO1 persists.

## Boundary

- The chain theorem characterizes the endpoint pair only; it does not localize
  which step introduced the obstruction.
- The Spectre model captures structural security policy contradiction, not
  probabilistic timing semantics or micro-op scheduling.
- The optimized_IR level in the absorbed chain has a higher accessible_support
  than the unoptimized input — optimizer recovery is a boundary of the current
  T26 monotone-restriction morphism formalism.

## Test Suite

41 tests, 41 passed.

```
python -m pytest tests/test_po1_chained_projection.py -v
```

## Reproducible Run

```
python -m models.run_t34
```

Output: `results/po1-chained-projection-v0.1.json`
