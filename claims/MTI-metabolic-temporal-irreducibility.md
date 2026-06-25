# MTI: Metabolic Temporal Irreducibility

## Claim

In hierarchically-branched physical transport systems satisfying the
West-Brown-Enquist-Moses joint energy-time optimization constraints, the
temporal delivery structure (characterized by the branching exponent beta)
contains information about source-event ordering that is not derivable from
the energy expenditure structure alone. Specifically: two systems with
identical total entropy production, event count, and causal order can differ
in their branching exponent and, consequently, in the source-order
certification they can perform at scale.

More precisely: if mu_M(r) = c * |r|^beta(r) is the metabolically-scaled
source measure, and if the G-absorption check (T184) shows that mu_M is not
fully determined by the D1RestrictionSystem's gluing data G, then mu_M
constitutes a source-measure candidate that distinguishes systems which are
energetically and causally identical but temporally-structurally different.

## Class

Formal candidate claim. Promoted to PARTIALLY_SUPPORTED status as of 2026-06-22.
Status: PARTIALLY_SUPPORTED -- T184, T185, and T186 all returned positive evidence.

This is a narrowed and disciplined descendant of the metabolic scaling
exploration's "time is co-equal" claim. It does NOT assert time is
ontologically fundamental. It asserts that in a specific and testable
class of physical systems, temporal delivery structure is not reducible to
energetic structure.

## Status

PARTIALLY_SUPPORTED (as of 2026-06-22). Evidence:

1. **T184** (mu_M non-additivity composition gate): COMPLETE. Test B Subcase 2
   found that under architectural-change composition (n1=10, n2=5, beta_seq=0.85),
   mu_M is SUPERADDITIVE while entropy is SUBADDITIVE -- opposite sign discrimination.
   G-absorption is conditional: absorbed for union compositions with fixed beta;
   non-absorbed in the architectural-change transition window.

2. **T185** (lambda*(s) MSY absorption test): COMPLETE. Three TaF-specific residues
   survive MSY reparameterization: stock-independent N, quadratic C (M/M/1 grounded),
   and separately-typed K (PO1 obstruction rate). Reparameterization impossibility
   proved for b != 0 and stock-independent N.

3. **T186** (metric vs. causal order beta test): COMPLETE. Two 5-event systems with
   identical causal order (ordering fraction f=3/5), identical entropy production, and
   identical causal-set quantities (interval sizes, MM dimension estimate) have
   different branching exponents: beta(Alpha)=0.3491 vs beta(Beta)=0.4438. The
   difference is determined by the delivery-time CV, a metric temporal quantity
   absent from causal-set data. This directly supports the MTI core assertion.

4. **Cap_TI Candidate C**: STEP 3 COMPLETE. Positive control confirms R(beta=0.85)=2 <
   R(beta=0.75)=3 for matched 20-event systems. Step 4 (hostile split) advances to
   CONDITIONAL_PASS via T186 fixture.

Remaining open blockers before full promotion:
- Exact WBE continuum derivation from first principles.

Settled blockers (no longer open):
- Exact Moses constrained optimization: RESOLVED by T187 (beta direction persists
  under exact optimization).
- FUNCTOR-OBL-TaF-001: RESOLVED by T221 (directional split — covariant F not a
  functor, contravariant F_op is). This does not change MTI status: the T184-T188
  metric-vs-causal evidence never depended on covariant functoriality.
- PO1-NCK-001: re-scoped by T221 (PO1 types K, not lambda*(S)). MTI does not rely
  on lambda*(S) being a PO1 consequence; it relies on beta carrying metric-temporal
  information, which stands independently.

## What This Does Not Claim

- This does not assert that time is ontologically primary or constitutive
  in a metaphysical sense.
- This does not assert that the Moses framework proves TaF's North Star
  claim.
- This does not claim that mu_M is already a nonabsorbed source primitive.
  (The G-absorption check in T184 must pass first.)
- This does not upgrade H7 status.
- This does not claim the 3/4 scaling exponent is universal or applies
  outside its grounding physical substrate class.
- This is not a new physical law or extension of thermodynamics.

## Why It Might Be True

The Moses framework (Moses et al. 2016; West-Brown-Enquist) derives the 3/4
metabolic scaling law from a joint energy-time optimization over hierarchical
branching transport networks. The derivation requires metric temporal structure
(delivery time as a measurable quantity), not just causal order (which events
happen before which). Causal order alone is insufficient to derive the 3/4
exponent: you also need to know that delay is a physical cost, which requires
a metric, not just a partial order.

This means: in systems governed by the Moses constraints, the branching
exponent beta encodes information about temporal metric structure that is not
already in the causal order. A system that tracks only which events came
before which (causal order) without tracking how long the gaps were (metric
temporal structure) cannot recover beta from its records. Two systems with
the same causal order can have different betas if their temporal metric
differs.

