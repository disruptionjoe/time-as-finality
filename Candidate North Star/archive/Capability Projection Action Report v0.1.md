# Capability Projection Action Report v0.1

## Status

This report is a Candidate North Star working artifact.

It is not canon.
It is not a claim update.
It is not a roadmap commitment.
It is not paper-ready.
It does not promote the Candidate North Star.

It translates the current folder posture, the candidate North Star note, and
`Prior Art And Physics Grounding For Capability Projection - Deep Research.md`
into labeled work that should be done next.

The governing posture is:

```text
strongest version first
hostile audit second
demotion third
deletion only if necessary
```

The core object to preserve is:

```text
pi_{O,Sigma,r,U} : Y -> X_{O,Sigma,r}(U)

Cap_{O,T,h,B}(y)

Question: does Cap factor through pi?
```

In plain language:

```text
observable equivalence is not necessarily capability equivalence
```

## Executive Judgment

The deep research does not kill the Candidate North Star. It sharpens it.

The core pattern is already native to mature frameworks: POMDPs, sufficient
statistics, Blackwell informativeness, control observability, bisimulation,
resource theories, sheaf obstruction, causal inference, Koopman/operator
dynamics, provenance, access control, and viability theory.

That means the North Star should not be framed as discovery of a new phenomenon.
The live question is whether the repo can build a useful unifying schema around
projection loss and future capability that either:

1. produces a same-neighbor-data separation not absorbed by existing theories;
2. becomes a clean translation layer across existing theories;
3. demotes into known reachability/provenance/resource/opportunity language.

All three outcomes are legitimate. The only bad outcome is keeping `Cap` vague
enough that it can explain anything after the fact.

## Label System

Use the following labels for follow-up work.

| Label | Meaning |
| --- | --- |
| `PRESERVE` | Keep the intuition alive as North Star material. |
| `TYPE` | Make an object mathematically typed enough to test. |
| `COMPARE` | Put the idea against mature prior art. |
| `TEST` | Build a finite witness, audit, or counterexample. |
| `PHYSICS-GROUND` | State known physics, analogy, non-claim, test route, and falsifier. |
| `DEMOTE-IF-ABSORBED` | Explicitly collapse into prior art if no residue survives. |
| `DO-NOT-PROMOTE` | Mark as not claim-led evidence. |

## Highest Priority Work

### 1. TYPE - Define `Cap` As An Indexed Preorder First

The deep research recommends starting with:

```text
Cap_{O,T,h,B}(y)
```

as an indexed preorder of admissible future operations, optionally paired with
a viability-filtered reachable set.

Do this before any stronger categorical language.

Minimum definition:

```text
O = observer/access profile
T = task family
h = horizon
B = budget, boundary, or resource condition

Cap_{O,T,h,B}(y) =
  preorder of admissible operations available from source state y
```

Capability equivalence:

```text
y1 ~_Cap y2
iff
Cap_{O,T,h,B}(y1) and Cap_{O,T,h,B}(y2)
are equivalent as indexed preorders
```

Why this matters:

- sets of operations are too weak;
- categories are probably too heavy too early;
- preorders align with resource theory, reachability, opportunity sets,
  convertibility, and admissible transformations;
- the indexing prevents `Cap` from becoming universal fog.

Deliverable:

```text
Capability Projection Schema v0.1
```

as a short formal note in this folder, not in core repo claims.

### 2. TEST - Build A Factorization Audit Template

Every future example should be forced through the same test:

```text
Given pi : Y -> X
and Cap : Y -> K,
does there exist Cbar : X -> K
such that Cap = Cbar o pi?
```

If yes:

```text
visible state is sufficient for this capability question
```

If no:

```text
projection is capability-nondetermining for this task/horizon/budget
```

Required fields:

```text
source structure Y
visible shadow X
projection pi
observer/schema/resolution/domain indices
task/horizon/budget indices
capability structure K
equivalence notion on K
factorization verdict
absorbing prior art
residue, if any
```

Deliverable:

```text
Capability Factorization Audit Template v0.1
```

This should become the standard way to prevent beautiful examples from becoming
rhetorical examples.

### 3. COMPARE - Run The Prior-Art Absorption Matrix

The deep research makes the prior-art situation unavoidable. For each witness,
ask whether it is already absorbed by:

- POMDP belief-state sufficiency;
- sufficient statistics / Blackwell order;
- control observability / controllability;
- bisimulation-preserving abstraction;
- resource theory convertibility;
- viability kernels;
- causal inference / interventional equivalence;
- sheaf local-to-global obstruction;
- Koopman observable choice;
- provenance and access-control systems;
- abstract interpretation;
- opportunity-set economics;
- affordance theory.

Required verdicts:

```text
absorbed
partially absorbed
not absorbed under same-neighbor data
unclear because Cap is under-typed
```

Deliverable:

```text
Capability Projection Prior-Art Absorption Matrix v0.1
```

This should be hostile, not decorative.

### 4. TEST - Same-Visible-State / Different-Capability Witness Table

Build a table of repo-native examples and force them into the same schema.

Initial rows:

| Domain | Same visible state | Different capability | Likely absorber |
| --- | --- | --- | --- |
| Git histories | same endpoint tree | different revert/bisect/merge/recovery options | provenance, version-control theory |
| detector packets | same raw payload | different admissibility/challenge/future operation rights | provenance, access control |
| LossKernel | same endpoints / maps / labels | different attribution if source witness obligations differ | why-not provenance, abstract interpretation, lenses, effects |
| ASP / FOA | same coarse state | different future operation availability | reachability, opportunity sets |
| maintenance | same coarse viability | different future usability | viability, resource theory |
| observer access | same local records | different reconstruction/audit access | sheaf/access-boundary theory |
| quantum local state | same reduced state | different purification/entanglement resource | quantum resource theory |

For each row, record:

```text
Cap factors through pi? yes/no/unknown
which prior art absorbs it?
what residue remains?
```

Deliverable:

```text
Capability Projection Witness Ledger v0.1
```

### 5. DEMOTE-IF-ABSORBED - State The Collapse Condition Up Front

Every document in this folder should preserve the dissolution condition:

```text
If Cap always factors through pi after using the right enriched known theory,
the North Star collapses into known theory.
```

This is not a failure of the work. It is a successful identification of the
right neighbor.

Suggested wording:

> The Candidate North Star survives as a distinct research program only where
> capability-nondetermination remains after mature neighboring accounts are
> given their full state. Otherwise it should be preserved as translation
> vocabulary or demoted into the absorbing framework.

## Physics-Facing Work

The folder posture says:

```text
do not remove physics
formalize it
```

The deep research supports keeping the physics sections, but only with strict
structure:

1. known physics;
2. candidate mathematical analogy or bridge;
3. non-claim boundary;
4. test route;
5. falsifier or dissolver.

### 6. PHYSICS-GROUND - General Relativity

Known physics:

General relativity already ties causal accessibility to spacetime geometry:
light cones, causal futures, horizons, global hyperbolicity, and causal curves.

Safe bridge:

```text
geometry constrains future accessibility
```

Candidate `Cap`:

```text
reachable causal futures
admissible interactions
possible observation domains
signal/reconstruction options
```

Do not claim:

```text
gravity is capability
capability explains gravity
```

What to do:

- Define a GR-facing toy schema where `Cap(p)` is built from `J+(p)` under an
  observer/budget/horizon index.
- Compare two projections that agree locally but differ in global causal
  accessibility.
- Check whether this reduces completely to standard causal structure.

Likely disposition:

Mostly absorbed by GR causal structure, but useful as grounding vocabulary.

### 7. PHYSICS-GROUND - Cosmological Expansion And Dark Energy

Known physics:

Expansion history affects horizons and large-scale causal accessibility.
Accelerated expansion changes asymptotic reachability.

Safe bridge:

```text
cosmic expansion changes future accessibility geometry
```

Do not claim:

```text
dark energy is capability
capability explains accelerated expansion
```

What to do:

- State `Cap` in terms of future causal contact, event horizons, or accessible
  domains for embedded observers.
- Compare local visible matter content with global horizon structure.
- Keep microphysical dark-energy interpretation out of the claim.

Likely disposition:

Useful analogy, probably absorbed by cosmological causal-horizon theory.

### 8. PHYSICS-GROUND - Dark Matter

Known physics:

Visible luminous/baryonic structure does not determine all gravitationally
relevant structure.

Safe bridge:

```text
visible structure can underdetermine dynamically relevant structure
```

