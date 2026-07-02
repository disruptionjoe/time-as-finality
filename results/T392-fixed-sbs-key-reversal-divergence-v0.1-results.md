# T392 Fixed-SBS-Key Reversal Divergence Witness — Results v0.1

- **Artifact:** `T392-fixed-sbs-key-reversal-divergence-v0.1`
- **Spec:** [tests/T392-fixed-sbs-key-reversal-divergence-witness.md](../tests/T392-fixed-sbs-key-reversal-divergence-witness.md)
- **Model:** [models/fixed_sbs_key_reversal_divergence.py](../models/fixed_sbs_key_reversal_divergence.py)
- **Test:** [tests/test_fixed_sbs_key_reversal_divergence.py](../tests/test_fixed_sbs_key_reversal_divergence.py)
- **Numbers:** [T392-fixed-sbs-key-reversal-divergence-v0.1.json](T392-fixed-sbs-key-reversal-divergence-v0.1.json)
- **Tags:** finite_witness, q1c_class1_existence_probe, sbs_key_fixed, reversal_divergence, no_claim_promotion, q1c_remains_dormant

## Verdict (house vocabulary)

**Witness holds in this finite family.** At a fixed full ordinary event-level
record and a fixed SBS closure key over the declared fragments `F1..F4`, the
reversal-cost axis splits the D1-relative-to-access verdict, and an auxiliary
channel on extra environment structure (`A0`) gives positive, non-screened-off
predeclared decision-risk lift across the tested finite loss family. On the
strength of this seven-qubit statevector model, **the T146 live class
`extra_environment_candidate` (T150: `typed_extra_environment_candidate`) is
non-empty as a finite existence result.**

This does **not** reinstate Q1C, does not name a platform, and does not clear
the T166 packet-intake gate or the T183 reinstatement stack. Q1C remains
**dormant**. The result is scoped to this finite family.

## Predeclarations (fixed before inspecting numbers)

- Weak-coupling angle `theta = pi/3` (fixed).
- Reversal-success visibility threshold `v* = 0.9`, predeclared. The natural
  preparation-A analytic visibility is `2 cos(theta/2)/(1 + cos(theta/2)^2) =
  0.98974...`, above `0.9`; the round `0.9` was kept unchanged.
- Verdict map `V = g(H)` fixed before the decision problem: finite `H` ->
  `recoverable-at-access-K`, infinite `H` -> `final-relative-to-K`.

## Exact computed values

### 1. Ordinary-record equality

Full ordinary event-level record `R` = joint `Z` distribution over `{S, M}`.
The stored outcome tuples are index-sorted, so the labels below read `(S, M)`
(`S` = qubit 0, `M` = qubit 1); e.g. the `0.375` row reads `P(S=1, M=0)`.

| `(S, M)` | P (prep A) | P (prep B) |
| --- | --- | --- |
| `(0, 0)` | 0.500000 | 0.500000 |
| `(1, 0)` | 0.375000 | 0.375000 |
| `(1, 1)` | 0.125000 | 0.125000 |

Max absolute difference A vs B: **0.0**. Records identical. `ordinary_records_equal = true`.

### 2. SBS closure-key equality (repo's T162 definition)

Key = `(pointer_observable, objectivity_status, pointer_value, partition_visible, R_delta)`,
using the imported `_class_count_for` and vocabulary from
`models/q1a_sbs_factorization_obstruction.py`.

- Key A = `('computational_z', 'sbs_objective', 'computational_z', True, 4)`
- Key B = `('computational_z', 'sbs_objective', 'computational_z', True, 4)`
- `sbs_keys_equal = true`.
- Both D1-finalized under `D1_INDEPENDENT_SUPPORT_THRESHOLD = 3`
  (`R_delta = 4 >= 3`): `d1_finalized_A = d1_finalized_B = true`.

The `A0` coupling in preparation B changes only *coherences* of the declared
subsystem (declared-register reduced-density-matrix max diff `0.433`), which are
invisible to both the `Z`-basis ordinary record and the pointer-record SBS key.

