# T504 - Boundary-Adapter Source-Category Functor Gate - v0.1 results

> Admission gate only. No claim-ledger, roadmap, README, North Star, public-posture, hard-policy, external-publication, or cross-repo truth movement.

- Spec: `tests/T504-boundary-adapter-source-category-functor-gate.md`
- Model: `models/boundary_adapter_source_category_functor_gate.py`
- Tests: `tests/test_boundary_adapter_source_category_functor_gate.py`
- Source open problem: `open-problems/boundary-adapter-as-functor-spec-2026-07-07.md`
- Target-category anchor: T41 / `models/typed_transport_category.py`
- Artifact JSON: `results/T504-boundary-adapter-source-category-functor-gate-v0.1.json`

## Overall verdict: BOUNDARY_SOURCE_CATEGORY_FUNCTOR_GATE_BUILT_REVIEW_ONLY

T504 does not build the real GU/TaF adapter. It builds the TaF-side admission gate for such an adapter. A synthetic finite boundary-sector category can map non-constantly into D1Cat and satisfy functor laws, which proves the check is executable. Object-only bridges, missing source morphisms, constant functors, bad composition maps, W-minus mis-targeting, and cross-repo shortcut packets are rejected or blocked.

## Decisions

| Packet | Admitted? | Label | Missing requirements | Blocked shortcuts |
| --- | --- | --- | --- | --- |
| synthetic_sector_restriction_functor | yes | ADMITTED_SOURCE_CATEGORY_FUNCTOR_REVIEW_TARGET | none | none |
| object_only_mirror_bridge | no | REJECTED_OBJECT_ONLY_NOT_A_FUNCTOR | morphism_map | none |
| missing_source_morphisms | no | REJECTED_SOURCE_CATEGORY_NOT_BUILT | source_category | none |
| constant_functor_control | no | REJECTED_CONSTANT_FUNCTOR_CONTROL | nonconstant_functor, w_minus_collective_complement_target | none |
| bad_composite_morphism_map | no | REJECTED_FUNCTOR_LAW_FAILURE | functor_laws | none |
| w_minus_wrong_target | no | REJECTED_WRONG_W_MINUS_TARGET | w_minus_collective_complement_target | none |
| sibling_truth_shortcut | no | BLOCKED_CROSS_REPO_OR_GOVERNANCE_SHORTCUT | none | cross_repo_truth_movement, sibling_repo_truth_dependency |

## Target Category Anchor

- T41 forms proper category: `True`
- T41 category laws hold: `True`
- PO1 is functor to Bool: `False`

## Future Packet Minimum

- declare boundary-sector objects inside a named source category
- declare source morphisms that compose and have identities
- map every source object to a D1Cat object or declared D1 subcategory object
- map every source morphism to a D1RestrictionMorphism
- prove F(id) = id and F(g;f) = F(g);F(f) on the finite fixture
- show the functor is non-constant on objects or nonidentity morphisms
- send the W-minus or mirror-sector object to the declared collective-complement target
- include constant-functor, object-only, and bad-composition hostile controls
- keep admission review-only until sibling repo source-category truth is supplied by that repo

## What This Does Not Earn

- real GU source category
- real GU/TaF adapter
- two-adapter gate
- adjunction or equivalence
- mirror equals collective-capability boundary
- category theorem beyond the finite synthetic fixture
- claim-ledger movement
- roadmap movement
- README movement
- North Star movement
- public-posture movement
- hard-policy movement
- external publication
- cross-repo truth movement
