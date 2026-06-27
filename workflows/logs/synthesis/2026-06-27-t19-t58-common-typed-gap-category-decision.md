---
document_type: synthesis_decision
primary_reader: governance
read_pattern: current_state
write_pattern: append
authority: non_authoritative
summarizable: true
source_queue_item: 10
owner_line: RL-001
support_line: RL-005
claim_status_change: none
---

# T19/T58 Common Typed Gap Category Decision

## Status

Non-authoritative synthesis artifact for queue item 10 in
`workflows/logs/best-next-move/2026-06-27-next-10-research-orchestration.md`.
This file records a bounded decision and protocol. It does not edit
`CLAIM-LEDGER.md`, `ROADMAP.md`, code, tests, results, or open-problem files.

## Read Surfaces

- `ROADMAP.md`: T92 blocker and the T56/T57/T58 gap-presheaf track.
- `CLAIM-LEDGER.md`: C1 and D1-Field rows, plus the T57 and T92 change-log
  entries.
- `workflows/registries/line-registry.md`: RL-001 primary owner and RL-005
  support context.
- `open-problems/accessible-witness-gap-restriction-theorem.md`.
- `open-problems/first-person-finality-complexity-separation.md`.
- `tests/T19-phenomenal-bridge-complexity-separation.md`.
- `tests/T56-sheaf-cohomology-apparent-finality.md`.
- `tests/T57-finality-reflection-property.md`.
- `tests/T58-gap-phantom-equivalence.md`.
- `tests/T89-accessible-witness-gap-lemma.md`.
- `tests/T92-accessible-witness-gap-restriction.md`.
- Results and technical reports for T56/T57/T58/T92 where present.

## Decision

T19 proposition-domain gaps and T58 order-pair gaps share a common typed
degree-0 gap schema. They are not the same presheaf, not the same section
object, and not merely a loose analogy.

Classification:

```text
degree-0 typed gap object/category, with presheaf-candidate behavior only after
the section sort and restriction maps are declared and the closure hypotheses
are checked.
```

The common object is not:

```text
one untyped presheaf whose sections are both R_self_finality propositions and
event-order pairs.
```

The common object is:

```text
a typed finite gap system (P, Patch, rho, A, F, G) where G(U)=A(U)-F(U),
A is ambient/third-person or ambient/event content, F is local/auditable or
apparent content, and restriction closure is licensed by explicit hypotheses.
```

The shared structure is H0/degree-0 "ambient content present, local content
missing" behavior. The section sorts remain distinct:

- T19/T89/T92: unary typed propositions, such as `R_obs` and
  `R_self_finality`.
- T56/T57/T58: non-reflexive event-order pairs, such as
  `(e1_A_locking, e3_composite_locking)`.

## Formal Schema TG0

A finite typed degree-0 gap system is a tuple:

```text
X = (Patch_X, P_X, type_X, rho_X, A_X, F_X, G_X)
```

with:

- `Patch_X`: a finite poset of observer patches.
- `P_X(U)`: a finite typed section domain at each patch.
- `type_X`: a stable type assignment for sections.
- `rho_X(U,V)`: restriction maps for `V subset U`, defined only when the
  restricted section remains expressible at `V`.
- `A_X(U) subset P_X(U)`: ambient content restricted to patch `U`.
- `F_X(U) subset P_X(U)`: local/auditable/apparent content at patch `U`.
- `G_X(U) = A_X(U) - F_X(U)`: the degree-0 gap.

The well-formedness gates are:

1. Ambient restriction: `rho(A(U)) subset A(V)` for `V subset U`.
2. Local reflection/audit monotonicity: local/auditable content cannot appear
   only by shrinking the patch unless a boundary control is being exhibited.
3. Stable typing: restriction does not relabel one section type as another.
4. Extension compatibility: `F(U) subset A(U)` when interpreting gaps as
   missing ambient content rather than local/ambient conflict.
5. Non-circular construction: `F` and `G` are not defined by post hoc deletion
   of the desired gap.
6. Closure not surjectivity: smaller-patch gaps need not lift to larger patches.

A morphism in the common category is a type-preserving patch/section map that
commutes with restrictions and preserves the `A`, `F`, and `G=A-F` structure.
Semantic relabeling morphisms are not admissible unless declared as collapse
maps, in which case they are boundary controls rather than evidence.

## Object Mapping

