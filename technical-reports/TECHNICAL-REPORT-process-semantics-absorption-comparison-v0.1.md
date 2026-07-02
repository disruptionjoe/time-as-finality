# Technical Report: Process-Semantics Absorption Comparison v0.1

## Status

Internal method-hardening artifact.

This report does not promote a claim, change the North Star, update the
roadmap, update the claim ledger, register a numbered test, create an
executable model, or assert new physics. It advances one remaining bounded
action from `Method - Research Program Guidelines.md`: run a
process-semantics absorption comparison using future tests, trace projection,
testing equivalence, failure semantics, bisimulation, and a Nerode-style
quotient.

The current worktree contains an active executable region/capability lane
touching `TESTS.md`, `ROADMAP.md`, claims, models, results, audits, and
numbered-test surfaces. This report intentionally stays in a disjoint
technical-report lane.

## Objective

Pressure-test the common pattern:

```text
same visible process trace or projection
different future-test capability
```

against mature process-semantics absorbers before treating it as Capability
Projection residue.

Expected result:

```text
translation residue unless a future executable artifact survives native
semantic completion and a predeclared test-language comparison
```

## Known Source Domain

Known theory or mature field:

```text
labelled transition systems, automata, operational semantics, process
semantics, testing equivalences, and Nerode-style behavioral quotients
```

Legitimate absorber state:

```text
states, initial state, action alphabet, observable/internal action split,
transition relation, branching structure, divergence policy, refusal/ready
sets where admitted, test language, success predicate, scheduler or
nondeterminism convention, composition rules, and horizon
```

Native operations:

```text
step, trace, hide, restrict, compose, synchronize, test, continue, observe
success, and quotient by a declared behavioral equivalence
```

Native equivalences or preorders:

```text
trace equivalence, failure equivalence, readiness equivalence, simulation,
bisimulation, may testing, must testing, testing preorder, language
equivalence, and Myhill-Nerode equivalence for deterministic sequential
fixtures
```

Native comparison:

```text
the chosen semantic equivalence or testing preorder, fixed before the fixture
is selected
```

## Source And Shadow

Source structure `Y`:

```text
finite labelled transition systems with a distinguished start state and a
declared observation/test alphabet
```

Observed base or interface `X`:

```text
the visible trace language, or a bounded visible trace summary, under the
declared alphabet and horizon
```

Observer/access profile `O`:

```text
an observer who sees completed visible traces but not branching time,
refusals, readiness sets, internal nondeterministic choice, or the full
transition relation unless those fields are explicitly included
```

Projection or shadow map:

```text
pi_trace(P) = visible traces of process P under the declared alphabet and
horizon
```

Visible equivalence:

```text
P ~=_X Q iff pi_trace(P) = pi_trace(Q)
```

Admissible source states:

```text
finite transition systems over the same alphabet, observation policy,
nondeterminism convention, and horizon
```

Boundary, horizon, or resource condition:

```text
the horizon, action alphabet, hidden-action policy, and test grammar are fixed
before comparing processes
```

## Capability Object

Task family:

```text
future tests or continuations drawn from the declared process-test grammar
```

Capability object:

```text
Cap(P) = the future-test envelope of P under the declared grammar:
         which tests it may pass, must pass, can refuse, is ready for,
         simulates, or is bisimilar to, depending on the chosen native regime
```

Capability codomain `K`:

```text
a behavioral semantics object: trace set, failure set, ready set,
may/must-testing profile, simulation/bisimulation class, or Nerode class
```

Native capability comparison `R_K`:

```text
the predeclared semantic equivalence or preorder on K
```

Why `Cap` is domain-native:

```text
process semantics already studies future discriminability by tests,
continuations, and behavioral equivalences
```

Positive preservation controls:

1. If `Cap` is trace language and `pi_trace` is the full declared trace
   language, then `Cap` factors through `pi_trace`.
2. If the projection is enriched to the declared bisimulation quotient, then
   every bisimulation-invariant test capability factors through the enriched
   projection.
3. In a deterministic finite automaton fixture, if the projection retains the
   Myhill-Nerode state for the declared language task, future language
   capability factors through that state.

Negative non-factorization fixture:

```text
P = a.b + a.c
Q = a.(b + c)
```

Under a trace-only observer:

```text
traces(P) = traces(Q) = { epsilon, a, ab, ac }
```

But after the visible trace `a`, the branching/readiness structure differs:

```text
P can be in a state ready only for b or only for c
Q is in a state ready for both b and c
```

A future test that asks for guaranteed availability of both `b` and `c` after
`a` can distinguish the processes under readiness, failure, must-testing, or
bisimulation-sensitive semantics.

Capability spread over the trace-visible fiber:

```text
Spread_Cap([traces = {epsilon, a, ab, ac}]) =
  { trace-only class,
    readiness profiles,
    failure profiles,
    may/must testing profiles,
    bisimulation classes,
    Nerode classes for deterministic completions }
```

The spread is non-singleton only when `Cap` asks for more than trace-language
capability.

## Absorber Passes

### Trace Equivalence

If the task only asks:

```text
which visible traces are possible?
```

