---
document_type: synthesis_preflight
queue_item: 7
status: complete
authority: non_authoritative
write_scope: workflows/logs/synthesis
claim_effect: none
source_open_problem: open-problems/cross-domain-shadow-protection-theorem.md
source_template: workflows/templates/north-star-shadow-audit.template.md
---

# Cross-Domain Shadow Protection Two-Fill Preflight

## Scope

This is a preflight artifact for the first bounded run in
`open-problems/cross-domain-shadow-protection-theorem.md`. The run should fill
`workflows/templates/north-star-shadow-audit.template.md` twice and compare only
the proof spine:

```text
visible fiber -> capability spread -> native absorber -> minimal enrichment
```

The two fills should be:

1. a database/view-determinacy or process-semantics example;
2. a quantum resource theory access-profile example.

This preflight does not state a theorem, promote a physics claim, or change any
claim ledger status.

The source open problem is marked dormant. This preflight preserves that status
until the two fill packets are actually completed and reviewed.

## Inputs To Freeze Before Execution

Read surfaces:

- `open-problems/cross-domain-shadow-protection-theorem.md`.
- `workflows/templates/north-star-shadow-audit.template.md`.
- Domain-native references or repo artifacts selected for the database/process
  fill and the quantum-resource fill.

For each domain `D`, freeze the following before computing the verdict:

```text
Y_D       source structure
O_D       observer/access profile
pi_D      observer shadow
X_D       visible codomain
~=_X,D    visible equivalence
Cap_D     domain-native capability object
K_D       capability codomain
R_K,D     native capability comparison
A_D       admissible source states
```

The executor must also freeze the positive preservation control and negative
non-factorization fixture for each domain before comparing proof spines.

## Two-Fill Protocol

1. Copy the North Star shadow-audit template into a new bounded run artifact.
2. Fill it once for database/view determinacy or process semantics.
3. Fill it once for quantum resource theory under an explicit access profile.
4. In each fill, grant native absorber state and native theorems before naming
   any residue.
5. Compute capability spread over visible fibers in each fill using the frozen
   `Cap_D`, `~=_X,D`, and `R_K,D`.
6. Identify the minimal enrichment that repairs shadow failure, if any.
7. Compare only the proof spine and not the surface vocabulary of the domains.
8. Record whether the same audit spine survived without changing definitions
   after seeing the examples.

## Required Fill Checks

Each fill must answer these questions:

| Check | Pass condition | Fail condition |
| --- | --- | --- |
| Native capability | `Cap_D` is forced by the domain task or native comparison. | `Cap_D` is chosen to match the hidden variable. |
| Visible fiber | The visible equivalence is declared before examples. | Fibers are redefined after observing the verdict. |
| Positive control | A known sufficient projection or preservation case is present. | Only negative or ambiguous cases are supplied. |
| Negative fixture | A non-factorization or insufficiency case can occur. | The setup passes by construction. |
| Absorber completion | Native state and theorems are granted first. | Residue is assigned before native repair attempts. |
| Minimal enrichment | The repair data is named and smaller than the full source when possible. | The only repair is trivial source reattachment without explanation. |

## Acceptance Criteria

The two-fill run is accepted as useful only if all of the following hold:

- Both fills use the same frozen audit fields from the open problem.
- Each fill contains a positive preservation control and a negative
  non-factorization or insufficiency fixture.
- The proof spine can be compared without changing the definition of
  shadow protection after seeing the examples.
- Native absorber state and native theorems are granted before any residue label
  is assigned.
- The run states whether the shared spine is nontrivial, trivial
  fiber-constancy, or broken by domain-specific definitions.
- Any successful result is phrased as reusable audit-spine evidence across two
  bounded domains, not as a general theorem.

Permitted verdicts:

```text
same_spine_nontrivial
same_spine_trivial_fiber_constancy_only
spine_breaks_by_domain_specific_definition
inconclusive_missing_native_fixture
```

## Null Or Demotion Conditions

Demote the theorem-shaped target if any of these occur:

- Every domain requires unrelated ad hoc definitions.
- `Cap_D` is gerrymandered to match the hidden variable.
- Mature absorber fields restore sufficiency with no useful transfer.
- The only universal statement left is the trivial fiber-constancy lemma.
- No domain supplies a nontrivial negative fixture after native state
  completion.
- Quantum-resource access profiles cannot be stated without importing a physics
  claim outside the bounded audit.
- Database/process and quantum fills agree only at the level of generic prose.

Null result language to preserve:

```text
The two-fill run did not support a cross-domain shadow-protection theorem
shape. At most, it preserved an atlas of domain-specific audits or a trivial
fiber-constancy lemma.
```

## No-Promotion Guardrails

- Do not promote a physics, quantum, geometry, spacetime, consciousness, or
  North Star claim from this run.
- Do not call the result a theorem unless a later authoritative artifact proves
  the statement under named hypotheses.
- Do not compare surface vocabulary across domains as evidence of transfer.
- Do not treat the trivial enrichment `pi'(y) = (pi(y), Cap(y))` as a
  substantive repair unless the run explicitly marks it trivial.
- Do not edit `CLAIM-LEDGER.md`, `ROADMAP.md`, tests, models, results, README,
  or open-problem files from this preflight.
- Do not use a successful two-fill spine to claim universality across mature
  domains.

## Next Executable Artifact Shape

Recommended next artifact:

```text
workflows/logs/synthesis/YYYY-MM-DD-cross-domain-shadow-protection-two-fill-run.md
```

Required sections:

```text
claim_under_test
not_claimed
database_or_process_fill
quantum_resource_fill
native_absorber_passes
positive_and_negative_controls
capability_spread_tables
minimal_enrichment_comparison
proof_spine_comparison
verdict
no_promotion_guardrail_check
```

Each fill should use the headings from
`workflows/templates/north-star-shadow-audit.template.md` and end with:

```text
projection_sufficient: yes | no | conditional | inconclusive
minimal_enrichment:
residue_label: canonical residue | formal audit residue |
               translation residue | heuristic residue |
               redundant or demoted
kill_condition:
```