### 3. Reversal divergence

Undo `U_K` = inverse `S->Fi` couplings on `K = {F1..F4}`, conditioned on `M`.

- Best-branch X-visibility of `S` after undo, prep A: **0.989743**
- Best-branch X-visibility of `S` after undo, prep B: **0.000000**
- **Visibility gap (A - B): 0.989743**

Prep B does not recover because `A0` (inaccessible) still holds a `Z`-copy of
`F4`'s record.

### 4. Typed axis H and verdict

- `H(A) = 4` (all four accessible fragments must be undone; any 3-subset stays
  below `v*`).
- `H(B) = inf` (no accessible subset reaches `v*`).
- `verdict_A = recoverable-at-access-K`, `verdict_B = final-relative-to-K`.
- Both verdict classes populated (prior mass `0.5` each). T150 support met.

### 5. Screening-off failure certificate

Auxiliary channel `A0` measured in `Z`; prior `P(A) = P(B) = 0.5`. Bayes
decision risk predicting `V` from `R` alone vs `(R, A0)`:

| Loss function | risk(V \| R) | risk(V \| R, A0) | lift |
| --- | --- | --- | --- |
| symmetric 0-1 | 0.5000 | 0.2500 | **0.2500** |
| false-recover-costly (5:1) | 0.5000 | 0.2500 | **0.2500** |
| false-final-costly (4:1) | 0.5000 | 0.2500 | **0.2500** |

Positive lift on **all three** loss functions (T155 finite decision family).

- Conditional mutual information **`I(V ; A0 | R) = 0.5` bits > 0**.

### 6. Null controls

- **T137 downstream-transform null.** Auxiliary channel `M XOR S` (a
  deterministic function of `R`): lift = **0.0** on all three losses,
  `I(V ; (M XOR S) | R) = 0.0`. Confirms the null class shows no lift.
- **B' product-state null.** Preparation B' (`A0` copies nothing) is bitwise
  identical to A: `statevector_identical = true`, records equal, SBS keys
  equal, reversal equal, `H` equal. Zero divergence on every metric.

## Why the reversal cost is not a T118 relabeling of support

T118 collapsed reversal cost inside the fixed-*data* Q1A family because that
family had no undo dynamics and its only reversal proxy was a class count equal
to audited support. Here the reversal cost is a genuine coherence-recovery cost
computed from exact undo dynamics: `H(A) = 4` and `H(B) = inf` at the SAME
`R_delta = 4` support count and the SAME closure key. Reversal cost therefore
carries verdict content beyond the SBS support count in this family — occupying
the reopening door T162 explicitly named.

## Honest weaknesses (reviewer-facing)

- The extra environment `A0` is engineered, not shown to be physically forced.
  A real Q1C platform would have to exhibit such structure without inserting it
  by hand. This is why the result earns only a finite existence claim.
- The strongest attack — "`A0` is a downstream `Z`-copy of `S`, hence T137-null"
  — is answered by the exact separation `I(V ; A0 | R) = 0.5` vs `I = 0` for the
  true downstream channel, because `R` is prep-invariant and cannot resolve the
  reversibility verdict. The spec records this exchange in full.
- The verdict is stated on the dominant `M = 0` branch; the rare `M = 1` branch
  does not recover coherence even in prep A (the meter entanglement there is not
  undone). This is disclosed and does not affect the fixed-key/fixed-record
  equalities.

## pytest output

