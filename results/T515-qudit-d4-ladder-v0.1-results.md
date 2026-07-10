# T515 Results -- the three-wall ladder at d=4 (and a CGLMP-d correction)

**Verdict:** `THREE_WALL_LADDER_GENERALIZES_TO_D4_CGLMP_OPERATOR_CORRECTED`
**Model:** `models/finality_qudit_d4_ladder.py` (exit 0, 21/21 checks)
**Closes:** honest-limit #4 of the qudit result ("d=3 only; d>=4 unchecked").

## Finding -- a latent CGLMP bug, surfaced at d=4

The CGLMP sum runs `k = 0 .. d/2 - 1`. For `d in {2, 3}` only `k = 0` fires, so
the `k >= 1` terms of `models.finality_qudit_three_walls.cglmp` were never
exercised. At d=4 the `k = 1` term fires and reveals a sign error in one
positive term: `P(B2 = A1 + k)` was coded `QAB(P12, k)`; it must be
`QAB(P12, -k)`. With the fix, `CGLMP(maximally entangled)` matches the standard
Collins-Gisin-Linden-Massar-Popescu values **exactly**:

| d | corrected | standard |
|---|---|---|
| 2 | 2.8284 | 2.8284 |
| 3 | 2.8729 | 2.8729 |
| 4 | 2.8962 | 2.8962 |
| 5 | 2.9105 | 2.9105 |

The old operator gave 2.9149 at d=4 (wrong). **The d=3 ladder result is
unaffected** (it only ever used the `k = 0` term). The corrected operator lives
in this model.

## The three walls at d=4 (isotropic line)

| wall | F | monotone | check |
|---|---|---|---|
| entanglement | 0.250 = 1/d | negativity | -- |
| shareability | 0.625 = (d+1)/2d | full symmetric-extension POCS (iters 1500) | closed form (T516) |
| CGLMP | 0.710 | corrected CGLMP-4 witness | visibility 0.6907 vs lit v_crit(4) ~ 0.6906 |

Ordered `1/d < (d+1)/2d < F_CGLMP`, distinct (gaps > 0.02), **both gaps
populated** (entangled-but-shareable and un-shareable-but-CGLMP-local isotropic
states both exist).

## Statewise sweep (I1)

55 random 4x4 states (30 generic + 25 noisy-maxent violators): 25 CGLMP-violating,
2 shareable. **I1 holds:** zero CGLMP-violating shareable states (monogamy of
nonlocality); zero CGLMP-violating separable states.

## Verdict

The three-wall ladder now holds at **d = 2, 3, 4**. The Werner/isotropic numbers
move with d (`1/d` and `(d+1)/2d` both shrink), but the structure is
dimension-independent.

## Honest limits

Shareability still via POCS (feasibility, not a dual-witness certificate; the
d=4 wall needed 1500 iterations to converge). CGLMP measurements are fixed (a
nonlocality witness: sufficient, not necessary). `d >= 5` structure unchecked
(CGLMP-d and POCS both parametrize d; the calibration already ran clean at d=5).
