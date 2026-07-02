# T403 Same-Domain Finality-Lock Screen Results

Artifact: `T403-same-domain-finality-lock-screen-v0.1`

## Verdict

Finite same-causal-domain finality-state screen built:

- the main pair imports the T402 causal-domain signature;
- causal-domain data, joint payload, verdict payload, revision budget, and
  declared operation menu are identical;
- the only capability split is `can_revise_final_verdict`;
- the provisional record can revise the final verdict;
- the sealed record cannot revise the final verdict;
- the split is not explained by causal reachability, domain of dependence, or
  ordinary joint input completion;
- the split is absorbed by explicit finality-state completion.

No claim-ledger movement is earned.

## Key Checks

| Check | Result |
| --- | --- |
| source causal fixture | T402 |
| `R` and `B` spacelike | pass |
| verdict in common future | pass |
| joint `R:B` domain contains verdict | true |
| visible causal-payload projection equal | true |
| same joint payload | true |
| same verdict payload | true |
| same operation menu | true |
| same revision budget | true |
| capability split | `can_revise_final_verdict` |
| finality-state completion restores factorization | true |

## Absorber Result

The same-domain lane is now sharper, but still absorbing:

- causal reachability and domain-of-dependence data are matched;
- ordinary joint input completion is matched;
- operation-menu variation is isolated as a separate absorber control;
- hidden label shortcuts are blocked;
- provisional/sealed finality state is the state completion that restores the
  revision capability.

## Next Constraint

A future upgrade needs a physically typed finality-lock substrate whose
provisional/sealed state is not merely stipulated and whose future-operation
availability survives fixed-accounting resource, provenance, control, and
boundary absorbers.
