# Candidate North Star v0.6 - GU Mismatch and Open-Gap Report v0.1

## Status

This is a companion audit for:

```text
Candidate North Star v0.6.md
```

It does not update canon.
It does not validate Geometric Unity.
It does not reject Geometric Unity.
It does not promote Capability Projection into a physics program.

Purpose:

```text
Check whether the GU-facing mathematical story is mismatched with Candidate
North Star v0.6, and classify the remaining open issues as potential errors,
gaps, inconsistencies, or work still needed.
```

## Executive Answer

No direct mathematical contradiction was found between Candidate North Star
v0.6 and the repo's conservative GU posture, provided the following boundary is
kept:

```text
established physics or a declared GU model -> typed Cap -> projection
sufficiency audit
```

The dangerous reversal is:

```text
Capability Projection or TaF intuition -> known physics
```

That reversal would conflict with v0.6's no-free-physics rule.

The main mismatch risk is not the use of GU's geometry itself. The main risk is
treating GU's speculative physical interpretation as if it were already an
established source of physical capability objects. The repo's GU notes mostly
avoid this by using GU as mathematical scaffolding: observerse, bundles,
sections, connections, gauge covariance, spin structure, holonomy, and
sheaf/cohomology bridges.

## Clarifying The GU Baseline

The safe repo-level statement is:

```text
GU is not simply "built from the Standard Model."
```

A more careful statement is:

```text
GU is an attempted unification framework that tries to recover or reorganize
Einstein/Yang-Mills/Dirac/Standard-Model-facing field content through a broader
geometric construction.
```

Therefore the Candidate North Star should not treat GU as established
Standard Model physics. It may treat the following as usable mathematical
scaffolding:

- fiber bundles;
- local sections;
- pullbacks;
- principal connections;
- gauge covariance;
- holonomy;
- spin structures;
- Cech cohomology and monodromy correspondences;
- deformation-complex language, where defined.

It should treat the following as conditional or speculative:

- GU as a correct physical theory;
- GU's recovery of the Standard Model;
- GU's recovery of quantum theory;
- GU's account of dark matter, dark energy, or cosmological observables;
- any claim that TaF or Capability Projection validates GU.

## Compatibility Summary

Candidate North Star v0.6 says:

```text
Capability Projection is projection sufficiency for typed capability objects.
Physics enters only through known physics inducing a typed capability object
under declared access and allowed operations. Capability language does not
derive physics.
```

The repo's GU roadmap says, in effect:

```text
Import GU-relevant mathematics before importing interpretations. Shared
language is not shared physics. TaF results must remain mathematically
independent of GU.
```

These two positions are compatible.

The compatibility breaks only if a future note says or implies:

```text
Because GU has observerse geometry, Capability Projection explains gravity,
dark matter, dark energy, black holes, quantum measurement, or time.
```

The correct GU-facing version is weaker but mathematically cleaner:

```text
If a declared GU model supplies Y, X, pi, fields, connection, symmetry group,
access profile, and allowed operations, then Candidate North Star can ask
whether pi is sufficient for the induced capability object Cap.
```

## Gap Taxonomy

