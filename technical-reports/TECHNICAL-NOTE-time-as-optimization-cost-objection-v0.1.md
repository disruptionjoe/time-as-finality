# Technical Note: The "Time as Optimization Cost" Objection to Metabolic
Scaling Grounding

**Version**: v0.1
**Date**: 2026-06-22
**Status**: Technical note. No claim promotion. This note resolves a
specific internal tension raised by the five-run metabolic-issuance persona
panel (2026-06-22), Run 1 (Maya Osei) and echoed by Runs 3, 4, and 5.

## The Objection Stated

The metabolic scaling exploration proposes that the Moses framework (which
extends West-Brown-Enquist to show the 3/4 scaling law requires joint
energy-time optimization) supports TaF's claim that time is "co-equal" with
energy and therefore not merely a secondary coordinate. The five-run panel
found a structural objection:

> "If time is merely an optimization parameter that must be minimized
> alongside energy, it is precisely the kind of secondary/derived quantity
> TaF claims to oppose. The optimization constraint IS the energy-time
> tradeoff -- time enters as a cost, not as a constitutive ground."
> (Run 1, Maya Osei, Strongest Critique)

The objection is: "time as co-equal optimization cost" is not the same claim
as "time is constitutive of events being real." The Moses framework establishes
that minimizing only energy produces a different network architecture than
minimizing energy plus time. But minimizing time is precisely the stance that
treats time as something to be reduced -- the opposite of what TaF holds.

This note examines whether the objection is decisive and whether a modified
claim from the metabolic scaling grounding survives.

## Analysis

### What the Moses Framework Actually Shows

The Moses et al. (2008) extension of West-Brown-Enquist derives the 3/4 scaling
law by showing that biological transport networks are shaped by a joint
optimization:

```
minimize: E_total = E_metabolic + E_delay
subject to: delivery of ATP/O2 to all cells
where: E_delay is proportional to time * power, capturing the cost of delay
```

The result: optimal transport networks are those that balance energy-per-unit-
time (metabolic rate) against delay-per-unit-delivery (temporal delivery cost).
This gives the 3/4 exponent as the unique solution to the joint optimization.

The key claim in the metabolic scaling exploration is: this shows that "time
is co-equal with energy as an optimization axis." The objection is that this
makes time a cost variable, not a constitutive ground.

### Dissecting the Objection

The objection conflates two different framings:

**Framing 1 (target of the objection)**: "Time enters as a cost because we
want to minimize delay. Minimizing time means time is bad/costly -- it is a
secondary quantity to be reduced."

**Framing 2 (what Moses framework actually does)**: "Time constrains what is
physically achievable. Networks that ignore temporal delivery constraints are
physically nonoptimal not because delay is bad per se, but because temporal
delivery determines whether cells receive resources within the physical window
of biological demand. The optimization reflects a physical constraint, not
a preference against time."

The distinction matters. In Framing 1, time is a cost to minimize. In
Framing 2, time is a physical boundary condition that cannot be ignored --
it shapes the space of viable solutions.

The Moses framework supports Framing 2: the optimization does not say "minimize
time." It says "find networks that satisfy temporal delivery constraints." The
3/4 exponent is the structure of the constraint boundary, not the minimum of
a time-cost function.

### The Constitutivity Reading

TaF does not need time to be constitutive in a strong metaphysical sense --
it needs time to not be derivable from other physical quantities. The Moses
framework supports a weaker but still useful claim:

> "For hierarchically-branched transport systems, the temporal delivery
> structure (the pattern of when resources arrive, not just how much) is
> not derivable from the energy structure alone. The 3/4 exponent is the
> minimal signature of this irreducibility."

This is different from saying "time is fundamental" or "time is prior to
energy." It says: in a class of physical systems (hierarchical transport
networks), temporal structure contains information not already captured by
energetic structure. Specifically:

- Two networks can have identical total metabolic energy expenditure but
  different temporal delivery patterns (one is a bus route, one is a
  hierarchical tree).
- The bus route is energetically equivalent but temporally inferior: distant
  cells experience longer delays.
- The 3/4 exponent selects the hierarchically-branched network as optimal
  precisely because temporal delivery is not already encoded in total energy.

### The TaF-Compatible Claim

From the metabolic scaling grounding, the correct claim for TaF is:

> **Metabolic Temporal Irreducibility (candidate claim)**: In hierarchically-
> branched physical transport systems satisfying the West-Brown-Enquist-Moses
> constraints, the temporal delivery structure (characterized by the branching
> exponent beta and the cadence of resource arrival) contains information
> about source-event ordering that is not derivable from the energy expenditure
> structure alone. A system that records energy flux but not temporal flux
> cannot reconstruct the branching architecture, and therefore cannot certify
> source-event order at scale.

