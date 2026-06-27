---
document_type: synthesis_preflight
queue_item: 6
status: complete
authority: non_authoritative
write_scope: workflows/logs/synthesis
claim_effect: none
source_open_problem: open-problems/observer-shadow-category.md
---

# Observer-Shadow Category Bounded Run Preflight

## Scope

This is a preflight artifact for the first bounded run named in
`open-problems/observer-shadow-category.md`. It does not define a category,
prove a preservation theorem, update any claim surface, or execute a model or
test.

The next run should test only whether two finite families can be expressed with
one shared observer-shadow object and morphism schema:

1. a typed transport network path;
2. a database/view projection or LossKernel witness-obligation fixture.

If the shared schema cannot represent either family without hand-built
case-specific data, the run should stop and record the obstruction.

## Inputs To Freeze Before Execution

Read surfaces:

- `open-problems/observer-shadow-category.md`.
- `workflows/templates/run-log.template.md` for run-report shape.
- Existing finite transport and database/view or LossKernel witness-obligation
  artifacts selected by the executor.

Executor must freeze these fields before judging the examples:

| Field | Required pre-run declaration |
| --- | --- |
| `Y` | typed source system |
| `O` | observer or access profile |
| `pi_O` | declared projection from source to visible data |
| `X_O` | visible codomain |
| `Cap` | domain-native capability object |
| `K` | capability codomain |
| `R_K` | native comparison on capability values |
| `A` | admissible source states, if not all of `Y` |
| `verdict` | shadow-protection verdict being preserved or refuted |

No field may be introduced after seeing a desired preservation result unless
the run records that as a schema failure.

## Candidate Object Schema

Use the conservative object from the open problem:

```text
(Y, O, pi_O, Cap, R_K)
```

Optional fields are allowed only if both finite families need them for native
typing:

```text
A          admissible source states
~=_X       visible equivalence
B, h       boundary and horizon, if already present in the source fixture
```

Adding optional fields is not a promotion. It is evidence that the minimal
object may need enrichment, and the run must state whether the enrichment is
shared or domain-specific.

## Candidate Morphism Schema

A candidate morphism from one observer-shadow object to another should include
only the following components unless the run explicitly logs an obstruction:

```text
source map          f : Y -> Y'
shadow map          x : X_O -> X'_{O'}
capability map      k : K -> K'
observer map        o : O -> O'
compatibility       x(pi_O(y)) = pi'_{O'}(f(y)) where defined
comparison respect  Cap(y) R_K Cap(z) => k(Cap(y)) R_K' k(Cap(z))
```

Composition is admissible only if the compatibility and comparison-respect
clauses remain well typed after composing the component maps.

## Preflight Protocol

1. Select one finite typed transport network path fixture and one database/view
   or LossKernel witness-obligation fixture.
2. Fill the object schema for both fixtures before defining any inter-object
   morphism.
3. Identify at least one within-family morphism or refinement in each fixture.
4. Compose two morphisms where the fixture supplies a natural triple. If no
   natural triple exists, record `composition_probe_unavailable`.
5. Test whether the composed morphism preserves the declared
   shadow-protection verdict under the frozen hypotheses.
6. If preservation fails, classify the obstruction using the open-problem list:
   capability object change, observer access change, native comparison change,
   visible equivalence change, absorber state completion change,
   path-dependent loss change, or gauge/representation quotient change.
7. Decide whether the schema is shared, needs a fibration/indexed structure, or
   should be demoted to set-level fiber-constancy audits.

## Acceptance Criteria

The bounded run passes only if all of the following are true:

- Both finite families are expressed with the same object schema without
  selecting `Cap` by hand after the verdict is known.
- At least one nontrivial morphism in each family satisfies the compatibility
  and comparison-respect clauses.
- A composition probe is run where the fixture permits it, or the lack of a
  composable triple is itself typed and explained.
- The verdict under composition is one of:
  `preserved_under_named_hypotheses`, `fails_with_typed_obstruction`,
  `requires_indexed_or_fibered_structure`, or `set_level_audit_only`.
- The run states the exact hypotheses under which preservation holds, or the
  exact obstruction that prevents preservation.
- The result adds a check beyond simply recomputing capability spread on visible
  fibers, or it records that no added check exists.

## Null Or Demotion Conditions

Demote categorical language for this line if any of these occur:

- Objects or morphisms are chosen mainly to force a commutative diagram.
- `Cap`, `R_K`, or visible equivalence must be reselected separately for each
  domain after the examples are known.
- The construction adds no check beyond the existing capability-spread audit.
- Mature domains require incompatible notions of morphism.
- Observer changes cannot be typed without manually rebuilding capability
  objects.
- Composition cannot be stated without importing untracked source data or
  unstated admissibility assumptions.
- The only reusable statement left is fiber constancy over visible classes.

Null result language to preserve:

```text
The bounded run did not find a shared observer-shadow category. The current
safe object is an atlas of domain-specific audits or set-level fiber-constancy
checks.
```

## No-Promotion Guardrails

- Do not call the output a category, indexed category, fibration, double
  category, or compositional theorem unless the run has verified composition
  under named hypotheses in both finite families.
- Do not promote the North Star geometry, physics, spacetime, consciousness, or
  general observer-shadow vision from this run.
- Do not edit `CLAIM-LEDGER.md`, `ROADMAP.md`, tests, models, results, README,
  or open-problem files from this preflight.
- Do not use a successful finite family as evidence for all domains.
- Do not hide schema failure by appending `Cap(y)` to the visible data and
  calling the result projection-sufficient.

## Next Executable Artifact Shape

Recommended next artifact:

```text
workflows/logs/synthesis/YYYY-MM-DD-observer-shadow-category-bounded-run.md
```

Required sections:

```text
selected_fixtures
frozen_object_schema_table
frozen_morphism_schema_table
transport_network_fill
database_or_losskernel_fill
composition_probe
shadow_protection_verdict_table
obstruction_classification
categorical_language_decision
no_promotion_guardrail_check
```

Minimum verdict block:

```text
verdict: preserved_under_named_hypotheses |
         fails_with_typed_obstruction |
         requires_indexed_or_fibered_structure |
         set_level_audit_only
claim_effect: none
next_step: test_spec | demote_language | rerun_with_named_fixture
```
