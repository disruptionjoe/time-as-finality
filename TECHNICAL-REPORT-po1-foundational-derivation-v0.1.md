# Technical Report: PO1 Foundational Derivation (T33) v0.1

## Overview

This report documents the T33 analysis of whether the PO1 Projection-Obstruction
Schema's admissibility conditions arise from two candidate mathematical frameworks:

- **IPT** (Invariant-Preservation Theorem): local-to-global consistency of
  structural invariants
- **RMT** (Resource-Monotonicity Theorem): global satisfiability resource
  is non-increasing under restriction projection

The analysis builds directly on T32's result that the seven T31 conditions
compress to six (AC4 derives from AC6 via T26 semantics) organized under four
structural principles.

## Mathematical Setup

### Resource State

For a D1RestrictionSystem S, the **global satisfiability resource** is:

```
R(S) = global_assignment_exists ∈ {True, False}
```

Equivalently (in 0/1 encoding):
- R = 1 if S has a global assignment (unobstructed, or no patches)
- R = 0 if S has no global assignment (obstructed)

This is distinct from `global_witness_count` because systems with no patches
return `global_witness_count=0` but `global_assignment_exists=True` (trivially
satisfied). The resource is the boolean, not the raw count.

### Invariant Level

For a D1RestrictionSystem S:
- Level 0 (H⁰ clear): global section exists
- Level 1 (H¹ obstruction): all patches locally satisfiable, no global section
- Level -1 (H⁰ failure): at least one patch locally inconsistent

A PO1 projection maps a system at level 0 to a system at level 1. This is the
invariant-class change that IPT detects.

### Resource Monotone

For a projection f: S_r → S (restricted → richer in T31 notation):

```
M(f) = R(richer) - R(restricted) ∈ {0, 1}
```

A PO1 instance has M(f) = 1 (strict decrease). Non-PO1 projections have M(f) = 0.

## Derivation Results

### IPT Framework

IPT operates over typed invariant carriers (D1RestrictionSystems) connected by
definable morphisms (D1RestrictionMorphisms).

**Derives:**
- AC1, AC2: typing obligations on the domain of discourse
- AC3: definability obligation for the projection map
- AC4: inherits from AC6 (T26 semantics, proved by T32)
- AC5-measurable: detects local profile loss (local_profiles_preserved=False)

**Does not derive:**
- AC5-naming: requires ProjectionCase.forgotten_structure metadata
- AC6, AC7 as requirements (only as compatible consequences)

IPT can confirm *whether* the invariant carrier changed but not *that* the
change was obstructive or *what* was named.

### RMT Framework

RMT operates over the global satisfiability resource M(f).

**Derives:**
- AC6: restricted system obstructed = R(restricted) = 0
- AC7: richer system unobstructed = R(richer) = 1 (prerequisite for strict decrease)
- AC4: inherits from AC6
- AC5-measurable: strict resource decrease implies local_profiles_preserved=False

**Does not derive:**
- AC3: total site map is a morphism definition, not a resource constraint.
  A partial site map still produces a restricted system with a computable resource.
- AC1, AC2: RMT requires a computable resource, not full T26 axiom satisfaction.
- AC5-naming: resource quantity does not entail mechanism identification.

### Synthesis

IPT and RMT are complementary:

```
IPT covers: {AC1, AC2, AC3, AC4, AC5-meas}
RMT covers: {AC4, AC5-meas, AC6, AC7}
Union:      {AC1, AC2, AC3, AC4, AC5-meas, AC6, AC7}
Residual:   {AC5-naming}
```

AC5-naming — the requirement that `forgotten_structure` be non-empty — is a
methodological transparency condition that neither framework entails.

## Hypothesis Matrix

| ID | Verdict | Reason |
| --- | --- | --- |
| H0: all independent | **rejected** | AC4, AC6, AC7 demonstrably derivable; IPT derives AC1-AC3 |
| H1: IPT alone | partially_supported | IPT misses AC6, AC7 as requirements; only compatible with them |
| H2: RMT alone | partially_supported | RMT misses AC3, and full T26 typing for AC1, AC2 |
| H3: both required | **supported** | Union covers all except AC5-naming; both needed for full coverage |
| H4: deeper single principle | boundary | Local-to-global resource framing unifies IPT+RMT abstractly, but is a rephrasing not a reduction |
| H5: no derivation | **rejected** | Multiple conditions demonstrably derivable from finite executable evidence |

