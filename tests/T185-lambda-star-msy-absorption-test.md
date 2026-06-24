# T185: lambda*(s) Maximum Sustainable Yield Absorption Test

## Target Claims

- H7 (Temporal Issuance branch, via `temporal-issuance-source-object-spec.md`)
- `lambda*(s)` as proposed dynamics for Ext_S
- Optimal Issuance Rate Curve Hypothesis
  (`explorations/explorer-optimal-issuance-rate-curve-2026-06-22.md`)

## Background

The five-run metabolic-issuance persona panel (2026-06-22), Run 4 (Resource
Theorist), identified a serious absorption risk for lambda*(s): the optimal
issuance rate functional N(lambda, S) - C(lambda, S) - K(lambda, S) maps
structurally onto the Maximum Sustainable Yield (MSY) functional from
classical renewable resource theory.

The MSY framework applies when:
1. A resource stock S has a natural growth rate r (intrinsic growth)
2. Harvesting occurs at rate H (the control variable)
3. Collapse risk K increases with over-harvesting
4. The goal is to find the harvest rate that maximizes long-term yield

The logistic MSY formula: lambda*(s) = r*K_cap/4 where K_cap is the carrying
capacity of the resource, r is the intrinsic growth rate, and the optimal
harvest is at half the carrying capacity.

If N-C-K maps cleanly onto the MSY functional, then lambda*(s) is not a
TaF-specific result -- it is classical renewable resource management, and the
Optimal Issuance Rate Curve Hypothesis is absorbed.

This test executes that mapping explicitly and checks whether the match is
exact, partial, or absent. A partial match with identifiable residue would
constitute the most useful outcome: it would specify exactly what TaF-specific
structure lambda*(s) adds to the standard MSY result.

## Setup

### The MSY Framework (Standard Form)

Let S be the resource stock and H = lambda * S be the harvesting rate
(proportional harvesting). The logistic growth model is:

```
dS/dt = r*S*(1 - S/K_cap) - H
dS/dt = r*S*(1 - S/K_cap) - lambda*S
```

At steady state (dS/dt = 0), the equilibrium stock is:

```
S*(lambda) = K_cap * (1 - lambda/r)
```

The sustainable yield at equilibrium is:

```
Y(lambda) = lambda * S*(lambda) = lambda * K_cap * (1 - lambda/r)
```

This is maximized at lambda_MSY = r/2, giving S*_MSY = K_cap/2 and
Y_MSY = r*K_cap/4.

The MSY result is: lambda*(s) = r/2, independent of the current stock S
(for the logistic model with proportional harvesting).

### The Issuance Rate Framework (Proposed Form)

The optimal issuance rate explorer proposes:

```
dS/dt = N(lambda) - C(lambda) - K(lambda, S)
```

where:
- N(lambda) = a*lambda: novelty/new coherent structure (linear in lambda)
- C(lambda) = b*lambda^2: coherence cost (quadratic in lambda)  
- K(lambda, S) = collapse risk (state-dependent, grows with lambda and S)

The proposed optimum:
```
lambda*(s) = argmax_lambda [N(lambda) - C(lambda) - K(lambda, S)]
           = argmax_lambda [a*lambda - b*lambda^2 - K(lambda, S)]
```

In the static case (K independent of S):
```
d/d(lambda)[a*lambda - b*lambda^2 - K] = 0
=> a - 2b*lambda - dK/d(lambda) = 0
=> lambda* = (a - dK/d(lambda)) / (2b)
```

For K = k*lambda (linear collapse risk):
```
lambda*(static) = (a - k) / (2b)
```

### Mapping Test

To test MSY absorption, we must map the issuance-rate framework to the MSY
framework variable by variable.

**Candidate mapping:**

| Issuance framework | MSY framework | Match quality |
|---|---|---|
| S (coherent structure stock) | S (resource stock) | Direct |
| N(lambda) = a*lambda | Inflow = r*S*(1 - S/K) | Partial: MSY inflow is stock-dependent; N is stock-independent |
| C(lambda) = b*lambda^2 | No direct analog | MSY has no quadratic harvest cost |
| K(lambda, S) | H = lambda*S (harvest rate) | Partial: K is a risk/cost; H is a rate |
| lambda*(s) | lambda_MSY = r/2 | If mapping is clean, should coincide |

**Key divergences identified before numerical test:**

