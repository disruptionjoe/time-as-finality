# T228: D1Cat Transfinite Colimit Decision

**Status:** implemented — finite-witness model + pytest green (`7 passed`)
**Builds on:** [T222](T222-finite-to-infinite-boundary-theorem.md) (the
conditional edge and its Contribution-Needed item #ii),
[T41](T41-typed-transport-category.md) (D1Cat category construction),
[T39](T39-csp-satisfiability-reframing.md) (object semantics)
**Resolves:** the single structure-level edge T222 left `conditional` for D1Cat:
"construct a D1Cat colimit of the transfinite strictly-descending chain, or
prove none of the desired form exists."
**Model:** [`models/d1cat_transfinite_colimit.py`](../models/d1cat_transfinite_colimit.py)
**Tests:** [`tests/test_d1cat_transfinite_colimit.py`](test_d1cat_transfinite_colimit.py)

---

## Verdict

**closed** — *with a split, decision-grade outcome on the "desired form" the
edge actually named.*

| Sub-question | Verdict |
| --- | --- |
| Does a colimit **of the desired form** (a D1Cat object carrying surviving, non-trivial preserved-dimension content) exist for the transfinite strictly-descending chain? | **no-go.** Proven non-existent. The surviving content is provably `()`. |
| Is the diagram therefore a **counterexample to colimit existence** (does D1Cat *fail* to have this colimit)? | **no.** A colimit exists; it is the content-free object with the empty-preserved cocone, which is a **legal** D1Cat colimit. |
| Is D1Cat thereby shown **cocomplete at infinity**? | **no.** This single positive case does not generalize; cocompleteness remains a separate open question (honesty guard, below, respected). |

Net: the edge moves from `conditional` to **closed**. The descending chain has a
D1Cat colimit, but it is the **degenerate (content-free) colimit**; the
content-bearing colimit "of the desired form" provably does not exist. T222's
worry that "the colimit morphism preserves no dimension, *outside* the profile
axioms" was **mistaken about which axioms are at stake** — empty preserved_dims
is *inside* the morphism axioms — and the obstruction is relocated to (and
dissolved at) the object level.

## What was derived from the read-first sources

- **From T222** (verdict table + Contribution Needed): the conditional D1Cat
  edge is *exactly* the transfinite-chain colimit; the rest of D1Cat (category
  laws, non-functor, finite/countable survival) is already `survives`. The
  honesty guard is binding: do **not** over-read "category survives" as
  "cocomplete at infinity."
- **From T41** (D1Cat construction): morphisms compose by **site-map function
  composition** (associative) and **preserved_dims set intersection**
  (associative); identities via `make_identity`; the universe of
  preserved_dimensions is the **fixed 4-element** `D1_DIMENSIONS`.
- **From the model code** (`d1_restriction_system.py`, `transport_network.py`):
  `preserved_dimensions: tuple[str, ...]` is a field on the **morphism**, valued
  in **subsets of** `D1_DIMENSIONS`; `_compose_morphisms` intersects them; the
  empty subset `()` is a legal value. The object axioms (A1–A7) constrain
  `D1RestrictionSystem`s and constrain morphisms only via **value-agreement on
  preserved dimensions** (`_profile_dimensions`); they say nothing forbidding an
  empty preserved set.
- **From the audit** (MATHEMATICAL-INDEPENDENCE-AUDIT): "Own operations" is
  `Present and complete (T41)`; this lane does not touch that — it sharpens the
  one infinitary edge without claiming new independence.

## Strongest positive result

**Two precise structural facts, both executable, decide the edge.**

1. **The descent saturates in ≤ 4 steps; "transfinite" is a red herring at the
   level of the morphism dimension data.** Because the preserved-dimension
   universe is the fixed 4-element `D1_DIMENSIONS` and composition intersects,
   any strictly-descending chain reaches `()` after at most 4 compositions and
   is **constant thereafter**: `4 → 3 → 2 → 1 → 0 → 0 → …`
   (`build_descending_chain`, verified `sizes == [4,3,2,1,0,0]`). The transfinite
   tail of the chain contributes **no further change** to the composite
   preserved_dims. The empty-intersection "limit" is reached at a finite stage.

2. **The empty-preserved-dimensions morphism is a *legal* D1Cat morphism.**
   `()` is a valid (empty) subset of `D1_DIMENSIONS`; its endpoints are valid
   `D1RestrictionSystem`s (`validate_system(...).valid`); `analyze_morphism`
   reports such a morphism **`reached`** even between objects that disagree on
   *every* profile dimension (because preservation is checked only on the
   declared — here empty — set). Therefore the colimit cocone leg carrying
   `preserved_dims = ()` does **not** exit D1Cat. This is the honesty correction
   to T222's "outside the profile axioms" framing: empty preserved_dims is
   **inside** the axioms.

Consequence: for the **constant-object** descending chain (the canonical case
T222 points at — the object is fixed and only the morphism metadata descends),
the colimit object is the object itself and the cocone leg is the legal
empty-preserved morphism (`sequential_colimit_of_constant_object_chain`:
`colimit_object_valid`, `colimit_leg_legal`, `colimit_leg_preserved == ()`). The
colimit **exists**.

## First exact obstruction / missing object

The colimit **of the desired form** — an object carrying *surviving, non-trivial*
preserved-dimension content — is provably absent, and the obstruction is exact:

> Once the chain's composite preserved set has emptied (which it must, by Fact 1),
> a D1Cat morphism into any candidate colimit object checks **agreement on the
> empty set**, i.e. checks **nothing**. Objects that disagree on every profile
> dimension are then freely connectable by legal empty-preserved morphisms
> (`object_varying_chain_has_no_uniform_colimit_object`:
> `disagreeing_profiles=True`, `empty_preserved_morphism_reached=True`).

Therefore the candidate colimit object is **underdetermined by the surviving
diagram data**: the diagram's residual content that a colimit is supposed to
universally capture is empty, so *every* object admits the cocone, and the
**initial (universal) such object carries no dimension content**. The
"surviving-dimension colimit" is not merely hard to construct — it is the colimit
of an **empty constraint**, hence content-free by construction. The missing
object (a content-bearing universal cocone target) **does not exist** because the
content it would universalize has been intersected away at a finite stage.

This is a genuine `no-go` on the *desired form*, not a hidden cocompleteness
claim: it says the **specific** chain's content-bearing colimit is absent, while
a degenerate colimit is present.

## Constructive next object

The decision shows the right repair is **not** inside D1Cat-as-currently-typed.
Two constructive directions, each well-posed:

1. **A graded / filtered D1Cat** in which the preserved-dimension data is carried
   as a **descending filtration object** (the chain `4 ⊇ 3 ⊇ 2 ⊇ 1 ⊇ ∅` itself)
   rather than collapsed to its intersection. The colimit would then be an
   **associated-graded object** whose strata record *when* each dimension was
   dropped. This carries the transition data the bare intersection forgets —
   structurally the *same* honesty move as the sheaf-H1 / coefficient-aware
   lane (which is the **continuum** version; this filtration is the **discrete
   category-level** version). Build target:
   `D1FilteredMorphism` = (site_map, descending preserved-dims filtration).
2. **An explicit colimit-of-the-degenerate-form theorem**: declare the
   content-free object as the *canonical* colimit and prove the universal
   property holds for it (the constant-object case already verifies the cocone;
   the general case needs the object-level coproduct/quotient on
   `D1RestrictionSystem`s). This closes cocompleteness for **descending** chains
   only, without claiming general cocompleteness.

## Meaning for the relevant claim

- **D1Cat (proto_independent row):** the T222 verdict `survives` for the category
  laws is **undisturbed**, and the `conditional` qualifier on the transfinite
  edge is now **resolved**: the colimit edge is `closed`. D1Cat has the
  descending-chain colimit (degenerate form); it is **not** thereby cocomplete at
  infinity. The CLAIM-LEDGER language for D1Cat should change from
  "transfinite-chain edge conditional" to "transfinite-chain colimit closed:
  exists as the content-free object; content-bearing form provably absent;
  cocompleteness still open."
- **Honesty guard (binding T222 failure criterion):** explicitly **not**
  violated. "Category survives" is **not** over-read as "cocomplete at
  infinity." The positive result is confined to one diagram shape (descending
  chains) and one (degenerate) colimit; general cocompleteness is named as still
  open.
