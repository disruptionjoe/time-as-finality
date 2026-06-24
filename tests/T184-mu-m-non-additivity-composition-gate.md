# T184: mu_M Non-Additivity Composition Gate

## Target Claims

- H7 (Temporal Issuance branch, via `temporal-issuance-source-object-spec.md`)
- `mu` field in `Y_TI` source object
- `open-problems/cap-ti-capability-object-spec.md` (Candidate A/B/C precondition)

## Background

The five-run metabolic-issuance persona panel (2026-06-22) identified a
specific underspecification in the mu_M non-additivity claim: the composition
operation for realizations is not declared. "Subadditivity" is a formal
property only relative to a named operation. Two natural operations exist:

- **Set-union composition**: r1 union r2 — the joint realization of two
  independent source subsystems. Non-additivity under union means
  mu_M(r1 union r2) < mu_M(r1) + mu_M(r2).

- **Sequential-extension composition**: r1 then r2 — the realization r2
  follows and extends r1 in time (r2 is a later stage of the same system).
  Non-additivity under sequential extension means
  mu_M(r1 followed by r2) vs mu_M(r1) + mu_M(r2).

These are formally distinct because:
- Under union, subadditivity reflects efficiency gains from combining
  independent hierarchical systems (different organisms sharing a network).
- Under sequential extension, subadditivity would mean later-stage
  additions to the same system contribute less than earlier-stage additions
  of equal size — a saturation effect.

The metabolic scaling claim (West-Brown-Enquist-Moses framework) predicts
subadditivity under union by the 3/4 exponent: a combined system of size
|r1| + |r2| has lower metabolic rate per unit than two separate systems.
Whether sequential-extension also produces subadditivity is a separate
empirical and formal question.

## Setup

### Formal Objects

Let R be a set of source realizations. Each realization r in R is described
by:
- |r|: size (number of source events or nodes)
- beta(r): branching exponent of the hierarchical transport network (
  0 < beta <= 1; metabolic scaling gives beta = 3/4 for biological systems)
- topology(r): the specific branching tree structure

The candidate source measure is:
```
mu_M(r) = c * |r|^beta(r)
```
where c is a substrate-specific constant.

### Two Composition Operations to Test

**Test A: Union Composition**

Given two independent realizations r1, r2 with |r1| = n1, |r2| = n2,
and the same branching exponent beta:

- Combined system: r_union = r1 union r2, with |r_union| = n1 + n2
- Claim: mu_M(r_union) < mu_M(r1) + mu_M(r2)
- Formal: c*(n1+n2)^beta < c*n1^beta + c*n2^beta

This is equivalent to: (n1+n2)^beta < n1^beta + n2^beta for 0 < beta < 1.

This is a standard result: for 0 < beta < 1, f(x) = x^beta is strictly
concave, so (n1+n2)^beta < n1^beta + n2^beta for all n1, n2 > 0 by the
strict concavity inequality.

**Test B: Sequential Extension Composition**

Given a base realization r1 and an extension r2 that adds new nodes to r1
(r2 is a growth increment on the same system):

- Extended system: r_seq = r1 extended by r2, with |r_seq| = n1 + n2
- The branching exponent of r_seq equals the branching exponent of r1 plus
  correction delta(r1, r2) accounting for how r2 integrates with r1's
  existing hierarchy.
- Claim: Whether mu_M(r_seq) < mu_M(r1) + mu_M(r2) depends on how delta
  behaves during sequential extension.

Three subcases:
1. If r2 integrates at the periphery (leaves of the hierarchy):
   - r2's nodes become new leaves; branching structure of r1 is unchanged
   - mu_M(r_seq) ≈ c*(n1+n2)^beta (same exponent as r1)
   - Since (n1+n2)^beta < n1^beta + n2^beta by concavity, subadditivity holds
2. If r2 integrates at an intermediate branch point:
   - A new intermediate level is added; branching exponent may increase
   - mu_M(r_seq) could be > mu_M(r1) + mu_M(r2) if the new architecture
     is more efficient (higher exponent achieves same metabolism at larger
     effective size)
