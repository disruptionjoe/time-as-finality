# Technical Report: PO1 Chained Projection Analysis (T34) — v0.1

## Summary

T34 asks whether PO1 extends naturally to chains of projections. The key
question: can a finite gluing obstruction emerge from the full chain
(source→endpoint) even when no partial prefix of the chain (source→Li) is
individually a PO1 instance?

Three chain shapes are analysed. All three are confirmed by the finite model:

| Chain shape | Description | Confirmed |
| --- | --- | --- |
| Emergent obstruction | Endpoint is PO1; no source→intermediate is PO1 | Yes |
| Stepwise propagation | Obstruction appears mid-chain; endpoint is PO1 | Yes |
| Absorbed obstruction | Obstruction appears mid-chain; endpoint is NOT PO1 | Yes |

## Background

T33 derives PO1's admissibility conditions (AC1-AC7, compressed to 6 by T32)
from two frameworks:

- **IPT** (Invariant-Preservation Theorem): derives AC1, AC2, AC3, and
  AC5-measurable (partial).
- **RMT** (Resource-Monotonicity Theorem): derives AC4, AC5-measurable, AC6,
  AC7.
- **P5** (Informative Forgetting, proposed): covers AC5-naming — the only
  condition not derivable from either IPT or RMT.

T34 applies this fully-derived PO1 schema to a hostile multi-step domain:
the code-to-transistors compilation chain. Each step in the chain is a
D1RestrictionMorphism in the T26 formalism. The test asks whether PO1 instances
can be compositely emergent — invisible at every strict prefix but present at
the full chain level.

## Model

Each system in the chain is a `D1RestrictionSystem` with three sites and
optionally a 3-patch gluing contradiction. Profiles (`D1Profile`) encode
structural richness at each abstraction level.

### Spectre Chain: Emergent Obstruction

```
source_code (D1Profile(4,4,2,4))
    → compiler_IR (D1Profile(3,3,2,3))        [no obstruction]
    → assembly (D1Profile(2,2,1,2))            [no obstruction]
    → machine_code (D1Profile(1,1,1,1))        [no obstruction]
    → microarchitecture (D1Profile(1,1,0,1))   [3-patch obstruction]
```

The 3-patch contradiction at microarchitecture models the Spectre timing side
channel:

```
access_level = cache_state   (speculative execution fills cache based on secret)
cache_state  = timing        (cache hit vs miss latency)
access_level ≠ timing        (security policy: timing must not reveal access level)
```

This is the A=B, B=C, A≠C finite H¹ gluing obstruction — the same pattern as
the Nielsen-Ninomiya no-go theorem and the CAP theorem, validated in T27-T29.

Checkpoint pairs check admissibility of (source_code, Li) for each intermediate
level Li. All three intermediate checkpoints fail AC6 (their targets are
unobstructed) and are therefore not PO1 instances. Only the full endpoint pair
(source_code, microarchitecture) is a PO1 instance.

**Emergent obstruction confirmed.**

### Stepwise Chain: Propagation

```
source_code (D1Profile(4,4,2,4))
    → compiler_IR (D1Profile(3,3,1,3))         [no obstruction]
    → assembly (D1Profile(2,2,1,2))             [3-patch obstruction]
    → machine_code (D1Profile(1,1,0,1))         [3-patch obstruction]
```

The register coloring obstruction appears at the IR→assembly step. The
checkpoint pair (source_code, assembly) is individually a PO1 instance. The
endpoint pair (source_code, machine_code) is also a PO1 instance.

**Stepwise propagation confirmed.**

### Absorbed Chain: Negative Control

```
source_code (D1Profile(4,4,2,4))
    → unoptimized_IR (D1Profile(2,2,1,2))       [3-patch obstruction]
    → optimized_IR (D1Profile(3,3,2,3))          [no obstruction]
    → assembly (D1Profile(1,1,1,1))              [no obstruction]
```

A phi-node contradiction at the unoptimized IR level is resolved by dead-code
elimination before assembly. The checkpoint pair (source_code, unoptimized_IR)
is a PO1 instance. The endpoint pair (source_code, assembly) is NOT — AC6 is
False at the endpoint, yielding verdict `non_admissible_no_new_obstruction`.

**Absorbed obstruction confirmed.**

## PO1 Chain Theorem (T34)

> A chained projection `L0 → L1 → ... → Ln` is a PO1 instance when its
> endpoint pair `(L0, Ln)` satisfies AC1-AC7, independent of whether any
> source→intermediate pair `(L0, Li)` in the chain is a PO1 instance.
>
> EMERGENT CASE: the obstruction at `Ln` can be invisible when projecting from
> `L0` to any strict intermediate level; only the full chain endpoint reveals
> the PO1 instance.
>
> ABSORBED CASE: a PO1 instance visible at an intermediate pair `(L0, Li)` is
> not guaranteed to persist to the endpoint; the chain can absorb the
> obstruction if later steps restore the missing structure.

## Boundary Conditions

- The chain theorem characterises the endpoint pair only. It does not localise
  which step in the chain introduced the obstruction.
- The Spectre model captures the structural security policy contradiction as a
  finite gluing obstruction. It does not model probabilistic timing differences,
  branch prediction micro-op semantics, or hardware-specific cache geometry.
- The optimized_IR level in the absorbed chain has a higher `accessible_support`
  than the unoptimized input. This models the optimizer recovering structure and
  marks a **boundary of the current T26 morphism formalism**: the formalism
  generally expects non-increasing profiles under restriction, and optimization
  passes that increase profile values are not a standard D1RestrictionMorphism
  in the intended direction.

## AC5 Accumulation

In all three chains, `forgotten_structure` at the endpoint is declared as the
union of structure lost across all steps. This is modelled by explicit naming in
`ProjectionCase.forgotten_structure`. A formal composition law that accumulates
AC5 automatically across steps is left as the principal open contribution.

## Evidence

41 unit tests, all passing.

```
python -m pytest tests/test_po1_chained_projection.py -v
# 41 passed, 7 subtests passed in 0.12s
```

Reproducible output: `results/po1-chained-projection-v0.1.json`

## Contribution Needed

1. **Chain composition theorem**: given a chain of D1RestrictionMorphisms
   `f1∘f2∘...∘fn: L0→Ln`, derive conditions under which the composed projection
   is a PO1 instance without checking each intermediate pair individually.

2. **Cumulative AC5 rule**: endpoint `forgotten_structure` should be the union
   of structure forgotten at each step, not just the explicitly declared name at
   the endpoint level.

3. **Non-monotone morphisms**: a morphism type that permits optimization passes
   (structure recovery) within the T26 formalism, alongside the standard
   restriction direction.

## Relation to Prior Tests

| Test | Connection |
| --- | --- |
| T27 | Establishes the 3-patch H¹ gluing obstruction pattern used at microarchitecture |
| T28 | Validates the same obstruction pattern for CAP (distributed consensus) |
| T29 | Defines the finite PO1 schema applied to each checkpoint pair |
| T31 | Seven-condition AC1-AC7 checklist used by check_admissibility |
| T32 | Confirms AC4 derives from AC6; minimal basis used throughout |
| T33 | IPT/RMT derivation of conditions; P5 (Informative Forgetting) applied to endpoint AC5 |