| ID | Category | Severity | Issue | Why it matters | Required work |
| --- | --- | --- | --- | --- | --- |
| G1 | Physics-status gap | High | GU is not established physics. | v0.6 requires physics-facing Cap to be induced by known physics or by a declared model with clear status. | Label GU examples as "conditional GU-model audits" unless the same Cap is derived from established physics. |
| G2 | Directionality error risk | High | GU can tempt the forbidden direction `Cap -> known physics`. | v0.6 explicitly forbids deriving known physics from Cap. | Every GU-facing section must state whether it is using known physics, a GU hypothesis, or pure math. |
| G3 | Standard Model connection gap | High | "GU is built from the Standard Model" is too strong. | GU aims to recover/reorganize Standard-Model-facing structures; that is not the same as starting from confirmed SM machinery. | Replace "built from the Standard Model" with "attempts to geometrically recover or connect to SM-like field content." |
| G4 | Capability object gap | High | GU supplies fields, bundles, actions, connections, and holonomy; it does not automatically supply `Cap`. | Candidate North Star needs an operational `K`, comparison `R_K`, task family, horizon, and access boundary. | Define `Cap_GU(y; O,T,h,B)` explicitly before any GU witness is considered. |
| G5 | Observer meaning mismatch | High | GU observer sections are often metric/geometric sections; v0.6 observers are access profiles. | Confusing the two turns a geometric section into an epistemic agent without proof. | Add a bridge map from GU section data to observer/access profile data, or keep them separate. |
| G6 | Causality gap | High | GU observerse geometry does not by itself supply causal access unless a Lorentzian metric/causal structure is selected. | The North Star story leans on accessible futures, horizons, and causal reachability. | Derive causal order from a declared metric/section and specify global hyperbolicity, domains of dependence, or horizon conditions. |
| G7 | Gauge-invariance gap | High | Capability differences that vary under gauge choice are not physical. | v0.6 requires physics witnesses to survive gauge, coordinate, relabeling, and representation absorption. | Prove `y ~_gauge y' => Cap(y) ~=_K Cap(y')`, unless the gauge change also changes physical access or boundary data. |
| G8 | Smooth/finite type mismatch | Medium-High | GU is smooth differential geometry; many TaF/Capability witnesses are finite, combinatorial, or audit-theoretic. | A Cech or finite witness may not automatically embed into a smooth GU field configuration. | Provide a discretization/continuization functor and state exactly what structure it preserves. |
| G9 | Sheaf bridge gap | Medium-High | GU does not automatically make the Candidate North Star a sheaf theory. | The repo has specific Cech/holonomy bridges, but those are conditional identifications. | Treat sheaf language as a bridge theorem target, not as native GU content unless the sheaf object is defined. |
| G10 | Holonomy overclaim risk | Medium-High | T63/T112 show conditional holonomy matching under H3 and spin-lift conventions, not a general GU derivation of quantum mechanics. | The result is mathematically interesting but limited. | Preserve the exact claim: finite/proxy match under H3; no derivation of Born probabilities, Tsirelson bound, or GU physics. |
| G11 | Naive observerse topology mismatch | Medium-High | The naive observerse `Y` is a negative control for nontrivial `Z/2` holonomy in the repo audit. | A claim that the ordinary observerse alone hosts the needed loop would be false in the tested setting. | Use `Y_spin` only where spin structure is declared, and keep the lift convention explicit. |
| G12 | Gauge group underdefinition | Medium-High | GU's exact gauge group is not fixed in a way the repo can freely rely on. | Holonomy, representation content, and operation classes depend on the group. | Treat `G` as a parameter until the GU model fixes it; do not infer physics from an unspecified group. |
| G13 | Action/equation-to-capability gap | Medium | The Shiab/action machinery may produce field equations, but `Cap` is about future operation availability. | Field equations are not the same type as operation rights, reachable tasks, or observer capability. | Define a functor or semantic map from solutions/dynamics to operational capability objects. |
| G14 | Boundary-condition gap | Medium | Same local visible state can hide topology, asymptotic data, environment, gauge sector, or boundary conditions. | A witness may be self-inflicted if the neighboring theory would normally include those variables. | Apply native state completion before declaring a projection-sufficiency failure. |
| G15 | Gravity wording risk | Medium | "Gravity changes capability geometry" is safe only if capability means causal/trajectory accessibility under GR or a declared GU metric. | Otherwise it sounds like a new theory of gravity. | Phrase as: "Given a metric/causal structure, gravity constrains causal reachability and admissible trajectories." |
| G16 | Dark matter analogy risk | Medium | "Visible state does not determine dynamical structure" is a safe analogy; "hidden capability explains dark matter" is not. | Dark matter has specific gravitational, cosmological, and particle-physics constraints. | Use dark matter only as a typed gravitational-dynamics audit or remove from physics-bearing claims. |
| G17 | Dark energy analogy risk | Medium | Future causal accessibility in cosmology can be discussed; dark energy as capability is not earned. | Dark energy is constrained by FLRW cosmology, expansion history, and observations. | Use only `Cap_cosmo` such as future causal contact/observability under a declared cosmological model. |
| G18 | Black-hole information gap | Medium | Black holes are excellent access-boundary stress tests, but not evidence for a new information theory. | The native absorbers include semiclassical gravity, algebraic QFT, holography, and quantum information. | State access domain, algebra, observer type, and reconstruction task before claiming capability spread. |
| G19 | Time/dynamics mismatch | Medium | GU and physics normally presuppose time or spacetime structure; TaF wants temporal order to emerge from record stabilization. | Importing GU dynamics could smuggle in the temporal arrow TaF is supposed to recover. | Audit every GU import for hidden time-orientation assumptions. |
| G20 | Novelty/absorption gap | Medium | Projection insufficiency is old across POMDPs, sufficient statistics, resource theories, sheaves, control, and process semantics. | GU language may be elegant but redundant unless it yields a sharper audit or transfer theorem. | Require a minimality theorem, canonical enrichment, cross-domain transfer, or executable witness suite. |

## Potential Errors To Avoid

### Error 1: Treating GU As Established SM/QM

