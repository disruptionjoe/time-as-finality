# T424 - M2 Route-A Decisive Fiber-Variation Index Probe - spec (frozen)

> Recorded-tier exploratory big-swing. `TESTS.md` and `CLAIM-LEDGER.md` are
> UNTOUCHED; the T-number lives only in this header / the results header (the
> numbering automation normalizes any collision later). NO claim promotion;
> ledger actions pause for Joe. Cross-domain material (combinatorial Hodge
> theory / index theory, judgment aggregation, signed graphs / balance theory)
> is the OBJECT OF STUDY, never evidence for physics or a sibling repo.
> ONE-WAY RULE (strict): GU / temporal-issuance / ai-epistemology /
> architecture-of-legitimacy are ADJACENCY, TEMPLATE, and VOCABULARY only --
> never cited as EVIDENCE. The only code imports are TaF-native: T413
> (`models.legitimacy_shapley_finality_probe`) and T423
> (`models.m2_observer_game`). A static + runtime import audit is part of the
> test suite.

- Model: `models/m2_route_a_index_probe.py`
- Tests: `tests/test_m2_route_a_index_probe.py`
- Results: `results/T424-m2-route-a-index-probe-v0.1-results.md`
- Run: `python -m pytest tests/test_m2_route_a_index_probe.py -q`

## The question this test settles

T423 (Route B) hit a REDESIGN: the two "independent descriptions" of the finality
datum (coalition-lattice Shapley `d(N)` and proposition-lattice MI-set `omega`)
both reduced to the SAME majority primitive -- `v_gap(S) == dilemma_indicator(S)`
as set functions over all 8 coalitions -- so the same-datum agreement was
category-relative (T422's ceiling recurred). The REDESIGN note names the only
door left open: a **second description that does NOT reduce to the coalition-
majority primitive** -- a genuine index/cohomology reading (Route A) that is not a
set-function relabel of the majority verdict.

This probe is the **decisive fiber-variation test** of whether Route A escapes the
relabel bar. It is a finite-witness demonstration + a Horn verdict + guard-the-
guard controls, NOT a universal theorem.

## Object (frozen before the model existed)

Judges N = {1,2,3}; agenda propositions p, q, r; doctrine `r_i = doc(p_i, q_i)`.
Profiles are all `4^3 = 64` assignments of `(p_i, q_i) in {0,1}^2` per judge, with
`r_i` DERIVED from the doctrine -- so every enumerated profile is individually
CONSISTENT by construction. Doctrine family `{AND, OR, DICT(r=p), NOCONN(r=0)}`
plus an `XOR(r = p^q)` control (XOR makes the coboundary/cohomology class
genuinely non-trivial). `smaj`, `premise_verdict`, `conclusion_verdict`,
`gap_value` are reused verbatim from T423 (the majority/verdict logic).

## Reference primitive (the fiber label)

For each profile, `v_gap(S) = premise_verdict(S) - conclusion_verdict(S) in
{-1,0,1}` over all 8 coalitions S, in a fixed canonical coalition order, is
hashed to a **fiber key**. This is the "relabel primitive." Two profiles are in
the same fiber iff they induce the identical `v_gap` set function. The finality
separator per profile is `1` iff the gap game's Mobius dividends give
`joint_record_completion_verdict = SURVIVES-R1` (the T413 grand-coalition datum),
else `0`.

## Candidate indices (three independent channels, each a function of the profile)

- **I_chi -- combinatorial-Hodge Euler characteristic.** Concrete chain complex:
  the clique complex `K(profile)` of the premise-compatibility graph (nodes =
  judges; edge `{i,j}` iff i,j do NOT cross on both premises; 2-cell `{1,2,3}` iff
  all three edges present). Boundary maps `d0: C1->C0`, `d1: C2->C1`. Betti
  numbers via EXACT integer matrix rank, cross-checked with a GF(2) rank.
  `I_chi = chi = b0 - b1 + b2 = |C0| - |C1| + |C2|` (alternating sum).
- **I_sf -- spectral flow (SSH / APS-eta channel).** Twisted Hermitian Dirac
  `D(theta) = [[0, B(theta)], [B(theta)^dagger, 0]]` where `B(theta)` is the signed
  node-edge incidence of the judge triangle with a phase twist `e^{i theta}` on a
  designated wrap edge. `I_sf` = signed count of zero-crossings of the branch
  nearest zero as `theta: 0 -> 2pi` (numpy `eigvalsh`), determinism cross-checked
  under grid refinement.
- **I_fr -- signed-graph FRUSTRATION index (the genuine loophole).** Edge sign
  `s_ij = -1` iff judges i,j cross on BOTH premises (`p_i != p_j and q_i != q_j`),
  else `+1` -- a pairwise CYCLE-PRODUCT / interaction of the votes, NON-thresholded
  and NOT a marginal. `I_fr` = min negative-edge count over all `2^3` gauge
  switches; cross-checked with the GF(2) coboundary/cocycle class (triangle sign
  product).

## Predeclared test structure

1. **Fiber test (per index).** Is `I` constant on every fiber of `v_gap`?
   - CONSTANT => `I = f(v_gap)` => RELABEL => **Horn 2** (index-side linearity
     lemma fires; the channel is the majority primitive read again).
   - NON-CONSTANT => independent channel => go to step 2.
2. **Separator-agreement (only for non-constant indices).** Across the ENTIRE
   dilemma class (all 64 profiles) and under the doctrine family, does `I` (under a
   fixed threshold) equal the finality separator for EVERY profile?
   - Independent AND structural-agree AND an invariance-witness (a deformation
     moving `v_gap` while `I` fixed, or `I` while `v_gap` fixed) => **Horn 1 / GO**.
   - Independent but disagrees off-fixture (some `I`-value carries both
     separator=1 and separator=0 profiles) => different data => still **no GO**.
3. **Guard-the-guard (mandatory, both directions).**
   - `I_fake_relabel` = a pure function of `v_gap` by construction -> MUST test
     "constant on fibers" (relabel-detector POSITIVE control).
   - `I_fake_independent` = the distinct profile serial id -> MUST test
     "non-constant" (detector can SEE independence). Without both, the test proves
     nothing.

## Verdicts

- **GO** -- a genuine independent index equals the separator across the class,
  with an invariance witness (the frustration escape valve is real).
- **REDESIGN / ABANDON** -- all indices are relabels (Horn 2) OR
  independent-but-different-data (agree only on the fixture) -- confirming the
  unified index-side lemma and the "same wall three times" finding (T422 / T423 /
  Route-A).

## Honest ceiling (binding)

Finite witness (n=3, 64 profiles per doctrine fully enumerated) + the Horn verdict
+ guard-the-guard controls. Exact arithmetic (integer / `Fraction` / GF(2))
everywhere except `I_sf`, which is `numpy` float with a refinement determinism
cross-check. NOT a universal theorem. Cross-domain (index theory, judgment
aggregation, signed graphs) is the object of study, never evidence. No claim
promotion; pauses for Joe.
