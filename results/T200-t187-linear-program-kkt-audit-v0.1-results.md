# T200 Results: T187 Linear-Program / KKT Audit

## Outcome

`killed`

## Main Readout

The stated T187 derivation is mathematically incorrect. A lower-bound diversity
floor does not yield inverse-time allocation.

## Fixture

For `t = (4,2,1)`:

| Regime | Weights | Objective |
| --- | --- | ---: |
| Pure LP | `(0,0,1)` | `1` |
| Lower-bound LP, `d = 0.1` | `(0.1,0.1,0.8)` | `1.4` |
| Inverse-time proxy | `(1/7,2/7,4/7)` | `12/7` |

## Absorber Pass

Standard linear programming absorbs the old KKT claim. The harmonic mean must
be demoted to proxy status unless a new objective is declared.

## Verdict: killed

## Next Step

Use T201 to search for legitimate objectives that produce inverse-time-like
allocations.
