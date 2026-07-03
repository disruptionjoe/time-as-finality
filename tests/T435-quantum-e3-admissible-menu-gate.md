# T435: Quantum E3 Admissible-Menu Gate

## Target Claims

Capability-boundary mode taxonomy, quantum E3 hinge, finite-closed
capability-boundary scope theorem.

## Setup

Use a finite two-sector quantum toy with a predeclared parity/superselection
generator:

```text
P = diag(1, -1)
```

The A1 admissible class contains only symmetry-respecting operations and
observables that commute with `P`, with no reference/asymmetry resource. The A2
class admits a reference/asymmetry resource that licenses relative-phase
observables such as `X`.

The main pair is:

```text
rho_plus  = |+><+|
rho_minus = |-><-|
```

They have the same A1 diagonal/statistical shadow but are separated by the
relative-phase observable `X`, which does not commute with `P`.

## Success Criteria

- The model records the main pair as A1-equivalent under the symmetry-respecting
  shadow.
- The model shows the separator is noncommuting and therefore not A1-admissible.
- Relative to A1 without a reference resource, the main pair receives an E3-style
  structural-symmetry verdict.
- The same pair becomes E0-declared once A2 admits a reference/asymmetry resource.
- Visible A1 controls, classical controls, post-hoc symmetry selectors, and hidden
  label oracles do not pass as E3 positives.

## Failure Criteria

- The artifact treats this as a proof of WAY, quantum mechanics, or physics.
- The artifact revives the T421 GU-adjacent adapter or uses sibling-repo content as
  support.
- The artifact moves `CLAIM-LEDGER.md`, `TESTS.md`, `ROADMAP.md`, North Star,
  canon, public posture, or cross-repo truth.
- The E3 verdict does not name the admissible class `A`.
- A hidden label, post-hoc symmetry, or non-native oracle can pass the gate.

## Known Physics Constraints

This is a finite symmetry/admissible-menu gate only. It illustrates the taxonomy's
A1/A2 dependence with a standard superselection/resource-asymmetry shape. It is
not a Wigner-Araki-Yanase theorem, not a quantum physics claim, not a GU adapter,
and not evidence for a promoted E3 claim.

## Contribution Needed

Use this as an internal control on the taxonomy: future quantum E3 work must name
the symmetry, admissible class `A`, reference-resource policy, and forbidden
operation before claiming a structural-symmetry boundary.
