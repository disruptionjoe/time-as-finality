# T395 Record-Order Trade-off Probe — Results v0.1

- **Artifact:** `T395-record-order-tradeoff-probe-v0.1`
- **Spec:** [tests/T395-record-order-tradeoff-probe.md](../tests/T395-record-order-tradeoff-probe.md)
- **Model:** [models/record_order_tradeoff_probe.py](../models/record_order_tradeoff_probe.py)
- **Test:** [tests/test_record_order_tradeoff_probe.py](../tests/test_record_order_tradeoff_probe.py)
- **Numbers:** [T395-record-order-tradeoff-probe-v0.1.json](T395-record-order-tradeoff-probe-v0.1.json)
- **Tags:** direction_a, record_order_probe, duality_collapse,
  kill_test_executed, exhaustive_finite_family, no_claim_promotion,
  prior_art_flagged_from_memory

## Verdict (house vocabulary)

**The v0.1 record-order bound reduces to interferometric duality in the
two-order family; separation, if any, lives at k >= 3 partial-record
structure.** The kill-test collapsed, and the collapse is exact: the
switch+record statevector IS a Mach-Zehnder-with-two-which-path-markers
state term by term (max difference `1.1e-16` across the full sweep), the
`(D, V)` curve is the Greenberger–Yasin/Englert duality with the target
acting as a second, fixed-strength order marker, and the residue in the
two-order family is interpretational only (calling the interferometer arms
"composition orders"), not quantitative. This is the decisive, honest
outcome the artifact was built to force: the Direction-A inequality, if it
exists, must contain structure beyond two orders.

The k = 3 probe shows what that structure looks like in the smallest honest
instance: a class-coarse (partial-access) record produces a class-graded
trade-off — binary duality exact pairwise across classes, exactly absent
within classes, and unreproducible by every tested global scalarization —
with a record ceiling on order postdiction (`2/3` for 3 orders, `1/3` for 6)
coexisting with intact within-class coherence at a PERFECT class record.
Finite observation, exhaustively verified in the declared family (91
configurations), not a theorem.

No claim promotion. No CLAIM-LEDGER entry. Q1D and R1 guardrails asserted.

## Predeclarations (fixed before inspecting numbers)

- `gamma` sweep: 21 values on `[0, pi]`, endpoints exact (spec floor >= 20).
- Exactness tolerance `1e-12` for every relation claimed exact.
- Canonical pair criterion: balanced two-marker point `|K| = 1/sqrt(2)`
  among the swept candidates; the degenerate maximal-sensitivity candidate
  (`|K| = 0`) documented, not chosen.
- `D` = trace-distance order-distinguishability of the record (Helstrom);
  `V` = exact control coherence `2|rho_c[0,1]|`, cross-checked on a 720-point
  phase grid. `V` is NOT a causal witness (named v0.1 limitation; SDP rung
  not built).
- Verdict strings predeclared as module constants, asserted verbatim.
- Subsystems index-sorted `(c, r, t)`; k-order control is a k-level system
  (total Hilbert dimension <= 24, inside the 6-qubit budget).

## Exact computed values

### 1. Canonical pair sweep (documented)

| pair (on psi = \|0>) | \|K\| | order sensitivity | chosen |
| --- | --- | --- | --- |
| Ry(pi/2), Rz(pi/2) | 0.707107 | 0.707107 | **yes** (balanced point, exactly 1/sqrt 2) |
| Ry(pi/2), Rz(pi) | 0.000000 | 1.000000 | no — degenerate: V == 0, trade-off invisible |
| Rx(pi/2), Rz(pi/2) | 0.707107 | 0.707107 | no (tie; first candidate kept) |
| Ry(pi/2), Rz(pi/4) | 0.923880 | 0.382683 | no |

### 2. The trade-off curve (two-order family, V0 = 0.707107)

| gamma | D | D_Z | V | D_joint | Helstrom success |
| --- | --- | --- | --- | --- | --- |
| 0 | 0.000000 | 0.000000 | 0.707107 | 0.707107 | 0.500000 |
| pi/4 | 0.382683 | 0.146447 | 0.653281 | 0.757115 | 0.691342 |
| pi/2 | 0.707107 | 0.500000 | 0.500000 | 0.866025 | 0.853553 |
| 3pi/4 | 0.923880 | 0.853553 | 0.270598 | 0.962692 | 0.961940 |
| pi | 1.000000 | 1.000000 | 0.000000 | 1.000000 | 1.000000 |

