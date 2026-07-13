# T548: APRD Cross-Family Prediction Stress Packet

## Target Claims

- S1 and TAF11 only as a source-law feeder branch.
- TAF4 only as a future finite-to-continuum beneficiary if a source-law route
  later survives without retuning.
- TAF8 only as a possible future shadow-protection feeder.
- No claim-ledger, Canon Index, canon-verdict, public-posture, North Star,
  external-publication, or cross-repo movement.

## Purpose

T547 found bounded held-out prediction for native APRD fixtures. T548 tests the
stricter cross-family burden: whether the frozen T547 predictor can assign APRD
debt for distinct native-candidate families before outcome labels and without
adding a family-specific rule.

The packet must pass:

- a known-family regression proving the T547 predictor still works on its own
  native family;
- distinct native-candidate family stress cases that honestly narrow if the
  frozen predictor has no family rule.

The packet must reject:

- manual family-rule injection after target selection;
- outcome-label leakage;
- proxy-label reading;
- hidden support change;
- cross-repo truth import;
- finite stress read as source-law or TAF4 movement.

## Success Criteria

1. T548 consumes the T547 held-out prediction verdict.
2. The known T547 family regression still predicts its APRD debt.
3. Distinct candidate families do not count as predicted merely because a new
   family rule could be injected.
4. No cross-family survivor is recorded without frozen-rule prediction.
5. All shortcut and governance controls reject.
6. No claim, canon, public-posture, North Star, external-publication, or
   cross-repo movement is made.

## Expected Result

`aprd_cross_family_stress_narrows_to_family_local_feeder`.

T548 should narrow APRD to a family-local feeder unless a distinct family clears
without retuning. If it narrows, TAF11 should reset route selection before any
finite-to-continuum or source-law reading.

## Reproduction

```bash
python -m models.t548_aprd_cross_family_prediction_stress_packet --write-results
python -m unittest tests.test_t548_aprd_cross_family_prediction_stress_packet -v
```
