# T169: Detector Deployment-Archetype Screen

## Route

Quantum measurement / classical records, with experimental-discriminator
pressure on the remaining Q1B deployment route.

## Target Claims

- [Q1B: Detector Provenance Admissibility](../claims/Q1B-detector-provenance-admissibility.md)
- [T138: Detector Manifest Workflow Fit](T138-detector-manifest-workflow-fit.md)
- [T161: Detector Control-Root Independence](T161-detector-control-root-independence.md)
- [Q1B Federated Detector Deployment Handoff](../open-problems/q1b-federated-detector-deployment-handoff.md)

## Question

After T138 and T161, which detector deployment archetypes are still live for
Q1B, and which ones are already null or scaffold-only before any lab data
appear?

## Motivation

The repo currently says Q1B survives as a federated pre-data detector route.
That is still too vague. "Federated" can mean:

- a single lab with a public archive;
- a nominal multi-role consortium with shared HSM or release control;
- a clean pre-data federation that still refuses later event-level review; or
- a genuinely reviewable packet with independent critical roots.

Without an archetype screen, future work can keep treating those as roughly the
same surviving hope.

## Setup

Audit six deployment archetypes:

1. `single_lab_posthoc_internal_pki`
   Accurate hardware and signed exports, but the manifest is assembled after
   the run inside one authority.
2. `predata_single_lab_public_archive_repair`
   The lab locks fields pre-data and uses a public archive, but trust audit and
   archive custody still collapse.
3. `nominal_federation_shared_archive_audit_hsm`
   A claim-review federation clears T138 only nominally, then shares the
   archive/audit HSM.
4. `nominal_federation_shared_release_root`
   A claim-review federation clears T138 only nominally, then shares a
   governance/archive release root.
5. `federated_independent_roots_private_escrow`
   The pre-data packet and critical roots are honest, but post-data review is
   limited to private escrow or proofs rather than reviewable event rows.
6. `federated_independent_roots_reviewable_rows`
   The pre-data packet is honest, the critical roots remain distinct, and the
   post-data packet is reviewable at event level without schema drift.

## Success Criteria

- Single-lab and public-archive-repair workflows are null before detector
  physics matters.
- Nominal federations with shared critical roots are null under T161.
- Private escrow without reviewable rows is scaffold-only, not a live Q1B
  deployment.
- Only the reviewable-row federation remains as a live external candidate
  class.
- The result stays at the level of detector evidence infrastructure rather than
  detector dynamics or Q1 support.

## Failure Criteria

- A workflow counts despite failing the T138 pre-data manifest gate.
- A nominal federation counts despite a T161 hidden critical-root merge.
- Proofs, summaries, or private escrow count as equivalent to reviewable
  event-level rows.
- The result is misread as empirical support rather than narrowing of the
  external deployment frontier.

## Claim Impact

Q1B remains `externally_blocked`.

Add this sharpening:

```text
The surviving Q1B route is no longer generic federated detector provenance.
Only a pre-data claim-review federation with an admissible effective authority
partition, distinct critical control roots, and a binding commitment to later
reviewable event-level rows remains live as an external candidate.
```

## Reproduction

```bash
python -m unittest tests.test_detector_deployment_archetype_screen -v
python -m models.run_t169
```
