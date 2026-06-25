# S6 G8 Finite Sheaf Engine Results

Result: focused tests pass `5/5`.

Machine-readable output:

- [s6-g8-finite-sheaf-engine-v0.1.json](s6-g8-finite-sheaf-engine-v0.1.json)

## Status

This is G8 in the second S6 ambitious-goal sequence.

It replaces bespoke descent logic with a reusable finite-site descent engine:

```text
finite site
local records on contexts
field policies
support thresholds
associated record
eta_F loss profile
```

Guardrail:

```text
Reusable finite descent engine only: not a general sheafification theorem and
not a proof that abstract sheafification creates time.
```

## Site And Policies

Site:

```text
contexts = E0, E1, E2, E3, E4
cover    = all five contexts
overlaps = 10 pairwise overlaps
```

Fields:

```text
pointer
prep_measure
measure_record
```

Each field requires support `4`.

## Prethreshold Control

At strength `1.0`:

```text
pointer support        = 3
prep_measure support   = 3
measure_record support = 3
stable                 = false
```

The engine refuses to create the final record before support is present.

## Threshold Result

At strength `1.2`:

```text
pointer support        = 4
prep_measure support   = 4
measure_record support = 4
stable                 = true
values                 = pointer=1, prep_measure=true, measure_record=true
eta_F loss             = phase_sensitive_branch
```

Final capabilities:

```text
read_pointer
reconstruct_provenance_order
```

Lost capability:

```text
phase_sensitive_branch
```

## Interpretation

G8 strengthens S6 because the threshold is no longer produced by custom S6
logic. The generic finite descent engine consumes G7 fragment records and
reproduces the same finality transition through declared field support.

## Verdict

```text
Project[O] + Finalize[R] + Lose[K]
not Issue[S]
```

## First Obstruction

The engine is still a finite associated-record reflector over declared fields.
It does not prove general sheafification or pick the site canonically.

The next goal is G9: use the generic engine to build a same-final-record /
different-presheaf-capability pair.

## Reproduction

```bash
python -m unittest tests.test_s6_g8_finite_sheaf_engine -v
python -m models.run_s6_g8_finite_sheaf_engine --output results/s6-g8-finite-sheaf-engine-v0.1.json
```
