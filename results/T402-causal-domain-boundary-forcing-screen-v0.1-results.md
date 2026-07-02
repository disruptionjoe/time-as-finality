# T402 Causal-Domain Boundary Forcing Screen Results

Artifact: `T402-causal-domain-boundary-forcing-screen-v0.1`

## Verdict

Finite physical-substrate forced-boundary candidate built:

- a common-future verdict event is causally downstream of both `R` and `B`
  inputs;
- `R`-only statistics and declared `R` interventions remain flat;
- boundary-local statistics remain flat;
- the common-future same/different verdict separates aligned from anti-aligned
  source distributions with binary success `1.0`;
- the result clears the causal-domain task-shape burden, but is absorbed by
  ordinary causal-domain completion and joint input access.

No claim-ledger movement is earned.

## Key Checks

| Check | Result |
| --- | --- |
| `R` and `B` spacelike | pass |
| verdict in common future | pass |
| `R`-only domain contains verdict | false |
| `B`-only domain contains verdict | false |
| joint `R:B` domain contains verdict | true |
| all `R`-supported statistic bound | `0.0` |
| finite `R` intervention menu max diff | `0.0` |
| boundary-local statistic bound | `0.0` |
| region-only binary success | `0.5` |
| common-future verdict success | `1.0` |

## Absorber Result

The physical-substrate task is forced by the declared causal setup, but the
separator is not residue:

- Lorentzian causal-domain completion absorbs the boundary-forcing shape.
- Ordinary joint input completion absorbs the same/different verdict after the
  common-future event has both incoming records.
- Optional joint labels, hidden datum in `R`, closure-key shortcuts, and
  class-marker shortcuts are blocked.

## Next Constraint

Do not repeat causal-domain completion as if it were a surviving
discriminator. A future upgrade needs a same-causal-domain-data capability
split not expressible as causal reachability, domain of dependence, or ordinary
joint input completion.
