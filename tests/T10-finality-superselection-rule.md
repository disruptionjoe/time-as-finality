# T10: Finality Superselection Rule

## Target Claims

- [Q1: Quantum Under-Finalization](../claims/Q1-quantum-under-finalization.md)
- [D1: Physical Finality Definition](../claims/D1-physical-finality-definition.md)
- [D2: Observer as Record-Bearing System](../claims/D2-observer-as-record-bearing-system.md)

## Origin

Quantum Measurement Theorist and Operator Algebra/NCG lenses, idea sprint 2026-06-16.

## Hypothesis

Observer-indexed finality imposes a superselection structure on the Hilbert space of system-plus-environment: superpositions between finalized and under-finalized subspaces are operationally forbidden, not merely suppressed. This would reframe the preferred-basis problem as a certification problem — pointer states are the eigenspaces of a finality operator, not just the states selected by environmental Hamiltonian coupling.

## Setup

1. Take a standard system-environment model (e.g., qubit coupled to a bosonic bath).
2. Define finality on joint system-environment states using D1's componentwise preorder: a state is finalized when it satisfies accessible-records, distinct-holder redundancy, causal-branch-support, and graph-reversal-count thresholds simultaneously.
3. Ask: do the finalized states form a superselection sector? Specifically, does the finality preorder induce a decomposition of the Hilbert space into sectors such that no observable connecting distinct sectors is operationally accessible to any observer satisfying D1's access constraints?
4. Compare the resulting sector decomposition against known pointer-state bases from decoherence theory.

## Success Criteria

- The finality preorder induces a sector decomposition that is (a) non-trivial and (b) coarser than, finer than, or transverse to the standard decoherence pointer basis — any structural difference is informative.
- The induced superselection structure is derivable from D1 without importing the pointer-state definition by hand.
- At least one operational distinction from standard decoherence is identified.

## Failure Criteria

- The finality sectors are identical to decoherence pointer states under all accessible observables — the test is empirically equivalent and adds no structure.
- The finality-induced decomposition is inconsistent with unitary quantum mechanics (e.g., requires explicit collapse).
- The finality operator does not have a well-defined spectral decomposition on the relevant Hilbert space.

## Contribution Needed

Define the finality operator explicitly for a tractable model Hamiltonian. Check whether its eigenspaces agree with, extend, or contradict the Zurek pointer-state criterion. Determine whether finality superselection is a new constraint or a restatement of existing decoherence results.
