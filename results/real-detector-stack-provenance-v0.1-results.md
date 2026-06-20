# T75 Results: Real Detector Stack Provenance Mapping

Selected stack: `hydraharp_wr_signed_archive`. Monte Carlo audit over 400 samples with deterministic seed 75031.

Strongest claim: A realistic photon time-tagging stack can occupy the engineered T74 recovery region if it combines picosecond time tags, sub-nanosecond clock distribution, and signed hash-chain archive provenance.

Weakened claim: The positive result is carried by engineered provenance logging, not by detector timing alone. The unsigned-control variant loses robust recovery despite retaining the same time-tagging hardware.

## Source anchors

| Parameter | Value used | Source |
| --- | --- | --- |
| time tagger timing precision | HydraHarp 500: 1 ps base resolution, 2.5 ps RMS timing precision, 680 ps dead time, 85 Mcps throughput | https://www.picoquant.com/products/time-tagging-tcspc-electronics/ |
| distributed timing | White Rabbit: sub-nanosecond distributed timing; CERN notes few-picosecond precision | https://openscience.cern/node/447 |
| signed archive | RFC 3161-style timestamp tokens sign hash imprints and include unique serial numbers | https://www.ietf.org/rfc/rfc3161.txt |

## Stack classification

| Mapping | Verdict | Robust | Withhold | Threshold-dependent | False independence | False dependence | D1 computable |
| --- | --- | --- | --- | --- | --- | --- | --- |
| hydraharp_wr_signed_archive | robust_recovery | 1.0 | 0.0 | 0.0 | 0.0 | 0.0 | 1.0 |
| hydraharp_wr_unsigned_archive_control | conservative_withhold | 0.005 | 0.8425 | 0.1525 | 0.0 | 0.0 | 0.005 |

## Q1 update

Q1 remains partially supported as an instrumentation/provenance claim for explicitly engineered detector stacks.

## Blocker

The timing inputs are source-anchored, but authentication, trust, batching, back-action, and DAG-observability ranges are plausible engineering posteriors rather than measured deployment posteriors.

## Next move

Replace the signed-archive priors with measurements from one lab deployment: event-loss logs, signature-verification failures, archive replay tests, perturbation tests, and DAG truncation audits.
