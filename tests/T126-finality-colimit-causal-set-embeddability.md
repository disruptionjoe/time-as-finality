# T126: Finality-Colimit Causal-Set Embeddability Audit

## Target Claims

- [S1: Spacetime As Consensus Envelope](../claims/S1-spacetime-consensus-envelope.md)
- [Spacetime as Colimit of Finality Domains](../open-problems/spacetime-as-finality-colimit.md)
- [T16: Spacetime Aggregation Toy Model](T16-spacetime-aggregation.md)
- [T51: Multi-Observer Apparent Finality Colimit](T51-multi-observer-apparent-finality-colimit.md)
- [T52: Symmetric Colimit Theorem](T52-symmetric-colimit-theorem.md)
- [T53: Observer-Colimit Descent Boundary](T53-observer-colimit-descent-boundary.md)
- [T54: Finite Finality Descent Theorem](T54-finite-finality-descent-theorem.md)
- [T56: Sheaf Cohomology of Apparent Finality](T56-sheaf-cohomology-apparent-finality.md)
- [T58: Gap-Phantom Equivalence Audit](T58-gap-phantom-equivalence.md)

## Central Question

After T16/T51/T52/T54-style colimits produce a finite global finality partial
order, can that order pass a disciplined causal-set manifoldlikeness audit?

T126 asks only for a finite necessary-condition filter:

```text
observer-local finality domains
  -> finite descent/colimit order
  -> causal-set validity checks
  -> manifoldlikeness obstruction classification
```

Passing the audit does not derive spacetime, GR, metric geometry, or a
Lorentzian manifold. It only means the finite colimit has not yet failed the
chosen causal-set embeddability filters.

## Hypothesis Under Audit

**A canonical finite finality colimit can be treated as a causal-set candidate,
but many valid finality colimits should be rejected by explicit
non-embeddability modes before S1 is strengthened.**

The audit is expected to classify three levels separately:

```text
valid finite partial order
  != canonical observer-descent colimit
  != manifoldlike causal-set candidate
```

## Formal Objects

### Input Datum

A finite `FinalityColimitCausetDatum` should contain:

- observer-local finality domains;
- event identity maps and overlap witnesses inherited from T54;
- local-to-global record maps;
- the quotient-union/global colimit relation, if already computed;
- phantom-gap annotations inherited from T56/T58, when available;
- optional causal-set diagnostics, such as interval counts, rank profile, and
  dimension-estimator samples.

### Candidate Causal Set

The candidate causal set is the finite relation:

```text
C = (E, <=_F)
```

where `E` is the finite event set and `<=_F` is the non-strict finality order
returned by the canonical colimit/descent construction.

The strict causal-set relation is:

```text
x <_F y iff x <=_F y and x != y
```

No metric, coordinates, topology, differentiable structure, or continuum limit
is part of the object under test.

## Audit Filters

### 1. Descent Gate

The input must first satisfy the T54 finite descent conditions:

- event identity maps are total and single-valued;
- overlap witnesses exist for identified events;
- source and target record merges are non-conflicting;
- finality-axis profiles agree across identified events;
- the quotient-union relation is a valid partial order;
- AM status is reported, whether valid or invalid.

If this gate fails, T126 must not continue to causal-set embeddability claims.

### 2. Causal-Set Gate

The colimit relation must be:

- finite;
- reflexive;
- antisymmetric;
- transitive;
- locally finite, which is automatic for finite `E` but should still be
  reported explicitly;
- free of observer-only phantom gaps that would change the strict order under
  the ambient colimit.

This gate classifies whether the finality colimit is a causal-set candidate at
all.

### 3. Manifoldlikeness Necessary-Condition Gate

For finite witnesses, the audit should use only combinatorial diagnostics that
can falsify obvious non-manifoldlike behavior. Candidate diagnostics include:

- interval abundance: counts of Alexandrov intervals by cardinality;
- rank/height profile: distribution of longest-chain depths;
- width profile: maximal antichain and layer sizes;
- link density: number of covering relations relative to total comparable
  pairs;
- dimension-estimator consistency across sampled intervals;
- interval homogeneity: similar-sized intervals should not have wildly
  incompatible internal profiles unless the witness is intentionally irregular;
- coarse locality: no small number of events should act as unnatural universal
  hubs for most comparabilities.

These diagnostics are necessary-condition filters only. They do not prove a
faithful embedding.

## Non-Embeddability Modes

T126 should make rejection explicit. Expected classifications:

