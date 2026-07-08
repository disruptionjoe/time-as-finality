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

## TaF-side admission gate: T504

T504 (`tests/T504-boundary-adapter-source-category-functor-gate.md`) turns the same CT-1 burden into a
repo-local executable admission gate:

```text
BOUNDARY_SOURCE_CATEGORY_FUNCTOR_GATE_BUILT_REVIEW_ONLY
```

T504 deliberately does **not** inspect sibling repos or assert their source-category truth. It uses a finite
synthetic boundary-sector fixture only to prove that the TaF-side check is executable against the T41 `D1Cat`
target. The gate admits one synthetic non-constant functor as a review target and rejects or blocks object-only
bridges, missing source morphisms, constant functors, bad composite morphism maps, wrong W-minus targets, and
sibling-repo/cross-repo shortcut packets.

The remaining burden is therefore sharper: a future real bridge packet must supply source-owned boundary
objects and morphisms, prove functor laws into `D1Cat` or a declared D1 subcategory, include constant/object-
only/bad-composition controls, and keep the result review-only until source-category truth is supplied by the
owning surface. T504 earns no real GU source category, real GU/TaF adapter, two-adapter gate, adjunction,
equivalence, mirror-boundary claim, or claim/public-posture movement.

## Second build result (2026-07-07) — faithfulness + adjoint, `models/boundary_adapter_functor_faithfulness.py`, exit 0

The named next legs, built and run. A subtlety first: `GUBdy` is a THIN category (a poset), so plain
faithfulness is automatic; the property that carries content is **ORDER-REFLECTION** (a D1 morphism
`F(A)->F(B)` exists IFF `A<=B`). An order-reflecting + injective-on-objects functor is an ORDER-EMBEDDING.

- **FAITHFULNESS LEG — PROMOTED on the physics-critical distinction, and it UNIFIES with physics-grounding.**
  `F` order-reflects the physical-vs-mirror FACE distinction: no mismatch involves `W-`, and `F(W-)->F(W+)`
  does NOT exist — the two boundary faces are reflected as incomparable. This holds PRECISELY because T12'
  gives `mirror.accessible_support = 0`, and the PHYSICS-WRONG functor (`mirror.accessible=1`) now FAILS it
  (a spurious `F(W-)->F(W+)` appears). So order-reflection is the exact property that functoriality missed in
  the first build, and the physics is what supplies it — the "faithfulness" and "physics-grounding" next-legs
  are **ONE leg**.
- **THE PRECISE LIMIT (a real finding, surfaced by the check, not a clean pass).** `F` is NOT a FULL
  order-embedding: its ONLY order-reflection failure is the pure-physical DIMENSION collapse `F(W+)->F(W+0)`.
  The flat per-site capability profile is blind to redundant identical physical directions, so D1 morphisms
  collapse the physical sector onto its sub-sector. Named fix: the capability object must carry sub-sector
  DIMENSION in a morphism-respecting way (profile-exact preservation makes this a genuine design question
  about what "restriction" means for capability). The mirror face is unaffected — the physics protects it.
- **ADJOINT / SECOND-ADAPTER LEG — PARTIAL.** `G = F^{-1}` gives `G o F = id` on objects and an order-iso only
  for the FACE poset `{physical, mirror, full}`; `F` is FAITHFUL-NOT-FULL into `D1Cat` (2 morphisms
  `F(W+0)->F(W+)` vs 1 in `GUBdy`). So this is ONE adapter (F and its inverse onto a non-full image), NOT the
  two INDEPENDENT adapters the tri-repo gate requires; a genuine reflection `G : D1Cat -> GUBdy` on all of
  `D1Cat` is unbuilt. The two-adapter gate is NOT closed.

Net after both builds: the adapter is a definite object that reflects the individual<->collective FACE
distinction **physics-forcedly** (the real content, and the physics is what makes it faithful), is blind to
within-face dimension (named fix), and stands as **ONE of the two** required adapters. The remaining
requirement is now precise: (i) a dimension-carrying capability encoding to make `F` a full embedding, and
(ii) a SECOND, INDEPENDENT adapter (e.g. via TI issuance or independent physics). No claim moved; no identity
asserted.

## Second INDEPENDENT adapter (2026-07-07) — the TI side, `models/boundary_adapter_second_ti.py`, exit 0

The two-adapter gate requires a SECOND adapter that is INDEPENDENT of the first (not F and its inverse). Built
from the TI side and grounded in TI's OWN forcing, not GU's:

- **The independent forcing:** TI's E002 bridge toy model, fixture **F2 (Same Records, Different Hidden
  Issuance)**, shows a source difference in a hidden constraint `h not in A_i` leaves ZERO trace on the
  individual observer's records — TI's own zero-trace / T395 signature, reached through source-realization
  logic, NOT Krein positivity. So `S : TIsrc -> D1Cat` forces `hidden.accessible = 0` via F2, exactly as
  `F` forces `mirror.accessible = 0` via T12'. **Two different primitives, same signature.**
- **Checked:** `S` is a functor into the same proven `D1Cat`; it order-reflects the accessible-vs-hidden FACE
  (forced by F2 — a TI-WRONG `S` with `hidden.accessible=1`, i.e. F2 refuted, FAILS it); `F` and `S` COHERE
  (land on the same D1 objects under the iso `physical<->accessible`, `mirror<->hidden`); and the agreement is
  FALSIFIABLE (the TI-wrong `S` disagrees with `F`), so it is not vacuous.
