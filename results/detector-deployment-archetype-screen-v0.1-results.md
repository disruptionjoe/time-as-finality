# T169 Results: Detector Deployment-Archetype Screen

## Archetype audits

| Archetype | Workflow verdict | Control verdict | Row commitment | Classification | Required next |
| --- | --- | --- | --- | --- | --- |
| `single_lab_posthoc_internal_pki` | `workflow_null_for_q1b` | `nominal_partition_already_inadmissible` | `summary_only_after_run` | `null_predata_manifest_or_nominal_authority_failure` | Repair the pre-data manifest and nominal authority partition before detector events. |
| `predata_single_lab_public_archive_repair` | `workflow_null_for_q1b` | `nominal_partition_already_inadmissible` | `public_archive_summary_and_selected_rows` | `null_predata_manifest_or_nominal_authority_failure` | Repair the pre-data manifest and nominal authority partition before detector events. |
| `nominal_federation_shared_archive_audit_hsm` | `claim_review_scaffold_fit` | `hidden_control_root_merge` | `reviewable_event_rows_promised` | `null_hidden_control_root_merge` | Separate the shared critical control roots or treat the workflow as self-certifying. |
| `nominal_federation_shared_release_root` | `claim_review_scaffold_fit` | `hidden_control_root_merge` | `reviewable_event_rows_promised` | `null_hidden_control_root_merge` | Separate the shared critical control roots or treat the workflow as self-certifying. |
| `federated_independent_roots_private_escrow` | `claim_review_scaffold_fit` | `control_roots_preserve_nominal_independence` | `immutable_private_escrow_only` | `scaffold_only_no_reviewable_event_rows` | Commit to reviewable event-level rows rather than proofs, summaries, or private escrow. |
| `federated_independent_roots_reviewable_rows` | `claim_review_scaffold_fit` | `control_roots_preserve_nominal_independence` | `reviewable_event_rows_with_independent_escrow` | `live_external_q1b_candidate` | Obtain a named signatory and actual pre-data manifest; no further internal toy model is needed. |

## Strongest claim

After T138 and T161 are composed, Q1B has only one surviving deployment archetype family: a pre-data claim-review federation with an admissible effective authority partition, distinct critical control roots, and a binding commitment to reviewable event-level rows. Single-lab, public-archive-repair, and nominal-federation stories are null; private escrow without reviewable rows is only scaffold.

## What this improved

T169 turns the detector handoff from an abstract federation ask into a concrete archetype census. Future Q1B discussions can now say exactly which organizational shapes are dead, which are scaffold-only, and which narrow class is still worth asking a lab to sign.

## What this weakened

This weakens Q1B further as an autonomous internal program. Most plausible workflow stories fail before detector physics is even relevant, and even a clean pre-data federation is null unless it also commits to later reviewable event rows.

## Falsification condition

T169 fails if a workflow lacking either a T138-valid pre-data manifest, a T161-valid effective authority partition, or a reviewable event-level row commitment should nevertheless count as a live Q1B deployment archetype.

## Q1B update

Q1B remains externally blocked. T169 narrows the surviving route to one external candidate class: pre-data claim-review manifest, independent effective control roots, and later reviewable event-level packet rows without schema drift.

## Claim ledger update

Add T169 to Q1B: the deployment frontier is no longer generic 'federated detector provenance'. Single-lab, public-archive repair, and hidden-root federation archetypes are null; private escrow is scaffold-only; only a reviewable-row federation remains live as an external candidate.

## Open blocker

No named real detector group in the repo currently instantiates the lone surviving T169 archetype with a signed pre-data packet and a commitment to later reviewable event rows.

## Recommended next

Either map one named collaboration onto the surviving T169 archetype and ask for a signed pre-data manifest, or demote Q1B below the active frontier if no realistic group can accept the reviewable-row burden.
