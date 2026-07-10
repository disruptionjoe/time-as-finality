# T514: CCNR / Realignment Bound-Entanglement Witness

## Target Claims

No claim-ledger target. Consolidates the outer wall of the qudit three-wall
ladder (`explorations/qudit-three-wall-ladder-result-2026-07-09.md`, honest
limit #2).

## Setup

For `d > 2`, negativity (NPT) misses PPT bound entanglement, so the ladder's
outer wall was only "NPT-entangled." T514 adds the computable cross-norm /
realignment (CCNR) criterion: with `R(rho)[(a a'),(b b')] = rho[(a b),(a' b')]`,
every separable state has `||R(rho)||_1 <= 1`, so `||R(rho)||_1 > 1 => entangled`
(sufficient, not necessary; independent of PPT).

## Success Criteria

- Separable product state: `CCNR <= 1`.
- Isotropic separability point `F = 1/d`: `CCNR = 1` (boundary).
- NPT-entangled isotropic `F = 0.9`: `CCNR > 1`, agreeing with negativity.
- Tiles UPB bound-entangled state: `negativity ~ 0` but `CCNR > 1` (the payoff).
- On the isotropic line, CCNR and negativity give the same wall (`F = 1/d`), so
  the ladder result is unchanged there.

## Verdict

`CCNR_WITNESS_VERIFIED_OUTER_WALL_UPGRADED`. CCNR passes all gates and detects
the Tiles PPT bound-entangled state (negativity `1.67e-16`, CCNR `1.0874`). The
outer wall is now "entangled" (NPT OR CCNR), closing honest-limit #2. Model:
`models/finality_ccnr_bound_entanglement_witness.py`;
tests: `tests/test_finality_ccnr_bound_entanglement_witness.py`;
results: `results/T514-ccnr-bound-entanglement-witness-v0.1-results.md`.
