# T40: Holarchy Lab — Emergent Holonic Finality via Recursive Typed Transport

## Target Claims

- D1RestrictionSystem (micro level)
- PO1 (Projection-Obstruction Principle)
- TTN (TypedTransportNetwork)
- MMT (Minimal Multiscale Transport, T38)
- CSP-PO1 (T39 — holonic obstruction is a cross-level parity conflict)
- T26 (3-site transitive obstruction — minimum holonic emergence case)

## Central Question

In a HolonicNetwork (directed graph of D1RestrictionSystems connected by
cross-level typed constraints), does macro-level finality (holonic global section)
emerge from or reduce to micro-level finality?

Specifically:
- Can cross-level constraints create holonic obstructions from micro-compatible systems?
- Is named cross-level forgotten structure (AC5) necessary for holonic PO1?

## Setup

A HolonicNetwork has:
- **HolonicNodes**: D1RestrictionSystems with designated entry and exit interface sites.
- **HolonicEdges**: cross-level PatchConstraints connecting exit sites of one node to
  entry sites of another, with optional `forgotten_dims` annotation.

Holonic global section (strict): ALL micro patches (from each node's system) AND all
cross-level patches (from edges) are jointly satisfiable under the signed-graph parity
criterion (T39).

Four scenarios:
1. **holonic_flat** (2 nodes, compatible same cross-edge): baseline satisfiable case.
2. **holonic_compatible_different** (2 nodes, compatible different cross-edge): shows
   "different" cross-level constraints do not automatically obstruct.
3. **holonic_emergent** (3 nodes, transitive parity conflict): minimum holonic emergence case.
4. **holonic_micro_obstructed** (2 nodes, one micro obstructed): control — micro obstruction
   propagates, not an emergence case.

Two PO1 bridge cases:
- **holonic_po1_main**: source satisfiable, target obstructed, AC5 fires → admissible.
- **holonic_po1_no_forgotten_control**: source satisfiable, target obstructed, AC5 empty
  → not admissible.

## Success Criteria

1. Holonic emergence is detected in the emergent scenario (H_A refuted).
2. Holonic PO1 admissible case found with non-empty forgotten_dims.
3. Control case (empty forgotten_dims) is NOT admissible despite source satisfiable + target obstructed.
4. H_B best supported: holonic finality is genuinely independent of micro finality.

## Failure Criteria

- No holonic emergence case found (H_A supported — would mean holonic finality reduces to micro finality).
- Holonic PO1 found with empty forgotten_dims (H_C refuted — would mean AC5 is not necessary).
- Holonic emergence depends on micro obstruction rather than cross-level topology.

## Known Physics Constraints

- Binary {-1,1} domain with same/different constraints (same fragment as T39).
- Holonic nodes are D1RestrictionSystems; a full holarchy would use TypedTransportNetworks
  as nodes (second-level nesting not yet implemented).
- The holonic emergence case is structurally equivalent to the T26/T39 minimum transitive
  obstruction, shifted from the within-level to the cross-level layer.

## Contribution Needed

- Extend nodes from D1RestrictionSystems to TypedTransportNetworks for full second-level nesting.
- Run parameter sweep over cross-level edge topologies to map emergence vs. reduction conditions.
- Test whether holonic AC5 condition is a strict strengthening of T32's admissibility basis.
- Compare the holonic global section definition to sheaf-theoretic cohomology (T13).
