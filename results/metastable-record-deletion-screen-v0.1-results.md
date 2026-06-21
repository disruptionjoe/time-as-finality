# T152 Results: Metastable-Record Deletion Screen

## Summary

Finite metastable barriers can make records long-lived and can support task-specific retention capabilities, but they do not make physical deletion constructor-impossible. Barrier height, reservoir state, control windows, and horizon choices are ordinary kinetic/resource data. Infinite barriers or denied controls create stipulated constructor or boundary restrictions. The only matched finite-barrier split is the T145 branch-topology residue, which changes future operation availability but not reverse admissibility.

## Audit Table

| Fixture | Matched accounting | Finite barriers | FOA split | H7 candidate | Verdict |
| --- | --- | --- | --- | --- | --- |
| `finite_barrier_lifetime_split` | `False` | `True` | `True` | `False` | `absorbed_by_kinetic_barrier_accounting` |
| `same_barrier_branch_topology_split` | `True` | `True` | `True` | `False` | `fixed_accounting_metastable_topology_residue_not_arrow` |
| `infinite_barrier_constructor_lock` | `False` | `False` | `True` | `False` | `absorbed_by_infinite_barrier_stipulation` |
| `control_window_denial` | `False` | `True` | `True` | `False` | `absorbed_by_control_boundary` |
| `hidden_cold_reservoir_or_engineered_barrier` | `False` | `True` | `True` | `False` | `absorbed_by_reservoir_or_temperature_accounting` |

## finite_barrier_lifetime_split

- Source: finite metastable memory barrier
- Reverse-edge class: `physical_record_deletion`
- Absorber vector matched: `False`
- Absorber mismatch fields: `['beta_barrier']`
- Finite barriers: `True`
- Survival probabilities: `0.9999999999064237` vs `0.0011850776263342881`
- D1 topology split: `False`
- Future operation: `retain_record_through_horizon`
- Future-operation split: `True`
- Reverse status: `finite_rate_possible_with_barrier_accounting`
- H7 upgrade candidate: `False`
- Verdict: `absorbed_by_kinetic_barrier_accounting`
- Interpretation: finite_barrier_lifetime_split is absorbed by finite barrier/lifetime accounting: The long-lived side survives the horizon because its finite barrier is larger. That is ordinary kinetic lifetime accounting, not constructor impossibility.

## same_barrier_branch_topology_split

- Source: T145 branch-topology residue instantiated in a metastable cell
- Reverse-edge class: `physical_record_deletion`
- Absorber vector matched: `True`
- Absorber mismatch fields: `[]`
- Finite barriers: `True`
- Survival probabilities: `0.9999979388485017` vs `0.9999979388485017`
- D1 topology split: `True`
- Future operation: `survive_one_branch_failure`
- Future-operation split: `True`
- Reverse status: `finite_rate_or_control_deletion_possible`
- H7 upgrade candidate: `False`
- Verdict: `fixed_accounting_metastable_topology_residue_not_arrow`
- Interpretation: same_barrier_branch_topology_split preserves a future-operation split under matched finite metastable accounting, but deletion remains finite-rate or finite-control possible. Treat it as topology residue, not H7 arrow evidence.

## infinite_barrier_constructor_lock

- Source: infinite-barrier idealization
- Reverse-edge class: `physical_record_deletion`
- Absorber vector matched: `False`
- Absorber mismatch fields: `['beta_barrier']`
- Finite barriers: `False`
- Survival probabilities: `0.9999999999064237` vs `1.0`
- D1 topology split: `False`
- Future operation: `make_deletion_impossible`
- Future-operation split: `True`
- Reverse status: `constructor_stipulated_by_infinite_barrier`
- H7 upgrade candidate: `False`
- Verdict: `absorbed_by_infinite_barrier_stipulation`
- Interpretation: infinite_barrier_constructor_lock relies on an infinite barrier idealization: An infinite barrier can forbid deletion only by changing the admissible state space or imposing an ideal constructor constraint. It is not a finite metastable substrate result.

## control_window_denial

- Source: finite metastable record with observer control withheld
- Reverse-edge class: `physical_record_deletion`
- Absorber vector matched: `False`
- Absorber mismatch fields: `['reversible_control', 'control_window']`
- Finite barriers: `True`
- Survival probabilities: `0.9999979388485017` vs `0.9999979388485017`
- D1 topology split: `False`
- Future operation: `delete_record_on_demand`
- Future-operation split: `True`
- Reverse status: `blocked_by_observer_control_boundary`
- H7 upgrade candidate: `False`
- Verdict: `absorbed_by_control_boundary`
- Interpretation: control_window_denial is observer/control-boundary accounting: The reverse is blocked only relative to an observer/control boundary. That is access accounting, not substrate-native physical deletion impossibility.

## hidden_cold_reservoir_or_engineered_barrier

- Source: reservoir/barrier engineering control
- Reverse-edge class: `physical_record_deletion`
- Absorber vector matched: `False`
- Absorber mismatch fields: `['beta_barrier', 'reservoir_state']`
- Finite barriers: `True`
- Survival probabilities: `0.0011850776263342881` vs `0.9999999999064237`
- D1 topology split: `False`
- Future operation: `retain_record_through_horizon`
- Future-operation split: `True`
- Reverse status: `absorbed_by_reservoir_and_barrier_state`
- H7 upgrade candidate: `False`
- Verdict: `absorbed_by_reservoir_or_temperature_accounting`
- Interpretation: hidden_cold_reservoir_or_engineered_barrier is reservoir or barrier-engineering accounting: The apparent arrow comes from changing reservoir or barrier engineering data that ordinary metastability already tracks.

## Metastable Lifetime Residues

- `finite_barrier_lifetime_split`

## Fixed-Accounting Topology Residues

- `same_barrier_branch_topology_split`

## H7 Arrow Candidates

None.

## What Improved

T152 screens the most plausible physical-deletion substrate left after T145/T148. It turns 'stable record' into a finite barrier, lifetime, control, and reservoir audit rather than a shortcut to physical-arrow language.

## What Weakened

Metastability does not reopen H7 as a thermodynamic-arrow claim. Finite lifetime is kinetic residue, infinite lifetime is an ideal constraint, and observer-inaccessible deletion is a control-boundary fact.

## Falsification Condition

T152 fails in H7's favor only if a finite, physically typed metastable record substrate has matched barrier, reservoir, erasure, capacity, sink, observer-boundary, provenance, source-copy, and reversible-control data, a task-natural future-operation split, and a physical deletion reverse that is constructor-impossible rather than merely exponentially unlikely or observer-inaccessible.

## H7 Update

Add T152 to H7: metastable records are lifetime/resource absorbers, not physical-arrow evidence. Finite barriers give nonzero deletion routes; infinite barriers and missing controls are constructor or boundary stipulations; matched finite-barrier topology remains future-operation residue.

## Claim Ledger Update

T152 tests the remaining physical-deletion gate against metastable records. No finite-barrier fixture clears H7. The route is absorbed by kinetic barrier/lifetime accounting, reservoir or control state, constructor idealization, or the already-demoted T145 future-operation topology residue.

## Open Blocker

No finite metastable substrate in the current audit yields a constructor-impossible physical deletion reverse after full barrier, reservoir, control, sink, capacity, boundary, provenance, and source-copy accounting.

## Suggested Next

Leave H7 in conditional constructor/resource-audit status unless a named finite physical record substrate can satisfy the T152 falsification condition. The next higher-value thermodynamic move would be a stochastic-thermodynamic citation map for this absorber.
