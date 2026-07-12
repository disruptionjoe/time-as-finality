# T538 Results: Descent-Obstruction Resolution Source-Law Packet

## Verdict

- Verdict: `descent_obstruction_family_narrowed_requires_depth_generator`
- Source T537 verdict: `source_law_family_packet_selected_descent_obstruction_resolution_family`
- Selected family: `descent_obstruction_resolution_family`
- Family status: `NARROWED_REQUIRES_RESOLUTION_DEPTH_GENERATOR`
- Target import used: `False`

## Recipe

Compute x < y from ordered resolution depths by the rule d(x, y) < d(y, x), using only finite record-cover variables.

## Fixture Evaluations

| fixture | shape | role | comparable pairs | realizes intended? | partial order? | source-law evidence? |
| --- | --- | --- | ---: | :---: | :---: | :---: |
| `antichain_control` | `antichain` | `hostile_antichain_control` | 0/6 | True | True | False |
| `total_chain_control` | `total_chain` | `hostile_total_chain_control` | 6/6 | True | True | False |
| `diamond_programming_fixture` | `diamond` | `programmability_probe` | 5/6 | True | True | False |
| `fork_programming_fixture` | `fork` | `programmability_probe` | 4/6 | True | True | False |

## Hostile Controls

| control | passed? | reason |
| --- | :---: | --- |
| `isomorphic_cover_relabel_control` | True | The computed relation is invariant under record and cover relabeling for the nondegenerate fixture. |
| `restriction_map_isomorphism_control` | True | Renaming cover nodes preserves the relation because the first packet depends only on supplied ordered depths. This passes the shallow isomorphism check but exposes underconstraint. |
| `total_chain_and_antichain_not_promoted_control` | True | Total-chain and antichain controls are computed but not promoted into source-law evidence. |
| `free_depth_programmability_control` | True | Free ordered resolution depths realize several incompatible strict partial-order shapes, so a depth generator is still missing. |

## Strongest Reading

The descent-obstruction resolution family survives the shallow relabeling and no-target-import checks, but the first computable form is underconstrained. Free ordered resolution depths can program antichain, total-chain, diamond, and fork relations. That means the current packet does not yet supply a source law.

## Recommended Next

Run T539 as a resolution-depth generator packet. It must derive ordered depths from local record-cover, restriction-map, and compatible-section data rather than accepting pairwise depths as free inputs. If no nonprogrammatic generator exists, retire this source-law family and re-rank TAF11 against TAF8.

## Claim Labels

- `COMPUTED` confidence `high`: T537 is consumed as selecting the descent_obstruction_resolution_family for T538.
- `COMPUTED` confidence `high`: The ordered-depth recipe realizes these finite relation shapes: antichain, total_chain, diamond, fork.
- `COMPUTED` confidence `high`: All hostile controls pass as diagnostics: isomorphic_cover_relabel_control, restriction_map_isomorphism_control, total_chain_and_antichain_not_promoted_control, free_depth_programmability_control.
- `ARGUED` confidence `medium`: Passing relabeling controls is not enough for a source law because the current packet accepts ordered resolution depths as free inputs. The family needs a generator for those depths.

## S1 Update

S1 remains `requires_added_assumption`. T538 narrows the selected TAF11 family and supplies no S1 evidence.

## Claim Ledger Update

No claim-ledger update is earned. T538 leaves claim rows, Canon Index tiers, and canon verdicts unchanged.

## Not Claimed

T538 does not establish a source law, derive spacetime, prove manifoldlikeness, repair T528, reverse T223, unpause the S1 finite-generator route, promote S1, change claim status, change canon, change public posture, authorize external publication, or move cross-repo truth. It is a Track-1 source-law stress test only.
