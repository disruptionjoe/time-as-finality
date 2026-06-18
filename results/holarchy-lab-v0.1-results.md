# T40: Holarchy Lab — Results v0.1

**Status:** implemented  
**Tests:** 45/45 pass  
**Best-supported hypothesis:** H_B  
**Model:** `models/holarchy_lab.py`

## Central Finding

Holonic emergence is confirmed: cross-level constraints in a HolonicNetwork
can create a holonic obstruction even when every micro node is individually
satisfiable. This refutes H_A (holonic finality reduces to micro finality).

Holonic PO1 requires named cross-level forgotten structure (AC5): the control
case (source satisfiable + target obstructed + empty forgotten_dims) is not
admissible. Named cross-level AC5 is necessary.

## Scenario Results

| Scenario | All micro sat. | Holonic sat. | Emergence | Obstruction source |
| --- | --- | --- | --- | --- |
| holonic_flat | True | True | False | none |
| holonic_compatible_different | True | True | False | none |
| holonic_emergent | True | False | **True** | holonic_emergence |
| holonic_micro_obstructed | False | False | False | micro_only |

## Theorem 1 — Holonic Emergence

> In a HolonicNetwork, a holonic obstruction can arise from cross-level
> constraints even when every micro node is individually satisfiable.

Minimum case: 3 nodes in a directed triangle.
- Node A: a1=a2 (same internal)
- Node B: b1=b2 (same internal)
- Node C: c1=c2 (same internal)
- Cross A→B: a2=b1 (same)
- Cross B→C: b2=c1 (same)
- Cross A→C: a2≠c1 (different) ← negative cycle

The A→B→C chain forces a1=a2=b1=b2=c1=c2. The A→C shortcut forces a2≠c1.
Combined: contradiction. Holonic obstructed; 0 witnesses.

Each micro node is individually satisfiable (2 witnesses each). Each pair of
cross-level edges is locally satisfiable. The three-way combination is obstructed.

This is structurally equivalent to the T26/T39 minimum transitive obstruction —
the same signed-graph negative cycle shifted from within-level to cross-level.

## Theorem 2 — Cross-Level AC5

> Holonic PO1 admissibility requires non-empty forgotten_dims at the cross-level
> morphism.

| Bridge case | Source sat. | Target obstructed | AC5 fires | Admissible |
| --- | --- | --- | --- | --- |
| holonic_po1_main | True | True | True | **True** |
| holonic_po1_no_forgotten_control | True | True | False | False |

The control case demonstrates that source-satisfiable + target-obstructed is
insufficient without named cross-level forgotten structure. The named forgotten
structure (`a1-b2-compatibility`) identifies WHICH cross-level compatibility was
lost in the projection, making the holonic obstruction causally attributed.

## Hypothesis Verdicts

**H_A** (holonic finality reduces to micro finality): **rejected**  
One emergence case falsifies the reduction hypothesis.

**H_B** (holonic finality is genuinely independent): **best supported**  
Holonic emergence is confirmed. The flat and compatible-different scenarios
show that cross-level edges do not automatically obstruct — the topology matters.

**H_C** (cross-level AC5 necessary for holonic PO1): **supported**  
All tested cases are consistent with necessity. The sample is small (1 admissible
+ 1 control); a broader parameter sweep would strengthen the claim.

## Boundary

- Results for binary {-1,1} domains with same/different constraints.
- HolonicNodes are D1RestrictionSystems; full second-level nesting (TypedTransportNetworks
  as nodes) not yet implemented.
- Parameter space: 4 scenarios, 2 PO1 bridges. A broader enumeration is needed.
- No absorption case: if any micro node is obstructed, the holonic network is also
  obstructed (strict holonic satisfiability propagates micro obstruction).

## Next Steps

1. Extend nodes to TypedTransportNetworks for genuine second-level nesting.
2. Parameter sweep over cross-level topologies (all signed-graph configurations on
   3-5 nodes) to exhaustively characterize emergence vs. reduction.
3. Compare holonic global section to Cech H¹ cohomology (T13).
4. Test holonic AC5 against T32 minimal basis: is it the same condition at a higher scale?
