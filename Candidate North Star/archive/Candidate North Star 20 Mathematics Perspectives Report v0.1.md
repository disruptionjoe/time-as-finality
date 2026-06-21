# Candidate North Star: 20 Mathematics-Based Perspectives Report v0.1

## Status

This is a companion report for:

```text
Candidate North Star v0.3.md
Candidate North Star Mathematical Strengthening Suggestions v0.1.md
```

It does not update canon.
It does not promote the Candidate North Star.
It does not claim new physics.
It does not treat repo results as evidence.

Purpose:

```text
Use 20 distinct mathematics-based perspectives to identify:
1. what can be strengthened;
2. what is weakest;
3. what would make the Candidate North Star difficult to attack
   at the mathematical level.
```

Working core:

```text
pi : Y -> X
Cap : Y -> K
```

The central question:

```text
Does Cap factor through pi up to the declared equivalence on K?
```

Equivalently:

```text
for all y1,y2 in Y,
pi(y1)=pi(y2) implies Cap(y1) ~=_K Cap(y2).
```

If not, the projection is capability-insufficient for the declared observer,
task, horizon, and boundary.

## Executive Synthesis

The strongest mathematical version of the Candidate North Star is:

```text
Projection sufficiency for typed capability objects.
```

The weakest point is not the factorization statement. That part is solid.

The weakest point is:

```text
What exactly is K?
What counts as capability equivalence?
Why is the chosen Cap canonical rather than gerrymandered?
```

The most durable strengthening move is:

```text
For every domain, require:

Y:
X:
pi:
K:
Cap:
equivalence ~=_K:
minimal capability-preserving quotient:
positive factorization case:
negative non-factorization case:
native prior-art absorber:
residue if any:
```

The boldest safe physics move is:

```text
Given known physics, derive the induced capability object from states,
dynamics, constraints, allowed operations, causal/access boundaries, and
resources. Then ask whether a chosen observer-facing projection preserves that
capability object.
```

This direction is hard to object to because it does not derive physics from
capability. It derives a capability audit from physics.

## Cross-Cutting Weak Points

Across the 20 perspectives, the same weaknesses recur.

1. `Cap` is under-typed.

```text
Set, preorder, category, resource theory, sheaf, and policy object are not
interchangeable. Each gives a different meaning to capability equivalence.
```

2. The projection equality is often underdeclared.

```text
same visible state
```

must become:

```text
same visible state under observer O, schema Sigma, resolution r, domain U,
time/snapshot convention tau, and equivalence ~=_X.
```

3. Non-factorization alone is too easy.

```text
Every bad projection loses something.
```

The hard target is a domain-natural projection and a domain-natural capability
object where the residue survives obvious enrichment and native theory.

4. State enrichment always repairs the diagram.

```text
pi'(y) = (pi(y), Cap(y))
```

always makes `Cap` factor. So the question is not whether repair is possible,
but whether the repair is minimal, canonical, natural, or physically meaningful.

5. Physics sections are safe only when written as induced-capability audits.

```text
Known physics -> induced Cap -> projection sufficiency question.
```

The reverse direction is not earned:

```text
Cap -> known physics.
```

## 1. Quotient And Descent Perspective

### Strengthen

Make the quotient/descent theorem explicit:

```text
Cap descends along pi iff Cap is constant, up to ~=_K, on every pi-fiber.
```

Define:

```text
y1 ~_Cap y2 iff Cap(y1) ~=_K Cap(y2).
```

Then:

```text
Y / ~_Cap
```

is the minimal capability-preserving quotient.

### Weakest Point

The note sometimes treats non-factorization as profound by itself. From this
perspective it is just descent failure.

### Hardening Move

For every example, show where `pi` sits relative to the capability quotient:

```text
ker(pi) subset ker(Cap)       sufficient
ker(pi) not subset ker(Cap)   insufficient
```

This is the core invariant. It is the spine.

## 2. Category-Theoretic Perspective

### Strengthen

Treat `Cap` not merely as a function but as a structure-preserving assignment:

```text
Cap : Y -> K
```

where `Y` and `K` may be categories, preorders, or indexed categories.

The factorization question becomes:

```text
Does Cap factor through pi in the relevant category?
```

### Weakest Point

The word "faithful" risks confusion. In category theory, faithful means
injective on hom-sets. The note's intended meaning is different.

### Hardening Move

Use:

```text
capability-insufficient projection
projection-sufficiency failure
capability-nondetermining projection
```

Avoid:

```text
capability-nonfaithful
```

unless a real functorial faithfulness condition is being used.

## 3. Fibration / Indexed-Category Perspective

### Strengthen

