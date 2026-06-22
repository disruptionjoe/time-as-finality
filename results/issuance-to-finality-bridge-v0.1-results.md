# T172 Results: Issuance-To-Finality Bridge

## Summary

Finality can be a sound observer-side reflection of a source realization order only when record generation, access, cadence, and gluing data are fixed. The same finite TaF readout can lose hidden source order or source-measure data; cadence and access can change apparent finality without changing source order; and unglued local records do not determine a global realization order.

## Audit Table

| Fixture | Same source order | Same records | Same readout | Same mu | Source split | Readout split | Verdict |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `sound_record_generation_reflection_control` | `True` | `True` | `True` | `True` | `False` | `False` | `positive_source_readout_reflection` |
| `same_issuance_different_cadence` | `True` | `False` | `True` | `True` | `False` | `False` | `cadence_boundary_not_source_arrow` |
| `same_records_different_hidden_issuance` | `False` | `True` | `True` | `True` | `True` | `False` | `source_capability_lost_by_taf_readout` |
| `same_issuance_records_different_mu` | `True` | `True` | `True` | `False` | `True` | `False` | `mu_invisible_to_taf_readout` |
| `nonmonotone_access_loss` | `True` | `True` | `True` | `True` | `False` | `False` | `access_boundary_not_source_arrow` |
| `gluing_failure_global_order_not_assumed` | `False` | `True` | `True` | `True` | `True` | `False` | `gluing_failure_not_global_order` |

## sound_record_generation_reflection_control

- Kind: `positive_reflection_control`
- Task: `source_order_reconstruction`
- Same source order: `True`
- Same observer records: `True`
- Same TaF readout edges: `True`
- Same `mu`: `True`
- Finality profile split: `False`
- Source capability split: `False`
- TaF readout split: `False`
- Left source order recovered: `True`
- Right source order recovered: `True`
- Left access scores: `[(0, 1), (1, 2), (2, 3)]`
- Right access scores: `[(0, 1), (1, 2), (2, 3)]`
- Left access monotone: `True`
- Right access monotone: `True`
- H7 source-arrow upgrade candidate: `False`
- Verdict: `positive_source_readout_reflection`
- Interpretation: The observer record chain is sound for visible source order. This is a reflection control, not evidence that finality generated the source order.

## same_issuance_different_cadence

- Kind: `cadence_boundary`
- Task: `source_order_reconstruction`
- Same source order: `True`
- Same observer records: `False`
- Same TaF readout edges: `True`
- Same `mu`: `True`
- Finality profile split: `True`
- Source capability split: `False`
- TaF readout split: `False`
- Left source order recovered: `True`
- Right source order recovered: `True`
- Left access scores: `[(0, 1), (1, 2), (2, 3)]`
- Right access scores: `[(0, 1), (2, 2), (4, 3)]`
- Left access monotone: `True`
- Right access monotone: `True`
- H7 source-arrow upgrade candidate: `False`
- Verdict: `cadence_boundary_not_source_arrow`
- Interpretation: The source order and readout order are unchanged while the local finality profile changes with observer cadence. The apparent timing is observer-side.

## same_records_different_hidden_issuance

- Kind: `hidden_source_loss`
- Task: `source_order_reconstruction`
- Same source order: `False`
- Same observer records: `True`
- Same TaF readout edges: `True`
- Same `mu`: `True`
- Finality profile split: `False`
- Source capability split: `True`
- TaF readout split: `False`
- Left source order recovered: `True`
- Right source order recovered: `True`
- Left access scores: `[(0, 1), (1, 2)]`
- Right access scores: `[(0, 1), (1, 2)]`
- Left access monotone: `True`
- Right access monotone: `True`
- H7 source-arrow upgrade candidate: `False`
- Verdict: `source_capability_lost_by_taf_readout`
- Interpretation: Identical records and TaF readout edges hide a difference in source realization order. The source capability does not factor through the readout.

## same_issuance_records_different_mu