```
platform linux -- Python 3.10.12, pytest-9.1.1, pluggy-1.6.0
collected 18 items

tests/test_fixed_sbs_key_reversal_divergence.py::test_ordinary_event_level_record_identical PASSED
tests/test_fixed_sbs_key_reversal_divergence.py::test_ordinary_record_is_a_normalized_distribution PASSED
tests/test_fixed_sbs_key_reversal_divergence.py::test_sbs_closure_keys_identical PASSED
tests/test_fixed_sbs_key_reversal_divergence.py::test_sbs_key_is_finalized_and_uses_repo_threshold PASSED
tests/test_fixed_sbs_key_reversal_divergence.py::test_reversal_restores_visibility_for_A_not_for_B PASSED
tests/test_fixed_sbs_key_reversal_divergence.py::test_undo_needs_the_full_accessible_set_in_A PASSED
tests/test_fixed_sbs_key_reversal_divergence.py::test_reversal_gap_matches_analytic_value PASSED
tests/test_fixed_sbs_key_reversal_divergence.py::test_typed_axis_H_finite_for_A_infinite_for_B PASSED
tests/test_fixed_sbs_key_reversal_divergence.py::test_verdict_map_splits_the_two_preparations PASSED
tests/test_fixed_sbs_key_reversal_divergence.py::test_reversal_cost_infinite_when_no_accessible_subset_reaches_vstar PASSED
tests/test_fixed_sbs_key_reversal_divergence.py::test_phi_independence_lemma_grounds_infinite_cost_in_B PASSED
tests/test_fixed_sbs_key_reversal_divergence.py::test_both_verdict_classes_populated_no_gerrymander PASSED
tests/test_fixed_sbs_key_reversal_divergence.py::test_auxiliary_channel_gives_positive_lift_across_loss_family PASSED
tests/test_fixed_sbs_key_reversal_divergence.py::test_conditional_mutual_information_strictly_positive PASSED
tests/test_fixed_sbs_key_reversal_divergence.py::test_downstream_transform_auxiliary_channel_has_zero_lift PASSED
tests/test_fixed_sbs_key_reversal_divergence.py::test_bprime_shows_zero_divergence_from_A PASSED
tests/test_fixed_sbs_key_reversal_divergence.py::test_witness_holds_end_to_end PASSED
tests/test_fixed_sbs_key_reversal_divergence.py::test_witness_language_is_restrained_house_vocabulary PASSED

18 passed
```

## Recommended next (no promotion)

- Do not treat this as a Q1C reopening. If Joe wants to press it, the next step
  is a physical-forcing argument for `A0`-like structure and a robustness sweep
  over imperfect copies and `theta`, staged through the T166 packet intake.

## v0.1 -> v0.1.1 review patches

Hostile review ruling: **stands, patches required** (reviewer scratch at
`_local/t392_hostile_check.py`). Five patches applied; no computed number
changed.

1. **Mixture legitimacy** — spec section added answering "the lift is merely
   preparation identification": the T137/T150 gates structurally require an
   A/B family; the 50/50 mixture is physically equivalent to a single frozen
   8-qubit architecture with one unmonitored coin qubit controlling the
   `F4 -> A0` coupling; and the earned verdict non-factorization content is
   independent of the mixture reading.
2. **Record labeling** — the ordinary-record table mislabeled the stored
   tuples as `(M, S)`; they are index-sorted `(S, M)`, so the correct reading
   of the `0.375` row is `P(S=1, M=0)`, not `P(M=1, S=0)`. Labels fixed here
   and in the model docstring; the `.json` stores unlabeled bitstrings (in
   `(S, M)` order) and needed no change. Every computed number unchanged.
3. **Class naming** — headline "Q1C Class 1" replaced with the repo's named
   classes: T146 `extra_environment_candidate` / T150
   `typed_extra_environment_candidate` (informal "Class 1" collides with
   T146's own numbering, where class 1 is a null class).
4. **Phi-independence lemma** — spec section plus a new test earning it:
   `rho_{S,F1..F4|M=0}` is exactly phi-independent in prep B and genuinely
   phi-dependent in prep A, which is the protocol-independent ground for
   `H(B) = inf`; disclosed that raw visibility alone is gameable by
   manufactured coherence, so the inverse-coupling restriction is not what
   `H(B) = inf` rests on. Suite is now 18 tests; all pre-existing numbers
   bit-identical.
5. **Registration** — T392 entered in TESTS.md (with a note that T391 is
   unassigned), and the model summary / verdict phrasing updated per patch 3.