- **HONEST CAVEAT — gate ADVANCED, NOT CLOSED.** Both adapters were built by ONE process in ONE encoding
  (the D1 profile convention, the shared poset shape). Per the registry's de-correlation test, TRUE
  independence needs genuinely de-correlated processes. So this is **independent-forcing within one program** —
  stronger than one adapter, weaker than external independent arrival. **The identity "GU boundary = TaF
  capability = TI source" is NOT licensed.** Remaining to close: (i) the dimension-carrying encoding (build 2's
  fix), (ii) genuine DE-CORRELATION of the two adapters, (iii) the still-uncomputed mu<->boundary and
  records-vs-redundancy legs. Adapter tally: **2 of 2 built and coherent, both physics/logic-forced;
  de-correlation pending.**

## De-correlation, made concrete (2026-07-07) — the observer/system gauge

"De-correlation" (the remaining requirement to close the two-adapter gate) was vague; the observer/system
gauge makes it precise. To collapse the multiway to one thread an observer makes path-equivalences, so
`(computation done by the system) + (computation done by the observer) = observed behavior`, and only the
total is observable — **the split is a gauge freedom** (Gorard; see
`explorations/physics-from-a-finite-observer-and-the-observer-system-gauge-2026-07-07.md`). That gauge is the
**manufactured-convergence knob**: one could attribute the individual<->collective boundary to the system
(GU's Krein structure) or to the observer (the capability reading) and *tune the split* to force `F` and `S`
to agree.

So **de-correlation = fixing the observer/system gauge INDEPENDENTLY on each adapter**: `F` fixes it via GU
physics (T12' — a system-side forcing), `S` fixes it via TI source-logic (F2 — a different forcing). If the
two independently-set splits *coincide*, the agreement is real; if they secretly share one tunable knob, the
agreement is gauge (manufactured). The current build's honest status — "independent-forcing within one
process/encoding" — is exactly the statement that the two splits are *forced* but not yet *demonstrably
un-shared*; a genuinely de-correlated run (different models/framings, no shared brief, per the ai-epistemology
de-correlation test) is what would show the knob is not shared. **The capability bound (`C(R)`, the complexity
lower bounds) fences the gauge**: a finite observer cannot carry unbounded burden, so the split is free only
up to capability — which is why the forcing on each side is finite and checkable rather than freely tunable.

## TaF-side CT-3 dinosaur guard: T505

T505 (`tests/T505-observer-system-gauge-reality-gate.md`) makes the CT-3
correction executable:

```text
OBSERVER_SYSTEM_GAUGE_REALITY_GATE_BUILT_DINOSAUR_GUARD_REVIEW_ONLY
```

The gate separates three cases:

- proven equivalence or reversible presentation change: route to invariant-only
  treatment;
- lack of direct observability alone: reject as a verificationist gauge
  shortcut;
- unobservable but hard-to-vary, falsifiable explanatory structure: admit only
  as review material.

For the current boundary-adapter lane, T505 classifies the F/S state as
single-process independent forcing: stronger than one adapter because the GU
and TI sides supply different forcing sources, but still not de-correlated
because the build shares one process and one D1 encoding. Constant/trivial
convergence, shared tunable knobs, missing hard-to-vary burden, and
claim/public-posture/external/cross-repo shortcuts are rejected or blocked.

The current two-adapter gate is therefore still open. A future de-correlated
packet must independently fix the observer/system split on each adapter, rule
out a shared knob or shared brief, include falsifiable disagreement controls,
declare the finite capability bound, and remain review-only until a runnable
artifact earns a narrower update.

## TaF-side dimension-carrying embedding gate: T506

T506 (`tests/T506-boundary-adapter-dimension-carrying-embedding-gate.md`) makes
build 2's named dimension defect executable:

```text
DIMENSION_CARRYING_EMBEDDING_GATE_BUILT_REVIEW_ONLY
```

The flat D1 baseline still admits the spurious pure-physical collapse
`F(W+) -> F(W+0)`, so a plain per-site profile is not enough to make the
adapter a full order-reflecting embedding. A local synthetic dimension-carrying
encoding repairs that specific defect when it predeclares exact dimension
atoms, requires injective site maps, and preserves the physical/mirror face
kind. Under those constraints, the finite boundary-sector order is reflected
exactly: expected inclusions remain and non-source-order target morphisms are
blocked.

The hostile controls matter as much as the positive fixture. Cardinality-only
dimension counting can block the `W+ -> W+0` collapse while losing the
mirror/physical face guard under a physics-wrong mirror packet. Noninjective
"dimension" maps still allow the original many-to-one collapse. Post-hoc
dimension retuning, claim/public-posture shortcuts, external-publication
shortcuts, and cross-repo shortcuts are rejected or blocked.

This earns only a TaF-side admission pattern for a future dimension packet. It
does not supply real GU source-category truth, real TI source truth, real
adapter identity, de-correlated adapter arrival, two-adapter gate closure,
claim-ledger movement, or public-posture movement.

## Guards

- **No claim moves.** This remains an open-problem record. Fixture builds and TaF-side admission gates are
  review material; they do not close the real adapter or move ledgers.
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
