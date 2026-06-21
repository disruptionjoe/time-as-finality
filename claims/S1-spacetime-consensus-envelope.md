# S1: Spacetime As Consensus Envelope

## Claim

Spacetime may be a consensus envelope for causally bounded finality.

## Class

Speculative extension.

## Status

Open formal target.

## What This Does Not Claim

- It has not yet derived spacetime.
- It does not defeat no-go theorems by declaration.
- It does not replace GR or quantum field theory.
- It is not required for the core essay to be useful.
- It does not claim there is a single global consensus state.

The guardrail is not "do not go here." The guardrail is: do not make S1
load-bearing until there is an explicit map from observer-local finality
domains to a spacetime-like object, plus a failure condition.

## Why It Might Be Interesting

If many bounded observer-systems maintain compatible histories without a universal now, spacetime may be understood as the stable interface in which that compatibility is possible. This is a bolder extension of the record-finality framework, not the core claim.

The dynamic but disciplined version is:

> Spacetime-as-interface may be the structure through which local record histories remain mutually compatible where causal domains overlap, without requiring global synchronization over all reality.

This keeps the heterodox "rendered interface" intuition alive while forcing a local-consistency discipline. The question is not whether a universal renderer computes all of reality. The question is whether observer-facing spacetime can be modeled as a compatibility interface among causally bounded record domains.

## How It Could Fail

- It cannot define the map between deeper source, observer protocol, and classical record layer.
- It conflicts with known spacetime physics.
- It remains an evocative phrase without technical content.
- It fails to distinguish observation by received records from direct local participation.
- It smuggles in a global synchronization layer under the word "consensus."

## Tests

- [Rendered Interface Assumptions](../open-problems/rendered-interface-assumptions.md)
- [Spacetime as Finality Colimit](../open-problems/spacetime-as-finality-colimit.md)
- [T7: Overlapping Causal Domains](../tests/T7-overlapping-causal-domains.md)
- [T16: Spacetime Aggregation Toy Model](../tests/T16-spacetime-aggregation.md)
- [T126: Finality-Colimit Causal-Set Embeddability Audit](../tests/T126-finality-colimit-causal-set-embeddability.md)
- [T154: T54/T58-to-T126 Bridge](../tests/T154-t54-t58-t126-bridge.md)
- [T156: Myrheim-Meyer Ordering-Fraction Screen](../tests/T156-myrheim-meyer-ordering-fraction-screen.md)
- [T157: T54 Ordering-Fraction Bridge](../tests/T157-t54-ordering-fraction-bridge.md)
- [T159: T54 Interval-Jackknife Screen](../tests/T159-t54-interval-jackknife-screen.md)
- [T151: Causal-Access Screen](../tests/T151-causal-access-screen.md)
- [T153: Lorentzian Causal-Diamond Screen](../tests/T153-lorentzian-causal-diamond-screen.md)

## Contribution Needed

Turn "consensus envelope" into a precise formal proposal. The minimum
deliverable is a defined aggregation, gluing, or colimit construction over
observer-local finality domains. The failure condition is equally important:
if the construction cannot preserve known causal, metric, or covariance
constraints, S1 should be weakened back to metaphor.

## T16 Result

[T16](../tests/T16-spacetime-aggregation.md) defines the first executable
aggregation target. Observer-local finality domains glue only when their
overlap restrictions agree and their union remains acyclic. The output is a
global partial order or a concrete obstruction witness.

This strengthens S1 as a formal target, not as a spacetime derivation.

## T151 Access-Map Guardrail

[T151](../tests/T151-causal-access-screen.md) adds a minimum access-map
requirement. Future S1 aggregation cannot use only compatible local orders. It
must also type:

- which source events can send records to which observer access events;
- whether access is direct participation, received classical signal, or an
  encoded/indirect channel;
- which boundaries are inward-only, outward-only, or bidirectional;
- whether crossing a boundary preserves or transforms record character.

Without those maps, "consensus envelope" remains underdeclared and risks
smuggling in a global synchronization layer.

## T126 Causal-Set Embeddability Gate

[T126](../tests/T126-finality-colimit-causal-set-embeddability.md) adds a
finite necessary-condition screen between finality colimits and spacetime
language. A candidate must first be canonical descent data, then a valid finite
causal-set candidate, then survive selected manifoldlikeness diagnostics.

