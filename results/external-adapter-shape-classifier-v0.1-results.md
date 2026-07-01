# T382 Results: External Adapter Shape Classifier

## Current Strongest Claim

Among the declared external-adapter shapes, the two-null-channel adapter is the
only clean survivor. It avoids global time import, couples locally, provides two
independent null signal directions, stays minimal, and supports reciprocal
observer scaling.

This strengthens the external-adapter reading: if something outside the observer
manifold touches the shared substrate without handing in an absolute clock, the
clean interface shape is two primitive null compatibility-signal channels.

## Result Summary

| adapter | status | classification |
|---|---|---|
| `absolute_clock` | `rejected_global_clock` | `null` |
| `scalar_source_action` | `rejected_no_signal_geometry` | `null` |
| `one_signal_channel` | `rejected_undercomplete` | `null` |
| `two_null_channel` | `uniquely_clean` | `survivor` |
| `overcomplete_multi_channel` | `demoted_overcomplete` | `demoted` |
| `gauge_like_local_adapter` | `partial_gauge_relabel_only` | `partial` |

## Hostile Comparators

| comparator | absorbs? | status |
|---|---:|---|
| `adapter_uniqueness` | `false` | `supported_within_declared_shapes` |
| `shape_catalog_completeness` | `true` | `still_absorbs` |
| `external_origin` | `true` | `still_open` |
| `global_clock_shortcut` | `false` | `rejected` |

## Plain-English Reading

T382 says:

```text
If an outside thing couples into the observer substrate without bringing an
absolute clock, the clean adapter shape is two null signal channels.
```

Other shapes fail in informative ways:

- absolute clock imports time directly,
- scalar action has no signal geometry,
- one channel is undercomplete,
- overcomplete channels must be demoted or factored,
- gauge-like local relabeling lacks observer calibration.

## What Improved

The two-null-channel object now has a role:

```text
clean external interface candidate
```

not merely:

```text
convenient algebraic basis
```

## What Weakened

The result does not prove origin. It says which adapter shape is clean among the
declared catalog. It does not show that such an adapter must exist, nor that the
catalog is complete.

## Claim Ledger Update

Register T382 as adapter-shape evidence. The two-null-channel object is the
cleanest external interface candidate, but catalog completeness and origin
remain open.

## Next

Stress the clean survivor:

```text
What breaks if signal speeds are anisotropic, scaling is nonreciprocal, channels
are delayed/noisy, one channel is missing, or extra channels are primitive?
```