If capability varies over visible states, express it as an indexed structure:

```text
P : X^op -> Cat
```

or as a fibration:

```text
q : E -> X.
```

Here, the fiber over `x` is not merely:

```text
pi^{-1}(x)
```

but a category of operations/capabilities available over that visible state.

### Weakest Point

The document uses "fiber" in two senses:

```text
projection fiber: pi^{-1}(x)
capability fiber: operations available over x
```

These should not be collapsed.

### Hardening Move

Reserve terms:

```text
source fiber = pi^{-1}(x)
capability fiber = q^{-1}(x) or Cap-spread over pi^{-1}(x)
```

Then ask whether the capability fibration is pulled back from `X` or requires
source-level structure in `Y`.

## 4. Order-Theoretic Perspective

### Strengthen

Model capability as a preorder:

```text
c1 <= c2
```

meaning:

```text
c2 has at least the admissible operations of c1
```

or:

```text
c1 can be simulated, refined, or reached by c2.
```

Then projection failure can be sharpened:

```text
pi(y1)=pi(y2)
but Cap(y1) and Cap(y2) are incomparable
```

or:

```text
Cap(y1) < Cap(y2).
```

### Weakest Point

Set equality is often too crude. Two capability sets can differ extensionally
while being equivalent under closure, simulation, or dominance.

### Hardening Move

Use preorders as the default `K` for future operations:

```text
K = capability preorder
~= _K = mutual reachability / order equivalence
```

This makes comparisons more robust than raw set equality.

## 5. Lattice / Closure-System Perspective

### Strengthen

If operations close under composition, union, restriction, or consequence,
capability should be a closure object.

Define:

```text
cl(Ops(y))
```

as the closure of operations generated from state `y`.

Then compare:

```text
cl(Ops(y1)) ~= cl(Ops(y2)).
```

### Weakest Point

A raw operation list is unstable. A critic can say the difference disappears
once operations are closed under the domain's natural rules.

### Hardening Move

Always compare closed capability objects:

```text
Cap(y) = closure of admissible generators under declared composition rules.
```

This prevents toy examples from depending on arbitrary operation naming.

## 6. Resource-Theoretic Perspective

### Strengthen

When physics or transformations are involved, define capability as
convertibility under allowed operations:

```text
y >=_R z
```

meaning:

```text
y can be converted to z under allowed operation class R.
```

Then:

```text
Cap_R(y) = { z | y >=_R z }.
```

### Weakest Point

"Future capability" can sound invented when resource theory already has
allowed operations, monotones, and convertibility.

### Hardening Move

For physics-facing sections, prefer:

```text
resource-theoretic capability
```

over a generic capability set. This immediately gives `K`, equivalence, and
absorbers.

## 7. Statistical Decision-Theory Perspective

### Strengthen

Use sufficiency language.

Let:

```text
pi(Y)
```

be a statistic or experiment output. It is sufficient for a decision problem
if it preserves all decision-relevant information.

North Star translation:

```text
pi is capability-sufficient for task family T iff it preserves all
T-relevant decision/capability values.
```

### Weakest Point

The core idea is old if it only says:

```text
a statistic can be insufficient.
```

### Hardening Move

Say explicitly:

```text
The North Star does not rediscover insufficiency. It asks whether a
cross-domain capability-sufficiency audit can compare several kinds of
insufficiency under one typed schema.
```

## 8. POMDP / Belief-State Perspective

### Strengthen

For decision/control settings:

```text
hidden state s
observation o = pi(s)
belief b = P(s | history)
```

Raw observation is generally not sufficient. Belief state is often the
standard sufficient object.

### Weakest Point

Any example where visible state fails for future control may be instantly
absorbed by POMDP theory.

### Hardening Move

In decision/control examples, require the question:

```text
Does Cap factor through observation, belief state, or neither?
```

If it factors through belief state, record the witness as absorbed, not as
new.

## 9. Control / Observability Perspective

### Strengthen

Control theory already distinguishes:

```text
same output
different internal state
different controllability / reachability / observability
```

The North Star can use:

```text
output map h : State -> Output
reachable set R(x)
```

Projection failure:

```text
h(x1)=h(x2)
but R(x1) != R(x2).
```

### Weakest Point

"Same visible state, different future capability" is almost exactly a control
observability/reachability issue in many domains.

### Hardening Move

For dynamical systems, define:

```text
Cap(y) = reachable set under declared controls, constraints, and horizon.
```

Then compare against standard observability and reachability before claiming
residue.

## 10. Abstract Interpretation Perspective

### Strengthen

Use:

```text
alpha : Concrete -> Abstract
gamma : Abstract -> P(Concrete)
```

