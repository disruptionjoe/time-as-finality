# T124 Results: Constructor-Admissibility Grounding Audit

## Summary

H7 can be used only as an audited admissibility ledger: every strict D1-increasing edge must classify the reverse edge under the same accounting boundary. Current witnesses permit only constructor-only or resource-accounting readings, never an unqualified physical arrow.

## Transformation Ledger

| Case | Source | Reverse status | Named resource/condition | Verdict |
| --- | --- | --- | --- | --- |
| `t18_constructor_rule` | T18 | `constructor-impossible` | constructor admissibility premise | `constructor_only` |
| `t80_reversible_window_definalization` | T80 | `reversible possible` | none | `rejected_reversible` |
| `t84_cyclic_export_accounting` | T84 | `reversible possible` | exported history or erasure channel | `resource_accounting_only` |
| `t106_bounded_sink_forward_branch` | T106 | `reversible possible` | finite blank sink capacity and excluded return path | `resource_accounting_only` |
| `t110_closed_permutation_orbit` | T110 | `reversible possible` | none | `rejected_reversible` |
| `t116_open_export_recorder` | T116 | `resource-consuming possible` | path log-ratio, exported history, or fresh blank capacity | `resource_accounting_only` |
| `t122_stationary_markov_upward_move` | T122 | `stochastic-balanced possible` | none | `rejected_stationary` |
| `t128_resource_drawdown` | T128 | `resource-impossible` | finite nonrenewed capacity | `resource_accounting_only` |
| `t128_constructor_restricted` | T128 | `constructor-impossible` | excluded reverse channel | `constructor_only` |

## t18_constructor_rule

- Source: T18
- Forward edge: less finalized record -> more finalized record
- D1 delta: strict increase by premise
- Accounting boundary: formal admissibility relation
- Forward status: `constructor-admissible possible`
- Reverse edge: more finalized record -> less finalized record
- Reverse status: `constructor-impossible`
- Reverse blocker: reverse is excluded by the D1-monotone admissibility rule
- Named resource or condition: constructor admissibility premise
- Permits unqualified physical arrow: `False`
- Permits constructor reading: `True`
- Permits resource-accounting reading: `False`
- Verdict: `constructor_only`
- Reason: This is a valid conditional theorem, but it does not ground the premise in substrate physics.

## t80_reversible_window_definalization

- Source: T80
- Forward edge: Rule-30 reversible physical step with raw window D1 decrease
- D1 delta: decrease, not strict finalization
- Accounting boundary: closed reversible second-order cellular automaton
- Forward status: `reversible possible`
- Reverse edge: direct inverse second-order CA step
- Reverse status: `reversible possible`
- Reverse blocker: none when the full reversible state is included
- Named resource or condition: none
- Permits unqualified physical arrow: `False`
- Permits constructor reading: `False`
- Permits resource-accounting reading: `False`
- Verdict: `rejected_reversible`
- Reason: Raw physical steps cannot be identified with T18 admissible steps; the inverse exists in the same accounted substrate.

## t84_cyclic_export_accounting

- Source: T84
- Forward edge: cyclic memory overwrite plus exported overwritten slot
- D1 delta: strict accounted-support increase
- Accounting boundary: local ring plus exported history channel
- Forward status: `resource-consuming possible`
- Reverse edge: restore prior ring and unexport the overwritten slot
- Reverse status: `reversible possible`
- Reverse blocker: blocked only if exported history or heat-bath channel is excluded
- Named resource or condition: exported history or erasure channel
- Permits unqualified physical arrow: `False`
- Permits constructor reading: `False`
- Permits resource-accounting reading: `True`
- Verdict: `resource_accounting_only`
- Reason: The monotone lives in exported history or erasure accounting, not in autonomous cyclic memory.

## t106_bounded_sink_forward_branch

- Source: T106
- Forward edge: ordered export into a bounded blank sink
- D1 delta: strict forward-branch accounted-support increase
- Accounting boundary: ring memory plus finite sink, before unwind
- Forward status: `resource-consuming possible`
- Reverse edge: reversible unwind after including the sink state
- Reverse status: `reversible possible`
- Reverse blocker: blocked only while the sink return path is omitted
- Named resource or condition: finite blank sink capacity and excluded return path
- Permits unqualified physical arrow: `False`
- Permits constructor reading: `False`
- Permits resource-accounting reading: `True`
- Verdict: `resource_accounting_only`
- Reason: The forward branch is monotone while sink capacity is consumed; the closed bounded cycle has a return-path decrease.

## t110_closed_permutation_orbit

- Source: T110
- Forward edge: putative scalar increase along a finite permutation edge
- D1 delta: cannot be globally nondecreasing and strict on a closed orbit
- Accounting boundary: closed finite reversible state space
- Forward status: `reversible possible`
- Reverse edge: later edge on the same finite orbit returns to the start
- Reverse status: `reversible possible`
- Reverse blocker: none inside the closed permutation orbit
- Named resource or condition: none
- Permits unqualified physical arrow: `False`
- Permits constructor reading: `False`
- Permits resource-accounting reading: `False`
- Verdict: `rejected_reversible`
- Reason: A strict scalar monotone on a finite closed orbit is impossible unless some edge decreases or a boundary is omitted.

