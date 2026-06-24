# T211 Results: Executable Same-Harmonic Different-C_flow Fixture

## Outcome

`promoted`

## Verification

Covered by:

```text
python -m pytest tests/test_mti_cflow_solver.py
```

## Result

| Fixture | Free path times | Harmonic | `C_flow` |
| --- | --- | ---: | ---: |
| Disjoint | `{2,2}` | `2` | `8/3` |
| Shared prefix | `{2,2}` | `2` | `10/3` |

## Verdict: promoted

The path-harmonic projection is insufficient for corrected overlapping-DAG
capability.
