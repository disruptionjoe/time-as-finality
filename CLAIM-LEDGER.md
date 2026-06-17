# Claim Ledger

This ledger tracks the current status of the Time as Finality conjecture suite. Claim IDs are stable handles so the essay, issues, tests, and discussions can link to the same object.

| ID | Class | Status | Claim | Primary test / work item |
| --- | --- | --- | --- | --- |
| [C1](claims/C1-experienced-time-as-record-finality.md) | core_claim | weakened | Accessible stabilization frontiers can reconstruct an observer-relative temporal partial order; total and phenomenal readings are unsupported. | [T1](tests/T1-record-graph-temporal-reconstruction.md) |
| [D1](claims/D1-physical-finality-definition.md) | definition | weakened | Finality is an observer-indexed comparative schema; its dimensions must be justified per substrate and do not automatically emerge independently. T17 adds a bounded theorem check; T20 gives holder redundancy a theorem-transfer role; T21 shows local finality need not imply global assignment. | [FORMALISM](FORMALISM.md), [T1](tests/T1-record-graph-temporal-reconstruction.md), [T5](tests/T5-thermodynamic-record-support.md), [T9](tests/T9-emergence-laboratory.md), [T17](tests/T17-consensus-finality-crosswalk.md), [T20](tests/T20-consensus-record-theorem-transfer.md), [T21](tests/T21-bell-contextuality-finality.md) |
| [D2](claims/D2-observer-as-record-bearing-system.md) | definition | revised | T1 distinguishes trace-bearer, recorder, reconciler, and conscious-observer capability levels. | [T1](tests/T1-record-graph-temporal-reconstruction.md), [N3](literature/N3-core-formalism-known-neighbors.md) |
| [A1](claims/A1-distributed-systems-finality-analogy.md) | analogy | active | Distributed-systems finality provides bridge language for candidate states becoming committed states; T17 gives collapse maps and T20 verifies one proof-preserving theorem transfer with boundaries. | [T1](tests/T1-record-graph-temporal-reconstruction.md), [T6](tests/T6-snowball-record-finality.md), [T17](tests/T17-consensus-finality-crosswalk.md), [T20](tests/T20-consensus-record-theorem-transfer.md) |
| [Q1](claims/Q1-quantum-under-finalization.md) | conjecture | partially_supported | Quantum states may be real but not yet finalized as global classical records in a given observer-environment context; T21 gives a finite contextuality model. | [T2](tests/T2-quantum-measurement-record-finality.md), [T6](tests/T6-snowball-record-finality.md), [T21](tests/T21-bell-contextuality-finality.md) |
| [R1](claims/R1-relativity-no-global-commit-order.md) | conjecture | open | Relativity is naturally compatible with no universal global finality order. | [T3](tests/T3-spacelike-events-no-global-commit-order.md), [T7](tests/T7-overlapping-causal-domains.md) |
| [B1](claims/B1-black-holes-finality-boundaries.md) | potential_byproduct | open | Black holes are stress tests for finality-domain boundaries and causal record accessibility. | [T4](tests/T4-black-hole-causal-access-boundary.md), [T7](tests/T7-overlapping-causal-domains.md) |
| [S1](claims/S1-spacetime-consensus-envelope.md) | speculative_extension | open_formal_target | Spacetime may be the compatibility structure produced by aggregating observer-local finality domains; T16 gives a finite gluing target but not a spacetime derivation. | [Rendered interface](open-problems/rendered-interface-assumptions.md), [Spacetime colimit](open-problems/spacetime-as-finality-colimit.md), [T7](tests/T7-overlapping-causal-domains.md), [T16](tests/T16-spacetime-aggregation.md) |
| [H7](claims/H7-finality-induced-direction.md) | conjecture | partially_supported | Finality structure can induce an observer-relative temporal direction when admissible transformations are monotone in D1 finality. | [T18](tests/T18-finality-direction-theorem.md), [Arrow theorem](open-problems/arrow-of-time-as-constructor-theorem.md) |
| [H-Domain](explorations/heliosphere-as-finality-domain.md) | conjecture | open | The heliosphere is a D1 finality domain: the heliopause is a substrate-exchange boundary where record-formation physics changes across D1's four dimensions in ways not reducible to particle density. | [T7](tests/T7-overlapping-causal-domains.md), exploration |
| [H-Soft-Boundary](explorations/heliosphere-as-finality-domain.md) | potential_byproduct | open | Finality-domain boundaries fall on a continuous permeability spectrum: the heliopause (bidirectional, character-changing) and the event horizon (one-way, capped) are two points on it. Extends B1 with a boundary-permeability parameter. | [T4](tests/T4-black-hole-causal-access-boundary.md), [T7](tests/T7-overlapping-causal-domains.md) |
| [N1](literature/N1-known-neighbors.md) | known_neighbor | active | The project is adjacent to decoherence, quantum Darwinism, relational time, causal structure, and thermodynamics. | Literature map |
| [N3](literature/N3-core-formalism-known-neighbors.md) | known_neighbor | active | Lamport, quantum Darwinism, IGUS, records-of-histories, and Landauer constrain the novelty and interpretation of v0.1. | Primary-source positioning |
| [N4](literature/N4-emergence-lab-known-neighbors.md) | known_neighbor | active | Reversible computation, cellular automata, Landauer cost, coarse-graining, and Boolean sensitivity constrain the Emergence Laboratory. | Primary-source positioning |
| H1-Sheaf | partially_supported | open | A Cech H¹ obstruction class for incompatible finality sections exists and is computable on finite domain covers; nontrivial H¹ means no global finality section exists even when pairwise restrictions agree. T21 gives the obstruction a finite CHSH-style contextuality referent. | [T13](tests/T13-finality-sheaf-cohomology.md), [T21](tests/T21-bell-contextuality-finality.md) |
| [G1](guardrails/G1-human-belief-does-not-create-matter.md) | not_claimed | active | Human belief does not create matter. | Guardrail |
| [G2](guardrails/G2-not-a-replacement-theory.md) | not_claimed | active | This does not replace QM, GR, thermodynamics, or proper time. | Guardrail |
| [G3](guardrails/G3-observer-rendering-not-mind-created-matter.md) | not_claimed | active | Observer rendering does not mean consciousness creates matter, spacetime, physical law, or other people. | Guardrail |

