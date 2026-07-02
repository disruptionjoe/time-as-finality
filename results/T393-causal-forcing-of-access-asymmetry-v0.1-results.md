# T393 Causal Forcing of the Access Asymmetry — Results v0.1

- **Artifact:** `T393-causal-forcing-of-access-asymmetry-v0.1`
- **Spec:** [tests/T393-causal-forcing-of-access-asymmetry.md](../tests/T393-causal-forcing-of-access-asymmetry.md)
- **Model:** [models/causal_forcing_access_asymmetry.py](../models/causal_forcing_access_asymmetry.py)
- **Test:** [tests/test_causal_forcing_access_asymmetry.py](../tests/test_causal_forcing_access_asymmetry.py)
- **Numbers:** [T393-causal-forcing-of-access-asymmetry-v0.1.json](T393-causal-forcing-of-access-asymmetry-v0.1.json)
- **Tags:** causal_forcing, tier1_conditional_on_emission, t392_upgrade,
  exact_certificate, no_claim_promotion, q1c_remains_dormant

## Verdict (house vocabulary)

**Forcing holds at the causal tier in this finite family.** When the
record-carrying degree of freedom is an emitted mode that propagates out of
the apparatus's causal control region on a discrete lightcone, the T392
access asymmetry follows from causal geometry: at a fixed full ordinary
event-level record and a fixed full SBS signature over `F1..F4`, the region
conditional state in preparation B is exactly phase-independent, so **no
channel supported on the control region** — not merely no inverse-coupling
protocol — recovers the prepared phase, while the identical in-region undo
recovers it before the mode escapes and a counterfactual enlargement across
the boundary recovers it after. T392's stipulated access triple is derived,
not assumed, **conditional on emission occurring**; the B' control shows
emission without record correlation splits nothing.

This upgrades the T392 existence result from Tier 3 (engineered) to Tier 1
(causal) in the typed forcing hierarchy, conditional on emission. It does
**not** reinstate Q1C, does not name a platform, and does not clear the T166
packet-intake gate or the T183 stack. Q1C remains **dormant**; packet/status
decisions pause for Joe per AGENTS.md.

## Predeclarations (fixed before inspecting numbers)

- Weak-coupling angle `theta = pi/3`; threshold `v* = 0.9` (both T392's,
  unchanged).
- Control region `{S, M, F1..F4, C0, C1}` (`r = 1`, chain `L = 3`), fixed
  once for every preparation; mode escape at step 2 by the discrete
  lightcone.
- Recovery figure of merit: phase-locked conditional X-visibility (declared
  because T392's own lemma showed raw visibility is gameable by manufactured
  coherence).
- Certificate sweep `phi in {0, 1.0, sqrt(2), pi/3, 2pi/3, pi/7}` (six
  values, including two incommensurate with `pi`); assertion `< 1e-12`.
- Haar spot-check: 50 samples, seed `20260701`, ceiling `0.05`, declared
  illustrative; the certificate carries the result.

## Exact computed values

### 1. Ordinary-record equality

`R` = joint `Z` distribution over `{S, M}`; tuples index-sorted, reading
`(S, M)` (`S` = qubit 0, `M` = qubit 1).

| `(S, M)` | P (prep A) | P (prep B) |
| --- | --- | --- |
| `(0, 0)` | 0.500000 | 0.500000 |
| `(1, 0)` | 0.375000 | 0.375000 |
| `(1, 1)` | 0.125000 | 0.125000 |

Max absolute difference A vs B: **0.0** (exact).

### 2. SBS closure key and full signature equality

- Key A = Key B = `('computational_z', 'sbs_objective', 'computational_z', True, 4)`;
  both D1-finalized (`R_delta = 4 >= 3`).
- Full signature (key + per-fragment conditional trace distances, all
  exactly `1.0` + full declared-register event-level `Z` distribution):
  max diff A vs B **0.0** (exact).
- Disclosure: the emission changes declared-register *coherences* only
  (reduced-density-matrix max diff `0.433`), invisible to the `Z`-basis
  record and the pointer-basis signature — same structure as T392.

