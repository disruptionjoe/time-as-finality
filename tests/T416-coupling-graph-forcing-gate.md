# T416 - Coupling-Graph Forcing Gate

## Target Claims

- Region-indexed capability discriminator.
- T412 separator refactorization gate.
- T414 certificate-identity bridge.
- T415 admissibility-derivation probe.

## Status

Executable Progress artifact. No claim promotion. No `CLAIM-LEDGER.md` entry.
Cross-domain governance/game material is cited only as object of study.

## Setup

T412 showed that a three-qubit parity separator has identical proper-subset
marginals and full-joint separation, but arbitrary entangling refactorization
can localize the datum into one factor.

T415 distinguished two ports of the game-side symmetry axiom:

- equality preservation, which is circular and admits 18 entangling
  equality-preservers;
- operational automorphism, which is the right structural port but bottoms out
  at R2: whether the factorization or coupling graph is physically forced.

T416 tests what kind of evidence can force the admissible automorphism group.
It uses the same `GL(3,2)` reversible linear refactorization universe as T415.

Three evidence packets are compared:

1. Separator-only evidence.
2. Independent singleton-operation support evidence.
3. Singleton-operation support plus a path coupling graph `0-1-2`.

Local bit flips are not enumerated in the linear group, but they preserve support
and graph structure; the model reports the affine count multiplier separately.

## Success Criteria

- The `GL(3,2)` count is 168.
- Separator-only evidence admits 24 equality-preserving maps, including 18
  entangling equality-preservers.
- Singleton-operation support evidence restricts admissibility to 6 product
  atom permutations, or 48 if local bit flips are added affinely.
- Path coupling evidence further restricts the class to the 2 automorphisms of
  the path graph, or 16 with local bit flips.
- The named entangling equality-preserver from T415 is excluded by singleton
  operation evidence.

## Failure Criteria

- If separator-only evidence already forces the product automorphism group, then
  T415's R2 burden is weaker than reported.
- If entangling equality-preservers also preserve singleton operation support,
  the proposed operation-support gate fails.
- If path coupling evidence does not restrict below the product atom
  permutations, then graph evidence adds no force in this fixture.

## Demotion Criteria

If the only evidence for the factorization is that it makes the separator
global, then R2 is unpaid and the separator remains factorization-relative.

If independent operation or coupling evidence is supplied, the gate may force a
local admissible automorphism group, but that is extra operational structure,
not a consequence of the separator.

## Known Constraints

- This is a finite linear refactorization gate, not a physics result.
- It does not prove a physical coupling graph.
- It does not upgrade T414/T415 into a claim.
- It registers a narrower operational burden for future R2 work: supply
  independent operation/coupling evidence, not separator-preserving relabels.
