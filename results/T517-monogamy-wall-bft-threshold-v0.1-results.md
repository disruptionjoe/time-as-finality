# T517 Results -- monogamy wall vs the BFT 2/3 threshold (a falsification check)

**Verdict:** `SHUT_AS_STATED` -- the monogamy-wall <-> BFT-2/3 correspondence is
falsified as a *structural* correspondence and preserved as a labeled coincidence.
**Model:** `models/finality_monogamy_wall_bft_threshold.py` (exit 0, 14/14 checks)
**Resolves:** prospecting corner 4 of
`explorations/lane-status-and-adjacent-space-prospecting-2026-07-09.md` ("worth one check").

## The hypothesis, made precise

`H(structural)`: the isotropic 2-shareability wall equals the Byzantine
fault-tolerance honest-fraction threshold `2/3` because monogamy of entanglement
*is* the structural cause of fault-tolerance bounds. If so, the wall should track
the BFT constant across regimes, not drift.

Using the certified closed form (T516): `F_share(d) = (d+1)/2d`, visibility form
`v_share(d) = (d+2)/(2(d+1))`.

## Datum FOR (why it was worth a check)

`v_share(2) = 4/6 = 2/3` exactly, and classical BFT needs `> 2/3` honest nodes.
At d=2, in the visibility parametrization, the numbers coincide.

## Data AGAINST a structural correspondence (decisive)

1. **The wall drifts, BFT does not.** `v_share(d) = (d+2)/(2(d+1))` decreases
   monotonically to `1/2` as `d -> inf`; the BFT threshold stays pinned at `2/3`.
   | d | 2 | 3 | 4 | 5 | 6 | ... | inf |
   |---|---|---|---|---|---|---|---|
   | v_share | 0.667 | 0.625 | 0.600 | 0.583 | 0.571 | ... | 0.500 |
2. **The qutrit wall is `5/8`, not `2/3`** (matches the note's datum).
3. **Parametrization-dependent.** The coincidence lands at d=2 in visibility, but
   at **d=3** in fidelity (`F_share(3) = 2/3`). A shared structure would not move
   the coincidence between parametrizations -- a coincidence signature.
4. **Axis mismatch (the structural kill).** 2-shareability fixes the number of
   shares at 2 and varies the *local dimension d*; BFT fixes the local structure
   and varies the *party count n* (`n > 3f`). The two `2/3`'s are values of
   functions of different variables.

Independent POCS confirms the walls used are real (shareable just below, un-
shareable just above `(d+1)/2d` at d = 2, 3, 4).

## Verdict

`SHUT` as precisely worded: no shared monogamy structure between the shareability
wall and the BFT threshold is earned. Preserved as a labeled negative result. The
genuine monogamy <-> access-structure (secret-sharing) bridge -- the strut that
survived earlier stress tests -- is untouched by this.