## t116_open_export_recorder

- Source: T116
- Forward edge: append/export a record through an open recorder
- D1 delta: strict accounted-record increase
- Accounting boundary: system plus exported history and path irreversibility
- Forward status: `resource-consuming possible`
- Reverse edge: erase or unexport the record through the environment
- Reverse status: `resource-consuming possible`
- Reverse blocker: requires reversing path irreversibility or paying the erasure/export account
- Named resource or condition: path log-ratio, exported history, or fresh blank capacity
- Permits unqualified physical arrow: `False`
- Permits constructor reading: `False`
- Permits resource-accounting reading: `True`
- Verdict: `resource_accounting_only`
- Reason: The arrow is absorbed by standard stochastic thermodynamics or capacity/export accounting.

## t122_stationary_markov_upward_move

- Source: T122
- Forward edge: upward score transition inside stationary support
- D1 delta: local increase balanced by downward drift elsewhere
- Accounting boundary: finite Markov chain at stationary distribution
- Forward status: `stochastic-balanced possible`
- Reverse edge: stationary-support downward or balancing transitions
- Reverse status: `stochastic-balanced possible`
- Reverse blocker: none; stationarity forces zero weighted drift
- Named resource or condition: none
- Permits unqualified physical arrow: `False`
- Permits constructor reading: `False`
- Permits resource-accounting reading: `False`
- Verdict: `rejected_stationary`
- Reason: A positive-looking stochastic move is not a scalar finality arrow on stationary support; stationarity forces zero weighted drift.

## t128_resource_drawdown

- Source: T128
- Forward edge: R3 -> R2 -> R1 -> R0 finite resource consumption
- D1 delta: strict drawdown increase
- Accounting boundary: finite nonrenewed capacity with depleted boundary
- Forward status: `resource-consuming possible`
- Reverse edge: R0 -> R1 -> R2 -> R3 refill path
- Reverse status: `resource-impossible`
- Reverse blocker: requires an external refill resource or boundary reset
- Named resource or condition: finite nonrenewed capacity
- Permits unqualified physical arrow: `False`
- Permits constructor reading: `False`
- Permits resource-accounting reading: `True`
- Verdict: `resource_accounting_only`
- Reason: This is the strongest non-stipulative finite survivor, but it is resource drawdown rather than a new thermodynamic arrow.

## t128_constructor_restricted

- Source: T128
- Forward edge: C0 -> C1 -> C2 allowed constructor steps
- D1 delta: strict constructor-rank increase
- Accounting boundary: declared constructor admissibility relation
- Forward status: `constructor-admissible possible`
- Reverse edge: C2 -> C1 -> C0
- Reverse status: `constructor-impossible`
- Reverse blocker: reverse transformations are stipulated inadmissible
- Named resource or condition: excluded reverse channel
- Permits unqualified physical arrow: `False`
- Permits constructor reading: `True`
- Permits resource-accounting reading: `False`
- Verdict: `constructor_only`
- Reason: This survives formally, but its direction is imported by the admissibility relation.

## What Improved

T124 turns the T18 admissibility premise into a checkable ledger. It records whether each candidate arrow is blocked by constructor impossibility, finite resource depletion, exported history, erasure, omitted return path, or stationarity/reversibility controls.

## What Weakened

No existing H7 witness grounds a new thermodynamic arrow. The best non-stipulative survivor is T128 resource drawdown; the formal constructor survivor works only by excluding the reverse by rule.

## Falsification Condition

T124 is falsified, and H7 could strengthen, by a finite or physically calibrated record substrate with a strict D1-increasing edge whose reverse is constructor-impossible under the same full state accounting, without relying on omitted environment, sink capacity, erasure, postselection, coarse-graining, stationarity violation, or stipulated admissibility.

## H7 Update

Add T124 to H7 as the reverse-edge grounding gate. H7 should not be read physically unless the reverse edge is audited under the same substrate and its impossibility or resource boundary is named.

## Claim Ledger Update

H7 remains partially supported only as a constructor/resource accounting lemma. T124 audits the reverse edge for T18, T80, T84, T106, T110, T116, T122, and T128-style cases. All strict surviving edges are either resource/accounting edges or constructor-only stipulations; reversible and stationary controls reject any unqualified physical-arrow reading.

## Open Blocker

The missing upgrade is a physically grounded constructor-impossibility relation for record deletion or definalization that does not reduce to ordinary resource, entropy, boundary, or coarse-graining accounting.

## Suggested Next

Either thermodynamically calibrate the T128 resource drawdown fixture against standard free-energy/capacity accounting, or move expected value to T127 LossKernel prior-art separation.
