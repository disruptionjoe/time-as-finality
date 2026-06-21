# Candidate North Star Mathematical Strengthening Suggestions v0.1

## Status

This is a companion note for:

```text
Candidate North Star v0.3.md
```

It suggests ways to strengthen the Candidate North Star using mathematics that
is difficult to argue against at the formal level.

It does not promote the Candidate North Star.
It does not update canon.
It does not claim new physics.
It does not treat existing repo tests as evidence for the North Star.

The goal is narrower:

```text
Find the strongest mathematically defensible ways to say the idea,
including bold physics-facing versions, without saying anything false.
```

## Selection Rule

Only include strengthenings that satisfy all three conditions:

1. The mathematical statement is standard, tautological, theorem-shaped, or
   directly checkable.
2. The physics-facing interpretation does not conflict with established
   objective physics.
3. The suggestion improves precision rather than merely making the prose more
   exciting.

The note should prefer:

```text
hard formal scaffold first
bold interpretation second
guardrail third
```

## Executive Summary

The strongest version of the Candidate North Star is not:

```text
hidden capability explains physics
```

It is:

```text
For a declared observer, task, horizon, and boundary condition,
future capability is a typed structure. A projection is adequate for that
future-facing question exactly when the capability structure factors through
the projection.
```

The mathematically strongest sentence is:

```text
Cap factors through pi iff Cap is constant, up to declared equivalence, on
every pi-fiber.
```

Everything else should be built around that.

The strongest physics-facing sentence is:

```text
Given any physical theory with states, dynamics, constraints, and allowed
interactions, one can define a capability object as the set, preorder, or
category of future operations admissible from a state. A coarse observation is
future-sufficient exactly when this capability object factors through that
observation.
```

That is bold enough to unify the language, but not incorrect. It does not
derive physics from capability. It derives capability objects from physics and
asks when projections preserve them.

## 1. Make Factorization The Central Theorem-Like Spine

Current core:

```text
pi(y1) = pi(y2) does not imply Cap(y1) ~= Cap(y2)
```

Strengthen to the exact equivalence:

```text
Cap descends to X through pi
iff
for all y1,y2 in Y,
pi(y1)=pi(y2) implies Cap(y1) ~=_K Cap(y2).
```

Diagram:

```text
Y  --Cap-->  K
|           ^
pi          |
v           Cbar
X  ---------
```

The descent exists exactly when the triangle commutes up to the declared
capability equivalence:

```text
Cap(y) ~=_K Cbar(pi(y)).
```

Why this is hard to argue against:

- It is just the universal property of quotient/descent/factorization.
- It immediately separates the mathematical question from metaphysics.
- It gives positive and negative cases.

Suggested language:

```text
The North Star question is a projection-sufficiency question:
does the observer-facing shadow carry enough information to determine the
declared future capability object?
```

## 2. Define The Minimal Capability-Preserving Quotient

For any capability assignment:

```text
Cap : Y -> K
```

define:

```text
y1 ~_Cap y2 iff Cap(y1) ~=_K Cap(y2).
```

Then:

```text
Y / ~_Cap
```

is the coarsest quotient that preserves the declared capability.

A projection:

```text
pi : Y -> X
```

is capability-sufficient exactly when:

```text
ker(pi) subset ker(Cap).
```

Equivalently, `pi` is no coarser than the capability quotient.

Why this is hard to argue against:

- It is quotient math.
- It gives the clean negative case.
- It prevents vague "hidden structure" language.

Suggested addition:

```text
For each proposed domain, the honest target is the minimal
capability-preserving quotient. If the visible state is coarser than that
quotient, it loses future capability distinctions. If it refines that quotient,
the projection is sufficient for the declared task.
```

## 3. Add The Trivial Enrichment Theorem

For any projection and capability assignment:

```text
pi : Y -> X
Cap : Y -> K
```

define the enriched projection:

```text
pi' : Y -> X x K
pi'(y) = (pi(y), Cap(y)).
```

Then `Cap` always factors through `pi'`.

Why this matters:

