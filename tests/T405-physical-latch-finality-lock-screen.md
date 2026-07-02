# T405: Physical-Latch Finality-Lock Screen

## Target Claims

- [Region-Indexed Capability Discriminator](../open-problems/region-indexed-capability-discriminator.md)
- T400 boundary-forced task gate
- T401 finality-boundary reconciliation screen
- T402 causal-domain boundary forcing screen
- T403 same-domain finality-lock screen
- T145 / T179 fixed-accounting capability absorber discipline

## Setup

Reuse the T403 causal-domain and joint-payload setup:

```text
R input:                  t=0, x=-1
B input:                  t=0, x= 1
common-future verdict:    t=1, x= 0
joint payload:            11
verdict payload:          same
```

Replace T403's stipulated `provisional` versus `sealed` label with a finite
physical latch substrate:

```text
rewritable latch: material_topology = rewritable_gate, seal bridge open
fused latch:      material_topology = fused_gate,      seal bridge closed
```

The main pair matches:

- causal-domain signature;
- joint payload;
- verdict payload;
- revision budget;
- declared operation menu;
- resource accounting;
- provenance;
- reversible-control class;
- observer boundary;
- latch support fields other than topology.

The capability object is future operation availability for:

- reading the verdict;
- appending a correction;
- revising the final verdict;
- certifying the final record.

## Success Criteria

- The imported causal-domain signature matches T403/T402.
- The main pair has the same visible causal-payload projection.
- The main pair has the same fixed-accounting projection.
- The main pair has the same joint payload, verdict payload, revision budget,
  and operation menu.
- The main pair has no T145-style absorber-vector mismatch.
- The lock state is derived from latch topology, not from an accepted label.
- The capability split is only `can_revise_final_verdict`.
- Latch-substrate completion restores factorization.
- Resource, provenance, control, boundary, hidden-label, and stipulated-label
  controls classify correctly.
- The result says no claim-ledger movement is earned.

## Failure Criteria

The artifact fails if:

- the main pair differs in causal-domain data;
- the main pair differs in joint payload;
- the main pair differs in revision budget or operation menu;
- the main pair differs in resource, provenance, control, or boundary
  accounting;
- a stipulated finality label or hidden source marker performs the separation;
- the revision capability remains split after latch-substrate completion;
- the finite latch is framed as physical-arrow evidence or a claim promotion.

## Known Physics Constraints

This is a finite physical-substrate screen, not a physical-arrow theorem. It
shows that the post-T403 split can be made less stipulative by deriving the
lock state from latch topology, and that this split survives the fixed
resource/provenance/control/boundary projection. It is still absorbed by
explicit latch-substrate completion.

## Contribution Needed

A future upgrade needs a substrate-native irreversibility or operation-
unavailability result that does not factor through explicit latch topology,
resource state, provenance state, control handle, or observer boundary.
