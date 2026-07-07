# The Boundary Adapter as a FUNCTOR — first specification (starting CT-1)

Open-problem note, 2026-07-07 (Joe, chat — "start #1"). **No claim moves in any repo.** This is a
specification, not a built functor. It applies the category-theoretic corrective **CT-1 (Name-the-Category)**
(`ai-epistemology/field-guide/branch-5-evolvability/category-theoretic-method-correctives.md`) to the tri-repo
boundary adapter, and sharpens Section 5 of `gu-ti-taf-reciprocal-bridge-contract.md`.

## The reframe (why the adapter is stuck at "analogy grade")

Every bridge the tri-repo work has left at "analogy grade" — "the mirror IS the collective-capability
boundary", "GU's boundary content = C(R)'s collective complement" — is stated at the level of **objects**, with
the category of **morphisms** never named. The one bridge that became a theorem this session (the Z/3-vs-D4
gate) named its category and computed a hom-set. CT-1 says: **the boundary adapter should BE a functor** — a
named source category, a named target category, and an action on morphisms — and "two adapters must prove out"
should mean "exhibit the functor and show it is not constant."

The reciprocal-bridge-contract already gestures at this (Section 5): `S : Compat_G^MLTT -> FiltSh(C)` and
`R : FiltSh(C) -> ReadoutValues`. But these are written as **maps**, never verified to be **functors**: no
action on morphisms is given, and no non-triviality is required. This note supplies the missing categorical
skeleton for the GU-boundary <-> TaF-capability leg.

## Target category: DONE — it already exists and is PROVEN (`D1Cat`, T41)

The capability side is not a gap. `time-as-finality` already has a proven category:

- **Objects:** `D1RestrictionSystem`s (record systems with observer sites, D1 profiles, transport edges).
- **Morphisms:** `D1RestrictionMorphism`s (`_compose_morphisms`, `make_identity`).
- **Category laws:** associativity + left/right unit **verified** in T41 (`models/typed_transport_category.py`,
  "Typed Transport Category Theorem"). This is a real, checked category — call it `D1Cat`.
- The capability object **C(R)** and T392/T395 (a capability difference with zero statistical trace) live over
  this category; the region-indexed capability structure is its natural home.

So the functor's **target is specified and machine-checked.** No work needed there beyond choosing whether the
target is `D1Cat` itself or a capability-decorated subcategory (objects = `C(R)` for bounded regions `R`,
morphisms = restriction morphisms `R' <= R`).

## Source category: THE GAP — GU boundary content is not yet a category

GU supplies boundary **content** (the mirror sector; the Krein-structured 192-dim carrier; the
`P_ghost`-eigenspaces; sectors of signature `(+96,-96,0)`) but **not as a category.** To build the functor,
GU's boundary data must first be given as a category `GUBdy`:

- **Objects (candidate):** boundary sectors / subspaces of the carrier — e.g. `P_ghost`-eigenspaces, Krein
  subspaces, or (region-indexed) boundary data attached to a bounded region.
- **Morphisms (candidate, UNBUILT — this is the first real task):** what is an allowed map between GU boundary
  objects? Candidates to test: Krein-isometric inclusions; sector-restriction maps; `P_ghost`-equivariant
  linear maps. The morphisms must compose and carry identities (a category), and must be the arrows the
  physics deems structure-preserving.
- **Composition + identity:** to be defined and checked, exactly as T41 checked them for `D1Cat`.

**Finding:** the adapter cannot be a functor until `GUBdy` is defined as a category. That is precisely the gap
CT-1 exposes — and it is a definite, bounded mathematical task, not prose.

## The functor `F : GUBdy -> D1Cat` (what must be specified and checked)

- **On objects:** send a GU boundary sector to its capability object — e.g. the mirror (`W-`) sector to
  `C(R)`'s **collective complement** (the content accessible collectively, not individually), per the mirror
  bridge hypothesis (`gu-formalization/.../mirror-as-collective-capability-boundary-2026-07-07.md`).
- **On morphisms (the part the prose omits):** `F` must send each `GUBdy`-morphism to a `D1RestrictionMorphism`
  **preserving composition and identity** — `F(g . f) = F(g) . F(f)`, `F(id) = id`. This functoriality is the
  content; an object-only assignment is not a functor and is exactly the analogy-grade state we are leaving.
- **Non-triviality (the categorical form of the two-adapter gate):** `F` must be **non-constant** (it must not
  collapse all boundary objects to one capability object — a constant functor "connects" everything and proves
  nothing, the categorical form of the discriminating control). "Two adapters prove out" becomes: exhibit `F`
  **and** a companion functor (a `G` back, or an independent second functor into a different verified target),
  neither constant; the strong target is an **adjunction** `F -| G` or an **equivalence on a subcategory**
  (which would be the honest cash-out of "same boundary, two faces").

## What this buys

It converts "is the mirror the collective-capability boundary?" (analogy grade, no adapter after weeks) into a
**definite question**: *is there a non-constant functor `F : GUBdy -> D1Cat` sending the `W-` sector to `C(R)`'s
collective complement, functorial on morphisms, with a companion adjoint/inverse?* That question has a yes/no
shape, a discriminating control (constant functors are refused), and a first buildable step.