1. **Stock-dependence of inflow**: MSY's growth term r*S*(1 - S/K_cap) is
   proportional to S. The issuance framework's novelty term N(lambda) = a*lambda
   is proportional to lambda but not to S. This means issuance novelty does
   not saturate with stock -- it saturates with lambda only. This is a
   structural difference: in MSY, a large stock grows fast (up to K_cap/2);
   in the issuance model, growth is determined by the issuance rate regardless
   of existing stock.

2. **Quadratic cost**: MSY has no C(lambda) = b*lambda^2 analog. In standard
   MSY, harvesting cost is linear in harvest rate. The quadratic coherence cost
   represents a TaF-specific claim: each additional unit of issuance rate has
   increasing marginal coherence cost. This is not an MSY assumption.

3. **Collapse risk as externality vs harvest**: In MSY, "collapse risk" is
   implicitly the harvest-exceeds-growth condition (lambda > r), which drives
   S to zero. In the issuance model, K is a separate term that represents
   coherence collapse independent of stock depletion. These are conceptually
   different mechanisms.

### Numerical Comparison

For a concrete comparison, take:
- N(lambda) = a*lambda, a = 2
- C(lambda) = b*lambda^2, b = 0.5
- K(lambda, S) = k*S*lambda, k = 0.1 (state-dependent, bilinear)
- S = 5 (current stock)

Issuance optimum (static with state-dependent K at S=5):

```
d/d(lambda)[2*lambda - 0.5*lambda^2 - 0.1*5*lambda] = 0
d/d(lambda)[2*lambda - 0.5*lambda^2 - 0.5*lambda] = 0
d/d(lambda)[1.5*lambda - 0.5*lambda^2] = 0
1.5 - lambda = 0
lambda*(S=5) = 1.5
```

MSY optimum for the corresponding logistic system with K_cap = 10, r = 2:

```
lambda_MSY = r/2 = 1.0
S*_MSY = K_cap/2 = 5
```

The numerical values differ: lambda*(S=5) = 1.5 vs lambda_MSY = 1.0 for
comparable parameter choices. The discrepancy of 0.5 units is attributable
to the quadratic coherence cost C(lambda) = b*lambda^2, which has no MSY
analog. Without C, the issuance framework gives:

```
d/d(lambda)[2*lambda - 0.5*lambda] = 1.5 ≠ 0
```

No interior optimum (the objective is monotone increasing without C). This
confirms that the quadratic coherence cost is the mechanism generating the
interior optimum -- not the MSY growth/harvest balance.

### The Discrimination Finding

The MSY interior optimum arises from the balance between growth (concave in S)
and proportional harvesting. The issuance-rate interior optimum arises from
the balance between linear novelty gain and quadratic coherence cost. These
are different mechanisms:

- **MSY mechanism**: S-concavity of logistic growth creates a peak in
  dS/dt * lambda as a function of lambda (the yield curve peaks at r/2).
- **Issuance mechanism**: C(lambda) = b*lambda^2 creates a concave net-gain
  functional that peaks at (a - dK/d(lambda)) / (2b).

The issuance rate framework has a residue over MSY: the quadratic coherence
cost term C(lambda) = b*lambda^2. This term represents the claim that
coherence cost grows superlinearly in issuance rate -- an assertion about
the structure of coherent-extension formation that has no analog in resource
dynamics.

## Success Criteria

**Partial absorption confirmed**: The issuance-rate framework partially maps
onto MSY (stock dynamics, growth/depletion structure, interior optimum
existence), but has identifiable residue:

1. The N(lambda) term (stock-independent novelty) differs from MSY's S-dependent
   growth. This is a structural divergence.
2. The C(lambda) = b*lambda^2 term has no MSY analog. It is the mechanism
   generating the interior optimum in the issuance model; removing it makes the
   optimum disappear or become a boundary solution.
3. K(lambda, S) as collapse risk differs from MSY's implicit collapse at lambda > r.

**Identification of TaF-specific structure**: After the MSY mapping, the
surviving TaF-specific claims are:
- Quadratic coherence cost (C(lambda) = b*lambda^2)
- Stock-independent novelty (N(lambda) not proportional to S)
- Separately typed collapse risk (K not identified with harvest-equals-growth)

These three claims constitute the minimal TaF-specific content of lambda*(s)
that is not explained by classical MSY.

## Failure Criteria

