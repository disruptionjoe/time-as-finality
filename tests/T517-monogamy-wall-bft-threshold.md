# T517: Monogamy Wall vs the BFT 2/3 Threshold (Falsification Check)

## Target Claims

No claim-ledger target. Resolves prospecting corner 4 of
`explorations/lane-status-and-adjacent-space-prospecting-2026-07-09.md`
("worth one check"). Preserved as a labeled negative result.

## Setup

The qubit 2-shareability wall is `2/3` (in visibility) and classical Byzantine
fault tolerance needs `> 2/3` honest nodes. Is this a shared monogamy structure
or a parametrization coincidence? Using the certified closed form (T516)
`F_share(d) = (d+1)/2d`, `v_share(d) = (d+2)/(2(d+1))`, we confront the
structural hypothesis.

## Success Criteria (falsification)

- Datum for: `v_share(2) = 2/3` exactly.
- Data against: the wall drifts (`v_share(d) -> 1/2`) while BFT `2/3` is
  d-independent; the qutrit wall is `5/8` not `2/3`; the coincidence moves to a
  different d under the fidelity parametrization; and the two `2/3`'s are
  functions of different variables (local dimension at fixed 2 shares vs party
  count `n > 3f`).
- Independent POCS confirms the walls used are real at d = 2, 3, 4.

## Verdict

`SHUT` as stated: the monogamy-wall <-> BFT-2/3 correspondence is falsified as a
structural correspondence and kept as a d=2 parametrization coincidence. The
genuine monogamy <-> access-structure (secret-sharing) bridge is untouched.
Model: `models/finality_monogamy_wall_bft_threshold.py`;
tests: `tests/test_finality_monogamy_wall_bft_threshold.py`;
results: `results/T517-monogamy-wall-bft-threshold-v0.1-results.md`.