This proves that "state enrichment absorption" is mathematically inevitable.
Any failed projection can be repaired by adding the missing capability-relevant
data to the visible state.

Why this is hard to argue against:

- It is tautological and exact.
- It clarifies that the real question is not whether enrichment can fix the
  failure.
- The real question is whether the added structure is canonical, minimal,
  domain-natural, or physically meaningful.

Suggested language:

```text
Every non-factorization can be repaired by enriching the state with the
capability object itself. Therefore the research question is not whether
enrichment is possible, but which enrichment is natural, minimal, and
domain-forced.
```

## 4. Replace "Capability-Nonfaithful" With Safer Terms

"Faithful" has a category-theoretic meaning. Avoid unnecessary collision.

Preferred terms:

```text
capability-nondetermining projection
capability-incomplete projection
capability-insufficient projection
future-insufficient projection
projection-sufficiency failure
```

Best default:

```text
capability-insufficient projection
```

Reason:

- It matches sufficient-statistic language.
- It avoids category-theory collision.
- It clearly says what failed: the projection is insufficient for the declared
  future capability question.

## 5. Make `Cap` The Central Open Problem

The strongest critique of the note is right:

```text
Cap is doing the real work.
```

Strengthen by making this explicit.

Suggested text:

```text
The central open problem is not whether projections can lose capability
distinctions. They can. The central open problem is what mathematical type
Cap should have in each domain, and when capability equivalence is canonical.
```

Candidate `Cap` types, from weakest to strongest:

| Cap type | When it is appropriate | Risk |
| --- | --- | --- |
| Set of operations | Finite task audits | Too extensional; ignores structure |
| Preorder | Convertibility, reachability, dominance | Needs justified order |
| Category | Operations plus composition | More expressive; harder to keep canonical |
| Resource theory | Physical or informational convertibility | Strong prior-art absorption |
| MDP/POMDP policy object | Decision/control settings | Usually absorbed by belief-state sufficiency |
| Sheaf/presheaf | Local-to-global compatibility | Must not confuse restriction with dynamics |
| Fibration/indexed category | Capability varying over visible states | Powerful but high ceremony |

Recommendation:

```text
Start with preorders or small categories of admissible operations.
Use sets only for finite toy tests.
Use resource theories when physical convertibility is central.
Use presheaves when locality/restriction is load-bearing.
```

## 6. Add A Pushforward Capability Spread

Given:

```text
pi : Y -> X
Cap : Y -> K
```

define the capability spread over a visible state:

```text
Spread_Cap(x) = { Cap(y) | y in pi^{-1}(x) } / ~=_K.
```

Then:

```text
Cap factors through pi
iff
for every x in X, Spread_Cap(x) is a singleton.
```

Why this helps:

- It gives a positive measure of how badly the projection fails.
- It avoids mystical hidden-fiber talk.
- It naturally supports finite audits.

Possible scalar summary:

```text
ambiguity_Cap(x) = |Spread_Cap(x)|
```

or, when `K` has order/metric structure:

```text
diameter_Cap(x) = diameter(Spread_Cap(x)).
```

Suggested language:

```text
The fiber pi^{-1}(x) is not itself the capability. The relevant object is the
spread of capability values across that fiber.
```

## 7. Use Abstract Interpretation As A Hard Mathematical Anchor

Let:

```text
alpha : Concrete -> Abstract
gamma : Abstract -> P(Concrete)
```

be an abstraction/concretization pair.

For a concrete transformer:

```text
f : Concrete -> Concrete
```

an abstract transformer:

```text
f# : Abstract -> Abstract
```

is complete for the property/capability when the abstraction preserves the
needed behavior.

This directly matches:

```text
projection sufficient for capability
```

Why this is hard to argue against:

- Abstract interpretation already owns this formal shape.
- It gives the right humility: many failures are just incomplete abstractions.

Strengthening:

```text
The Candidate North Star should explicitly treat itself as a cross-domain
projection-completeness audit, not as a new discovery of projection loss.
```

## 8. Use Database View Determinacy As The Cleanest Finite Anchor

Database theory gives very precise finite cases.

Let:

