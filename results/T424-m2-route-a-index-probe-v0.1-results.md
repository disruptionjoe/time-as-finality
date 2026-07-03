# T424 - M2 Route-A Decisive Fiber-Variation Index Probe - v0.1 results

> Recorded-tier exploratory big-swing. `TESTS.md` and `CLAIM-LEDGER.md` are
> UNTOUCHED; the T-number lives only in this header / the spec header (numbering
> automation normalizes any collision later). NO claim promotion; ledger actions
> pause for Joe. Cross-domain material (combinatorial Hodge / index theory,
> judgment aggregation, signed-graph balance theory) is the OBJECT OF STUDY, never
> evidence for physics or a sibling repo. ONE-WAY RULE holds (verified by a
> static + runtime import audit in the suite): GU / temporal-issuance /
> ai-epistemology / architecture-of-legitimacy are ADJACENCY / TEMPLATE /
> VOCABULARY only; the only code imports are TaF-native T413
> (`models.legitimacy_shapley_finality_probe`) and T423
> (`models.m2_observer_game`). Do NOT commit (per orchestrator instruction).

- Spec (frozen first): `tests/T424-m2-route-a-index-probe.md`
- Model: `models/m2_route_a_index_probe.py`
- Tests: `tests/test_m2_route_a_index_probe.py` (23 asserts, all pass, ~73 s)
- Artifact JSON: `results/T424-m2-route-a-index-probe-v0.1.json`
- Run: `python -m pytest tests/test_m2_route_a_index_probe.py -q`

## Overall verdict: REDESIGN (no GO) -- Route A escapes the relabel bar but fails the agreement bar

**The decisive question.** T423 (Route B) died at the relabel bar: its two
"independent descriptions" both reduced to one majority primitive
(`v_gap(S) == dilemma_indicator(S)` as set functions), so the same-datum agreement
was category-relative. The REDESIGN note named the only door left: a genuine
index/cohomology reading (Route A) that is **not a set-function relabel of the
majority verdict**. This probe builds three such index channels and runs the
decisive **fiber test**: is the index a function of the `v_gap` set function
(RELABEL -> Horn 2), or does it carry information beyond it, and if so does it
equal the finality separator across the whole class (Horn 1 -> GO)?

**The finding is a clean, sharpened negative.** Two of the three channels
(`I_chi`, `I_fr`) **do escape the relabel bar** -- they take different values on
profiles that share an identical `v_gap` set function, so they are provably NOT
functions of `v_gap`. This is genuinely more than Route B achieved. **But they
fail the next bar: neither equals the finality separator across the class.** The
same index value carries BOTH separator=1 and separator=0 profiles, so no
threshold recovers the separator -- *independent-of-`v_gap`-but-different-data*
(Horn 1.5). The third channel (`I_sf`, spectral flow) is **degenerate/null at
n=3**: the twisted triangle Dirac is gapless, so its spectral flow is not robustly
defined and its only profile-dependent residue merely re-reads the frustration
cocycle. So no index is a relabel-free separator, and the overall call is
**REDESIGN** -- the wall stands a third time (T422 / T423 / Route-A), now with a
precise diagnosis of *which* bar each channel hits.

| index (AND class) | escapes relabel? | equals separator across class? | Horn |
| --- | --- | --- | --- |
| **I_chi** (Euler char) | YES (non-constant on fibers) | NO (chi=1 carries sep 0 and 1) | **1.5** |
| **I_sf** (spectral flow) | -- (gapless / null at n=3) | -- (no signal) | **null** |
| **I_fr** (frustration) | YES (non-constant on fibers) | NO (fires on 18 non-dilemmas too) | **1.5** |

## The reference primitive and the fiber structure (AND class)

All `4^3 = 64` profiles enumerated; `r_i = doc(p_i,q_i)` derived, so every profile
is individually consistent by construction. Reference primitive = the `v_gap` set
function over all 8 coalitions in canonical order, hashed to a fiber key. For the
AND doctrine the class collapses to **exactly two fibers**:

| fiber (`v_gap` over coalitions) | #profiles | finality separator |
| --- | --- | --- |
| `(0,0,0,0,0,0,0,0)` (identically 0) | 58 | 0 |
| `(0,0,0,0,0,0,0,1)` = `u_N` (grand only) | 6 | 1 |

The finality separator (SURVIVES-R1 of the gap game, the T413 grand-coalition
datum) is **constant on each fiber** and equals the fiber indicator -- which is
expected, since the separator is itself computed from `v_gap`. The frozen T423
dilemma `p=(1,1,0), q=(1,0,1)` lands in the `u_N` fiber with separator 1
(re-confirmed in code). So the fiber test asks the sharp question: **do the index
channels distinguish profiles that `v_gap` itself cannot** (the 58-profile
all-zero fiber), and if so, do they distinguish them *in the direction of the
separator*?

