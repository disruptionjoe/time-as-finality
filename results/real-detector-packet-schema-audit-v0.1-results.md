# T121 Results: Real Detector Packet Schema Audit

## Schema fields

`detector_identity`, `run_session_id`, `causal_ordering_data`, `raw_measurement_payload`, `calibration_reference`, `provenance_chain`, `signatures`, `authority_domains`, `publication_status`, `revocation_status`, `key_state`, `witness_references`, `reconstruction_paths`, `admissibility_tokens`, `challenge_status`

## Packet cases

| Packet | Raw payload valid | Verdict | Failures | Future operations | Missing schema requirements |
| --- | --- | --- | --- | --- | --- |
| `valid_packet` | `True` | `admissible` | `[]` | `['audit_authority', 'bind_calibration', 'challenge_packet', 'publish_packet', 'reconstruct_event', 'retain_raw_payload', 'score_admissibility', 'use_for_detector_claim_review', 'verify_lineage']` | `[]` |
| `missing_provenance` | `True` | `inadmissible` | `['missing_strict_packet_fields', 'missing_provenance_chain', 'missing_admissibility_tokens']` | `['retain_raw_payload']` | `['strict_packet_fields_must_be_present']` |
| `key_compromised` | `True` | `inadmissible` | `['signing_key_compromised']` | `['retain_raw_payload']` | `['key-compromise and rotation-continuity state must be explicit']` |
| `revoked_authority` | `True` | `inadmissible` | `['authority_or_packet_revoked']` | `['retain_raw_payload']` | `['revocation registry and check time must be part of packet']` |
| `publication_delayed` | `True` | `inadmissible` | `['packet_not_published_before_analysis', 'missing_admissibility_tokens']` | `['retain_raw_payload']` | `[]` |
| `authority_domains_collapsed` | `True` | `inadmissible` | `['authority_domains_collapsed', 'missing_admissibility_tokens']` | `['retain_raw_payload']` | `[]` |
| `valid_raw_data_inadmissible_packet` | `True` | `inadmissible` | `['missing_strict_packet_fields', 'missing_signatures', 'missing_witness_references', 'missing_reconstruction_paths', 'missing_admissibility_tokens']` | `['retain_raw_payload']` | `['strict_packet_fields_must_be_present']` |
| `same_raw_data_reduced_future_rights` | `True` | `withhold` | `['missing_admissibility_tokens', 'open_challenge_or_dispute']` | `['inspect_dispute', 'preserve_evidence', 'retain_raw_payload']` | `['challenge/dispute lifecycle must gate future use']` |

## Strongest claim

Before detector admissibility can be reasoned about, the evidence object must include raw payload plus provenance, authority, publication, revocation, key-state, witness, reconstruction, token, and dispute fields. Valid raw data alone is insufficient.

## Fields strictly necessary

All declared schema fields are strictly necessary for this minimal packet because each supports either raw-payload identity/order, evidence admissibility, or future operations over the packet.

## Failures changing admissibility

Missing provenance, compromised key, revoked authority, delayed publication, collapsed authority domains, missing signatures, missing witnesses, missing reconstruction paths, missing tokens, and open disputes all block or withhold admissibility.

## Failures changing future operation availability

Every negative case reduces future operations. The clearest split is same raw data with open dispute: raw retention remains available, but claim review, lineage verification, challenge closure, and detector-claim use are withheld.

## Handled by existing protocol artifacts

Provenance, signatures, publication, authority separation, witness references, reconstruction paths, and admissibility tokens are mostly handled by T78/T87/T97/T100. Revocation status, key-compromise state, and challenge lifecycle need explicit packet-level fields.

## Missing schema requirements

The audit reveals three schema requirements not cleanly owned by the older raw-log artifacts: revocation registry/check time, key rotation and compromise continuity, and challenge/dispute lifecycle state.

## Claim impact recommendation

No Q1 or detector-physics promotion. Treat T121 as infrastructure: a minimal detector evidence packet object required before D1 scoring or detector-branch admissibility claims.

## Recommended next

Integrate this packet schema with the T97 dry-run packet and require revocation, key-continuity, and dispute-state checks before any future real detector packet is scored.
