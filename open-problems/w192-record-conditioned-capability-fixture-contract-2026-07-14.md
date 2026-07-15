# W192 Record-Conditioned Capability Fixture Contract

## Status

Action-4 fixture implemented and independently verified. T581 remains the
already selected closeout router and T582 is the separate W192 gate. No claim,
Canon Index, steering, or cross-repo truth movement is earned.

## Frozen cases

Both cases share the written W192 proxy, source family, region identifier, and
intervention menu. The before case has no accessible `psi`. The after case is
given the frozen K-positive `psi`. Both explicitly record that the fixed source
family already contains spinor states and that no generation evidence or
physical boundary witness exists.

Keep state existence, formation, and access separate:

```text
psi_exists
psi_access
psi_identifier
psi_provenance
formation_mode
formation_evidence_hash
action_or_EL_residual
boundary_data_hash
gauge_orbit_identifier
```

Frozen W192 is delayed access to a state inside a fixed family. A later
W195-like packet may propose endogenous formation and must not be forced into
the delayed-access schema.

The region record must expose access-complete shadow fields, including
`psi_access`, identifier, and provenance. It must leave causal domain, observer
worldline, horizon, cadence, thermodynamic and information ledgers, resource
cost, gluing, gauge quotient, and physical boundary witness absent until
evidence supplies them. The algebraic observer section is not a TaF causal
region.

## Fixed menu and tasks

Use the same menu before and after:

1. construct a state-independent Spin(9,5)-equivariant proxy lift
   `L0: V -> V tensor S`;
2. form the record-conditioned vertex lift `L_psi(e_mu)=e_mu psi`;
3. for an independently supplied `v`, certify existence of a written-shiab
   preimage and its fiber dimension;
4. evaluate only the operator spectrum/rank drop of the written proxy shell;
5. construct a typed adjoint current and adapter;
6. apply the joint gauge quotient;
7. test current/carrier overlap;
8. test an independent rank/minor holdout;
9. measure a native retarded current response.

Expected current results:

| Task | Before | After |
| --- | --- | --- |
| state-independent proxy lift `V -> V tensor S` | exact fail | exact fail |
| record-conditioned vertex lift | missing resource | proxy pass |
| arbitrary-`v` written-shiab preimage | surjective pass, 256-dimensional fiber | same |
| operator-only proxy shell | proxy pass | proxy pass |
| typed adjoint current/adapter | unavailable | unavailable |
| joint quotient and overlap | unavailable | unavailable |
| independent holdout | unavailable | unavailable |
| retarded response | unavailable | unavailable |

Only the record-conditioned vertex lift changes, and it is decided completely
by `psi_access`. The exact proxy failure does not decide a native
`Lambda^2 H tensor ad(P) -> H tensor ad(P)` map. The lift family is covariant as
`L_{g psi}(g v)=g L_psi(v)` and, for frozen `psi`, equivariant only under its
stabilizer. It does not choose a curvature preimage.

The arbitrary-`v` task must not use `v(psi)`. If it does, the before case is
unavailable and it creates a second access-dependent delta. The shell task is
operator-only and excludes the state-dependent statement that the record
vertex sees the shell.

## Equality certificates

Emit separate certificates for:

- structural observation equality: passes;
- access-complete observation equality: fails because the capability-deciding
  resource differs;
- all region-supported intervention equality: fails or remains unavailable
  because the record-conditioned intervention and response model are absent
  before the event.

Structure-only equality is underdescribed and cannot support a capability
claim.

## Immediate controls

Run no-psi/no-psi and psi/psi no-difference controls; exact proxy-lift failure;
arbitrary-`v` lift; identical proxy-shell output; fixed richer-source delayed
access; completed-shadow state access; changed-menu completion; missing native
response; Action-2-only and Action-3-only dependency controls.

## Evidence interfaces