## Counterexamples

### 1. AC5-naming is not entailed by RMT

**Construction:** D1Profile(2,2,1,2) rich → D1Profile(1,1,0,1) restricted (obstructed). Total site map. `preserved_dimensions=("branch_support",)`. `forgotten_structure=()`.

**Result:** AC1=T, AC2=T, AC3=T, AC4=T, AC5=F, AC6=T, AC7=T.
Verdict: `non_admissible_no_forgotten_structure`.

**Shows:** A projection with complete resource decrease and measurable profile
loss is not automatically a PO1 instance if it names nothing.

### 2. AC3 is not entailed by RMT

**Construction:** Same profiles, but site_map omits C (partial map).

**Result:** AC3=F. RMT still records the resource decrease.

**Shows:** Projection definability is a morphism-definition condition, not
a consequence of the global satisfiability resource.

### 3. AC6 is not required by IPT

**Construction:** Valid typed pair, total site map, measurable profile loss,
but restricted system has no patches (no obstruction).

**Result:** AC6=F. IPT validates the typed pair and definable projection.

**Shows:** IPT does not require the restricted system to be obstructed.
Obstruction polarity comes from RMT.

## Smaller Theorem Candidate

> **PO1 as a derived theorem:**
> Given a valid morphism f: S_r → S between valid D1RestrictionSystems
> (AC1-AC3 satisfied), if S has a global section (AC7) and S_r has a proper
> H¹ finite gluing obstruction (AC6), then f witnesses a strict decrease in
> the global satisfiability resource R = [global_assignment_exists].
>
> A **PO1 instance** additionally requires the mechanism of decrease to be
> identified by name (AC5). AC5 decomposes:
> - AC5-measurable: follows from strict resource decrease (RMT)
> - AC5-naming: a methodological transparency condition (Principle P5)

This theorem candidate identifies PO1 instances as exactly those morphisms in
the category of valid D1RestrictionSystems that witness strict resource decrease
with named mechanism.

## Obstruction Classification

The T26 finite analogue of sheaf cohomology classifies obstructions as:

| Certificate type | Meaning | AC4 | AC6 |
| --- | --- | --- | --- |
| `H1_finite_gluing` | All patches local; no global section | True | True |
| `trivial_local_failure` | At least one patch inconsistent | False | False |
| `no_obstruction` | Global section exists | True | False |

PO1 instances require `H1_finite_gluing` in the restricted system and
`no_obstruction` in the richer system.

## Boundary of Current Analysis

1. **AC5-naming as P5**: The naming obligation has no derivation from IPT or RMT.
   It should be promoted to a first-class named principle (Principle P5:
   *Informative Forgetting*). T32 already noted this as non-intrinsic to
   D1RestrictionSystem.

2. **Categorical refinement**: The "category of valid D1RestrictionSystems"
   requires more development to state the theorem at full categorical generality.
   T33 works with finite executable witnesses only.

3. **Chained projections**: T33 does not analyze PO1 for compositions of
   projections (source → IR → assembly → transistors). Whether a H¹ obstruction
   can appear only after multiple forgetful steps is a candidate for T34-T35.

## Files

| File | Role |
| --- | --- |
| `models/po1_foundational_derivation.py` | Resource/invariant types, derivation attempts, hypothesis evaluators, counterexamples, T33Result |
| `models/run_t33.py` | Runner; writes JSON to results/ |
| `tests/test_po1_foundational_derivation.py` | 50 tests across 7 test classes |
| `tests/T33-po1-foundational-derivation.md` | Test specification |
| `results/po1-foundational-derivation-v0.1.json` | Full structured output |
| `results/po1-foundational-derivation-v0.1-results.md` | Summary table |

## Verdict

**H3 is the best-supported hypothesis.** PO1's admissibility conditions are
partially derived: IPT generates the typing/definability obligations and RMT
generates the obstruction polarity obligations. AC5-naming remains a
methodological transparency condition that should be elevated to Principle P5.

PO1 should be reclassified from "empirical schema" to "partially derived theorem
with one methodological boundary condition."
