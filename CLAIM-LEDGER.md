# Claim Ledger

This ledger tracks the current status of the Time as Finality conjecture suite. Claim IDs are stable handles so the essay, issues, tests, and discussions can link to the same object.

| ID | Class | Status | Claim | Primary test / work item |
| --- | --- | --- | --- | --- |
| [C1](claims/C1-experienced-time-as-record-finality.md) | core_claim | weakened | Accessible stabilization frontiers can reconstruct an observer-relative temporal partial order; total and phenomenal readings are unsupported. | [T1](tests/T1-record-graph-temporal-reconstruction.md) |
| [C2](claims/C2-typed-compositional-finality.md) | core_claim | weakened | Evidence may compose by provenance-preserving join, while inherited expression, access, profiles, coarse-graining, and decisions need not preserve that algebra. | [T11](tests/T11-compositional-finality.md) |
| [C3](claims/C3-signed-readout-separation.md) | core_claim | supported | Phase-blind finality profiles do not determine signed or Born-style readout, even when evidence and finality grow monotonically. | [T13](tests/T13-signed-interfering-readout.md) |
| [D1](claims/D1-physical-finality-definition.md) | definition | weakened | Finality is an observer-indexed comparative schema; T13 shows its profile is not a complete phase-sensitive readout state. | [FORMALISM](FORMALISM.md), [T1](tests/T1-record-graph-temporal-reconstruction.md), [T5](tests/T5-thermodynamic-record-support.md), [T9](tests/T9-emergence-laboratory.md), [T10](tests/T10-proof-carrying-metastable-finality.md), [T11](tests/T11-compositional-finality.md), [T13](tests/T13-signed-interfering-readout.md) |
| [D2](claims/D2-observer-as-record-bearing-system.md) | definition | revised | T1 distinguishes capabilities; T12 makes coupling profile an explicit observer parameter; T13 separates access-dependent readout from finality. | [T1](tests/T1-record-graph-temporal-reconstruction.md), [T10](tests/T10-proof-carrying-metastable-finality.md), [T11](tests/T11-compositional-finality.md), [T12](tests/T12-coupling-profile-reconstruction.md), [T13](tests/T13-signed-interfering-readout.md), [N3](literature/N3-core-formalism-known-neighbors.md) |
| [A1](claims/A1-distributed-systems-finality-analogy.md) | analogy | revised | Snowball-style sampling models bounded convergence and safety-liveness tradeoffs, not truth creation or physical law. | [T1](tests/T1-record-graph-temporal-reconstruction.md), [T10](tests/T10-proof-carrying-metastable-finality.md) |
| [M1](claims/M1-coupling-profile-reconstruction.md) | conjecture | toy_supported | Coupling profile can change which temporal relation an observer reconstructs without introducing causal contradiction. | [T12](tests/T12-coupling-profile-reconstruction.md) |
| [Q1](claims/Q1-quantum-under-finalization.md) | conjecture | open | Quantum states may be real but not yet finalized as classical records in a given observer-environment context. | [T2](tests/T2-quantum-measurement-record-finality.md) |
| [R1](claims/R1-relativity-no-global-commit-order.md) | conjecture | open | Relativity is naturally compatible with no universal global finality order. | [T3](tests/T3-spacelike-events-no-global-commit-order.md) |
| [B1](claims/B1-black-holes-finality-boundaries.md) | potential_byproduct | open | Black holes are stress tests for finality-domain boundaries and causal record accessibility. | [T4](tests/T4-black-hole-causal-access-boundary.md) |
| [S1](claims/S1-spacetime-consensus-envelope.md) | speculative_extension | open | Spacetime may be a consensus envelope for causally bounded finality. | [Open problem](open-problems/rendered-interface-assumptions.md) |
| [N1](literature/N1-known-neighbors.md) | known_neighbor | active | The project is adjacent to decoherence, quantum Darwinism, relational time, causal structure, and thermodynamics. | Literature map |
| [N3](literature/N3-core-formalism-known-neighbors.md) | known_neighbor | active | Lamport, quantum Darwinism, IGUS, records-of-histories, and Landauer constrain the novelty and interpretation of v0.1. | Primary-source positioning |
| [N4](literature/N4-emergence-lab-known-neighbors.md) | known_neighbor | active | Reversible computation, cellular automata, Landauer cost, coarse-graining, and Boolean sensitivity constrain the Emergence Laboratory. | Primary-source positioning |
| [N5](literature/N5-proof-carrying-metastable-finality-known-neighbors.md) | known_neighbor | active | Snow consensus, zero knowledge, proof-carrying data, coarse-graining, and physical metastability constrain T10. | Primary-source positioning |
| [N6](literature/N6-compositional-finality-known-neighbors.md) | known_neighbor | active | CRDT joins, coarse-graining, sheaf gluing, and epigenetic inheritance constrain T11's composition claims. | Primary-source positioning |
| [N7](literature/N7-signed-readout-known-neighbors.md) | known_neighbor | active | Quantum measure theory, decoherent histories, quantum Darwinism, and Wigner negativity constrain T13's interpretation. | Primary-source positioning |
| [G1](guardrails/G1-human-belief-does-not-create-matter.md) | not_claimed | active | Human belief does not create matter. | Guardrail |
| [G2](guardrails/G2-not-a-replacement-theory.md) | not_claimed | active | This does not replace QM, GR, thermodynamics, or proper time. | Guardrail |

