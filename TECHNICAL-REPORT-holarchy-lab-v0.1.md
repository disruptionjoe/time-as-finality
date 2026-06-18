# Technical Report: Holarchy Lab (T40) v0.1

**Status:** implemented  
**Tests:** 45/45 pass  
**Best-supported hypothesis:** H_B  
**Model:** `models/holarchy_lab.py`

---

## 1. Motivation

The Time as Finality research program asks how stable structure is preserved,
transformed, forgotten, and newly created as it moves across recursively nested
organizational levels. T37 and T38 established the minimal transport formalism
for a single level of nesting (TypedTransportNetwork + CompressionRecord +
EmergenceRecord). T39 showed that the gluing obstruction is a parity-conflicting
binary CSP.

T40 asks the next question: **does a second level of nesting (networks whose
nodes are themselves networks) produce genuinely new obstruction phenomena, or
does it reduce to flat CSP?**

A holarchy is a system of nested wholes where each level is simultaneously a
whole relative to its components and a part relative to the level above. In the
TypedTransportNetwork formalism, this suggests nodes that are themselves networks,
connected by cross-level typed constraints.

---

## 2. Setup

### 2.1 Holarchy primitives

A `HolonicNetwork` has:

- **HolonicNodes**: each a `D1RestrictionSystem` with designated `entry_site` and
  `exit_site` — the canonical interface variables at which cross-level constraints attach.
- **HolonicEdges**: cross-level `PatchConstraints` connecting the exit site of one node
  to the entry site of another, plus an optional `forgotten_dims` annotation.

**Holonic global section (strict)**: all patches from all micro nodes AND all cross-level
patches from all edges are jointly satisfiable. This is equivalent to the signed-graph
parity check (Theorem 2 of T39) applied to the combined constraint set.

This is a strict definition: if any micro node is obstructed, the holonic network is
also obstructed. This is the correct baseline — absorption (micro obstructed but macro
satisfiable) is not tested here because it requires a weaker definition of holonic
satisfiability (macro-only patches).

### 2.2 Scenarios

Four scenarios cover the relevant cases:

| Scenario | Description | Micro | Holonic | Emergence |
| --- | --- | --- | --- | --- |
| holonic_flat | 2 nodes, same cross-edge | ✓ | ✓ | No |
| holonic_compatible_different | 2 nodes, different cross-edge | ✓ | ✓ | No |
| holonic_emergent | 3-node triangle, negative cycle | ✓ | ✗ | **Yes** |
| holonic_micro_obstructed | 2 nodes, one micro obstructed | ✗ | ✗ | No |

Two PO1 bridge cases:
- `holonic_po1_main`: AC5 fires, admissible.
- `holonic_po1_no_forgotten_control`: AC5 empty, not admissible.

---

## 3. Theorems

### Theorem 1 — Holonic Emergence

> In a HolonicNetwork, a holonic obstruction can arise from cross-level constraints
> even when every micro node is individually satisfiable.

**Proof witness:** the 3-node triangle scenario.

Nodes A, B, C each have one internal "same" patch (satisfiable: 2 witnesses each).
Cross-level edges: A→B (same), B→C (same), A→C (different).

Combined signed graph: a1-a2 (same), b1-b2 (same), c1-c2 (same), a2-b1 (same),
b2-c1 (same), a2-c1 (different). The chain a2=b1=b2=... with the transitive parity
forces a2=c1, contradicting a2≠c1. Negative cycle detected; 0 witnesses.

**Structural observation:** this is exactly the T26/T39 minimum transitive obstruction
(A=B, B=C, A≠C) applied at the cross-level layer rather than the within-level layer.
Holarchic structure does not create new obstruction mathematics; it re-applies the same
parity mechanism at a higher level of organization.

**Corollary:** holonic emergence requires at least 3 nodes and a directed triangle of
cross-level constraints. A 2-node holonic network cannot have holonic emergence from
cross-level same/different constraints alone (2 variables, 2 constraints in a cycle
would require self-loops or multi-edges, which are not physical).

### Theorem 2 — Cross-Level AC5

> Holonic PO1 admissibility requires non-empty `forgotten_dims` at the cross-level
> morphism.

The standard AC5 condition (from T31/T32) states: the typed morphism must declare
what named structure was forgotten. T40 extends this to the holonic level: the
cross-level morphism from a richer holonic network to a restricted holonic network
must declare what cross-level structure was forgotten.

**Control case** (`holonic_po1_no_forgotten_control`): source holonically satisfiable,
target holonically obstructed, but `forgotten_dims = ()`. Not admissible.

