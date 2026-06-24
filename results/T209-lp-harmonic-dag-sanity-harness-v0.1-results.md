# T209 Results: LP-Harmonic-DAG Sanity Harness

## Outcome

`promoted`

## Main Readout

The executable harness distinguishes harmonic proxy values from LP optima and
flags shared-edge DAG incidence.

| Fixture | Harmonic | Pure LP | LP `d=.1` | Check |
| --- | ---: | ---: | ---: | --- |
| Alpha `{4,2,1}` | `12/7` | `1` | `7/5` | mismatch caught |
| Beta `{3,2,1}` | `18/11` | `1` | `13/10` | mismatch caught |
| Gamma `{4,2,5,3}` | `240/77` | `2` | `13/5` | mismatch caught |
| Delta `{3,2,4,3}` | `48/17` | `2` | `12/5` | mismatch caught |

## Shared-Edge Check

The T195 reconvergent DAG reports edge loads greater than one, so `T*_DAG` is
admissible only as a declared path-summary proxy.

## Verdict: promoted

The harness is a pre-registration gate for future finite Moses / MTI / Cap_TI
claims.

## Verification

Run:

```text
python -m pytest tests/test_mti_lp_harmonic_sanity.py
```

Executed on 2026-06-24:

```text
6 passed
```
