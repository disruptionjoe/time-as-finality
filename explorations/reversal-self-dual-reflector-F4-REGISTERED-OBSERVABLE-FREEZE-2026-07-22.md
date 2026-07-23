---
title: "F4 registered-observable freeze and blocked adapter verdict"
status: blocked_missing_registered_observable
doc_type: pre_results_reference_freeze
created: 2026-07-22
lane: "1"
track: "bounded TaF-1 own-absorber check"
claim_effect: none
compute_effect: none
---

# F4 registered-observable freeze and blocked adapter verdict

## Decision

The exact repaired-S1 and Myrheim-Meyer sources exist, but the frozen F4 panel
cannot run honestly from their current public interfaces. This gate therefore
returns the predeclared outcome `blocked_missing_registered_observable` before
enumeration. No panel object was generated and no result-dependent choice was
made.

## Frozen source references

| Role | Exact source | Frozen content |
|---|---|---|
| repaired S1 suite | `models/t525_repaired_s1_manifoldlikeness_suite.py` (`sha256:82965b824f8206553baddabd64a96bee038bf9298bd9ab52e7eef9c01b025521`) | T126 hard gates plus event-count-matched empirical bands for ordering fraction, height, width, and largest interval; the profile-spread/order-dimension leg is quarantined |
| random-control calibration | `models/t524_t126_random_sprinkle_diagnostic_repair.py` (`sha256:bfa716affb79a99bd7ab7ce0bd78bd3df2f0db2c5df6e0fe70dfc8964630dacd`) | seeded 1+1 light-cone sprinkles; `DEFAULT_SEEDS = tuple(range(8))`; current registered sizes `(8, 12, 16, 20)` |
| Myrheim-Meyer readout | `models/myrheim_meyer_dimension_estimator.py` (`sha256:6c650ceb9e216a9b901c666e7763b9cad47b4646667174eaed494ae5c34076ee`) | `f(d)=Gamma(d+1)Gamma(d/2)/(2 Gamma(3d/2))`; `estimate_dimension` inverts on `[0.5,12]`; the `+/-0.25` tolerance validates known-dimension sprinklings and is not an F4 acceptance band |
| causal-set diagnostics | `models/finality_colimit_causal_set_embeddability.py` | finite-poset gate; hub cutoff `>=3/4`; chain/antichain rank-width rejection; profile-spread quarantine source; interval-profile obstruction at height `<=2`, strict pairs `>=n`, and link density `>=9/10` |

## Why the panel is blocked

1. `run_t525_analysis()` is closed over its registered random controls and
   T249/T252 candidates. Its arbitrary-candidate calibration and audit helpers
   are private implementation functions, not a frozen adapter contract.
2. The F4 panel includes `n=6`, while the registered random-control sizes begin
   at `n=8`. Extending calibration to six events may be reasonable, but doing
   so now would add a threshold/construction after the panel spec was frozen.
3. A new F4 poset still needs a pre-results mapping into
   `FinalityColimitCausetDatum`, including descent, canonical-colimit,
   phantom-gap, and minimum-event fields. Those values are not entailed by the
   bare poset plus reversal map. Choosing them during implementation could
   manufacture or suppress a hard-gate result.
4. The Myrheim-Meyer estimator provides a dimension-valued readout, not a
   registered pass/fail threshold for F4 versus planted 2D controls. Its
   validation tolerance cannot be repurposed as that acceptance band.
5. The predeclared outcome requires the registered observables to agree at
   every size. Without an adapter and comparison rule frozen before results,
   “agreement” is undefined.

## Exact wake

Reopen only after one owner-governed, pre-results adapter specification freezes
all of the following without viewing F4 panel results:

- the mapping from an arbitrary finite poset plus reversal map into the T126
  datum fields;
- whether `n=6` is removed by a new explicit panel revision or calibrated by a
  separately justified seed/control rule;
- the public repaired-S1 candidate-audit interface for F4, random, KR, chain,
  antichain, and planted-2D families;
- the Myrheim-Meyer comparison rule against the planted controls, explicitly
  not reusing the `+/-0.25` validation tolerance as a favorable result band;
- the multi-observable agreement and statistical-separation rule; and
- the invariant relation-density matching procedure.

Until then, do not enumerate, retune, substitute a proxy, or label the absence
of a result as evidence against or for reversal self-duality.

## Nonclaims

This block says only that the registered executable interface is incomplete for
the frozen panel. It does not say self-duality underselects, generate a
continuum claim, move S1, establish a physical source law, or change TaF's
supplier relationship to Dynamic Unity.
