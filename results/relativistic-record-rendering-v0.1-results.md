# T377 Results: Relativistic Record Rendering Fixture

## Current strongest claim

A finite no-time-column `u/v` record carrier can render two observer coordinate
histories with different simultaneity slices and the same interval-like
invariant.

The result is a calibration, not a claim upgrade, because fixed-schema and
fixed-completed-table absorbers still fire.

## Result summary

| check | result |
|---|---:|
| carrier compatible | `true` |
| source rows have no primitive time column | `true` |
| rendered interval invariant recovered | `true` |
| observer simultaneity disagreement | `true` |
| causal order alone sufficient | `false` |
| overall verdict | `rendered_interval_recovered_but_fixed_carrier_absorbed` |

## Hostile comparators

| comparator | absorbs? | status |
|---|---:|---|
| `minkowski_first` | `false` | `not_imported_but_null_rank_caveat` |
| `fixed_schema_log` | `true` | `fixed_carrier_schema_absorbs` |
| `fixed_completed_table` | `true` | `finite_completed_table_absorbs` |
| `hidden_preferred_foliation` | `false` | `not_required` |
| `causal_order_only` | `false` | `insufficient` |
| `t376_fixed_admissibility` | `true` | `guardrail_triggers` |

## Plain-English reading

This fixture does the first positive thing we wanted:

```text
the source table has no time column;
two observers render different time coordinates;
they disagree on simultaneity;
they still recover the same interval-like invariant.
```

But it does not yet beat the deeper absorber. The source carrier has a fixed
schema with `u_rank`, `v_rank`, and a fixed interval rule:

```text
interval = Delta_u * Delta_v
```

So the result can still be read as:

```text
a fixed lightlike-rank table plus two coordinate renderings
```

rather than genuine source-side temporal issuance.

## What improved

T377 improves the target shape. It shows that "time is not a source column"
can be made executable while still recovering relativistic-looking observer
disagreement and invariant agreement.

## What weakened

It weakens the easy positive reading:

```text
no source time column + invariant rendering = TaF bridge
```

The fixed carrier schema and finite completed table still absorb the result.

## Claim ledger update

Register T377 as a finite rendering calibration, not a claim upgrade. It
supports the next-test shape but does not defeat fixed-schema or
fixed-completed-table absorption.

## Next

The next live target is:

```text
nonfixed record-rendering carrier
```

or, more precisely:

```text
a row-append / rendering fixture where the interval-like structure cannot be
precompiled into one fixed schema, fixed completed table, or fixed admissibility
rule.
```
