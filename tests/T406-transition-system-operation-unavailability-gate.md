# T406: Transition-System Operation-Unavailability Gate

## Target Claims

- [Region-Indexed Capability Discriminator](../open-problems/region-indexed-capability-discriminator.md)
- T400 boundary-forced task gate
- T403 same-domain finality-lock screen
- T405 physical-latch finality-lock screen
- T145 / T179 fixed-accounting future-operation absorber discipline

## Setup

Reuse the T405/T403 common-future final-verdict setup and hold fixed:

- causal-domain payload;
- joint payload;
- verdict payload;
- revision budget;
- declared operation menu;
- resource accounting;
- provenance;
- reversible-control class;
- observer boundary;
- non-dynamic substrate support.

The main pair varies only the finite operation-labeled transition relation:

```text
reachable case:   final_verdict_same --revise_verdict--> revised_verdict_same
unreachable case: no revise_verdict edge from final_verdict_same
```

The capability object is future operation availability for:

- reading the verdict;
- appending a correction;
- revising the final verdict;
- certifying the final record.

## Success Criteria

- The main pair has the same fixed-accounting projection.
- The main pair has the same operation menu, revision budget, and non-dynamic
  substrate support.
- The main pair has no resource, provenance, control, or boundary mismatch.
- The main pair splits only `can_revise_final_verdict`.
- The split is absorbed by transition-system completion.
- Matched transition-system completion implies matched capability in the
  finite fixture.
- Operation-menu, resource, provenance, control, boundary, hidden-label, and
  latch-topology shortcut controls classify correctly.
- The result says no claim-ledger movement is earned.

## Failure Criteria

The artifact fails if:

- two cases with identical transition-system completion split on revision
  capability;
- the main pair differs in causal payload, operation menu, resource,
  provenance, control, boundary, or non-dynamic substrate support;
- a hidden source label or latch-topology marker performs the split;
- transition-system completion does not restore factorization;
- the result is framed as a physical-arrow theorem or claim promotion.

## Known Physics Constraints

This is a finite absorber/precheck, not a physical-arrow theorem. It shows
that operation-unavailability language is not enough by itself: if the only
changed object is the transition relation, the residue is absorbed by native
transition-system completion.

## Contribution Needed

A future positive route needs a domain-native law or measured substrate
dynamics that forces the transition relation while the transition-system
completion relevant to the task is already matched. Otherwise the route
repeats operation-menu or transition-system underdescription.
