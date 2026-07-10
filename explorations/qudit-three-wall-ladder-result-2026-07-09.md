# The three-wall ladder generalizes to qutrits (d=3)

2026-07-09. The qudit "big swing," executed. Model: `models/finality_qudit_three_walls.py` (exit 0). Spec:
`open-problems/qudit-ladder-generalization-spec-2026-07-09.md`. Prior (two-qubit) result:
`explorations/P1-constructor-axiom-and-three-wall-ladder-2026-07-08.md`.

## What was built

The genuinely new piece was the **CGLMP Bell operator** (CHSH does not generalize to d>2). It passed its
calibration gate before anything else ran:

- `CGLMP(maximally entangled qutrit) = 2.8729` -- the standard qutrit value, so the operator is correct;
- `CGLMP(white noise) = 0.0000`.

Reused, verified: isotropic family, generalized negativity, full symmetric-extension POCS (calibrated to the
2/3 wall on qubit Werner).

## Result 1 -- three distinct nested walls on the isotropic line

| wall | F | monotone |
|---|---|---|
| entanglement | 1/d = 0.333 | negativity |
| shareability | 0.670 | full symmetric-extension SDP (POCS) |
| CGLMP | 0.730 | fixed optimal CGLMP-3 measurements |

Ordered `1/d < F_share < F_CGLMP`, distinct (gaps > 0.02), **both gaps populated**: an entangled-but-
shareable isotropic state exists between walls 1 and 2, and an un-shareable but CGLMP-local state exists
between walls 2 and 3.

Literature cross-check: `F_CGLMP = 0.730` maps to visibility `v = (9F-1)/8 = 0.696`, matching the known
CGLMP-3 noise-threshold visibility ~0.6961 for the maximally entangled qutrit -- an independent confirmation
that the CGLMP operator is right.

## Result 2 -- statewise nesting off the isotropic line

170 random 3x3 states (120 generic + 50 standard-basis-aligned noisy-maxent, added specifically so the
sweep produces genuine violators). Of these, **49 CGLMP-violating** and 41 shareable:

- **I1 holds NON-vacuously:** zero of the 49 CGLMP-violating states are shareable (monogamy of nonlocality:
  a 2-shareable state admits a local model, so cannot violate any Bell inequality). This is the substantive
  test -- the first random sweep produced 0 violators and so was vacuous; the violator batch fixes that.
- `{CGLMP-violating} subset {entangled}`: zero violations.
- Both gaps stay non-empty off the isotropic line: 41 entangled-but-shareable, 80 un-shareable-but-CGLMP-
  local.

## Verdict

**The three-wall ladder generalizes from qubits to qutrits.** Entanglement < shareability < CGLMP are three
distinct nested walls at d=3, each with its own monotone; both gaps stay populated on and off the isotropic
line; and the key implication (CGLMP-violating => un-shareable) holds statewise on genuine violators. The
Werner/isotropic NUMBERS differ from d=2 but the STRUCTURE is the same -- consistent with the theorem-backed
generality established in the two-qubit off-Werner test.

## Follow-up (2026-07-09, later session): three honest limits closed

- **#1 shareability closed form -- CLOSED (T516).** The isotropic 2-shareability
  wall is `F_share(d) = (d+1)/(2d)` (Johnson & Viola PRA 88 032323; arXiv
  0906.5255), independently bracketed by POCS at d=2,3,4. So `F_share=0.670` at
  d=3 is exactly `2/3`. `results/T516-isotropic-shareability-closed-form-v0.1-results.md`.
- **#2 bound entanglement -- CLOSED (T514).** A CCNR/realignment witness upgrades
  the outer wall from "NPT-entangled" to "entangled"; it detects the Tiles UPB
  bound-entangled state (negativity ~0, CCNR 1.087). The isotropic-line ladder is
  unchanged (PPT=sep there). `results/T514-ccnr-bound-entanglement-witness-v0.1-results.md`.
- **#4 d>=4 -- EXTENDED (T515).** The ladder holds at d=4 too. Building CGLMP-4
  surfaced a latent sign bug in `models.finality_qudit_three_walls.cglmp` (the
  k>=1 term, never fired at d<=3); the corrected operator matches the standard
  CGLMP values exactly at d=2,3,4,5. **This d=3 result is unaffected** (it only
  ever used k=0). `results/T515-qudit-d4-ladder-v0.1-results.md`.

Still open: certified dual-witness SDP for shareability (POCS remains a
feasibility test); CGLMP measurements are a witness (sufficient, not necessary).

## Honest limits (the remaining build, unchanged from the spec)

- **Shareability via POCS, not a certified SDP.** POCS returns a tolerance verdict, not a dual-witness
  certificate; the methods-pass recommendation (exact SDP with certificates, or the symmetry-reduced
  closed form for the isotropic wall) is still the right upgrade. `F_share=0.670` should be confirmed
  against a closed form.
- **"Entangled" = NPT (negativity>0).** Bound (PPT) entanglement is not separately detected; a CCNR witness
  is still to be added. Bound-entangled states are measure-~0 in random sampling, so this does not affect
  the sweep results, but it means the outer wall is "NPT-entangled," not "entangled," until CCNR is wired in.
- **Fixed CGLMP measurements** = a nonlocality WITNESS (sufficient, not necessary): it certifies violation
  for aligned states and can miss violation for rotated ones. This only strengthens I1 (every flagged
  violator is genuinely nonlocal) but means CGLMP-non-violation here is not a certificate of locality.
- **d=3 only.** d>=4 unchecked; the symmetry-reduced calibration would make higher d cheap.
