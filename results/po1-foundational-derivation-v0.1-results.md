# T33 Results: PO1 Foundational Derivation v0.1

## Summary

T33 determines whether PO1's admissibility conditions (AC1-AC7) arise from
two deeper mathematical frameworks — IPT (Invariant-Preservation) and RMT
(Resource-Monotonicity) — or remain independent empirical conditions.

**Verdict: H3 — Both IPT and RMT are required; neither alone is sufficient.**

## Hypothesis Verdicts

| Hypothesis | Statement | Verdict |
| --- | --- | --- |
| H0 | AC1-AC7 are independent empirical conditions | **rejected** |
| H1 | All conditions arise from IPT alone | partially_supported |
| H2 | All conditions arise from RMT alone | partially_supported |
| H3 | Both IPT and RMT are required | **supported** |
| H4 | A single deeper principle exists | boundary (rephrasing of H3) |
| H5 | No derivation currently justified | **rejected** |

## Derivation Matrix

### IPT (Invariant-Preservation Theorem)

| Condition | Status | Notes |
| --- | --- | --- |
| AC1 | derived | Typing obligation for richer D1RestrictionSystem |
| AC2 | derived | Typing obligation for restricted D1RestrictionSystem |
| AC3 | derived | Total site map makes projection definable |
| AC4 | derived | Inherits from AC6 via T26 semantics (T32 result) |
| AC5 (measurable) | partially_derived | Profile loss detectable; naming requires metadata |
| AC5 (naming) | **independent** | Requires ProjectionCase.forgotten_structure; outside IPT |
| AC6 | partially_derived | Compatible consequence of IPT; not a requirement |
| AC7 | partially_derived | Compatible consequence of IPT; not a requirement |

### RMT (Resource-Monotonicity Theorem)

| Condition | Status | Notes |
| --- | --- | --- |
| AC1 | partially_derived | Needs computable resource, not full T26 axioms |
| AC2 | partially_derived | Same as AC1 |
| AC3 | **not_applicable** | Total site map is morphism definition, not resource constraint |
| AC4 | derived | Inherits from AC6 via T26 semantics |
| AC5 (measurable) | **derived** | Strict resource decrease implies measurable profile loss |
| AC5 (naming) | **independent** | Resource quantity does not entail mechanism naming |
| AC6 | **derived** | Restricted system obstructed = resource dropped to zero |
| AC7 | **derived** | Richer system unobstructed = resource was positive before |

## Conditions Coverage by Principle

| Coverage | Conditions |
| --- | --- |
| IPT covers | AC1, AC2, AC3, AC4, AC5-measurable (partial) |
| RMT covers | AC4, AC5-measurable, AC6, AC7 |
| Both together cover | AC1, AC2, AC3, AC4, AC5-measurable, AC6, AC7 |
| Neither covers | **AC5-naming** |

## Resource Monotone Witnesses

All four T31 positive cases show strict resource decrease:

| Case | Richer resource | Restricted resource | Strictly decreasing |
| --- | --- | --- | --- |
| witten_1981 | 1 (section exists) | 0 (obstructed) | yes |
| nielsen_ninomiya | 1 (section exists) | 0 (obstructed) | yes |
| cap_theorem | 1 (section exists) | 0 (obstructed) | yes |
| git_semantic_merge | 1 (section exists) | 0 (obstructed) | yes |

## Counterexamples

Three finite counterexamples establish the boundaries:

### 1. AC5-naming independence from RMT
- Systems with resource drop, measurable profile loss, total site map
- `forgotten_structure=()` → AC5=False despite complete resource decrease
- **Shows:** RMT does not entail the naming obligation

### 2. AC3 independence from RMT
- Systems with resource drop and partial site map (C not mapped)
- AC3=False; RMT records decrease regardless
- **Shows:** Total site map is a morphism definition, not a resource constraint

### 3. AC6 independence from IPT
- Valid typed pair with total site map and measurable profile loss
- Restricted system has no obstruction (no patches)
- **Shows:** IPT validates structural change without requiring obstruction

## Smaller Theorem Candidate

> Given a valid morphism f: S_r → S between valid D1RestrictionSystems
> (AC1-AC3 satisfied), if S has a global section (AC7) and S_r has a proper
> H¹ finite gluing obstruction (AC6), then f witnesses a strict decrease in
> the global satisfiability resource R = [global_assignment_exists].
> A full PO1 instance additionally requires the mechanism of decrease to be
> identified by name (AC5). AC5 decomposes: the measurable-loss half follows
> from RMT; the naming half is a methodological transparency condition that
> neither IPT nor RMT entail.

## Remaining Independence

**AC5-naming** is the only condition not derivable from either IPT or RMT.
It requires `ProjectionCase.forgotten_structure` metadata — a named list of
what the projection forgets — which lives outside the D1RestrictionSystem
lattice both principles operate over.

## Recommendation

PO1 should be treated as a **partially derived theorem**:
- AC1-AC4, AC6, AC7, and AC5-measurable are derivable from IPT+RMT
- AC5-naming is a methodological transparency condition that should be
  promoted to a first-class named obligation (Principle P5)

Proposed revision:  
*"A projection is a PO1 instance iff it is a valid typed morphism (IPT)
witnessing strict resource decrease (RMT) with named mechanism (P5)."*

## T32 Basis (Inherited)

- Minimal condition basis: AC1, AC2, AC3, AC5, AC6, AC7
- Impossible condition vectors: 32 (AC6=True and AC4=False)
- Feasible condition vectors: 96
- T32 best hypothesis: "H2 with H4 boundary"
- T33 advances this to: **H3** (IPT + RMT, with AC5-naming as P5)
