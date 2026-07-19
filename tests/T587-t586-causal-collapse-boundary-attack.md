# T587: T586 Causal-Collapse Boundary Attack

## Target Claims

- T586's record-capability order is tested against ordinary dependency and
  causal comparators on the same frozen event system.
- Boundary inputs are typed so record production is not confused with access
  changes, interventions, observer readout, stochastic input, continuous flux,
  final-boundary selection, or capability deltas by themselves.
- The result must return either an exact residual beyond ordinary dependency /
  causal order or a clean downgrade.

## Setup

Use T586 as the source gate. Compare its produced-record dependency closure
with:

- ordinary task-prerequisite dependency;
- the strongest standard dependency relation from task prerequisites plus all
  declared causal parents;
- the supplied causal order;
- clock-label and entropy-rank controls inherited from T586.

Then classify the boundary-input classes named by the active T586 attack.

## Success Criteria

- The ordinary task-prerequisite comparator either exactly collapses T586 or
  names a record-only residual.
- The strongest dependency and causal comparators either absorb T586 or expose
  a relation-level edge that they cannot explain.
- Only explicit physical record production and native record-issuance rules
  count as record-order sources.
- The verdict states the downgrade or residual without moving claim status.

## Failure Criteria

- Access change, observer readout, intervention, final-boundary selection,
  continuous flux, stochastic input, or capability change is counted as a
  record-order edge without an issued record.
- The result claims physical time, temporal issuance, causal-order replacement,
  source-law novelty, claim-ledger movement, public-posture movement,
  publication, or cross-repo truth.

## Contribution Needed

Run `python -m models.t587_t586_causal_collapse_boundary_attack --write-results`
and the focused unit test before treating T587 as the T586 causal-collapse
attack endpoint.
