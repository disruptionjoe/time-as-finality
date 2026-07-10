# T515: The Three-Wall Ladder at d=4 (and a CGLMP-d Correction)

## Target Claims

No claim-ledger target. Extends the qudit three-wall ladder result to d=4
(honest limit #4) and corrects the CGLMP-d operator.

## Setup

The ladder (`entanglement < shareability < CGLMP`) was verified at d=3. T515
extends it to d=4. Building the CGLMP-4 operator surfaced a latent bug: the
CGLMP sum runs `k = 0 .. d/2 - 1`, so for `d in {2,3}` only `k = 0` fired and
the `k >= 1` terms were never tested. At d=4 the `k = 1` term revealed a sign
error in the positive term `P(B2 = A1 + k)` (coded `QAB(P12, k)`, must be
`QAB(P12, -k)`). The corrected operator is carried here.

## Success Criteria

- Corrected `CGLMP(maxent)` matches the standard CGLMP values at d=2,3,4,5
  (2.8284, 2.8729, 2.8962, 2.9105); white noise gives 0.
- Three ordered, distinct walls at d=4: `1/d = 0.25 < (d+1)/2d = 0.625 < F_CGLMP`,
  both gaps populated. CGLMP wall visibility `~ 0.6906` (literature v_crit(4)).
- Statewise I1 holds: no CGLMP-violating shareable state; no CGLMP-violating
  separable state.

## Verdict

`THREE_WALL_LADDER_GENERALIZES_TO_D4_CGLMP_OPERATOR_CORRECTED`. The ladder holds
at d = 2, 3, 4; numbers move with d, structure is dimension-independent. The d=3
result is unaffected by the CGLMP fix (it used only `k = 0`). Model:
`models/finality_qudit_d4_ladder.py`;
tests: `tests/test_finality_qudit_d4_ladder.py`;
results: `results/T515-qudit-d4-ladder-v0.1-results.md`.
