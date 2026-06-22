# T179 Results: Fixed-Accounting Capability Topology

## Theorem Candidate

For a fixed absorber vector A and a fixed future task F, a record-topology profile tau carries fixed-accounting capability residue exactly when two admissible states have the same A, different tau, and different F-availability. This residue is H7 physical-arrow evidence only under the stricter added condition that the reverse edge is physical_record_deletion with status constructor_impossible_after_full_accounting.

## Audit Table

| Case | Accounting matched | Topology split | Capability split | H7 candidate | Verdict |
| --- | --- | --- | --- | --- | --- |
| `same_accounting_branch_survival_split` | `True` | `True` | `True` | `False` | `fixed_accounting_capability_topology_residue` |
| `same_accounting_same_topology_control` | `True` | `False` | `False` | `False` | `no_capability_residue` |
| `changed_erasure_floor_absorber_control` | `False` | `True` | `True` | `False` | `absorber_owned_capability_split` |
| `provenance_loss_non_deletion_control` | `True` | `True` | `True` | `False` | `non_deletion_capability_split` |
| `constructor_impossible_positive_control` | `True` | `True` | `True` | `True` | `synthetic_h7_reinstatement_positive_control` |

## Residue Cases

- `same_accounting_branch_survival_split`

## H7 Candidates

- `constructor_impossible_positive_control`

## Strongest Claim

The T145 survivor is not a thermodynamic arrow, but it is a legitimate capability-kernel target: branch topology can matter for a future operation even when ordinary deletion accounting is matched. The useful next theorem is about minimal topology data needed for future capability, not about time's arrow.

## What Improved

T179 preserves the negative H7 verdict while extracting a precise positive object from it: fixed-accounting capability topology. It separates three gates that were easy to blur: absorber matching, future-capability split, and constructor-impossible physical deletion.

## What Weakened

This weakens any attempt to cite the T145 branch-topology split as physical-arrow evidence. The same finite pattern becomes formal capability residue unless the stricter reverse-status gate is cleared.

## Falsification Condition

The theorem target fails if fixed absorber vector plus topology profile is insufficient to determine the declared future task, or if a mature absorber shows that the topology profile is just a disguised thermodynamic, boundary, provenance, or control variable under the same comparison.

## Claim Ledger Update

Add T179 to H7/T129: the T145 fixed-accounting branch-topology split should be preserved as capability/topology residue and formalized as a minimal future-capability kernel target, while remaining explicitly non-evidence for H7 physical-arrow promotion.

## Open Blocker

No minimality theorem yet proves which record-topology fields are necessary and sufficient for a class of future tasks under matched thermodynamic and control accounting.

## Suggested Next

Prove or refute the finite minimality theorem: for branch-failure tasks, branch_support is the minimal topology coordinate that restores capability sufficiency at fixed absorber vector.
