# D1-Field: Multiscale Observer Finality

## Claim

For claims that cross observers, populations, institutions, communication
networks, scales, or time, D1 requires more than one global profile. T24
introduced this as a field-valued extension. T25 narrows the best-supported
minimal object to a finite graph-indexed local-to-global D1 restriction
system. T26 formalizes that object as `D1RestrictionSystem`.

The local value remains the existing D1 profile:

```text
F_O,e(x) = (accessible support, holder redundancy, branch support, reversal cost)
```

The field-valued extension is:

```text
D1Field(x) = (
  observer sites,
  local D1 profiles,
  proposition values,
  transport edges,
  local patches,
  gluing constraints
)
```

The T25 minimal object is:

```text
GraphD1Restriction = (
  local D1 profiles,
  observer sites,
  trusted transport edges,
  optional patch constraints
)
```

T26 implements the formal object as:

```text
D1RestrictionSystem = (
  sites,
  local D1 profiles,
  proposition values,
  trusted transport edges,
  optional overlap tests,
  optional patch constraints,
  projection maps,
  compatibility predicate,
  global-section predicate
)
```

## Class

Formal extension.

## Status

Partially supported.

## What This Does Not Claim

- It does not replace the existing D1 profile.
- It does not claim finality is continuous over spacetime.
- It does not claim one institution or civilization has a literal mind.
- It does not identify social consensus with physical truth.
- It does not prove a full sheaf or bundle theory of D1.
- It does not claim full IPT representation.
- T26 does not make the restriction system continuous, covariant, or complete.

## Why It Might Be True

Existing tests already pressure D1 away from a single global profile:

- T2 gives different D1 profiles to different observers in one measurement
  chain.
- T21 shows local finality sections can fail to glue globally.
- T23 makes observer access and reduction maps explicit transport objects.

T24 adds direct counterexamples:

- scalar min and max both lose observer-distribution data in a stratified
  access model;
- two scenarios with the same observer-profile vector differ in transport
  because their communication graphs differ;
- local patches can each be satisfiable while the global assignment fails.

T25 adds a hypothesis audit:

- scalar D1 is retained only for fixed-observer or uniform cases;
- vector D1 is sufficient only when observer distribution matters but transport
  and gluing do not;
- graph-indexed restriction is the smallest structure that handles transport
  and gluing in the finite evidence;
- full sheaf language is promising but not yet required.

T26 adds a formal object:

- scalar D1 is an executable projection from `D1RestrictionSystem`;
- vector D1 is an executable projection that can lose graph and patch data;
- trusted transport and finite patch constraints are first-class data;
- restriction morphisms can pass or fail under explicit preservation checks.

T53 adds a multi-observer colimit boundary:

- bounded observer views can merge into valid partial orders;
- valid partial-order colimits need not be canonical;
- event identity maps and overlap data are required for unique reconstruction;
- AM-compatible axis profiles are required if finality-axis dominance is used
  to reconstruct temporal order.

T54 turns that boundary into a finite descent theorem:

- event identity maps must be total and single-valued;
- cross-observer identified events need overlap witnesses;
- source and target records must merge without explicit contradiction;
- identified events must agree on finality-axis profiles;
- the quotient-union order must be a valid partial order;
- Axis Monotonicity must hold for axis-based temporal reconstruction.

T55 adds conflict relations to the descent data:

- mutually exclusive finality events are not the same as incomparable events;
- conflict can descend canonically when finite conflict conditions hold;
- conflict is independent data, not reconstructible from order or AM alone.

## How It Could Fail

- A better aggregate rule may recover all relevant multiscale information.
- Field edges may be unnecessary once observer access boundaries are stated
  more carefully.
- Gluing obstruction may belong only to T13/T21 contextuality, not to D1
  generally.
- The field object may be too flexible to constrain predictions.
- Conflict or provenance data may require a different object than the current
  quotient-union descent datum.

## T24 Result

[T24](../tests/T24-d1-multiscale-observer-field.md) compares scalar, vector,
and field interpretations across finite toy models.

The verdict is:

```text
single_global_scalar_sufficient = false
vector_d1_required_for_multiscale_snapshots = true
field_d1_required_for_transport_and_gluing_claims = true
scalar_d1_recoverable_as_special_case = true
replace_existing_d1 = false
```

The recommended interpretation is:

```text
existing D1 profile = local value
D1 field = extension for multiscale and global claims
```

## T25 Result

[T25](../tests/T25-minimal-d1-generalization.md) compares five hypotheses:

```text
H0: scalar D1 is sufficient
H1: vector-valued D1 is sufficient
H2: field-valued D1 is required
H3: another finite local-to-global structure is required
H4: no canonical generalization is currently justified
```

The best-supported hypothesis is:

```text
H3
```

The recommendation is to formalize the graph-indexed D1 restriction system
before attempting full sheaf semantics or full IPT representation.

## T26 Result

[T26](../tests/T26-d1-restriction-system.md) formalizes the T25 result as:

```text
D1RestrictionSystem
```

The best-supported hypothesis is:

```text
H1: finite graph-indexed D1 restriction system is sufficient
```

T26 reaches scalar recovery, vector recovery, graph necessity, gluing
obstruction, and restriction-morphism checks. It defers full IPT
representation because current IPT objects still lack site maps and
restriction-map commutation data.

## T53 Result

[T53](../tests/T53-observer-colimit-descent-boundary.md) shows that
multi-observer apparent-finality colimits require finite descent data for
canonical reconstruction. T47-style acyclicity can protect partial-order
consistency, but it does not decide whether observer-local event labels refer
to the same global event, whether hidden records repair an apparent mismatch,
or whether finality-axis dominance reconstructs the merged record order.

This strengthens D1-Field only within its current status. It supports finite
graph-indexed local-to-global structure over scalar/vector summaries, but it
does not force full sheaf machinery.

## T54 Result

[T54](../tests/T54-finite-finality-descent-theorem.md) defines
`ObserverDescentDatum` and an executable quotient-union completion algorithm.
It classifies T51 and T52 as canonical and T53 as underdetermined, then supplies
counterexamples for each omitted descent condition.

The result strengthens D1-Field as the finite local-to-global object needed for
cross-observer finality. It does not require full sheaf or categorical descent
machinery for the tested finite witness family.

## T55 Result

[T55](../tests/T55-conflict-finalievent-descent.md) extends the finite descent
object with an explicit conflict relation. The result supports D1-Field's
local-to-global posture because conflict is extra cross-observer structure:
two structures can share the same record order and AM-valid axis profiles while
differing in conflict.

The extension remains finite. Full event-structure, sheaf, or categorical
machinery can still be postponed for the tested witness family.

## Tests

- [T24: D1 Multiscale Observer Field](../tests/T24-d1-multiscale-observer-field.md)
- [T25: Minimal D1 Generalization](../tests/T25-minimal-d1-generalization.md)
- [T26: D1 Restriction System](../tests/T26-d1-restriction-system.md)
- [T53: Observer-Colimit Descent Boundary](../tests/T53-observer-colimit-descent-boundary.md)
- [T54: Finite Finality Descent Theorem](../tests/T54-finite-finality-descent-theorem.md)
- [T55: Conflict-Enriched FinaliEvent Descent](../tests/T55-conflict-finalievent-descent.md)

## Contribution Needed

Define composition laws for D1 restriction morphisms. Then test whether T13/T21
obstruction and T23 transport factor through the same finite restriction
semantics before upgrading to full sheaf language.
