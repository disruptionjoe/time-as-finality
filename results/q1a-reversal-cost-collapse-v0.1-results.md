# T118 Results: Q1A Reversal-Cost Collapse

## Aggregate checks

- Proxy defined exactly when partition visible: True
- Proxy equals support on all visible cases: True
- Proxy splits any same-support class: False
- Branch-history changes leave fixed-data gate: True
- Any load-bearing reversal-cost witness in current family: False

## Support to reversal-cost mapping

| Case | Accessible provenance support | D1 verdict | Reversal-cost proxy |
| --- | --- | --- | --- |
| access_none__partition_E1__E2__E3 | 0 | not_finalized | 0 |
| access_none__partition_E1-E2__E3 | 0 | not_finalized | 0 |
| access_none__partition_E1-E3__E2 | 0 | not_finalized | 0 |
| access_none__partition_E1__E2-E3 | 0 | not_finalized | 0 |
| access_none__partition_E1-E2-E3 | 0 | not_finalized | 0 |
| access_E1__partition_E1__E2__E3 | 1 | not_finalized | 1 |
| access_E1__partition_E1-E2__E3 | 1 | not_finalized | 1 |
| access_E1__partition_E1-E3__E2 | 1 | not_finalized | 1 |
| access_E1__partition_E1__E2-E3 | 1 | not_finalized | 1 |
| access_E1__partition_E1-E2-E3 | 1 | not_finalized | 1 |
| access_E2__partition_E1__E2__E3 | 1 | not_finalized | 1 |
| access_E2__partition_E1-E2__E3 | 1 | not_finalized | 1 |
| access_E2__partition_E1-E3__E2 | 1 | not_finalized | 1 |
| access_E2__partition_E1__E2-E3 | 1 | not_finalized | 1 |
| access_E2__partition_E1-E2-E3 | 1 | not_finalized | 1 |
| access_E1-E2__partition_E1__E2__E3 | 2 | not_finalized | 2 |
| access_E1-E2__partition_E1-E2__E3 | 1 | not_finalized | 1 |
| access_E1-E2__partition_E1-E3__E2 | 2 | not_finalized | 2 |
| access_E1-E2__partition_E1__E2-E3 | 2 | not_finalized | 2 |
| access_E1-E2__partition_E1-E2-E3 | 1 | not_finalized | 1 |
| access_E3__partition_E1__E2__E3 | 1 | not_finalized | 1 |
| access_E3__partition_E1-E2__E3 | 1 | not_finalized | 1 |
| access_E3__partition_E1-E3__E2 | 1 | not_finalized | 1 |
| access_E3__partition_E1__E2-E3 | 1 | not_finalized | 1 |
| access_E3__partition_E1-E2-E3 | 1 | not_finalized | 1 |
| access_E1-E3__partition_E1__E2__E3 | 2 | not_finalized | 2 |
| access_E1-E3__partition_E1-E2__E3 | 2 | not_finalized | 2 |
| access_E1-E3__partition_E1-E3__E2 | 1 | not_finalized | 1 |
| access_E1-E3__partition_E1__E2-E3 | 2 | not_finalized | 2 |
| access_E1-E3__partition_E1-E2-E3 | 1 | not_finalized | 1 |
| access_E2-E3__partition_E1__E2__E3 | 2 | not_finalized | 2 |
| access_E2-E3__partition_E1-E2__E3 | 2 | not_finalized | 2 |
| access_E2-E3__partition_E1-E3__E2 | 2 | not_finalized | 2 |
| access_E2-E3__partition_E1__E2-E3 | 1 | not_finalized | 1 |
| access_E2-E3__partition_E1-E2-E3 | 1 | not_finalized | 1 |
| access_E1-E2-E3__partition_E1__E2__E3 | 3 | finalized | 3 |
| access_E1-E2-E3__partition_E1-E2__E3 | 2 | not_finalized | 2 |
| access_E1-E2-E3__partition_E1-E3__E2 | 2 | not_finalized | 2 |
| access_E1-E2-E3__partition_E1__E2-E3 | 2 | not_finalized | 2 |
| access_E1-E2-E3__partition_E1-E2-E3 | 1 | not_finalized | 1 |

## Hidden partition control

- Case: access_E1-E2-E3__partition_hidden
- D1 verdict: withhold_partition_unavailable
- Reversal-cost proxy: None

## Strongest claim

Reversal cost is not a surviving independent lever in the current fixed-data Q1A family. Once the witness language is restricted to already formed records with fixed ordinary quantum-side summaries, the only admissible reversal-cost proxy is how many audited accessible provenance classes would need to be erased or overwritten. That proxy is identical to accessible provenance support whenever the partition is visible and is withheld when the partition is hidden. So reversal cost adds no verdict content beyond the T105 support count in the present family.

## What this improved

T118 closes the last obvious Q1A fixed-data loophole. The repo can now say explicitly that the current witness family carries no independent reversal-cost structure, not even at the level of an admissible proxy.

## What this weakened

This weakens Q1A again. In the present fixed-data regime all live verdict content is exhausted by audited accessible provenance support plus partition visibility. Reversal-cost language should not be presented as extra measurement structure unless it is tied to a physically calibrated undo observable outside this collapsed counting regime.

## Falsification condition

T118 fails only if an admissible fixed-data witness in the current Q1A language exhibits different reversal-cost values at the same audited accessible provenance-support count while ordinary quantum-side summaries stay fixed, or if a physically calibrated undo observable becomes available that is neither post hoc nor equivalent to counting audited accessible record classes.

## Q1A update

Q1A should not cite reversal cost as a live independent witness dimension in the current fixed-data family. At present the only admissible reversal-cost proxy is the audited accessible provenance-support count itself, with withholding when the partition is unavailable.

## Claim ledger update

Add T118 to Q1A: reversal cost does not presently escape the accessible-class reduction. In the current fixed-data witness family its only admissible proxy is the number of audited accessible provenance classes that would need to be erased or overwritten, so it adds no independent verdict content.

## Open blocker

The repo still lacks a finite quantum witness with a physically calibrated undo or erasure observable that can vary while decoherence, fragment-information summaries, raw redundancy, branch/history availability, and audited accessible support stay fixed.

## Recommended next

Either construct a genuinely dynamic witness with a predeclared undo observable that survives the fixed-data gate, or state plainly in paper-facing summaries that current Q1A evidence is fully reduced to audited record-accounting discipline.
