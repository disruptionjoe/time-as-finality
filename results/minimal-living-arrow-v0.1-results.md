# T128 Results: Minimal Living Arrow

## Summary

- Strongest surviving minimal model: `test_c_resource_drawdown`
- Strongest failed model: `control_b_stationary_markov`
- Smallest formal ingredient set: constructor restriction alone, but only because the reverse transformation is excluded by definition
- Smallest non-stipulative ingredient set: finite nonrenewed resource drawdown with an absorbing depleted boundary

## Model Audits

| Model | Ingredient | Direction survives | T122 assumptions violated | Verdict |
| --- | --- | --- | --- | --- |
| `control_a_closed_reversible` | none | `False` | `[]` | dead: directed cycle blocks a strict scalar monotone |
| `control_b_stationary_markov` | stationary stochasticity only | `False` | `[]` | dead: directed cycle blocks a strict scalar monotone |
| `test_c_resource_drawdown` | finite nonrenewed capacity | `True` | `['nonstationary resource drawdown', 'transient support', 'absorbing depleted boundary']` | lives only with explicit resource/boundary accounting |
| `test_d_maintenance_cost` | maintenance burden plus finite resource | `True` | `['nonstationary resource drawdown', 'transient support', 'absorbing failed-maintenance boundary']` | lives only with explicit resource/boundary accounting |
| `test_e_open_boundary` | open source/sink boundary | `True` | `['open boundary', 'exported history', 'finite sink capacity', 'transient support']` | lives only with explicit resource/boundary accounting |
| `test_f_constructor_restricted` | explicit impossible reverse transformations | `True` | `['excluded reverse channel', 'constructor admissibility restriction']` | lives formally, but by stipulated admissibility restriction |

## Control A: closed reversible finite cycle

- State space: `['A', 'B', 'C']`
- Transition rules: `['A->B p=1 (permutation step)', 'B->C p=1 (permutation step)', 'C->A p=1 (permutation return)']`
- Resource accounting: none: closed finite permutation, no sink or drawdown
- Direction candidate: constructor_rank
- Direction values: `[{'state': 'A', 'value': 0}, {'state': 'B', 'value': 1}, {'state': 'C', 'value': 2}]`
- Future operation sizes: `[{'state': 'A', 'available_operation_count': 3}, {'state': 'B', 'available_operation_count': 3}, {'state': 'C', 'available_operation_count': 3}]`
- Obstruction status: Killed by T110: a strict scalar monotone cannot live on a finite closed reversible orbit.
- T122 assumptions violated: `[]`
- Direction survives: `False`
- Equivalence note: Baseline obstruction control.

## Control B: stationary finite Markov chain

- State space: `['low', 'high']`
- Transition rules: `['low->low p=0.7 (stationary self transition)', 'low->high p=0.3 (stationary upward transition)', 'high->low p=0.3 (stationary downward transition)', 'high->high p=0.7 (stationary self transition)']`
- Resource accounting: none: pi=(1/2,1/2), P is time-independent
- Direction candidate: state_height
- Direction values: `[{'state': 'low', 'value': 0}, {'state': 'high', 'value': 1}]`
- Future operation sizes: `[{'state': 'low', 'available_operation_count': 3}, {'state': 'high', 'available_operation_count': 3}]`
- Obstruction status: Killed by T122: stationarity forces zero stationary-weighted expected drift, so upward drift is balanced by downward drift.
- T122 assumptions violated: `[]`
- Direction survives: `False`
- Equivalence note: Baseline stationary stochastic obstruction control.

## Test C: finite resource drawdown

- State space: `['R3', 'R2', 'R1', 'R0']`
- Transition rules: `['R3->R2 p=1 (consume one unit)', 'R2->R1 p=1 (consume one unit)', 'R1->R0 p=1 (consume one unit)']`
- Resource accounting: finite stock r=3,2,1,0 with no refill
- Direction candidate: drawdown = 3 - resource
- Direction values: `[{'state': 'R3', 'value': 0}, {'state': 'R2', 'value': 1}, {'state': 'R1', 'value': 2}, {'state': 'R0', 'value': 3}]`
- Future operation sizes: `[{'state': 'R3', 'available_operation_count': 3}, {'state': 'R2', 'available_operation_count': 2}, {'state': 'R1', 'available_operation_count': 1}, {'state': 'R0', 'available_operation_count': 0}]`
- Obstruction status: Survives only by leaving the T110/T122 assumptions: the model is not closed reversible and not stationary.
- T122 assumptions violated: `['nonstationary resource drawdown', 'transient support', 'absorbing depleted boundary']`
- Direction survives: `True`
- Equivalence note: Smallest non-stipulative survivor in this audit: direction is the declared loss of finite future capacity.

