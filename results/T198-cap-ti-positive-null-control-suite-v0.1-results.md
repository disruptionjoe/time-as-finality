# T198 Results: Cap_TI Positive / Null Control Suite

## Correction Notice

Updated after the T187 review/T200-T209 follow-up. The positive/null controls
below are registered for the finite harmonic-proxy regime. T209 is now the
required arithmetic guardrail before reusing them in corrected LP or DAG-flow
settings.

## Outcome

The Cap_TI Candidate C control logic is now explicit and reusable.

The suite canonizes the current exact-family rule:

```text
controls that move T* should split;
controls that preserve T* should not.
```

## Control Summary

| Control | Expected behavior | Status |
| --- | --- | --- |
| P1 Alpha/Beta | positive split | admitted |
| P2 monotone T* family | positive ordering | admitted |
| N1 branch relabeling | null | admitted |
| N2 compensated same-T* tradeoff | null | admitted |
| N3 topology variation with same T* | null | admitted |
| S1 structural-difference stress | null unless T* moves | admitted |
| S2 higher-moment stress | null unless T* moves | admitted |
| S3 scale stress | positive only through T* | admitted |

## Why This Matters

T193 and T194 already did the underlying conceptual work. T198 packages that
work into a reusable harness so later tests can distinguish:

- real capability movement;
- fake positives driven by visually rich but summary-invariant changes;
- genuine positive controls that actually move the reduced invariant.

## Repo-Safe Reading

T198 is infrastructure, not a new physics or formalism result. Its value is
that later tests can now say:

```text
passes P1/P2,
fails N1-N3,
respects S1-S3,
```

instead of rebuilding the same argument from scratch.

## What This Changes

- T197 should cite this suite when testing absorber ownership of the
  harmonic-mean-based capability.
- Any future Candidate C promotion should cite these controls explicitly.
- If a future test breaks one of the null controls at fixed `T*`, both T193 and
  T194 become suspect and the suite must be revised.
