# T204 Results: Same Path Harmonic, Different Edge Congestion Family

## Outcome

`promoted`

## Main Readout

Both systems have free path times `{2,2}` and harmonic mean `2`, but the
corrected capacity-aware value differs.

## Verdict: promoted

| System | Structure | Corrected value |
| --- | --- | ---: |
| D | disjoint paths | `C_flow = 8/3` |
| S | shared prefix bottleneck | `C_flow = 10/3` |

## Result

The unweighted path harmonic cannot be a sufficient statistic for overlapping
finite DAG capability.

## Repo-Safe Reading

This promotes edge congestion as required state completion, not as independent
MTI residue.
