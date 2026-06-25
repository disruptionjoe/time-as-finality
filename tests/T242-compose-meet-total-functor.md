# T242: Is `compose_meet` a legality-closed TOTAL filtered composition, and is `gr` then a TOTAL functor?

**Status:** implemented — finite-witness model + pytest green (`18 passed`; `63 passed` with the T232/T228/T237 siblings — import-only contract, no sibling breakage)
**Builds on:** [T237](T237-d1filtered-graded-functor.md) (`gr` is a STRICT functor only on the gr-composable / filtration-NESTED subcategory; first exact obstruction = `compose_filtered` is **not legality-closed** on non-nested legal morphisms), via [T232](T232-d1cat-filtered-colimit.md) (`D1FilteredMorphism`, `compose_filtered`, `associated_graded`) and [T228](T228-d1cat-transfinite-colimit-decision.md) (binding cocompleteness honesty guard).
**Resolves (the named repair):** T237's *Constructive next object (1)* verbatim — *"Legality-closed filtered composition `compose_meet`: replace `_refine_filtrations`' size-sort with the SUBSET-LATTICE MEET-CLOSURE of the two descending chains … Decide whether `compose_meet` is associative with identities (making `D1FilteredCat_meet` a proper TOTAL category) and whether `gr` is then a TOTAL (strict or lax) functor on it."*
**Model:** [`models/d1filtered_compose_meet.py`](../models/d1filtered_compose_meet.py)
**Tests:** [`tests/test_d1filtered_compose_meet.py`](test_d1filtered_compose_meet.py)
**Results:** [`results/d1filtered-compose-meet/T242-results.json`](../results/d1filtered-compose-meet/T242-results.json)
**Tags:** `finite_witness` (executable fixture over the fixed 4-element dimension universe `D1_DIMENSIONS = (a,h,b,r)`; no continuum/scalable theorem asserted) · `poly_decider` (finite meet-closure + greedy descending filter; not a hidden search, not a hardness/NP claim)

---

## Verdict

**conditional.** *T237's named repair SUCCEEDS — a proper **total category** with **total** `gr` IS reachable — but ONLY by a **codomain change**, and `gr` then becomes **genuinely lax**, not strict. The decisive structural fact this lane found: the **pairwise-meet-closure of two descending CHAINS is in general NOT a chain** — it is a meet-semilattice containing an **antichain** (for the T237 witness, `{a,h,b}` and `{h,r}` are incomparable). Consequently:*