### 3. The forcing theorem

- Phase-locked visibility after full in-region undo, prep A: **0.989743**
  (= `4 sqrt(3) / 7`, the T392 value; raw visibility identical).
- Phase-locked visibility after any tested in-region operation, prep B:
  **0.0** (`<= 1e-12`).
- **Certificate:** max pairwise difference of `rho_region|M=0` across the
  six-phase sweep — prep B: **2.2e-16** (asserted `< 1e-12`); prep A:
  **0.857** (asserted `> 0.1`). Every channel supported on the control
  region acts only on this state, so in B no channel output depends on the
  prepared phase.
- Haar spot-check (illustrative): 50 in-region Haar unitaries, max
  phase-locked visibility **1.6e-17** (ceiling `0.05`). Disclosure: max raw
  visibility across the same draws was `0.161` — phase-independent
  manufactured coherence, which is exactly why raw visibility is not the
  figure of merit.
- Manufactured-coherence control (T392's exploit, in-region on B): raw
  visibility **1.000000**, phase-locked **7.5e-17**.
- Representative non-unitary in-region channel (measure `C0`, feed back `X`
  on `S`, fragment undo): phase-locked visibility **0.0**.

### 4. Typed axis H and verdict

- `H(A) = 4` (all four fragments; any smaller subset gives locked visibility
  `0`). `H(B) = inf`, grounded in the causal certificate.
- `verdict_A = recoverable-in-control-region`,
  `verdict_B = final-relative-to-control-region`; both classes at prior mass
  `0.5` (T150 support met).

### 5. Far-end auxiliary channel (Z readout at C2)

| Loss function | risk(V \| R) | risk(V \| R, C2) | lift |
| --- | --- | --- | --- |
| symmetric 0-1 | 0.5000 | 0.2500 | **0.2500** |
| false-recover-costly (5:1) | 0.5000 | 0.2500 | **0.2500** |
| false-final-costly (4:1) | 0.5000 | 0.2500 | **0.2500** |

- `I(V ; C2 | R) = 0.5` bits `> 0`. Identical exact values to T392's `A0`
  channel — the escaped mode plays A0's role with its access status now
  forced by geometry.
- **T137 null:** downstream transform `S XOR M` of the ordinary record:
  lift exactly `0.0` on all three losses, CMI exactly `0.0`.
- **Disclosed boundary (emission-confound mixture):** in the uniform
  three-prep mixture `{A, B, B'}`, the 0-1 and false-final-costly lifts
  degenerate to exactly `0.0` at that symmetric prior (mass coincidence),
  while CMI stays positive (`0.2516` bits) and the false-recover-costly
  lift stays positive (`0.3333`). The T155 lift claim is scoped to the
  declared A/B family, matching T392; this mixture is disclosed, not
  claimed.

### 6. B' emission null control

- Verdict-relevant quantities vs A: record max diff **0.0**, full SBS
  signature max diff **0.0**, region conditional state max diff **0.0**
  (at every swept `phi`), locked undo visibility difference **0.0**,
  `H = 4` both, verdicts equal.
- The emission is real: global statevector max diff vs A **0.707**; chain
  excitation number `A: 0.0`, `B: 0.5`, `B': 1.0`. B' emits *more* chain
  energy than B and splits nothing: emission per se, and its energy
  signature, are not doing the work.

### 7. Recovery window and boundary sanity

| step | mode site | in region | locked visibility (in-region undo) |
| --- | --- | --- | --- |
| 0 | 0 | yes | **0.989743** |
| 1 | 1 | yes | **0.989743** |
| 2 | 2 | no | **0.000000** |

- Counterfactual enlargement (undo support includes escaped site `C2`):
  prep B recovery **0.989743**, difference from A **0.0** (exact); the
  enlarged conditional state is `phi`-dependent again (max diff `0.857`).
- Same circuit, same region, only the mode's causal position differs: the
  asymmetry tracks the light-cone, not a declaration.

## Forcing hierarchy position

Tier 1 (causal) earned here, conditional on emission. Tier 2
(thermodynamic — bath dispersion, undo cost scaling with bath contact,
Direction-C-facing dissipation accounting) is the named open card, not
built. Tier 3 (engineered) is T392, unchanged.

## Honest weaknesses (reviewer-facing)

- **"You chose to correlate the mode."** True, and scoped in-spec: the claim
  is not that measurements must emit records, but that WHEN a
  record-carrying mode is emitted — generic in real detectors (spontaneous
  emission, photon loss during readout) — the T392 access triple follows
  from causal geometry. The forcing is conditional on emission; the class
  is physically populated, not engineered.
- The toy lightcone is three perfect-SWAP sites with a perfect Z-copy;
  realism (partial emission amplitude, imperfect copies, longer chains) is
  future work and is why this stays a finite-family result.
- The uniform three-prep mixture disclosure above: two of three losses lose
  their lift at that specific symmetric prior. Scope of the lift claim is
  the declared A/B family, as in T392.
- The verdict is stated on the dominant `M = 0` branch, as in T392.

## pytest output

```
platform linux -- Python 3.10.12, pytest-9.1.1, pluggy-1.6.0
collected 23 items

tests/test_causal_forcing_access_asymmetry.py::test_lightcone_table_time_indexes_region_membership PASSED
tests/test_causal_forcing_access_asymmetry.py::test_ordinary_event_level_record_identical_A_vs_B PASSED
tests/test_causal_forcing_access_asymmetry.py::test_ordinary_record_is_a_normalized_distribution PASSED
tests/test_causal_forcing_access_asymmetry.py::test_sbs_closure_keys_identical_and_finalized PASSED
tests/test_causal_forcing_access_asymmetry.py::test_full_sbs_signature_identical_A_vs_B PASSED
tests/test_causal_forcing_access_asymmetry.py::test_full_in_region_undo_restores_A_to_t392_value PASSED
tests/test_causal_forcing_access_asymmetry.py::test_in_region_undo_fails_in_B PASSED
tests/test_causal_forcing_access_asymmetry.py::test_forcing_certificate_phi_independence_in_B PASSED
tests/test_causal_forcing_access_asymmetry.py::test_haar_spot_check_is_illustrative_and_null PASSED
tests/test_causal_forcing_access_asymmetry.py::test_manufactured_coherence_is_disclosed_and_nulled_by_phase_locking PASSED
tests/test_causal_forcing_access_asymmetry.py::test_non_unitary_in_region_channel_also_fails PASSED
tests/test_causal_forcing_access_asymmetry.py::test_typed_axis_H_finite_for_A_infinite_for_B PASSED
tests/test_causal_forcing_access_asymmetry.py::test_verdict_map_splits_with_both_classes_populated PASSED
tests/test_causal_forcing_access_asymmetry.py::test_far_end_detector_gives_positive_lift_across_loss_family PASSED
tests/test_causal_forcing_access_asymmetry.py::test_conditional_mutual_information_matches_t392 PASSED
tests/test_causal_forcing_access_asymmetry.py::test_t137_downstream_transform_null_is_exactly_zero PASSED
tests/test_causal_forcing_access_asymmetry.py::test_emission_confound_mixture_disclosure PASSED
tests/test_causal_forcing_access_asymmetry.py::test_bprime_identical_to_A_on_all_verdict_relevant_quantities PASSED
tests/test_causal_forcing_access_asymmetry.py::test_bprime_emission_is_real_but_innocuous PASSED
tests/test_causal_forcing_access_asymmetry.py::test_recovery_window_closes_exactly_at_escape_step PASSED
tests/test_causal_forcing_access_asymmetry.py::test_boundary_enlargement_restores_recovery_in_B PASSED
tests/test_causal_forcing_access_asymmetry.py::test_forcing_holds_end_to_end PASSED
tests/test_causal_forcing_access_asymmetry.py::test_verdict_language_is_restrained_house_vocabulary PASSED

23 passed in 6.00s
```

The T392 suite was re-run alongside and remains green (18 passed); T393
imports T392's machinery without modifying it.

## Recommended next (no promotion)

- The Tier-2 thermodynamic forcing card (bath dispersion, undo cost scaling,
  Direction-C dissipation connection) is the natural continuation if Joe
  wants to press Direction B further.
- Robustness sweeps (partial emission amplitude, imperfect copies, chain
  scaling) before any platform-facing conversation; T166 intake would pause
  for Joe in any case.

## Changelog

### v0.1.1 (2026-07-01) — post-hostile-review hardenings

Hostile-review ruling: **"(a) stands as stated"** — no blocking patches. Two
recommended hardenings, both validated independently in the reviewer's
scratch (`_local/t393_hostile_check.py`, a from-scratch re-implementation
with no repo imports), are now applied as earned model functions and tests.
**No existing number changed**: every v0.1 value above, every pre-existing
model print, and every existing `.json` field is bit-identical; the new
material is additive (`boundary_location_sweep` and
`partial_amplitude_robustness` blocks in the model output and JSON).

**Hardening 1 — boundary-location sweep** (`boundary_location_sweep`, three
new tests). The forcing certificate re-run for a smaller (`r = 0`) and an
enlarged (`r = 2`) control region, each fixed once for every preparation:

| region | step | mode site | cert max pairwise diff (prep B) | direction |
| --- | --- | --- | --- | --- |
| `r = 0` | 1 | `C1` (outside) | **2.2e-16** | forced: exactly `phi`-independent |
| `r = 0` | 0 | `C0` (inside) | **0.857** | not forced: `phi`-dependent |
| `r = 2` | 2 | `C2` (inside) | **0.857** | not forced: `phi`-dependent |

Every tested boundary placement (`r = 0, 1, 2`) yields the corresponding
verdict in both directions. The spec's stipulation-regress answer is
upgraded accordingly: the residual premise is only that the apparatus has
SOME bounded control region, not where its boundary sits.

**Hardening 2 — partial-amplitude thresholded forcing**
(`partial_amplitude_robustness`, `in_region_channel_bound`, three new
tests; staged v0.2 content brought forward). Emission via
`controlled-Ry(alpha)` (`F4 -> C0`) instead of CNOT:

| `alpha` | emit prob | frag-undo locked recovery | analytic `cos(alpha/2) * 4 sqrt(3)/7` | in-region channel bound | `< v* = 0.9` |
| --- | --- | --- | --- | --- | --- |
| `0.75 pi` | 0.8536 | 0.378758 | 0.378758 | **0.7575** | yes |
| `0.90 pi` | 0.9755 | 0.154830 | 0.154830 | **0.3097** | yes |
| `0.98 pi` | 0.9990 | 0.031089 | 0.031089 | **0.0622** | yes |
| `pi` | 1.0000 | 0.000000 | 0.000000 | **~0 (1.4e-16)** | yes |

The channel bound is channel-independent —
`2 (||Re X||_1 + ||Im X||_1)` with
`X = mean_phi e^{i phi} rho_region|M(phi)`, by Hoelder plus CPTP trace-norm
contractivity — so it covers EVERY channel supported on the control region
at once (unitary or not, with or without in-region ancillas). Sanity checks:
prep A's own bound (`1.9795`) respects its achievable recovery (`0.98974`);
the exact-CNOT prep-B bound is numerically zero; `alpha = pi` reproduces
the CNOT statevector exactly (max diff `3.7e-17`, the chain target starts
in `|0>`). **Forcing at threshold `v* = 0.9` is certified for
`alpha >~ 0.75 pi`**: the exact-zero form of the main theorem is the
`alpha = pi` idealization of a robust fact. Still open (unchanged pointers):
the analytic `alpha*(v*)` boundary and the Tier-2 thermodynamic card.

Suite after hardenings: **29 passed** in
`tests/test_causal_forcing_access_asymmetry.py` (23 v0.1 tests unchanged +
6 new), T392 suite still green alongside (18 passed).
