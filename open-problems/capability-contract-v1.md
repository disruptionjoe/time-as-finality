# CapabilityContract v1

## Status

Provisional TaF-owned source definition and executable review contract.

T583 implements this contract as a finite deterministic instrument. It does
not promote a claim, establish a universal capability measure, derive time,
or move cross-repository truth.

T584 adds the first finite invariance morphism gate over the contract. In that
fixture, capability factors through admissible representation, gauge, and
irrelevant-coarse-graining quotients, while a task-vocabulary merge is caught
as an inadmissible counterexample. This is still review-only; the next burden
is a genuine physical system with source-derived states, operations, resources,
costs, records, access, quotient, and task performance.

## Purpose

Capability language is too cheap unless the physical and operational context
is fixed before comparing cases. CapabilityContract v1 makes that context an
explicit object and treats capability as an attainable task-performance-cost
envelope rather than a scalar by default.

The required direction for physics-facing use is:

```text
known physics
  -> admissible states, operations, resources, and costs
  -> induced capability object
  -> capability comparison
```

The contract cannot infer known physics from a chosen capability object.

## Contract Object

Declare a context

```text
Gamma = (
  D, A, equivalent_phys,
  R, O, Access,
  T, M, provenance_M,
  Resources, provenance_Resources,
  B, h,
  Q_gauge,
  K, relation_K,
  Coarse_irrelevant
)
```

with:

- `D`: source theory or domain;
- `A`: admissible physical states;
- `equivalent_phys`: physical equivalence, including admissible renaming and
  representation changes;
- `R`: bounded region;
- `O`: observer or control profile;
- `Access`: subsystems, records, instruments, communication rights, reference
  frames, and state-inspection rights available to `O` in `R`;
- `T`: task family, fixed before selecting the comparison pair;
- `M`: allowed operation or intervention menu;
- `provenance_M`: whether `M` is law-derived, experimentally measured,
  operationally certified, declared, or only a proxy;
- `Resources`: ancillas, catalysts, baths, memory, communication, reference
  frames, work stores, and other task inputs;
- `provenance_Resources`: source of the resource accounting;
- `B`: explicit energy, time, communication, memory, and error budgets;
- `h`: horizon, cadence, or stopping rule;
- `Q_gauge`: physical gauge quotient;
- `K`: native capability codomain;
- `relation_K`: native comparison on `K`; and
- `Coarse_irrelevant`: fields proven irrelevant for this comparison.

Access, menu, resource, and budget fields are not annotations. They are part
of the capability type. A pair with different values is not a matched
intrinsic-capability pair.

## Capability Value

For state `y` and task `t`, an attainable point is

```text
p = (t, success, energy, time, communication, memory, error).
```

The point is admissible only when it is produced by an operation in `M`, uses
declared resources, and lies inside `B` and `h`.

Define

```text
C_Gamma(y) = the nondominated attainable points for every t in T.
```

The default native structure is the task-indexed Pareto preorder. One envelope
covers another when every point in the second is matched by a same-task point
with at least as much success and no greater declared cost or error.

This gives four basic relations:

```text
equivalent
superset
subset
incomparable
```

A scalar may be applied only when a domain supplies and justifies a scalar
utility, monotone, or risk functional. Scalarization is not part of the
default contract.

## Invariance Requirements

### Renaming and representation

Equivalent task names, protocol labels, coordinate labels, and physical
representations must give the same native capability relation after applying
the declared equivalence map.

### Gauge

Gauge representatives are not separate physical capabilities. Capability
must factor through `Q_gauge`, or the witness fails the physical-equivalence
gate.

### Irrelevant coarse-graining

A field may be removed as irrelevant only if the contract declares it before
pair selection and its removal preserves the physical payload, the admissible
operation menu, and the attainable envelope. If removal changes any of those,
it is a projection change rather than an invariance result.

## Nontriviality

Capability is not the full physical state. Two physically distinct state
identifiers may have equivalent attainable envelopes. A contract that assigns
different capabilities to every different state merely restates the state and
fails the nontriviality gate.

## Completion And Null Classes

The first matching class in the declared comparison scope controls the result:

1. `NO_CAPABILITY_DELTA`;
2. `RENAMING_OR_GAUGE_EQUIVALENCE`;
3. `IRRELEVANT_COARSE_GRAINING`;
4. `TASK_REDEFINITION_COMPLETION`;
5. `MENU_COMPLETION`;
6. `ACCESS_COMPLETION`;
7. `RESOURCE_BUDGET_COMPLETION`;
8. `EXPLICIT_STATE_RESOURCE_COMPLETION`;
9. `FIXED_SOURCE_COMPLETION`;
10. `NATIVE_STATE_COMPLETION`.

A capability difference becomes a review candidate only after the context is
matched, visible equality is earned, admitted completions fail, the physical
boundary is forced, the menu is law-derived or measured, and an independent
holdout survives. Passing those fields in a synthetic fixture still earns
only review-candidate status.

## Controls

Every implementation must include:

- a positive preservation control under renaming, gauge, or representation;
- an irrelevant coarse-graining control;
- a distinct-state/equal-capability control;
- a negative nonfactorization fixture;
- a changed access, menu, resource, or budget mutation that is absorbed;
- a fixed-source or explicit-state completion control;
- an independent holdout field; and
- a synthetic complete packet whose ceiling is review-only.

## W192 Calibration

The current frozen W192 proxy changes exactly one task when access to the
frozen `psi` state/resource is supplied. CapabilityContract v1 must therefore
return:

```text
EXPLICIT_STATE_RESOURCE_COMPLETION
```

It must not convert W192 into a positive physical capability result.

## Evidence And Promotion Boundary

T583 verifies the contract mechanics on finite fixtures. It does not verify
that a task family is physically natural, that an operation menu is truly
law-derived, that a completion is physically inadmissible, or that a synthetic
boundary exists in nature.

No claim-ledger, Canon Index, public posture, publication, TAF3, TAF8, S1, or
cross-repository movement follows from the contract.

## Falsifiers And Reopening Conditions

Revise the contract if:

- a representation-equivalent or gauge-equivalent pair changes capability;
- an allegedly irrelevant coarse-graining changes the attainable envelope;
- a state difference automatically creates a capability difference;
- a changed access, menu, resource, or budget is accepted as matched;
- a domain-native capability cannot be represented by an equivalence,
  preorder, metric, risk, or category-valued comparison without distortion;
- a mature neighboring theory supplies a standard completion omitted here;
  or
- a real physical packet exposes a necessary contract field not represented.