A future physically forced boundary must declare E1 asymptotic, E2 hardness, or
E3 structural-symmetry mode and carry the task-relevant source law and optional
generation map, Hamiltonian/action, causal region, boundary event, state
formation/access status, resource/conservation ledger, fixed-source null,
Action-3 nonreproduction, completion nonadmissibility, perturbation
preservation, and evidence hashes.

Stage the native-response interface:

1. `TYPE_ADMISSIBLE`: gauge scope (`full_native`, `embedded_subalgebra`, or
   `proxy`), representation/embedding, real action, correctly indexed
   `g*`-valued variational current, declared nondegenerate invariant form,
   Ward certificate, state provenance, adapter, and identity-claim status.
2. `QUOTIENT_RESPONSE_READY`: joint gauge quotient, current/carrier overlap,
   selector ledger, independent holdout, and rival construction.
3. `RETARDED_PHYSICS_READY`: Hamiltonian/kinetic operator, retarded
   prescription, `rho_J`, pole sheets, thresholds, interacting C metric, and
   perturbative stability.

Only stage 3 can support a physical-response reading. An embedded-subalgebra
packet may reach stages 1 or 2 without being mislabeled full native or physical.
The connection generators or raised algebra representative are even and
K-anti; the current coefficients remain `g*`-valued until the invariant form is
applied.

## Absorber matrix

Readout, explicit state, description, fixed-source, resource/competency, and
latch/substrate completion fire now. Joint record and finality label fire
conditionally. Causal domain and gauge/basis are not testable. Menu completion
fires if the menu changes. Law-sector completion is not defeated. Spectral
dynamics blocks the physical reading.

## Verdict lattice

Apply, in order:

```text
invalid schema
no capability difference
explicit state/resource completion
shadow equality not earned
declared boundary only
waiting Action 2
waiting Action 3
absorbed by named absorber
formal candidate missing native response
physically forced capability review candidate
```

The maximum result is review-candidate status.

Current expected verdict:

```yaml
verdict: EXPLICIT_STATE_RESOURCE_COMPLETION
capability_delta: [record_conditioned_vertex_lift]
deciding_fields: [psi_access, psi_identifier]
fixed_source_null_reproduces: true
positive_capability_verdict_allowed: false
```

## Deterministic output and tests

Produce stable sorted JSON containing the frozen packet, cases, region, menus,
task results, capability delta, equality certificates, controls, boundary and
native-response evidence, absorber matrix, dependencies, verdict trace,
blockers, claim labels, and not-claimed list.

Tests must pin the current W192 classification; exact one-task delta; proxy
lift, vertex-lift family covariance/stabilizer scope, arbitrary-`v` versus
`v(psi)` preimage, and operator-only versus source-visible shell controls;
failed access-complete equality; fixed-source
reproduction; separate Action-2 and Action-3 blocks; absorber precedence; and a
synthetic complete case that reaches at most review-candidate status.

Mutation tests must also prove that the proxy central failure does not fail the
`ad(P)` task, an embedded-subalgebra packet is not labeled full native, and a
typed quotient-ready packet without `rho_J` cannot reach physical-response
status.

Recommended post-T581 slug:

```text
w192_record_conditioned_capability_discriminator_gate
```

## Verification receipt

Executed serially on 2026-07-14 with bytecode disabled:

- T581 result generation completed and its focused suite passed 7 of 7 tests;
- T582 result generation completed and its focused suite passed 10 of 10 tests;
- the corrected combined T580/T581/T582 regression passed 25 of 25 tests;
- an initial combined command used a nonexistent T580 module name and failed
  at import only; the repository's actual T580 test module was located and the
  full corrected regression passed.

The verified result remains `EXPLICIT_STATE_RESOURCE_COMPLETION`. Exactly the
record-conditioned vertex-lift task changes, `psi_access` and `psi_identifier`
decide it, fixed-source completion reproduces it, and type, quotient, and
retarded-physics readiness remain false.
