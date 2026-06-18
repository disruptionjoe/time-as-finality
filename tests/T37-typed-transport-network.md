# T37: Typed Transport Network

## Target Claims

- TypedTransportNetwork as the next formal object above D1RestrictionSystem
- PO1 admissibility can be path-dependent within a network
- D1RestrictionMorphism composition (intersection of preserved_dimensions)
- T34 emergent obstruction pattern is reproducible via the network formalism

## Setup

A TypedTransportNetwork is a finite directed graph where:
- **Nodes** are NetworkLayer objects (each wrapping a D1RestrictionSystem)
- **Edges** are NetworkTransport objects (each wrapping a D1RestrictionMorphism
  plus explicit forgotten_structure and preserved_structure declarations)

Two test networks:

**spectre_network** (linear, 3 layers):
```
SRC (rich, unobstructed) --[type_guarantee forgotten]--> MID (restricted, unobstructed)
                         --[nothing forgotten]--> TGT (restricted, obstructed)
```

**diamond_network** (4 layers, branching):
```
SRC --[type_guarantee forgotten]--> L_A --[nothing]--> TGT
SRC --[nothing, 3 dims only]-----> L_B --[nothing]--> TGT
```

For each network, the model:
1. Enumerates all simple paths via DFS
2. Composes morphisms along each path (intersection of preserved_dimensions)
3. Accumulates forgotten_structure (union across transports)
4. Checks PO1 admissibility of each path's endpoint case

## Success Criteria

- Spectre network: single path SRC→MID→TGT is PO1-admissible
- Spectre partial path SRC→MID: NOT PO1 (AC6 fails; MID unobstructed)
- T34 consistency: endpoint PO1 + partial not PO1 = emergent obstruction
- Diamond path via L_A: PO1-admissible (forgotten = ("type_guarantee",), AC5 passes)
- Diamond path via L_B: NOT PO1 (forgotten = (), AC5 fails)
- Diamond network: path_dependent = True
- Witness: same source/target, different paths, different PO1 verdicts
- Witness failing_conditions = ("AC5",)

## Failure Criteria

- If both diamond paths give the same PO1 verdict: path-dependence is not witnessed
- If the spectre partial path is PO1: emergent obstruction claim fails
- If composition does not correctly intersect preserved_dimensions: AC5 results corrupt
- If validate_system fails on any layer: admissibility checks are invalid

## Known Constraints

- The path-dependence result holds within AC1-AC7. Only AC5 varies by path;
  AC1, AC2, AC3, AC6, AC7 are endpoint-determined and path-invariant.
- Morphism composition law (associativity, identity) is not yet proven.
  The intersection of preserved_dimensions is the natural candidate but requires
  a formal proof before the composition can be called a category.
- The 3-site gluing obstruction (A=B, B=C, A≠C) is the same obstruction model
  used in T26-T29.

## Contribution Needed

- Test longer chains (4+ intermediate layers) for path-dependence
- Determine whether a canonical minimal forgotten_structure exists for a given
  (source, target) endpoint pair
- Prove or disprove associativity of D1RestrictionMorphism composition
- Determine whether path-dependence can arise from AC1-AC4 or AC6-AC7 differences
  (currently only AC5 has been shown to vary by path)
