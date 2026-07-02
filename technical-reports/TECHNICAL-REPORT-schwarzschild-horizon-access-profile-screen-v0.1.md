# Technical Report: Schwarzschild Horizon Access-Profile Screen v0.1

## Status

Internal method-hardening and absorber artifact.

This report does not promote a claim, change the North Star, update public
posture, assert a black-hole information result, or move cross-repo truth. It
implements the safe follow-up named by the access-profile alignment note:

```text
Apply the alignment rule to a GR causal-accessibility witness.
```

## Objective

Test the simplest Schwarzschild horizon version of the access-profile alignment
rule:

```text
pi_exterior
```

must be compared to:

```text
Cap_exterior
```

unless the run explicitly declares a cross-profile question involving an
infalling or full-slice capability.

## Model Scope

The executable model uses radial Schwarzschild causal structure only. In
ingoing Eddington-Finkelstein coordinates, outgoing radial null rays satisfy:

```text
dr/dv = (1/2) * (1 - r_s / r)
```

The screen sets `r_s = 2M = 2` and checks three qualitative regimes:

| Region | Sign of `dr/dv` | Meaning |
| --- | --- | --- |
| `r > r_s` | positive | outgoing null signal can reach a finite exterior cutoff |
| `r = r_s` | zero | horizon generator |
| `r < r_s` | negative | outgoing null direction moves to smaller radius |

This is enough for an access-profile absorber. It is not a continuum theorem
and not a black-hole information model.

## Main Fixture

Two states match all exterior data:

```text
mass = 1
horizon radius = 2
exterior log = (collapse_mass_1, horizon_radius_2)
```

They differ only in an interior record at `r = 1.5`.

The stationary exterior projection cannot receive that record; an outgoing null
trace from `r = 1.5` does not reach the exterior cutoff.

Therefore:

```text
pi_exterior(BH0) = pi_exterior(BH1)
Cap_exterior(BH0) = Cap_exterior(BH1)
```

There is no same-profile projection-sufficiency failure.

## Cross-Profile Trap

If the same exterior projection is compared to:

```text
Cap_infalling_or_full_slice
```

the pair splits, because that profile is granted interior or full-slice access
by definition.

The correct verdict is:

```text
cross_profile_mismatch_absorbed_by_horizon_access_profile
```

not:

```text
exterior observer-shadow residue
```

## Positive Control

The guard has teeth. A record emitted outside the horizon at `r = 3` reaches the
exterior cutoff and is distinguishable by the exterior profile. The screen is not
declaring all records invisible; it is applying standard Schwarzschild causal
access.

## Absorber Verdict

The result is conservative:

```text
same exterior Schwarzschild shadow + different interior record
does not create an exterior-native capability split.
```

The apparent split appears only after changing access profiles.

## Not Claimed

This artifact does not model or claim:

- Hawking radiation;
- evaporation or Page curves;
- holography;
- QFT local algebras;
- semiclassical gravity;
- black-hole information recovery;
- a new horizon physics result;
- a TaF spacetime theorem.

## Reuse Rule

Future B1/S1/R1 horizon-facing witnesses should pass this intake gate:

1. Declare the observer/access profile.
2. Declare the received-record algebra or capability object native to that
   profile.
3. Compare `pi_O` only to `Cap_O`, unless a cross-profile question is declared.
4. Treat ordinary horizon causal access as an absorber, not as residue.

## Short Verdict

T418 turns the GR causal-accessibility next action into an executable guardrail.
It keeps the observer-shadow method honest: the horizon blocks exterior recovery
in the exterior profile, while infalling or full-slice recovery belongs to a
different profile.
