# T514 Results -- CCNR / realignment bound-entanglement witness

**Verdict:** `CCNR_WITNESS_VERIFIED_OUTER_WALL_UPGRADED`
**Model:** `models/finality_ccnr_bound_entanglement_witness.py` (exit 0, 7/7 checks)
**Closes:** honest-limit #2 of `explorations/qudit-three-wall-ladder-result-2026-07-09.md`.

## Objective

The qudit three-wall ladder's outer wall was "NPT-entangled" (negativity > 0),
not "entangled": for `d > 2`, negativity misses PPT bound entanglement. T514
adds the computable cross-norm / realignment (CCNR) criterion -- a genuine
bound-entanglement witness independent of the PPT test -- and certifies it
against a known bound-entangled state.

CCNR: for the realignment `R(rho)[(a a'),(b b')] = rho[(a b),(a' b')]`, every
separable state has `||R(rho)||_1 <= 1`. Hence `||R(rho)||_1 > 1 => entangled`.
Sufficient, not necessary.

## Calibration gates (all pass)

| state | negativity | CCNR | reading |
|---|---|---|---|
| separable product | 0 | 0.4181 | `<= 1` (correct) |
| isotropic `F = 1/d` (sep point) | ~0 | 1.000000 | exactly on the CCNR boundary |
| isotropic `F = 0.9` (NPT-ent) | 0.8500 | 2.7000 | `> 1`, agrees with negativity |

## Payoff -- a PPT state negativity cannot see

The Tiles UPB bound-entangled state (Bennett et al., 3x3):

- negativity `= 1.67e-16` (PPT -- invisible to the old outer wall),
- **CCNR `= 1.0874 > 1`** -- caught by the upgraded wall.

## Effect on the ladder

On the isotropic family `PPT <=> separable`, so CCNR and negativity give the
**same** entanglement wall at `F = 1/d`. The qudit ladder result is unchanged on
the isotropic line; the upgrade only adds detection of bound entanglement **off**
that line.

## Honest limits

CCNR is sufficient, not necessary -- PPT-entangled states it misses may remain.
No claim-ledger movement; this consolidates the qudit ladder's outer wall.
