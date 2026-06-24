# T186: Metric vs. Causal Order Beta Test

## Target Claims

- MTI (Metabolic Temporal Irreducibility claim: claims/MTI-metabolic-temporal-irreducibility.md)
- H7 (Temporal Issuance branch, via temporal-issuance-source-object-spec.md)
- Cap_TI Candidate C (reconciliation-bound prediction, open-problems/cap-ti-capability-object-spec.md)

## Origin

T184 (mu_M non-additivity composition gate) found that mu_M is G-absorbed for
abstract D1RestrictionSystems under resolved compositions, but may carry
temporal-metric information before G is updated (the architectural-change
transition window). T185 (lambda*(s) MSY absorption test) confirmed that the
issuance dynamics have PO1-grounded TaF-specific structure. The MTI claim
asserts that the branching exponent beta contains temporal-metric information
beyond causal order.

This test directly tests the MTI core assertion: can two D1RestrictionSystems
have identical causal order but different branching exponent beta, and if so,
does beta require metric temporal structure (not just causal order) to be
determined?

## Background

### The MTI Core Assertion

MTI claims:
> In hierarchically-branched physical transport systems satisfying the
> West-Brown-Enquist-Moses joint energy-time optimization constraints, the
> temporal delivery structure (characterized by the branching exponent beta)
> contains information about source-event ordering that is not derivable from
> the energy expenditure structure alone.

The West-Brown-Enquist-Moses derivation of the 3/4 exponent uses:
1. Hierarchical branching tree structure (topological constraint)
2. Energy conservation (energy constraint)
3. Minimization of delivery TIME (metric temporal constraint)

Claim (3) requires metric temporal structure — not just causal order. Causal
order tells you which event came before which, but not how long the gap was.
Metric time tells you how large the gaps were. The Moses derivation minimizes
total delivery time (not just causal chain length), so it requires a metric.

**The hypothesis tested here (H_beta)**: Two physical systems can have the same
causal order (same sequence of events, same before-after relations) but different
branching exponents, and the difference in beta is determined by the metric
temporal structure (delivery time distribution) rather than the causal structure.

### Known Caution from MTI

MTI Failure Mode 2 states: if beta is computable from causal-set data (ordering
fraction via Myrheim-Meyer), MTI is absorbed by the causal-set framework. This
test is designed to check whether that failure mode applies.

## Setup

### Two D1RestrictionSystems with Identical Causal Order, Different Delivery Time

Construct two source systems:

**System Alpha:**
- Source events: e1, e2, e3, e4, e5 (5 events)
- Causal order (partial): e1 < e2, e1 < e3, e2 < e5, e3 < e5, e4 incomparable to e1-e3
  (e4 is a separate branch that also precedes e5)
- Causal diagram: e1 -> {e2, e3} -> e5, and e4 -> e5 (two branches merging at e5)
- This is a 5-element poset with the partial order described above

**System Beta:**
- Source events: f1, f2, f3, f4, f5 (5 events)
- Causal order (partial): IDENTICAL to System Alpha (same Hasse diagram)
  f1 < f2, f1 < f3, f2 < f5, f3 < f5, f4 incomparable to f1-f3, f4 < f5
- Causal diagram: IDENTICAL

**Difference between Alpha and Beta:**
- System Alpha: delivery times are t(e1->e2) = 1, t(e1->e3) = 1, t(e4->e5) = 2
  (the e4 branch is slower to deliver to e5)
- System Beta: delivery times are t(f1->f2) = 1, t(f1->f3) = 1, t(f4->f5) = 0.5
  (the f4 branch is faster to deliver to f5)

**Note**: The CAUSAL ORDER is identical (same partial order). The DELIVERY TIMES differ.

### Expected Behavior Under Moses Optimization

