# T418 - Schwarzschild Horizon Access-Profile Screen - Results v0.1

- **Artifact:** `T418-schwarzschild-horizon-access-profile-screen-v0.1`
- **Status:** `implemented_guardrail_no_claim_promotion`
- **Claim ledger update:** none; no claim promotion
- **North Star / public posture update:** none

## Verdict

T418 supplies a GR causal-accessibility absorber screen: same exterior Schwarzschild shadow plus different interior records does not create an exterior capability split; comparing to an infalling or full-slice capability is a cross-profile mismatch unless declared.

## Horizon Geometry Audit

| Probe | dr/dv | Trace classification | Escapes exterior cutoff? |
| --- | ---: | --- | --- |
| inside r=1.5 | -0.16666666666666663 | `hits_singularity_before_escape` | `False` |
| horizon r=2.0 | 0.0 | `horizon_generator_no_escape` | `False` |
| outside r=3.0 | 0.16666666666666669 | `reaches_exterior_cutoff` | `True` |

## Access-Profile Alignment Audit

- Exterior projections equal: `True`
- Aligned exterior capabilities equal: `True`
- Cross-profile infalling/full-slice capability splits: `True`
- Alignment verdict: `no_same_profile_projection_failure`
- Mismatch verdict: `cross_profile_mismatch_absorbed_by_horizon_access_profile`
- Residue label: `absorbed_by_schwarzschild_causal_access_and_profile_alignment`

## Positive Control

- Both outside signals reach exterior: `True`
- Exterior profile distinguishes outside records: `True`
- Residue label: `ordinary_exterior_causal_record_access`
- Reason: The guard has teeth: records emitted outside the horizon can reach the exterior cutoff and are ordinary causal record access.

## Absorber Audit

### schwarzschild_event_horizon

- Status: `absorbs`
- Reason: Inside the horizon, outgoing radial null directions do not increase through r_s. Exterior non-recovery is ordinary GR causal-access structure in this model.

### access_profile_alignment

- Status: `absorbs`
- Reason: Exterior projection compared to exterior capability does not split. The split appears only when the capability is silently moved to an infalling/full-slice profile.

### black_hole_information_claim

- Status: `not_attempted`
- Reason: The artifact does not model Hawking radiation, QFT algebras, Page curves, holography, or evaporation.

## Recommended Next

- Use T418 as a horizon/access-profile guardrail for future B1/S1/R1 screens.
- Do not cite interior-record recovery by a non-exterior profile as exterior projection residue.
- A stronger GR-facing artifact would need matched access profiles plus a native black-hole information or algebraic-QFT capability object declared up front.

## Falsification Condition

The screen would fail in TaF's favor only if two states matched the Schwarzschild exterior geometry, observer access profile, received record algebra, and task boundary, yet split an exterior-native capability not expressible as standard horizon causal access.
