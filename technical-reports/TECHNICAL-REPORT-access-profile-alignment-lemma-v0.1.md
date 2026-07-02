# Technical Report: Access-Profile Alignment Lemma v0.1

## Status

Internal method-hardening artifact.

This note does not promote a claim, change the North Star, update the roadmap,
update the claim ledger, register a numbered test, create an executable result,
or assert new physics. It extracts the narrow reusable rule earned by the
two-domain native-comparison shadow audit:

```text
Cap must be indexed to the same observer/access boundary as pi unless the run
explicitly declares a cross-profile insufficiency question.
```

The purpose is to make that rule copy-ready for future witness intake.

## Objective

Prevent a common false-positive pattern in observer-shadow and capability
projection runs:

```text
pi_O(y1) ~=_X pi_O(y2)
but
Cap_{O'}(y1) not R_K Cap_{O'}(y2)
```

where `O` and `O'` are different access profiles and the run has not declared
that mismatch as the question under test.

Without an alignment rule, this pattern can look like projection residue. In
most cases it is only an access-profile mismatch or native state
underdescription.

## Minimal Setup

Declare an audit context:

```text
Y       source structure
A       admissible source states, A subset Y
O       observer or access profile
pi_O    visible projection available to O
X_O     visible codomain for O
~=_X,O  visible equivalence for O
T       task family
h       horizon
B       boundary, budget, or resource condition
Cap_O   capability object available to O
K_O     native capability codomain
R_K,O   native capability comparison
```

An access profile includes all rights needed for the question:

```text
subsystems, records, instruments, boundary-crossing menus, communication
rights, free-operation class, environment or purifier access, state-inspection
rights, query rights, update rights, budgets, and native completion state.
```

It is not just a person or location. It is the operational boundary that
determines which states, operations, and comparisons are legitimate.

## Alignment Rule

A witness is access-aligned when the projection and capability object use the
same access profile:

```text
pi_O : A -> X_O
Cap_O : A -> K_O
```

Then the ordinary projection-sufficiency question is meaningful:

```text
pi_O(y1) ~=_X,O pi_O(y2) => Cap_O(y1) R_K,O Cap_O(y2)
```

The visible fiber and the capability spread are both indexed to `O`:

```text
Spread_Cap,O([x]) =
  { Cap_O(y) | y in A and pi_O(y) ~=_X,O x }
```

The native comparison `R_K,O` decides whether that spread collapses.

## Cross-Profile Exception

A run may intentionally compare:

```text
pi_O
```

against:

```text
Cap_{O'}
```

but only if it declares a cross-profile insufficiency question before choosing
the witness pair.

The run must then name:

```text
O          smaller or different access profile
O'         larger or different access profile
relation  inclusion, restriction, boundary extension, communication grant,
          state-completion map, or explicit absence of such a map
meaning   why Cap_{O'} is being compared to pi_O
```

Without that declaration, the result is killed as:

```text
access-profile mismatch
```

not promoted as residue.

## Lemma-Shaped Rule

### Rule

For an observer-shadow audit, a projection-sufficiency failure is admissible
only if one of the following holds:

1. `pi_O` and `Cap_O` are indexed to the same access profile; or
2. the run explicitly declares a cross-profile question and names the
   comparison relation between `O` and `O'`.

Otherwise the apparent failure is not evidence about projection sufficiency.
It is a typing error in the audit context.

### Proof Sketch

Projection sufficiency asks whether the visible state available to an observer
determines the capability available under the declared task, horizon, and
boundary.

If `pi` is indexed to `O` but `Cap` is indexed to `O'`, the antecedent and
consequent refer to different operational boundaries. The visible fiber is an
`O`-fiber, while the capability spread is an `O'` spread. Unless the run has
declared a map or comparison relation between those profiles, there is no
single native object whose preservation is being tested.

The mismatch can always be repaired in one of two ordinary ways:

```text
lower the capability object to Cap_O
```

or:

```text
enrich the projection to pi_{O'} when O' access is legitimately granted
```

If neither repair is allowed, the correct output is an access-boundary
diagnostic, not a residue label.

## Decision Table

