# Claim Ledger

This ledger tracks the current status of the Time as Finality conjecture suite. Claim IDs are stable handles so the essay, issues, tests, and discussions can link to the same object.

| ID | Class | Status | Claim | Primary test / work item |
| --- | --- | --- | --- | --- |
| [C1](claims/C1-experienced-time-as-record-finality.md) | core_claim | weakened | Accessible stabilization frontiers can reconstruct an observer-relative temporal partial order; total and phenomenal readings are unsupported. | [T1](tests/T1-record-graph-temporal-reconstruction.md) |
| [D1](claims/D1-physical-finality-definition.md) | definition | weakened | Finality is an observer-indexed comparative schema; its dimensions must be justified per substrate and do not automatically emerge independently. | [FORMALISM](FORMALISM.md), [T1](tests/T1-record-graph-temporal-reconstruction.md), [T5](tests/T5-thermodynamic-record-support.md), [T9](tests/T9-emergence-laboratory.md) |
| [D2](claims/D2-observer-as-record-bearing-system.md) | definition | revised | T1 distinguishes trace-bearer, recorder, reconciler, and conscious-observer capability levels. | [T1](tests/T1-record-graph-temporal-reconstruction.md), [N3](literature/N3-core-formalism-known-neighbors.md) |
| [A1](claims/A1-distributed-systems-finality-analogy.md) | analogy | active | Distributed-systems finality provides bridge language for candidate states becoming committed states. | [T1](tests/T1-record-graph-temporal-reconstruction.md), [T6](tests/T6-snowball-record-finality.md) |
| [Q1](claims/Q1-quantum-under-finalization.md) | conjecture | open | Quantum states may be real but not yet finalized as classical records in a given observer-environment context. | [T2](tests/T2-quantum-measurement-record-finality.md), [T6](tests/T6-snowball-record-finality.md) |
| [R1](claims/R1-relativity-no-global-commit-order.md) | conjecture | open | Relativity is naturally compatible with no universal global finality order. | [T3](tests/T3-spacelike-events-no-global-commit-order.md), [T7](tests/T7-overlapping-causal-domains.md) |
| [B1](claims/B1-black-holes-finality-boundaries.md) | potential_byproduct | open | Black holes are stress tests for finality-domain boundaries and causal record accessibility. | [T4](tests/T4-black-hole-causal-access-boundary.md), [T7](tests/T7-overlapping-causal-domains.md) |
| [S1](claims/S1-spacetime-consensus-envelope.md) | speculative_extension | open_formal_target | Spacetime may be the compatibility structure produced by aggregating observer-local finality domains; not yet derived. | [Rendered interface](open-problems/rendered-interface-assumptions.md), [Spacetime colimit](open-problems/spacetime-as-finality-colimit.md), [T7](tests/T7-overlapping-causal-domains.md) |
| [H-Domain](explorations/heliosphere-as-finality-domain.md) | conjecture | open | The heliosphere is a D1 finality domain: the heliopause is a substrate-exchange boundary where record-formation physics changes across D1's four dimensions in ways not reducible to particle density. | [T7](tests/T7-overlapping-causal-domains.md), exploration |
| [H-Soft-Boundary](explorations/heliosphere-as-finality-domain.md) | potential_byproduct | open | Finality-domain boundaries fall on a continuous permeability spectrum: the heliopause (bidirectional, character-changing) and the event horizon (one-way, capped) are two points on it. Extends B1 with a boundary-permeability parameter. | [T4](tests/T4-black-hole-causal-access-boundary.md), [T7](tests/T7-overlapping-causal-domains.md) |
| [N1](literature/N1-known-neighbors.md) | known_neighbor | active | The project is adjacent to decoherence, quantum Darwinism, relational time, causal structure, and thermodynamics. | Literature map |
| [N3](literature/N3-core-formalism-known-neighbors.md) | known_neighbor | active | Lamport, quantum Darwinism, IGUS, records-of-histories, and Landauer constrain the novelty and interpretation of v0.1. | Primary-source positioning |
| [N4](literature/N4-emergence-lab-known-neighbors.md) | known_neighbor | active | Reversible computation, cellular automata, Landauer cost, coarse-graining, and Boolean sensitivity constrain the Emergence Laboratory. | Primary-source positioning |
| [G1](guardrails/G1-human-belief-does-not-create-matter.md) | not_claimed | active | Human belief does not create matter. | Guardrail |
| [G2](guardrails/G2-not-a-replacement-theory.md) | not_claimed | active | This does not replace QM, GR, thermodynamics, or proper time. | Guardrail |
| [G3](guardrails/G3-observer-rendering-not-mind-created-matter.md) | not_claimed | active | Observer rendering does not mean consciousness creates matter, spacetime, physical law, or other people. | Guardrail |

## Status Values

- `open` - claim is under active formalization or challenge.
- `open_formal_target` - ambitious claim is allowed as a research target only
  with explicit definitions, tests, and failure conditions.
- `active` - claim is currently used as a guardrail, analogy, or literature bridge.
- `revised` - claim has been changed substantially from an earlier version.
- `weakened` - claim remains useful but no longer supports its original ambition.
- `rejected` - claim failed a test or was superseded.

## Change Log

### 2026-06-11 - First executable formal result

- C1 changed from `open` to `weakened`: T1 supports partial-order
  reconstruction but the three-event counterexample rejects a general total
  order. A phenomenal-experience bridge was not demonstrated; it is now
  tracked as an open formal target rather than treated as settled.
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
