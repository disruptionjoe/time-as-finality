# T123 Results: Same-Payload Packet FOA Witness

## Strongest claim

Yes. In the finite detector-packet audit, packet-level structure changes admissibility, reconstruction, challenge, certification, and future operation availability while raw payload, immediate measurement result, and coarse detector summary remain fixed.

## Fixed measurement view

- Raw payload: `['event:e1:+', 'event:e2:-', 'event:e3:+', 'event:e4:-']`
- Measurement result: `plus=2;minus=2;balance=0`
- Coarse detector summary: `[{'field': 'detector_identity', 'value': 'detector:hbt-stack-a'}, {'field': 'run_session_id', 'value': 'run:2026-06-20:001'}, {'field': 'calibration_reference', 'value': 'calibration:cal-2026-06-20:signed'}, {'field': 'event_count', 'value': 4}, {'field': 'plus_count', 'value': 2}, {'field': 'minus_count', 'value': 2}]`

## Packet variants

| Packet | Changed packet fields | Verdict | Signature valid | Same raw/result/summary | Future operations | Removed vs reference |
| --- | --- | --- | --- | --- | --- | --- |
| `same_payload_reference_packet` | `[]` | `admissible` | `True` | `True` | `['audit_authority', 'bind_calibration', 'certify_packet', 'challenge_packet', 'publish_packet', 'read_immediate_result', 'reconstruct_event', 'retain_raw_payload', 'score_admissibility', 'use_for_detector_claim_review', 'verify_lineage']` | `[]` |
| `missing_provenance_same_payload` | `['provenance_chain', 'admissibility_tokens']` | `inadmissible` | `False` | `True` | `['read_immediate_result', 'retain_raw_payload']` | `['audit_authority', 'bind_calibration', 'certify_packet', 'challenge_packet', 'publish_packet', 'reconstruct_event', 'score_admissibility', 'use_for_detector_claim_review', 'verify_lineage']` |
| `authority_collapsed_same_payload` | `['authority_domains', 'admissibility_tokens']` | `inadmissible` | `True` | `True` | `['read_immediate_result', 'retain_raw_payload']` | `['audit_authority', 'bind_calibration', 'certify_packet', 'challenge_packet', 'publish_packet', 'reconstruct_event', 'score_admissibility', 'use_for_detector_claim_review', 'verify_lineage']` |
| `invalid_signature_same_payload` | `['signatures', 'admissibility_tokens']` | `inadmissible` | `False` | `True` | `['read_immediate_result', 'retain_raw_payload']` | `['audit_authority', 'bind_calibration', 'certify_packet', 'challenge_packet', 'publish_packet', 'reconstruct_event', 'score_admissibility', 'use_for_detector_claim_review', 'verify_lineage']` |
| `key_compromised_same_payload` | `['key_state']` | `inadmissible` | `True` | `True` | `['read_immediate_result', 'retain_raw_payload']` | `['audit_authority', 'bind_calibration', 'certify_packet', 'challenge_packet', 'publish_packet', 'reconstruct_event', 'score_admissibility', 'use_for_detector_claim_review', 'verify_lineage']` |
| `revoked_authority_same_payload` | `['revocation_status']` | `inadmissible` | `True` | `True` | `['read_immediate_result', 'retain_raw_payload']` | `['audit_authority', 'bind_calibration', 'certify_packet', 'challenge_packet', 'publish_packet', 'reconstruct_event', 'score_admissibility', 'use_for_detector_claim_review', 'verify_lineage']` |
| `publication_delayed_same_payload` | `['publication_status', 'admissibility_tokens']` | `inadmissible` | `True` | `True` | `['read_immediate_result', 'retain_raw_payload']` | `['audit_authority', 'bind_calibration', 'certify_packet', 'challenge_packet', 'publish_packet', 'reconstruct_event', 'score_admissibility', 'use_for_detector_claim_review', 'verify_lineage']` |
| `missing_witnesses_same_payload` | `['witness_references']` | `inadmissible` | `True` | `True` | `['read_immediate_result', 'retain_raw_payload']` | `['audit_authority', 'bind_calibration', 'certify_packet', 'challenge_packet', 'publish_packet', 'reconstruct_event', 'score_admissibility', 'use_for_detector_claim_review', 'verify_lineage']` |
| `missing_reconstruction_same_payload` | `['reconstruction_paths']` | `inadmissible` | `True` | `True` | `['read_immediate_result', 'retain_raw_payload']` | `['audit_authority', 'bind_calibration', 'certify_packet', 'challenge_packet', 'publish_packet', 'reconstruct_event', 'score_admissibility', 'use_for_detector_claim_review', 'verify_lineage']` |
| `open_challenge_same_payload` | `['admissibility_tokens', 'challenge_status']` | `withhold` | `True` | `True` | `['inspect_dispute', 'preserve_evidence', 'read_immediate_result', 'retain_raw_payload']` | `['audit_authority', 'bind_calibration', 'certify_packet', 'challenge_packet', 'publish_packet', 'reconstruct_event', 'score_admissibility', 'use_for_detector_claim_review', 'verify_lineage']` |

## What changed

Provenance completeness, authority separation, signature validity, key-compromise status, revocation status, publication timing, witness availability, reconstruction paths, and challenge state each remove future operations in at least one same-payload variant.

## What did not change

The raw rows, plus/minus measurement result, detector identity, run identifier, calibration reference, event count, and coarse plus/minus summary are identical across all T123 packet variants.

## Claim impact note

No Q1 or detector-physics promotion. T123 is detector evidence infrastructure: raw measurement sameness does not imply equal packet admissibility or equal future operation rights.

## Falsification condition

T123's same-payload FOA split is falsified if packet protocols declare that admissibility, reconstruction, challenge, certification, and claim-review rights are functions only of raw payload, immediate measurement result, and coarse detector summary. Such a protocol would also abandon the T78/T87/T97/T100/T121 evidence requirements.

## Open blocker

The audit is still schema-level. It must be integrated into the T97 dry-run packet and then populated by a real pre-registered detector deployment before any detector branch can be evaluated.

## Recommended next

Add a T97 packet fixture that emits the T123 same-payload variants with signed manifests, then require the real detector packet to report both immediate measurement results and FOA verdicts side by side.

## Claim ledger update

Q1B remains externally blocked and receives no empirical upgrade. T123 adds detector evidence infrastructure: same raw payload, same measurement result, and same coarse detector summary can still yield different admissibility and future operation availability when packet provenance, authority, signature, key, revocation, publication, witness, reconstruction, or challenge fields differ.