## I_chi -- combinatorial-Hodge Euler characteristic (Horn 1.5)

Concrete chain complex: the clique complex `K(profile)` of the premise-
compatibility graph (nodes = judges; edge `{i,j}` iff i,j do NOT cross on both
premises; 2-cell iff all three edges present). Boundary maps `d0: C1->C0`,
`d1: C2->C1`; Betti numbers by EXACT integer (Fraction) rank, cross-checked by a
GF(2) rank. `I_chi = chi = b0 - b1 + b2 = |C0| - |C1| + |C2|`.

- **Exact/GF(2) consistent for all 64 profiles** (`euler_consistent` and
  `gf2_betti_match` hold everywhere).
- Value distribution `{chi=1: 52, chi=2: 12}`.
- **Escapes the relabel bar:** within the all-zero `v_gap` fiber, `I_chi` takes
  both 1 and 2. Invariance witness (deformation with `v_gap` FIXED, index MOVED):
  profile `((0,0),(0,0),(0,0)) -> chi=1` vs `((0,0),(0,0),(1,1)) -> chi=2`, both in
  the identically-0 fiber. So `I_chi` is provably NOT a function of `v_gap`.
- **Fails the separator bar:** all 6 dilemmas have `chi=1`, but `chi=1` also
  occurs on non-dilemma profiles (collision at value 1 -> carries separator 0 AND
  1). No threshold on `I_chi` recovers the separator. Independent-but-different-
  data.
- Honest n=3 limitation: on 3 nodes the clique complex has `b1 = 0` (a filled or
  forest complex), so `chi` reduces to a component/fill count; the `d1`/`b2`
  machinery and the GF(2) cross-check are exercised but no genuine 1-cycle appears
  at this witness size.

## I_sf -- spectral-flow / APS-eta channel (NULL at n=3)

Twisted Hermitian Dirac `D(theta) = [[0, B(theta)],[B(theta)^dagger, 0]]`, with
`B(theta)` the signed node-edge incidence of the judge triangle and a phase twist
`e^{i theta}` on the wrap edge. Analytically `det B(theta) = -1 + P e^{i theta}`
with `P = s01 s12 s20` the triangle sign product. This curve **passes through the
origin for every profile** (`min |eigenvalue| ~ 0` over the theta loop, verified
by `numpy eigvalsh`): the untwisted triangle Dirac is **gapless at n=3**, so the
spectral flow / APS-eta index is not robustly defined at the gapless point.

- Under a gap-opening regularization (`wrap_weight = 2`) the winding of
  `det B(theta)` becomes **profile-independent** (`= 1` for all 64 profiles;
  grid-stable under refinement) -- a degenerate/null channel with no signal.
- Exactly at the gapless point the only profile-dependent residue is `P`, which
  **equals the `I_fr` frustration cocycle class** for all 64 profiles (verified) --
  i.e. any residual spectral-flow signal is just the frustration primitive
  re-read, not an independent channel.
- Honest reading: the SSH/APS spectral-flow route needs a complex with a genuine
  gapped cycle to separate profiles; the single-cycle triangle with one wrap twist
  is gapless and null at n=3. This is itself informative -- the index-route
  "third description" is simply *unavailable* at this finite-witness size, rather
  than a relabel.

## I_fr -- signed-graph frustration index (the genuine loophole; Horn 1.5)

Edge sign `s_ij = -1` iff judges i,j cross on BOTH premises
(`p_i != p_j and q_i != q_j`) -- a pairwise cycle-product / interaction read,
NON-thresholded, NOT a marginal. Frustration = min negative-edge count over all
`2^3` gauge switches; GF(2) cross-check via the triangle sign product (cocycle
class). `gf2_matches_mingauge` holds for all 64 profiles.

- Value distribution `{0: 40, 1: 24}`.
- **Escapes the relabel bar (AND):** non-constant on the all-zero fiber.
  Invariance witness: `((0,0),(0,0),(0,0)) -> 0` vs `((0,0),(0,1),(1,0)) -> 1`,
  both in the identically-0 `v_gap` fiber.
- **The precise reason it fails the separator bar -- necessary but not
  sufficient.** Every one of the 6 genuine dilemmas is frustrated (`I_fr=1` on
  all dilemmas -> NECESSARY), but `I_fr=1` on **24** profiles total, i.e. **18
  non-dilemma profiles are also frustrated** (NOT sufficient). Frustration
  over-fires: it reads the premise-crossing interaction, which is present in many
  non-dilemma profiles, so it cannot be thresholded to the finality separator.
  This is the sharpest single result of the probe: the frustration escape valve
  reads *real* interaction structure and correctly flags every dilemma, but it is
  **not** the finality datum.
