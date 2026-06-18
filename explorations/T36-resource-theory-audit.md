# T36 Resource Theory / Monotones Audit

## Verdict

Finality is resource-like, but the repo does not yet have a full resource
theory of finality.

The cleanest current resource is not finality itself. It is:

```text
R(S) = 1 if global_assignment_exists(S), else 0
```

for finite `D1RestrictionSystem`s. A positive PO1 case is a strict loss:

```text
R(richer) = 1 -> R(restricted) = 0
```

So obstruction is resource loss only in the admissible PO1 sense: valid typed
pair, total projection, nontrivial restricted gluing obstruction, unobstructed
richer system, and named informative forgetting.

D1 finality itself is better treated as an observer-indexed preorder or
Lyapunov-style order parameter. In T18, admissible transformations are
D1-nondecreasing, so finality increases along allowed dynamics. That is
opposite the usual "free operations cannot create resource" convention unless
the order is inverted or "unfinality" is treated as the consumable resource.

## Closest Existing Mathematics

- Finite resource theories over preorders: objects are states/systems, allowed
  maps generate convertibility, monotones constrain conversion.
- Abstract interpretation: richer semantics projected to a restricted
  abstraction can create false impossibility or lose relational data.
- Sheaf/contextuality obstruction theory: local satisfiability without global
  section.
- Order-enriched categories: D1 profiles form a componentwise preorder;
  restriction morphisms need composition laws.
- Data-processing style monotonicity: projections should not increase selected
  information or section resources, but this is not yet proved for a stable
  operation class.

## Clean Mappings

Objects:

```text
D1 profiles: (A, R, B, C)
D1RestrictionSystem: finite sites + local profiles + transport + patches
ProjectionCase: richer system + restricted system + site map + forgotten structure
```

Preorder:

```text
x <= y iff every D1 component of x is <= the matching component of y
```

This is a preorder over propositions because distinct propositions can share a
profile. It is a partial order only after quotienting by equal profiles.

T18 allowed transformations:

```text
admissible iff after.d1 >= before.d1 componentwise
strict finalization iff at least one component strictly increases
```

This gives finite monotones:

```text
A, R, B, C are each nondecreasing along T18-admissible transformations.
```

PO1 section resource:

```text
R(S) = [global_assignment_exists(S)]
```

For positive PO1 projections, `R` strictly decreases. The obstruction
indicator

```text
O(S) = 1 - R(S)
```

is nondecreasing on locally satisfiable PO1 targets, but only inside the
restricted PO1 operation class.

Conserved or preserved quantities are not universal. IPT and T26 preserve only
declared invariants: selected D1 dimensions, trusted reachability, pointer
basis, quorum-intersection safety, holder redundancy, or obstruction status
when explicitly required.

## Failed or Weak Mappings

- "Finality is a conserved resource" fails. T18 allows finality to increase;
  PO1 projections usually lower profile detail; neither gives conservation.
- "Obstruction is always resource loss" fails. Shared obstruction is inherited,
  local failure is trivial, non-definable projection is outside the conversion
  relation, and loss without obstruction is a counterexample.
- "Raw global witness count is the resource" fails. Systems with no patches
  have `global_witness_count = 0` but `global_assignment_exists = True`.
- "D1 rank is the monotone" is weak. The sum of components is monotone under
  componentwise increase, but it destroys the repo's central incomparability
  result.
- "T33 derives AC5-measurable from RMT" is overstated. Global satisfiability
  depends on patch constraints, not necessarily D1 profile mismatch. A
  resource drop can be built with identical local profiles and different
  patches, so profile loss needs an extra axiom.

## Overclaims

Avoid saying:

- PO1 is a full resource theory.
- AC1-AC7 are fully derived from one principle.
- RMT alone derives the admissibility checklist.
- Projection loss implies obstruction.
- Obstruction persists through chains.
- T35 discovers theorems automatically.
- PO1 proves the original physics, CAP, Spectre, or Git examples.

The strongest fair claim:

```text
PO1 is a finite, partially derived projection-obstruction schema
with a boolean global-assignment monotone and explicit boundary cases.
```

## Implementation Audit Notes

The T33 local-failure branch appears to contain an unhit code path:

```text
classify_obstruction() references gs.patch_count
GlobalSectionResult has no patch_count field
```

A local probe of a restricted system with one locally inconsistent patch raises
`AttributeError`. This does not undermine the positive PO1 cases, but it means
the local-failure certificate path should be fixed before relying on T33's
obstruction classifier for hostile cases.

## Underdeveloped Mathematics

- The free operation class is not independently fixed. "Allowed projection"
  must be defined before monotonicity, or the monotone claim becomes circular.
- Composition is incomplete. T34 shows endpoint PO1 behavior, but AC5
  accumulation and step localization are still open.
- There is no monoidal product, tensor/disjoint-union theorem, catalytic
  behavior, or conversion-rate theory.
- `forgotten_structure` is metadata, not first-class formal structure.
- Non-monotone recovery is unresolved. T34's absorbed optimizer case increases
  accessible support and removes obstruction, which is outside a simple
  restriction-only resource theory.

## Required Mathematics Before Serious Uptake

1. Define a category or preorder of valid finite `D1RestrictionSystem`s.
2. Define free maps independently: total site-map restrictions, allowed patch
   handling, allowed profile loss, and forbidden recovery.
3. Prove `R(S) = [global_assignment_exists]` is monotone for exactly that map
   class.
4. Prove or reject composition: if `S0 -> S1 -> S2`, when does endpoint PO1
   follow?
5. Promote `forgotten_structure` into typed formal data.
6. Separate T18 finalization dynamics from PO1 abstraction projections.
7. Add counterexamples for same-profile resource drop, obstruction removal,
   partial site maps, and local failure.

## Recommended Next Theorem or Counterexample

Next theorem candidate:

**PO1 Resource Monotonicity Theorem**

For valid D1RestrictionSystems and a specified class of total finite
restriction projections, `R(S) = [global_assignment_exists]` is non-increasing.
Strict decrease occurs exactly when the endpoint satisfies AC6 and the source
satisfies AC7, with AC5 supplied by first-class informative forgetting data.

But first try to break it with this counterexample:

```text
Richer: same sites, same D1 profiles, no obstruction.
Restricted: same sites, same D1 profiles, patches a=b, b=c, a!=c.
Site map: identity and total.
Result: R drops 1 -> 0, but local_profiles_preserved=True.
```

If admitted, this refutes the AC5-measurable derivation from RMT and proves
AC5 needs independent formal content.

## Notes for Synthesis

Use "global-assignment resource" or "section-availability monotone," not
"finality resource," unless the order convention is explicit.

Treat obstruction as strict loss only for fully admissible PO1 cases.

Keep T18 and PO1 separate: T18 is D1-nondecreasing dynamics; PO1 is lossy
projection.
