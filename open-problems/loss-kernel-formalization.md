# Loss Kernel Formalization

## Status

Open formal target.

Post-T127 note: the strongest live version may be the narrower
[LossKernel Witness-Obligation Normal Form](loss-kernel-witness-obligation-normal-form.md),
not a prior-art-separated theorem about a new attribution object.

## Diligence Gate

LossKernel is not yet cleared for canon or public theorem language. External
skeptical diligence classifies the current draft as mostly definitional unless
LossKernel becomes stricter than a set of user-chosen labels. Treat existing
T34/T37/T69/T73 checks as finite fixture evidence, not as proof that the
object is mathematically novel.

Before promotion, the program must answer three questions:

1. **Canonical semantics:** is `LossKernel(f)` derived from the morphism and
   source/target structures, or merely attached as metadata?
2. **Prior-art separation:** what attribution judgment is recoverable by
   LossKernel that is not already recoverable by standard CSP data plus
   provenance, why-not provenance, abstract interpretation, lenses, or
   graded/effect annotations?
3. **Quotient survival:** does path dependence survive after quotienting by
   same endpoints, same composite map, same endpoint satisfiability behavior,
   and same naive set of lost labels?

If the answer to these is negative, LossKernel should be retained only as an
honest annotation vocabulary.

## Strategic Role

`LossKernel` is the proposed central accounting object for the repo's next
phase. The goal is to move from many discovered patterns to one explicit object
for typed loss under information-losing morphisms.

After T108 and T127, that role should be read conservatively. The main value
may be to normalize source-derived witness obligations and collapse tests, not
to claim a new obstruction mechanism.

The repo should increasingly distinguish:

```text
known local-to-global obstruction
```

from the possible original contribution:

```text
typed attribution calculus for obstruction created or displaced by
information-losing morphisms
```

## Core Definition Target

For a typed morphism or projection:

```text
f: Source -> Target
```

define:

```text
LossKernel(f) = typed structure forgotten by f
```

This should be stricter than a free-text note. It should name structure in a
form that can be checked, composed, compared across paths, and used in
admissibility predicates.

## Required Laws To Investigate

Identity:

```text
LossKernel(id_A) = empty
```

Composition:

```text
LossKernel(g o f) = compose_loss(LossKernel(f), LossKernel(g))
```

The composition may be strict, lax, partial, or obstruction-sensitive. One of
the first tasks is to determine which.

Current finite fixtures support union accumulation, but that should be stated
as a monoid-valued annotation law on the tested morphism family unless a
stronger categorical or universal property is proved.

## Open Questions

1. Is `LossKernel(f)` just existing `forgotten_structure`, or a stricter typed
   object with source/target references and witness obligations?
2. Does loss compose functorially, lax-functorially, or only partially?
3. Can T34/T37 path dependence be re-expressed as unequal composed loss kernels?
4. Can T39/T40 obstruction attribution be rewritten as a `LossKernel`
   condition?
5. Can T19/T64/T66/T67 be treated as access/provenance loss corollaries?
6. Can a non-empty loss kernel be necessary without being sufficient for
   admissible obstruction attribution?
7. What is the correct equivalence relation on loss kernels: syntactic equality,
   same resolved obstruction, same resource decrease, or same typed witness?
8. Can LossKernel produce a separation theorem from ordinary CSP plus
   provenance/effect bookkeeping?
9. Are the T69 failure-type results valid only for the chosen finite cover
   fixtures, or do they survive standard Cech/sheaf-theoretic hypotheses?
10. Does the iterated orbit `{LossKernel(T^n) : n >= 1}` reveal stable,
    periodic, saturating, or failure-type-degrading behavior not visible from
    the one-step kernel `LossKernel(T)`?
11. Can obstruction relocation be made precise: when a projection removes an
    object-level obstruction, does a typed reconstruction obligation appear in
    provenance, loss, admissibility, or gap data?
12. Can LossKernel induce a measurable target-side reconstruction debt, such as
    ambiguity, non-uniqueness, or missing-witness lower bounds?

## Candidate Data Shape

```text
LossKernel =
  source_structure
  target_structure
  lost_types
  lost_witnesses
  preserved_types
  resolution_role
  composition_rule
```

`lost_types` names what kind of structure is removed. `lost_witnesses` names
the specific source-side data or constraints removed. `resolution_role` states
whether the lost structure is known to resolve the target obstruction, merely
correlates with it, or is not yet linked.

## Relationship To Existing Machinery

| Existing object | Relationship to LossKernel |
| --- | --- |
| `ProjectionCase.forgotten_structure` | Current informal predecessor. |
| AC5 / P5 | Requires informative forgetting; LossKernel should make this first-class. |
| `NetworkTransport.forgotten_structure` | Path-level predecessor; composition should accumulate kernels. |
| T34 chain analysis | Tests emergent, stepwise, and absorbed obstruction under composed loss. |
| T37 path dependence | Tests whether same endpoints can differ because composed loss differs. |
| T39 CSP reframing | Separates known parity obstruction from typed attribution metadata. |
| T40 holonic emergence | Requires cross-level forgotten dimensions for holonic attribution. |
| Iterated loss orbit | Candidate extension; must show behavior not already explained by one-step T69/T73 union accumulation. |
| Obstruction relocation | Candidate accounting principle; must avoid exact conservation language and classify where the failure moved. |
| T19/T64/T66/T67 | Candidate access/provenance loss corollaries. |

## Success Criteria

- Define a typed `LossKernel` object without relying on time, consciousness, or
  physics language.
- Prove or executable-check identity and composition laws for the finite T34/T37
  family.
- State whether the law is merely powerset-union annotation or something with a
  stronger universal, kernel, congruence, or witness-extraction role.
- Provide at least one quotient/separation result showing that LossKernel does
  theorem-level work beyond ordinary provenance or effect accumulation.
- Re-express AC5/P5 as a statement about non-empty, attribution-relevant loss.
- Show that at least one previous path-dependent result is exactly a difference
  in composed loss kernels.
- Preserve absorbed-obstruction cases without forcing a false conservation law.

If the quotient/separation criterion fails, the fallback success condition is
weaker but still real: derive a canonical witness-obligation normal form that
improves admissibility review even if it collapses into mature neighbor
machinery under same-data comparison.

## Failure Criteria

- `LossKernel` collapses to a synonym for `forgotten_structure` with no stronger
  typing, composition, or witness obligations.
- The best law is only `LossKernel(g o f) = LossKernel(f) union LossKernel(g)`
  with no semantic witness obligation beyond label accumulation.
- Path dependence is fully explained by endpoint conditions plus empty/non-empty
  label bookkeeping.
- Loss composition is not definable even in the finite T34/T37 families.
- AC5/P5 remains purely methodological metadata after the attempted
  formalization.
- The object cannot express absorbed obstruction or recovery without ad hoc
  exceptions.

T127 already puts heavy pressure on theorem-level separation. If future work
cannot derive a canonical witness-obligation object, demote `LossKernel` to an
integration vocabulary and stop treating TF1 as the default novelty window.

## First Concrete Test

Re-run T34 and T37 conceptually through `LossKernel`:

```text
spectre full path:
  non-empty composed loss -> endpoint PO1

spectre prefix:
  non-empty loss but no target obstruction -> not PO1

diamond path A:
  loss includes type_guarantee -> PO1

diamond path B:
  loss empty or attribution-irrelevant -> not PO1
```

If these cases cannot be expressed cleanly, the LossKernel proposal is too weak
or the existing AC5 machinery is doing less formal work than expected.