Since mu_M = c * |r|^beta is a function of beta, and beta requires metric
temporal information beyond causal order, mu_M may be a source measure that
differentiates systems with identical causal structures but different temporal
metrics. If the D1RestrictionSystem's gluing data G does not encode metric
temporal structure (only causal-order structure), mu_M would survive
G-absorption.

The five-run metabolic-issuance persona panel (2026-06-22) found this to be
the strongest discriminating property of the metabolic scaling exploration:
"the sublinearity arises from the hierarchical branching architecture itself,
not from saturation or interference effects that entropy production also
captures" (Run 1, Maya Osei, Strongest Insight).

## How It Could Fail

**Failure mode 1 (G-absorption)**: If the D1RestrictionSystem's gluing data G
is defined to include metric temporal structure (timestamps, durations, or
delay annotations), then mu_M = c * |r|^beta is computable from G and the
claim is absorbed by TaF's existing formalism. The G-absorption check in T184
is the decisive test.

**Failure mode 2 (causal-set absorption)**: The causal-set program already
works with metric temporal structure through sprinkling and Myrheim-Meyer
ordering fractions. If the branching exponent beta is computable from causal-
set data (not just causal order), MTI is absorbed by the causal-set framework.
T185 does not test this; a separate causal-set absorption check would be needed.

**Failure mode 3 (entropy production absorption)**: If beta is determined by
the entropy production profile of the transport network (higher-entropy
networks have higher branching efficiency), then mu_M is a function of the
thermodynamic ledger and is absorbed by stochastic thermodynamics. This
requires checking whether the 3/4 exponent can be derived from entropy-
production data alone without metric time.

**Failure mode 4 (substrate restriction)**: If MTI holds only for biological
organisms and not for the class of physical systems TaF cares about (observer
records, detector systems, distributed computers), the claim is a biological
fact, not a general TaF result. The Moses et al. (2016) extension to computing
systems is evidence against this failure mode, but extension to arbitrary
D1RestrictionSystems requires justification.

**Failure mode 5 (non-additivity absorbed)**: T184 may find that mu_M's
non-additivity under all composition operations is reproduced by entropy or
G. In that case, mu_M carries no discriminating information and MTI is vacuous.

## Tests

1. **T184** (mu_M non-additivity composition gate): Tests whether mu_M has
   a composition operation where it is non-additive while absorbers are
   additive, and whether G absorbs mu_M.

2. **T185** (lambda*(s) MSY absorption test): Tests whether the dynamics
   of the Ext_S system guided by mu_M is absorbed by classical MSY or has
   TaF-specific residue. A positive result (non-absorption) would corroborate
   MTI by showing that mu_M guides dynamics that cannot be replicated by
   energy-only measures.

3. **Proposed T186** (metric vs. causal order beta test): Explicitly construct
   two D1RestrictionSystems with identical causal order but different temporal
   metric (same sequence of events, different gaps between them). Check whether
   beta differs and whether mu_M is consequently different. If yes, MTI is
   supported. If beta is the same for both (because beta is determined by
   network topology rather than temporal metric), MTI may be weaker than
   claimed.

## Known Neighbors

- West-Brown-Enquist metabolic scaling (1997, 1999): the 3/4 law grounding
- Moses et al. (2016): extension to computing systems, substrate-independence
- Causal-set theory: uses both causal order and metric (sprinkling density)
- Stochastic thermodynamics: entropy production rates in transport networks
- D1-Field (D1-field-multiscale-observer-finality.md): cross-scale D1 transport
- T37 (TypedTransportNetwork): typed morphisms with explicit forgotten structure
- T184 (mu_M non-additivity composition gate): primary test
- T185 (lambda*(s) MSY absorption test): corroborating test
- `open-problems/cap-ti-capability-object-spec.md`: capability object target
- `technical-reports/TECHNICAL-NOTE-time-as-optimization-cost-objection-v0.1.md`:
  resolution of the "time as cost" objection to this claim

## Contribution Needed

This claim is open and not promoted. It should not be added to CLAIM-LEDGER.md
until:

1. T184 runs and returns a non-null result (mu_M has a discriminating
   composition operation and survives G-absorption).

2. At least one Cap_TI candidate from
   `open-problems/cap-ti-capability-object-spec.md` is tested with a
   positive-control fixture, showing that a system with mu_M as its source
   measure can perform a task that entropy-only systems cannot.

3. One failure mode above is definitively ruled out by a test.

If T184 returns null (G absorbs mu_M or no discriminating composition exists),
this claim file should be updated to status "demoted" and the reason recorded.
Do not delete the file; it is useful as a record of what was attempted and why
it failed.
