# T539 Results: Resolution-Depth Generator Packet

## Verdict

- Verdict: `descent_obstruction_family_retired_programmable_rank_generator`
- Source T538 verdict: `descent_obstruction_family_narrowed_requires_depth_generator`
- Selected family: `descent_obstruction_resolution_family`
- Family status: `RETIRED_CURRENT_ROUTE_REQUIRES_NEW_SOURCE_LAW_FAMILY`
- Target import used: `False`

## Generator Recipe

Compute cover ranks from restriction maps; assign each record its first compatible local-section rank; generate d(x, y) from the source record's rank; declare x < y when d(x, y) < d(y, x).

## Fixture Evaluations

| fixture | shape | role | ranks | comparable pairs | expected? | partial order? | source-law evidence? | failure mode |
| --- | --- | --- | --- | ---: | :---: | :---: | :---: | --- |
| `generated_antichain_control` | `antichain` | `hostile_antichain_control` | a:0, b:0, c:0, d:0 | 0/6 | True | True | False | `programmable_scalar_rank_channel` |
| `generated_total_chain_control` | `total_chain` | `hostile_total_chain_control` | a:0, b:1, c:2, d:3 | 6/6 | True | True | False | `programmable_scalar_rank_channel` |
| `generated_diamond_probe` | `diamond` | `rank_programmability_probe` | a:0, b:1, c:1, d:2 | 5/6 | True | True | False | `programmable_scalar_rank_channel` |
| `generated_fork_probe` | `fork` | `rank_programmability_probe` | a:0, b:0, c:1, d:1 | 4/6 | True | True | False | `programmable_scalar_rank_channel` |

## Hostile Controls

| control | passed? | reason |
| --- | :---: | --- |
| `no_pairwise_depth_table_control` | True | All ordered depths are generated from activation ranks rather than supplied as pairwise table entries. |
| `record_and_cover_relabel_control` | True | Renaming records and cover nodes preserves the generated diamond relation. |
| `scalar_rank_programmability_control` | True | The same generator realizes antichain, total-chain, diamond, and fork shapes by changing compatible local-section ranks; this is diagnostic programmability, not source-law evidence. |
| `no_source_law_promotion_control` | True | The generated-depth packet remains a stress test. It does not promote hostile controls or rank-programmed fixtures into source-law evidence. |
| `t538_retirement_trigger_control` | True | T538 required a nonprogrammatic depth generator; T539 found only a programmable rank generator for the current route. |

## Strongest Reading

T539 removes the pairwise depth table, but the resulting generator collapses to a programmable scalar rank. The same source-cover schema can realize antichain, total-chain, diamond, and fork relations by moving compatible local sections across ranks. That is a useful negative result: the current descent-obstruction family route should be retired rather than wrapped in another router.

## Recommended Next

Retire the current descent-obstruction resolution family route. Re-rank TAF11 against TAF8 and route the next swing to the cross-domain shadow-protection theorem target unless a genuinely new, non-rank source-law family is proposed.

## Claim Labels

- `COMPUTED` confidence `high`: T538 is consumed as requiring a resolution-depth generator before the descent-obstruction family can count as a source law.
- `COMPUTED` confidence `high`: The generated-depth recipe uses no pairwise depth table and realizes these finite relation shapes: antichain, total_chain, diamond, fork.
- `COMPUTED` confidence `high`: All T539 controls pass as diagnostics: no_pairwise_depth_table_control, record_and_cover_relabel_control, scalar_rank_programmability_control, no_source_law_promotion_control, t538_retirement_trigger_control.
- `ARGUED` confidence `medium`: The generator reduces to a scalar activation-rank channel. That is too programmable to rescue the current descent-obstruction source-law family.

## S1 Update

S1 remains `requires_added_assumption`. T539 supplies no source law and therefore no S1 evidence.

## Claim Ledger Update

No claim-ledger update is earned. T539 is a negative generator stress test and leaves claim rows, Canon Index tiers, and canon verdicts unchanged.

## Not Claimed

T539 does not establish a source law, derive spacetime, prove manifoldlikeness, repair T528, reverse T223, unpause the S1 finite-generator route, promote S1, change claim status, change canon, change public posture, authorize external publication, or move cross-repo truth. It is a Track-1 source-law generator stress test only.