Exact relations, max residual over the full 21-point sweep:

| relation | max residual |
| --- | --- |
| `D = sin(gamma/2)` | 1.1e-16 |
| `V = V0 cos(gamma/2)` | 1.1e-16 |
| `D^2 + (V/V0)^2 = 1` (normalized binary duality) | 4.4e-16 |
| `D_joint^2 + V^2 = 1` (Englert saturation, joint marker) | 8.9e-16 |
| `D^2 + V^2 + (1 - D^2) Dt0^2 = 1` (three-way decomposition) | 2.2e-16 |
| `D_Z = D^2` (accessible Z-readout disclosure) | 2.2e-16 |

`D` strictly increasing, `V` strictly decreasing; the candidate bound
`D^2 + V^2 <= 1` holds with slack exactly `(1 - V0^2)(1 - D^2)` — the unread
target-marker term (min slack over sweep `0.0`, at `gamma = pi`).

### 3. Accessibility (the record-fixed / causally-separable boundary)

Reduced (control, target) state, record traced vs measured-and-forgotten:
max difference **5.6e-17** at every swept `gamma`. Elementary (an identity of
partial trace) but load-bearing: at fixed `gamma`, record ACCESSIBILITY moves
no process marginal; the (1)/(2) boundary is capability-relative (what the
record holder can postdict, `D`), not marginal-statistics-relative.

### 4. Q1D no-signalling certificate

- Joint (c, r) Z-marginal over 4 setting combinations x 5 gammas x 2 control
  phases: max difference **1.7e-16** (settings `A_x = A Rz(0.9)^x`,
  `B_y = B Rx(0.7)^y`, predeclared).
- Record marginal over control phase: max difference **1.7e-16**.
- Teeth: the same settings move the target marginal by >= **0.1611**.
- Disclosed: a single target traverses both operations; the asserted surface
  is that order/record readout cannot be steered by local operation choices.

### 5. The reduction audit (the kill-test)

| check | value |
| --- | --- |
| switch state vs mapped MZ state (21 gammas x 3 phases) | **1.1e-16** |
| `D` curve vs plain-MZ `D` curve | **0.0** |
| normalized `V` curve vs plain-MZ `V` curve | **1.1e-16** |
| Englert saturation (joint marker) | **8.9e-16** |
| **collapsed_to_duality** | **True** |

Mapping (implemented, not just argued): control -> path, order branches ->
arms, record -> which-path marker (same controlled-Ry coupling), target ->
internal dof = second fixed-strength marker with branch overlap `K`.

### 6. The k = 3 probe (canonical: orders {ABC, BAC, CAB}, class = "A before B")

- Circuit vs branch-sum construction: max diff **6.7e-17**; norms exact.
- Within-class coherence gamma-flatness: max deviation **0.0** (exact).
- Cross-class pairwise duality `sin^2 + (V_ij/V_ij(0))^2 = 1`: max residual
  **5.6e-16**; cross-class cos-scaling residual **exact to 1e-15** throughout.
- Order postdiction from the record alone:
  `P(gamma) = (1/3)(1 + sin(gamma/2))` — endpoints `1/3` and **2/3** (the
  class ceiling), monotone; grid achievability within `1e-4` and never above
  the analytic optimum (2000-point projective grid).
- Class postdiction (Helstrom, priors 2/3 : 1/3): `2/3` at `gamma = 0`,
  **1.0** at `gamma = pi` — the class IS recorded even though the order is not.
- Global scalarizations, circle residual `D_glob^2 + V_s^2 - 1` at
  `gamma = pi`: mean **-0.639**, min **-0.750**, max **+0.250** (exactly
  `+sin^2(gamma/2)/4`). None stays on the circle anywhere on the sweep
  (`no_scalarization_stays_on_circle = True`). The binary form fails in both
  directions depending on scalarization: irreducibly class-graded.
- Baseline pairwise coherences (canonical subset): ABC|BAC 0.707107,
  ABC|CAB 0.707107, BAC|CAB 1.000000 (a cross-class pair with full baseline;
  its coherence dies exactly as cos(gamma/2)).

### 7. Six-order coherent sum (all 3! orders, class = permutation parity)

- Within-class flatness and cross-class duality: **exact (0.0 residuals)**;
  2 degenerate zero-baseline pairs disclosed (they satisfy the cos-scaling
  form trivially).