| Sub-question (T237's (a)/(b)) | Verdict |
| --- | --- |
| (a-i) Chain-valued `compose_meet` — force a single descending chain out of the meet-closure. Legal? | **closed (yes).** `compose_meet_chain` is **always set-descending by construction**, so always legal — including on the exact witness that makes `compose_filtered` illegal. The size-sort obstruction is gone. |
| (a-ii) …is that chain-valued composition **associative** (a category of filtrations)? | **no-go.** **NOT associative.** Forcing a chain out of an antichain-containing semilattice is **bracketing-dependent**: `(f;g);h` and `f;(g;h)` collapse the size-1 antichain `{a}` vs `{h}` in different orders → `left_filtration != right_filtration` (both legal). A chain-valued total category of filtrations does **not** exist. |
| (a-iii) Semilattice-valued `compose_meet` — keep the full meet-closure as a graded meet-semilattice. Total category? | **closed (yes), at the cost of a CODOMAIN CHANGE.** `compose_meet_semilattice` is **associative** (meet-closure is bracketing-independent), **unital**, **always legal**, and **extends `compose_filtered`** on the nested subcategory (a nested composite is already a chain = its own meet-closure). So `D1FilteredCat_meet` is a proper **total** category — but its morphism data is a meet-**semilattice** of preserved-dimension sets, **not** a chain (filtration). |
| (b) Is `gr` then a TOTAL functor on `D1FilteredCat_meet` — strict or genuinely lax? | **closed: TOTAL, genuinely LAX.** Identity preserved; **strict** on nested pairs (where the composite is still a chain — recovers T237 exactly); on the **newly-legal non-nested** pairs the strata form an **antichain-containing poset** while T237's schedule `mu` returns a chain, so the comparison `gr(f;g) → mu(gr f, gr g)` **exists** (same dropped support + same floor) but is **NOT strict**. Totality **forces** laxity. |
| Does this establish general cocompleteness at infinity? | **no (open).** Finite-category totality only; non-monotone filtrations still rejected; cocompleteness named **still open** (binding T228 guard). |

**Net:** T237's obstruction (`compose_filtered` not legality-closed) is **diagnosed at the root**: it is not a defect of the *size-sort* but a structural feature — the meet-closure of two chains is a semilattice with an antichain, and **no** legality-closed chain-valued composition can be associative. A total category exists only after **changing the codomain from chains to meet-semilattices**, on which `gr` is total and **genuinely lax**. The verdict is `conditional`, not `closed`, because totality is conditioned on the codomain change and the functor degrades to lax.

## What was derived from the read-first sources (IMPORT ONLY)

- **From `models/d1cat_filtered_colimit.py` (T232), imported, never modified:** `D1FilteredMorphism`, `Filtration`, `compose_filtered`, `filtration_is_legal`, `filtered_equal`, `make_filtered_identity`, `bare_intersection`, `_normalize_layer`, `_compose_site_maps`, `_one_site_system`. `compose_filtered` is invoked as the live operation it provides; its illegality on the non-nested witness is what T242 repairs.
- **From `models/d1filtered_graded_functor.py` (T237), imported, never modified:** `gr` (= `associated_graded`), **`mu` (schedule semantics — the NON-CIRCULAR reference)**, `graded_comparison`, `graded_dropped`, `graded_bottom`, `graded_support`. `mu` is the independent yardstick for strict-vs-lax; it is **never** re-derived from any compose code in this file.
- **The decisive new structural fact this lane surfaced:** `meet_closure_set(a,b)` of two descending chains is a meet-semilattice that, for non-nested inputs, **contains an antichain** (`meet_closure_has_antichain == True`). Since a filtration is a chain, this is the exact reason a legality-closed *chain-valued* composition cannot be associative — latent in T237's obstruction, not isolated there.

## Strongest positive result

**Five executable facts decide the two rungs (all from `results/d1filtered-compose-meet/T242-results.json`).**

1. **Chain variant is legal but non-associative (no-go).** On the T237 witness `f: 4 ⊇ {a,h,b}`, `g: 4 ⊇ {h,r}`: `compose_filtered(f,g).is_legal() == False` (the original obstruction) while `compose_meet_chain(f,g).is_legal() == True` and is descending. But `(f;g);h ≠ f;(g;h)` for `h: 2 ⊇ 1` — `left_filtration` ends `… {a,h}, {a}, {}` vs `right` `… {a,h}, {h}, {}`, both legal, unequal (`chain_variant_non_associative == True`). The nested control triple stays associative.

2. **The structural cause is an antichain.** `meet_closure_has_antichain(f,g) == True`; the closure contains `{a,h,b}` and `{h,r}` with neither `⊆` the other.

3. **Semilattice variant is a total category.** `compose_meet_semilattice` is **associative across every triple including all non-nested ones** (`all_associative == True`), satisfies left/right **identity laws** (`both == True`), is **legal on the breaking witness** (composite is a genuine poset, `composite_has_antichain == True`), and **extends `compose_filtered` on nested pairs** (`all_agree_on_nested == True`, and each such composite is itself a chain).

4. **`gr` is a TOTAL functor, strict-on-nested / lax-on-non-nested.** `nested_strict == True` (recovers T237's strict result where the composite is still a chain); on newly-legal non-nested pairs `non_nested_comparison_exists == True` and `non_nested_strict == False` with `non_nested_any_antichain == True` → `totality_forces_lax == True`. Identity preserved (`identity_law_holds == True`). On the chain case `gr_semilattice(F;G) == gr(compose_filtered(f,g))` exactly.

5. **The comparison datum holds.** For the witness, `gr_semilattice(f;g)` and `mu(gr f, gr g)` drop the **same** dimensions `{a, b, r}` and share the **same** floor `{h}`; together they recover the full universe (`drops ∪ floor == D1_DIMENSIONS`). So the lax comparison morphism exists; only the *grouping* (poset vs chain) differs.

## Honesty guards (explicitly listed; none triggered)

- **`mu` is NOT a copy of the compose code (non-circular).** `mu` is imported from T237 (schedule semantics) and yields a **chain**; the semilattice composite yields an **antichain-containing poset**. They agree on dropped-support + floor but **differ in structure** (`structures_differ == True`). This divergence is impossible if `mu` had copied `compose_meet` — so strictness/laxity is judged against an independent yardstick. *Confirmed:* `test_mu_is_not_a_copy_of_compose_code`.
- **Legality on the breaking witness.** Both `compose_meet` variants are asserted legal on the **exact** witness that makes `compose_filtered` illegal. *Confirmed:* `test_chain_variant_legal_where_compose_filtered_is_not`, `test_semilattice_legal_on_breaking_witness`.
- **The no-go is a real counterexample, not a fiat.** Non-associativity is exhibited with an explicit unequal-but-both-legal bracketing pair. *Confirmed:* `test_chain_variant_explicit_bracketing_counterexample`.
- **No over-reading as cocompleteness at infinity (binding T228 guard).** Non-monotone pseudo-filtration is rejected by `gr`; totality is asserted **only** for the fixed finite category; cocompleteness named still open. *Confirmed:* `test_honesty_boundary_non_monotone_rejected`, `test_non_monotone_filtration_is_illegal_directly`.
- **`gr_semilattice` is a real total assignment, not `gr` re-tuned per pair.** It is computed once from the Hasse-cover differences of the semilattice and coincides with T237's `associated_graded` on every chain. *Confirmed:* `test_gr_semilattice_on_chain_coincides_with_associated_graded`.

## First exact obstruction / missing object

**The codomain "filtrations (descending chains)" is not closed under any associative legality-closed composition.** The meet-closure of two chains has an antichain (`{a,h,b} ∦ {h,r}`); a filtration is a chain; any deterministic chain-extraction from a semilattice-with-antichain (the running-meet over a fixed total order) is **bracketing-dependent**, hence non-associative. So the *missing object* is not "a smarter chain composition" — that provably cannot exist — but a **codomain change**: morphism data must be a graded **meet-semilattice**, on which composition is the meet-closure (associative) and `gr` is total but **lax**. That object IS built here (`D1MeetSemilatticeMorphism`, `compose_meet_semilattice`, `gr_semilattice`); what is **not** resolved is whether the lax comparison cells assemble into a **coherent lax functor / pseudofunctor** (the coherence pentagon over triples), which the current battery checks only object-wise.

## Constructive next object (named, not built)

1. **Lax-functor coherence for `gr` on `D1FilteredCat_meet`:** verify the comparison 2-cells `gr(f;g) → mu(gr f, gr g)` satisfy the lax-functor associativity coherence (the schedule-pentagon) over composable **triples**, upgrading "object-wise lax" to a genuine **lax functor** (or pseudofunctor if the cells are invertible). The semilattice associativity proven here is the prerequisite.
2. **The forgetful section `J ⊣ U`:** the chain-embedding `J: D1FilteredCat → D1FilteredCat_meet` (`_from_chain`) and the bottom-stratum forgetful map; decide whether `J` is a (non-full) inclusion of the gr-composable subcategory and whether `bottom ∘ gr_semilattice` recovers T232's bare-intersection forgetful `U: D1FilteredCat → D1Cat` as a sub-functor.

Both are **discrete category-level** objects, **explicitly distinct** from the continuum coefficient-sheaf-H1 cofinality lanes (T236/T241); they touch no κ / sheaf / MTI / attribution file.

## Meaning for the relevant claim (report at test level; promotion deferred to integrator)

- **D1Cat / D1FilteredCat (proto_independent row):** T237's `conditional` strict-on-nested functor is **undisturbed and explained**. Its first obstruction (`compose_filtered` not legality-closed) is now **diagnosed at the root**: it is structural (antichain in the meet-closure), not a fixable defect of the size-sort. The honest net: a **total category IS reachable**, but it requires **changing the morphism codomain from chains to meet-semilattices**, and on that category `gr` is **total but genuinely lax** (strict exactly on the old gr-composable / chain subcategory). Within the original filtration codomain, legality-closed composition is a **no-go** (legal-but-non-associative). General cocompleteness at infinity remains **open, untouched**.
- **No over-promotion:** no physics/geometry/curvature/new-object/Čech/sheaf language. "filtration / associated-graded / meet-semilattice / functor / lax" name finite operations on subsets of a fixed 4-element set. This is the **discrete** lane, distinct from the κ / sheaf-H1 / MTI files, none of which it touches.

## Failure conditions for this verdict (and confirmation none triggered)

- **The chain variant turns out associative** (so a chain-valued total category exists). *Checked false:* `test_chain_variant_is_non_associative_NO_GO`, `test_chain_variant_explicit_bracketing_counterexample` — explicit unequal bracketings.
- **The meet-closure of the witness is actually a chain** (no antichain → no obstruction). *Checked false:* `test_meet_closure_of_breaking_witness_has_antichain`.
- **The semilattice composition fails associativity / units / nested-extension** (so `D1FilteredCat_meet` is not a category). *Checked false:* `test_semilattice_is_associative_on_non_nested_triples`, `test_semilattice_identity_laws`, `test_semilattice_extends_filtered_on_nested`.
- **`gr` is strict on the non-nested pairs** (so totality did NOT force laxity / no real codomain cost). *Checked false:* `test_gr_total_strict_on_nested_lax_on_non_nested` — `non_nested_strict == False`, `totality_forces_lax == True`.
- **`mu` was secretly a copy of the compose code** (strictness/laxity circular). *Guarded:* `test_mu_is_not_a_copy_of_compose_code` — structures differ (poset vs chain) while support/floor agree.
- **A cocompleteness-at-infinity / non-monotone claim is read into this.** *Guarded:* non-monotone rejected; totality scoped to the finite category; cocompleteness named open.

## Known Physics Constraints

None. T242 is a pure category-theoretic decision about whether one finite legality-closed composition forms a category and whether one finite associated-graded assignment is a functor on it. No hardness/scale claim (finite meet-closure over a 4-element universe; per COMPLEXITY-LEDGER the engines are `poly_decider` / `finite_witness`). No physics/geometry/curvature/new-object vocabulary promoted. Distinct from the continuum coefficient-sheaf-H1 cofinality lanes (T236/T241); touches no κ / sheaf / MTI files.

## Reproduction

```
cd "<repo root>"
python -m pytest tests/test_d1filtered_compose_meet.py -q          # 18 passed
python -m pytest tests/test_d1cat_filtered_colimit.py \
                tests/test_d1cat_transfinite_colimit.py \
                tests/test_d1filtered_graded_functor.py \
                tests/test_d1filtered_compose_meet.py -q            # 63 passed (no sibling breakage)
python -m models.d1filtered_compose_meet                            # prints the decision payload
```

## Next proof / computation step

1. Verify the lax-functor **coherence pentagon** for `gr` over composable triples in `D1FilteredCat_meet` (upgrade object-wise lax → genuine lax functor).
2. Decide the adjunction/section `J: D1FilteredCat → D1FilteredCat_meet` and whether `bottom ∘ gr_semilattice` recovers T232's forgetful `U` as a sub-functor.
3. Only after (1)/(2): revisit whether any of this touches cocompleteness for broader diagram shapes — **not** claimed here.
