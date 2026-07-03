# T423 - M2 Observer-Game / Judgment-Aggregation Finality Probe (Route B) - spec (frozen)

> Recorded-tier exploratory big-swing. `TESTS.md` and `CLAIM-LEDGER.md` are
> UNTOUCHED; the T-number lives only in this header / the results header (the
> numbering automation normalizes any collision later). NO claim promotion;
> ledger actions pause for Joe. Cross-domain material (social choice, judgment
> aggregation, cooperative game theory) is the OBJECT OF STUDY, never evidence
> for physics or a sibling repo. ONE-WAY RULE (strict): GU / temporal-issuance /
> ai-epistemology / architecture-of-legitimacy are ADJACENCY, TEMPLATE, and
> VOCABULARY only -- never cited as EVIDENCE. The only code import is TaF-native
> T413 (`models.legitimacy_shapley_finality_probe`).

- Model: `models/m2_observer_game.py`
- Tests: `tests/test_m2_observer_game.py`
- Results: `results/T423-m2-observer-game-v0.1-results.md`
- Run: `python -m pytest tests/test_m2_observer_game.py -q`

## Object (frozen before the model existed)

Judges N = {1,2,3}; agenda propositions p, q, r with doctrine r <-> (p AND q).
Frozen profile (the classic n=3 doctrinal paradox):

| judge | p | q | r = p&q |
| --- | --- | --- | --- |
| 1 | 1 | 1 | 1 |
| 2 | 1 | 0 | 0 |
| 3 | 0 | 1 | 0 |

`smaj(col, S)` = strict majority over S, tie -> reject. Premise-based verdict
`P(S) = smaj(p,S) & smaj(q,S)`; conclusion-based `C(S) = smaj(r,S)`; gap game
`v_gap(S) = P(S) - C(S)`; dilemma indicator `1[P!=C]`. Route A (game) reads the
coalition lattice; Route B (logic) reads the proposition lattice. They must not
share code.

## Predeclared success legs (GO only if S1-S3 clean AND S4 reported with its
## honest demotion intact)

- **S1 GENUINE DILEMMA (K2 guard).** Every individual judgment is consistent
  (`r_i = p_i & q_i` verified in code) yet the collective majority set is
  inconsistent: maj-p & maj-q ACCEPT r while maj-r REJECTS. Not a tie artifact
  (p and q each carry a strict 2/3 majority).
- **S2 GLOBAL-NO-LOCAL.** `v_gap = u_N` exactly (0 on all 7 proper coalitions,
  1 on N; single grand dividend). `dilemma_indicator = 0` on every proper
  subset, `= 1` only on N. `joint_record_completion_verdict(v_gap, 0)` returns
  SURVIVES-R1 (`datum_in_proper_subset = False`).
- **S3 AUMANN-SHAPLEY IS THE SEPARATOR.** `shapley_by_dividends ==
  shapley_by_permutations = (1/3,1/3,1/3)`; `d(N) = 1` IS T413 Pair-2's
  grand-coalition SURVIVES-R1 datum (tie to the existing datum, not a fresh
  number). k-replication trend: Delta = v_gap(N) = 1 preserved while individual
  shares dilute.
- **S4 CANONICITY, HONESTLY SCOPED (not a clean win).** (a) localization
  agreement: gap-dividend support = {N} AND independent agenda obstruction
  omega = 1 = d(N), with the explicit log that on consistent judges
  `v_gap == dilemma_indicator` (shared primitive -> K1-partial, does NOT alone
  escape T422); (b) the obstruction co-varies with the SURVIVES-R1 separator
  across the doctrine family {AND->1, OR->0, DICT->0, NOCONN->0} without
  re-tuning; (c) magnitude teeth: premise game `d(N) = 2 != 1` and
  `phi = (2/3,1/6,1/6) != (1/3,1/3,1/3)` -> the two readings are NOT identical
  by construction.
- **S5 FALSIFIERS STATED AND BEHAVE.** consistency-relaxation decouples the two
  routes (agreement is regime-specific, not an identity); a proper subset
  reconstructing the dilemma would kill global-no-local (does not trigger);
  doctrine-family disagreement would kill co-variation (does not trigger).

## Predeclared kill / demotion legs

- **K1 T422 RECURRENCE (the live risk).** If the only surviving agreement is the
  shared-primitive localization (gap game = dilemma indicator = same set
  function) and neither the co-variation nor the magnitude leg adds independent
  signal -> clean canonicity NOT achieved -> DEMOTE to a logged disanalogy at
  synthesis tier. Follows from T413 Leg 8 (Shapley linear in v => exact
  agreement <=> same game).
- **K2 ENGINEERED/TRIVIAL DILEMMA.** Any individual judgment inconsistent, or
  the paradox is a tie-rule artifact -> REDESIGN.
- **K3 VALUE NOT THE SEPARATOR.** `v_gap`'s d(N) not grand-concentrated (a proper
  subset absorbs it; joint_record_completion returns ABSORBED) -> REDESIGN.
- **K4 DIFFERENT DATA UNDER SAME IDENTIFICATION.** Two descriptions claimed equal
  compute different numbers -> ABANDON that leg to a logged disanalogy.
- **K5 SIBLING LOAD-BEARING.** Any ai-epistemology / TI / GU result used as
  support -> one-way violation -> rebuild import-free.
- **K6 PRIOR ART.** If the literature already states "(Aumann-)Shapley value = a
  judgment-aggregation obstruction" of this kind -> CITE; novelty demotes to the
  finality cross-application at synthesis tier.

## Honest ceiling (binding)

Finite witness (n=3) + doctrine family + small replication + a DEMOTING
canonicity argument + a definite falsifier. NOT a universal theorem. The
predeclared honest verdict is a DEMOTION: a genuine finality <-> List-Pettit
cross-application at synthesis tier plus a falsifiable magnitude-decoupling
disanalogy -- not the clean triple-coincidence canonicity M2 hoped for.
