# T133 Results: Detector Packet Tiered Minimality

## Tier cores

- Raw identity fields: `['detector_identity', 'run_session_id', 'causal_ordering_data', 'raw_measurement_payload', 'calibration_reference']`
- Provisional admission fields: `['detector_identity', 'run_session_id', 'causal_ordering_data', 'raw_measurement_payload', 'calibration_reference', 'provenance_chain', 'signatures', 'authority_domains', 'publication_status', 'revocation_status', 'key_state', 'admissibility_tokens']`
- Claim-review extension fields: `['witness_references', 'reconstruction_paths', 'challenge_status']`

## Packet audits

| Packet | Changed fields | Raw preserved | Provisionally admissible | Claim-review ready | Strict T121 verdict | Strict-only fields triggered |
| --- | --- | --- | --- | --- | --- | --- |
| `same_payload_reference_packet` | `[]` | `True` | `True` | `True` | `admissible` | `[]` |
| `missing_provenance_same_payload` | `['provenance_chain', 'admissibility_tokens']` | `True` | `False` | `False` | `inadmissible` | `[]` |
| `authority_collapsed_same_payload` | `['authority_domains', 'admissibility_tokens']` | `True` | `False` | `False` | `inadmissible` | `[]` |
| `invalid_signature_same_payload` | `['signatures', 'admissibility_tokens']` | `True` | `False` | `False` | `inadmissible` | `[]` |
| `key_compromised_same_payload` | `['key_state']` | `True` | `False` | `False` | `inadmissible` | `[]` |
| `revoked_authority_same_payload` | `['revocation_status']` | `True` | `False` | `False` | `inadmissible` | `[]` |
| `publication_delayed_same_payload` | `['publication_status', 'admissibility_tokens']` | `True` | `False` | `False` | `inadmissible` | `[]` |
| `missing_witnesses_same_payload` | `['witness_references']` | `True` | `True` | `False` | `inadmissible` | `['witness_references']` |
| `missing_reconstruction_same_payload` | `['reconstruction_paths']` | `True` | `True` | `False` | `inadmissible` | `['reconstruction_paths']` |
| `open_challenge_same_payload` | `['admissibility_tokens', 'challenge_status']` | `True` | `True` | `False` | `withhold` | `['challenge_status']` |

## Strongest claim

The current detector packet burden is tiered, not flat. Under the same-payload witness family, provenance/signature/authority/publication/revocation/key-state fields form the provisional admission core, while witness references, reconstruction paths, and dispute state are additional claim-review requirements.

## Weakened claim

T121's packet-wide strictness is too coarse as a description of what each field does. The current executable route should not say that every packet field is equally needed for the first admission decision. Some fields gate stronger review and future operations, not raw evidence preservation or provisional intake.

## Falsification condition

T133 fails if witness references, reconstruction paths, and challenge state can be removed while keeping full detector-claim review rights, or if provenance, signature, authority, publication, revocation, and key-state failures no longer block even provisional packet admission.

## Open blocker

The tier split is still a schema audit over synthetic same-payload packets. A real T97 dry-run packet must publish both provisional admission and claim-review readiness before the detector branch can present itself as a reproducible evidence protocol.

## Recommended next

Refactor the T97 dry-run packet into explicit tier outputs: raw evidence preserved, provisionally admitted, and claim-review ready. Then require any real deployment to freeze which tier is being claimed before event collection.

## Claim ledger update

Q1B remains externally blocked. T133 sharpens the packet burden: detector evidence now has a smaller provisional-admission core plus a stricter claim-review extension. This weakens any flat reading that treats every packet field as equally necessary at the first admissibility step.
