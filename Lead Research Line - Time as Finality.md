# North Star

## The Motivating Intuition

Observers participate in recursively nested structures where accessible worlds
expand through stabilized records, compatibility relations, and cross-layer
transport. Time may correspond to increasing finality within those
observer-accessible sections.

This is an aspirational intuition, not a claim. It is the direction that
motivates exploration. The mathematical program is the disciplined effort to
discover whether any part of this intuition survives rigorous testing — and
which parts do not.

The mathematics is not trying to prove the North Star. The mathematics is
trying to discover which small pieces of the North Star are actually true.

## Viability Filter Refinement

One current refinement is:

```text
geometry supplies candidate structures
  -> dynamics supplies reachable structures
  -> maintenance supplies structures that persist long enough
  -> finality supplies observer-reconstructable structures
  -> emergence supplies structures that become platforms for further structure
```

[T114](tests/T114-viability-filter.md) treats this only as a finite
viability-filter schema. It does not upgrade a core claim. The refinement is
useful only if record-finality or emergence-platform gates separate cases
after standard geometry, dynamics, maintenance, and thermodynamic variables
have been matched. Otherwise it collapses to ordinary stability accounting.

## Protected Intuition Anchor

The following intuition is protected as a source of research direction:

- Reality contains many observers.
- Observers create and exchange records.
- Records stabilize at finite rates.
- The structure of those stabilization processes may be more fundamental than
  the clocks observers later infer.

This is not a conclusion. It is a north-star generator of questions.

Do not dismiss this intuition merely because it is incomplete, imprecise,
difficult to formalize, or currently unsupported. Before replacing it with a
more conventional theory, ask:

```text
What follows if this intuition contains an important truth?
```

At the same time, do not jump directly from this intuition to strong physical
conclusions about the speed of light, relativity, spacetime, quantum mechanics,
or cosmology. Those conclusions must be earned independently.

The preferred research style is:

- ask what follows from local record systems;
- ask what follows from reconstruction constraints;
- ask what follows from stabilization processes;
- ask what mathematical structures emerge if records are primary;
- prefer executable tests over arguments;
- prefer theorem candidates over explanations;
- discover consequences rather than defend the intuition.

Good examples of the desired style include T19, T63, T69, T73, the H0/H1
reconstruction hierarchy, and the gated LossKernel program. These results and
open formal targets did not prove the intuition. They asked what followed from
it.

Failure modes to avoid:

- "the universe is a blockchain";
- "this explains the speed of light";
- "this proves spacetime emerges from records";
- treating the intuition as already established;
- dismissing the intuition because the current mathematics is incomplete;
- replacing the intuition with a fashionable framework before extracting its
  consequences.

The mathematics remains free to confirm, refine, weaken, reinterpret, or
partially reject any specific consequence. The goal is not:

```text
prove the intuition
```

The goal is:

```text
discover what necessarily follows if the intuition is pointing toward
something real
```

## What the Mathematics Has Moved Away From

The recent trajectory — T1 through T36 — has moved consistently away from
three assumptions that appeared reasonable at the start:

- **A hidden substrate** that all observers share and which ground the partial
  orders. The evidence pushes toward observer-relative sections, not a single
  underlying reality.
- **A privileged global object** from which local facts are projections. The
  evidence consistently shows that global sections often do not exist, and the
  obstruction to their existence is the most informative result.
- **Local-to-global as the natural direction**. The restriction direction has
  proven more productive: structure is projected downward, forgotten at each
  step, and the failure of that forgetting to be reversible is where the
  interesting mathematics lives.

These are not philosophical commitments. They are empirical findings from the
executable models. The North Star is stated in a way that does not depend on
any of them.

## What This Is Not

The purpose of this project is **not** to prove the founding intuitions correct.

If deeper mathematics explains current concepts as special cases, the current
concepts should be weakened, replaced, or removed. If a concept that was
treated as primitive turns out to be derived, remove it from the primitives.
If an intuition that motivated early work turns out to be wrong, preserve it
as a labeled negative result and move on.

The North Star should almost certainly be partially wrong. Its job is to
generate better questions, not to be vindicated.

## Research Stack

The project operates across five levels. Each level has different stability
and different evidential requirements.