| Classification | Meaning |
| --- | --- |
| `not_descent_datum` | T54-style event maps, overlap witnesses, or record maps are missing or malformed. |
| `noncanonical_colimit` | The observer data admit multiple compatible completions, so there is no unique candidate causet. |
| `not_poset` | The colimit relation is cyclic, non-antisymmetric, or non-transitive. |
| `phantom_gap_unresolved` | T56/T58-style apparent gaps still change the ambient strict order, so the tested object is observer-apparent rather than event-finality. |
| `order_dimension_obstruction` | Finite order diagnostics require incompatible effective dimensions across essential intervals. |
| `interval_profile_obstruction` | Alexandrov interval counts or internal interval profiles are incompatible with the chosen manifoldlikeness filter. |
| `rank_width_obstruction` | Height, layer, or antichain profiles are too degenerate for the selected finite manifoldlike control class. |
| `hub_nonlocality_obstruction` | A small set of events creates excessive nonlocal comparabilities or covering links. |
| `insufficient_scale` | The witness is too small for the selected diagnostics to be meaningful. |
| `passes_filter_only` | No specified obstruction was found; this is not an embedding proof. |

## Required Witness Classes

The specification should eventually be exercised on these witness classes:

1. `t16_positive_poset_control`
   - A compatible finite aggregation from T16.
   - Expected to pass the causal-set gate.
   - May still be `insufficient_scale` for manifoldlikeness diagnostics.

2. `t51_t52_colimit_controls`
   - Positive observer-colimit cases with phantom incomparabilities repaired by
     the event-finality colimit.
   - Expected to distinguish observer-apparent orders from the ambient colimit
     order before running embeddability filters.

3. `t53_noncanonical_boundary`
   - A valid partial-order merge that does not determine a unique canonical
     completion.
   - Expected classification: `noncanonical_colimit`, not an embeddability
     verdict.

4. `t54_descent_failure_controls`
   - Missing identity maps, conflicting records, conflicting axes, and
     nondefinable maps.
   - Expected classification: `not_descent_datum` or the matching T54 failure,
     not causal-set rejection.

5. `explicit_nonmanifoldlike_causet_controls`
   - Finite posets designed to be valid causal sets but fail selected
     manifoldlikeness diagnostics: extreme hub orders, layered complete
     bipartite orders, degenerate chains, degenerate antichains, and interval
     profiles with incompatible dimension estimates.

## Success Criteria

T126 succeeds as a specification if it:

- defines the causal-set candidate as the finite event-finality colimit order;
- refuses to audit noncanonical or malformed descent data as embeddability
  evidence;
- separates partial-order validity from manifoldlikeness;
- lists explicit non-embeddability modes;
- includes at least one class that can pass the causal-set gate while failing a
  manifoldlikeness gate;
- preserves the S1 guardrail that no spacetime, GR, metric, or manifold has
  been derived;
- leaves implementation as future work.

## Failure Criteria

T126 fails if the specification:

- treats any valid finite partial order as spacetime-like by default;
- silently upgrades T16/T51/T52/T54 colimits into manifold derivations;
- runs manifoldlikeness filters before descent/canonicality is established;
- collapses observer-apparent finality into event-finality despite T56/T58 gap
  warnings;
- lacks explicit rejection modes for valid-but-nonmanifoldlike causal sets;
- uses continuum geometry, Einstein equations, or GR assumptions as premises.

## Non-Goals

- Do not derive spacetime.
- Do not derive GR, Lorentzian geometry, field equations, metric structure, or
  diffeomorphism invariance.
- Do not prove faithful embedding into any continuum.
- Do not treat manifoldlikeness as required for the core finality framework.
- Do not erase the distinction between an observer-apparent order and the
  event-finality colimit.
- Do not make S1 load-bearing.

## Expected Scientific Value

T126 should turn the S1 open-problem guardrail into a concrete finite audit:

```text
Before asking whether finality colimits approximate spacetime,
first reject finality colimits that are not even plausible finite causal-set
candidates.
```

This keeps the project from promoting a successful colimit theorem into a
spacetime derivation without passing intermediate causal-set discipline.

## Run Command

None yet. This is a test specification only; no implementation is claimed.

## Dependencies

- T16 supplies finite finality aggregation into a global partial order.
- T51 and T52 supply observer-colimit controls with phantom incomparabilities.
- T53 supplies noncanonical descent-boundary cases.
- T54 supplies finite canonical-descent gates and failure classes.
- T56 supplies the apparent/ambient presheaf distinction.
- T58 supplies the gap-phantom equivalence condition for well-formed extension
  cases.

## Boundary

The strongest possible positive T126 result is:

```text
this finite finality colimit passes the selected causal-set/manifoldlikeness
necessary-condition filters.
```

That verdict is weaker than:

```text
this finite finality colimit embeds in a manifold;
this finite finality colimit derives spacetime;
this finite finality colimit reproduces GR.
```