## Status Values

- `open` - claim is under active formalization or challenge.
- `open_formal_target` - ambitious claim is allowed as a research target only
  with explicit definitions, tests, and failure conditions.
- `active` - claim is currently used as a guardrail, analogy, or literature bridge.
- `partially_supported` - finite tests support a narrowed form, while major
  physical or generalization conditions remain open.
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

### 2026-06-16 - Sheaf Cohomology Implementation (T13/T16)

- H1-Sheaf added as `potential_byproduct`, status `open`: Cech H¹ obstruction detection is now executable on the finite domain cover model. FinalitySection and RestrictionMap are the formal objects. The canonical h1_obstruction_scenario demonstrates nontrivial H¹ on a 3-domain cover.

### 2026-06-16 - Consensus Finality Theorem Check

- A1 remains `active`: T17 now has explicit collapse maps, divergence
  witnesses, and an executable bounded theorem check over a stated finite
  asynchronous model.
- D1 remains `weakened`: the theorem check supports keeping D1 dimensions
  separate, but only within the stated finite model and not as a universal
  physics claim.

### 2026-06-16 - Finality Direction Theorem Check

- H7 added as `partially_supported`: T18 proves that D1-monotone admissibility
  induces an acyclic finality direction in a finite constructor model.
- The guardrail remains active: this is not a derivation of the thermodynamic
  arrow, proper time, or a physical law without further substrate grounding.

### 2026-06-17 - v2 Idea Sprint — Seven Convergence Clusters

- H1-Sheaf upgraded from `potential_byproduct` to `partially_supported`: seven
  independent groups across four disciplinary traditions identified the H¹
  obstruction as a genuine substrate-independent invariant that is underexploited.
  Immediate next steps: Bell-test mapping, measurement-problem no-go statement.
- T19 assigned to phenomenal bridge complexity separation (see tests/T19-phenomenal-bridge-complexity-separation.md).
- See explorations/all-persona-idea-sprint-2026-06-16-v2.md for full sprint results.

### 2026-06-17 - Consensus-Record Theorem Transfer

- A1 remains `active`: T20 verifies that quorum-intersection safety transfers
  into physical-record finality as redundant-holder overlap with the same
  proof structure.
- D1 remains `weakened`: T20 strengthens holder redundancy's role but also
  shows that quorum safety does not prove T13-style global-section existence.

### 2026-06-17 - Bell Contextuality Finality

- Q1 changed from `open` to `partially_supported`: T21 gives a finite
  CHSH-style contextuality model where local finality sections exist but no
  global assignment exists.
- H1-Sheaf remains `partially_supported`: T21 supplies the requested
  Bell/contextuality referent, while probability-bearing Bell simulation
  remains open.
