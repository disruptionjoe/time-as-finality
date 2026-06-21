# Candidate North Star Low-Hanging Physics Patch Report v0.1

## Status

This is a patch report for the next Candidate North Star version.

It is not canon.
It is not the next draft.
It is not evidence for a physics thesis.
It does not promote physics examples to novelty claims.

Purpose:

```text
Resolve low-hanging physics cleanup items so the next Candidate North Star
version can keep the physics strong while making every physics-facing claim
typed, auditable, and harder to misread.
```

Core posture to preserve:

```text
known physics -> induced Cap -> projection sufficiency audit
```

Do not reverse this into:

```text
Cap -> known physics
```

## Executive Patch Summary

The next version should make the physics sections more technical, not more
timid.

Low-hanging patches:

1. Add a no-free-physics rule.
2. Require physical access profiles.
3. Add a gauge/relabeling invariance audit.
4. Add a known-physics-induces-Cap template.
5. Promote the strongest physics witness families.
6. Demote weak or dangerous witness families unless typed models are supplied.
7. Keep dark matter and dark energy heuristic unless they are written as typed
   model audits.

The next version should not say:

```text
physics supports the North Star
capability explains gravity
capability explains dark matter
capability explains dark energy
capability replaces physical time
```

It should say:

```text
Established physical theories induce domain-native capability objects.
The Candidate North Star audits whether observer-facing projections preserve
those objects under declared access, task, horizon, and resource boundaries.
```

## Patch 1: Add A No-Free-Physics Rule

Add this rule near the physics-forward section or witness rules:

```text
No physics-facing claim is allowed unless it can be written as:

Known theory:
Y:
X:
pi:
Cap:
K:
Equivalence on K:
Allowed operations:
Observer/access profile:
Horizon/resource boundary:
Factorization question:
Native absorber:
Not claimed:
```

Use:

```text
no_free_physics_violation
```

when a physics paragraph remains evocative but cannot fill the template.

Disposition rule:

```text
If the template cannot be filled, keep the material as intuition or heuristic
analogy. Do not treat it as a physics strongman witness.
```

## Patch 2: Require Physical Access Profiles

Add this requirement:

```text
Physics access profiles must specify physical access, not merely narrative
perspective.
```

Allowed access-profile fields include:

- local measurements only;
- detector/interface readout;
- environment or purifier access;
- joint operations;
- classical communication;
- asymptotic observer data;
- exterior-domain access;
- causal-past access;
- finite-energy operations;
- finite-time operations;
- apparatus resolution;
- boundary-condition access;
- allowed intervention class.

Use:

```text
access_profile_underdeclared
```

when a proposed physics witness says "observer" without specifying the
physical operations, measurements, region, communication, or resource boundary
that define the observer's access.

Important preservation control:

```text
Same reduced/local state should imply same strictly local operational
statistics unless extra access is declared.
```

This is especially important for quantum examples. Hidden global structure is
not local capability unless the observer can access or exploit it.

## Patch 3: Add Gauge / Relabeling Invariance Audit

Add this invariance condition:

```text
If y and y' differ only by gauge, coordinate, phase-convention, basis, or
other representational redundancy, then:

Cap(y) ~=_K Cap(y')

unless the difference changes physical access, boundary conditions, allowed
operations, or superselection/sector data rather than representation.
```

Equivalent compact form:

```text
Cap(g.y) ~=_K Cap(y)
```

for every allowed gauge/relabeling transformation `g`.

Use:

```text
gauge_variant_capability
```

when a proposed physics `Cap` changes under pure representational redundancy.

Audit questions:

- Is the distinction physical, or only a coordinate/gauge choice?
- Is `K` defined on physical equivalence classes rather than descriptions?
- Does the proposed operation respect constraints and superselection sectors?
- Does changing gauge alter the observer's real access or only the notation?

## Patch 4: Add Known-Physics-Induces-Cap Template

Use this as the default physics instantiation template:

```text
Given established physical theory P:

State_P:
Dynamics_P:
Constraints_P:
Symmetries_P:
Observers_P:
AllowedOps_P:
Boundary/resource data:

Cap_P(y; O,T,h,B) =
  admissible operation, reachability, convertibility, measurement,
  reconstruction, communication, certification, or response structure induced
  by P from state y for observer O, task family T, horizon h, and boundary B.

Projection audit:
  Does Cap_P factor through pi_P up to the declared equivalence on K?
```

Required direction:

```text
known theory P induces Cap_P
pi_P is then audited for capability sufficiency
```

Forbidden direction:

```text
invent Cap first
then imply P follows from it
```

## Patch 5: Promote Strong Physics Witness Families

These families should be promoted as the best physics-facing anchors, with
absorbers named honestly.

### 1. Quantum Resource Theory Under Explicit Access Profiles

Promote.

Best form:

```text
Y = global quantum state plus resource/access structure
X = reduced state or restricted measurement interface
pi = partial trace or allowed readout
K = resource convertibility preorder under allowed operation class R
Cap_R(y) = reachable/downset resource states under R
equivalence = mutual convertibility or declared operational equivalence
absorber = quantum information, LOCC, resource theory, channel theory
```

