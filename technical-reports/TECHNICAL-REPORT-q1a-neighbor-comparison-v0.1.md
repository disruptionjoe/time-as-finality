# Technical Report: Q1A Neighbor Comparison v0.1

## Claim Under Test

After T101, the only live quantum-facing branch is Q1A:

```text
observer-indexed access-boundary record accounting
```

The highest-value question is no longer whether Q1 can keep accumulating
internal sub-branches. It is whether Q1A distinguishes itself from the nearby
frameworks it already overlaps with, or whether it collapses into a careful
redescription of them.

## Result

Q1A does not yet earn paper-facing status as a distinct measurement framework
or interpretation.

The current verdict is narrower:

```text
Q1A survives only as access-boundary and independence accounting over already
formed records.
```

The comparison against the six named neighbors is:

| Neighbor | Shared content | Candidate TaF delta | Current verdict | Collapse condition |
| --- | --- | --- | --- | --- |
| Decoherence | environment-induced record formation and interference suppression | a record may be decohered yet not finalized for one observer because the accessible cut is missing | narrow partial delta | if D1 always reduces to decoherence plus ordinary observer reachability |
| Quantum Darwinism | redundant environmental encodings and fragment sampling | accessible redundancy and independence-corrected redundancy need not agree when duplicates share provenance | narrow partial delta | if D1 holder redundancy always equals admissible accessible redundancy |
| Consistent histories | record-bearing classical-looking history families | Q1A would need an observer-indexed finality preorder beyond consistent-set choice | not yet earned | if every witness is just a consistent-history selection |
| Relational quantum mechanics | observer-relative facts | Q1A would need threshold and independence rules beyond ordinary relational facts | not yet earned | if finality adds no rule beyond relation-to-observer |
| QBism | observer-indexed availability talk | Q1A would need a physical record predicate beyond agent credence update | category separation only | if finality is only belief revision in new language |
| Many-worlds | no-collapse branching and branch-relative records | Q1A would need access or independence structure not already implied by branch-relative record availability | not yet earned | if every witness is only Everettian access bookkeeping |

## Fixed-Data Gate

Q1A should not be sold as distinct until it clears the following gate:

```text
hold fixed the ordinary quantum-side summaries used by neighboring
frameworks:
  - decoherence / pointer-basis evidence
  - fragment-information summaries
  - ordinary branch/history availability

then force a different D1 verdict only by changing the observer-specific
access boundary or the independence structure of the records.
```

This gate matters because many apparent Q1A wins disappear once the comparison
is made honestly. If the witness changes decoherence, changes the redundancy
profile, or changes which branches/histories are available, then the
neighboring framework can usually absorb the effect.

## Current Strongest Claim

The strongest defensible Q1A claim is now:

```text
Q1A is an observer-indexed accounting layer over access boundaries and record
independence. It is not yet a distinct measurement theory or interpretation.
Its best remaining route to distinctness is a fixed-data witness where
standard quantum-side summaries stay the same but the D1 verdict changes.
```

## What This Improved

T102 turns a loose literature obligation into a falsifiable gate. A serious
reader can now ask one sharp question:

```text
what fixed-data witness would force a D1 verdict that decoherence, Quantum
Darwinism, consistent histories, RQM, QBism, and many-worlds cannot absorb?
```

That is a much better standard than adding more prose about observer-relative
facts.

## What This Weakened Or Falsified

This weakens Q1A again.

It blocks the move from "partial internal witness" to "distinct external
framework" without a direct neighbor comparison gate.

It also narrows the present positive content. T2, T22, T62, and T64 remain
useful partial separations, but they do not yet hold enough ordinary
quantum-side data fixed to force a clean external distinction.

## Falsification Criterion

T102 fails in Q1A's favor if one witness holds fixed:

- decoherence / pointer-basis evidence;
- fragment-information summaries;
- ordinary branch/history availability;

while changing the D1 verdict only through access-boundary or independence
structure in a way the six named neighbors cannot reproduce without importing
Q1A's extra predicate.

T102 succeeds against Q1A if every proposed witness can be rewritten entirely
inside decoherence, accessible redundancy, consistent-history choice,
relational facts, personalist credence, or branch-relative access.

## Claim Ledger Update

Q1 should remain `partially_supported` only as an umbrella pointer, and the
surviving Q1A branch should be stated more narrowly:

```text
Q1A currently survives only as observer-indexed access-boundary and
independence accounting over already formed records. It does not yet earn a
paper-facing distinction from decoherence, Quantum Darwinism, consistent
histories, RQM, QBism, or many-worlds. Upgrade it only after a fixed-data
neighbor-comparison witness changes the D1 verdict while those standard
quantum-side summaries stay fixed.
```

## Open Blocker

The repo still lacks one decisive fixed-data witness. The existing T2/T22/T62/
T64 cases show partial separation, but they do not yet freeze enough
neighbor-owned summaries to force a clean distinction.

## Next Work

Build one finite witness family where all of the following remain fixed:

- decoherence / pointer-basis evidence;
- accessible raw redundancy;
- ordinary branch/history availability;

and only one of the following changes:

- the observer's access cut; or
- the independence partition over duplicate records.

If no such witness exists, Q1A should be demoted further from "candidate
physics distinction" to "useful bookkeeping language over standard quantum
accounts."

## Reproduction

```bash
python -m unittest tests.test_q1a_neighbor_comparison -v
python -m models.q1a_neighbor_comparison
```
