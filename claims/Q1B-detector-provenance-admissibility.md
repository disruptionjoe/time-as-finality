# Q1B: Detector Provenance Admissibility

## Claim

Detector records may count as D1 finality evidence only when the run supplies a
pre-registered, event-level, auditable provenance packet that fixes record
independence before D1 scoring.

## Class

Subclaim of Q1.

## Status

Externally blocked.

## Current Strongest Form

Q1B is an admissibility protocol over already formed detector records. It does
not currently provide empirical support for Time as Finality, because no real
event-level deployment packet has passed the T87/T97/T100 gates. T133 sharpens
the burden: there is a provisional-admission core for intake, plus a stricter
claim-review extension for reconstruction, certification, and dispute-ready
use.

## Earned Content

- T66-T72 show that calibrated detector statistics and passive correlations do
  not determine the D1 independence partition.
- T74-T86 narrow the surviving route to pre-registered raw-log provenance with
  isolated hostile controls for tags, perturbation response, ancestry DAGs,
  trust boundaries, and demotion rules.
- T87 rejects dashboard summaries and post hoc policies before scoring.
- T95-T100 map the named detector-stack route to a schema-complete packet and
  show that at least four non-conflicting authority domains are required.
- T121-T123 show that raw-payload validity and same-measurement sameness are
  weaker than packet admissibility and future operation availability.
- T133 shows the packet burden is tiered: provenance/signature/authority/
  publication/revocation/key-state fields gate provisional admission, while
  witness/reconstruction/dispute fields gate full claim review.

## Not Earned

- No native detector-physics discriminator.
- No calibration-free Stern-Gerlach or photon-counting prediction.
- No empirical support without real event rows.
- No upgrade from dashboard summaries, fixture counts, or post hoc
  provenance labels.

## Falsification Or Demotion Condition

If no realistic lab workflow can freeze the required raw-log packet, controls,
trust audit, and authority separation before data collection, then detector
provenance should be demoted below the active Q1 frontier.

## Reinstatement Condition

The branch becomes live only when a concrete deployment publishes the locked
event-level packet, passes T87/T97/T100 without changing schema or policy after
data collection, and then yields a verdict that survives the T83 null
criterion.

## Primary Evidence

- [T66: POVM Detector Calibration Obstruction](../tests/T66-povm-detector-calibration-obstruction.md)
- [T78: Pre-registered Detector Deployment Protocol](../tests/T78-preregistered-detector-deployment-protocol.md)
- [T83: Q1 Detector Null Criterion](../tests/T83-q1-detector-null-criterion.md)
- [T87: Real-Run Raw-Log Contract](../tests/T87-real-run-raw-log-contract.md)
- [T95: Detector Stack Export Map](../tests/T95-detector-stack-export-map.md)
- [T97: Detector Dry-Run Packet Skeleton](../tests/T97-detector-dry-run-packet-skeleton.md)
- [T100: Detector Authority-Domain Bound](../tests/T100-detector-authority-domain-bound.md)
- [T121: Real Detector Packet Schema Audit](../tests/T121-real-detector-packet-schema-audit.md)
- [T123: Same-Payload Packet FOA Witness](../tests/T123-same-payload-packet-foa-witness.md)
- [T133: Detector Packet Tiered Minimality](../tests/T133-detector-packet-tiered-minimality.md)