The strongest positive T126 result is only `passes_filter_only`. Valid
finality posets can still fail hub, interval-profile, rank/width, or local
dimension-profile screens. Passing T126 does not derive a manifold, metric,
Lorentzian geometry, GR, or a continuum limit.

## T154 Direct Colimit Bridge

[T154](../tests/T154-t54-t58-t126-bridge.md) connects the actual T54
canonical T51/T52 quotient-union completions to T126 after the T58
phantom-gap well-formedness gate. Both become finite causal-set candidates,
but both are classified `insufficient_scale`.

This weakens any reading that T51/T52 already supply spacetime-facing
evidence. They are currently causal-set gate controls only, not
manifoldlikeness, dimension-estimator, sprinkling, locality, embedding, or
continuum-limit witnesses.

## T156 Ordering-Fraction Guardrail

[T156](../tests/T156-myrheim-meyer-ordering-fraction-screen.md) adds a named
Myrheim-Meyer-style ordering-fraction check after T126. For a declared flat
1+1 interval target, the ordering fraction is `1/2` with a finite audit band
of `+/- 1/10`.

The deterministic light-cone-coordinate control lands inside that band
(`7/15`). But the six-event 2x3 product-grid colimit and the existing T126
3x3 grid survivor both pass T126 while failing the target (`4/5` and `3/4`).

This weakens S1 again: `passes_filter_only` is only a pre-diagnostic T126
verdict. It is not dimension evidence, sprinkling evidence, a faithful
embedding, a Lorentzian metric reconstruction, or a continuum-limit result.

## T157 T54 Ordering-Fraction Bridge

[T157](../tests/T157-t54-ordering-fraction-bridge.md) removes one narrow
blocker left by T156. A constructed six-event T54 canonical quotient-union
colimit reaches T126 and matches the declared flat 1+1 ordering-fraction band:
`7/15` versus target `1/2 +/- 1/10`.

This is a control, not an upgrade. The product-grid T54 control still passes
T126 while failing the target (`4/5`), and the six-event chain is rejected at
T126. T157 shows that T54 can realize a finite 1+1-like ordering-fraction
control, but it does not supply interval abundance, locality, sprinkling,
embedding, covariance, continuum-limit, or Lorentzian metric evidence.

## T159 Interval-Jackknife Screen

[T159](../tests/T159-t54-interval-jackknife-screen.md) demotes the T157
positive boundary back to calibration-only. The T157 flat T54 control still
passes T126, T156, and the parent interval-support screen, but it fails a
single-deletion stability check: deleting `p4` drops the ordering fraction to
`1/5`, outside the declared `1/2 +/- 1/10` band.

This is not a continuum no-go theorem. It is a finite fragility screen. The
earned update is that a single hand-built T54 ordering-fraction survivor is
not robust S1 evidence. Future S1 colimits need a non-hand-built family,
deletion-stable finite samples, or a declared random-sprinkling/locality
comparison before spacetime-facing residue language is considered.

## T163 Rank-Pair Family Census

[T163](../tests/T163-t54-rank-pair-family-census.md) answers one part of that
post-T159 blocker. In the exhaustive six-event T54 rank-pair family with fixed
causal ranks and all `6!` information-rank permutations, deletion-stable
survivors do exist: 26 labeled cases clear T126, T156, parent-interval
support, and the T159 single-deletion screen.

This improves the finite S1 boundary but only slightly. The original T157
construction remains fragile, and most of the family is still blocked earlier:
T126 rejects 142 cases, T156 rejects 273 more, parent-interval support rejects
149 more, and 130 additional cases are jackknife-fragile. The surviving 26 are
therefore a small finite subfamily, not spacetime evidence.

The next burden shifts from "find any deletion-stable six-event sample" to
"quotient and stress-test the surviving subfamily." Until that is done, S1
still lacks isomorphism control, random-sprinkling comparison, locality tests,
embedding theorems, covariance, and continuum reconstruction.

## T153 Lorentzian Absorber Gate

[T153](../tests/T153-lorentzian-causal-diamond-screen.md) weakens any S1
reading that relies only on access or reconstructability splits. In the tested
1+1 controls, verdicts factor through causal pasts, access diamonds, spacelike
separation with common futures, and domains of dependence.

Future S1 work must therefore match the Lorentzian causal relation, observer
world tube, access diamond, record channels, and domain-of-dependence inputs
before claiming a finality-colimit residue. A verdict split caused by changed
causal data is standard spacetime causal structure, not evidence that S1 has
derived spacetime.
