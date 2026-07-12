# T537 Results: Source-Law Family And Falsifier Packet

## Verdict

- Verdict: `source_law_family_packet_selected_descent_obstruction_resolution_family`
- Source T536 verdict: `taf11_successor_route_selected_source_law_family_and_falsifier_packet`
- Source T536 selected routes: `t537_source_law_family_and_falsifier_packet`
- Selected family ids: `descent_obstruction_resolution_family`

## Spent Shapes Excluded From Selection

- `two_channel_receipt_product_order`
- `three_channel_receipt_product_order`
- `record_window_separation_order`
- `external_lorentzian_uv_reference_law`
- `t528_screen_conditioned_receipt_mixture`
- `posthoc_repaired_band_fit`

## Family Decisions

| family | outcome | selected? | role | missing requirements | next packet | reason |
| --- | --- | :---: | --- | --- | --- | --- |
| `descent_obstruction_resolution_family` | `SELECTED_FOR_EXECUTION` | True | `track_1_next_family` | none | `t538_descent_obstruction_resolution_source_law_packet` | The family is finality-domain native, new relative to spent shapes, computable without target import, and carries an explicit falsifier. |
| `stabilization_certificate_filtration_family` | `REVIEW_ONLY` | False | `underdeclared_family` | executable_next_packet_specific | `none` | The family is useful context but lacks one or more T537 execution requirements. |
| `record_window_separation_rescue_family` | `REJECTED_DUPLICATE` | False | `spent` | new_relative_to_spent_shapes, executable_next_packet_specific, no_spent_shape_repeat | `none` | The family repeats a shape already spent by T532/T534. |
| `ordering_fraction_target_fit_family` | `BLOCKED_TARGET_IMPORT` | False | `blocked` | finality_domain_family, new_relative_to_spent_shapes, independent_naturality, computable_without_target_import, executable_next_packet_specific, later_burdens_named, no_target_density_fit | `none` | The family chooses the law from the target statistic. |
| `lorentzian_reference_sampler_family` | `BLOCKED_TARGET_IMPORT` | False | `blocked` | finality_domain_family, new_relative_to_spent_shapes, independent_naturality, computable_without_target_import, executable_next_packet_specific, later_burdens_named, no_lorentzian_reference_import | `none` | The family imports the target Lorentzian reference law. |
| `real_taf10_data_packet_wait_family` | `PAUSED_TRACK_2` | False | `track_2_waiting` | finality_domain_family, source_variables_declared, independent_naturality, computable_without_target_import, executable_next_packet_specific, hostile_controls_named, later_burdens_named, not_blocked_on_real_data_packet, track_2_does_not_replace_track_1 | `none` | T535 found no real data-bearing packet, and Track 2 cannot replace Track 1. |

## Selected Family Contract

- Family: `descent_obstruction_resolution_family`
- Source variables: `local_record_cover`, `restriction_maps`, `compatible_local_sections`, `descent_obstruction_witness`, `allowed_refinement_steps`, `resolution_depth`
- Predeclared falsifier: Reject if the relation is not invariant under cover relabeling and restriction-map isomorphism, if it collapses to total-chain or antichain controls, or if any density target or Lorentzian coordinate is needed to choose the relation.

## Hostile Controls

| control | blocks families | reason |
| --- | --- | --- |
| `isomorphic_cover_relabel_control` | none | A selected family must give the same decision under cover relabeling and restriction-map isomorphism. |
| `total_chain_and_antichain_collapse_control` | none | A selected family must not succeed only by collapsing every fixture to a total chain or an antichain. |
| `spent_shape_replay_control` | `record_window_separation_rescue_family` | Spent finite-generator and endpoint-window shapes do not re-enter TAF11. |
| `target_import_control` | `ordering_fraction_target_fit_family`, `lorentzian_reference_sampler_family` | A source law must be chosen before target statistics or Lorentzian coordinates are read. |

## Claim Labels

- `COMPUTED` confidence `high`: T536 is consumed as selecting the source-law family and falsifier packet route.
- `COMPUTED` confidence `high`: Exactly one T537 family is selected: descent_obstruction_resolution_family.
- `COMPUTED` confidence `high`: Spent-shape replay, target-density fitting, Lorentzian reference import, and Track-2 replacement are rejected or paused: record_window_separation_rescue_family, ordering_fraction_target_fit_family, lorentzian_reference_sampler_family, real_taf10_data_packet_wait_family.
- `ARGUED` confidence `medium`: The descent-obstruction family is the best next source-law candidate because it uses record-cover, restriction, and obstruction-resolution data already native to the TaF proof program while remaining falsifiable before target import.

## Recommended Next

Run t538_descent_obstruction_resolution_source_law_packet. It should instantiate finite record-cover fixtures for the descent-obstruction resolution family, compute the obstruction-resolution relation before seeing any target ordering statistic, and reject the family if it collapses under the predeclared hostile controls.

## S1 Update

S1 remains `requires_added_assumption`. T537 selects one computable source-law family for the next packet and supplies no S1 evidence.

## Claim Ledger Update

No claim-ledger update is earned. T537 is TAF11 work selection and source-family scoping only; it leaves claim rows, Canon Index tiers, and canon verdicts unchanged.

## Not Claimed

T537 does not establish a source law, derive spacetime, prove manifoldlikeness, repair T528, reverse T223, unpause the S1 finite-generator route, promote S1, change claim status, change canon, change public posture, authorize external publication, or move cross-repo truth. It is a Track-1 source-law family selection packet only.
