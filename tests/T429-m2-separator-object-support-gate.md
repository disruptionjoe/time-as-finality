# T429 - M2 Separator-Object Support Gate - spec (frozen)

> Recorded-tier exploratory guardrail. `TESTS.md` and `CLAIM-LEDGER.md` are
> UNTOUCHED; the T-number lives only in this header / the results header. NO claim
> promotion; ledger actions pause for Joe. Cross-domain social-choice / index
> language is the OBJECT OF STUDY, never evidence for physics or a sibling repo.
> The only code imports are TaF-native standard-library-only M2 support machinery.

- Model: `models/m2_separator_object_support_gate.py`
- Tests: `tests/test_m2_separator_object_support_gate.py`
- Results: `results/T429-m2-separator-object-support-gate-v0.1-results.md`
- Run: `python -m pytest tests/test_m2_separator_object_support_gate.py -q`

## The question this test settles

T428 blocked the common nonquota full-judgment selector branch and left the
remaining bounded M2 escape hatch:

```text
genuinely different separator object
```

T429 tests a small predeclared separator-object family over the same finite
AND-doctrine judgment-state universe. The gate asks:

```text
Can a separator object create larger-n SURVIVES-R1 positives without merely
reading support counts, ambient size, deletion-critical wording, or graph
diagnostics already reducible to full support fibers?
```

## Object Family

For every profile over states `(00, 01, 10, 11)` and every coalition, compute
whether the coalition satisfies a candidate separator object:

- all four judgment states appear;
- both crossing diagonals appear;
- compatibility graph has positive cycle rank;
- complete signed graph has positive frustration index;
- exactly one crossing edge;
- exact support shapes `2,2` and `2,1,1,1`;
- ambient-size even support shape.

A profile is counted as `SURVIVES-R1` for an object only when the grand coalition
satisfies the object and no proper coalition does. It is counted as `ABSORBED`
when a proper coalition already satisfies the same object.

## Controls

Every object reports whether separator status is fully determined by full support
counts over `(00, 01, 10, 11)`. A stable positive that is support-determined or
ambient-size-dependent is not an independent canonicity channel; it is a
completion artifact.

## Success / Kill Criteria

### RECHECK

If an object creates `SURVIVES-R1` positives at both n=4 and n=5 and the separator
status is not determined by support counts or ambient size, inspect it as a
possible finite M2 redesign lead. This still would not promote a claim.

### REDESIGN

If all cross-size positives are support-count or ambient-size completion artifacts,
and all non-ambient objects are size-local or absorbed by proper subsets, then
this bounded separator-object hatch does not repair M2 canonicity.

## Honest Ceiling

Finite enumeration only: AND-doctrine judgment-state profiles over
`n in {3, 4, 5}`. This is not a universal theorem about judgment aggregation,
separator objects, signed graphs, social choice, index theory, or finality. It
only tests whether this bounded family gives the existing M2 redesign lane a clean
next finite target.
