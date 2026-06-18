# D1Cat Recovery Morphism Audit

**Status:** Exploration note. No claim update. No new theorem.
**Date:** 2026-06-18
**Prompted by:** TS-PERSONA-SPRINT-001 finding that H1 (TypedTransportNetwork)
has no defined mechanism for upward recovery propagation once forgotten_dims
are non-empty.

**Audit question:** Does the existing D1Cat categorical structure already
answer part of this, or is "recovery" genuinely outside the current static
formalism?

---

## Q1. Can a morphism from an obstructed system to an unobstructed system already be defined?

Yes. A `D1RestrictionMorphism` requires only: a source system, a target system,
a site_map, preserved_dimensions, and two boolean flags. Nothing in the type
definition prevents source from being obstructed and target from being
unobstructed.

The relevant flag is `require_obstruction_preservation`. If `True`, validation
(MorphismAnalysis) will flag that the morphism violates its declared constraints.
If `False`, the morphism is syntactically well-formed even with source obstructed
and target unobstructed.

In D1Cat, such a morphism is a valid arrow. The category has no built-in
constraint that arrows preserve obstruction status; that constraint is optional
and declared per-morphism.

---

## Q2. What does that morphism mean structurally?

A morphism f: A_obstructed → B_unobstructed with `require_obstruction_preservation=False`
is structurally a site map that happens to connect an obstructed system to an
unobstructed one, preserving a declared subset of D1 dimensions.

In PO1 terms, this is not a PO1 instance: AC6 requires the target to be obstructed,
which B_unobstructed is not. The morphism fails AC6 and is not classifiable as a
projection-obstruction case.

Structurally, it could represent several things: a coarsening that drops the
constraints causing obstruction, an aggregation to a summary level where the
conflict doesn't exist, or an arbitrary structural map with no physical motivation.
The morphism type does not distinguish between these possibilities.

---

## Q3. Under what conditions could such a morphism be interpreted as "recovery"?

For f: A_obstructed → B_unobstructed to be interpreted as recovery, three
conditions would need to hold simultaneously:

(a) **Same-system identity**: A_obstructed and B_unobstructed represent the same
    physical system at different moments, not two structurally different systems.

(b) **Semantic annotation of change**: the morphism represents a state transition,
    not a structural projection. The site_map tracks *what changed*, not *what
    was lost in projection*.

(c) **Before/after temporal order**: there is a declared t₁ < t₂ such that
    source is the state at t₁ and target is the state at t₂.

The current formalism has none of (a), (b), or (c). D1RestrictionSystems have
no time index. D1RestrictionMorphisms have no semantic tag distinguishing
"projection" from "evolution." The `forgotten_structure` field names what was
lost in projection, not what changed within a system.

A morphism f: A_obstructed → B_unobstructed can be constructed; it cannot be
interpreted as recovery without external annotation that the current types do
not carry.

---

## Q4. What additional data would distinguish the four interpretations?

| Interpretation         | What is currently present             | What is missing                                     |
|------------------------|---------------------------------------|-----------------------------------------------------|
| Arbitrary structural map | site_map, preserved_dims, flags     | Nothing — this is already definable                 |
| Projection (PO1)       | AC1-AC7 checked by check_admissibility | Nothing for this direction — PO1 is already defined  |
| Re-propagation         | The morphism f can be re-applied to A_t2 | A time index and same-system identity across t1/t2  |
| Repair                 | site_map exists                        | Site-level annotation of which constraints were resolved |
| Recovery over time     | A morphism from obstructed to unobstructed is definable | t₁ < t₂, same-system identity, semantic tag distinguishing evolution from projection |

The minimum additional data for recovery over time is: a pair (t, system_id)
attached to each D1RestrictionSystem so that two systems can be identified as
"same system at different moments" rather than "two different systems." Without
this, there is no way to distinguish a projection f: A→B (where A ≠ B structurally)
from an evolution f: A_t1→A_t2 (where A_t1 and A_t2 are the same system updated).

This is a **type-level gap**, not an operation-level gap. The operation of applying
a morphism is already defined. What's missing is a semantic tag on the objects,
not a new operation on the morphisms.

---

## Q5. Does any current claim require temporal recovery propagation?

Reviewing the claims in CLAIM-LEDGER.md, HYPOTHESES.md, and the theorem ladder:

- **D1**: defines a static componentwise preorder. No temporal evolution.
- **H1 (Record Reconstruction)**: asks whether temporal partial order can be
  *inferred* from existing record configurations — a static inference problem.
- **H7 (Finality-Induced Direction)**: derives a temporal direction from
  D1-monotone admissibility — but this is a property of the morphism structure,
  not a claim about how individual systems evolve over time.
- **T34 (PO1 Chain Theorem)**: endpoint admissibility is independent of
  intermediate admissibility — purely structural.
- **T40 (Holonic Emergence)**: holonic obstruction arises from cross-level
  constraints even when micro nodes are satisfiable — static snapshot claim.
- **T41 (Category Theorem)**: D1RestrictionMorphisms form a proper category —
  purely structural.

No current claim requires tracking how a system recovers from obstruction over
time. All existing claims are about configurations and their structural
relationships, not about sequences of configurations or state evolution.

---

## Q6. Preserve the current static scope boundary.

The audit supports preserving the static scope boundary. No current claim is
inexpressible in static terms. The inability to track "upward recovery
propagation" is not a missing operation — it is the correct scope for a
mathematics of structure.

The formalism correctly describes what is present, what is forgotten, what can
glue, and what cannot be recovered **at a moment in time**. Questions about
what happens before and after that moment are outside its current scope, and
that scope is appropriate given the claims being investigated.

---

## Q7. What would the smallest temporal extension be, if it ever became necessary?

This is hypothetical — no current claim requires it. Documented here for
future reference only.

The minimum extension would not be a new operation. It would be a type-level
annotation: a `system_identity: str` field on `D1RestrictionSystem` and a
`step: int` field (or similar ordering). Two systems with the same
`system_identity` and different `step` values could then be declared to be
"the same system at different moments," making a morphism between them
interpretable as evolution rather than projection.

This is the smallest change because it does not alter any existing operation:
`_compose_morphisms`, `check_admissibility`, `global_section()`, and all
existing category machinery remain unchanged. It only adds semantic metadata
that allows two morphisms with the same structure to be classified differently
depending on whether source and target share a system identity.

Whether this extension is warranted depends entirely on whether a future claim
requires asserting something about sequences of configurations rather than
about individual configurations. That moment has not arrived.

---

## Summary

| Question | Answer |
|----------|--------|
| Can a morphism f: A_obstructed → B_unobstructed be defined? | Yes |
| What does it mean structurally? | An arbitrary structural map; not PO1; semantically ambiguous |
| Can it be interpreted as recovery? | Not without additional data (same-system identity, temporal order) |
| What data would distinguish recovery from projection? | A system_identity tag and temporal ordering on objects — a type-level addition, not a new operation |
| Does any current claim require temporal recovery? | No |
| Should the static scope boundary be preserved? | Yes |
| What is the smallest temporal extension if needed? | system_identity + step annotation on D1RestrictionSystem; no new operations required |

**The gap identified by TS-001 is real but correctly scoped.** "Recovery" is a
temporal concept. D1Cat is a category of static structural snapshots. The
inability to express recovery in D1Cat is not a missing operation — it is the
boundary of the formalism's scope, and that boundary is currently maintained
correctly.
