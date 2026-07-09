# Spec: generalizing the three-wall ladder to qudits (d > 2)

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

## First move next session

Confirm `F_share(3)` and `F_CGLMP(3)` from the literature (a short research step), wire them into the
skeleton's calibration asserts, implement the CGLMP operator, then run the statewise sweep.
