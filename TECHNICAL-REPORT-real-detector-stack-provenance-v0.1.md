# Technical Report: Real Detector Stack Provenance Mapping v0.1

## Claim Under Test

T74 showed that robust detector-provenance recovery occupies a narrow
engineered region. T75 asks whether any source-anchored detector/logging
architecture can plausibly occupy that region under explicit posterior
assumptions.

## Selected Stack

The selected stack is a photon time-tagging architecture:

```text
photon detector
  -> PicoQuant HydraHarp 500 time tagger
  -> White Rabbit synchronized timing fabric
  -> hash-chained RFC 3161-style signed archive
```

This is not a claim that a bare time tagger solves provenance. The signed
archive and ancestry graph are part of the detector/logging stack under test.

## Source Anchors

- PicoQuant's HydraHarp 500 materials report 1 ps timing resolution,
  few-picosecond stability, 680 ps dead time, high throughput, and White Rabbit
  support for distributed synchronization.
- White Rabbit timing systems provide sub-nanosecond distributed timing and
  few-picosecond synchronization precision.
- RFC 3161 gives the signed timestamp-token pattern: hash imprint, unique
  serial number, trusted time value, and verifier-checkable signature.

## Posterior Mapping

T75 maps those anchors into the normalized T72/T74 protocol coordinates:

- clock error: tight local time-tag uncertainty, with archive-time uncertainty
  dominated by synchronization and logging rather than the detector TDC;
- batching/archive latency: small engineered batching windows for event-hash
  archival, not arbitrary offline bulk export;
- authentication reliability: high verification and low forgery/spoofing only
  when event batches are signed or timestamped;
- trust boundaries: high but not perfect lab-controlled detector, transport,
  and archive trust;
- perturbation back-action: low, because perturbing copied metadata or signed
  archive entries should not physically couple independent detector channels;
- DAG observability: high only for a hash-chained archive that records ancestry
  between event batches and copies.

An unsigned-control posterior keeps the same timing hardware but weakens
signature, archive trust, and DAG observability.

## Current Strongest Claim

A source-anchored photon time-tagging stack can plausibly occupy the engineered
T74 recovery region if it combines picosecond time tags, sub-nanosecond timing
distribution, and signed hash-chain archive provenance. This is a posterior
mapping, not measured deployment support.

## What This Improved

T75 answers the immediate T74 blocker in a limited way. There is at least one
source-anchored detector/logging architecture that maps into the engineered
recovery region under plausible posteriors.

The important qualification is that the recovery is not carried by detector
timing alone. The unsigned-control variant is included specifically to prevent
that over-reading.

## What This Weakened

T75 weakens any reading of Q1 that treats high-resolution detector timing as
sufficient for D1 finality. Timing must be coupled to signed provenance and
observable ancestry. Without that archive layer, the same detector hardware
does not provide robust recovery in the T75 control.

## Q1 Recommendation

Keep Q1 `partially_supported` as an instrumentation/provenance claim for
explicitly engineered detector stacks:

```text
Detector-level D1 finality is operational only when time-tagged detector
records are coupled to authenticated, observable provenance infrastructure.
```

Do not upgrade Q1 to a generic detector-measurement claim.

## Main Limitation

The timing inputs are source-anchored, but the authentication, trust, batching,
back-action, and DAG-observability ranges are plausible engineering posteriors
rather than measured deployment posteriors.

## Next Work

Replace the T75 priors with measurements from one lab deployment:

- event-loss and tag-retention logs;
- signature-verification failure rates;
- archive replay and forgery tests;
- perturbation tests for copied versus independent records;
- DAG truncation and ancestry-observability audits.

## Reproduction

```bash
python -m unittest tests.test_real_detector_stack_provenance -v
python -m models.run_t75
```
