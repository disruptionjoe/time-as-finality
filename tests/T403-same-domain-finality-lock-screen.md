# T403: Same-Domain Finality-Lock Screen

## Target Claims

- [Region-Indexed Capability Discriminator](../open-problems/region-indexed-capability-discriminator.md)
- T400 boundary-forced task gate
- T401 finality-boundary reconciliation screen
- T402 causal-domain boundary forcing screen
- H7 / future-operation-availability absorber discipline

## Setup

Reuse the T402 finite 1+1 causal-domain fixture:

```text
R input:                  t=0, x=-1
B input:                  t=0, x= 1
common-future verdict:    t=1, x= 0
c = 1
```

The main pair matches:

- causal-domain signature;
- joint payload;
- verdict payload;
- revision budget;
- declared operation menu.

The only intended difference is record-finality state:

```text
provisional_same: joint payload 11, finality_state = provisional
sealed_same:      joint payload 11, finality_state = sealed
```

The capability object is future operation availability for:

- reading the verdict;
- appending a correction;
- revising the final verdict before the horizon.

## Success Criteria

- The imported causal-domain signature matches T402.
- The main pair has the same visible causal-payload projection.
- The main pair has the same joint payload and same verdict payload.
- The main pair has the same revision budget and same operation menu.
- The capability split is only `can_revise_final_verdict`.
- Finality-state completion restores factorization.
- Matched-finality, joint-input-completion, operation-menu-completion, and
  hidden-label controls classify correctly.
- The result says no claim-ledger movement is earned.

## Failure Criteria

The artifact fails if:

- the main pair differs in causal-domain data;
- the main pair differs in joint payload;
- the main pair differs in revision budget or operation menu;
- the revision capability remains split after finality-state completion;
- a hidden source label or class marker performs the separation;
- the finite lock state is framed as a physical claim rather than an absorber.

## Known Physics Constraints

This is a finite record-state screen. It does not claim that a real physical
record lock has been derived. It shows only that the post-T402 same-domain lane
can be made precise, and that the first clean split is absorbed by explicit
finality-state completion.

## Contribution Needed

A future upgrade needs a physically typed finality-lock substrate whose
provisional/sealed state is not merely stipulated and whose operation
availability remains fixed-accounting after the usual resource, provenance,
control, and boundary absorbers are granted.