| Case | Input shape | Allowed verdict |
| --- | --- | --- |
| Same profile | `pi_O` versus `Cap_O` | Run native spread and absorber tests. |
| Larger capability profile declared | `pi_O` versus `Cap_{O'}` with relation named | Cross-profile insufficiency diagnostic. |
| Larger capability profile undeclared | `pi_O` versus `Cap_{O'}` with no relation | Killed as access-profile mismatch. |
| Native state missing inside same profile | `pi_O` omits legitimate state used by `Cap_O` | Projection-underdescribed until native completion is tested. |
| Trivial enrichment only | `pi'(y) = (pi_O(y), Cap(y))` | Vacuous repair; not residue. |

## Examples

### Quantum Resource Theory

Strict local access:

```text
pi_A(rho_AB) = rho_A
Cap_A        = local-A operational capability
```

This is access-aligned. The local visible state can determine local operational
statistics and local operation availability under the declared frame.

Mismatched global capability:

```text
pi_A(rho_AB) = rho_A
Cap_AB       = LOCC or global resource-conversion envelope
```

This is not a local-A capability claim. It is either:

```text
an explicit cross-profile question
```

or:

```text
an access-profile mismatch
```

The native repair is to align the capability to `O_A` or enrich the visible
state and operation frame to `O_AB`.

### Vector Retrieval

Corpus-only projection:

```text
pi_user(system) = visible corpus and metadata
```

Deployment capability:

```text
Cap_deployed = recall/latency/top-k envelope under index, parameters,
               workload, metric, and hardware budget
```

This is often not a different-person mismatch, but it is still an
underdeclared operational boundary. If the deployed system's hidden index and
execution state are legitimate parts of the task capability, the native repair
is to include:

```text
index family, construction parameters, search parameters, workload, metric,
filter policy, and resource budget
```

The result is translation residue or heuristic underdescription detection, not
ANN novelty.

### Boundary-Crossing Capability Screens

If a future region-indexed screen compares:

```text
pi_R
```

against a capability requiring:

```text
O_{R:B}
```

the run must say whether it is testing a forced boundary-crossing task or
accidentally importing a larger access profile. If the larger profile is merely
optional enlarged-state access, the split is absorbed by boundary relocation.

This note does not decide any active region-indexed result. It only names the
intake gate.

## Native Absorber Questions

Before assigning any residue label, ask:

1. Are `pi` and `Cap` indexed to the same access profile?
2. If not, is the mismatch the declared object of the run?
3. What relation between profiles is being tested?
4. Is the larger profile physically, operationally, or procedurally granted?
5. Would lowering `Cap` to the smaller profile collapse the spread?
6. Would enriching `pi` to the larger profile restore sufficiency through
   native state completion?
7. Does the neighboring field already treat the missing profile data as
   ordinary state, operation, boundary, or resource frame?

## Residue Discipline

Allowed labels:

```text
access-aligned projection-sufficiency failure
cross-profile insufficiency diagnostic
projection-underdescribed
native state completion
translation residue
heuristic residue
redundant or demoted
```

Blocked labels unless further work earns them:

```text
canonical residue
new physics
geometry theorem
observer-shadow theorem
novel resource distinction
```

## Relationship To The Cross-Domain Theorem Target

This note strengthens the dormant theorem target only as an audit scaffold.

It does not prove a cross-domain theorem. The only domain-independent statement
still earned is the spread criterion:

```text
For the declared O, projection sufficiency means the native capability spread
over O-visible fibers collapses under R_K,O.
```

The alignment rule makes that criterion well-typed. It does not make it
nontrivial.

## Next Bounded Artifacts

Safe follow-ups:

1. Apply this alignment rule to a GR causal-accessibility witness using the
   North Star shadow-audit template.
2. Build a tiny executable resource-preorder fixture that demonstrates the
   difference between aligned capability and cross-profile mismatch.
3. Add a checklist row to future witness templates only after the dirty active
   model/test lane is settled.

Do not update claims from this note alone.

## Short Verdict

The access-profile alignment rule is a conservative intake lemma for future
observer-shadow artifacts. It prevents profile mismatch from being misread as
projection residue and keeps the repo's current method discipline intact.