This claim does NOT say:
- Time is ontologically primary.
- Temporal cost minimization grounds time as constitutive.
- The Moses optimization "proves" time is real.

This claim DOES say:
- In a specific class of physical systems, temporal structure is not energy-
  reducible.
- This creates a class of source systems where mu_M (the branching-scaled
  measure) carries information not captured by entropy or energy alone.
- For TaF's source-object contract, this motivates the mu_M candidate as
  potentially nonabsorbed.

### The Residual Worry

Even with this reading, a concern remains: "temporal delivery constraints are
causal constraints expressed in time coordinates." In a causal-order framework,
"cell X must receive oxygen within T seconds" is a causal dependency (oxygen
arrival must precede cell activity) combined with a metric constraint (the
interval must be less than T). TaF needs to show that the metric constraint
cannot be dissolved into causal order alone.

This is the crux: is the 3/4 branching exponent a fact about causal structure
or about the metric structure of time?

**Partial answer**: The branching exponent arises from optimizing over networks
with a fixed spatial extent and a fixed metabolic demand. In a pure causal
framework without metric time, there is no notion of "delay" -- only
"happens before." The delay cost in the Moses framework requires a metric:
delay = distance / velocity, where velocity is a finite causal propagation
speed. This metric structure is precisely what a pure causal-order framework
lacks.

Therefore: the Moses framework implicitly requires a metric space, not just
a causal partial order. The 3/4 exponent encodes metric-temporal information
that is not captured by causal order alone. This is a meaningful claim for
the TaF source-object program.

## Verdict

**The "time as optimization cost" objection is partially valid but not decisive.**

Valid component: "time as co-equal optimization axis" does not directly support
"time is constitutive in TaF's sense." The Moses framework establishes that
temporal delivery constraints are physically irreducible from energetic
constraints -- not that time itself is ontologically constitutive.

Not decisive: The valid component does not close the metabolic scaling line.
Instead, it narrows the claim that metabolic scaling can support:

- **Closed**: "Time is co-equal with energy as an optimization axis" as a
  grounding for TaF's constitutivity claim.

- **Surviving**: "In hierarchically-branched transport systems, temporal
  delivery structure (captured by the branching exponent) is not reducible
  to energetic structure alone, constituting a class of source systems where
  mu_M carries non-energy-reducible information about source-event ordering."

The surviving claim is weaker than TaF's North Star but is not vacuous. It
motivates mu_M as a source measure that can distinguish systems that are
energetically identical but temporally different -- which is exactly the
discriminating datum needed for Cap_TI construction.

## Recommended Action

1. The metabolic scaling exploration file should be updated to remove the
   "time as co-equal" phrasing and replace it with the narrower claim:
   "temporal delivery structure is not energetically reducible in
   hierarchically-branched transport systems (Metabolic Temporal
   Irreducibility)."

2. This narrower claim becomes the physical motivation for mu_M as a source
   measure candidate -- not a claim that time is fundamental, but a claim
   that a specific class of physical systems encodes temporal-structural
   information not already in their energy ledger.

3. Cap_TI construction (see `open-problems/cap-ti-capability-object-spec.md`)
   should be grounded in Metabolic Temporal Irreducibility: the capability
   a Temporal Issuance system has is the ability to certify source-event
   order at scale using mu_M, precisely because mu_M encodes temporal-
   structural information that energy-only measures cannot provide.

4. This technical note should be referenced from the metabolic scaling
   exploration file as the official resolution of the "time as optimization
   cost" objection.

## What This Note Does Not Claim

- This note does not claim that the Moses framework proves TaF's North Star.
- This note does not upgrade H7.
- This note does not add Metabolic Temporal Irreducibility to CLAIM-LEDGER.md
  (a test would be needed first: specifically, whether the 3/4 exponent's
  metric-structure dependence survives the same-neighbor-data freeze with
  causal order matched but metric time varied).
- This note does not confirm that mu_M is a nonabsorbed source primitive.

## Relationship to TESTS.md

This technical note is a prerequisite input to T184 (mu_M non-additivity
composition gate). T184 must incorporate the metric-structure dependency
finding: the G-absorption check in T184 should specifically verify whether
the gluing data G encodes metric-temporal structure (not just causal-order
structure). If G is purely causal-order-indexed, mu_M's metric-temporal
content may survive G-absorption. If G encodes metric structure (distances,
durations), mu_M is more likely absorbed by G.