Required control:

```text
strictly local observer + same reduced state -> no local operational
distinction
```

Only side access, purifier access, joint operations, communication, or resource
protocols may create different future capability.

### 2. GR Causal Accessibility And Horizons

Promote.

Best form:

```text
Y = spacetime plus metric, stress-energy, global causal/boundary structure
X = local observer-visible data over patch U
pi = restriction to local observables or causal-domain readout
K = observer-indexed causal reachability / communication structure
Cap_GR(y) = future-directed causal curves, domains of dependence,
            communication possibilities, measurement trajectories, and
            reachable regions under declared constraints
absorber = standard GR causal structure
```

Good toy target:

```text
locally isometric patches with different global causal futures
```

Disposition:

```text
typed witness, likely absorbed by GR, useful as strong physics translation
```

### 3. Detector / Instrumentation Provenance

Promote as finite physics-adjacent witness.

Best form:

```text
Y = raw signal + calibration + instrument state + timing + provenance +
    uncertainty model + access rights
X = reported payload under interface Sigma
Cap = audit, challenge, recalibration, reconstruction, certification, or
      error-diagnosis operations
K = certification/audit/reconstruction capability structure
absorber = metrology, detector calibration, uncertainty quantification,
           provenance
```

Value:

```text
Concrete bridge between physics practice, database provenance, and
projection-sufficiency auditing.
```

### 4. Thermodynamic Resource Convertibility

Promote.

Best form:

```text
Y = thermodynamic/quantum thermodynamic state plus bath, work storage,
    catalysts, and boundary conditions
X = coarse thermodynamic readout
K = convertibility preorder or work/heat/resource envelope
Cap(y) = reachable states or extractable work under declared thermal
         operations
absorber = thermodynamic resource theory, nonequilibrium free energy,
           statistical mechanics
```

Required declarations:

- allowed operations;
- reservoirs/baths;
- coarse-graining;
- dissipation;
- erasure;
- finite resources;
- boundary conditions.

### 5. Condensed Matter / Topological Response

Promote as a promising future witness family.

Best form:

```text
Y = many-body state / phase / Hamiltonian with boundary conditions
X = local correlation or readout data at fixed resolution
Cap = transport response, edge-mode availability, braiding operations,
      defect manipulation, or phase-transition accessibility
K = response/operation structure under declared perturbations
absorber = topological order, response theory, condensed matter theory
```

Why it is strong:

```text
Local shadows can fail to determine global/topological operational structure,
but the native theory already knows this. Likely translation residue unless a
cross-domain theorem emerges.
```

### 6. Simulation Restart / Reconstruction / Provenance

Promote as finite physics-adjacent witness.

Best form:

```text
Y = full simulation state plus mesh, solver, timestep, random seed,
    conservation diagnostics, and boundary data
X = rendered or observer-visible field snapshot
Cap = restart, refine, continue, perturb, verify conservation, or reproduce
      simulation
K = continuation/reconstruction/reproducibility capability structure
absorber = numerical analysis, simulation provenance, reproducibility
```

Value:

```text
Excellent finite fixture for same visible field / different future operation
availability.
```

### 7. EFT / RG Preservation Controls

Promote mainly as preservation controls.

Best form:

```text
Y = UV or microscopic theory/state
X = low-energy effective description at scale Lambda
pi = coarse-graining / RG projection
Cap = admissible operations, predictions, or responses below the declared
      scale and resource boundary
K = scale-indexed predictive/operational equivalence
absorber = EFT, RG universality, relevant/irrelevant operators
```

Important positive case:

```text
If UV distinctions are irrelevant for the declared task, horizon, and energy
scale, Cap should factor through the effective description.
```

This gives physics-facing preservation examples, not only failures.

## Patch 6: Hold Or Narrow These Witness Families

### Standard Model / Particle Properties

Hold, but narrow.

Allowed framing:

```text
particle properties constrain admissible interactions
```

Avoid:

```text
charge is capability
spin is capability
mass is capability
```

Best form:

```text
Cap(y) = allowed interaction, scattering, decay, transformation, and
selection-rule structure under declared energy, representation, conservation
laws, detector context, and resolution.
```

Absorber:

```text
Standard Model representation theory, gauge theory, selection rules,
scattering theory, detector physics
```

### Black Holes

Hold as strong stress test, not standalone flagship.

Required observer split:

- infalling observer;
- exterior stationary observer;
- asymptotic observer;
- finite-time observer;
- observer with Hawking-radiation access;
- holographic boundary observer where applicable.

Do not use "reconstruction capability" without declaring the theory:

- semiclassical gravity;
- QFT in curved spacetime;
- algebraic QFT;
- holography / entanglement wedge reconstruction;
- quantum error correction.

### Time

Hold with strict boundary language.

Allowed framing:

```text
visible present records may underdetermine future operations such as
reconstruction, erasure, maintenance, intervention, or reversibility under
declared openness, coarse-graining, resource, and boundary conditions.
```

Not allowed:

```text
capability replaces physical time
observers create time
closed reversible systems generate strict finality arrows without extra
structure
```

