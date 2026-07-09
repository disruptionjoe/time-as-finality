# Spec: generalizing the three-wall ladder to qudits (d > 2)

> **STATUS 2026-07-09: big swing DONE for d=3** -- three distinct nested walls confirmed
> (1/d < F_share=0.670 < F_CGLMP=0.730), CGLMP operator built and self-checked (2.8729 on maxent; visibility
> 0.696 matches literature), I1 confirmed non-vacuously on 49 genuine violators. Result:
> `explorations/qudit-three-wall-ladder-result-2026-07-09.md`, model `models/finality_qudit_three_walls.py`.
> Remaining: certified SDP (POCS -> dual witness) + symmetry-reduced closed-form F_share; CCNR bound-
> entanglement witness; d>=4. The items below are the still-open build.


Open-problem spec, 2026-07-09. Sets up the next campaign: does the three-wall ladder
(entanglement < shareability < Bell) survive beyond two qubits? Companion skeleton:
`models/finality_ladder_qudit.py`. Prior result (two qubits, confirmed):
`explorations/P1-constructor-axiom-and-three-wall-ladder-2026-07-08.md`.

## Goal

Test whether `{Bell-violating} subset {un-shareable} subset {entangled}` (three distinct nested walls, each
with its own monotone) holds for `d x d` states with `d >= 3`, and whether the walls stay distinct
(both gaps non-empty). If it holds, the ladder is a general feature of finality, not a qubit accident.

## Four technical shifts from the two-qubit test (why this is a heavier build)

1. **PPT is no longer separability.** For `d > 2` there exist PPT-bound-entangled states. So negativity = 0
   NO LONGER implies separable, and the 2-qubit `PPT => shareable` short-circuit (used to fix the I2 false-
   negatives) is INVALID. Consequences:
   - "entangled" splits into NPT (negativity > 0) and PPT-bound-entangled. Decide what the outer rung means.
     Recommended: keep the outer rung as **separable vs entangled**, and restrict CALIBRATION to families
     where separability is analytically known (isotropic), so the split is controlled.
   - shareability must be decided by the **full symmetric-extension SDP** every time -- no shortcut.
2. **Entanglement detection.** Negativity stays a valid monotone (>0 => entangled) but no longer certifies
   separability. Add the CCNR / realignment criterion as a second bound-entanglement witness if the general
   sweep is attempted; for the isotropic calibration family it is not needed (isotropic has no bound
   entanglement: PPT <=> separable <=> F <= 1/d).
3. **Bell inequality.** CHSH -> **CGLMP** (Collins-Gisin-Linden-Massar-Popescu), the natural d-outcome,
   2-setting Bell inequality. Local bound 2; the "Bell wall" becomes the CGLMP-violation threshold. The
   CGLMP Bell operator must be constructed and its optimal-measurement expectation evaluated.
4. **Cost.** The extension SDP lives in `d^3` dimensions (d=3 -> 27x27). POCS is fine there but slower;
   random-state sampling with a per-state SDP is the expensive part.

## Calibration family: isotropic states

`rho(F, d) = F |Phi><Phi| + (1-F)/(d^2 - 1) (I - |Phi><Phi|)`, with `|Phi> = (1/sqrt d) sum_i |ii>` and
singlet fraction `F in [0,1]`. Known anchors:

- **Separable / entanglement wall:** isotropic is separable iff `F <= 1/d` (Horodecki); PPT <=> separable
  here, so negativity crosses 0 exactly at `F = 1/d`. (Reliable calibration anchor.)
- **Shareability wall:** the isotropic 2-extendibility threshold `F_share(d)` -- CONFIRM against literature
  (Johnson-Viola / Terhal-Doherty-type results) before trusting the skeleton's empirical POCS value.
- **CGLMP wall:** the isotropic CGLMP-violation threshold `F_CGLMP(d)` -- known numeric for d=3; confirm.

The nesting predicts `1/d < F_share(d) < F_CGLMP(d)` and both gaps non-empty.

## Test structure (mirrors the two-qubit model)

1. **Calibrate** the extension SDP on the isotropic line: its empirical shareability wall must match the
   literature `F_share(d)`; if not, report the shareability rung UNVERIFIED (do not proceed to statewise).
