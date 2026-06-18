# T37: Typed Transport Network — v0.1 Results

## Evidence Verdict

**Path-dependent admissibility witnessed.** Two simple paths between the same
source and target layer yield different PO1 verdicts when they accumulate
different forgotten_structure. The theorem is executable and the counterexample
is preserved.

## Networks Analyzed

### Spectre Network (linear, 3 layers)

```
SRC (rich, unobstructed)
  --[type_guarantee forgotten, ALL_4 dims]--> MID (restricted, unobstructed)
  --[nothing forgotten, ALL_4 dims]---------> TGT (restricted, obstructed)
```

| Path | Verdict | AC5 | Forgotten |
| --- | --- | --- | --- |
| SRC -> MID -> TGT | fully_admissible (PO1) | True | ("type_guarantee",) |
| SRC -> MID (partial) | non_admissible_no_new_obstruction | — | ("type_guarantee",) |

**Partial path fails AC6** because MID has no gluing obstruction. The endpoint
pair (SRC, TGT) is PO1-admissible while no partial prefix (SRC, MID) is PO1.
This is emergent obstruction — the same pattern confirmed in T34 — now
reproducible via the network formalism.

**T34 consistency: True.**

### Diamond Network (4 layers, branching)

```
SRC --[type_guarantee forgotten, ALL_4 dims]--> L_A --[nothing]--> TGT
SRC --[nothing, 3 dims only]-----------------> L_B --[nothing]--> TGT
```

| Path | Verdict | Failed | Forgotten |
| --- | --- | --- | --- |
| SRC -> L_A -> TGT | fully_admissible (PO1) | — | ("type_guarantee",) |
| SRC -> L_B -> TGT | non_admissible_no_forgotten_structure | AC5 | () |

**Path-dependent admissibility confirmed.** Both paths connect SRC
(unobstructed, rich profiles) to TGT (obstructed, restricted profiles). AC1,
AC2, AC3, AC4, AC6, AC7 pass for both paths — they depend only on the
endpoint systems. Only AC5 varies:

- Path via L_A: accumulated forgotten_structure = ("type_guarantee",);
  composed morphism has local_profiles_preserved = False → AC5 passes.
- Path via L_B: accumulated forgotten_structure = (); AC5 fails regardless
  of profile behavior.

**Path dependence witness:**

| Field | Value |
| --- | --- |
| source | SRC |
| target | TGT |
| PO1 path | SRC → L_A → TGT |
| non-PO1 path | SRC → L_B → TGT |
| PO1 forgotten | ("type_guarantee",) |
| non-PO1 forgotten | () |
| failing conditions | ("AC5",) |

## Theorem

**Path-Dependent Admissibility:** In a TypedTransportNetwork, two simple paths
between the same source and target layer yield different PO1 verdicts when they
accumulate different forgotten_structure. AC1, AC2, AC3, AC6, AC7 are
endpoint-determined and path-invariant. Only AC5 (informative forgetting) can
vary by path when paths accumulate genuinely different forgotten_structure.

## Boundary

- The result holds within AC1-AC7. Only AC5 has been shown to vary by path.
- Morphism composition (intersection of preserved_dimensions) has not been
  proven associative. The composition law remains an open formal obligation.
- The result requires genuinely different accumulated forgotten_structure
  between paths; it does not apply when all paths forget the same structure.

## New Formal Object

**TypedTransportNetwork** is a new primitive above D1RestrictionSystem:

| Component | Role |
| --- | --- |
| NetworkLayer | a named D1RestrictionSystem |
| NetworkTransport | a typed morphism with forgotten/preserved declarations |
| NetworkPath | a simple path as an ordered sequence of transports |
| PathAdmissibility | PO1 verdict for a path's endpoint case |
| PathDependenceWitness | two paths with different PO1 verdicts |
| TypedTransportNetwork | a finite directed graph of layers and transports |

**Operations:**

| Operation | Behavior |
| --- | --- |
| `_compose_morphisms(f, g)` | chains site maps; intersects preserved_dimensions |
| `_path_accumulated_forgotten(path)` | union of forgotten_structure across transports |
| `all_paths(network, src, tgt)` | DFS simple-path enumeration |
| `check_path_admissibility(network, path)` | AC1-AC7 check for path's endpoint case |
| `analyze_network(network, src, tgt)` | full analysis with path-dependence detection |

## Test Suite

57 tests, all passing. Classes:
- TestNetworkConstruction (12)
- TestMorphismComposition (5)
- TestPathEnumeration (7)
- TestForgottenAccumulation (4)
- TestSpectreAdmissibility (5)
- TestDiamondAdmissibility (5)
- TestNetworkAnalysis (12)
- TestT34Consistency (1)
- TestT37Result (7)

## What This Does Not Claim

- The composition law (associativity, identity morphisms) has not been proven.
- Path-dependence via AC1-AC4 or AC6-AC7 has not been demonstrated; only AC5
  has been shown to vary by path in the tested networks.
- The network formalism has not yet been tested on hostile non-physics domains.
- No claim is made about infinite networks, continuous transport, or networks
  where paths have more than two intermediate layers.

## Next Steps

1. Prove or disprove associativity of D1RestrictionMorphism composition.
2. Test whether path-dependence can arise from AC1-AC4 or AC6-AC7 differences.
3. Determine whether a canonical minimal forgotten_structure exists for a given
   (source, target) endpoint pair.
4. Apply the discovery engine (T35) to generate TypedTransportNetwork instances
   without domain-specific heuristics.
5. Test the network formalism on hostile non-physics domains (T30 extension).
