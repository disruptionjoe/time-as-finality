# T75: Real Detector Stack Provenance Mapping

## Question

Does a realistic detector/logging architecture occupy the engineered T74
provenance region where D1 finality is operational?

## Selected Stack

T75 maps a photon time-tagging stack:

```text
photon detector
  -> PicoQuant HydraHarp 500 time tagger
  -> White Rabbit synchronized timing fabric
  -> hash-chained RFC 3161-style signed archive
```

The timing pieces are source-anchored. The signed archive, trust, batching,
back-action, and DAG-observability ranges are plausible engineering posteriors
for an explicitly instrumented lab stack, not measured deployment posteriors.

## Source Anchors

- PicoQuant lists HydraHarp 500-class timing electronics with 1 ps resolution,
  few-picosecond timing stability, 680 ps dead time, high throughput, and a
  White Rabbit option.
- White Rabbit timing systems provide sub-nanosecond distributed timing and
  few-picosecond synchronization precision.
- RFC 3161 supplies the time-stamp-token pattern: hash imprint, unique serial,
  trusted time value, and signed timestamp token.

## Success Criteria

- The selected signed stack lands in the `robust_recovery` region.
- An unsigned-control variant with the same timing hardware does not recover
  provenance from timing alone.
- Q1 remains scoped to engineered instrumentation/provenance, not generic
  detector measurement.

## Failure Criteria

- The signed stack mostly withholds D1 or creates false-independence or
  false-dependence risk.
- The unsigned-control variant also lands in robust recovery, implying timing
  alone is being over-counted.
- The result depends on ad hoc thresholds rather than declared protocol bounds.

## Claim Impact

If T75 passes, Q1 remains `partially_supported` for explicitly engineered
detector provenance stacks. If a measured deployment later falls outside this
region, detector Q1 should be demoted to a conditional accounting framework
requiring externally supplied provenance.