## Status Values

- `open` - claim is under active formalization or challenge.
- `active` - claim is currently used as a guardrail, analogy, or literature bridge.
- `revised` - claim has been changed substantially from an earlier version.
- `weakened` - claim remains useful but no longer supports its original ambition.
- `rejected` - claim failed a test or was superseded.

## Change Log

### 2026-06-11 - First executable formal result

- C1 changed from `open` to `weakened`: T1 supports partial-order
  reconstruction but the three-event counterexample rejects a general total
  order, and no phenomenal-experience bridge was demonstrated.
- D1 changed from `open` to `revised`: the prose dimensions became an
  observer-indexed componentwise preorder.
- D2 changed from `open` to `revised`: the broad observer definition became a
  capability taxonomy and was positioned against IGUS prior art.

### 2026-06-11 - Emergence Laboratory

- D1 changed from `revised` to `weakened`: its four dimensions do not emerge
  as one universal structure. Accessibility and branch structure survive,
  while support, raw redundancy, and terminal intervention cost collapse in
  the simplest binary trace model.
- The stronger claim that finality is one mechanism spanning causal,
  computational, and thermodynamic irreversibility is rejected. The surviving
  result is a comparative framework for observer-indexed records.

### 2026-06-11 - Proof-carrying metastable finality

- A1 changed from `active` to `revised`: Snowball-style confidence is useful
  for modeling bounded convergence and explicit safety-liveness tradeoffs, but
  it does not outperform direct Bayesian aggregation as a truth criterion.
- D1 remains `weakened`: T10 separates coarse reversal radius, proof validity,
  independent support, protocol confidence, and liveness. These dimensions are
  useful but largely arise from an engineered observer protocol.

### 2026-06-11 - Compositional finality

- C2 added as `weakened`: compatible evidence states form a
  provenance-preserving join-semilattice, but finality profiles do not
  universally inherit that join.
- D1 remains `weakened`: the profile is a stage-specific observer summary.
  Conflict, coarse-graining, and inherited expression can alter later stages.
- T11 operationalizes the epigenetic lens as inherited, context-dependent,
  locally reprogrammable expression over stable record identity. It does not
  assert biological mechanism, fractal scaling, or a fixed number of layers.

### 2026-06-16 - Coupling and signed readout

- M1 added as `toy_supported`: T12 shows coupling profiles can change the
  reconstructed temporal relation without producing causal inversions.
- C3 added as `supported`: T13 gives finite witnesses showing that D1
  finality profiles do not determine Born-style signed readout.
- D1 remains `weakened`: the finality profile is a stability summary, not a
  complete readout state.
