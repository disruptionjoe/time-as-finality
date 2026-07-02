# Technical Report: Native Comparison Regime Appendix v0.1

## Status

Internal method-hardening artifact.

This report does not promote a claim, change the North Star, update the test
registry, move the roadmap, alter public posture, or assert new physics. It
implements the first next research action named in
`Method - Research Program Guidelines.md`: write a native-comparison appendix
for capability objects whose codomains are not simple equality-valued sets.

The current worktree already contains an active region-indexed capability batch
touching `TESTS.md`, `ROADMAP.md`, claims, models, results, and tests. This
report intentionally stays in a separate documentation lane and gives future
witnesses an intake gate rather than creating a new numbered test.

## Objective

Turn the generic Capability Projection question:

```text
Does the visible projection determine the capability object?
```

into a regime-specific audit:

```text
For the declared structure on K, what does "determine" mean, which native
comparison R_K is allowed, and what absorber would restore sufficiency without
residue?
```

This matters because many TaF and Capability Projection candidates now use
capability objects that are naturally preorder-valued, metric/tolerance-valued,
decision-valued, stochastic, resource-theoretic, or category-like. Treating all
of them as equality-valued objects makes witnesses too easy to inflate and too
easy to dismiss.

## Common Spine

For an audit context, declare:

```text
Y       source structure
A       admissible source states, A subset Y
O       observer or access profile
pi      visible projection, pi : A -> X
~=_X    visible equivalence
T       task family
h       horizon
B       boundary, budget, or resource condition
Cap     capability object, Cap : A -> K
R_K     native capability comparison on K
```

The reusable proof spine is:

```text
visible fiber -> capability spread -> native absorber -> minimal enrichment
```

For a visible class `[x]`, define the raw capability spread:

```text
Spread_Cap([x]) = { Cap(y) | y in A and pi(y) ~=_X x }
```

The projection is capability-sufficient only after `Spread_Cap([x])` is judged
under the declared native regime. "Singleton" is the right test only in the
plain equivalence-valued regime.

## Regime 1: Equivalence-Valued K

Use when the native capability verdict is genuinely a class, label, exact
certificate, or isomorphism type.

Declare:

```text
R_K = ~=_K
```

Sufficiency test:

```text
for all y1, y2 in A:
  pi(y1) ~=_X pi(y2) => Cap(y1) ~=_K Cap(y2)
```

Spread criterion:

```text
Spread_Cap([x]) / ~=_K has cardinality 1 for every visible class.
```

Allowed result language:

- `factors through visible equivalence`;
- `capability-kernel quotient`;
- `exact projection-sufficiency failure`.

Absorber questions:

- Did the visible equivalence forget a legitimate native state field?
- Is the alleged distinction only relabeling, gauge, basis choice, or
  convention?
- Is the quotient already a standard completion in the neighboring field?

Demotion condition:

```text
Adding the neighboring field's normal state variables makes Cap constant on
visible fibers.
```

## Regime 2: Preorder-Valued K

Use when capability means reachability, convertibility, dominance, inclusion
of available operations, future option sets, or viability.

Declare:

```text
K       preorder, (K, <=_K)
R_K     mutual convertibility, same downset/upset, order-embedding preservation,
        or a named monotone-preservation criterion
```

Do not silently collapse a preorder into a scalar. A product preorder can have
incomparability that is completely ordinary and already absorbed by resource
or opportunity-set language.

Possible sufficiency tests:

```text
mutual-equivalence test:
  Cap(y1) <=_K Cap(y2) and Cap(y2) <=_K Cap(y1)

downset/upset test:
  Down(Cap(y1)) = Down(Cap(y2)) and Up(Cap(y1)) = Up(Cap(y2))

monotone-vector test:
  declared complete monotone vector agrees
```

Spread criterion:

```text
Spread_Cap([x]) collapses to one equivalence class in the declared preorder
reflection, or its order width stays within the declared threshold.
```

Allowed result language:

- `preorder absorption`;
- `incomparability is ordinary resource structure`;
- `capability split survives preorder reflection`;
- `order-width witness`.

Absorber questions:

- Is the capability object just a native resource preorder under another name?
- Did the witness compare a product preorder to a scalar and mistake
  non-totality for novelty?
