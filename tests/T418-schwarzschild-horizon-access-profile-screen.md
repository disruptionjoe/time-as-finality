# T418 - Schwarzschild Horizon Access-Profile Screen

## Route

Capability Projection / GR causal accessibility / access-profile alignment.

## Target Claims

- [R1: Relativity And No Global Commit Order](../claims/R1-relativity-no-global-commit-order.md)
- [S1: Spacetime As Consensus Envelope](../claims/S1-spacetime-consensus-envelope.md)
- [B1: Black Holes As Finality-Domain Boundaries](../claims/B1-black-holes-finality-boundaries.md)
- Method guardrail from [Access-Profile Alignment Lemma v0.1](../technical-reports/TECHNICAL-REPORT-access-profile-alignment-lemma-v0.1.md)

## Question

When the observer is a stationary exterior Schwarzschild observer, does a pair
with the same exterior shadow but different interior record create an
exterior-native capability split?

## Setup

Use the radial null structure of Schwarzschild geometry in ingoing
Eddington-Finkelstein coordinates:

```text
dr/dv = (1/2) * (1 - r_s / r)
```

with `r_s = 2M = 2`.

The fixtures are:

1. `horizon_geometry_audit`
   Checks that outgoing radial null directions move outward outside the horizon,
   generate the horizon at `r = r_s`, and move inward inside the horizon.
2. `same_exterior_shadow_different_interior_record`
   Two states have the same mass, horizon radius, and exterior log, but different
   interior records at `r < r_s`.
3. `outside_signal_positive_control`
   Two outside records at `r > r_s` reach the exterior cutoff and are ordinary
   exterior causal record access.

## Success Criteria

- The inside-horizon outgoing null trace does not cross outward through the
  horizon or reach the exterior cutoff.
- The outside-horizon outgoing null trace reaches the exterior cutoff.
- The two interior-record states have equal exterior projection.
- Exterior projection compared to exterior capability has no split.
- Exterior projection compared to an infalling/full-slice capability splits and
  is classified as an access-profile mismatch.
- The outside-signal positive control is distinguishable by the exterior profile.

## Failure Criteria

- The fixture treats an interior record as exterior-recoverable without changing
  the access profile.
- The artifact compares `pi_exterior` to `Cap_infalling` without declaring the
  profile mismatch.
- The event horizon is treated as TaF residue rather than standard GR causal
  access in this simple screen.
- The artifact makes black-hole information, QFT, holography, evaporation, or
  semiclassical gravity claims.

## Claim Impact

No claim-ledger movement.

T418 is a guardrail and absorber screen. It says:

```text
same exterior Schwarzschild shadow + different interior record
does not by itself create an exterior-native projection-sufficiency failure.
```

The apparent split appears only when the capability is silently moved to an
infalling/full-slice profile.

## Reproduction

```bash
python -m pytest tests/test_schwarzschild_horizon_access_profile_screen.py -q
python -m models.run_t418
```