Do not claim:

```text
dark matter is hidden capability
capability explains dark matter
```

What to do:

- Use dark matter only as an analogy for projection insufficiency.
- If modeled, use a pair:

```text
same luminous projection
different gravitational/dynamical source structure
```

- Ask whether future orbital/lensing/dynamical capability differs.

Likely disposition:

Analogy only. Strong evidence that projection insufficiency is physically
non-naive, not evidence for the North Star.

### 9. PHYSICS-GROUND - Black Holes

Known physics:

Horizons are causal boundaries. Observer location changes signal, verification,
and reconstruction possibilities.

Safe bridge:

```text
horizon = boundary in future operation availability
```

Do not claim:

```text
capability solves the information problem
black holes prove TaF
```

What to do:

- Define observer-indexed operations:

```text
signal out
verify record
reconstruct exterior state
intervene on interior/exterior degrees of freedom
```

- Ask which operations remain available to exterior, infalling, and asymptotic
  observers.

Likely disposition:

Good testbed for observer-indexed `Cap`; claims should remain absorbed by
standard horizon/causal-access language unless a new finite audit separates.

### 10. PHYSICS-GROUND - Quantum Theory

Known physics:

Reduced local states can hide purification, entanglement, resource, or
environment-side structure.

Safe bridge:

```text
same local state
different future operational capability
```

Strong examples:

- same reduced density matrix, different purification;
- same local observable state, different entanglement resource;
- same outcome projection, different reversibility or future transform options;
- same visible detector payload, different admissibility/provenance rights.

What to do:

- Make quantum theory the strongest physics neighbor for the North Star.
- Compare directly with quantum resource theories and LOCC convertibility.
- Do not claim novelty unless a same-neighbor-data witness survives.

Likely disposition:

Partly absorbed by quantum information/resource theory, but probably the
cleanest physics-facing source of finite examples.

### 11. PHYSICS-GROUND - Standard Model Structure

Known physics:

Charge, spin, mass, gauge representation, phase, and selection rules constrain
allowed interactions.

Safe bridge:

```text
physical internal structure constrains admissible transformations
```

Do not claim:

```text
charge = capability
spin = capability
mass = capability
```

What to do:

- Use representation data as a source of capability constraints.
- Compare:

```text
same spacetime/event projection
different internal fiber data
different allowed interactions
```

- Treat this as an analogy or external math source unless made executable.

Likely disposition:

Good language import. Do not promote.

### 12. PHYSICS-GROUND - Time

Known physics:

Relativity and thermodynamics already govern temporal structure and physical
arrows. Recent H7 work blocks any careless claim that closed reversible systems
generate a strict finality arrow.

Safe bridge:

```text
capability changes along physical time
```

or:

```text
physical time can be accompanied by changing future-operation structure
```

Do not claim:

```text
observers create time
capability replaces time
capability derives the thermodynamic arrow
```

What to do:

- Tie this to T124-style constructor-admissibility accounting.
- Require every directional capability claim to name openness, resources,
  erasure, boundary condition, coarse-graining, or nonstationarity.

Likely disposition:

Potentially generative, but must remain under H7/T124 discipline.

### 13. PHYSICS-GROUND - Emergence

Known neighbors:

Viability theory, affordance theory, niche construction, major transitions,
constructor theory, resource theory.

Safe bridge:

```text
emergent structures can become platforms for future capability
```

What to do:

- Define emergence cases as:

```text
structure -> preserved capability -> further structure
```

- Compare with viability and major-transition frameworks.
- Ask when new structures expand, preserve, restrict, or redirect admissible
  future operations.

Likely disposition:

Very useful as North Star language. Novelty uncertain.

## Specific Reports / Artifacts To Draft

### A. Capability Projection Schema v0.1

Label: `TYPE`

Purpose:

Define the minimal formal schema:

```text
pi_{O,Sigma,r,U}
Cap_{O,T,h,B}
factorization
capability equivalence
capability-nondetermining projection
```

Must include:

- why `faithful` is avoided;
- why `Cap` starts as indexed preorder;
- examples of `Cap` structures by domain;
- preservation cases where `Cap` does factor through `pi`.

### B. Capability Factorization Audit Template v0.1

Label: `TEST`

Purpose:

A reusable template for any example.

Must include:

- source/shadow/projection;
- observer/schema/resolution/domain;
- task/horizon/budget;
- `Cap` type;
- equivalence notion;
- factorization verdict;
- absorber;
- residue.

### C. Prior-Art Absorption Matrix v0.1

Label: `COMPARE`

Purpose:

Turn the deep research into a hostile absorption checklist.

Must include:

- POMDPs;
- sufficient statistics / Blackwell order;
- control observability;
- bisimulation;
- resource theory;
- viability;
- causal inference;
- sheaf obstruction;
- Koopman;
- provenance/access control;
- abstract interpretation;
- opportunity sets;
- affordance theory.

### D. Physics Grounding Appendix v0.1

Label: `PHYSICS-GROUND`

Purpose:

Preserve the physics-forward material while making each section disciplined.

Structure per section:

```text
Known physics
Safe bridge
Not claimed
Test route
Falsifier / likely absorber
```

### E. Candidate North Star v0.2

Label: `PRESERVE + TYPE`

Purpose:

Create a new version rather than replacing the current note.

Changes from current candidate:

- use `capability-nondetermining projection`;
- define `Cap` as indexed preorder by default;
- move prior-art trinity near the top:

```text
POMDPs
control/observability
resource convertibility
```

- mark physics sections as analogy-only but keep them;
- add collapse condition prominently.

## Proposed Finite Tests

### Test 1 - Projection Factorization Smoke Test

Label: `TEST`

Question:

Can a simple finite fixture distinguish:

```text
same pi(y)
same standard visible summary
different Cap(y)
```

without making `Cap` arbitrary?

Start with three domains:

- detector packet admissibility;
- Git history operation rights;
- quantum local-state/purification resource.

Success:

- same visible shadow;
- typed `Cap`;
- explicit non-factorization;
- absorber identified.

Failure:

- `Cap` is just post hoc labels;
- prior art fully recovers the distinction;
- visible state was not actually the same.

### Test 2 - Capability Preservation Positive Controls

Label: `TEST`

Question:

When does `Cap` factor through `pi`?

This is necessary to avoid tautology.

Build examples where visible state is sufficient:

- fully observed deterministic finite state;
- sufficient statistic for a fixed decision problem;
- bisimulation-preserving abstraction;
- resource monotone complete for a tiny fixture.

Success:

The schema can say both:

```text
projection loses capability
```

and:

```text
projection preserves capability
```

Failure:

The North Star is unfalsifiable.

### Test 3 - Same-Neighbor-Data Capability Audit

Label: `TEST + COMPARE`

Question:

Can capability projection produce a residue after prior art receives its full
allowed data?

This should coordinate with T127.

Success:

Two cases match under standard neighbor data but differ under typed source
capability obligations.

Failure:

Demote the North Star into translation vocabulary.

## Immediate Do / Do Not List

## Do

- Preserve the intuition.
- Use `capability-nondetermining projection`.
- Use `Cap does not factor through pi`.
- Index every capability object.
- Start `Cap` as an indexed preorder.
- Add positive controls where `Cap` does factor.
- Compare against prior art before physics.
- Keep physics sections, but make them rigorous analogy sections.
- Record absorption as information.

## Do Not

- Do not call the projection `nonfaithful` unless a real categorical setting is
  defined.
- Do not leave `Cap` untyped.
- Do not let `Cap` mean "anything useful later."
- Do not claim physics support from analogies.
- Do not say dark matter, dark energy, gravity, or time are explained.
- Do not treat prior-art absorption as embarrassment.
- Do not edit the canonical North Star without explicit approval.

## Suggested Order Of Work

1. Draft `Capability Projection Schema v0.1`.
2. Draft `Capability Factorization Audit Template v0.1`.
3. Draft `Prior-Art Absorption Matrix v0.1`.
4. Draft `Candidate North Star v0.2`.
5. Draft `Physics Grounding Appendix v0.1`.
6. Only then consider executable finite tests or repo-routing.

## Bottom Line

The deep research says:

```text
This intuition is real enough to preserve.
It is not yet distinct enough to promote.
It is surrounded by strong prior art.
Its best next move is typing, factorization testing, and hostile absorption.
```

The strongest compact formulation remains:

```text
For fixed observer, task, horizon, and resource boundary,
future capability need not factor through observer-visible state.
```

That is worth preserving.