```text
Y = full database instance
pi = view or materialized snapshot
Cap = query workload, recovery operation, audit operation, or update right
```

Then:

```text
Cap factors through pi
```

means:

```text
the view determines the declared workload/capability.
```

Why this is hard to argue against:

- View determinacy and query rewriting are mature.
- Positive and negative cases are easy.
- It makes "same visible state" precise.

Recommended use:

```text
Make database cases the finite calibration fixture for the whole North Star.
Physics sections can then be bold analogies over a mathematically grounded
schema rather than the first place readers meet the idea.
```

## 9. Use POMDPs And Belief States As The Decision-Theory Absorber

In a POMDP:

```text
hidden state: s
observation: o = pi(s)
policy value: V(b)
```

Raw observation is generally not sufficient for optimal future control.
Belief state is the standard sufficient enrichment:

```text
b = P(s | history)
```

Strengthening:

```text
The North Star should acknowledge that when Cap means future decision/control
value, belief-state sufficiency is the default absorber.
```

Hard-to-argue use:

```text
This gives a mathematically mature example where visible state fails but a
known enrichment restores sufficiency.
```

## 10. Use Resource Theory For Physical Capability

If `Cap` means:

```text
what transformations are possible under allowed operations
```

then resource theory is the natural language.

Let:

```text
y1 >=_R y2
```

mean:

```text
y1 can be converted to y2 under allowed operations R.
```

Then capability is a convertibility structure.

Projection failure:

```text
pi(y1) = pi(y2)
but
Down_R(y1) != Down_R(y2)
```

where:

```text
Down_R(y) = { z | y >=_R z }.
```

Why this is hard to argue against:

- It gives the cleanest physics-adjacent notion of capability.
- It avoids making capability mysterious.
- It absorbs many claims honestly.

Recommended physics-facing phrasing:

```text
When capability means physically allowed transformation, the natural formal
object is a resource-theoretic convertibility structure.
```

## 11. Use Sheaf/Presheaf Language Only Where Locality Matters

Sheaf language is strong only if locality/restriction/gluing is load-bearing.

Let:

```text
Cap : C^op -> K
```

assign capability objects to patches.

Projection sufficiency becomes patch-indexed:

```text
Does Cap(U) factor through pi(U) for each patch U?
```

Gluing question:

```text
Do locally capability-sufficient projections assemble into a globally
capability-sufficient projection?
```

Why this is valuable:

- It connects the North Star to the repo's local/global machinery.
- It gives real obstruction questions.

Guardrail:

```text
Restriction maps are not time evolution.
Forward dynamics must be added separately.
```

## 12. Strong Physics Rule: Derive Capability From Physics, Not Physics From Capability

This is the safest bold framing.

Do not say:

```text
capability explains gravity / particles / dark energy / time
```

Say:

```text
Given a physical theory, the theory induces capability structures: reachable
regions, allowed interactions, possible transformations, measurement
operations, reconstruction operations, and resource-constrained futures.
```

Then ask:

```text
which projections preserve those induced capability structures?
```

This is bold but safe because it respects known physics.

General schema:

```text
Physical theory -> state space Y
Physical law / constraints -> allowed transformations A
Observer / apparatus / horizon -> access boundary O
Task family -> T
Capability -> C_{O,T,h}(y)
Projection/readout -> pi : Y -> X
Audit -> does C factor through pi?
```

## 13. Gravity: Make Causal Accessibility The Capability

Strongest safe form:

```text
In general relativity, spacetime geometry constrains causal accessibility.
If capability includes reachable future events, possible communication, or
admissible trajectories, then gravity constrains capability.
```

Mathematical object:

```text
Y = spacetime model (M,g) plus relevant matter/observer data
X = observer-visible local data over patch U
pi = restriction/readout to U
Cap(y) = causal future, reachable worldlines, or admissible communication /
         measurement trajectories under declared constraints
K = causal reachability structure
```

Non-factorization question:

```text
Can two source geometries agree on the observer-visible patch while differing
in future reachable regions or causal boundary structure?
```

Why hard to argue against:

- GR already makes causal accessibility geometry-dependent.
- The claim is not that capability explains gravity.
- The claim is only that gravity induces capability constraints.

Safe bold sentence:

```text
Gravity is a domain where future capability is naturally constrained by
geometry.
```

## 14. Dark Matter: Use Dynamical Sufficiency, Not Capability Explanation

Strongest safe form:

```text
Dark matter illustrates that visible/luminous structure is not a sufficient
invariant for gravitational dynamics.
```

Mathematical object:

```text
Y = full gravitational source structure
X = luminous/electromagnetic visible distribution
pi = projection to luminous matter
Dyn(y) = gravitational dynamical consequences: lensing, rotation behavior,
         structure formation, binding
```

Use `Dyn` before `Cap` here unless capability is explicitly defined as
gravitationally possible future trajectories.

Non-factorization:

```text
pi(y1) = pi(y2)
but
Dyn(y1) != Dyn(y2)
```

Why hard to argue against:

- It mirrors the empirical role of dark matter without explaining it.
- It avoids the false claim that dark matter is capability.

Safe bold sentence:

```text
Dark matter is a cautionary example: visible projection need not determine
future-relevant dynamical structure.
```

## 15. Dark Energy: Use Future Causal Contact

Strongest safe form:

```text
Cosmic expansion affects large-scale future accessibility.
```

Mathematical object:

```text
Y = cosmological spacetime with expansion history
X = observer-visible local/cosmological data
pi = restriction to observed data
Cap(y) = future causal contact, reachable regions, communication possibility,
         or structure-formation accessibility
K = long-horizon causal accessibility structure
```

Non-factorization question:

```text
Can the observer-visible matter distribution fail to determine long-horizon
causal accessibility without the expansion model?
```

Why hard to argue against:

- Accelerated expansion affects horizons and future causal contact.
- This is not an explanation of dark energy.

Safe bold sentence:

```text
Dark energy is relevant to the North Star only as a reminder that future
accessibility depends on large-scale geometry, not local visible matter alone.
```

## 16. Black Holes: Capability Boundaries Are Causal Boundaries

Strongest safe form:

```text
Black holes are natural stress tests for observer-indexed operation
availability because horizons are causal boundaries.
```

Mathematical object:

```text
Y = global spacetime with black hole region
X = exterior observer-accessible data
pi = restriction to exterior domain
Cap(y) = signaling, reconstruction, verification, intervention, or retrieval
         operations available to observer O
K = observer-indexed operation availability across causal boundary
```

Non-factorization question:

```text
Can exterior-accessible data fail to determine operation availability that
depends on inaccessible global or horizon structure?
```

Why hard to argue against:

- Horizons constrain which operations are available to which observers.
- The statement does not solve the black hole information problem.

Safe bold sentence:

```text
A horizon is a concrete physical case where future operation availability is
observer-indexed by causal access.
```

## 17. Electrons And Physical Structure: Use Allowed Interactions

Strongest safe form:

```text
Physical properties constrain admissible interactions.
```

Mathematical object:

```text
Y = physical state including representation labels, quantum numbers, fields,
    couplings, and context
X = coarse detector-visible event/state
pi = measurement/readout/coarse-graining
Cap(y) = allowed interactions, transformations, scattering channels, or
         measurement outcomes under the theory
K = admissible-interaction structure
```

Non-factorization question:

```text
Can two states have the same coarse detector-visible shadow while differing in
allowed future interactions due to internal quantum numbers or context?
```

Why hard to argue against:

- Standard physics already treats charge, spin, mass, and representation data
  as constraining interactions.
- The note need not say these properties are capability.

Safe bold sentence:

```text
Charge, spin, mass, and representation data are not capability, but they help
determine physically admissible future interactions.
```

## 18. Time: Use Capability Trajectories, Not Replacement Time

Strongest safe form:

```text
Along a physical time parameter or causal ordering, capability structures may
change even when a chosen visible projection appears unchanged.
```

Mathematical object:

```text
y_t in Y
x_t = pi(y_t)
Cap_t = Cap_{O,T,h}(y_t)
```

Possible situation:

```text
x_t = x_{t'}
but
Cap_t != Cap_{t'}.
```

Why hard to argue against:

- It is just a statement about a time-indexed trajectory in a richer state
  space.
- It does not replace time.

Safe bold sentence:

```text
For future-facing questions, the trajectory of capability can contain
information not visible in the trajectory of a chosen shadow state.
```

## 19. Emergence: Use Platform Capability

Strongest safe form:

```text
An emergent structure can be studied as a structure that becomes a platform
for additional admissible operations.
```

Mathematical object:

```text
E subset Y
Cap_before(y)
Cap_after(Phi_t(y))
```

Platform condition:

```text
Cap_after contains new operation families not available before,
while preserving viability or maintenance constraints.
```

This can be set-valued, preorder-valued, or category-valued.

Why hard to argue against:

- It is compatible with viability theory, affordances, resource theory, and
  major-transition language.
- It does not claim all emergence is capability expansion.

Safe bold sentence:

```text
Emergence can be audited by asking whether a structure preserves or creates
new admissible future operations under declared constraints.
```

## 20. Add A Mandatory Negative Case

The North Star should explicitly say when it fails.

Strongest negative condition:

```text
If, for every domain-natural capability object of interest, Cap factors
through the accepted state description or is fully absorbed by a mature native
theory, then Capability Projection adds no new formal structure.
```

Even stronger:

```text
If all non-factorization witnesses disappear under minimal sufficient
state enrichment, and that enrichment is already standard in the native field,
then the North Star has only translation or heuristic value.
```

Why hard to argue against:

- It gives hostile readers a real failure path.
- It prevents unfalsifiable framing.

## 21. Add A "No Free Physics" Rule

Suggested rule:

```text
No physics-facing claim is allowed unless it can be written as:

Known theory:
Y:
X:
pi:
Cap:
K:
Equivalence on K:
Factorization question:
Absorbing native theory:
Not claimed:
```

This makes bold physics sections safer, not weaker.

Example:

```text
Known theory: GR causal structure
Y: spacetime with metric and observer data
X: local observer-visible patch
pi: restriction to local patch
Cap: reachable future events / communication trajectories
K: causal reachability preorder
Equivalence: same reachable domain under declared horizon
Factorization question: does local visible patch determine future reachability?
Absorber: standard causal structure in GR
Not claimed: capability explains gravity
```

## 22. Add A Residue Scale

Not every result should be treated equally.

Suggested scale:

```text
0. Redundant: already exactly owned by mature theory.
1. Heuristic: helps find missing variables.
2. Translation: aligns several mature theories under one audit surface.
3. Formal: gives a clean typed object or theorem not already explicit.
4. Canonical: identifies a natural capability object forced across domains.
5. Physics-bearing: produces a physics-facing consequence without conflicting
   with known theory.
```

Current honest expectation:

```text
Most Capability Projection cases are level 1 or 2.
The North Star becomes stronger only if it reaches level 3 or 4.
Physics-bearing level 5 should be treated as long-horizon only.
```

## 23. Add A Mathematics-First Physics Derivation Template

If the user wants to derive physics-facing language from the mathematics, use
this template.

For a physical theory `P`:

```text
State_P = allowed physical states
Obs_P = observer/readout map
Dyn_P = dynamics or transition relation
Ops_P = allowed operations/interactions
Boundary_P = causal/resource/access constraints
```

Define:

```text
Cap_P(y; O,T,h,B) =
  { operation sequences in Ops_P admissible from y
    for observer O, task family T, horizon h, boundary B,
    under Dyn_P and constraints Boundary_P }.
```

Then the North Star question becomes:

```text
Does Cap_P factor through Obs_P?
```

This is extremely hard to object to because it is definitional once the theory,
operations, and equivalence are declared.

Bold but safe interpretation:

```text
Physics can be read as inducing a capability geometry over states. The
Candidate North Star asks which observer-facing shadows preserve that induced
geometry.
```

Guardrail:

```text
This does not derive the physical theory. It derives a capability audit from
the physical theory.
```

## 24. Add A Stronger "Same Visible State" Discipline