and ask whether the abstraction is complete for the capability property.

Projection sufficiency becomes:

```text
alpha is complete for Cap.
```

### Weakest Point

Most projection failures are merely incomplete abstractions.

### Hardening Move

Classify each witness:

```text
sound abstraction?
complete abstraction?
incomplete but repairable?
minimal complete abstraction known?
```

This gives the North Star a mature mathematical backbone.

## 11. Process Semantics / Bisimulation Perspective

### Strengthen

In process theory, two states are equivalent only relative to allowed tests:

```text
trace equivalence
failure equivalence
ready equivalence
bisimulation
may/must testing
```

North Star translation:

```text
Cap is the class of future tests a state can pass.
```

### Weakest Point

The idea "same observation, different future discriminability" is deeply
studied here.

### Hardening Move

For any computational/protocol example, ask:

```text
Which process equivalence is the capability equivalence?
```

If a known equivalence already classifies the distinction, record absorption.

## 12. Automata / Nerode Perspective

### Strengthen

For sequential behavior, use the Myhill-Nerode style idea:

```text
s1 ~ s2 iff all future continuations produce equivalent outcomes.
```

Capability quotient:

```text
states are equivalent when no future task distinguishes them.
```

### Weakest Point

If future capability means all possible future continuations, then minimal
automata theory may already give the coarsest sufficient quotient.

### Hardening Move

For finite sequential examples, define the capability-preserving quotient as a
Nerode-style equivalence. This is extremely hard to dismiss.

## 13. Sheaf / Local-To-Global Perspective

### Strengthen

If the North Star involves local observer patches, define:

```text
Cap : C^op -> K
```

where `C` is a site or patch category.

Then ask:

```text
local factorization on patches
global factorization after gluing
```

### Weakest Point

Sheaf language is often ornamental unless restriction and gluing really do
work.

### Hardening Move

Require a local/global test:

```text
Do locally capability-sufficient projections glue into a globally
capability-sufficient projection?
```

If not, identify the obstruction.

## 14. Topological Perspective

### Strengthen

Topology asks what structure survives continuous maps, quotients, and
identifications.

Projection failure can be expressed as:

```text
pi identifies points lying in different capability strata.
```

Define strata:

```text
Y_k = { y | Cap(y) has type k }.
```

Then `pi` is capability-sufficient only if it does not collapse distinct
capability strata into one visible state.

### Weakest Point

Without topology on `Y`, `X`, or `K`, geometric language may be decorative.

### Hardening Move

When using geometry, define at least one of:

```text
topology on Y
topology on X
stratification by capability type
continuity or semicontinuity of Cap
```

Then say what projection preserves or destroys.

## 15. Differential-Geometric Perspective

### Strengthen

If `Y -> X` is treated as a bundle, separate:

```text
bundle fibers
sections
connections / transport
capability assignments
```

A geometry-backed capability object might be:

```text
Cap(s) = admissible transports, curves, or sections from s
```

### Weakest Point

Geometry language can overstate itself. A bundle alone does not provide
dynamics, rates, or capability.

### Hardening Move

Use differential geometry only when a real geometric object is declared:

```text
connection
metric
distribution
constraint subbundle
reachable distribution
holonomy
```

Then derive capability from that object.

## 16. Gauge / Invariant-Theory Perspective

### Strengthen

Distinguish:

```text
gauge-equivalent differences
physical/capability-relevant differences
```

Projection should not count pure relabelings as capability distinctions.

Mathematical condition:

```text
Cap(g.y) ~=_K Cap(y)
```

for gauge/relabeling transformations `g`.

### Weakest Point

If capability changes under mere relabeling, it is not well-defined.

### Hardening Move

Add an invariance audit:

```text
pure relabeling: Cap invariant
access-boundary change: Cap covariant
illegal transformation: outside domain
```

This connects directly to the repo's gauge-invariance discipline.

## 17. Measure / Probability Perspective

### Strengthen

If capability is uncertain, define a probability kernel:

```text
P(Cap | x)
```

or use disintegration over fibers:

```text
P_Y(dy | pi(y)=x).
```

Then projection insufficiency becomes:

```text
positive conditional spread of Cap over pi^{-1}(x).
```

### Weakest Point

Set-based fiber spread ignores likelihood. Some distinctions may exist but be
measure-zero or operationally negligible.

### Hardening Move

Add probabilistic summaries:

```text
entropy of Cap over fiber
expected regret from using pi
deficiency / decision loss
probability of capability misclassification
```

This makes the audit quantitative when exact equality is too brittle.

## 18. Information-Theoretic Perspective

### Strengthen