The Moses framework optimizes the branching exponent to minimize total delivery
time while conserving energy. For System Alpha (slow secondary branch), the
optimization favors a resource-conserving strategy that routes less through the
slow branch — lower effective branching efficiency, lower beta. For System Beta
(fast secondary branch), the optimization can exploit the fast secondary route —
higher branching efficiency, higher beta.

**Formal prediction**:
- beta(Alpha) < beta(Beta) even though causal_order(Alpha) = causal_order(Beta)

### The Causal-Set Absorption Check

The causal-set framework uses the Myrheim-Meyer ordering fraction:
```
f(P) = number_of_comparable_pairs / number_of_pairs
```
For both Alpha and Beta with the same causal order:
```
Comparable pairs: (e1,e2), (e1,e3), (e1,e5), (e2,e5), (e3,e5), (e4,e5) = 6 pairs
Total pairs: C(5,2) = 10
f(Alpha) = f(Beta) = 6/10 = 0.6
```

**The Myrheim-Meyer ordering fraction is IDENTICAL for Alpha and Beta** because
they have the same causal order.

If beta is derivable from causal-set data (including ordering fraction), then
beta(Alpha) should equal beta(Beta). If beta(Alpha) ≠ beta(Beta) (as predicted
by Moses optimization), then beta contains information not in the causal-set.

**This is the decisive test for MTI vs. causal-set absorption.**

## Test Protocol

### Step 1: Enumerate Causal Order Data

For both systems, compute all causal-set-theoretic quantities:
- Hasse diagram: identical (by construction)
- Ordering fraction f(P): identical (0.6)
- Interval sizes |I(x,y)| for all pairs (x,y): identical
- Myrheim-Meyer dimension estimate d_MM: identical (same ordering fraction)
- T167-style ordinal scaling: identical (same labeled poset)

If any causal-set quantity distinguishes Alpha from Beta, the test is invalid
(we did not match causal-set data correctly).

### Step 2: Compute Entropy Production

For both systems, compute entropy production along each causal chain:
- Assume uniform state transition probability at each event
- S(e) = sum over events of log(state_options) = same for both (by assumption of
  identical event types)

Entropy production: IDENTICAL (by construction — all we changed is delivery time)

### Step 3: Compute Beta via Moses Optimization

Apply the West-Brown-Enquist-Moses joint energy-time optimization:
- Total delivery time minimized subject to energy constraints
- The branching exponent beta emerges from the optimization

For System Alpha (slow secondary branch, t(e4->e5) = 2):
The optimization will assign less "weight" to the slow e4->e5 branch, reducing
the effective exponent:
```
beta(Alpha) ≈ 3/4 * (1 - correction for slow branch)
             = 0.75 * (1 - delta_alpha)  where delta_alpha > 0
```

For System Beta (fast secondary branch, t(f4->f5) = 0.5):
The optimization will increase the weight on the fast branch:
```
beta(Beta) ≈ 3/4 * (1 + correction for fast branch)
            = 0.75 * (1 + delta_beta)  where delta_beta > 0
```

**Predicted outcome**: beta(Alpha) < 0.75 < beta(Beta).

The exact values require the Moses calculation (minimizing sum of delivery times
over all leaf nodes subject to hierarchical branching constraints). For this
finite 5-node system, the calculation is tractable.

### Moses Calculation (5-Node System)

For a tree with root e1, two middle nodes e2/e3, and a separate root e4, all
converging at e5:

Let total delivery time T = sum over all leaf-to-root paths of (time * flow weight).

System Alpha:
- Path e1->e2->e5: time = 2, weight = w12
- Path e1->e3->e5: time = 2, weight = w13
- Path e4->e5: time = 2, weight = w4
- Optimization: minimize T = 2*w12 + 2*w13 + 2*w4 subject to sum_weights = 1
- Solution: all weights equal (no efficiency gradient). beta_Alpha = 3/4

Wait — in this parameterization all paths have equal time, so no asymmetry.
Let me use the intended asymmetry:

System Alpha: t(e1->e2) = 1, t(e2->e5) = 1, t(e1->e3) = 1, t(e3->e5) = 1, t(e4->e5) = 2
System Beta:  t(f1->f2) = 1, t(f2->f5) = 1, t(f1->f3) = 1, t(f3->f5) = 1, t(f4->f5) = 0.5

Path lengths:
- Alpha path 1 (e1->e2->e5): total = 2
- Alpha path 2 (e1->e3->e5): total = 2
- Alpha path 3 (e4->e5): total = 2
- All paths equal! No asymmetry in Alpha (if all e1 paths are 1+1=2 = 2).

**Revised setup with clearer asymmetry:**

System Alpha:
- 5 events: root->a, root->b, a->leaf, b->leaf, separate->leaf
- Path lengths: root-a = 3, root-b = 1, a-leaf = 1, b-leaf = 1, separate-leaf = 1
- Path root->a->leaf: time = 4
- Path root->b->leaf: time = 2
- Path separate->leaf: time = 1

Moses optimization for Alpha: assign higher flow to lower-time paths.
Effective beta depends on average transport efficiency. Higher time variance -> lower beta.

System Beta (same causal order, compressed timing):
- Same causal structure, but path root->a is shortened to 2 instead of 3
- Path root->a->leaf: time = 3
- Path root->b->leaf: time = 2
- Path separate->leaf: time = 1

Beta comparison: Beta (System Beta) > Beta (System Alpha) because delivery time
variance is lower in System Beta (paths are more equal in time = more efficient
branching network overall).

**Formal approximation:**

Let T_i be the delivery time for path i, w_i the flow weight.
Effective branching exponent beta ∝ 1 - Var(T_i) / E(T_i)^2

System Alpha: T = {4, 2, 1}, E(T) = 7/3 = 2.33, Var(T) = (4-2.33)^2/3 + (2-2.33)^2/3 + (1-2.33)^2/3
= 2.79/3 + 0.11/3 + 1.77/3 = (2.79+0.11+1.77)/3 = 4.67/3 = 1.56
CV(T)_Alpha = sqrt(1.56)/2.33 = 1.25/2.33 = 0.54

System Beta: T = {3, 2, 1}, E(T) = 6/3 = 2.00, Var(T) = (3-2)^2/3 + (2-2)^2/3 + (1-2)^2/3
= 1/3 + 0 + 1/3 = 2/3 = 0.67
CV(T)_Beta = sqrt(0.67)/2.00 = 0.82/2.00 = 0.41

**Beta(Alpha) ∝ 1 - 0.54 = 0.46 vs Beta(Beta) ∝ 1 - 0.41 = 0.59**

Normalizing to the 3/4 biological calibration:
- beta(Alpha) ≈ 0.75 * (0.46/0.59) = 0.59
- beta(Beta) ≈ 0.75 * (0.59/0.59) = 0.75

**Prediction: beta(Alpha) = 0.59, beta(Beta) = 0.75 for two systems with IDENTICAL CAUSAL ORDER.**

The causal order (which e comes before which) is identical. The delivery times are not.
This is the metric temporal structure that MSY requires but causal order does not provide.

## Success Criteria

**Primary success**: Find two D1RestrictionSystems with:
1. Identical causal order (same Hasse diagram)
2. Same Myrheim-Meyer ordering fraction
3. Same entropy production
4. Different branching exponent beta (as determined by Moses delivery-time optimization)

AND verify that:
- No causal-set quantity distinguishes the two systems (they are identical to causal-set theory)
- The beta difference IS determined by delivery-time distribution (metric temporal structure)

**This constitutes positive evidence for MTI**: temporal metric structure (delivery
times) carries information that causal order does not.

## Failure Criteria

**Primary failure**: The beta difference between Alpha and Beta is computable
from the causal-set data (ordering fraction, interval sizes, dimension estimate)
after matching. If a causal-set quantity distinguishes the two systems (beyond
the deliberately-varied delivery time), the test setup has a flaw.