2. **Rigorous rung (no SDP):** random general `d x d` states -- confirm `{CGLMP-violating} subset
   {entangled}` with zero violations, and the gap non-empty (entangled but CGLMP-local exist).
3. **Full nesting (if calibrated):** statewise `{CGLMP} subset {un-shareable} subset {entangled}` on a
   random + isotropic sample; both gaps non-empty. Handle PPT-bound entanglement honestly (a bound-entangled
   state is entangled but NPT-negativity misses it -- use CCNR, and expect it to sit inside the entangled
   wall).

## Kill criteria

- If a **shareable** state is found that **violates CGLMP** (I1 fails on a genuine SDP verdict, not a
  numerical edge), the nesting is false for qudits -- a real, publishable negative.
- If PPT-bound entanglement makes the outer "entangled" wall incoherent (e.g., bound-entangled states are
  shareable AND un-CGLMP but the ladder can't place them), the ladder does not generalize cleanly and needs
  reformulation (perhaps the outer rung should be **distillable** entanglement, not entanglement).
- If the SDP cannot be calibrated to the literature `F_share(3)`, the tooling is not ready and the qudit
  claim stays open.

## Skeleton status (`models/finality_ladder_qudit.py`)

Implemented and runnable now (d=3): isotropic family, generalized negativity, generalized symmetric-
extension POCS, and it prints the empirical entanglement wall (expect `1/d`) and shareability wall. Marked
TODO (the real remaining build): (a) CGLMP Bell operator + isotropic threshold, (b) CCNR bound-entanglement
witness, (c) the random-state statewise sweep, (d) literature confirmation of `F_share(3)` and `F_CGLMP(3)`.

## Recommended implementation approach (ten-persona methods pass, 2026-07-09)

The key realization: **most of this test should not be brute-forced.**

- **Calibration by symmetry reduction, not POCS.** The isotropic family is `U (x) conj(U)`-invariant, so the
  extension SDP twirls into a block-diagonal form (Schur-Weyl / commutant) and collapses to a handful of
  scalars -- `F_share(d)` comes out closed-form. This replaces the slow, tolerance-fragile POCS calibration
  AND supplies the literature value in one move. (Generalizes swing C's S_3-twirl.)
- **Prove the nesting order, do not test it.** Both implications are theorems (Toner-Verstraete monogamy;
  separable => shareable). Computation is only needed for whether the walls stay DISTINCT (gaps non-empty)
  off the symmetric line.
- **Off-symmetry distinctness sweep = the only hard part.** Build it as: batched/vectorized NLA (numpy
  stacks or Torch/GPU) for negativity + CGLMP over many states; a cheap learned/heuristic classifier to gate
  the expensive step to near-boundary states only; an EXACT SDP with dual certificates (DPS-1 + PPT via
  CVXPY/PICOS -> MOSEK/SCS) for those -- infeasibility returns an unextendibility witness, not a tolerance
  verdict (this is what removes the POCS false-negative failure mode); and property-based fuzzing that
  actively hunts counterexamples at bound-entangled and high-symmetry states.
- **Fail-closed calibration gate.** Regression-test against the PROVEN d=2 numbers and HALT on mismatch --
  encode "never trust an uncalibrated tool" as a hard check. Seed RNG; emit JSON with provenance.

**Other ways (counterfactual / alternative formulations) to keep as cross-checks:**

- **Cloning-game (counterfactual):** recast 2-shareability as "could a hypothetical symmetric third party
  hold the same correlation?" -- a monogamy game value, not a matrix construction. Independent cross-check on
  the SDP verdict.
- **Operational certification:** certify each wall from correlations + witnesses (CGLMP from statistics;
  monogamy witness for unshareability), bypassing the state representation and its tolerance ambiguity.
- **Formal proof** (Lean / rigorous interval SDP) for the theorem-backed implications and the final wall
  values.

## First move next session

Symmetry-reduce the isotropic calibration to get `F_share(3)` closed-form (this replaces the POCS
calibration and confirms the literature value at once); confirm `F_CGLMP(3)`; implement the CGLMP operator;
then run the off-symmetry distinctness sweep with the certified-SDP-behind-a-classifier stack above. Use the
cloning-game as an independent cross-check on shareability.
