# T232: D1FilteredMorphism — does the content-bearing graded colimit exist in the filtered category?

**Status:** implemented — finite-witness model + pytest green (`17 passed`; `24 passed` with the T228 sibling)
**Builds on:** [T228](T228-d1cat-transfinite-colimit-decision.md) (closed the bare-intersection edge with a no-go on the desired form; named this repair object verbatim), [T41](T41-typed-transport-category.md) (D1Cat construction: site-map composition + preserved-dims intersection)
**Resolves:** the single constructive-next object T228 named —
`D1FilteredMorphism = (site_map, descending preserved-dims filtration)` — and the live question T228 left for it: re-posed in the filtered category, is the descending-chain colimit content-**bearing** where the bare-intersection colimit was content-**free**?
**Model:** [`models/d1cat_filtered_colimit.py`](../models/d1cat_filtered_colimit.py)
**Tests:** [`tests/test_d1cat_filtered_colimit.py`](test_d1cat_filtered_colimit.py)
**Tags:** `finite_witness` (executable fixture over the fixed 4-element dimension universe; no continuum/scalable theorem asserted) · `poly_decider` (finite enumeration; not a hidden search, not a hardness/NP claim)

---

## Verdict

**conditional** — *the content-bearing filtered colimit EXISTS for descending chains (positive, decided), under the explicitly named extra hypothesis that the diagram's preserved-dimension data is **monotone descending**. It does NOT establish general cocompleteness at infinity (honesty guard, binding from T228).*

| Sub-question | Verdict |
| --- | --- |
| Is `D1FilteredMorphism` a proper category (`D1FilteredCat`): associative composition + two-sided identities? | **closed (yes).** Filtered composition = refinement of descending filtrations; associativity + identity laws pass by finite-enumeration witness. |
| Does a forgetful functor `U: D1FilteredCat → D1Cat` recover T228's bare-intersection morphism? | **closed (yes).** `U` keeps only the bottom layer (= bare intersection); `U(id)` is the D1Cat identity. The content-free object T228 saw is exactly `U` of the filtered colimit. |
| Re-posed in `D1FilteredCat`, is the descending-chain colimit **content-bearing**? | **conditional (yes, for descending chains).** The colimit is the **associated-graded** object; its strata `gr_k = F_k \ F_{k+1}` are the non-empty singletons recording the drop schedule — exactly the content the bare intersection collapsed to `()`. |
| Does this make `D1FilteredCat` **cocomplete at infinity**? | **no (open).** The construction is typed to monotone-descending filtrations; a non-monotone "pseudo-filtration" (re-adding a dropped dimension) is an illegal morphism, so the result does not extend to arbitrary diagrams. |

Net: the colimit edge T228 closed degenerately at the OBJECT/intersection level is **re-opened content-bearing** at the GRADED level. The schedule "WHEN each of the 4 fixed dimensions was dropped" — destroyed by intersection in D1Cat — **survives** as the associated-graded strata in `D1FilteredCat`. The verdict is `conditional`, not `closed`, because (a) the surviving content is exactly the drop-schedule grading, not a new categorical limit beyond it, and (b) the positive result is confined to descending chains by the monotonicity typing.

## What was derived from the read-first sources

- **From T228** (the no-go + the named repair): the bare-intersection colimit of the strictly-descending chain exists only as the content-free object because composition intersects `preserved_dims` to `()` in ≤ 4 finite steps over the fixed 4-element `D1_DIMENSIONS`; "transfinite" is a red herring at the morphism-dimension level. T228 named the repair **verbatim**: a graded/filtered D1Cat whose morphism carries the descending filtration `4 ⊇ 3 ⊇ 2 ⊇ 1 ⊇ ∅` itself, so the colimit becomes an **associated-graded object** whose strata record *when* each dimension dropped. Binding honesty guard inherited: a content-bearing filtered colimit for descending chains does **not** establish general cocompleteness at infinity.
- **From T41** (D1Cat construction): morphisms compose by site-map function composition (associative) and preserved-dims **intersection** (associative); identities via `make_identity`; the universe is the fixed 4-element `D1_DIMENSIONS`. T232 keeps the object component and the site-map component unchanged and **replaces only** the preserved-dims component (intersection → descending filtration).
- **From the model code** (`d1cat_transfinite_colimit.py`, `d1_restriction_system.py`): `preserved_dimensions` is a morphism field valued in subsets of `D1_DIMENSIONS`; the empty subset `()` is legal; `validate_system` certifies the object endpoints; the descending chain saturates `4→3→2→1→0` at a finite stage. T232 reuses `_one_site_system`, `validate_system`, `SiteMap`, and the same chain shape.