Do not allow informal equality.

Replace:

```text
same visible state
```

with:

```text
same visible state under declared observer O, schema Sigma, resolution r,
domain U, time/snapshot convention tau, and equivalence ~=_X.
```

Mathematical form:

```text
pi_{O,Sigma,r,U,tau}(y1) ~=_X pi_{O,Sigma,r,U,tau}(y2)
```

Then test:

```text
Cap_{O,T,h,B}(y1) ~=_K Cap_{O,T,h,B}(y2).
```

Why hard to argue against:

- It removes ambiguity.
- It blocks cheap counterarguments based on hidden changes to observation
  context.

## 25. Add A "Projection Was Too Crude" Classifier

Many witnesses will be boring because the projection was obviously too crude.

Add failure label:

```text
projection_underdescribed
```

Use it when the projection intentionally omitted native state required by the
domain.

Examples:

- endpoint repo tree without commit DAG;
- database snapshot without transaction log;
- visible matter without gravitational mass model;
- local patch without causal boundary conditions;
- reduced state without allowed-operation context;
- top-k search result without index/search parameters.

This strengthens the note by showing it can demote its own examples.

## 26. Add A "Canonical Enrichment" Target

The strongest possible positive result is not:

```text
projection failed
```

It is:

```text
the same kind of enrichment repairs projection failure across multiple mature
domains.
```

Candidate enrichments:

- provenance;
- access rights;
- causal boundary;
- resource budget;
- operation semantics;
- witness structure;
- reconstruction paths;
- viability constraints.

Hard research question:

```text
Is there a small typed family of canonical enrichments that repeatedly restores
capability sufficiency across domains?
```

This is bolder and more publishable than another non-factorization example.

## 27. Add A Conservative "Derivation" Claim

If the note wants to say "derive physics" without being wrong, use this:

```text
Given established physics, derive the capability object induced by that
physics for a declared observer/task/horizon/boundary. Then ask whether a
chosen projection preserves it.
```

Do not use:

```text
derive established physics from capability
```

until an actual theorem exists.

Strong safe sentence:

```text
The immediate direction is not capability -> physics, but physics -> induced
capability geometry -> projection sufficiency audit.
```

Long-horizon speculative sentence:

```text
Only if the induced capability geometries across mature theories share a
canonical form would it become reasonable to ask whether capability geometry is
more than an audit layer.
```

## 28. Best Possible Strengthened Governing Paragraph

Suggested replacement governing paragraph:

```text
For a declared observer, schema, resolution, domain, task family, horizon, and
resource boundary, a projection pi : Y -> X is sufficient for future capability
exactly when the domain-native capability object Cap : Y -> K factors through
pi up to the declared equivalence on K. Equivalently, Cap must be constant on
each pi-fiber. The Candidate North Star is not that projections can fail; that
is old. The possible contribution is a disciplined audit surface for typing
Cap, testing projection sufficiency, identifying minimal capability-preserving
quotients, and comparing the canonical enrichments that repair projection
failure across domains.
```

## 29. Best Possible Strengthened Physics Paragraph

Suggested high-level physics paragraph:

```text
Physics should enter only after the mathematical schema is fixed. Given a
physical theory with states, dynamics, allowed interactions, causal/access
boundaries, and resource constraints, the theory induces a capability object:
the admissible future operations available from a state to a declared observer
over a declared horizon. Gravity, black holes, dark energy, particle quantum
numbers, and cosmological hidden structure are not evidence for the North
Star. They are domains where established physics already makes future
operation availability depend on geometry, causal access, representations,
resources, or source structure. The disciplined question is whether a chosen
observer-facing projection preserves those induced capability objects.
```

## 30. Best Possible Strengthened Bottom Line

Suggested bottom line:

```text
The hard mathematical content is projection sufficiency for typed capability
objects. The hard negative result is prior-art absorption. The hard positive
target is a canonical capability-preserving quotient or enrichment family that
appears across domains. The physics-facing ambition is allowed only in the
direction from known physics to induced capability geometry, unless future
theorems justify going further.
```