### Emergence

Hold as translation layer.

Required fields:

- structure;
- maintenance constraints;
- environmental coupling;
- new operations;
- preserved operations;
- lost operations;
- resource costs;
- viability boundary.

Avoid:

```text
all emergence is capability expansion
```

Use:

```text
emergent structures can preserve, expand, restrict, redirect, or trade off
future operation classes.
```

## Patch 7: Demote Dark Matter And Dark Energy Unless Typed Models Exist

### Dark Matter

Default disposition:

```text
heuristic projection-insufficiency analogy
```

Reason:

```text
Dark matter is primarily omitted gravitational source structure, not hidden
capability.
```

Safe form:

```text
Y = full gravitational source structure
X = luminous/electromagnetic visible matter distribution
pi = projection to visible matter
Dyn(y) = lensing, rotation, binding, structure formation
optional Cap(y) = gravitationally possible future trajectories or interactions
K = gravitational-dynamical consequence structure
absorber = astrophysical mass modeling, lensing, galactic dynamics, cosmology
```

Required wording:

```text
Dark matter does not show that hidden capability exists. It shows that
luminous visible state is not a sufficient invariant for gravitational
dynamical futures under known astrophysical modeling.
```

Promote only if a typed model supplies:

- `Y`;
- `X`;
- `pi`;
- `Dyn` or `Cap`;
- `K`;
- equivalence on `K`;
- observer/access profile;
- native absorber;
- preservation and failure controls.

### Dark Energy

Default disposition:

```text
future-causal-accessibility analogy
```

Reason:

```text
Dark energy should not be framed as capability explaining accelerated
expansion.
```

Safe form:

```text
Y = global cosmological spacetime with expansion history and model parameters
X = observer-visible cosmological data within a horizon
pi = restriction/inference from accessible cosmological observations
Cap_cosmo = future causal contact, observability, communication, and
            structure-formation accessibility
K = long-horizon causal-contact / reachability structure
absorber = FLRW cosmology, causal horizons, structure formation,
           observational cosmology
```

Required wording:

```text
Accelerated expansion changes long-run causal accessibility in standard
cosmology. Capability language audits that induced accessibility object; it
does not explain the cause of acceleration.
```

Promote only if a typed cosmological model supplies:

- cosmological model class;
- parameter-estimation assumptions;
- observer location/access;
- horizon/resource boundary;
- `Cap_cosmo`;
- equivalence on future accessibility;
- absorber;
- not-claimed boundary.

## Patch 8: Add Physics Failure Labels

Add these labels beside the existing `gerrymandered_capability` and
`same_visible_state_underspecified` labels:

```text
no_free_physics_violation
access_profile_underdeclared
gauge_variant_capability
local_capability_smuggling
physics_direction_reversal
typed_model_missing
```

Definitions:

```text
local_capability_smuggling
```

Use when inaccessible global structure is counted as part of a local
observer's capability without a declared access route.

```text
physics_direction_reversal
```

Use when the text implies that capability explains or derives known physics,
rather than known physics inducing a capability object.

```text
typed_model_missing
```

Use when a physics witness is promoted without enough typed fields to run the
projection-sufficiency audit.

## Patch 9: Add A Physics Reviewer Checklist

Add this compact checklist:

```text
Known theory named?
Y domain-native?
X observer-visible?
pi declared?
K typed?
equivalence on K fixed?
Cap induced by known physics?
allowed operations declared?
access profile physical?
horizon/resource boundary fixed?
same-visible-state context sufficient?
gauge/relabeling invariant?
strictly local controls included where relevant?
native absorber named?
not-claimed boundary explicit?
residue label honest?
```

## Recommended Next-Version Placement

Suggested locations:

1. Put the no-free-physics rule in the witness-rules or physics-forward
   section.
2. Put the known-physics-induces-Cap template before the individual physics
   examples.
3. Put access-profile and gauge-invariance requirements in the same-visible
   state discipline section.
4. Put witness promotions/demotions in a physics strongman appendix or queue
   note, not in the formal core.
5. Put the dark matter / dark energy demotions directly in their respective
   sections if those sections remain.

## Minimal Insert Candidate

If the next version needs one compact insert, use:

```text
Physics-facing claims must derive Cap from established physical theory, not
derive physics from Cap. For every physics section, declare the known theory,
state space, observer/readout projection, allowed operations, access profile,
horizon/resource boundary, capability object, equivalence on capability,
native absorber, and not-claimed boundary. Any capability distinction must be
invariant under gauge, coordinate, and relabeling redundancy, and must not
count inaccessible global structure as local observer capability. Dark matter
and dark energy remain heuristic unless supplied as typed model audits.
```

## Bottom Line

The low-hanging physics cleanup is not to weaken the physics.

It is to make every physics-facing claim pass this discipline:

```text
known physics induces a typed capability object;
observer access determines what part of that object is operational;
gauge/relabeling redundancy cannot create fake capability differences;
projection sufficiency is then audited honestly;
native absorbers get credit;
dark matter and dark energy stay demoted unless typed models exist.
```
