---
document_type: synthesis_preflight
queue_item: fifth_batch_5
status: complete
authority: non_authoritative
write_scope: workflows/logs/synthesis
claim_effect: none
source_open_problem: open-problems/functor-obl-taf-001-coherent-section-functor.md
source_results: tests/T190-coherent-section-functor-base-cases.md; tests/T192-lambda-star-derivation-from-po1-obstruction-dynamics.md; tests/T221-coherent-section-functoriality-verdict.md
---

# PO1-NCK F_partial ParSets Preflight

## Scope

This preflight states what a covariant partial-map repair would need to provide
after T221 refuted the covariant `FinSets` functor and proved only the
contravariant `FinSets` functor.

It does not build `F_partial`, prove a partial functor, promote PO1-NCK, or
promote `lambda*(S)`. The current ledger-safe reading remains:

```text
PO1 types K(lambda,S), not lambda*(S).
```

## Read Surfaces

- `open-problems/functor-obl-taf-001-coherent-section-functor.md`.
- `tests/T190-coherent-section-functor-base-cases.md`.
- `tests/T192-lambda-star-derivation-from-po1-obstruction-dynamics.md`.
- `tests/T221-coherent-section-functoriality-verdict.md`.
- `CLAIM-LEDGER.md` PO1-NCK row.

## Settled Starting Point

The following is not open in this preflight:

```text
F : States(Ext_S) -> FinSets is not a functor.
F_op : States(Ext_S)^op -> FinSets is a functor.
```

The covariant `FinSets` failure is not a composition nit. It is a morphism
typing failure: a section-killing extension can require a total function
`1 -> 0`, which does not exist in `FinSets`.

The only live route for a forward issuance formalism is therefore a different
codomain, for example:

```text
F_partial : States(Ext_S) -> ParSets
```

where arrows are partial maps, partial relations, or an explicitly chosen
equivalent partial-map category.

## Object To Freeze

A later ParSets run must freeze the category and object map before examples are
scored.

Minimum declaration:

```text
ParSets_category
objects: finite sets
morphisms: partial functions with declared domains of definition
composition: ordinary partial-function composition
identity: total identity partial function
undefined_behavior: deleted sections are undefined, not mapped to a new point
```

Then define:

```text
F_partial(S) = F(S)
```

and for an admissible extension `e : S -> S'`:

```text
dom(F_partial(e)) = { sigma in F(S) | sigma satisfies the added constraints of e }
F_partial(e)(sigma) = sigma, viewed as an element of F(S')
```

If the intended morphism can create new sections rather than only preserve or
delete old ones, the run must declare that as a different state-transition
semantics. It cannot be slipped into `Ext_S` while still relying on T221's
monotone constraint-addition result.

## Partial-Functor Laws To Check

The next executable must test, at minimum:

```text
F_partial(id_S) = id_{F(S)}
F_partial(e2 o e1) = F_partial(e2) o F_partial(e1)
```

under partial-function equality:

```text
same domain of definition
same value on every defined source section
same undefined source sections
```

The composition check must include:

```text
selective_survival_chain
total_obstruction_chain
non_obstructed_redundant_chain
mixed_delete_then_preserve_chain
```

The `total_obstruction_chain` is essential: it should become a partial map with
empty domain, not a fake total map into an empty set.

## Forward-Rate Burden

Even if `F_partial` is a lawful partial functor, that alone does not promote
PO1-NCK. The run must also show whether forward-rate data can be typed without
turning into either trivial deletion bookkeeping or generic optimal control.

Required rate fields:

```text
survival_domain_size(e,S)
deleted_section_count(e,S)
new_proposal_count(lambda,S)
obstruction_probability p_obs(S)
N(lambda,S)
C(lambda,S)
K(lambda,S)
```

Minimum honest interpretation:

```text
K(lambda,S) = lambda * |F(S)| * p_obs(S)
```

is PO1-native if `p_obs(S)` is defined by PO1 gluing obstruction. A nonzero
interior `lambda*(S)` still requires independently typed `N` and `C`.

## Controls

| Control | Expected behavior |
| --- | --- |
| Identity | Total identity partial map on every `F(S)`. |
| Redundant extension | Total partial map whose domain is all of `F(S)`. |
| Selective survival | Partial map defined exactly on surviving sections. |
| Total obstruction | Empty-domain partial map into the empty set. |
| Sequential deletion | Composite domain equals sections surviving every step. |
| Contravariant comparison | `F_op` remains the ordinary inclusion functor and is not confused with forward issuance. |
| Section-preserving subcategory | Functorial but dynamically sterile; cannot carry nontrivial `N` or `K`. |
| PO1-only objective | With no independent `N` or `C`, optimizer is boundary `lambda*=0`. |

