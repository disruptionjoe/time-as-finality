# Capability Projection Schema v0.1

## Status

This is a Candidate North Star schema note.

It is not canon.
It is not a claim update.
It is not a roadmap commitment.
It is not paper-ready.
It is not evidence for the Candidate North Star.

Purpose:

```text
Make capability projection testable before it becomes persuasive.
```

Governing principle:

```text
No capability distinction counts unless Cap was typed, indexed, and
equivalenced before the witness verdict.
```

## Headline Statement

For fixed observer, task, horizon, and resource boundary:

```text
future capability need not factor through observer-visible state
```

Formal shape:

```text
pi_{O,Sigma,r,U} : Y -> X_{O,Sigma,r}(U)

Cap_{O,T,h,B} : Y -> K_{O,T,h,B}
```

Question:

```text
Does Cap factor through pi up to the declared capability equivalence on K?
```

If yes:

```text
the visible state is sufficient for that capability question
```

If no:

```text
the projection is capability-nondetermining for that capability question
```

## Objects

### Source Structure

```text
Y
```

The richer source structure. It may include physical state, history, provenance,
resource state, hidden correlation, access rights, environmental structure,
or other domain-native data.

`Y` is not assumed to be ontologically ultimate. It is simply the richest state
space admitted by the test.

### Visible Projection

```text
pi_{O,Sigma,r,U} : Y -> X_{O,Sigma,r}(U)
```

Indices:

```text
O      observer or access profile
Sigma  observational schema or interface
r      resolution, fidelity, or coarse-graining level
U      local domain, patch, or scope
```

The projected state:

```text
x = pi_{O,Sigma,r,U}(y)
```

is the observer-facing shadow used in the comparison.

### Capability Object

```text
Cap_{O,T,h,B}(y)
```

Indices:

```text
O  observer or access profile
T  task family
h  horizon
B  budget, boundary, or resource condition
```

Default audit type:

```text
indexed preorder of admissible future operations
```

Interpretation:

```text
a <= b
```

means operation/capability `b` is at least as capable, reachable, dominant,
or convertible as `a` under the declared domain convention.

The preorder is the default audit interface, not the final ontology.

## Domain-Native Structures

Some domains already provide better native structure. They may be mapped into
the indexed-preorder interface for cross-domain comparison.

| Domain | Native structure | Mapping into audit interface |
| --- | --- | --- |
| Git/provenance | graph or category of transformations | preorder of available operations |
| detector packets | admissibility/challenge/access rights | preorder of permitted audits and interventions |
| POMDPs | belief-state/update object | preorder over policies, values, or reachable beliefs |
| control theory | reachable/controllable state set | preorder by reachability or dominance |
| resource theory | convertibility preorder/category | native preorder, possibly enriched |
| quantum theory | operational/resource structure | preorder under allowed operation class |
| sheaf examples | sections, restrictions, obstruction data | preorder of extend/reconstruct/glue operations |
| viability theory | viability kernel / reachable set | inclusion or dominance preorder |
| access control | permissions and future rights | preorder of authorized operations |

## Capability Equivalence

Every audit must declare an equivalence relation or equivalence criterion on
the capability structure.

Examples:

```text
equal operation sets
mutual reachability in a preorder
order isomorphism
bisimulation equivalence
policy/value equivalence
resource convertibility equivalence
same viability kernel
same permitted audit/challenge rights
same reconstruction/gluing capability
```

Notation:

```text
Cap(y1) ~=_K Cap(y2)
```

means the two capability objects are equivalent under the declared equivalence
on `K`.

## Factorization Up To Equivalence

Strict factorization:

```text
Cap = Cbar o pi
```

is usually too strict. Use factorization up to declared capability equivalence.

Definition:

`Cap` factors through `pi` up to equivalence when there exists:

```text
Cbar : X_{O,Sigma,r,U}(U) -> K_{O,T,h,B}
```

such that for every admissible source state `y`:

```text
Cap_{O,T,h,B}(y) ~=_K Cbar(pi_{O,Sigma,r,U}(y))
```

Equivalent finite test:

For every pair `y1`, `y2`:

```text
pi(y1) = pi(y2)
```

implies:

```text
Cap(y1) ~=_K Cap(y2)
```

If a counterexample pair exists, then `pi` is capability-nondetermining for the
declared capability question.

## Non-Arbitrariness Conditions

A capability witness is admissible only when these are fixed before the verdict.

1. Operation grammar.
2. Task family `T`.
3. Observer/access profile `O`.
4. Horizon `h`.
5. Budget, boundary, or resource condition `B`.
6. Capability structure `K`.
7. Capability equivalence `~=_K`.
8. Source state space `Y`.
9. Projection `pi`.
10. Positive controls where factorization should hold.
11. Negative controls where factorization should fail.
12. Absorbing prior-art frameworks and their allowed state.