Use conditional information:

```text
I(Cap(Y); Y | pi(Y))
```

If this is zero, the projection captures capability information. If positive,
there is capability-relevant information left in the source state.

### Weakest Point

Information measures alone do not define capability. They quantify dependence
after `Cap` is defined.

### Hardening Move

Use information theory only after typing `Cap`:

```text
first define Cap
then measure how much capability-relevant information pi preserves
```

Possible metric:

```text
Capability information loss = I(Cap(Y); Y) - I(Cap(Y); pi(Y)).
```

## 19. Causal-Inference Perspective

### Strengthen

Causal inference distinguishes:

```text
observational equivalence
interventional equivalence
counterfactual equivalence
```

North Star translation:

```text
same observed state may not determine intervention capability.
```

Define:

```text
Cap(y) = set of identifiable interventions, effects, or policies from y.
```

### Weakest Point

If the capability question is really interventional identifiability, causal
inference already owns it.

### Hardening Move

For causal examples, state whether `Cap` is:

```text
observational query
interventional query
counterfactual query
policy query
```

Then compare to standard identifiability before claiming residue.

## 20. Physics-Induced Capability Geometry Perspective

### Strengthen

This is the boldest safe perspective.

For a physical theory `P`, define:

```text
State_P
Dynamics_P
Ops_P
Constraints_P
Observers_P
```

Then:

```text
Cap_P(y;O,T,h,B) =
  admissible operation sequences from y
  under Dynamics_P, Ops_P, Constraints_P,
  for observer O, task family T, horizon h, boundary B.
```

The projection audit is:

```text
Does Cap_P factor through the observer readout pi_P?
```

### Weakest Point

If written carelessly, this sounds like deriving physics from capability.
That is not earned.

### Hardening Move

Write the direction explicitly:

```text
known physics -> induced capability geometry -> projection sufficiency audit
```

not:

```text
capability geometry -> known physics
```

This permits bold physics sections without contradicting known objective truth.

## Ranking: Hardest Strengthenings To Attack

These are the strongest additions because they are close to definitions,
standard theorems, or mature mathematical frameworks.

1. Factorization iff fiber-constancy.
2. Minimal capability-preserving quotient.
3. Trivial enrichment theorem.
4. Capability spread over projection fibers.
5. Abstract interpretation completeness framing.
6. Database view determinacy as finite calibration.
7. Resource-theoretic convertibility for physical capability.
8. POMDP belief-state absorber for decision capability.
9. Gauge/relabeling invariance audit.
10. Physics-induced capability geometry template.

## Ranking: Weakest Current Surfaces

These are the places hostile mathematical readers will press first.

1. `Cap` type not fixed.
2. Capability equivalence not fixed.
3. Physics examples can read as claims unless forced through the template.
4. Non-factorization can be trivial if the projection is obviously too crude.
5. "Same visible state" can be underspecified.
6. Raw set equality of operations can be too brittle.
7. Sheaf/bundle language can become decorative.
8. Probability and information measures can be applied before `Cap` is typed.
9. Prior art may absorb most examples.
10. No canonical enrichment family has been proven.

## Suggested Report-Level Additions To v0.3

### Add This Definition

```text
A projection pi : Y -> X is capability-sufficient for Cap : Y -> K when Cap
factors through pi up to ~=_K. It is capability-insufficient when there exist
y1,y2 in Y with pi(y1)=pi(y2) but Cap(y1) not ~=_K Cap(y2).
```

### Add This Theorem-Shaped Lemma

```text
Lemma: Cap factors through pi up to ~=_K iff Cap is ~=_K-constant on every
pi-fiber.
```

### Add This Failure Condition

```text
If every domain-natural witness is absorbed by minimal state enrichment or by
the native theory's own sufficiency/completeness/equivalence theorem, then
Capability Projection has translation value only.
```

### Add This Physics Guardrail

```text
Physics sections must derive Cap from known physics and then test projection
sufficiency. They must not derive physics from Cap.
```

### Add This Positive Target

```text
The strongest possible positive result is not another projection failure. It
is a small canonical family of enrichments that repeatedly restores capability
sufficiency across mature domains.
```

## Final Recommendation

The Candidate North Star can be made much harder to poke holes in if it shifts
from:

```text
observable equivalence is not capability equivalence
```

to:

```text
projection sufficiency for typed capability objects,
with explicit minimal quotients, enrichment repairs, and prior-art absorption
tests.
```

The physics sections should stay. They should become more technical, not
shorter, but they must follow the safe direction:

```text
known physics induces capability structures;
the North Star audits which observer-facing projections preserve them.
```

That is bold. It is also mathematically sober.