**Secondary failure**: The Moses delivery-time optimization does not distinguish
Alpha from Beta because the metric temporal structure washes out into the same
effective beta. This would happen if beta is determined by topological properties
of the tree (branching depth, number of levels) rather than by the delivery-time
distribution. If so, beta is G-absorbed (topology is in G).

**Tertiary failure**: The Moses framework does not apply to abstract
D1RestrictionSystems (only to biological organisms), in which case T186 is
testing a claim in a domain where MTI was never meant to apply.

## Relationship to Known Tests

- **T184** (mu_M non-additivity): found G-absorption under resolved compositions,
  but identified the architectural-change transition window as the candidate
  non-absorbed window. T186 tests whether beta is metric-temporal in that window.

- **T185** (lambda*(s) MSY absorption): found non-absorption with C(lambda) as
  the PO1-grounded residue. T186 is the prerequisite for knowing whether beta
  in mu_M (the input to the N-C-K model) carries information beyond causal order.

- **Cap_TI Candidate C**: the positive-control fixture (reconciliation-bound
  prediction) advances to step 4 only if T186 confirms that beta differs for
  same-causal-order systems. T186 is the critical gate.

- **S1 (spacetime as finality colimit)**: T186 is relevant to S1 because the
  causal-set program's use of Myrheim-Meyer ordering fractions assumes that
  metric information is recoverable from causal structure alone (sprinkling).
  If T186 shows that beta cannot be recovered from causal-set data, it strengthens
  the argument that TaF adds metric temporal structure beyond causal sets.

## Contribution Needed

1. Implement the two-system fixture (Alpha and Beta) in Python, computing:
   - Causal order (Hasse diagram, ordering fraction)
   - Entropy production (uniform state transitions)
   - Delivery times (assigned as described above)
   - Beta via Moses delivery-time optimization (minimize sum of delivery times
     subject to branching constraints)

2. Verify that causal-set quantities are identical between Alpha and Beta
   (Myrheim-Meyer ordering fraction, interval sizes, dimension estimate).

3. Verify that beta(Alpha) ≠ beta(Beta) despite identical causal order.

4. If the verification passes: this is positive evidence for MTI. Update
   MTI claim status from OPEN to PARTIALLY_SUPPORTED.

5. Run the causal-set absorption check: can any causal-set quantity (beyond
   the intentionally varied delivery time) distinguish Alpha from Beta? If yes,
   the fixture has a flaw.

6. If all checks pass: proceed to Cap_TI Candidate C step 4 (hostile same-
   neighbor-data split in physical substrate context). The T186 fixture IS
   the physical substrate context needed for the hostile split.

## Expected Outcome

Based on the T184 and T185 findings, the expected outcome is:
- **Positive**: beta(Alpha) < beta(Beta) for identical causal order
- **Causal-set quantities**: identical between Alpha and Beta (no causal-set absorption)
- **MTI update**: PARTIALLY_SUPPORTED, with the Moses delivery-time calculation
  as the first physical substrate fixture

The expected outcome is conditional on the Moses calculation correctly
distinguishing delivery-time distributions with identical causal structure.
If the Moses calculation collapses Alpha and Beta to the same beta (because
the delivery-time distribution is not a free parameter of the hierarchical
branching model), the expected outcome fails and MTI is demoted.

## Registered Status

This test is REGISTERED as of 2026-06-22. It is NOT yet run.
Implementation should be added to: models/run_t186.py
Results should be written to: results/T186-metric-vs-causal-order-beta-v0.1-results.md

TESTS.md entry should be added:
| [T186](tests/T186-metric-vs-causal-order-beta-test.md) | Metric vs. causal order beta test | MTI, H7, Cap_TI | open: tests whether branching exponent beta requires temporal-metric structure beyond causal order; implements two 5-event systems with identical causal order and different delivery times |
