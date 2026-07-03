# T432 - Classical Finite-Boundary Declarability Gate - v0.1 results

> Recorded-tier exploratory artifact. `TESTS.md`, `ROADMAP.md`, and `CLAIM-LEDGER.md` are UNTOUCHED. No claim promotion. This is a classical finite-state C-fragment certificate only; it does not touch the quantum E3 route.

- Spec (frozen first): `tests/T432-classical-finite-boundary-declarability-gate.md`
- Model: `models/classical_finite_boundary_declarability_gate.py`
- Tests: `tests/test_classical_finite_boundary_declarability_gate.py`
- Artifact JSON: `results/T432-classical-finite-boundary-declarability-gate-v0.1.json`
- Run: `python -m pytest tests/test_classical_finite_boundary_declarability_gate.py -q`

## Overall verdict: C_FRAGMENT_EXECUTABLE_E0_FOR_SINGLE_INSTANCE

In the tested classical finite product regime, every separator outside the A0 region algebra is recovered by A1 full-code lookup. Even a full-support parity separator with no proper coordinate support is declared relative to A1, not single-instance physical.

## Named Certificates

| certificate | region A0 | minimal coordinate supports | boundary pair? | verdict |
| --- | --- | --- | --- | --- |
| hidden_complement_bit | {x0} | {x1} | yes | E0_DECLARED_RELATIVE_TO_A1_FULL_CODE |
| region_visible_control | {x0,x1} | {x0} | no | NO_BOUNDARY_A0_REGION_DETERMINES_DATUM |
| full_support_parity_separator | {x0,x1} | {x0,x1,x2} | yes | E0_DECLARED_RELATIVE_TO_A1_FULL_CODE |
| region_plus_complement_relation | {x0} | {x0,x1} | yes | E0_DECLARED_RELATIVE_TO_A1_FULL_CODE |

## Exhaustive Small Boolean Sweep

| n bits | checks | boundary functions | A1-declared boundaries | physical candidates | no-proper-support boundaries |
| --- | --- | --- | --- | --- | --- |
| 1 | 4 | 2 | 2 | 0 | 2 |
| 2 | 48 | 38 | 38 | 0 | 30 |
| 3 | 1792 | 1730 | 1730 | 0 | 1526 |

## What this earns / does not earn

Earns: an executable finite-classical check for the taxonomy's C-fragment: single-instance separators outside A0 are still recovered by A1 full-code lookup. The `full_support_parity_separator` is the guard case: no proper coordinate subset determines it, but the finite closed full code still does.

Does not earn: a universal no-go theorem, a quantum theorem, a WAY/E3 result, a claim-ledger update, a public-posture update, or cross-repo support.

Honest ceiling: This supports only the classical finite-state C fragment as an executable certificate. It is not a universal no-go theorem, not a quantum statement, not an E3 result, not claim-ledger movement, and not cross-repo evidence.
