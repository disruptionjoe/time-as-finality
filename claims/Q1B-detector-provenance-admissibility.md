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
use. T134 adds the integration gate: filled T97 raw-log rows are necessary but
not sufficient unless the T121/T133 packet wrapper is also frozen before data
collection. T136 makes that freeze object explicit: a pre-event manifest must
bind the T97 table hashes, T121/T133 wrapper-field commitments, T100 authority
partition, top-level manifest hash, no-data boundary, and claimed tier before
the first detector event. T138 turns that manifest into a human-fillable
workflow gate: common single-lab photonic coincidence and single-lab
public-archive repairs are null if post hoc or authority-collapsed; only a
federated pre-data scaffold clears T136, and that remains non-evidence until
real rows populate the bound packet. T161 closes the nominal-federation
loophole: role labels alone do not count if critical manifest, archive, audit,
publication, or revocation control roots are shared, because those hidden
merges collapse the effective authority partition back into self-certification.
T169 narrows the surviving frontier again: even an honest pre-data federation
is scaffold-only unless it also commits to later reviewable event-level rows
without schema drift. T171 then sharpens what that commitment must mean:
proof-only, escrow-only, sampled-row, and delayed-release substitutes are
scaffold-only because they lose reconstruction or challenge rights. The only
live external candidate class is now a pre-data claim-review federation with
distinct critical roots and full reviewable rows during the challenge window.

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
- T134 shows that T97 raw-log readiness alone cannot clear those tiers; a
  combined T97 plus T121/T133 packet must declare the claimed tier before the
  first detector event.
- T136 turns the combined packet requirement into a pre-event manifest gate:
  T97-only, post hoc, invalid-authority, deferred-tier, hash-mismatch, and
  pre-known-payload variants are null for the claimed tier.
- T138 maps the manifest onto concrete workflow shapes: a common single-lab
  photonic coincidence workflow and a public-archive repair with merged
  authorities are null, while a federated pre-data scaffold only clears
  claim-review readiness as a scaffold.
- T161 shows that even a nominally admissible T100/T138 authority split is
  null if critical control roots are shared across those roles. The operative
  object is the effective authority partition after quotienting by shared
  manifest-registration, archive-write, audit-attestation, publication, and
  revocation roots.
- T169 composes the T138 and T161 gates at the deployment-archetype level:
  single-lab and public-archive repairs are null before detector detail
  matters, nominal federations with shared roots are null, private escrow
  without reviewable rows is scaffold-only, and only a reviewable-row
  federation remains live as an external candidate.
- T171 resolves the last ambiguity inside that surviving class: reviewable-row
  means the full bound event-level packet is reviewable during the challenge
  window with independent escrow. Aggregate summaries, proof certificates,
  private escrow with auditor statements, sampled public rows, and late full
  release after challenge expiry are all scaffold-only substitutes.

## Not Earned

- No native detector-physics discriminator.
- No calibration-free Stern-Gerlach or photon-counting prediction.
- No empirical support without real event rows.
- No named real lab has signed the federated T138/T136 template pre-data.
- No upgrade from dashboard summaries, fixture counts, or post hoc
  provenance labels.
- No named real lab in the repo exposes a critical control-root map proving
  that its nominal authority split is operationally independent.
- No named real lab in the repo instantiates the lone T169 surviving
  reviewable-row federation archetype.
- No named real lab in the repo currently accepts the stronger T171 burden of
  full reviewable rows before challenge expiry rather than proof-only,
  summary-only, sampled-row, or private-escrow substitutes.

## Falsification Or Demotion Condition

If no named realistic lab workflow can sign and freeze the federated T138/T136
manifest before data collection, including the claimed tier, wrapper fields,
T100-compatible nominal authority partition, and a critical control-root map
whose effective partition remains admissible under T161, then detector
provenance should be demoted below the active Q1 frontier. The same demotion
applies if realistic groups can only offer proof-only, escrow-only,
sampled-row, or delayed-release substitutes instead of T171-level full
reviewable rows during the challenge window.

## Reinstatement Condition

The branch becomes live only when a concrete deployment publishes a T136
manifest satisfying the T138 workflow-fit gate before event collection, fills
the bound event-level packet without changing schema, authority, tier, or
wrapper policy, exposes enough control-root data to show that the T161
effective authority partition remains admissible, passes the T87/T97/T100 and
T121/T133 gates, satisfies the T169 reviewable-row commitment in the stronger
T171 sense of full reviewable rows during the challenge window with
independent escrow, and then yields a verdict that survives the T83 null
criterion.

## Operational Handoff

The current handoff is [Q1B Federated Detector Deployment Handoff](../open-problems/q1b-federated-detector-deployment-handoff.md).
It is a lab-facing issue draft, not evidence. It converts the external blocker
into a pre-data manifest ask, event-row packet requirements, null conditions,
and a demotion rule if no realistic workflow can supply independent archive and
trust-audit roles before detector events.

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
- [T134: Detector Dry-Run Tier Gate](../tests/T134-detector-dry-run-tier-gate.md)
- [T136: Detector Pre-registration Manifest](../tests/T136-detector-preregistration-manifest.md)
- [T138: Detector Manifest Workflow Fit](../tests/T138-detector-manifest-workflow-fit.md)
- [T161: Detector Control-Root Independence](../tests/T161-detector-control-root-independence.md)
- [T169: Detector Deployment-Archetype Screen](../tests/T169-detector-deployment-archetype-screen.md)
- [T171: Detector Row-Review Substitution Screen](../tests/T171-detector-row-review-substitution-screen.md)