## Acceptance Criteria

The next artifact is accepted as useful only if all of the following hold:

- It treats covariant `FinSets` functoriality as refuted, not pending.
- It defines the partial-map category before scoring examples.
- It defines domains of definition and undefined behavior explicitly.
- It proves or finite-checks identity and composition under partial-function
  equality.
- It handles the `1 -> 0` obstruction case as an empty-domain partial map.
- It distinguishes the contravariant `F_op` inclusion functor from the
  covariant `F_partial` repair.
- It states whether `F_partial` carries nontrivial forward-rate data.
- It separately types `N`, `C`, and `K`, or reports which terms remain
  untyped.
- It keeps the final verdict inside this list:

```text
parsets_partial_functor_passes_no_rate_promotion
parsets_partial_functor_passes_K_only
parsets_partial_functor_passes_NCK_typed_candidate
partial_functor_law_fails
inconclusive_category_not_frozen
```

Only `parsets_partial_functor_passes_NCK_typed_candidate` would authorize a
later bounded test of `lambda*(S)`. It still would not promote it.

## Null Or Demotion Conditions

Demote the ParSets route to K-only or retire it if any condition holds:

- The partial-map category is not specified.
- Undefined deleted sections are mapped to an ad hoc failure point without
  declaring a pointed-set codomain.
- Composition equality ignores undefined-domain differences.
- `F_partial` is functorial only on the section-preserving subcategory, making
  `N = K = 0`.
- The run uses contravariant `F_op` to infer forward growth.
- `N` and `C` are imported as generic gain/cost terms with no TaF or PO1 typing.
- A nonzero `lambda*(S)` appears only because `N` and `C` were chosen after
  seeing the fixture.
- The PO1-only objective still yields the boundary optimum `lambda*=0`.

Null result language to preserve:

```text
The ParSets repair did not recover a nontrivial PO1-NCK forward issuance
formalism. PO1-NCK remains re-scoped to a PO1-native K term, and lambda*(S)
remains a mixed-dynamics object outside a promoted PO1 theorem.
```

## No-Promotion Guardrails

- Do not state that covariant `F : States(Ext_S) -> FinSets` is repaired.
- Do not promote PO1-NCK from `candidate (re-scoped)`.
- Do not promote `lambda*(S)` as a consequence of PO1.
- Do not use a lawful partial functor alone as evidence for `N` or `C`.
- Do not treat `K` typing as a full issuance-rate optimum.
- Do not claim MTI promotion from this categorical repair.
- Do not edit `CLAIM-LEDGER.md`, `ROADMAP.md`, tests, models, results, README,
  or open-problem files from this preflight.

## Next Executable Artifact Shape

Recommended next artifact:

```text
workflows/logs/synthesis/YYYY-MM-DD-po1-nck-f-partial-parsets-run-card.md
```

If later authorized for implementation, convert the run-card into a test/model
pair only after the category and rate terms are frozen:

```text
tests/TXXX-po1-nck-f-partial-parsets.md
models/po1_nck_f_partial_parsets.py
results/po1-nck-f-partial-parsets-v0.1-results.md
```

Required run-card sections:

```text
not_claimed
settled_starting_point
ParSets_category
F_partial_definition
identity_check
composition_check
obstruction_case_check
rate_term_typing
controls
null_or_demotion_check
no_promotion_guardrail_check
verdict
```

Minimum machine-readable record:

```text
artifact_type: po1_nck_f_partial_parsets_run_card
category:
object_map:
morphism_rule:
undefined_rule:
identity_law: pass | fail | inconclusive
composition_law: pass | fail | inconclusive
obstruction_empty_domain_case: pass | fail | inconclusive
N_typed: yes | no | partial
C_typed: yes | no | partial
K_typed: yes | no | partial
lambda_star_status:
  blocked |
  K_only |
  NCK_typed_candidate |
  retired
final_verdict:
  parsets_partial_functor_passes_no_rate_promotion |
  parsets_partial_functor_passes_K_only |
  parsets_partial_functor_passes_NCK_typed_candidate |
  partial_functor_law_fails |
  inconclusive_category_not_frozen
claim_impact: no_status_change
```