3. If r2 replaces a branch (internal reorganization):
   - This is not extension but substitution; composition undefined in this test

Subcase 2 is the critical case: sequential extension that creates a new
intermediate level can make mu_M superadditive under sequential extension
even while union composition is subadditive. These are formally distinct
non-additivity claims.

### Absorber Comparison Objects

For each composition test, the following comparison measures must be computed
and matched:
- Entropy: S(r) = sum of log(1/p_i) for micro-states (Shannon entropy)
- Event count: N(r) = |r| (counting measure)
- Volume: Vol(r) = |r| (in finite case, same as count)
- Information: I(r) = information content of record, context-dependent

The mu_M test requires that mu_M(r1 op r2) vs mu_M(r1) + mu_M(r2) gives a
different verdict from S(r1 op r2) vs S(r1) + S(r2) when the absorbers
are matched.

For entropy: if local entropy is extensive (additive), S(r1 union r2) =
S(r1) + S(r2) when r1, r2 are independent. Then mu_M is subadditive under
union while entropy is additive -- a genuine difference. This is the
discriminating comparison.

For sequential extension: if S(r_seq) = S(r1) + S(r2) + delta_S where
delta_S >= 0 is the entropy of the new constraints, then mu_M's subadditivity
under peripheral-extension (Subcase 1) matches entropy's additivity at the
same comparison. But if Subcase 2 applies (new intermediate level), mu_M may
be superadditive while entropy is still additive -- a different and important
divergence.

## Success Criteria

**For Test A (Union)**:
- Formal proof that mu_M(r1 union r2) < mu_M(r1) + mu_M(r2) for all
  n1, n2 > 0 and 0 < beta < 1. (This follows from strict concavity --
  a known result. The contribution is naming it explicitly for Y_TI.)
- Verification that the corresponding entropy comparison is additive, not
  subadditive: S(r1 union r2) = S(r1) + S(r2) for independent r1, r2.
- Conclusion: mu_M and entropy have different additivity properties under
  union -- mu_M is not absorbed by entropy with respect to this composition.

**For Test B (Sequential Extension, Subcase 1 -- peripheral)**:
- Numerical check: mu_M(r_seq) < mu_M(r1) + mu_M(r2) for n1 = n2 = 10,
  beta = 3/4, peripheral extension.
- Comparison: S(r_seq) ≈ S(r1) + S(r2) + delta_S (small positive term).
- Both are subadditive or nearly-additive; distinction is smaller in this
  subcase. Result: Test B Subcase 1 is less discriminating.

**For Test B (Sequential Extension, Subcase 2 -- new intermediate level)**:
- Numerical check: mu_M(r_seq) > mu_M(r1) + mu_M(r2) for n1 = n2 = 10,
  beta_r1 = 3/4, and beta_r_seq = 4/5 (new level improves exponent).
- Comparison: S(r_seq) = S(r1) + S(r2) + delta_S (still additive with
  small positive correction).
- mu_M is superadditive while entropy is (nearly) additive: this is the
  sharpest case. It shows that not all sequential extensions of hierarchical
  systems are subadditive in mu_M -- only the architecturally-efficient ones.
- Conclusion: Sequential-extension non-additivity depends on whether the
  extension adds or reorganizes hierarchy levels, which entropy does not
  capture. This is a genuine discriminating datum for the branching-exponent
  interpretation of mu_M.

## Failure Criteria

**Primary failure**: Either composition test shows that mu_M(r1 op r2) vs
mu_M(r1) + mu_M(r2) is reproduced exactly by a corresponding comparison on
entropy or event count under the same composition. If this holds for both
compositions, mu_M's non-additivity is absorbed by existing measures.

**Secondary failure**: The branching exponent beta is not operationally
definable without reference to the absorber vector (e.g., if beta must be
computed from the entropy production profile of the system, then mu_M is a
function of entropy and is absorbed).

**Tertiary failure**: Test B Subcase 2 (superadditivity under new-level
extension) cannot be reproduced in any concrete finite model because real
hierarchical systems do not actually change their branching exponent during
growth. If the exponent is fixed at 3/4 always, Subcase 2 is empty and the
discriminating case disappears.

## Known Physics Constraints