- Kind: `mu_invisible_loss`
- Task: `source_mu_profile`
- Same source order: `True`
- Same observer records: `True`
- Same TaF readout edges: `True`
- Same `mu`: `False`
- Finality profile split: `False`
- Source capability split: `True`
- TaF readout split: `False`
- Left source order recovered: `True`
- Right source order recovered: `True`
- Left access scores: `[(0, 1), (1, 3)]`
- Right access scores: `[(0, 1), (1, 3)]`
- Left access monotone: `True`
- Right access monotone: `True`
- H7 source-arrow upgrade candidate: `False`
- Verdict: `mu_invisible_to_taf_readout`
- Interpretation: The same issuance order and observer records can carry different source mu data. Mu is decorative for plain finality order, but it is lost if the declared task needs source-measure information.

## nonmonotone_access_loss

- Kind: `access_boundary`
- Task: `source_order_reconstruction`
- Same source order: `True`
- Same observer records: `True`
- Same TaF readout edges: `True`
- Same `mu`: `True`
- Finality profile split: `True`
- Source capability split: `False`
- TaF readout split: `False`
- Left source order recovered: `True`
- Right source order recovered: `True`
- Left access scores: `[(0, 1), (1, 2), (2, 2), (3, 3)]`
- Right access scores: `[(0, 1), (1, 2), (2, 1), (3, 2)]`
- Left access monotone: `True`
- Right access monotone: `False`
- H7 source-arrow upgrade candidate: `False`
- Verdict: `access_boundary_not_source_arrow`
- Interpretation: The source order is unchanged while accessible finality support drops. The nonmonotonicity is an observer-boundary effect, not a source-arrow result.

## gluing_failure_global_order_not_assumed

- Kind: `gluing_failure`
- Task: `source_order_reconstruction`
- Same source order: `False`
- Same observer records: `True`
- Same TaF readout edges: `True`
- Same `mu`: `True`
- Finality profile split: `False`
- Source capability split: `True`
- TaF readout split: `False`
- Left source order recovered: `False`
- Right source order recovered: `False`
- Left access scores: `[(0, 2)]`
- Right access scores: `[(0, 2)]`
- Left access monotone: `True`
- Right access monotone: `True`
- H7 source-arrow upgrade candidate: `False`
- Verdict: `gluing_failure_not_global_order`
- Interpretation: The same unglued local records are compatible with different global source orders. Global order must be reconstructed by declared gluing data, not assumed.

## Reflection Controls

- `sound_record_generation_reflection_control`

## Cadence Boundaries

- `same_issuance_different_cadence`

## Source Capability Losses

- `same_records_different_hidden_issuance`

## Mu-Invisible Losses

- `same_issuance_records_different_mu`

## Access Boundary Cases

- `nonmonotone_access_loss`

## Gluing Failures

- `gluing_failure_global_order_not_assumed`

## H7 Arrow Candidates

None.

## What Improved

T172 turns the Temporal Issuance bridge into an executable projection-sufficiency audit. It supplies a positive reflection control plus hostile fixtures for cadence, hidden issuance, mu, access loss, and gluing.

## What Weakened

This weakens any H7 or TaF prose that reads finality as generating source-level temporal direction. At most, finality is currently a typed observer readout or certificate of source order under declared soundness and reconstruction conditions.

## Falsification Condition

The bridge earns a stronger claim only if a non-gerrymandered source system and observer projection prove that TaF finality preserves the declared source capability across cadence changes, hidden issuance alternatives, mu-sensitive tasks, access loss, and gluing ambiguity without importing ordinary time, entropy, information growth, or a preferred global frontier.

## H7 Update

Add T172 to H7 as a source/readout recast: H7 remains weakened_conditional. Finality-induced direction should be treated as an observer-side reflection or factorization test, not as source-level arrow generation.

## Claim Ledger Update

T172 tests the Temporal Issuance bridge. A sound record chain can reflect visible source order, but same-readout hidden issuance, mu-sensitive source tasks, nonmonotone access, and missing gluing all block finality-alone source-arrow readings.

## Open Blocker

No typed source dynamics for issuance order or mu has yet survived absorber tests against ordinary causal order, entropy, information growth, record reconstruction, or a hidden global frontier.

## Suggested Next

Run an absorber map for Temporal Issuance against causal sets, block-universe causal order, stochastic thermodynamics, and information-theoretic growth before adding richer bridge models.

## Not Claimed

T172 does not import Temporal Issuance as true, does not derive the thermodynamic arrow, does not replace physical time, and does not prove that records create source realization order.
