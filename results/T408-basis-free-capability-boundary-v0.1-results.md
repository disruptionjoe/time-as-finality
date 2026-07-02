# T408 Basis-Free Flat Pair and the Physical Capability Boundary — Results v0.1

- **Artifact:** `T408-basis-free-capability-boundary-v0.1`
- **Spec:** [tests/T408-basis-free-capability-boundary.md](../tests/T408-basis-free-capability-boundary.md)
- **Model:** [models/basis_free_capability_boundary.py](../models/basis_free_capability_boundary.py)
- **Test:** [tests/test_basis_free_capability_boundary.py](../tests/test_basis_free_capability_boundary.py)
- **Numbers:** [T408-basis-free-capability-boundary-v0.1.json](T408-basis-free-capability-boundary-v0.1.json)
- **Tags:** basis_free_flat_pair, menu_support_obstruction, graded_flat_curve,
  dissipation_bookkeeping_only, no_claim_promotion

**Numbering collision -- resolved 2026-07-01, authorized by Joe:** a
sibling lane's quartet (`T404-resource-theory-absorber-audit`) also landed
as T404 this session; distinct slugs, both quartets intact. The absorber
audit registered first and keeps T404; this artifact is renumbered
T404 -> T408 (per the T397/T407 precedent). See the spec's Status section.

## Verdict (house vocabulary)

**The basis-free flat pair holds in this finite family.** Two preparations
whose FULL record-region states are exactly identical as operators — so
every POVM on `R` in every basis, and every `R`-supported
intervention-then-readout statistic, is exactly equal — split on capability
under one fixed accessible-zone menu, with the zero side certified against
ALL channels supported on the menu's support. The split is sourced in a
single physical fact: whether the annex record carrier leaked onto the
outgoing mode and escaped the causal boundary (T393's forced escape,
conditional on emission). T407's statistics-flatness leg is thereby
upgraded from **declared-readout-relative** to **operator-level**: the
capability/statistics boundary in this family is not a readout convention.

The residual boundary is located exactly: by the menu-support obstruction
lemma (witnessed in both directions), the flat surface can be pushed to the
complement of the menu support and no further — a capability gap REQUIRES a
statistical trace within the menu's reach, and here that trace lives
entirely in zone coherences invisible to `R` in any basis and to the full
joint Z-basis readout on the whole zone. The graded alpha family sits on
one flat surface with a certified no-recovery band; the dissipation ledger
is bookkeeping only. **No claim promotion; no CLAIM-LEDGER entry; ledger
actions pause for Joe per AGENTS.md.**

## Predeclarations (fixed before inspecting numbers)