Unsafe:

```text
GU is built from the Standard Model, so a GU-shaped Capability Projection
witness inherits Standard Model validity.
```

Safer:

```text
GU is a proposed geometric unification framework with Standard-Model-facing
ambitions. Candidate North Star may use its declared mathematical objects as
conditional scaffolding, but any physics-facing Cap must come from established
physics or from an explicitly labeled GU hypothesis.
```

### Error 2: Equating The Source Fiber With Capability

Unsafe:

```text
F_x = pi^{-1}(x) is the capability fiber.
```

Safer:

```text
F_x is the source fiber. The audit object is the spread

Spread_Cap([x]) = { Cap(y) | y in A and pi(y) ~=_X x } / ~=_K.
```

Only call this a capability fiber if a genuine capability fibration has been
defined.

### Error 3: Turning Gauge Choice Into Physical Difference

Unsafe:

```text
Two gauge-related GU descriptions have different capabilities.
```

Safer:

```text
Gauge-related descriptions must have equivalent capability objects unless the
transformation also changes the physical access profile, boundary condition, or
allowed operation class.
```

### Error 4: Treating Holonomy Matching As Quantum Derivation

Unsafe:

```text
The CHSH Cech obstruction matches spin holonomy, so GU derives quantum
measurement.
```

Safer:

```text
Under H3 and a declared spin-lift convention, the finite/proxy CHSH Cech
obstruction matches a Z/2 spin-holonomy sign. This does not derive Born
probabilities, Tsirelson's bound, all contextuality, or GU physics.
```

### Error 5: Smuggling Time Into A TaF Claim

Unsafe:

```text
Use GU spacetime dynamics to prove TaF's temporal order.
```

Safer:

```text
Use GU geometry only after auditing whether the construction presupposes the
temporal order or time orientation TaF is trying to reconstruct.
```

## Open Work Items

### W1: GU-Cap Typing Template

Before any GU witness is promoted, fill this template:

```text
GU model status:
Y:
X:
pi:
A subset Y:
observer/access profile O:
observational schema Sigma:
resolution r:
domain U:
task family T:
horizon h:
resource/boundary condition B:
fields/connections included in y:
gauge group G:
gauge equivalence:
allowed operations:
Cap_GU:
K:
native comparison R_K:
causal structure used:
factorization question:
native absorber:
not claimed:
```

If any of these fields are missing, the witness should remain intuition or a
formal analogy.

### W2: GU Observer Section vs Access Profile Bridge

Define whether a GU observer section:

```text
sigma : X -> Y
```

is being used as:

- a geometric metric section;
- an observer's physical frame;
- an epistemic access boundary;
- a measurement interface;
- a task-specific operation constraint.

These are different mathematical roles. A report may use one section for
several roles only after stating the bridge map.

### W3: Causal Structure Extraction

For gravity, dark energy, black holes, and time-facing sections, define:

```text
metric/causal structure -> causal futures -> admissible operations -> Cap
```

Minimum required objects:

- Lorentzian metric or declared causal order;
- causal curves or reachability relation;
- observer worldline or access region;
- horizon/domain boundary if relevant;
- finite-energy or finite-time operation constraints;
- comparison relation on accessible futures.

### W4: Gauge-Invariance Lemma

For each GU-facing Cap, prove or test:

```text
y ~_G y'  =>  Cap_GU(y) ~=_K Cap_GU(y')
```

If this fails, classify the failure:

- pure gauge artifact, reject;
- boundary/access change, retype the observer profile;
- physical superselection-sector difference, include it in `Y`;
- unresolved ambiguity, demote witness.

### W5: Smooth/Finite Bridge

The repo should not jump directly from finite witnesses to smooth GU claims.
For each bridge, declare one of:

- finite proxy only;
- discretization of smooth GU structure;
- continuization of finite TaF structure;
- categorical bridge preserving specified limits/colimits;
- sheaf/Cech bridge preserving a named cohomology class;
- no bridge yet.

### W6: Absorber Pass

Every GU-facing physics witness must grant the standard absorber first:

| Domain | Absorber |
| --- | --- |
| Gravity | GR causal structure, domains of dependence, global hyperbolicity, horizon theory. |
| Quantum/contextuality | Quantum theory, sheaf-theoretic contextuality, algebraic QFT, resource theories. |
| Gauge fields | Gauge theory, principal bundles, representation theory, Wilson loops, topological sectors. |
| Dark matter | GR plus stress-energy/dynamical mass models, cosmology, particle/modified-gravity alternatives. |
| Dark energy | FLRW/Lambda-CDM, causal horizons, observational cosmology. |
| Black holes | Semiclassical gravity, QFT in curved spacetime, holography, quantum information. |
| Time/emergence | Dynamical systems, thermodynamics, causal order, statistical mechanics, process theories. |

