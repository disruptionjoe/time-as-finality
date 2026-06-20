# T103: Q1A Fixed-Data Witness

## Route

Quantum measurement / classical records.

## Question

Can Q1A clear its T102 fixed-data gate: hold fixed the ordinary quantum-side
summaries used by nearby frameworks, then change the D1 verdict only through
access-boundary or independence structure?

## Motivation

T102 weakened Q1A to observer-indexed access-boundary and independence
accounting over already formed records. It also named the next gate. A valid
witness must not change decoherence, fragment-information summaries, raw
accessible redundancy, or ordinary branch/history availability while claiming a
new D1 verdict.

## Success Criteria

- Construct at least two cases with the same fixed quantum-side signature.
- Keep decoherence/pointer-basis evidence fixed.
- Keep fragment-information summaries fixed.
- Keep accessible raw redundancy fixed.
- Keep ordinary branch/history availability fixed.
- Change D1 only by changing the independence partition or access to that
  partition.
- Include negative controls where coherence, raw redundancy, or branch/history
  availability changes and the fixed-data gate rejects the case.

## Failure Criteria

- A purported Q1A win also changes decoherence, redundancy, or branch/history
  data.
- D1 is inferred from raw redundancy when the independence partition is hidden.
- The result is advertised as new measurement dynamics, collapse content,
  Born-rule content, or empirical quantum support.

## Claim Impact

T103 gives Q1A an internal fixed-data witness but not an external measurement
theory. The result supports only conditional record-accounting language. If
neighboring frameworks adopt the same provenance/independence partition, Q1A
collapses to disciplined bookkeeping.

## Reproduction

```bash
python -m unittest tests.test_q1a_fixed_data_witness -v
python -m models.run_t103
```
