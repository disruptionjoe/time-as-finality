# Q1B Federated Detector Deployment Handoff

## Status

External deployment issue draft. This is not detector evidence, not a
prediction, and not a Q1B upgrade.

## Route

Quantum measurement / classical records, with experimental-discriminator
pressure on detector evidence infrastructure.

## Why This Exists

T140 says the Q1 branch has no active internal upgrade route. Q1A is absorbed
as bookkeeping, Q1C is dormant under the full-record gate, and Q1D is
guardrail-only. Q1B is the only non-null experimental path, but it is blocked
until a named deployment signs a T136/T138-valid manifest before detector
events and later publishes real event-level packet rows.

This file converts that blocker into a concrete issue draft. Its purpose is to
make Q1B externally testable or demote its operational priority.

## Current Strongest Claim

Q1B survives only as a pre-data admissibility protocol over already formed
detector records:

```text
No detector run counts for Q1B unless its event-level records, wrapper fields,
authority domains, export rules, hostile controls, and claimed tier are frozen
before the first event and then populated without schema, authority, or policy
drift.
```

The live question is not whether a lab has accurate time tags. The question is
whether the lab can precommit the full evidence object without collapsing the
archive and trust-audit roles into self-certification, including hidden
collapses through shared critical control roots, and whether it will later
make the full bound event rows reviewable during the challenge window rather
than substituting proofs, summaries, private escrow, or delayed release.

## Issue Draft

### Title

Pre-data federated detector manifest for Q1B admissibility

### Objective

Find one detector group or collaboration willing to freeze a T136/T138
manifest before event collection, populate the bound packet with real
event-level rows after collection, and accept the null verdicts below.

### Background To Send

The project is not asking the lab to endorse Time as Finality. It is asking
whether a detector workflow can produce a pre-registered evidence packet strong
enough that later D1 scoring would not be post hoc provenance selection.

The nearest repo artifacts are:

- [T136 Detector Pre-registration Manifest](../tests/T136-detector-preregistration-manifest.md)
- [T138 Detector Manifest Workflow Fit](../tests/T138-detector-manifest-workflow-fit.md)
- [T140 Q1 Frontier Escape Matrix](../tests/T140-q1-frontier-escape-matrix.md)

### Minimum Pre-data Commitment

Before the first detector event, the deployment must freeze:

1. Stable run id and claimed tier: `raw_log_preservation`,
   `provisional_admission`, or `claim_review`.
2. T97 table schema hashes and empty-export checksums.
3. T121/T133 wrapper-field commitments for the claimed tier.
4. A T100-compatible authority partition with at least four non-conflicting
   domains.
5. A T161 control-root map for manifest registration, archive mutation, audit
   attestation, publication release, and revocation control.
6. A raw-payload export rule, not observed payload values.
7. Hostile-control plan for replay/spoof, perturbation/back-action,
   provenance-DAG truncation or false ancestry, signature/key failure, and
   delayed publication.
8. Top-level manifest hash and timestamp before any event data are inspected.

### Authority Partition Required

For claim review, the clean scaffold uses five separated roles:

```text
analysis_governor
instrument_operator
control_designer
archive_custodian
trust_auditor
```

T100 permits a few four-domain merges, but the trust auditor must remain
independent. T161 adds that nominal role labels are insufficient when critical
control roots are shared. Any workflow merging archive custody and trust audit,
or sharing manifest/archive/audit/publication/revocation roots in a way that
collapses the effective partition, is null for Q1B unless the packet design is
changed and re-audited before data.

### After-data Packet Required

After event collection, the group must publish or make reviewable:

1. Event-level raw measurement payload rows under the precommitted export rule.
2. Event loss and retention rows.
3. Signature verification and key-state rows.
4. Replay/spoof control rows.
5. Perturbation or back-action control rows.
6. Provenance-DAG ancestry and truncation-control rows.
7. Publication timing and immutable archive rows.
8. Reconstruction-path, witness-reference, revocation, and challenge-state rows
   if the claimed tier is `claim_review`.
9. Enough key/root provenance to audit whether the declared authority split was
   operationally real rather than nominal only.
10. Reviewable access to the full bound event rows during the challenge window,
    not merely aggregate summaries, proof certificates, sampled rows, delayed
    release, or auditor statements about private escrow.

Dashboard summaries do not substitute for these rows.

## Non-null Outcomes

The only positive near-term outcome is narrow:

```text
A named deployment signs a pre-data manifest, later publishes the bound packet
without drift, and survives T87/T97/T100/T121/T133/T136/T138/T83.
```

That would not prove Q1B or Time as Finality. It would make Q1B reviewable as a
real detector-admissibility artifact instead of a scaffold.

## Null Outcomes

Treat the route as null for Q1B if any of these occur:

- The manifest is assembled after data collection.
- The lab offers dashboard summaries instead of event-level rows.
- The claimed tier changes after data.
- Schema, wrapper policy, authority partition, or export rules drift after the
  manifest hash.
- The nominal authority split hides shared critical control roots that collapse
  the effective partition.
- Archive custody and trust audit are controlled by the same authority.
- The payload field contains observed detector values before the event
  boundary.
- Hostile controls are absent or only reported as aggregate pass/fail claims.
- The group cannot publish or independently escrow packet rows.
- The group can only offer proof-only, summary-only, sampled-row, private-
  escrow-only, or delayed-release substitutes instead of reviewable full rows
  during the challenge window.

## Decision Rule

If no named group will sign the pre-data manifest with independent archive and
trust-audit roles and an admissible T161 control-root map, Q1B should remain
externally blocked and should not receive additional internal toy-model work.
Future autonomous runs should prefer thermodynamic-arrow,
spacetime-reconstruction, or formal-machinery targets unless a concrete Q1B
signatory appears.

If a group can sign the manifest but refuses full event-level packet review
during the challenge window after collection, Q1B remains a scaffold-only
protocol and gains no empirical support.

## What This Would Improve

- Converts the Q1B blocker into a yes/no external ask.
- Prevents "good detector hardware" from being confused with admissible
  detector evidence.
- Gives a concrete demotion path if realistic workflows cannot satisfy the
  authority and event-row requirements.

## What This Weakens

This weakens Q1B as an autonomous research route. The branch now depends on
external organizational behavior, not another internal finite witness. If the
federated manifest cannot be signed by a realistic detector group, Q1B should
stay below active quantum-measurement work.

## Claim Ledger Update

Q1B remains `externally_blocked`. The next non-null artifact is not another
model; it is a named detector deployment that signs the T136/T138 manifest
pre-data, exposes a T161-valid control-root map, and later supplies real
event-level packet rows in the stronger T171 sense: full reviewable rows during
the challenge window with independent escrow. Without that, Q1B is an
admissibility scaffold only.
