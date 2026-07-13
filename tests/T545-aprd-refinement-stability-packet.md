# T545: APRD Refinement Stability Packet

## Target Claims

- S1 and TAF11 only as a source-law feeder branch.
- TAF4 only as a future finite-to-continuum beneficiary if functorial behavior
  is later earned.
- TAF8 only as a possible future shadow-protection feeder.
- No claim-ledger, Canon Index, canon-verdict, public-posture, North Star,
  external-publication, or cross-repo movement.

## Purpose

T544 found finite minimal non-detector APRD survivors. T545 tests whether those
survivor debt sets remain stable under:

- harmless refinement of the presentation;
- harmless relabeling;
- declared support-preserving restriction maps.

The packet must also reject:

- support loss hidden as relabeling;
- padded debt atoms;
- scalar-rank replacement;
- non-harmless restriction read as theorem evidence.

## Success Criteria

1. T545 consumes the T544 APRD survivors and verdict.
2. Harmless refinement preserves canonical APRD debt labels.
3. Harmless relabeling preserves canonical APRD debt labels.
4. Declared support-preserving restriction preserves canonical APRD debt labels.
5. Non-harmless support-losing restriction narrows the object rather than
   promoting it.
6. Hidden support change, padded debt, unstable harmless relabeling, and
   scalar-rank replacement reject.
7. No claim, canon, public-posture, North Star, external-publication, or
   cross-repo movement is made.

## Expected Result

`aprd_refinement_stability_gate_clears_harmless_changes`.

T545 should keep APRD alive as a finite source-law feeder, not a source law.
The next useful packet should test functorial naturality across native
morphisms and composites.

## Reproduction

```bash
python -m models.t545_aprd_refinement_stability_packet --write-results
python -m unittest tests.test_t545_aprd_refinement_stability_packet -v
```
