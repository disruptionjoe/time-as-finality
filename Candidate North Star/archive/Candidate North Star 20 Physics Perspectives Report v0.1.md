# Candidate North Star: 20 Physics Perspectives Report v0.1

## Status

This is a companion review for:

```text
Candidate North Star v0.3.md
Candidate North Star Mathematical Strengthening Suggestions v0.1.md
Candidate North Star 20 Mathematics Perspectives Report v0.1.md
Candidate North Star Next Version Update Queue v0.4.md
```

It does not update canon.
It does not promote the Candidate North Star.
It does not claim new physics.
It does not treat physics analogies as evidence.

Purpose:

```text
Use 20 distinct physics expert personas to review the mathematical
strengthening direction and identify what must be fixed before the next
Candidate North Star version.
```

## Executive Synthesis

The physics panel agrees with the mathematics reports:

```text
known physics -> induced capability object -> projection sufficiency audit
```

is the safe bold direction.

The reverse direction:

```text
capability geometry -> known physics
```

is not earned.

The strongest physics-facing version is:

```text
Given a physical theory with states, dynamics, symmetries, constraints,
allowed operations, observers, and resource/access boundaries, define the
domain-native capability object induced by that theory. Then ask whether a
declared observer-facing projection preserves that object.
```

The recurring physics warning is:

```text
do not smuggle inaccessible global structure into the local observer's Cap
```

The recurring strengthening is:

```text
make every physics section define Y, X, pi, Cap, K, equivalence, allowed
operations, observer access, horizon, absorber, and not-claimed boundary.
```

## Cross-Cutting Physics Requirements

## 1. No Free Physics

Every physics-facing claim must use:

```text
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

If a section cannot fill those fields, keep it as intuition, not as a
physics-facing strongman.

## 2. Access Profiles Must Be Physical

An observer/access profile cannot be arbitrary prose.

It must specify physical access such as:

- local measurements only;
- access to an environment or purifier;
- joint operations;
- asymptotic observer data;
- exterior-domain access;
- causal-past access;
- finite-energy operations;
- finite-time operations;
- apparatus resolution;
- classical communication;
- allowed intervention class.

## 3. `Cap` Must Be Induced By The Theory

For physics sections, prefer:

```text
Cap_P(y; O,T,h,B)
```

where `P` is an established physical theory or model class.

`Cap_P` should be built from:

- dynamics;
- constraints;
- symmetries;
- conservation laws;
- causal structure;
- allowed operations;
- resource constraints;
- measurement interfaces;
- boundary conditions.

## 4. Gauge And Coordinate Redundancy Must Not Change Capability

If:

```text
y ~ gauge y'
```

then:

```text
Cap(y) ~=_K Cap(y')
```

unless the "difference" changes observer access, boundary conditions, or
physical operation class rather than mere representation.

Add an explicit invariance audit to all physics-facing examples.

## 5. Local Equality Must Not Hide Boundary Conditions

Physics examples often fail because:

```text
same local visible patch
```

does not specify:

- boundary conditions;
- global topology;
- asymptotic structure;
- environment state;
- gauge sector;
- superselection sector;
- energy/momentum constraints;
- horizon/access domain;
- measurement context.

Use:

```text
same_visible_state_underspecified
```

when these are missing.

## 20 Physics Personas

## 1. General Relativist / Causal Geometer

Review:

The gravity section is on the right track if `Cap` is causal accessibility,
not "gravity as capability." The domain-native object is causal structure:
future sets, causal curves, domains of dependence, horizons, and global
hyperbolicity conditions.

Needed update:

```text
Cap_GR(y) = observer-indexed causal reachability / communication /
measurement-trajectory structure under declared horizon and resource bounds.
```

Weak point:

Local observational agreement does not define a GR state. If the example uses
"same local patch," it must say whether global topology, boundary conditions,
asymptotics, and stress-energy outside the patch are included or excluded.

Absorber:

Standard GR causal structure.

Potential proof target:

Construct a toy GR/causal-spacetime pair with locally isometric patches but
different global causal futures for an observer. Mark it as absorbed by GR,
but useful as a typed witness.

## 2. Relativistic Field Theorist

Review:

Capability should be attached to local algebras or field configurations only
after specifying the region, dynamics, symmetries, and allowed operations.

Needed update:

For relativistic fields:

```text
Y = field state plus boundary/asymptotic data
X = local observable algebra or detector readout over region U
pi = restriction to local algebra/readout
Cap = operations/measurements/scattering preparations allowed from that state
K = operational equivalence class under declared field theory
```

Weak point:

Do not let `Cap` distinguish gauge-equivalent field descriptions.

Absorber:

Algebraic QFT, local observables, scattering theory, and gauge theory.

## 3. Quantum Information / Resource Theorist

Review:

The quantum section should be one of the strongest, but only under strict
access profiles. Same reduced density matrix gives the same strictly local
statistics. Differences require side access, joint operations, purification
access, communication, or resource protocols.

Needed update:

Use resource convertibility as default:

```text
K = convertibility preorder under allowed operation class R
Cap_R(y) = downset or reachable resource states under R
```

Weak point:

"Hidden global resource" is not operational capability unless the observer can
access or exploit it.

Absorber:

Quantum resource theory, LOCC, purification/HJW-style results, channel theory.

Potential proof target:

Same reduced state, different global resource capability under explicitly
different access profiles. Include the strictly local preservation control.

## 4. Quantum Foundations / Measurement Theorist

Review:

Measurement examples must distinguish epistemic update, physical disturbance,
postselection, decoherence, and future reversibility. "Same outcome" is not
enough.

Needed update:

Declare whether `Cap` is:

- future reversibility;
- distinguishability;
- compatible future measurements;
- reconstruction;
- intervention capability;
- certification capability.

Weak point:

Do not conflate outcome equivalence with state equivalence, and do not treat
counterfactual global state as local capability.

Absorber:

Quantum operations, POVMs, instruments, decoherence theory, resource theory.

## 5. Condensed Matter / Topological Phases Physicist

Review:

Condensed matter is a promising physics-facing domain because local observables
can fail to determine global/topological order, edge modes, or response
capability.

Needed update:

Add a possible future physics witness class:

```text
Y = many-body state / phase / Hamiltonian with boundary conditions
X = local correlation/readout data at fixed resolution
Cap = transport response, edge-mode availability, braiding operations, defect
      manipulation, or phase-transition accessibility
K = response/operation structure under declared perturbations
```

Weak point:

Must compare against existing topological order and response theory. This is
likely translation residue unless a cross-domain theorem emerges.

Potential value:

Better physics strongman than dark matter for "local shadow does not determine
global operational structure."

## 6. Particle Phenomenologist

Review:

The Standard Model section should focus on allowed interactions and scattering
channels, not metaphysical capability.

Needed update:

For particle examples:

```text
Cap(y) = allowed interaction/scattering/decay channels under declared energy,
conservation laws, representations, and detector context
```

Weak point:

"Same detector signature" is not enough. Detector resolution, background
model, event reconstruction, and quantum numbers must be declared.

Absorber:

Standard Model representation theory, selection rules, scattering theory, and
detector physics.

## 7. Gauge Theorist

Review:

Gauge redundancy is the fastest way for physics critics to attack the draft.
Capability must be invariant under gauge transformations.

Needed update:

Add a physics invariance condition:

```text
Cap(g.y) ~=_K Cap(y)
```

for gauge transformations `g`.

Weak point:

If a proposed capability distinction changes under gauge choice, it is not
physical.

Absorber:

Gauge theory, constraint reduction, physical observables, representation
theory.

## 8. Black Hole / Quantum Gravity Physicist

Review:

Black holes are a strong stress test for observer-indexed operation
availability, but not evidence for the North Star.

Needed update:

Specify observer class:

- infalling observer;
- exterior stationary observer;
- asymptotic observer;
- finite-time observer;
- observer with access to Hawking radiation;
- observer with full boundary theory in holographic settings.

Weak point:

"Reconstruction capability" is theory-dependent. In semiclassical gravity,
QFT in curved spacetime, and holography, the native absorbers differ.

Absorber:

Horizon causal structure, algebraic QFT, quantum information, holographic
reconstruction where applicable.

## 9. Cosmologist

Review:

The cosmology/dark energy section is safe if it talks about causal contact and
horizon-limited future accessibility. It becomes unsafe if it sounds like a
new explanation of acceleration.

Needed update:

Define:

```text
Cap_cosmo = future causal contact, observability, communication, and
structure-formation accessibility under a declared cosmological model
```

Weak point:

Observer-visible cosmological data is model-dependent and inference-laden.
The projection must include parameter-estimation assumptions.

Absorber:

FLRW cosmology, causal horizons, structure formation, observational cosmology.

## 10. Astrophysicist / Dark Matter Specialist

Review:

Dark matter is a good cautionary analogy but a weak flagship witness. It is a
case of omitted source structure, not mysterious capability.

Needed update:

Use `Dyn` before `Cap` unless the capability is explicitly gravitational
future trajectories:

```text
Dyn(y) = lensing, rotation, binding, structure formation
```

then optionally:

```text
Cap(y) = gravitationally possible future trajectories/interactions
```

Weak point:

Do not imply dark matter is hidden capability.

Absorber:

Standard astrophysical mass modeling, lensing, galactic dynamics, cosmology.

## 11. Statistical Mechanics / Thermodynamics Physicist

Review:

Time and emergence sections must respect coarse-graining, entropy production,
openness, and boundary conditions.

Needed update:

Any directional capability claim must name:

- coarse-graining;
- erasure;
- dissipation;
- reservoir/bath;
- boundary condition;
- nonstationarity;
- entropy production;
- finite resources.

Weak point:

Closed reversible systems do not give strict capability arrows without
additional structure.

Absorber:

Statistical mechanics, thermodynamics, nonequilibrium physics, resource
theories of thermodynamics.

## 12. Quantum Thermodynamics Physicist

Review:

Capability language maps naturally to thermodynamic resource theories, work
extraction, state transformations, catalysts, and thermal operations.

Needed update:

For thermodynamic examples:

```text
K = thermodynamic convertibility preorder or work/heat/resource envelope
Cap(y) = reachable states or extractable work under allowed thermal operations
```

Weak point:

Must declare allowed operations. Different thermodynamic resource theories
give different `Cap`.

Absorber:

Thermodynamic resource theory and nonequilibrium free energy.

## 13. Dynamical Systems / Chaos Physicist

Review:

Projection insufficiency is old in dynamical systems. Same coarse observation
can hide different future trajectories.

Needed update:

Use:

```text
Cap(y) = reachable/predictable/control-relevant future set over horizon h
```

and compare against:

- observability;
- delay embeddings;
- Koopman observables;
- invariant manifolds;
- symbolic dynamics.

Weak point:

If the point is only "coarse-graining loses predictive information," it is
fully absorbed.

Potential value:

Use dynamical systems for quantitative capability spread over fibers.

## 14. Plasma / Nonlinear Systems Physicist

Review:

Plasma and nonlinear systems expose capability dependence on instabilities,
boundary driving, and multiscale coupling. Same coarse state may support
different reachable regimes if hidden modes differ.

Needed update:

Require:

- boundary driving;
- field configuration;
- conserved quantities;
- stability regime;
- scale separation;
- dissipative terms.

Weak point:

Without equations and boundary conditions, the example is rhetoric.

Absorber:

MHD, kinetic theory, nonlinear stability, control of PDEs.

## 15. Experimental Detector / Instrumentation Physicist

Review:

Detector examples are strong because "same payload" is visibly insufficient
unless calibration, provenance, timing, resolution, and authority are included.

Needed update:

For detector packets:

```text
Y = raw signal + calibration + instrument state + timing + provenance +
    access rights
X = reported payload under interface Sigma
Cap = audit, challenge, recalibration, reconstruction, or certification rights
```

Weak point:

If calibration/provenance is legitimate state, many examples are absorbed by
instrumentation and metrology.

Absorber:

Metrology, detector calibration, uncertainty quantification, provenance.

## 16. Computational Physicist / Simulation Expert

Review:

Simulation states make projection sufficiency very concrete: same rendered
state can hide different mesh, solver, random seed, timestep, or conservation
errors.

Needed update:

Add as finite physics-adjacent witness:

```text
Y = full simulation state plus solver metadata
X = rendered/observable field snapshot
Cap = restart, refine, verify conservation, perturb, or continue simulation
```

Weak point:

Mostly absorbed by numerical analysis and reproducibility standards.

Value:

Excellent finite bridge between database/log/provenance witnesses and physics
practice.

## 17. Mathematical Physicist

Review:

The mathematics should use descent, quotient, fibration, and resource
structures cleanly. Avoid decorative geometry.

Needed update:

Add:

```text
source fiber = pi^{-1}(x)
capability spread = { Cap(y) | y in pi^{-1}(x) } / ~=_K
capability fiber = fiber of a capability fibration, only if a fibration is
actually defined
```

Weak point:

The word "fiber" can become ambiguous between source fibers and capability
fibers.

Absorber:

Standard quotient/descent/fibration theory.

## 18. Holography / Quantum Information Gravity Persona

Review:

Holography complicates black hole capability claims because boundary data may
encode bulk information nonlocally. Observer/access profile is everything.

Needed update:

For holographic language, declare:

- boundary region;
- code subspace;
- reconstruction wedge;
- allowed boundary operations;
- error-correction assumptions.

Weak point:

Exterior-visible data may not mean the same thing in semiclassical and
holographic formulations.

Absorber:

Entanglement wedge reconstruction, quantum error correction, holographic
duality.

## 19. Effective Field Theory / Renormalization Persona

Review:

Projection and coarse-graining are native to EFT/RG. Same low-energy effective
description can hide UV differences that may or may not matter for future
capability at a given scale.

Needed update:

Add a scale discipline:

```text
observer resolution r
task horizon h
energy scale Lambda
allowed operations below/above Lambda
```

Weak point:

If UV distinctions are irrelevant under RG for the declared task, `Cap` should
factor through the effective description.

Absorber:

EFT, RG universality, relevant/irrelevant operators.

Potential strength:

Great source of preservation controls: different microstates, same effective
capability at scale.

## 20. Complex Systems / Emergence Physicist

Review:

Emergence should be framed as platform capability under constraints, not as a
universal capability expansion story.

Needed update:

Require:

```text
structure
maintenance constraints
environmental coupling
new admissible operations
preserved operations
lost operations
resource costs
```

Weak point:

Some emergent structures restrict capability while enabling new higher-level
operations. The preorder may be partial, not monotone expansion.

Absorber:

Viability theory, affordance theory, major transitions, niche construction,
renormalization, resource theory.

## Cross-Persona Rankings

## Strongest Physics-Facing Anchors

1. Quantum resource theory under explicit access profiles.
2. GR causal accessibility and horizons.
3. Detector/instrumentation provenance.
4. Thermodynamic/resource-theoretic convertibility.
5. Condensed matter/topological response and edge/defect operations.
6. Simulation restart/reconstruction/provenance.
7. EFT/RG preservation controls.

## Weakest Or Most Dangerous Anchors

1. Dark matter as more than projection-insufficiency analogy.
2. Dark energy as anything beyond future causal accessibility.
3. Time as replacement for physical time.
4. Particle properties described as "capability" rather than constraints on
   admissible interactions.
5. Black hole reconstruction without specifying observer/access theory.
6. Any quantum example that ignores strictly local operational equivalence.

## Needed Updates To Queue

1. Add the physics review as a required input before the next version.
2. Add a no-free-physics rule.
3. Add a physics access-profile requirement.
4. Add a gauge/relabeling invariance audit.
5. Add a "known physics induces Cap" template.
6. Add condensed matter/topological phases as a possible strong physics
   witness family.
7. Add EFT/RG as a preservation-control source.
8. Add detector/instrumentation provenance as a finite physics-adjacent
   witness.
9. Add simulation/restart/provenance as a finite physics-adjacent witness.
10. Downgrade dark matter and dark energy to heuristic physics analogies unless
    a typed model is produced.

## Proposed Insert For The Next Queue

```text
Physics-facing claims must derive Cap from established physical theory, not
derive physics from Cap. For each physics section, declare the physical theory,
state space, observer/readout projection, allowed operations, resource/access
constraints, capability object, equivalence on capability, native absorber, and
not-claimed boundary. Any capability distinction must be invariant under gauge
or coordinate redundancy and must not smuggle inaccessible global structure
into a local observer's capability set.
```

## Bottom Line

The 20 physics perspectives agree:

```text
keep the physics strong
make it more technical
derive capability from known physics
audit projection sufficiency
do not claim physics follows from capability
```

This preserves ambition without giving hostile physicists an easy target.