## First concrete step (bounded — this is Thread B from the Gorard mapping, now definite)

1. **Define `GUBdy` as a category:** choose the objects (boundary sectors) and, critically, the **morphisms**;
   check composition + identity on a finite fixture (reuse the T12'/ghost-parity carrier
   `gu-formalization/tests/big-swing/t12p_mirror_capability_wall.py` for the objects).
2. **Define `F` on objects and morphisms** and **check functoriality** on that fixture (the T41 harness,
   `models/typed_transport_category.py`, is the template — it already verifies category/functor laws on finite
   D1 systems).
3. Only then ask about non-triviality, a companion functor, and adjunction. Do **not** assert "the adapter" in
   prose again until step 2 typechecks.

## First build result (2026-07-07) — `models/boundary_adapter_functor.py`, exit 0

Built and ran. **`GUBdy` is a category and `F : GUBdy -> D1Cat` is a well-defined functor into the PROVEN
`D1Cat`** — and the controls make the result honest and self-critical:

- **Source category built:** `GUBdy` = the poset `{W+0 < W+ < W, W-}` of Krein sub-sectors, morphisms =
  K-isometric inclusions (signature monotone along each). Composition closure and identities hold. The chain
  `W+0 <= W+ <= W` gives a non-trivial composite to test.
- **`F` into the real `D1Cat`:** every `F(object)` is a valid `D1RestrictionSystem`; every `F(inclusion)` is a
  reached `D1RestrictionMorphism`; **composition and identity are preserved** (checked with the actual T41
  machinery `_compose_morphisms` / `morphisms_equal_modulo_name` / `analyze_morphism`). The action-on-morphisms
  the contract's `S`/`R` prose omitted is now supplied.
- **Profiles grounded, not asserted:** a mini-T12' fixes `accessible_support(mirror) = 0` (individually
  invisible) and `accessible_support(physical) = 1`. *Honest caveat:* the individual-invisibility leg here is
  **analytic** (a W+-supported observable depends only on the W+ component, so two states sharing their W+ part
  are indistinguishable to it); the full empirical zero-trace over random accessible operations is the
  192-dim T12' (`gu-formalization/tests/big-swing/t12p_mirror_capability_wall.py`), not re-run in this fixture.

**The decisive finding (why a passing functor is NOT the adapter): functoriality is
NECESSARY-NOT-SUFFICIENT.** Two controls fire:

1. A **constant** functor (every object -> one system, every morphism -> its identity) **also passes**
   functoriality — it "connects everything" and proves nothing. What separates the real `F` from it is
   **faithfulness** (the real `F` distinguishes the two boundary faces `F(W+<=W) != F(W-<=W)`; the constant
   functor collapses them).
2. A **physics-wrong** functor (`mirror.accessible_support = 1`, contradicting T12') **also passes**
   functoriality and validity — so the functor axioms **do not enforce the physics**; the T12' grounding is
   *extra content* on top of functoriality.

**So the adapter's real content, now named by construction, is: (i) FAITHFULNESS + (ii) PHYSICS-GROUNDING
(profiles FORCED by T12', not chosen), plus (iii) a companion adjoint/inverse (the two-adapter gate).** This
is the CT-2 lesson applied to itself: functoriality is the "pushout-easy" part; the content is the harder
limit-side (faithfulness / forced structure). The build advanced #1 from prose to a definite object and
**located the next requirement**; it did not close the adapter, and no claim moved.

## Guards

- **No claim moves.** This is a spec; `F` is not built. The finding "`GUBdy` is not yet a category" is the
  honest first result.
- **Manufactured-convergence, categorical form:** a constant functor, or one factoring through a trivial
  category, "connects" everything and proves nothing — refuse it exactly as the Z/3-gate refused the
  "both mod-3" method.
- **Tri-repo discipline:** cross-repo material is stress-test input; building `F` does not move GU's or TaF's
  ledger; the two-adapter gate stands (now stated as "two non-constant functors, ideally adjoint").
- **Single-process caution.** Source and target being co-developed under one process, an exhibited functor is
  weaker evidence than one arrived at independently; the functoriality check is the discipline, not the
  elegance.

## Cross-links

- Sharpens `open-problems/gu-ti-taf-reciprocal-bridge-contract.md` Section 5 (`S`, `R` as functors, with
  action-on-morphisms and non-triviality supplied).
- Target category: `models/typed_transport_category.py` (T41, `D1Cat` proven); capability object C(R),
  T392/T395.
- Object content + the collective-complement reading: `gu-formalization/explorations/time-as-finality-crosswalk/
  mirror-as-collective-capability-boundary-2026-07-07.md`; carrier `t12p_mirror_capability_wall.py`.
- Method: CT-1 in `ai-epistemology/field-guide/branch-5-evolvability/category-theoretic-method-correctives.md`;
  Gorard mapping Thread B in `explorations/gorard-three-insights-repo-mapping-2026-07-07.md`.