- `theta = pi/3`, `v* = 0.9` (T392's, imported unchanged); phase-locked
  visibility as the recovery figure of merit (T392's gameability lemma).
- Record region `R = {S, M, F1..F4}`; accessible zone
  `Z = R + {AX, C0, C1}` (T393's `r = 1` convention); escaped tail `C2`;
  all fixed once for every preparation; `N_STEPS = 2`.
- Certificate sweep `phi in {0, 1.0, sqrt(2), pi/3, 2pi/3, pi/7}` (T393's,
  incommensurate values included); flatness assertions `< 1e-12`.
- Alpha sweep `{0, 0.25, 0.5, 0.7, 0.75, 0.9, 0.98, 1.0} x pi`.
- Haar spot check 15 samples seed `20260702` ceiling `0.05`; random-basis
  check 20 samples seed `20260703`; both declared illustrative.
- Failure verdict predeclared: if no construction gave exact `rho_R`
  equality with a certified gap, report "capability difference requires an
  in-region statistical trace" (did not occur).

## Exact computed values

### Part 1 — basis-free flat pair

| Quantity | Value |
| --- | --- |
| `rho_R` operator diff, A vs {B, B', all alphas}, all 6 phases | **1.1e-16** |
| `rho_R` trace distance (max; certifies ALL POVMs + all R-channels) | **7.4e-17** |
| `rho_R` diff at lightcone steps 0/1/2 | **0.0** |
| M-conditioned active-region diff | **0.0** |
| 20 Haar-random bases on R, max prob diff (illustrative) | **0.0** |
| Declared Z-readout diff (a fortiori) | **0.0** |
| `rho_R` phi-independence within each prep (disclosure) | 1.7e-16 |
| Locked visibility A (extended undo, zone menu) | **0.989743** = `4 sqrt(3)/7` |
| Locked visibility B (best protocol / all-channel cert) | **6.1e-17** |
| Zone phi-independence certificate, B | **2.2e-16** |
| Zone channel-independent bound, B | **1.4e-16** (< v* = 0.9) |
| Zone phi-dependence teeth, A | 0.857 |
| R-only null: cert A / cert B (both preps final relative to R) | 2.2e-16 / 2.2e-16 |
| H(A) / H(B) (best 4-holder subset for A: 0.0) | **5 / inf** |
| Haar zone spot check (15 seeded unitaries, illustrative) | 1.6e-17 |
| Manufactured-coherence control raw / locked | 1.000000 / 6.9e-17 |
| B' capability diff from A / region diff / chain excitation | 0.0 / 0.0 / 1.0 |
| Recovery window (B): step 0 / 1 / 2 | 0.989743 / 0.989743 / 6.1e-17 |
| Counterfactual enlargement: visibility / diff from A | 0.989743 / 0.0 |
| Tail witnesses (A,A_tail), (B,B_tail): zone family / capability diffs | 1.1e-16 / <= 4.4e-16 |
| Zone trace distance A vs B (the located trace) | **0.494872** |
| Zone joint Z-basis readout diff / single-qubit marginal diff | **0.0 / 0.0** |

Verdicts: `recoverable-in-access-zone` (A) vs `final-relative-to-access-zone`
(B); both classes populated.

### Part 2 — graded curve (all rows on ONE operator-flat family)

| `alpha/pi` | `rho_R` flat | achieved | analytic `cos(a/2)·vis_A` | bound | escaped D | escaped Holevo (bits) | band |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 0.00 | 0.0 | 0.989743 | 0.989743 | 1.9795 | 0.000000 | 0.000000 | feasible_zero_cost |
| 0.25 | 5.6e-17 | 0.914404 | 0.914404 | 1.8288 | 0.382683 | 0.229549 | feasible_zero_cost |
| 0.50 | 5.6e-17 | 0.699854 | 0.699854 | 1.3997 | 0.707107 | 0.591673 | undetermined_by_bound |
| 0.70 | 5.7e-17 | 0.449334 | 0.449334 | **0.8987** | 0.891007 | 0.833095 | certified_infeasible |
| 0.75 | 5.6e-17 | 0.378758 | 0.378758 | 0.7575 | 0.923880 | 0.878335 | certified_infeasible |
| 0.90 | 1.1e-16 | 0.154830 | 0.154830 | 0.3097 | 0.987688 | 0.967745 | certified_infeasible |
| 0.98 | 5.6e-17 | 0.031089 | 0.031089 | 0.0622 | 0.999507 | 0.984526 | certified_infeasible |
| 1.00 | 0.0 | 0.000000 | 0.000000 | 0.0000 | 1.000000 | 0.985228 | certified_infeasible |

- Complementarity `(achieved/vis_A)^2 + D^2 = 1`: residual `<= 4.4e-16` at
  every row; `D = sin(alpha/2)` to `< 1e-9`.
- Analytic protocol-feasibility edge: `alpha = 0.273195 pi`
  (`= 2 acos(v*/vis_A)`), consistent with the bands.
- **Disclosure:** the bound computes to exactly `2x` the achieved value in
  this family, so certification starts at `~0.70 pi` while feasibility ends
  at `0.273 pi`; the mid-band is honestly undetermined (T393's open
  `alpha*(v*)` card, now measured loose in two artifacts).

### Part 3 — dissipation ledger (T142 conventions; bookkeeping only)

| Entry | Mode | erased bits | `beta W` floor | capability outcome |
| --- | --- | --- | --- | --- |
| restore A (in-zone) | correlated_uncopy (5 holders) | **0** | 0.0 | 0.989743 restored |
| delete A (in-zone) | blind_reset (5 holders) | 5 naive (`5 ln 2 = 3.4657` nats); joint record entropy 0.98523 bits at `M=0`, 1.0 unconditioned | 3.4657 naive | **0.0 restored; record deleted (residual 0.0)** |
| restore B (in-zone) | — feasible set EMPTY (certified) | — | **inf (empty-set infimum)** | limiting resource: ACCESS to the escaped holder, not work |
| restore B (counterfactual, zone + C2) | correlated_uncopy (6 holders) | 0 | 0.0 | 0.989743 restored exactly (blind-reset disclosure `6 ln 2`) |

The stated correspondence in this family: capability retained
`cos(alpha/2)`, escaped-holder distinguishability `sin(alpha/2)` (exact
complementarity), escaped Holevo content `0 -> h2(3/7) = 0.98523` bits;
in-zone restoration ledger `0` wherever feasible and an empty-set infimum
where certified infeasible; **blind-reset dissipation at any alpha buys
record deletion, never capability restoration** (deletion is not
definalization — T144/T145 discipline, computed). The B-side infinity is
typed precisely: NOT a divergent work requirement (this closed unitary
model has no work parameter); an access obstruction recorded in
extended-real bookkeeping. The genuine open-system bound (bath dispersion,
work/entropy scaling with bath contact) is T393's Tier-2 card — named,
unbuilt.

### Guardrails

- **Q1D:** declared R readout invariant across preparations, phases, leak
  amplitudes (`1.1e-16`); in-zone undo moves the escaped marginal by `0.0`
  (no signalling out) while the counterfactual enlarged undo moves it by
  `0.42857 = 3/7` (teeth); zone trace-distance teeth `0.494872`.
- **R1:** untouched; the discrete SWAP-chain lightcone carries T393/T379's
  caveats.

## Tests

`tests/test_basis_free_capability_boundary.py`: **35 passed** (~1.4 s).
Neighbor suites re-run green alongside: T392 (18), T393 (29), T407 region
no-go (34), T142 (6) — **87 passed**. Deterministic; exact statevector; the
only sampling (Haar, random bases) is seeded and illustrative.

## What this does not earn

No thermodynamic theorem (Part 3 is bookkeeping in a finite closed unitary
model); no clearing of T400's boundary-forced-task gate; no new mathematics
(the flat pair's existence is presumed textbook purification freedom —
flagged from memory, unverified); no hardware or platform; not TI's Ext_S
surplus; no CLAIM-LEDGER movement. All promotion decisions pause for Joe.