then the trace projection is sufficient by construction. The negative fixture
does not separate capability under trace-valued `K`.

Absorber verdict:

```text
trace-valued capability absorbs the alleged split
```

### Failure And Readiness Semantics

If the task asks which actions can be refused, offered, or guaranteed after a
trace, trace language is underdescribed. Failure or readiness semantics are
the native completion.

The fixture above is useful as a calibration case, but it is not residue
beyond process semantics. It says:

```text
trace projection forgot native branching/refusal/readiness data
```

Absorber verdict:

```text
failure/readiness completion restores the domain-native comparison
```

### May/Must Testing

If `Cap` is the set of future tests a process may or must pass, then testing
semantics is not an analogy. It is the native object.

The audit must declare:

```text
test language, success condition, nondeterminism convention, may/must choice,
and horizon
```

before selecting the pair. Otherwise the witness is post hoc.

Absorber verdict:

```text
testing equivalence or testing preorder is the capability comparison
```

### Bisimulation And Simulation

If the task is branching-time, interaction-sensitive, or step-by-step
simulation-sensitive, bisimulation or simulation is the native comparison.

A trace-equivalent but non-bisimilar pair is therefore not surprising. It is
the standard reason bisimulation exists.

Absorber verdict:

```text
bisimulation/simulation completion absorbs branching-sensitive future tests
```

### Nerode-Style Quotient

For deterministic sequential fixtures, the coarsest state summary preserving
all future continuations for a declared language task is a Nerode-style
equivalence.

If a future capability object is:

```text
all future suffixes that lead to acceptance
```

then the minimal repair is not `pi'(y) = (pi(y), Cap(y))`. It is the
domain-native Nerode state.

Absorber verdict:

```text
Nerode quotient supplies the minimal sufficient enrichment for deterministic
language capability
```

## Absorption Matrix

| Declared capability `K` | Trace-only projection sufficient? | Native absorber |
| --- | --- | --- |
| Visible trace language | Yes | Trace equivalence |
| Refusal/failure capability | No | Failure semantics |
| Ready-set capability | No | Readiness semantics |
| May-test capability | Usually no | May testing preorder/equivalence |
| Must-test capability | Usually no | Must testing preorder/equivalence |
| Branching interaction capability | No | Simulation or bisimulation |
| Deterministic language continuation capability | No, unless Nerode state is visible | Myhill-Nerode quotient |

## Minimal Enrichment Discipline

The trivial enrichment:

```text
pi'(P) = (pi_trace(P), Cap(P))
```

always restores sufficiency. It is not the interesting repair.

Domain-natural repairs are:

```text
trace language                     for trace tasks
failure or ready sets              for refusal/readiness tasks
testing profile or preorder class  for future-test tasks
bisimulation quotient              for branching interaction tasks
Nerode state                       for deterministic continuation tasks
```

Each repair must be judged under the morphisms and equivalences that the
process-semantics domain already admits.

## Relationship To Current TaF Lanes

This report does not touch the active region-indexed capability discriminator
lane and does not decide any T404/T407/T408/T409/T410 result.

It does give a conservative review rule for future "operation availability"
or "future-test" artifacts:

```text
Before assigning residue, ask which process semantics is the native capability
comparison. If the split is exactly restored by transition-system completion,
testing equivalence, failure/readiness semantics, bisimulation, or a
Nerode-style quotient, record translation residue or native absorption.
```

This is consistent with the T406 transition-system gate: if the only changed
object is the transition relation or the semantic completion of that relation,
operation-unavailability language is underdescription rather than a claim
upgrade.

## Verdict

Projection-sufficient?

```text
Yes, when `K` is the visible trace language or when `pi` is enriched to the
native semantic quotient required by the declared task.
```

Projection-insufficient?

```text
Yes, trace-only projection is insufficient for refusal, readiness, may/must
testing, branching-time, and deterministic continuation capabilities that
require more than trace language.
```

Minimal enrichment or repair:

```text
use the native semantic quotient or profile: failure/readiness, testing,
bisimulation/simulation, or Nerode state, depending on the declared task
```

Residue label:

```text
translation residue
```

What survives:

```text
The Capability Projection audit usefully asks whether the visible projection
has enough native semantic state for the declared future-test capability.
```

What does not survive:

```text
No new process-semantics theorem.
No claim that same trace / different future tests is novel.
No claim-ledger movement.
No physics or geometry upgrade.
```

Kill condition:

```text
Any future witness that claims residue from trace-equivalent but
future-test-distinguishable processes is killed unless it first grants the
native process semantics appropriate to the declared tests and still finds a
same-neighbor-data split.
```

## Next Bounded Artifact

After the active dirty executable lane is settled, a safe next artifact would
be a small numbered executable fixture that computes the calibration pair
above across trace, readiness, failure, testing, bisimulation, and
Nerode-style summaries.

That future artifact should be numbered only after `TESTS.md` and `tests/`
are clean enough to check for conflicts.

## Short Verdict

Process semantics absorbs the generic future-test version of Capability
Projection. The useful contribution is not novelty; it is an intake rule:
declare the native process equivalence before selecting the witness pair, then
demote any trace-only split that disappears under standard semantic
completion.