- Are all free operations, allowed transitions, and resource boundaries fixed?

Demotion condition:

```text
The split is exactly recovered by the neighboring field's admitted preorder,
monotones, or viability kernel.
```

## Regime 3: Metric Or Tolerance-Valued K

Use when capability is error, distance, distortion, regret, robustness,
latency, reconstruction loss, or certified approximation quality.

Declare:

```text
d_K     native distance or divergence
epsilon accepted tolerance
R_K     d_K(Cap(y1), Cap(y2)) <= epsilon
```

Sufficiency test:

```text
diameter_dK(Spread_Cap([x])) <= epsilon for every visible class.
```

Do not choose `epsilon` after seeing the witness pair. The tolerance must come
from the domain's native success criterion, measurement resolution, risk
budget, or review protocol.

Allowed result language:

- `bounded-spread preservation`;
- `epsilon-sufficiency`;
- `value-gap failure`;
- `robustness envelope`.

Absorber questions:

- Is the value gap below the domain's normal tolerance?
- Is the metric the one the neighboring field uses?
- Does a calibration, error bar, confidence interval, or finite-sample
  threshold absorb the spread?

Demotion condition:

```text
All visible-fiber spreads stay inside the native tolerance envelope.
```

## Regime 4: Decision Or Risk-Valued K

Use when capability is action quality, Bayes risk, policy value, experiment
informativeness, decision dominance, or optimal control performance.

Declare:

```text
L       loss or payoff family
D       decision/action class
V_K     value, risk, regret, or deficiency object
R_K     value gap <= epsilon, equal optimal policy set, Blackwell-style
        dominance, or a declared task-family comparison
```

Sufficiency test options:

```text
same optimal decisions:
  argopt_D V(y1) = argopt_D V(y2)

bounded value gap:
  |V(y1) - V(y2)| <= epsilon

experiment dominance:
  experiment(pi(y1)) and experiment(pi(y2)) are equivalent under the declared
  comparison of experiments
```

Spread criterion:

```text
Spread_Cap([x]) has zero or bounded regret/value gap under the predeclared
decision family.
```

Allowed result language:

- `decision-sufficiency failure`;
- `Blackwell-style absorber candidate`;
- `regret spread`;
- `policy-set split`.

Absorber questions:

- Is the task family fixed before selecting the witness?
- Would a belief state, sufficient statistic, experiment map, or control state
  restore sufficiency?
- Is the split universal over a decision class or only one cherry-picked loss?

Demotion condition:

```text
A native sufficient statistic, belief state, experiment comparison, or control
state absorbs the split under the same task family.
```

## Regime 5: Probabilistic Or Statistical K

Use when capability is a distribution, posterior, likelihood family, stochastic
kernel, predictive law, or confidence-bearing certificate.

Declare:

```text
Delta_K native comparison: equality in distribution, total variation,
        Wasserstein, KL under conditions, coupling, likelihood-ratio class,
        posterior decision equivalence, or confidence envelope
R_K     Delta_K(Cap(y1), Cap(y2)) <= epsilon
```

Sufficiency test:

```text
sup_{y1,y2 in fiber} Delta_K(Cap(y1), Cap(y2)) <= epsilon
```

Allowed result language:

- `statistical experiment split`;
- `distributional spread`;
- `coupling failure`;
- `posterior-sufficiency boundary`.

Absorber questions:

- Are sample size, estimator, measurement channel, and uncertainty budget
  fixed?
- Does the neighboring statistical model already include the latent parameter,
  sufficient statistic, or experiment family?
- Is an observed difference smaller than the declared inference threshold?

Demotion condition:

```text
The split vanishes under the native statistical experiment, sufficient
statistic, or uncertainty envelope.
```

## Regime 6: Resource-Theoretic K

Use when capability is constrained conversion under free operations, resource
monotones, catalytic availability, thermodynamic work, entanglement,
communication, memory, erasure budget, or operation availability.

Declare:

```text
F       free operations
~_F     mutual convertibility under F
M       declared monotones, if complete for the finite fixture
R_K     ~_F, or equality/threshold of a declared complete monotone vector
```

Sufficiency test:

```text
pi(y1) ~=_X pi(y2) => Cap(y1) ~_F Cap(y2)
```

or, where monotones are complete in the finite artifact:

