# Computational Status Ledger

## Status

Governance ledger for computational-status language. This file does not
promote any claim. It records what the current executable artifacts honestly
earn about scale, search, and hardness.

Use this ledger before saying that a branch is brute-force, polynomial,
theorem-backed, NP-hard, CSP-complete, or scalable.

## Status Labels

| Label | Meaning |
| --- | --- |
| `finite_witness` | Current support is a finite executable fixture or finite-family check. It may use efficient operations internally, but no general scalable theorem has been earned. |
| `poly_decider` | The implemented decision surface is a finite polynomial-style classifier over declared inputs, not a hidden search over completions. |
| `theorem_backed` | The main claim has an explicit scalable proof argument, with finite code used only for sanity checks or examples. |
| `open_hardness` | Hardness is only an open question. Do not use NP-hard or CSP-complete language. |

## Current Ledger

| Surface | Primary status | Input size / scope | Current decision method | Scale / hardness guardrail |
| --- | --- | --- | --- | --- |
| [T26 D1 Restriction System](tests/T26-d1-restriction-system.md) | `finite_witness` | Number of patch variables and finite constraints in a `D1RestrictionSystem`. | `global_section()` checks the current finite witnesses by assignment enumeration over patch variables. | Do not call this a scalable obstruction algorithm; use T39 for the signed-graph tractable fragment. |
| [T39 CSP / Satisfiability Reframing](tests/T39-csp-satisfiability-reframing.md) | `poly_decider` | Binary same/different constraints over `{-1, 1}`. | Signed-graph parity / 2-coloring classifies the tested obstruction fragment. | This earns tractability for the declared binary parity fragment, not NP-hardness or general CSP-completeness. |
| [T45 Measurement Asymmetry — obstructed-source lemma](results/measurement-po1-asymmetry-v0.1-results.md) | `theorem_backed` | Any morphism between `D1RestrictionSystem`s under the PO1 AC1–AC7 checklist. | AC7 argument: no PO1-admissible morphism can originate from an obstructed system; the admissible relation lies inside (unobstructed × obstructed). Finite run is a control. | GENERAL but elementary: an order-property of the *partially-supported* PO1 schema, inheriting its ceiling. ZERO temporal/empirical content — it does NOT show measurement is physically irreversible, nor that time is finality. |
| [T47 PO1-DAG Theorem](results/po1-dag-theorem-v0.1-results.md) | `theorem_backed` | Admissible morphisms in `D1Cat` over arbitrary finite `D1RestrictionSystem`s. | AC6 (target obstructed) and AC7 (source unobstructed) are necessary and complementary, so the admissible relation ⊆ (unobstructed × obstructed) is trivially acyclic, bipartite, depth ≤ 1. The K_{2,3} run is a control. | Same guardrail as T45: a GENERAL but elementary structural lemma about the PO1 schema; inherits PO1's `partially_supported` ceiling; ZERO temporal/empirical content. |
| [T54 Finite Finality Descent Theorem](tests/T54-finite-finality-descent-theorem.md) | `poly_decider` | Finite observer-local events, identity maps, records, axis profiles, and overlap witnesses. | Quotient-union construction plus finite record/order/Axis-Monotonicity checks classify canonical, underdetermined, conflicting, nondefinable, and AM-invalid cases. | Keep the theorem finite. It does not prove infinite descent or sheaf/categorical descent machinery. |
| [T73 LossKernel Composition](tests/T73-losskernel-composition.md) | `finite_witness` | Declared T34/T37 finite morphism paths and their `forgotten_structure` annotations. | Set union computes the current LossKernel annotation and finite tests compare it to path-dependent PO1 admissibility. | State this as a powerset-union monoid-valued annotation law, not as a lax functor or new categorical object. Quotient/prior-art gates remain open. |
| [T110 Finite-Permutation Monotone Obstruction](tests/T110-finite-permutation-monotone-obstruction.md) | `theorem_backed` | Finite closed reversible dynamics, modeled as permutation orbits. | Orbit argument: edgewise nondecrease on a finite cycle forces constancy. Exhaustive finite cycle checks are controls. | This blocks strict scalar finality monotones in finite closed reversible systems only. Open-system, coarse-grained, resource, and constructor variants require their own assumptions. |
| [T132 Weak-Measurement Non-Null Criterion](tests/T132-weak-measurement-nonnull-criterion.md) | `poly_decider` | Declared protocol features for a weak-measurement candidate. | Fixed finite rule audit classifies same-record, post hoc, constant-branch, monotone-proxy, and independent-axis cases. | This is a gate, not a prediction. It does not make Q1C empirical or near-ready. |
| [T138 Detector Manifest Workflow Fit](tests/T138-detector-manifest-workflow-fit.md) | `poly_decider` | Declared T136 manifest fields and authority-domain workflow structure. | Finite field, authority, pre-data-boundary, and outcome-smuggling checks via the T136 validator. | Passing a scaffold is not detector evidence. Q1B remains externally blocked until real pre-event manifest and event-level packet exist. |

## Global Guardrail

No surveyed core branch currently earns:

```text
NP-hard / CSP-complete core result
```

Hardness language is blocked until a branch proves a reduction or supplies an
accepted complexity-class placement under declared input encoding and
admissible transformations.

The honest current summary is:

```text
mixed computational status: finite witnesses, several polynomial finite
classifiers, and three theorem-backed results — the T110 finite-permutation
obstruction (a NEGATIVE result, under the weakened H7) plus the T45/T47 elementary
order-properties of the partially-supported PO1 schema (no temporal or empirical
content). No top-line claim is a proven general theorem; no earned general
hardness rhetoric.
```
