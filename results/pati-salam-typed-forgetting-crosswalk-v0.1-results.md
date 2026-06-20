# T88 Results: Pati-Salam Typed Forgetting Crosswalk

Strongest claim: The GU Pati-Salam verification supplies a clean external typed-forgetting witness for TaF: the 16-state carrier and B-L data survive the naive projection, but the forgotten T3R term is load-bearing for the Standard-Model hypercharge invariant.

Weakened claim: T88 does not validate GU physics, TaF physics, Q1, H1, H7, or spacetime reconstruction. It imports only a finite representation arithmetic witness for typed structure preservation.

## Transport comparison

| Map | Rule | LossKernel | Exact table match | n values | Verdict |
| --- | --- | --- | --- | --- | --- |
| standard_pati_salam_to_sm | `Y = T3R + (B-L)/2` | empty | True | -4, -3, 0, 1, 2, 6 | exact_table_reconstruction |
| b_minus_l_only_projection | `Y' = (B-L)/2` | SU2R_cartan_T3R, right_isospin_splitting | False | -3, -1, 1, 3 | typed_forgetting_failure |

## Standard multiplets

| SU3 | SU2_L dim | n=6Y | Dim |
| --- | ---: | ---: | ---: |
| 3 | 2 | 1 | 6 |
| 3bar | 1 | -4 | 3 |
| 3bar | 1 | 2 | 3 |
| 1 | 2 | -3 | 2 |
| 1 | 1 | 0 | 1 |
| 1 | 1 | 6 | 1 |

## B-L only projection multiplets

| SU3 | SU2_L dim | n=6Y' | Dim |
| --- | ---: | ---: | ---: |
| 3 | 2 | 1 | 6 |
| 3bar | 1 | -1 | 6 |
| 1 | 2 | -3 | 2 |
| 1 | 1 | 3 | 2 |

## Loss attribution

Within the tested map family, the failure is attributable to a non-empty LossKernel naming SU2R_cartan_T3R. Restoring T3R in Y = T3R + (B-L)/2 restores the exact table.

## PO1 status

not_a_po1_instance_without_gluing_object: this is an invariant reconstruction failure under typed forgetting, not yet a D1RestrictionSystem local-to-global obstruction.

## Falsification condition

Reject this crosswalk if B-L alone reproduces the paper n=1 multiplet table, if the full Pati-Salam map fails to reproduce the table, or if the failure can be repaired without restoring a right-isospin-equivalent term.

## TaF update

TF1 gains a narrow external mathematics witness: named forgotten structure can be necessary for preserving a downstream invariant. No current TaF physics claim is upgraded.

## Next move

If this route is continued, reformulate the Pati-Salam table as a typed transport object with source, target, preserved invariants, and LossKernel fields; only then ask whether it can be embedded in PO1-style gluing machinery.
