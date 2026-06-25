# T237: Is the associated-graded map gr: D1FilteredCat -> GradedSets a (lax) functor?

**Status:** implemented — finite-witness model + pytest green (`21 passed`; `45 passed` with the T232/T228 siblings)
**Builds on:** [T232](T232-d1cat-filtered-colimit.md) (D1FilteredMorphism + `compose_filtered` + `associated_graded` + the forgetful `U` + the monotone-descending typing with non-monotone proven illegal — named this constructive-next object (1) verbatim), [T228](T228-d1cat-transfinite-colimit-decision.md) (the bare-intersection colimit is content-free; binding cocompleteness honesty guard)
**Resolves:** the first constructive-next object T232 named — *"`gr: D1FilteredCat -> GradedSets` sending a morphism to its associated-graded strata, and a check whether `gr` is itself a (lax) functor under filtered composition — i.e. whether `gr(f;g)` refines `gr(f)` and `gr(g)` coherently."* This upgrades T232's "the colimit carries the schedule" to the question "is the schedule **functorial**."
**Model:** [`models/d1filtered_graded_functor.py`](../models/d1filtered_graded_functor.py)
**Tests:** [`tests/test_d1filtered_graded_functor.py`](test_d1filtered_graded_functor.py)
**Results:** [`results/d1filtered-graded-functor/T237-results.json`](../results/d1filtered-graded-functor/T237-results.json)
**Tags:** `finite_witness` (executable fixture over the fixed 4-element dimension universe; no continuum/scalable theorem asserted) · `poly_decider` (finite enumeration over the fixed universe; not a hidden search, not a hardness/NP claim)

---

## Verdict

**conditional** — *`gr` IS a functor, **strictly**, on the gr-composable subcategory of `D1FilteredCat` (the pairs whose composite filtration stays legal/descending — equivalently the filtration-NESTED pairs, which includes the entire T232 colimit chain). It is NOT a functor on all of `D1FilteredCat`, because `compose_filtered` is **not closed on legal morphisms**: two legal descending morphisms with mutually non-nested filtrations compose to a non-descending (illegal) morphism on which `gr(f;g)` is undefined. The binding extra hypothesis is gr-composability (filtration-nesting). This does NOT establish general cocompleteness at infinity (inherited T228/T232 honesty guard).*

| Sub-question | Verdict |
| --- | --- |
| Is `gr` well-defined on objects + morphisms (sending a `D1FilteredMorphism` to `associated_graded(filtration)`)? | **closed (yes).** `gr(m)` is exactly T232's `associated_graded(m.filtration)`; on objects it is the carrier label (GradedSets object). |
| Identity law: `gr(id) == id_gr`? | **closed (yes).** `make_filtered_identity` has the single full-universe layer; its associated-graded is the single full bottom stratum, dropping nothing — `graded_identity()`. |
| Composition law on the gr-composable (nested) sub-domain: `gr(f;g) == mu(gr f, gr g)`? | **closed (yes, strict).** Strict equality across the whole nested battery (7 pairs) **and** the full descending T232 colimit chain; no loss / no gain of dropped dimensions; canonical comparison exists in every case. |
| Composition law on ALL of `D1FilteredCat`? | **no (obstructed).** `compose_filtered` is not legality-closed for non-nested filtrations, so `gr(f;g)` is **undefined** there — `gr` is at best a **partial** functor without the nesting restriction. |
| Does this establish cocompleteness at infinity / extend to non-monotone diagrams? | **no (open).** `gr` is undefined on non-monotone filtrations by construction; the result is confined to the monotone-descending typing. |

Net: T232's "the colimit **carries** the schedule" is upgraded to "the schedule is **strictly functorial on the gr-composable subcategory**." The verdict is `conditional`, not `closed`, because the functor is **domain-restricted by an exhibited obstruction** (non-nested composition leaves the legal subcategory), and the positive result is confined to monotone-descending filtrations.

## What was derived from the read-first sources