**Complete absorption**: If a reparameterization exists that maps N-C-K exactly
onto an MSY functional for some K_cap, r, and harvesting rule, then lambda*(s)
IS an MSY optimum and the Optimal Issuance Rate Curve Hypothesis is absorbed
by classical renewable resource theory. In this case:

- lambda*(s) remains a useful dynamics equation for Ext_S but does not
  constitute a TaF-specific formal result.
- It should be registered as an MSY analog, not a new claim.
- The Optimal Issuance Rate Curve Hypothesis is demoted from hypothesis
  candidate to illustration of a known MSY result.

**Known conditions for complete absorption**:
- If C(lambda) = 0 (no coherence cost) AND N(lambda, S) = r*S*(1 - S/K_cap)
  (logistic growth), the framework is exactly MSY.
- No parameter choice with C ≠ 0 and stock-independent N produces exact MSY
  absorption.

## Known Physics Constraints

1. The MSY framework applies to renewable resources with logistic dynamics.
   Coherent structure in Ext_S is not a renewable resource in the biological
   sense; the analogy must be justified.

2. The bifurcation finding from Run 2 (Elena Voss) applies here: the interior
   optimum may be a saddle rather than a stable attractor. MSY assumes the
   logistic model has a unique stable equilibrium. If the issuance dynamics
   have a pitchfork bifurcation (two stable fixed points separated by a saddle),
   the MSY framework applies only in the region below the bifurcation point.

3. The quadratic cost C(lambda) = b*lambda^2 is an assumption, not derived from
   TaF formalism. Before treating it as TaF-specific, it must be grounded in
   the D1RestrictionSystem semantics. If C(lambda) is a modeling convenience
   (chosen to guarantee an interior optimum), it is not a TaF claim.

## Verdict Table

| Issuance term | MSY analog | Absorbed? | Residue (if not absorbed) |
|---|---|---|---|
| S (stock) | S (resource stock) | Yes | None |
| N(lambda) = a*lambda | r*S*(1-S/K) | Partial | Stock-independence of N |
| C(lambda) = b*lambda^2 | None | No | Quadratic coherence cost |
| K(lambda, S) | Harvest-equals-growth boundary | Partial | Separately typed collapse mechanism |
| lambda*(s) as interior optimum | lambda_MSY = r/2 | Partial | Different mechanism (C, not S-concavity) |

**Summary verdict**: lambda*(s) is NOT fully absorbed by MSY. The partial
absorption is confirmed: MSY owns the stock-dynamics structure and interior
optimum existence (under logistic growth). The quadratic coherence cost is
the discriminating TaF-specific term. However, this term is an assumption
that must be grounded in D1RestrictionSystem semantics before it constitutes
a genuinely independent contribution.

## Next Steps After T185

1. If partial absorption is confirmed (as this test finds): ground C(lambda) in
   D1RestrictionSystem semantics. Ask: does the category of coherent sections
   (Run 3, Category Theorist) predict that the rate of new obstructions grows
   quadratically in the issuance rate? If yes, C(lambda) = b*lambda^2 is a
   consequence of the coherent section functor, not an assumption.

2. Run the bifurcation analysis (Run 2, Elena Voss recommendation): determine
   whether the lambda*(s) interior optimum is a stable attractor or a saddle.
   This determines whether lambda*(s) is a dynamically achievable operating
   point or a theoretical optimum that the system overshoots.

3. If C(lambda) is grounded in PO1 obstruction dynamics: the quadratic cost
   arises because each additional unit of issuance rate creates an independent
   probability p of a new gluing obstruction, and K = p * lambda * S grows
   bilinearly. The net effect after the quadratic cost term gives a
   PO1-motivated interior optimum that is genuinely distinct from MSY.

## Contribution Needed

1. Numerical implementation of the N-C-K dynamical system with logistic MSY
   comparison, confirming the partial absorption finding in this file.

2. An explicit reparameterization check: can any substitution R_TI -> R_MSY
   map N-C-K to the standard MSY functional? If such a substitution exists,
   specify it; if not, prove impossibility via the stock-independence of N.

3. Semantic grounding for C(lambda): derive the quadratic coherence cost from
   PO1 obstruction dynamics or declare it an ungrounded assumption.

4. A one-paragraph update to the Optimal Issuance Rate Curve exploration file
   (`explorations/explorer-optimal-issuance-rate-curve-2026-06-22.md`) noting
   the MSY comparison result and identifying the discriminating residue.