1. The West-Brown-Enquist-Moses 3/4 exponent applies to biological metabolic
   scaling at the organismal level. Its applicability to arbitrary finite
   D1RestrictionSystems requires justification that is not yet provided.

2. The branching exponent in general need not be 3/4. The test should work
   for any beta in (0, 1) exclusive. The biological value 3/4 is a
   calibration point, not a universal law.

3. The union composition test assumes r1 and r2 are "independent" in the
   sense that their branching hierarchies do not interact. For source systems
   that share environment or substrate, the joint system may have a different
   effective exponent, which would complicate the absorber comparison.

4. Shannon entropy is strictly additive only for independent (product-
   measure) systems. If r1 and r2 have correlated micro-states, S(r1 union
   r2) < S(r1) + S(r2) by subadditivity of entropy for correlated systems.
   In that case, the entropy comparison also shows subadditivity, and the
   contrast with mu_M is weakened.

   Constraint: Test A must be run on independent (uncorrelated) r1, r2.
   For correlated systems, a different absorber comparison must be used
   (mutual information, conditional entropy).

## G-Absorption Check (Required Before Claiming Mu_M Independence)

The metabolic scaling exploration identifies a potential absorption of mu_M by
the gluing data G: if the branching topology is fully encoded in G, then
mu_M is a function of G and is absorbed by TaF's own existing formalism.

This test must include an explicit G-absorption check:

1. Construct a D1RestrictionSystem where G encodes the full branching tree
   (identity, overlap, and gluing data include the parent-child relationships
   of the hierarchy).
2. Ask: is mu_M(r) = c*|r|^beta(r) computable from G alone?
3. If yes: mu_M is absorbed by G. The non-additivity under union is then
   a property of G, not an independent mu primitive.
4. If no: what additional data about r is needed beyond G? That additional
   data is the candidate for a genuinely nonabsorbed component of mu_M.

## Relationship to Cap_TI

This test is a necessary precondition for Cap_TI construction, not itself
a Cap_TI candidate. The test determines:

1. Which composition operations make mu_M non-additive in ways entropy is not.
2. Whether that non-additivity is absorbed by G or genuinely independent.

After T184 runs, the non-absorber-absorbed composition rule (if any) becomes
the mu specification input for one of the Cap_TI candidates in
`open-problems/cap-ti-capability-object-spec.md`.

Without a specified composition operation, Cap_TI Candidate A (scale-sensitive
source-order certification) cannot be defined, because it requires a
comparison between mu_M values for combined systems.

## Contribution Needed

1. A formal proof or numerical verification that Test A (union) shows the
   claimed subadditivity, with explicit check that entropy is additive in
   the same fixture.

2. A numerical fixture implementing Test B Subcases 1 and 2, with:
   - n1 = n2 = 10, beta = 3/4 for Subcase 1 (peripheral extension)
   - n1 = 10, n2 = 5, beta_r1 = 3/4, beta_r_seq = 4/5 for Subcase 2
     (new intermediate level)
   - Entropy and mu_M computed for both base and extended systems
   - Result table showing which subcases are discriminating

3. The G-absorption check: explicit test of whether a D1RestrictionSystem
   with G encoding the full branching tree makes mu_M computable from G.

4. A one-sentence verdict: "mu_M is / is not absorbed by G under Test A and
   Test B Subcase [X]; the discriminating composition operation is [X]
   or [no composition operation survives]."

## Non-null Outcome Conditions

If T184 finds a composition operation where mu_M is non-additive while all
absorbers are additive, AND the G-absorption check fails (mu_M requires
data beyond G), then:

- The specific composition operation and subadditivity direction become the
  typed composition rule for mu_M in Y_TI.
- The non-absorbed component of mu_M becomes a candidate input for Cap_TI
  construction.
- T184 is a prerequisite input to the first hostile same-neighbor-data split.

If T184 finds no such composition operation or G absorbs all cases:

- mu_M closes as a mu candidate.
- The Temporal Issuance metabolic scaling line closes as translation residue
  unless a new mu candidate is proposed.
- Record the demotion in CLAIM-LEDGER.md under H7 status notes.