## Strongest positive result

**Two executable facts decide the edge.**

1. **`D1FilteredCat` is a proper category and maps onto D1Cat.** Filtered composition `compose_filtered` (i) composes site maps as functions and (ii) **refines** the two descending filtrations into a single monotone descending chain retaining every layer plus the composite bare-intersection bottom. This is associative (`filtered_composition_is_associative`) with two-sided identities (`filtered_identity_laws_hold`, the identity's single full layer being absorbed by refinement). The forgetful functor `U` (`to_d1cat_morphism`) keeps only the bottom layer and lands exactly on T228's bare-intersection morphism — `U` of the filtered colimit **is** the content-free colimit T228 closed on (`forgetful_functor_lands_in_d1cat`, `test_forgetful_functor_recovers_bare_intersection_morphism`: `U(m).preserved_dimensions == ()`).

2. **The filtered colimit is content-bearing where the bare one is content-free.** The composite filtration of the length-6 descending chain is the **full** descending chain `4 ⊇ 3 ⊇ 2 ⊇ 1 ⊇ ∅` (`test_chain_composite_filtration_is_the_full_descending_chain`: sizes `[4,3,2,1,0]`). Its associated-graded (`associated_graded`) is four **singleton** drop strata `[reversal_cost], [branch_support], [holder_redundancy], [accessible_support]` plus the empty bottom (`test_associated_graded_recovers_drop_schedule`). So: `bare_intersection == ()` is content-**free** (T228), while the graded strata recover the **entire** dimension universe in drop order (`schedule_recovers_universe == True`) — content-**bearing** (`filtered_colimit_is_content_bearing`). Nothing was lost; the data was **re-graded** instead of intersected away.

## First exact obstruction / missing object

The obstruction is no longer "the content was intersected to `()`" — it is **relocated to a typing boundary**: the content-bearing colimit exists **only** while the preserved-dimension data is **monotone descending**.

> A non-monotone pseudo-filtration that re-adds a dropped dimension (`4 ⊇ 3 ⊆ 4`) is **not** a legal `D1FilteredMorphism` (`filtration_is_legal` returns `False`; `non_monotone_pseudofiltration_is_illegal`: `non_monotone_morphism_legal == False`, while the descending counterpart is legal).

Therefore `D1FilteredCat` does **not**, by this construction, possess colimits for arbitrary diagrams whose preserved data is non-monotone. The missing object is a colimit construction for **non-descending** diagrams — and that is exactly where general cocompleteness at infinity would have to be argued. It is **not** built here and **not** claimed (`general_cocompleteness_still_open == True`). This is the binding T228 failure criterion made executable: "category survives" / "descending colimit content-bearing" is **not** over-read as "cocomplete at infinity."

## Constructive next object

Two well-posed directions, neither built here:

1. **The graded colimit as a functor** `gr: D1FilteredCat → GradedSets` sending a morphism to its associated-graded strata, and a check whether `gr` is itself a (lax) functor under filtered composition — i.e. whether `gr(f;g)` refines `gr(f)` and `gr(g)` coherently. This would upgrade "the colimit carries the schedule" to "the schedule is functorial," the natural next rung.
2. **A cocompleteness boundary theorem for `D1FilteredCat`**: characterize precisely which diagram shapes (beyond monotone-descending chains) admit a content-bearing filtered colimit, and exhibit the first shape that does **not** — turning the typing boundary above into a sharp positive/negative dividing line. Only this would touch the still-open cocompleteness-at-infinity question.

These are the **discrete category-level** analogues of the coefficient-aware refinement; they are **explicitly distinct** from the continuum coefficient-sheaf-H1 lane (T226/T231) and do not touch it.

## Meaning for the relevant claim

- **D1Cat / D1FilteredCat (proto_independent row):** T228's `closed` no-go on the bare-intersection colimit is **undisturbed** — that colimit is still content-free, and `U` recovers it exactly. T232 **adds** a graded refinement `D1FilteredCat` in which the descending-chain colimit is **content-bearing** (`conditional`, descending chains only). The honest net for the ledger: the transfinite-chain edge has a content-free colimit in D1Cat (T228, closed) and a content-bearing colimit in the graded refinement D1FilteredCat for descending chains (T232, conditional); general cocompleteness at infinity remains **open** in both.
- **Honesty guard (binding T228 criterion):** explicitly **not** violated. The positive result is confined to monotone-descending filtrations; the non-monotone case is a proven-illegal boundary, and cocompleteness at infinity is named as still open.
- **No over-promotion:** no physics/geometry/curvature/new-object language; no Čech/sheaf claim. "Associated-graded" / "filtration" name a finite descending chain of subsets of a fixed 4-element set and its successive differences — named as such. This lane is the **discrete** analogue and is distinct from the continuum sheaf-H1 / κ / functor / MTI files, none of which it touches.

## Failure conditions for this verdict

This verdict is **wrong** if any of the following is shown:

- **Filtered composition is not associative** or lacks identities. *Checked false:* `filtered_composition_is_associative()` and `filtered_identity_laws_hold()` both hold over the test battery (refinement of descending chains is associative; the identity's full layer is absorbed).
- **The forgetful functor `U` does not recover T228's bare-intersection morphism.** *Checked false:* `U(m).preserved_dimensions == ()` for the saturating chain and `U(id)` is the full-preserved identity (`forgetful_functor_lands_in_d1cat`).
- **The associated-graded strata are empty / do not recover the drop schedule** (i.e. the filtered colimit is *also* content-free). *Checked false:* the four drop strata are non-empty singletons recovering the full universe (`schedule_recovers_universe == True`); the bare bottom is `()` (`bare_is_content_free == True`), so the two readings genuinely diverge.
- **A non-monotone pseudo-filtration is accepted as a legal morphism** (which would mean the construction is not actually typed to descending chains and the honesty guard's boundary is fictitious). *Checked false:* `non_monotone_morphism_legal == False` while `descending_counterpart_legal == True`.
- **A general cocompleteness-at-infinity claim is read into this result.** *Guarded:* the construction refuses non-descending diagrams; cocompleteness is named open, not closed.

## Known Physics Constraints

None. T232 is a pure category-theoretic decision about a graded refinement of D1Cat at a single descending diagram. No hardness/scale claim is made (finite enumeration over a 4-element universe; per COMPLEXITY-LEDGER the relevant engines are `poly_decider`/`finite_witness`). No physics/geometry/curvature/new-object vocabulary is promoted. This lane is **distinct** from the continuum coefficient-sheaf-H1 lane (T226/T231) and does not touch the κ, functor, or MTI files.

## Reproduction

```
cd "<repo root>"
python -m pytest tests/test_d1cat_filtered_colimit.py -q      # 17 passed
python -m models.d1cat_filtered_colimit                       # prints the decision payload
```

## Next proof / computation step

1. Define `gr: D1FilteredCat → GradedSets` and test whether the associated-graded is **functorial** under filtered composition (does `gr(f;g)` cohere with `gr(f), gr(g)`?), upgrading "colimit carries the schedule" to "the schedule is functorial."
2. Characterize the diagram shapes beyond monotone-descending chains for which a content-bearing filtered colimit exists, and exhibit the first shape that does **not** — converting the monotonicity typing boundary into a sharp cocompleteness dividing line.
3. Only after (1)/(2): revisit whether `D1FilteredCat` is cocomplete for broader diagram shapes — **not** claimed here.
