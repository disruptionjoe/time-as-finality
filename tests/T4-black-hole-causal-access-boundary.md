# T4: Black-Hole Causal Access Boundary

## Target Claims

- [B1: Black Holes As Finality-Domain Boundaries](../claims/B1-black-holes-finality-boundaries.md)
- [G2: Not A Replacement Theory](../guardrails/G2-not-a-replacement-theory.md)

## Setup

Model an exterior observer, an infalling observer, and an event horizon as a causal-access boundary.

## Success Criteria

- Interior events can be locally final for infalling systems.
- Exterior observers lack direct classical record export from the interior.
- The model does not claim the interior is unreal.
- The model leaves room for holography, complementarity, and unitary evaporation where applicable.

## Failure Criteria

- The model treats the horizon as a physical wall for the infalling observer.
- The model denies local interior experience.
- The model makes claims about information loss/preservation without the needed physics.

## Contribution Needed

Add a specialist critique of the phrase "finality-domain boundary" and propose safer wording where needed.

## Status Addendum: T418 Horizon Access-Profile Guardrail v0.1

`models/schwarzschild_horizon_access_profile_screen.py` supplies the runnable
guardrail requested by this T4 spec. The artifact is registered as
[T418](T418-schwarzschild-horizon-access-profile-screen.md) because the
Schwarzschild access-profile audit was built later in the numbered sequence.

T418 uses radial null structure in ingoing Eddington-Finkelstein coordinates to
separate two questions:

- Exterior-native capability: two states with the same exterior Schwarzschild
  shadow and different interior records do not split exterior record-recovery
  capability.
- Cross-profile capability: an infalling or full-slice profile can distinguish
  the interior records, but that is an access-profile mismatch unless the
  profile change is declared.

Safe reading: the event horizon is a standard GR causal-access boundary for the
stationary exterior observer in this screen. It is not TaF residue by itself,
does not deny local interior experience, and does not make a black-hole
information, holography, evaporation, semiclassical-gravity, or replacement
geometry claim.

Result packet:
`results/T418-schwarzschild-horizon-access-profile-screen-v0.1-results.md`.
