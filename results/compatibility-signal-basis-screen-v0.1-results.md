# T380 Results: Compatibility Signal-Basis Screen

## Current strongest claim

In a 1+1 compatibility module, two independent primitive null signal channels
force the product interval:

```text
Delta_left * Delta_right
```

up to scale. Reciprocal lineage scaling is then exactly the interval-preserving
observer family, and `c = 1` is a rest-rendering unit normalization.

This sharpens T379. The Lorentz-looking algebra is not arbitrary once the
two-null-channel basis is granted. But the existence of exactly two independent
primitive null channels is still not derived from compatibility alone.

## Result summary

| check | result |
|---|---:|
| two independent null channels force product interval | `true` |
| `c = 1` is unit normalization | `true` |
| reciprocal scaling preserves interval | `true` |
| nonreciprocal scaling fails | `true` |
| single channel underdetermines interval | `true` |
| collinear channels fail to form basis | `true` |
| three noncollinear null channels overconstrain 1+1 form | `true` |
| extra collinear channel is redundant | `true` |
| generated substrate intervals match forced form | `true` |
| checked generated substrate pairs | `4950` |
| basis fully derived from compatibility alone | `false` |
| overall verdict | `product_interval_forced_given_two_null_channels_but_signal_basis_not_derived` |

## Candidate verdicts

| candidate | status | passes? |
|---|---|---:|
| `two_independent_null_channels` | `product_interval_forced_up_to_scale` | `true` |
| `single_null_channel` | `underdetermined` | `false` |
| `collinear_two_channels` | `not_a_two_direction_basis` | `false` |
| `three_noncollinear_null_channels` | `overconstrained` | `false` |
| `extra_collinear_null_channel` | `redundant_channel_factors_through_basis` | `true` |

## Hostile comparators

| comparator | absorbs? | status |
|---|---:|---|
| `minkowski_metric_import` | `false` | `weakened_by_null_constraint_solution` |
| `two_channel_basis_import` | `true` | `still_absorbs` |
| `null_signal_assumption` | `true` | `still_absorbs` |
| `bilinear_interval_premise` | `true` | `still_absorbs` |
| `numeric_c_equals_one` | `false` | `unit_normalization` |
| `compatibility_alone` | `true` | `insufficient` |

## Plain-English Reading

T380 says:

```text
If you already have two independent primitive directions for information travel,
and both are null signal directions, then the interval structure is forced.
```

The forced structure is:

```text
interval = left_signal_count * right_signal_count
```

And the observer transformations that preserve it are exactly reciprocal
rescalings:

```text
left  -> scale * left
right -> right / scale
```

That is the finite algebraic core behind T379's Lorentz pattern.

## What Improved

T379 assumed the light-channel basis and then derived Lorentz-pattern observer
maps. T380 narrows the assumption. It shows that once two independent null
signal channels are accepted, the product interval is not a free choice. It is
the unique nondegenerate symmetric bilinear form up to scale.

It also clarifies `c = 1`: that number is not a separate discovery. It is the
unit normalization for the rest rendering of the two null channels.

## What Weakened

The deeper claim remains blocked:

```text
compatibility alone derives the two-channel light basis
```

The controls show why:

- one signal channel underdetermines the interval,
- two collinear channels do not make a 1+1 basis,
- three noncollinear primitive null channels overconstrain a 1+1 nondegenerate
  bilinear interval.

So the live imported object is now very specific:

```text
exactly two independent primitive null compatibility-signal directions
```

## Claim Ledger Update

Register T380 as a basis-forcing boundary result. T379's Lorentz algebra is not
arbitrary once a two-null-channel basis is granted, but that basis is still the
live imported object.

## Next

The next live target is:

```text
derive or independently motivate the two primitive null channels
```

More precisely:

```text
find a compatibility-only condition that forces exactly two independent
primitive signal directions, or show that this must remain an external adapter
assumption.
```