- Order postdiction ceiling at `gamma = pi`: **1/3** (= 2/6). A PERFECT
  parity record leaves 2/3 of order postdiction unreachable and all
  within-parity coherence intact.

### 8. Exhaustive family sweep

All C(6,3) = 20 three-order subsets x 3 bipartitions (**60 configs**) plus
the full 6-order sum x all 31 bipartitions (**31 configs**), each on the full
21-point gamma sweep: within-class flatness max **0.0**, cross-class duality
max residual **6.7e-16**, cos-scaling max residual **6.7e-16**, guess ceiling
`2/k` in every configuration. **all_pass = True.** Within this declared
family the k >= 3 pattern is exhaustive; beyond it, nothing is claimed.

### 9. Full-resolution contrast

A k-level record register at `gamma = pi`: postdiction **1.000000**, max
pairwise coherence **0.0** (the binary-duality corner). The class-coarse
ceiling is a consequence of partial ACCESS, not of k: class-coarse perfect
record gives postdiction 0.666667 with within-class coherence 0.707107.

## Honest weaknesses (reviewer-facing)

- **The collapse was definitionally forced (an identity of the branch
  form), not merely foreseeable — and is likely known.** The switch with a
  decohered/marked control being an interferometer over orders is very
  plausibly explicit in the causal-order literature (Brukner-group control
  decoherence work; the "is the photonic switch an interferometer?" debate)
  — all flagged from memory, unverified. The artifact's value is pricing the
  Direction-A hinge honestly, not novelty of the two-order result.
- **The k = 3 headline results are likewise identities of the branch form.**
  Within-class gamma-flatness, cross-class cos-scaling/duality, and the
  `2/k` ceiling follow directly from the branch form (the within-class
  record branch overlap is identically 1; cross-class identically
  cos(gamma/2)), so the 91-configuration sweep re-verifies an identity 91
  times rather than probing 91 independent contingencies.
- **`V` is not a causal witness.** All statements are scoped to the
  visibility signature; the SDP random-robustness rung is the named next
  step. A genuine witness could in principle behave differently from `V`
  (though not in what it is a function of: the reduced process is fixed).
- **The k = 3 residue has a named absorber.** Multibeam-interferometer
  duality (Dürr / Englert-et-al.-style, from memory) may transplant the
  class-graded structure exactly the way binary duality transplanted the
  two-order structure. Until that absorber is run, the "genuinely new
  territory" reading of k >= 3 is provisional.
- **The scalarization exhibit mixes structure levels.** `D_glob` (full-order
  postdiction) against pairwise-coherence scalarizations is an honest
  demonstration that no tested scalar pair keeps the binary form, not a
  uniqueness proof; a cleverer scalar pair is not excluded by exhaustion
  over three scalarizations.
- **Ties, not incomparability.** The k = 3 record induces a partition with
  ties; genuine T49-style incomparability (nested/partial partitions,
  multi-holder records) is future work. The anti-scalar connection is
  structural vocabulary, not a derivation.

## pytest output

