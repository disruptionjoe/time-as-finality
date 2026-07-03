# T429 - M2 Separator-Object Support Gate - v0.1 results

> Recorded-tier exploratory guardrail. `TESTS.md` and `CLAIM-LEDGER.md` are UNTOUCHED; the T-number lives only in this header / the spec header. NO claim promotion; ledger actions pause for Joe. Cross-domain social-choice / index language is the OBJECT OF STUDY, never evidence for physics or a sibling repo.

- Spec (frozen first): `tests/T429-m2-separator-object-support-gate.md`
- Model: `models/m2_separator_object_support_gate.py`
- Tests: `tests/test_m2_separator_object_support_gate.py` (6 passed)
- Artifact JSON: `results/T429-m2-separator-object-support-gate-v0.1.json`
- Run: `python -m pytest tests/test_m2_separator_object_support_gate.py -q`

## Overall verdict: REDESIGN_SEPARATOR_SUPPORT_COMPLETION

The only tested separator object with positives at both n=4 and n=5 is an ambient-size support-shape predicate. All tested separator positives are constant on full-support fibers, so the branch produces support/ambient-size completion artifacts rather than an independent M2 canonicity channel.

## Separator-object map

| object | class | ambient size? | n=4 SURVIVES-R1 | n=4 absorbed | n=5 SURVIVES-R1 | n=5 absorbed |
| --- | --- | --- | ---: | ---: | ---: | ---: |
| full_support_seen | support_predicate | no | 24 | 0 | 0 | 240 |
| both_cross_diagonals_seen | support_predicate | no | 24 | 0 | 0 | 240 |
| compatibility_cycle_positive | compatibility_graph_predicate | no | 24 | 220 | 0 | 1024 |
| signed_frustration_positive | signed_graph_predicate | no | 0 | 168 | 0 | 840 |
| crossing_count_exactly_one | crossing_graph_predicate | no | 0 | 48 | 0 | 80 |
| support_two_two | exact_support_predicate | no | 36 | 0 | 0 | 0 |
| support_2111 | exact_support_predicate | no | 0 | 0 | 240 | 0 |
| ambient_even_support_shape | ambient_size_support_predicate | yes | 24 | 0 | 240 | 0 |

## Stable larger-size cells

- `ambient_even_support_shape`: n=4 24 positives; n=5 240 positives; ambient-size leak = True

The stable larger-size row is not clean M2 canonicity progress: it reads the ambient support shape directly. In every tested object family, separator status is constant on full support-count fibers, so support completion recovers the signal.

## What this says about M2

The bounded separator-object branch does not repair the M2 canonicity problem. Non-ambient objects either appear only at one finite size or are absorbed by proper subsets at the next size. The only cross-size object is an explicit ambient-size support predicate, which is exactly the kind of completion leak the gate was built to reject.

Future M2 work should move off this family, or predeclare a separator whose value is not recoverable from support counts, ambient size, deletion-critical wording, or the same graph diagnostics already tested.

## What this earns / does not earn

Earns: a finite guardrail for the remaining simple separator-object escape hatch after T428.

Does not earn: a universal no-go theorem, a stable M2 rescue, a canonical separator object, any claim-ledger movement, any physics-facing claim, or any cross-repo evidential use.