- **In the XOR control class, `I_fr` becomes a genuine RELABEL (Horn 2):** it is
  constant on every `v_gap` fiber -- there frustration IS a function of `v_gap`.
  So the "independence" of `I_fr` is doctrine-regime-specific, not intrinsic.

## Doctrine family + XOR control

| doctrine | #fibers | #separator profiles | note |
| --- | --- | --- | --- |
| AND | 2 | 6 | the only class with finality separators |
| OR | 10 | 0 | no SURVIVES-R1 (matches T423: OR ABSORBS) |
| DICT (r=p) | 1 | 0 | gap identically 0 (premise = conclusion) |
| NOCONN (r=0) | 1 | 0 | gap identically 0 |
| XOR (r=p^q) | 16 | 0 | cohomology genuinely defined; still no separator |

Only the AND class produces finality separators, so it is the decisive class; the
others are reported with the honest note that the separator-agreement question is
**vacuous** there (no separator to agree with), which the model flags explicitly
rather than scoring as a spurious GO. The XOR control confirms the machinery runs
where the coboundary/cohomology class is non-trivial, and delivers the extra
finding that `I_fr` is a relabel in that regime.

## Guard-the-guard (MANDATORY; both directions pass, all 5 doctrine classes)

- **Relabel-detector positive control.** `i_fake_relabel = sum(v_gap)` is a pure
  function of `v_gap` by construction -> the fiber test correctly reports
  **constant on every fiber** (`pass = True`). The detector fires "relabel" when
  it should.
- **Independence-detector positive control.** `i_fake_independent = distinct
  profile serial id` -> the fiber test correctly reports **non-constant** (a fiber
  with >= 2 profiles necessarily varies; `pass = True`). The detector can SEE
  independence when it exists.

Without both controls the fiber test would prove nothing; both are green in every
doctrine class, so the "constant on fibers" and "non-constant on fibers" verdicts
above are trustworthy.

## Honest ceiling (binding)

- **Finite witness + Horn verdict + controls, NOT a universal theorem.** n=3, 64
  profiles per doctrine, 5 doctrines, fully enumerated. Exact arithmetic
  (integer / `Fraction` / GF(2)) everywhere except `I_sf` (numpy float, with a
  grid-refinement determinism cross-check that is green for all profiles).
- **What Route A genuinely adds over Route B:** `I_chi` and `I_fr` are provably
  NOT functions of `v_gap` (exhibited invariance witnesses inside a single fiber).
  Route A therefore *escapes the relabel/linearity bar* that killed Route B. That
  is a real, positive structural fact.
- **Why it is still no GO:** escaping the relabel bar is necessary, not
  sufficient. To be the CANONICAL finality datum the index must also EQUAL the
  separator across the class; none does. `I_fr` is necessary-but-not-sufficient
  (fires on 18 non-dilemmas), `I_chi` collides at `chi=1`, `I_sf` is null. So the
  index channels read *some* real interaction structure but not *the* finality
  datum -- a different, sharper wall than Route B's, but a wall.
- **n=3 caps two channels.** `I_chi` has `b1=0` on the triangle (no genuine
  1-cycle); `I_sf` is gapless/null. A larger complex (more independent cycles)
  would be needed for either to be a bona fide separating channel -- explicitly
  out of scope for this finite-witness probe and flagged, not hidden.
- Cross-domain (index theory, judgment aggregation, signed graphs) is the object
  of study, never evidence. No claim promotion; no ledger / TESTS.md edit; not
  committed; pauses for Joe.

## What this earns / does not earn

**Earns (recorded, synthesis tier, method not evidence):** a finite, fully
enumerated, mostly-exact decisive test of the Route-A escape hypothesis, with (a)
a genuine demonstration that combinatorial-Hodge and signed-graph-frustration
indices ESCAPE the relabel bar (not functions of `v_gap`), (b) a precise
diagnosis that they nonetheless FAIL the separator-agreement bar
(frustration = necessary-but-not-sufficient; Euler char collides; spectral flow
null/gapless at n=3), and (c) a validated relabel/independence detector
(guard-the-guard green both directions). This unifies T422 (category-relativity),
T423 (Route-B relabel), and Route-A into one finding: **the finality datum is
finite-witnessed but not canonically computed by any of the three index channels
at n=3.**

**Does not earn:** any canonical/category-free computation of the finality datum
(REDESIGN -- no index equals the separator across the class); any universal
theorem; any claim promotion; any cross-repo evidential use; any physics or
governance claim. The frustration escape valve is real interaction structure but
NOT the finality separator. Pauses for Joe.
