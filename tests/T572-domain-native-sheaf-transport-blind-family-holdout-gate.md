# T572: Domain-Native Sheaf Transport Blind-Family Holdout Gate

## Purpose

T572 consumes T571's selected burden and freezes the T570/T571 role-level
semantic generator before evaluating a predeclared blind family withheld from
the known admitted-family panel.

## Executable Artifact

- Model: `models/t572_domain_native_sheaf_transport_blind_family_holdout_gate.py`
- Test: `tests/test_t572_domain_native_sheaf_transport_blind_family_holdout_gate.py`
- Results:
  - `results/T572-domain-native-sheaf-transport-blind-family-holdout-gate-v0.1.json`
  - `results/T572-domain-native-sheaf-transport-blind-family-holdout-gate-v0.1-results.md`

## Result

Status: implemented / review-only.

The holdout contract predeclares
`settlement_attestation_blind_family`, which was absent from the T570/T571
admitted-family panel, before evaluation.

It admits one blind-family survivor:

- `settlement_attestation_blind_survivor`.

It rejects five controls:

- `blind_family_calibration_replay_falsifier`;
- `blind_family_target_import_falsifier`;
- `blind_family_optional_payload_falsifier`;
- `blind_family_missing_transport_square_falsifier`;
- `blind_family_foreign_truth_falsifier`.

This strengthens the TAF11 route by showing that the frozen generator predicts
one withheld family without family replay, target import, optional payload,
missing transport square, Observerse/APRD replay, or cross-repo truth import.
It remains review-only. It does not earn public source-law status,
claim-ledger movement, Canon Index movement, canon-verdict movement,
public-posture movement, TAF4 movement, TAF8 execution, S1 movement, external
publication, or cross-repo truth movement.

## Next Burden

T572 names the next executable TAF11 burden:
`t573_domain_native_sheaf_transport_adversarial_blind_family_holdout_gate`.

That packet should turn the blind-family success into adversarial holdout
pressure by changing the blind family's surface genre again while preserving
the frozen source roles, absorber boundaries, and semantic requirements.