- **From T232** (`models/d1cat_filtered_colimit.py`, imported verbatim, never modified): `D1FilteredMorphism` (site_map + descending preserved-dims filtration), `compose_filtered` (= `_refine_filtrations`: concatenate both filtrations' layers, **dedupe by frozenset, re-sort descending by size**), `associated_graded` (`gr_k = F_k \ F_{k+1}` + bottom stratum), `make_filtered_identity` (single full layer), `filtration_is_legal` (non-empty + every layer ⊆ universe + **set-descending**), and `D1FilteredMorphism.is_legal()`. T237 builds `gr` directly on `associated_graded` and tests the functor laws against `compose_filtered` — the live operation, untouched.
- **From T228** (honesty guard, binding): a positive descending-chain result must **not** be over-read as general cocompleteness at infinity. T237 re-verifies the boundary (`gr` rejects non-monotone filtrations) and confines all functoriality claims to the monotone-descending typing.
- **The decisive structural fact this lane surfaced** (latent in T232's `_refine_filtrations`, never tested there because T232's battery used only **prefix-nested** chains): the re-sort-by-size in `_refine_filtrations` only yields a descending composite when the two input filtrations are mutually **nested**. T232's own tests never hit a non-nested pair, so the non-closure was invisible until the functoriality question forced general composable pairs.

## Strongest positive result

**Three executable facts decide the rung.**

1. **Identity is preserved strictly.** `gr(make_filtered_identity(X))` is the single full-universe bottom stratum, dropping nothing, equal to `graded_identity()` (`gr_preserves_identity` → `identity_law_holds == True`, `identity_drops_nothing == True`).

2. **Composition is STRICT on the gr-composable subcategory.** Define the canonical schedule concatenation `mu(gr f, gr g)` = "do f's drops, then g's drops within f's residue; joint floor = intersection of floors" — defined **independently** of `_refine_filtrations`, from the schedule semantics, NOT by copying the compose code. Across the entire nested battery (successive `4→3→2`, `4→2→1`; shared-top nested `4→3`/`4→2`; residue-restrict `4→3`/`4→1`; left/right identity; saturating `4→2→∅`) **and** the full length-6 T228 descending colimit chain, `gr(compose_filtered(f,g)) == mu(gr f, gr g)` **strictly** (`strict_on_composable_subdomain == True`, `chain_associativity.strict_equal == True`), with `no_loss_no_gain` (the composite records exactly the union of the two summand drops) and a canonical comparison existing in every case. So on the subcategory where it is defined, `gr` is not merely lax — it is a **strict** functor.

3. **The comparison structure is the right one.** The target category `GradedSets` (built here, finite, thin/poset-style) has a canonical comparison morphism `gr(f;g) → mu(gr f, gr g)` that **exists iff the two gradings drop the same dimensions and share the same floor** (the lax-coherence datum), and is **strict iff the strata coincide in order**. The test battery confirms: same-schedule/different-grouping pairs admit the comparison but are non-strict (genuinely lax-capable), while different-floor pairs admit no comparison (`graded_comparison` separates the two). The machinery would have **detected** laxity had any composable pair been only lax — it found strictness instead.

## First exact obstruction / missing object

**`compose_filtered` is not closed on legal `D1FilteredMorphism`s.** Concretely (the witness in `test_non_nested_composite_is_illegal_so_gr_undefined`):

> `f: 4 ⊇ {a,h,b}` (drops `reversal_cost`) and `g: 4 ⊇ {h,r}` (drops `accessible_support, branch_support`) are **each** legal descending morphisms (`f.is_legal()`, `g.is_legal()`). Their filtration bottoms `{a,h,b}` and `{h,r}` are **incomparable** (neither contains the other). `_refine_filtrations` concatenates the layers and re-sorts by size, producing `4 ⊇ {a,h,b} ⊇ {h,r} ⊇ {h}` — but `{a,h,b} ⊇ {h,r}` is **false** (`{a,h,b}` lacks `r`). The composite is **not descending**: `compose_filtered(f,g).is_legal() == False`, and `gr` of it raises (`gr_composable(f,g) == False`).

Therefore `gr(f;g)` is **undefined** precisely when the two filtrations are non-nested, and `gr` is **not** a functor on all of `D1FilteredCat`. The missing object is a **legality-closed filtered composition** — either (a) a `compose_filtered` whose `_refine_filtrations` takes the **layerwise meet-closure** (the lattice join of the two descending chains in the subset poset) so the composite is always descending, restoring a total category on which `gr` could be a genuine (lax) functor; or (b) an explicit restriction of `D1FilteredCat` to the **filtration-nested subcategory** as the honest domain, on which T237 already proves `gr` strict. Neither is built here.

This obstruction is **not** present in T232 because T232's battery used only prefix-nested chains; it is the new information this rung produces.

## Constructive next object

Two well-posed directions, neither built here:

1. **Legality-closed filtered composition** `compose_meet`: replace `_refine_filtrations`' size-sort with the **subset-lattice meet-closure** of the two descending chains (insert all pairwise intersections so the merged chain is genuinely set-descending). Decide whether `compose_meet` is associative with identities (making `D1FilteredCat_meet` a proper *total* category) and whether `gr` is then a **total** (strict or lax) functor on it. This is the direct repair of the obstruction above.
2. **A `gr`-fibration / naturality statement**: with `gr` strict on the nested subcategory, ask whether the comparison morphisms `gr(f;g) → mu(gr f, gr g)` assemble into a **natural transformation** (lax-functor coherence cells) over the nested subcategory, and whether the bottom-stratum assignment `m ↦ graded_bottom(gr m)` recovers the forgetful `U: D1FilteredCat → D1Cat` as a sub-functor (it should: `graded_bottom(gr m) == bare_intersection(m.filtration) == U(m).preserved_dimensions`).

Both are **discrete category-level** objects, **explicitly distinct** from the continuum coefficient-sheaf-H1 cofinality lane (T231/T236), which they do not touch and must never be conflated with.

## Meaning for the relevant claim

- **D1Cat / D1FilteredCat (proto_independent row):** T232's `conditional` content-bearing colimit is **undisturbed**, and its named next object (1) is now **decided**: `gr` is a **strict functor on the gr-composable subcategory** (identity + strict composition across the nested battery and the full colimit chain), `conditional` on the filtration-nesting hypothesis. The honest net for the ledger: "the schedule is functorial" holds **strictly where filtered composition stays legal**, and the first obstruction to a *total* functor is the **non-legality-closure of `compose_filtered` under non-nested composition** (newly exhibited). General cocompleteness at infinity remains **open**, untouched.
- **Honesty guard (binding T228/T232 criterion):** explicitly **not** violated. The positive result is confined to monotone-descending filtrations and to the legal (nested) composites; `gr` rejects non-monotone filtrations; cocompleteness is named still open. The strict-functor result is **not** over-read as totality — the obstruction is recorded, not hidden.
- **No over-promotion:** no physics/geometry/curvature/new-object/Čech/sheaf language. "associated-graded / filtration / functor / graded set" name finite operations on descending chains of subsets of a fixed 4-element set. This lane is the **discrete** analogue and is distinct from the κ / sheaf-H1 / MTI files, none of which it touches.

## Failure conditions for this verdict

This verdict is **wrong** if any of the following is shown:

- **The identity law fails** (`gr(id) ≠ id_gr`). *Checked false:* `test_identity_law_holds`, `gr_preserves_identity().identity_law_holds == True`.
- **Composition is NOT strict on some gr-composable (nested) pair** (only lax, or fails). *Checked false:* `test_strict_everywhere_on_composable_subdomain` + `test_chain_associativity_strict` — strict equality on all 7 nested pairs and the full colimit chain.
- **The non-nested composite is actually legal** (so the obstruction is fictitious and `gr` is total). *Checked false:* `test_non_nested_composite_is_illegal_so_gr_undefined` — `compose_filtered(f,g).is_legal() == False` for legal non-nested `f,g`; `gr` raises.
- **`mu` was secretly a copy of `_refine_filtrations`** (so strictness is circular). *Guarded:* `mu` is defined from schedule semantics (stage-2 restricted to stage-1 residue, joint floor by intersection) and is tested to **diverge in grouping** from a re-grouped schedule in `test_comparison_exists_iff_same_schedule` (same support, non-strict) — the comparison machinery can register laxity; it registered strictness.
- **A general cocompleteness / non-monotone claim is read into this** result. *Guarded:* `gr` rejects non-monotone filtrations (`test_gr_rejects_non_monotone_filtration`); cocompleteness named open.

## Known Physics Constraints

None. T237 is a pure category-theoretic decision about whether one finite associated-graded assignment is a functor. No hardness/scale claim is made (finite enumeration over a 4-element universe; per COMPLEXITY-LEDGER the relevant engines are `poly_decider`/`finite_witness`). No physics/geometry/curvature/new-object vocabulary is promoted. This lane is **distinct** from the continuum coefficient-sheaf-H1 cofinality lane (T231/T236) and does not touch the κ, sheaf, or MTI files.

## Reproduction

```
cd "<repo root>"
python -m pytest tests/test_d1filtered_graded_functor.py -q          # 21 passed
python -m pytest tests/test_d1cat_filtered_colimit.py \
                tests/test_d1cat_transfinite_colimit.py \
                tests/test_d1filtered_graded_functor.py -q           # 45 passed (no sibling breakage)
python -m models.d1filtered_graded_functor                           # prints the decision payload
```

## Next proof / computation step

1. Build `compose_meet` (subset-lattice meet-closure replacing the size-sort) and decide whether `D1FilteredCat_meet` is a proper **total** category on which `gr` is a total (strict/lax) functor — the direct repair of the non-closure obstruction.
2. Promote the per-pair comparison morphisms to a **natural transformation** over the nested subcategory (lax-functor coherence) and verify `m ↦ graded_bottom(gr m)` recovers the forgetful `U` as a sub-functor.
3. Only after (1)/(2): revisit whether any of this touches cocompleteness for broader diagram shapes — **not** claimed here.