Only residue after this pass belongs in Candidate North Star.

## What Is Not A Mismatch

The following are compatible with Candidate North Star v0.6:

1. Using GU's `pi : Y -> X` as one concrete source-shadow projection, provided
   `Y`, `X`, and `pi` are typed.
2. Using observerse language as a geometric analogy for observer-indexed
   access, provided the bridge to access profiles is explicit.
3. Using Cech/holonomy correspondences, provided the coefficient group,
   bundle, loop, and transition functions are fixed.
4. Using spin structure in the CHSH holonomy investigation, provided the claim
   remains conditional on H3 and the declared lift convention.
5. Using gravity, dark energy, or black holes as access-boundary stress tests,
   provided the native physical theory supplies `Cap`.
6. Saying "visible projection may forget future-relevant structure," provided
   this is treated as an old projection-sufficiency question, not a novelty
   claim.

## Highest-Risk Mismatch

The highest-risk mismatch is this:

```text
GU wants to geometrize physics.
Candidate North Star v0.6 wants physics to induce Cap, not Cap to induce
physics.
```

This is not a contradiction if the direction is declared.

It becomes a contradiction if a future draft says:

```text
Because Cap has a GU-looking fiber geometry, it explains physical forces,
particles, cosmology, or time.
```

The mathematically defensible version is:

```text
Given a physical model or conditional GU model, define a domain-native Cap and
ask whether the observer-facing projection is sufficient for that Cap.
```

## Recommended Classification Labels

Use these labels in future reports:

- `EST-MATH`: established mathematics used without physics interpretation;
- `KNOWN-PHYSICS-CAP`: Cap induced by established physics;
- `GU-CONDITIONAL-CAP`: Cap induced by an explicitly declared GU hypothesis;
- `STRUCTURAL-ANALOGY`: formal resemblance only;
- `TYPE-GAP`: objects do not yet live in the same category or comparison regime;
- `GAUGE-RISK`: distinction may be representation artifact;
- `ACCESS-RISK`: distinction may rely on access not granted to the observer;
- `CAUSALITY-GAP`: causal order/horizon/reachability not yet specified;
- `FINITE-SMOOTH-GAP`: finite witness not yet bridged to smooth geometry;
- `ABSORBED`: native theory already explains the distinction;
- `PROMOTABLE`: survives typing, gauge audit, absorber pass, and controls.

## Minimal Safe GU Wording

Use wording like this in future Candidate North Star edits:

```text
GU supplies a possible geometric scaffold, not an earned physical foundation
for this note. Where GU language is used, the active object is the declared
projection pi : Y -> X and the typed capability object induced by a specified
model, access profile, task family, horizon, and boundary condition. Any
physics-facing claim must either be derived from established physics or labeled
as conditional on the GU model. Capability Projection does not validate GU and
does not derive known physics.
```

## Verdict

Candidate North Star v0.6 is not mismatched with the repo's conservative GU
workflow.

The remaining issue is bridge discipline:

```text
GU math can help organize the projection story.
GU physics cannot be borrowed as earned support.
```

The next rigorous step is not another analogy. It is a typed GU-Cap witness
with:

- a fixed `Y`, `X`, and `pi`;
- a declared gauge group and equivalence;
- a declared causal/access structure;
- a domain-native `Cap_GU`;
- an invariance lemma;
- a smooth/finite bridge if needed;
- an absorber pass against established physics and mathematics;
- an explicit demotion condition.

Until that exists, GU-facing material should be categorized as
`EST-MATH`, `STRUCTURAL-ANALOGY`, or `GU-CONDITIONAL-CAP`, not as physics
evidence.

## Local Sources Reviewed

- `Candidate North Star v0.6.md`
- `Candidate North Star 20 Physics Perspectives Report v0.1.md`
- `tests/T63-taf-gu-holonomy-dictionary.md`
- `technical-reports/TECHNICAL-REPORT-geometric-unity-integration-roadmap-v0.1.md`
- `technical-reports/TECHNICAL-REPORT-spin-observerse-holonomy-step2-v0.1.md`
- `technical-reports/TECHNICAL-REPORT-d1-gauge-invariance-audit-v0.1.md`

## External Orientation Sources

- `https://geometricunity.org/`
- `https://www.semanticscholar.org/paper/Geometric-Unity%3A-Author%E2%80%99s-Working-Draft%2C-v-1.0-Weinstein/19c0198305887ab3a39b4db6b5d492c5cf028bc2`