If these are chosen after seeing the pair `y1`, `y2`, the example does not
count.

## Same-Neighbor-Data Condition

Before claiming residue beyond prior art, each neighboring framework must
receive the data it legitimately treats as state.

For example:

| Neighbor | Must be allowed to use |
| --- | --- |
| POMDP | belief state, history, transition model, observation model |
| control theory | latent state, output map, dynamics, control inputs |
| resource theory | allowed operations, free states, monotones, catalysts if admitted |
| causal inference | graph class, latent confounding assumptions, interventions |
| provenance | history, dependency graph, signatures, authority domains |
| access control | permissions, roles, policies, revocation/challenge state |
| abstract interpretation | abstraction/concretization maps, fibers, invariants |
| sheaf theory | cover, sections, restriction maps, coefficient system |
| viability theory | constraints, dynamics, horizon, viability kernel |

Same-neighbor-data witness:

```text
Two cases are equivalent under each neighbor's legitimate state representation,
but differ under the declared Cap audit.
```

If a neighbor can distinguish the cases using its legitimate state, record:

```text
absorbed by neighbor
```

not:

```text
North Star residue
```

## Verdicts

Every audit should return exactly one primary verdict.

| Verdict | Meaning |
| --- | --- |
| `factors` | `Cap` factors through `pi` up to declared equivalence. |
| `non_factorizing` | same visible state can carry inequivalent `Cap`. |
| `under_typed` | `Cap`, equivalence, or indices were not fixed enough. |
| `absorbed` | prior art explains the distinction with its legitimate state. |
| `invalid_witness` | visible states differ, controls fail, or verdict was post hoc. |

Optional secondary labels:

```text
positive_control_passed
negative_control_passed
same_neighbor_data_passed
physics_analogy_only
```

## Positive Controls

A serious schema must recognize cases where projection is sufficient.

Required early positive controls:

1. Fully observed deterministic finite state.
2. Sufficient statistic for a fixed decision problem.
3. Bisimulation-preserving abstraction.
4. Complete resource monotone for a tiny resource fixture.
5. Full detector packet containing all admissibility fields.
6. Full provenance graph for a Git operation-right fixture.

If the schema cannot produce `factors` in obvious preservation cases, it is not
falsifiable.

## Negative Controls

Required early negative controls:

1. Same endpoint Git tree with different history-dependent recovery rights.
2. Same detector payload with different packet wrapper/admissibility rights.
3. Same reduced quantum state with different global resource capability, but
   only under an access profile that includes joint operations or side access.
4. Same coarse reachable state with different viability kernel.
5. Same local section with different extend/reconstruct/glue capability.

If a negative control depends on post hoc capability labels, mark it invalid.

## Quantum Caveat

Same reduced density matrix does not automatically mean different capability
for the same observer.

For a strictly local observer with no side access:

```text
different purifications may be operationally unavailable
```

Capability may differ only when the access profile includes:

- purifying system access;
- joint operations;
- side information;
- future interaction with environment;
- entanglement-conversion rights;
- resource-theoretic protocols that expose the global distinction.

This caveat is mandatory in quantum examples.

## Physics Quarantine

Physics sections are not support for this schema.

They are:

- analogy;
- stress tests;
- borrowed constraints;
- examples of projection insufficiency.

They are not:

- evidence for the Candidate North Star;
- replacements for known physics;
- explanations of gravity, dark matter, dark energy, black holes, quantum
  theory, or time.

Every physics use must state:

```text
Known physics
Safe bridge
Not claimed
Test route
Falsifier / likely absorber
```

## Minimal Audit Template

```text
Name:

Source Y:
Visible X:
Projection pi:

Observer/access O:
Schema Sigma:
Resolution r:
Domain U:

Task family T:
Horizon h:
Budget/boundary/resource B:

Capability type K:
Capability equivalence ~=_K:
Operation grammar:

Candidate pair y1, y2:
Check pi(y1) = pi(y2):
Check Cap(y1) ~=_K Cap(y2):

Factorization verdict:
Positive controls:
Negative controls:

Neighbor frameworks considered:
Same-neighbor-data passed?:
Absorber:
Residue:

Final verdict:
```

## Decision Gate

After three finite negative witnesses and three positive controls, decide:

1. distinct schema;
2. translation layer;
3. absorbed vocabulary.

Default expectation:

```text
translation layer or absorbed vocabulary
```

Distinct-schema status requires at least one same-neighbor-data witness that
survives prior-art absorption.

## Bottom Line

This schema does not try to prove the Candidate North Star.

It tries to make the Candidate North Star easier to kill cleanly.

That is the point.