```text
M(Cap(y1)) = M(Cap(y2))
```

Allowed result language:

- `resource-preorder absorption`;
- `fixed-free-class capability split`;
- `monotone-vector certificate`;
- `conversion obstruction`.

Absorber questions:

- Are the free operations, catalysts, budgets, access regions, and boundary
  conditions fixed?
- Is the region index merely a context parameter of the resource theory?
- Are monotones complete only for the finite fixture, or generally?

Demotion condition:

```text
The split is exactly a standard resource-state, free-operation, or monotone
distinction once the native frame is admitted.
```

## Regime 7: Category-Valued Or Structure-Valued K

Use when capability is a category, functor, fibration, sheaf, presheaf,
transition system, process semantics, proof obligation set, or structured
interface.

Declare:

```text
K       target category or structured class
R_K     isomorphism, equivalence, natural isomorphism, simulation,
        bisimulation, reflection, fibration-preserving comparison, or a named
        semantic preorder
```

Sufficiency test:

```text
visible-equivalent sources map to R_K-equivalent structures.
```

Spread criterion:

```text
Spread_Cap([x]) is equivalent in the declared categorical/semantic
comparison, or collapses under the declared reflection.
```

Allowed result language:

- `semantic abstraction failure`;
- `functoriality boundary`;
- `reflection absorption`;
- `bisimulation/testing-equivalence split`.

Absorber questions:

- Is the comparison too strict, treating presentation differences as semantic
  differences?
- Does a standard quotient, reflection, completion, or bisimulation collapse
  the split?
- Is functoriality actually proved in the declared direction?

Demotion condition:

```text
The alleged split disappears under the neighboring field's standard semantic
equivalence or reflection.
```

## Cross-Regime Guardrails

Every future witness should answer these before any residue label:

1. Which regime is primary?
2. Is `R_K` fixed before selecting the witness pair?
3. Is `Cap` domain-native or operationally forced?
4. Does the positive control preserve under the same `R_K`?
5. Does the negative fixture fail under the same `R_K`?
6. Which native absorber is granted first?
7. Which trivial enrichment restores sufficiency?
8. Is the proposed minimal enrichment smaller than `pi'(y) = (pi(y), Cap(y))`?
9. Is any physical, geometric, or novelty language earned only after the
   native absorber pass?
10. What exact result would demote the witness to translation, heuristic,
   redundant, or closed?

## Relationship To Current TaF Lanes

This appendix does not decide the active region-indexed capability
discriminator lane. It clarifies how that lane should be judged:

- T398-style `C(R)` profile objects are preorder/resource-regime objects, not
  scalar objects.
- T399-T406 boundary and finality-lock screens require decision/task,
  causal-access, transition-system, and resource-state comparisons to be fixed
  before residue language.
- A future stronger discriminator must survive all relevant native regimes, not
  merely one equality-valued projection test.

It also reactivates the dormant cross-domain shadow-protection theorem only as
a method target:

```text
If two domains instantiate the same visible-fiber / capability-spread /
native-absorber / minimal-enrichment spine with their own R_K, then the repo
has a reusable audit form.
```

That is not a physics theorem and not a novelty claim.

## Recommended Next Artifact

Working title:

```text
Two-Domain Native-Comparison Shadow Audit
```

Minimum scope:

1. Fill `workflows/templates/north-star-shadow-audit.template.md` for one
   formal/computational domain and one physics-facing or resource-facing domain.
2. Predeclare `R_K` in each domain before choosing the witness pair.
3. Include one positive preservation control and one negative non-factorization
   fixture per domain.
4. Run native absorber passes before assigning residue.
5. Compare only the spine, not surface vocabulary.

Success criterion:

```text
The same audit spine works in two domains while each domain keeps its own
native comparison.
```

Failure criterion:

```text
The only shared result is the trivial fiber-constancy lemma, or each domain
requires an ad hoc comparison invented after the fixture is known.
```

## Claim And Governance Impact

No claim status changes.

No claim-ledger update.

No roadmap edit.

No test registry edit.

No external-facing posture change.

The durable result is a conservative intake rule:

```text
Do not ask whether pi preserves Cap until K's native comparison has been
declared and the neighboring absorber has been granted its normal state,
operations, equivalences, thresholds, and theorems.
```