| Level | Description | Stability |
| --- | --- | --- |
| **North Star** | The motivating intuition. Intentionally broader than current evidence. Should inspire decades of work while remaining falsifiable in pieces. | Rare change |
| **Research Program** | A sustained collection of models, claims, and theorems organized around a named intuition (e.g., Time as Finality). A program may become an application of the mathematical core rather than the center of it. | Slow evolution |
| **Research Bets** | Intermediate hypotheses that seem plausible given current evidence. Executable, falsifiable, replaceable. Examples: D1, PO1, IPT, RMT, H3. | Active revision |
| **Executable Models** | Finite computational models that generate the next questions. These are not merely test harnesses; they are epistemic instruments. A model that consistently produces surprising results is more valuable than one that confirms expectations. | Per-test iteration |
| **Claims and Theorems** | Specific statements supported by finite mathematical evidence (Claims) or formally established within the mathematical framework (Theorems). These are the only parts of the project that should be treated as durable mathematical knowledge. | High bar to change |

## Research Philosophy

A bold intuition is a starting point, not a conclusion.

Every attractive intuition should be treated as a hypothesis. Every hypothesis
should be made executable. Every executable model should be used to search
aggressively for counterexamples, not to confirm the hypothesis. Every
counterexample should be preserved and labeled, not explained away.

The methodology that has developed over T1 through T36:

1. Start with a bold intuition.
2. Build the smallest executable mathematics.
3. Search aggressively for counterexamples.
4. Narrow the claim to what survives.
5. Preserve the failures explicitly.
6. Promote only what the evidence earns.

Never mistake today's successful abstraction for tomorrow's primitive. Whenever
a richer mathematical structure explains several existing concepts as derived
observables, prefer the richer structure — even if it forces weakening or
abandoning earlier intuitions.

## Time as Finality

Time as Finality is the first major research program within this project. It
may turn out to be the first major application of a broader mathematical program
rather than its permanent center. That is not a problem; it would be evidence
that the mathematics has matured.

The mathematical objects generated so far — finite restriction systems, typed
forgetting, projection, obstruction, admissibility, the discovery engine — may
have accumulated enough independence that they no longer require TaF concepts to
be defined or applied. Whether that independence has been earned is tracked in
[MATHEMATICAL-INDEPENDENCE-AUDIT.md](MATHEMATICAL-INDEPENDENCE-AUDIT.md).

## Guiding Principle

The success criterion is not arrival at the destination.

The success criterion is that each step leaves us with mathematics that is more
precise, more falsifiable, and more explanatory than what we had before.

## Tri-Repo Placement (2026-07-02)

This lead line is TaF's leg of the ratified tri-repo division of labor: TaF
owns the **capability measure** — defining and testing the bounded-region
capability object C(R), the certificate machinery, and the region-indexed
capability discriminator (`open-problems/region-indexed-capability-discriminator.md`),
which is the current primary open problem. gu-formalization owns boundary
content; temporal-issuance owns the source question. Identity claims across
the three repos remain gated behind adapter contracts. See
[Coordination - Tri-Repo Division of Labor.md](Coordination%20-%20Tri-Repo%20Division%20of%20Labor.md).

## Adopted organizing frame (2026-07-02): capability-boundary mode taxonomy

The program's working classification of capability/finality boundaries is the
**four-mode taxonomy** — E0 declared / E1 asymptotic-limit / E2 hardness-assumption
/ E3 structural-symmetry — adopted as an internal map (a frame, not a promoted
claim): `technical-reports/capability-boundary-mode-taxonomy-REFERENCE.md`. It
derives from (and reframes) the primary open problem after the
finite-closed scope-theorem candidate was reviewed down from a universal no-go
(prior art all located: E1 Kadanoff, E2 crypto, E3 resource-theory-of-asymmetry,
framing constructor theory). The first **E2** computational-finality /
computational-arrow-of-time swing is recorded as T419 with a REDESIGN verdict, and
T420 now hardens the finite-cycle anti-relabel guard: the D2 question remains open
for a family-level period-hardness redesign/abandon decision
(`open-problems/computational-finality-arrow.md`). The **E3** GU adapter is held as
the cross-repo prize.