**Admissible case** (`holonic_po1_main`): source holonically satisfiable, target
holonically obstructed, `forgotten_dims = ("a1-b2-compatibility",)`. Admissible.

The named forgotten structure identifies WHICH cross-level compatibility was lost —
making the holonic obstruction causally attributed rather than accidentally co-occurring.
This is exactly the T39 observation that AC5 is the layer of PO1 not expressible in
standard CSP.

---

## 4. Hypothesis Verdicts

### H_A — Holonic finality reduces to micro finality

**Verdict: rejected.**

If H_A were true, every holonically obstructed network would have at least one
micro-obstructed node. The emergent scenario falsifies this: all three micro nodes
are satisfiable (2 witnesses each), but the holonic network is obstructed (0 witnesses).

### H_B — Holonic finality is genuinely independent

**Verdict: best supported.**

Holonic emergence is confirmed and is topology-dependent. The flat scenario (same
cross-edge) and the compatible-different scenario (different cross-edge) both produce
holonically satisfiable networks, showing that cross-level edges do not automatically
obstruct. The emergent scenario (triangle) shows that with the right topology, holonic
emergence is possible from fully micro-compatible nodes.

### H_C — Cross-level AC5 is necessary for holonic PO1

**Verdict: supported (not fully confirmed).**

Every admissible holonic PO1 case (1 of 1 tested) has non-empty `forgotten_dims`.
The control case with empty `forgotten_dims` is not admissible despite satisfying
source-satisfiable + target-obstructed. The sample is small; a parameter sweep
would strengthen the claim.

---

## 5. Connection to Prior Tests

| Test | Connection |
| --- | --- |
| T26 | Minimum transitive obstruction (3-site case) is the structural skeleton of holonic emergence |
| T39 | Holonic obstruction = cross-level parity conflict (same math, different level) |
| T37 | TypedTransportNetwork is the base formalism; T40 asks the next level up |
| T38 | EmergenceRecord tracks structure-creation at target; T40 Holonic Emergence is emergence at the cross-level |
| T32 | AC5 is the key non-derivable admissibility condition; T40 Cross-Level AC5 applies the same condition holonically |

---

## 6. Boundary Conditions and Limitations

**What T40 tests:**
- One level of holarchic nesting (D1RestrictionSystems as nodes).
- Binary {-1,1} domains with same/different constraints.
- 4 scenarios + 2 PO1 bridges (small parameter space).

**What T40 does not test:**
- Full second-level nesting (TypedTransportNetworks as nodes — networks of networks).
- Holonic absorption: micro obstructed but macro satisfiable under a weaker definition
  of holonic satisfiability.
- Parameterized exploration: all cross-level topologies on 3-5 nodes.
- Connection to sheaf cohomology (T13): the holonic global section may correspond to
  a Cech H¹ obstruction class.

---

## 7. Relation to Original Holarchy Lab Proposal

The original Holarchy Lab request (H1-EXT-001) proposed a `HolonicNode` class,
50 Monte Carlo simulations, and statistical success criteria. T40 redrafts this to
fit repo conventions:

| Original | T40 equivalent |
| --- | --- |
| HolonicNode class | `HolonicNode` dataclass wrapping `D1RestrictionSystem` |
| 50 Monte Carlo simulations | 4 deterministic finite scenarios + 2 PO1 bridges |
| Statistical success criteria | Hypothesis verdicts H_A/H_B/H_C with falsifiable conditions |
| "Emergent Holonic Finality" | Holonic Emergence Theorem (Theorem 1) |
| Cross-level transport | `HolonicEdge` with `forgotten_dims` annotation |

The key translation: Monte Carlo is replaced by exhaustive small-case construction.
The repo's approach is to build the smallest case that witnesses or refutes a claim —
a single emergent obstruction case has more epistemic weight than 50 random simulations
because it provides an explicit falsifying/confirming witness.

---

## 8. Next Steps

1. **Second-level nesting**: replace HolonicNodes (D1RestrictionSystems) with
   TypedTransportNetworks to implement the full "networks of networks" holarchy.

2. **Parameter sweep**: enumerate all signed-graph configurations on 3-5 holonic
   nodes and classify which topologies produce emergence, reduction, or absorption.

3. **Holonic H¹**: compare the holonic global section condition to T13's Cech
   cohomology obstruction. If the holonic obstruction corresponds to a nontrivial
   H¹ class, holarchic structure connects to topological obstruction theory.

4. **Cross-level AC5 derivation**: determine whether holonic AC5 is a strict
   strengthening of T32's minimal basis or collapses to the same four-principle
   basis at the holonic level.
