# T34: Chained Projection Analysis

## Target Claims

PO1, T29, T31, T32, T33

## Setup

Three chains of D1RestrictionMorphisms are constructed, each modelling a
different pattern of obstruction propagation through a sequence of abstraction
levels:

1. **Spectre chain** — `source_code → compiler_IR → assembly → machine_code →
   microarchitecture`. At each intermediate level the system has a global
   section (no obstruction). At the microarchitecture endpoint a 3-patch
   gluing contradiction models the Spectre timing side channel: access_level
   determines cache_state (speculation), cache_state determines timing (latency
   hit/miss), security policy requires timing to be independent of access_level.
   The A=B, B=C, A≠C finite H¹ gluing obstruction is the same pattern as
   Nielsen-Ninomiya and CAP theorem cases established in T27-T29.

2. **Stepwise chain** — `source_code → compiler_IR → assembly (obstructed) →
   machine_code (obstructed)`. The register coloring obstruction appears at the
   assembly level and persists to the endpoint. The source→assembly pair is an
   individually admissible PO1 instance; the source→machine_code endpoint is
   also a PO1 instance.

3. **Absorbed chain** — `source_code → unoptimized_IR (obstructed) →
   optimized_IR (clean) → assembly (clean)`. A phi-node contradiction at the
   unoptimized IR level is resolved by dead-code elimination before assembly.
   The source→unoptimized_IR pair is a PO1 instance; the source→assembly
   endpoint is NOT (AC6=False at endpoint — no new obstruction introduced).

For each chain, `CheckpointPair` objects capture the admissibility of
(source, Li) for every intermediate level Li. `_analyze_chain` determines:
- `emergent_obstruction`: endpoint is PO1; no checkpoint pair is PO1
- `stepwise_propagation`: obstruction mid-chain; endpoint is PO1; at least one
  checkpoint pair is PO1
- `absorbed_obstruction`: obstruction mid-chain; endpoint is NOT PO1

## Success Criteria

- Spectre chain: `emergent_obstruction=True`, endpoint `fully_admissible`, all
  three checkpoint pairs have `po1_evidence=False`.
- Stepwise chain: `stepwise_propagation=True`, endpoint `fully_admissible`,
  `assembly` checkpoint has `po1_evidence=True`.
- Absorbed chain: `absorbed_obstruction=True`, endpoint verdict
  `non_admissible_no_new_obstruction`, `unoptimized_IR` checkpoint has
  `po1_evidence=True`.
- All three top-level flags in T34Result are `True`.

## Failure Criteria

- Spectre chain emergent flag is False (meaning some checkpoint pair became a
  PO1 instance — the obstruction was not truly emergent).
- Stepwise endpoint is not fully admissible (stepwise propagation failed).
- Absorbed endpoint is fully admissible (optimizer did not resolve the
  obstruction in the model).
- Any top-level confirmation flag is False.

## Known Physics Constraints

The Spectre model uses the same 3-patch A=B, B=C, A≠C gluing contradiction
structure validated in T27-T31. The physical Spectre attack involves
probabilistic timing differences and micro-op semantics not captured in the
finite graph model. The claim is structural: the security policy creates a
local-to-global constraint inconsistency at the microarchitecture level that is
invisible when projecting from source to any strict subset of the abstraction
chain.

The optimized_IR level in the absorbed chain has a higher accessible_support
than unoptimized_IR. This models the optimizer recovering structure and marks a
boundary of the current T26 morphism formalism — D1RestrictionMorphisms
generally expect non-increasing profiles under restriction, but optimization
passes can violate this.

## Contribution Needed

- A formal chain composition theorem: given f1∘f2∘...∘fn: L0→Ln where each fi
  is a D1RestrictionMorphism, derive conditions under which the composed
  projection is a PO1 instance without checking each step individually.
- A cumulative AC5 rule: endpoint forgotten_structure should be the union of
  structure forgotten at each step, not just the declared name at the endpoint
  level.
- A morphism type that permits non-monotone profile sequences (optimizer passes
  that recover structure) within the T26 formalism.