## Test D: maintenance burden with finite repair budget

- State space: `['M3', 'M2', 'M1', 'M0']`
- Transition rules: `['M3->M2 p=1 (pay one maintenance unit)', 'M2->M1 p=1 (pay one maintenance unit)', 'M1->M0 p=1 (budget exhausted; persistence fails)']`
- Resource accounting: maintenance consumes one unit from a finite repair budget per step; health persists only while budget remains
- Direction candidate: lost future operations
- Direction values: `[{'state': 'M3', 'value': 0}, {'state': 'M2', 'value': 1}, {'state': 'M1', 'value': 2}, {'state': 'M0', 'value': 3}]`
- Future operation sizes: `[{'state': 'M3', 'available_operation_count': 3}, {'state': 'M2', 'available_operation_count': 2}, {'state': 'M1', 'available_operation_count': 1}, {'state': 'M0', 'available_operation_count': 0}]`
- Obstruction status: Survives, but not independently: maintenance creates direction only because a finite repair budget is being depleted.
- T122 assumptions violated: `['nonstationary resource drawdown', 'transient support', 'absorbing failed-maintenance boundary']`
- Direction survives: `True`
- Equivalence note: Equivalent to resource drawdown plus a persistence task label. Maintenance without finite budget is not shown to produce a new arrow.

## Test E: finite open boundary with sink fill

- State space: `['S0', 'S1', 'S2', 'S3']`
- Transition rules: `['S0->S1 p=1 (export one record to sink)', 'S1->S2 p=1 (export one record to sink)', 'S2->S3 p=1 (sink reaches capacity)']`
- Resource accounting: system resource is refilled by source; boundary sink capacity fills from 0 to 3
- Direction candidate: sink_fill
- Direction values: `[{'state': 'S0', 'value': 0}, {'state': 'S1', 'value': 1}, {'state': 'S2', 'value': 2}, {'state': 'S3', 'value': 3}]`
- Future operation sizes: `[{'state': 'S0', 'available_operation_count': 3}, {'state': 'S1', 'available_operation_count': 2}, {'state': 'S2', 'available_operation_count': 1}, {'state': 'S3', 'available_operation_count': 0}]`
- Obstruction status: Survives only when the boundary state is counted. If the sink is not part of the state, this reduces to omitted history.
- T122 assumptions violated: `['open boundary', 'exported history', 'finite sink capacity', 'transient support']`
- Direction survives: `True`
- Equivalence note: Equivalent to resource drawdown in the environment: sink capacity is the resource being consumed.

## Test F: constructor-restricted transformations

- State space: `['C0', 'C1', 'C2']`
- Transition rules: `['C0->C1 p=1 (allowed constructor step)', 'C1->C2 p=1 (allowed constructor step)']`
- Resource accounting: none internal; reverse transformations are excluded by the admissibility relation
- Direction candidate: constructor_rank
- Direction values: `[{'state': 'C0', 'value': 0}, {'state': 'C1', 'value': 1}, {'state': 'C2', 'value': 2}]`
- Future operation sizes: `[{'state': 'C0', 'available_operation_count': 2}, {'state': 'C1', 'available_operation_count': 1}, {'state': 'C2', 'available_operation_count': 0}]`
- Obstruction status: Formally survives, but direction is imported by stipulating the admissible transformation preorder.
- T122 assumptions violated: `['excluded reverse channel', 'constructor admissibility restriction']`
- Direction survives: `True`
- Equivalence note: Smallest formal survivor if stipulation is allowed; weakest physical survivor because it names no substrate cost.

## What Improved

T128 identifies the first finite models that live after the obstruction stack: strict direction appears only when a resource, sink, boundary, or constructor restriction is explicitly included.

## What Weakened

Maintenance and open-boundary arrows do not emerge as independent ingredients in these fixtures. They reduce to resource drawdown, exported history, sink-capacity accounting, or stipulated constructor admissibility.

## Claim Impact Recommendation

Preserve H7 only as a resource-accounting or constructor lemma. Do not promote it as a thermodynamic-arrow claim.

## Open Blocker

The strongest survivor is still an accounting model. A physical upgrade would need a named free-energy or capacity variable and a comparison to standard stochastic thermodynamics.

## Claim Ledger Update

H7 remains partially supported only in narrowed form. T128 shows that closed reversible and finite stationary Markov controls still fail, while the smallest non-stipulative finite survivor is explicit finite resource drawdown. Maintenance and open boundary survive only as resource/sink/export accounting; constructor restriction survives by stipulation.

## Suggested Next

Build a thermodynamic calibration for the resource-drawdown survivor and test whether its direction is anything beyond ordinary free-energy or capacity accounting.