| Artifact | Typed section domain | `A(U)` | `F(U)` | `G(U)` | TG0 status |
| --- | --- | --- | --- | --- | --- |
| T19 | Propositions about observer R | Ambient full-graph truth over `P_R` | Propositions auditable from R's accessible holders | `R_self_finality` at the internal patch | Degree-0 accessible-witness instance, finite witness only |
| T56 | Event-order pairs | Ambient/global order restricted to a patch | Locally computed apparent order | Phantom pair at the hidden-intermediary patch | H1 route rejected; H0 gap route proposed |
| T57 | Event-order pairs | Same T56 ambient order | Same T56 apparent order with Finality Reflection Property | Restriction-closed gap assignment | Finite closure audit for T56-style gaps |
| T58 | Event-order pairs in T51/T52 observer views | Event-finality/colimit order | Observer-local apparent order | Exactly the independently reported phantom incomparability pair in tested views | Bounded equivalence under `F(U) subset A(U)` |
| T92 | Typed propositions | Ambient/third-person proposition object | Locally auditable proposition object | Accessible-witness proposition gap | Conditional finite theorem witness with explicit boundaries |

This mapping requires type tags. Without type tags, the proposed common object
would have to identify proposition sections with order-pair sections by hand,
which the semantic-relabeling control explicitly blocks.

## Controls

| Control | Source | Expected role | Current outcome |
| --- | --- | --- | --- |
| Non-chain witness | T92 `non_chain_joint_witness_gap` | Shows the proposition-domain theorem is not only the original T19 chain | Passes gap closure under ambient restriction, audit monotonicity, and stable typing |
| Semantic relabeling | T92 control | Blocks hand-built identification of `R_self_finality` with `R_obs` | Fails gap closure as intended |
| Audit monotonicity violation | T92 control | Shows closure depends on witness monotonicity | Fails gap closure as intended |
| Generic complement counterexample | T57 | Shows complements are not automatically presheaves | FRP fails and complement closure fails |
| Local reversal | T58 hostile control | Separates missing ambient order from local/ambient conflict | `G` is nonempty but not a phantom incomparability |
| Non-lifting examples | T57/T92 | Separates closure from surjectivity | Smaller-patch gaps need not lift |

## Acceptance Criteria Satisfaction

| Queue acceptance criterion | Satisfaction |
| --- | --- |
| Map T19, T56, T57, T58, and T92 objects into one proposed schema or prove why one field cannot be common without semantic hand-building | Satisfied. TG0 maps all five into one typed degree-0 gap schema. A single untyped field is rejected because it would require semantic relabeling across section sorts. |
| Include at least one non-chain witness and one semantic-relabeling control | Satisfied. T92 `non_chain_joint_witness_gap` is the non-chain positive control; T92 `semantic_relabeling_control` is the hostile control. |
| State whether the result is a degree-0 gap object, a presheaf candidate, or an analogy-only boundary | Satisfied. Result is a degree-0 typed gap object/category. It is a presheaf candidate only after typed restrictions and closure hypotheses are checked. It is not analogy-only. |
| Avoid consciousness, complexity-class, H1/cohomology, or phenomenal-bridge upgrades | Satisfied. The decision uses finite records, typed sections, restrictions, and gap closure only. No C1 upgrade, no complexity-class placement, no H1 theorem, and no phenomenal explanation is claimed. |

## No-Promotion Guardrails

- C1 remains `weakened`; D1-Field remains `partially_supported`.
- Do not claim a solution to consciousness or the phenomenal bridge.
- Do not claim `FIRST-PERSON-FINALITY` has been placed in a complexity class.
- Do not claim a general H1/cohomology theorem. T56 explicitly moved the live
  invariant to H0/degree-0 gap behavior for the tested cover.
- Do not identify T19 proposition gaps with T58 order-pair phantom gaps. They
  are distinct typed instances.
- Do not use raw `G=A-F` without the extension gate `F(U) subset A(U)` when
  interpreting order-pair gaps as phantom incomparability.
- Do not use semantic relabeling to force a common object.
- Do not upgrade finite witness audits to arbitrary-observer, arbitrary-cover,
  or arbitrary-presheaf theorems.

## Durable Protocol For Future Work

A future formalization can promote TG0 from synthesis schema to theorem only if
it proves the following finite lemma with explicit quantifiers:

```text
For any finite typed gap system X satisfying ambient restriction, stable typing,
local reflection/audit monotonicity, and extension compatibility, G(U)=A(U)-F(U)
restricts contravariantly: rho_{U,V}(G(U)) subset G(V).
```

It must then show that:

1. the T56/T57/T58 order-pair systems instantiate the lemma;
2. the T19/T89/T92 proposition systems instantiate the lemma;
3. semantic relabeling, audit-monotonicity failure, and local reversal remain
   failing controls;
4. the conclusion is only a typed degree-0 gap theorem, not a C1 status change.