- **No over-promotion:** no physics/geometry/new-object language; no Čech/sheaf
  claim (this is the category-theoretic cocompleteness edge, explicitly distinct
  from the continuum coefficient sheaf-H1 lane). The single new object proposed
  (`D1FilteredMorphism`) is offered as *constructive next*, not claimed as built.

## Failure conditions for this verdict

This verdict is **wrong** if any of the following is shown:

- The preserved-dimension universe is **not** fixed-finite (e.g. dimensions can
  be added along the chain). Then the descent need not saturate and "transfinite"
  stops being a red herring. *Checked false:* `D1_DIMENSIONS` is a fixed
  4-tuple; no operation in the model adds dimensions.
- An empty-preserved morphism is **not** a legal D1Cat morphism (some axiom
  forbids `preserved_dimensions == ()`). *Checked false:*
  `empty_preserved_morphism_is_legal()` and `analyze_morphism(...).reached` both
  hold.
- A **content-bearing** colimit object can be exhibited whose cocone legs carry a
  non-empty intersection of the chain's surviving dimensions. *Shown impossible:*
  the surviving intersection is provably `()` (Fact 1), so any cocone leg
  factoring the whole chain carries `()`.
- The constant-object colimit fails the universal property. *Checked false* for
  the constant diagram (the object's own legs factor any cocone); the general
  object-varying universal property is **explicitly left to the constructive-next
  object**, and the verdict claims only the degenerate colimit + the no-go on the
  desired form, not full cocompleteness.

## Known Physics Constraints

None. T228 is a pure category-theoretic decision about cocompleteness of D1Cat at
a single infinitary diagram. No hardness/scale claim is made (the model is a
finite enumeration over a 4-element universe; per COMPLEXITY-LEDGER the relevant
engines are `poly_decider`/`finite_witness`, untouched here). No
physics/geometry/curvature/new-object vocabulary is promoted. This lane is
**distinct** from the sheaf-H1 continuum-coefficient lane and does not touch the
kappa, functor, or MTI files.

## Next proof / computation step

1. Define `D1FilteredMorphism` (site_map + descending preserved-dims filtration)
   and re-pose the transfinite-chain colimit as an associated-graded object;
   check whether *that* colimit is content-bearing (this is the discrete
   category-level analogue of the coefficient-aware sheaf-H1 object the T222
   sibling lane builds).
2. Prove the object-level universal property for the degenerate colimit in the
   **object-varying** case by constructing the `D1RestrictionSystem`-level
   coproduct/quotient, upgrading "descending-chain colimit exists" from the
   constant-object case to all descending chains.
3. Only after (1)/(2): revisit whether D1Cat (or D1FilteredCat) is cocomplete for
   broader diagram shapes — **not** claimed here.