```
platform linux -- Python 3.10.12, pytest-9.1.1, pluggy-1.6.0
collected 35 items

tests/test_record_order_tradeoff_probe.py::test_gamma_sweep_predeclared PASSED
tests/test_record_order_tradeoff_probe.py::test_state_normalized_and_circuit_equals_branch_sum PASSED
tests/test_record_order_tradeoff_probe.py::test_canonical_pair_documented_and_balanced PASSED
tests/test_record_order_tradeoff_probe.py::test_D_endpoints_exact PASSED
tests/test_record_order_tradeoff_probe.py::test_V_endpoints_exact PASSED
tests/test_record_order_tradeoff_probe.py::test_D_matches_sin_half_gamma PASSED
tests/test_record_order_tradeoff_probe.py::test_V_matches_V0_cos_half_gamma PASSED
tests/test_record_order_tradeoff_probe.py::test_monotonicity_D_up_V_down PASSED
tests/test_record_order_tradeoff_probe.py::test_helstrom_success_endpoints PASSED
tests/test_record_order_tradeoff_probe.py::test_accessible_z_readout_is_D_squared PASSED
tests/test_record_order_tradeoff_probe.py::test_normalized_duality_exact PASSED
tests/test_record_order_tradeoff_probe.py::test_englert_joint_saturation_exact PASSED
tests/test_record_order_tradeoff_probe.py::test_three_way_decomposition_exact PASSED
tests/test_record_order_tradeoff_probe.py::test_fringe_grid_matches_exact_visibility PASSED
tests/test_record_order_tradeoff_probe.py::test_asymmetric_control_spot_check PASSED
tests/test_record_order_tradeoff_probe.py::test_accessibility_trace_vs_measure_invariance PASSED
tests/test_record_order_tradeoff_probe.py::test_no_signalling_cr_marginals_setting_independent PASSED
tests/test_record_order_tradeoff_probe.py::test_no_signalling_check_has_teeth PASSED
tests/test_record_order_tradeoff_probe.py::test_mz_statevector_identity_across_sweep PASSED
tests/test_record_order_tradeoff_probe.py::test_plain_mz_curves_coincide_with_normalized_switch PASSED
tests/test_record_order_tradeoff_probe.py::test_reduction_verdict_is_collapse PASSED
tests/test_record_order_tradeoff_probe.py::test_mz_mapping_is_documented PASSED
tests/test_record_order_tradeoff_probe.py::test_k3_circuit_equals_branch_sum PASSED
tests/test_record_order_tradeoff_probe.py::test_k3_within_class_coherence_gamma_flat PASSED
tests/test_record_order_tradeoff_probe.py::test_k3_cross_class_pairwise_duality_exact PASSED
tests/test_record_order_tradeoff_probe.py::test_k3_guess_prob_formula_endpoints_and_monotone PASSED
tests/test_record_order_tradeoff_probe.py::test_k3_guess_prob_grid_achievability PASSED
tests/test_record_order_tradeoff_probe.py::test_k3_perfect_class_record_ceiling PASSED
tests/test_record_order_tradeoff_probe.py::test_k3_class_helstrom_reaches_1_at_pi PASSED
tests/test_record_order_tradeoff_probe.py::test_k3_global_scalarizations_fail_binary_form PASSED
tests/test_record_order_tradeoff_probe.py::test_six_order_parity_ceiling_one_third PASSED
tests/test_record_order_tradeoff_probe.py::test_exhaustive_family_sweep_all_pass PASSED
tests/test_record_order_tradeoff_probe.py::test_full_resolution_contrast PASSED
tests/test_record_order_tradeoff_probe.py::test_verdict_strings_are_predeclared_and_restrained PASSED
tests/test_record_order_tradeoff_probe.py::test_result_dict_is_json_serializable PASSED

35 passed in 5.80s
```

The T392 (18) and T393 (29) suites were re-run alongside and remain green
(47 passed); T395 imports nothing from them.

## Recommended next (no promotion)

- Run the multipath-duality absorber against the k = 3 class-graded
  structure (this artifact's own kill-test pattern, one level up) BEFORE any
  investment in a k >= 3 inequality.
- The SDP causal-witness rung, if Direction A continues: replace `V` with a
  random-robustness witness as a function of `gamma` and re-run the audit.
- Multi-holder record structure (D1 redundancy axis) is where record
  FINALITY, as opposed to record existence, first becomes distinguishable in
  this lane — and where the capability-relative accessibility result (§3)
  says the criterion must live.
- Verify the flagged prior art before any external-facing artifact; the
  two-order collapse in particular should be checked against the switch
  control-decoherence literature. Pauses for Joe per AGENTS.md.

## v0.1 → v0.1.1 review patches

Hostile-review re-scopes; ruling: "(b) stands re-scoped". No numbers or
verdict values changed.

- Two-order collapse re-scoped: definitionally forced by the v0.1
  operationalization (D = marker trace-distance, V = control coherence, pure
  two-branch family) — an algebraic identity of the branch form, not a
  contingent kill-test outcome. Earned content: the explicit term-by-term MZ
  mapping and the three-way pricing.
- Honest-weaknesses bullet strengthened from "foreseeable" to
  "definitionally forced (an identity of the branch form), not merely
  foreseeable".
- Matching k = 3 re-scope: within-class flatness, cross-class cos-scaling,
  and the `2/k` ceiling are identities of the branch form; the
  91-configuration sweep re-verifies an identity 91 times.
- Test-suite docstring re-pinned: regression-pinned to the analytically
  forced verdict (was: "asserted whichever way the numerics land").
- Spec Claim/Status and Reduction Audit carry the same re-scope sentence;
  "an honest collapse is a decisive outcome" re-phrased to "a forced
  collapse, made explicit".
