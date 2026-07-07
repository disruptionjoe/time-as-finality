# T492 - Typed Gap Category Bridge - v0.1 results

> Finite typed-schema bridge only. `CLAIM-LEDGER.md`, `ROADMAP.md`, `README.md`, North Star files, public posture, hard policy, and cross-repo truth are untouched.

- Spec: `tests/T492-typed-gap-category-bridge.md`
- Model: `models/typed_gap_category_bridge.py`
- Tests: `tests/test_typed_gap_category_bridge.py`
- Artifact JSON: `results/T492-typed-gap-category-bridge-v0.1.json`
- Sources: T92, T113, T89, and the gap-presheaf / accessible-witness open problems

## Overall verdict: COMMON_TYPED_GAP_SCHEMA_SUPPORTED_OBJECT_IDENTITY_BLOCKED

T113 and T92 share a common finite typed-gap schema, but not the same section object, classifier, or theorem target. The useful abstraction is a typed gap-system interface: A, F, G, restriction, and an admissibility predicate tau. The target interpretation stays domain-specific.

## Abstract Schema

- finite patch family with restriction maps
- ambient object A(U) of content fixed by the larger system
- local or auditable subobject F(U) with a declared inclusion into A(U)
- gap object G(U)=A(U)-F(U) or its typed subobject
- typed admissibility predicate tau selecting meaningful gap sections
- restriction closure rho(tau(G(U))) subset tau(G(V)) for V subset U
- domain-specific target interpretation kept outside the schema

## Instance Summary

| Instance | Carrier | Target | Positive count | Controls | Raw-gap status |
| --- | --- | --- | ---: | ---: | --- |
| t113_order_pair_phantom_gap | nonreflexive_order_pair_sections | phantom_incomparability_witnesses | 10 | 10 | raw H0(G) refuted as classifier |
| t92_unary_accessible_witness_gap | unary_typed_proposition_sections | accessible_witness_unauditability_gaps | 7 | 2 | not a raw T58 order-pair object; T92 uses typed proposition gaps |

## Candidate Evaluation

| Candidate | Admitted? | Label | Reason |
| --- | --- | --- | --- |
| common_minimal_typed_gap_schema | yes | ADMITTED_COMMON_TYPED_GAP_SCHEMA_NO_IDENTITY | Both branches instantiate the same minimal finite schema while keeping carrier kind, target kind, and typing predicates distinct. |
| raw_h0_gap_identity | no | REJECTED_RAW_H0_REFUTED_BY_T113 | raw_h0_refuted_by_t113 |
| same_section_object_identity | no | REJECTED_CARRIER_MISMATCH | carrier_mismatch |
| cohomology_or_physical_torsion_promotion | no | REJECTED_COHOMOLOGY_TORSION_PROMOTION_BLOCKED | cohomology_torsion_promotion_blocked |
| consciousness_or_complexity_promotion | no | REJECTED_CONSCIOUSNESS_COMPLEXITY_PROMOTION_BLOCKED | consciousness_complexity_promotion_blocked |
| semantic_relabeling_as_bridge | no | REJECTED_CARRIER_MISMATCH | carrier_mismatch |
| local_reversal_as_gap | no | REJECTED_RAW_H0_REFUTED_BY_T113 | raw_h0_refuted_by_t113 |

## Why Identity Is Blocked

- T113 carriers are nonreflexive ordered event-pair sections; T92 carriers are unary typed proposition sections.
- T113 classifies phantom incomparability witnesses; T92 classifies accessible-witness unauditability gaps.
- T113's typing rule is endpoint/canonical/local-incomparability; T92's typing rule is ambient-restriction/audit-monotonicity/stable-proposition-typing.
- T113 refutes raw H0(G) as too broad, so a raw-gap identity cannot be the bridge.
- T92 explicitly blocks identifying T19 proposition gaps with T58 order-pair gaps.

## What this earns / does not earn

Earns: a conservative typed-gap schema shared by T113 and T92, useful as a future bridge checklist.

Does not earn: section-object identity, raw H0 classification, a general category theorem, cohomology, physical torsion, consciousness or complexity-class claims, claim-ledger movement, public posture, or cross-repo support.

Honest ceiling: Finite typed-schema bridge only. T492 supports a common typed-gap schema for T113 order-pair phantom gaps and T92 unary proposition gaps, but blocks object identity, raw H0(G) classification, a general cohomology theorem, physical torsion language, consciousness claims, complexity-class claims, claim-ledger movement, public posture, and cross-repo support.

## Open Blocker

T492 does not prove a general category theorem. A future result would need explicit morphisms between typed gap systems and a natural transformation or equivalence theorem, not just two instances of a schema.

## Recommended Next

- Use the typed-gap schema as a checklist for future T19/T58 bridge attempts.
- Do not use raw H0(G), physical torsion, cohomology, consciousness, or complexity-class language from T492.
- If this branch continues, define morphisms between typed gap systems and test a third carrier kind.
