# T412: Separator Refactorization Gate

## Target Claims

- [Region-Indexed Capability Discriminator](../open-problems/region-indexed-capability-discriminator.md)
- [T411: Departed-Record Capability Discriminator](T411-departed-record-capability-discriminator.md)
- The R1 fallback named by
  [Physical-Boundary Discriminator - Hegelian Persona Pass](../explorations/physical-boundary-hegelian-persona-pass-2026-07-02.md)

## Setup

Use a three-qubit parity pair as the canonical finite shadow of T411's beta=0
global-correlation separator:

```text
rho_even = uniform mixture over even parity bitstrings
rho_odd  = uniform mixture over odd parity bitstrings
```

In the declared tensor product, every nonempty proper subset marginal is
identical. The full joint parity readout separates perfectly.

Then test two classes of relabeling:

1. Product-structure-preserving relabels: qubit permutations, local bit flips,
   and a product-basis spot check.
2. Arbitrary entangling refactorization: a reversible parity fan-in
   `y0 = x0 xor x1 xor x2`, `y1 = x1`, `y2 = x2`.

## Success Criteria

- All proper-subset trace distances are zero in the declared tensor product.
- The full trace distance is one and full parity separates perfectly.
- Product-structure-preserving relabels preserve the no-proper-subset
  separator property.
- The entangling refactorization localizes parity into one factor.
- The verdict records the admissibility boundary without claim promotion.

## Failure Criteria

The gate fails if:

- any proper subset separates in the declared tensor product;
- product-structure-preserving relabels localize the datum;
- the entangling refactorization does not localize the datum;
- the artifact treats the separator as factorization-free, physical-boundary
  evidence, or a claim-ledger upgrade.

## Known Physics Constraints

This is a finite linear-algebra guardrail. It does not model hardware,
thermodynamics, spacetime, recovery dynamics, or a physical boundary. It only
tests what kind of refactorization can be admitted before the global separator
collapses.

## Contribution Needed

Future separator work must declare an admissibility rule for factorization
changes: product/coupling-preserving relabels are safe in this gate, while
arbitrary entangling refactorizations are not. A later transport or scrambling
fixture should derive that operational factorization from dynamics rather than
declaring it after the fact.
