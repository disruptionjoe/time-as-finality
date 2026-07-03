# T433 - Classical Declarability Proof Certificate - v0.1 results

> Recorded-tier exploratory artifact. `TESTS.md`, `ROADMAP.md`, and `CLAIM-LEDGER.md` are UNTOUCHED. No claim promotion. This is a classical finite-product proof certificate only; it does not touch the quantum E3 route.

- Spec (frozen first): `tests/T433-classical-declarability-proof-certificate.md`
- Model: `models/classical_declarability_proof_certificate.py`
- Tests: `tests/test_classical_declarability_proof_certificate.py`
- Artifact JSON: `results/T433-classical-declarability-proof-certificate-v0.1.json`
- Run: `python -m pytest tests/test_classical_declarability_proof_certificate.py -q`

## Overall verdict: CLASSICAL_DECLARABILITY_PROOF_CERTIFIED

T433 discharges the classical single-instance proof obligation: once A1 contains the full co-present finite classical code, every total separator is recoverable by lookup. A0 insufficiency is a declared boundary relative to A1, not a physical one.

## Theorem Statement

For any finite classical product code Omega and any total datum d: Omega -> V, d is A1-measurable when A1 contains the full co-present code / identity readout. Therefore an A0 boundary created by d not factoring through the region projection is E0-declared relative to A1, not a single-instance physical boundary.

## Proof Certificate

| step | content | discharged by |
| --- | --- | --- |
| P1 | Classical instance is a finite product code Omega. | FiniteProductCode(domains) |
| P2 | A0 observables factor through the declared region projection pi_R. | is_constant_on_projection(code, table, region) |
| P3 | A1 includes the identity/full-code readout on Omega. | code.full_coords |
| P4 | Every total datum factors through identity by finite lookup. | is_constant_on_projection(code, table, code.full_coords) |
| P5 | A boundary is physical relative to A1 only if it has an A0 same-fiber split and fails A1 measurability. | has_boundary and not a1_measurable is always false for valid cases |

## Named Cases

| case | domain shape | region A0 | minimal supports | boundary pair? | verdict |
| --- | --- | --- | --- | --- | --- |
| region_visible_control | 2 x 2 x 2 | {x0,x1} | {x0} | no | NO_BOUNDARY_A0_REGION_DETERMINES_DATUM |
| hidden_complement_bit | 2 x 2 | {x0} | {x1} | yes | E0_DECLARED_RELATIVE_TO_A1_BY_CONSTRUCTIVE_LOOKUP |
| full_support_parity_guard | 2 x 2 x 2 | {x0,x1} | {x0,x1,x2} | yes | E0_DECLARED_RELATIVE_TO_A1_BY_CONSTRUCTIVE_LOOKUP |
| nonbinary_region_complement_relation | 3 x 2 | {x0} | {x0,x1} | yes | E0_DECLARED_RELATIVE_TO_A1_BY_CONSTRUCTIVE_LOOKUP |

## Mixed Finite Sweep

| domain shape | checks | boundary functions | A1-declared boundaries | physical candidates |
| --- | --- | --- | --- | --- |
| 2 | 4 | 2 | 2 | 0 |
| 2 x 2 | 48 | 38 | 38 | 0 |
| 2 x 3 | 192 | 178 | 178 | 0 |
| 3 x 2 | 192 | 178 | 178 | 0 |
| 2 x 2 x 2 | 1792 | 1730 | 1730 | 0 |

## What this earns / does not earn

Earns: a constructive classical proof certificate replacing the small-sweep reading with the general finite-product argument: every total datum factors through the A1 identity/full-code readout by lookup.

Does not earn: a universal no-go theorem, a quantum theorem, an E3/WAY statement, a claim-ledger update, a public-posture update, or cross-repo support.

Honest ceiling: Classical finite product codes only. This is not a quantum theorem, not an E3/WAY statement, not a universal no-go, not claim-ledger movement, and not cross-repo evidence.
