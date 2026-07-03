# T431 - M2 Independent-Channel Admission Gate - v0.1 results

> Recorded-tier exploratory admission artifact. `TESTS.md`, `ROADMAP.md`, and `CLAIM-LEDGER.md` are UNTOUCHED; the T-number lives only in this header / the spec header. NO claim promotion; ledger actions pause for Joe. Cross-domain social-choice / index language is the OBJECT OF STUDY, never evidence for physics or a sibling repo.

- Spec (frozen first): `tests/T431-m2-independent-channel-admission-gate.md`
- Model: `models/m2_independent_channel_admission_gate.py`
- Tests: `tests/test_m2_independent_channel_admission_gate.py`
- Artifact JSON: `results/T431-m2-independent-channel-admission-gate-v0.1.json`
- Run: `python -m pytest tests/test_m2_independent_channel_admission_gate.py -q`

## Overall verdict: REDESIGN_M2_NO_CURRENT_INDEPENDENT_CHANNEL

The current T424 Route-A channel candidates do not clear T430's independent-channel admission bar. I_chi and I_fr are independent of the old v_gap primitive but are recoverable from full support counts; I_sf is null at this witness size. A future M2 swing needs a newly predeclared domain channel that survives these no-completion controls.

## Admission Table

| channel | class | vgap independent? | completion leaks | status |
| --- | --- | --- | --- | --- |
| finality_separator | current_target | no | support_counts, quota_step, selector_tie_completion, deletion_critical_wording | rejected_completion_recoverable |
| I_chi | t424_candidate_index | yes | support_counts, quota_step | rejected_completion_recoverable |
| I_fr | t424_candidate_index | yes | support_counts, quota_step | rejected_completion_recoverable |
| I_sf | t424_candidate_index | no | support_counts, ambient_size, quota_step, selector_tie_completion, deletion_critical_wording | rejected_null_channel |
| support_count_11 | leaky_negative_control | yes | support_counts, quota_step | rejected_completion_recoverable |
| quota_margin_signature | leaky_negative_control | yes | support_counts, quota_step | rejected_completion_recoverable |
| profile_serial_guard | positive_control_not_domain_channel | yes | none | admitted_guard_only |

## Source Artifacts

- T424: `results/T424-m2-route-a-index-probe-v0.1-results.md`
- T430: `results/T430-m2-support-completion-closure-gate-v0.1-results.md`

## What this says about M2

T424's `I_chi` and `I_fr` were real improvements over Route B because they are not functions of the old `v_gap` primitive. T431 shows why that is still not enough after T430: both channels are fully recovered by support-count completion over the four judgment states. The spectral flow channel remains null at this finite witness size.

Do not reopen support, quota, selector, tie-completion, ambient-size, or deletion-critical variants until a candidate channel passes these no-completion controls as a domain channel rather than a guard label.

## What this earns / does not earn

Earns: an executable admission gate for future M2 independent-channel attempts, plus a bounded negative result for the current T424 channel candidates.

Does not earn: a universal no-go theorem, a closed M2 program, a stable M2 rescue, a canonical separator object, any claim-ledger movement, any physics-facing claim, or any cross-repo evidential use.

Honest ceiling: This is not a universal no-go theorem, not a claim-ledger movement, and not evidence for physics or a sibling repo. It is an executable admission/control gate for future M2 attempts in the current finite AND-doctrine universe.
