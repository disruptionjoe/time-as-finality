# T400: Boundary-Forced Task Gate

## Target Claims

- [Region-Indexed Capability Discriminator](../open-problems/region-indexed-capability-discriminator.md)
- T397 region-indexed capability no-go
- T398 resource-profile absorber
- T399 boundary-crossing intervention statistics screen

## Setup

Use T399's two-qubit Bell-pair fixture as the substrate:

```text
phi_plus = (|00> + |11>) / sqrt(2)
psi_plus = (|01> + |10>) / sqrt(2)
```

T399 already proves the measurement side:

- every `R`-supported statistic and intervention statistic agrees;
- every boundary-local statistic agrees;
- a joint `RB` boundary-crossing menu separates the pair perfectly.

T400 adds a task-declaration audit on top of that substrate. The gate asks
whether the boundary-crossing menu is forced by the declared task/setup rather
than merely admitted as ordinary enlarged-state access.

Audited cases:

- T399-style optional state-label readout;
- synthetic relational parity task positive control;
- hidden-datum smuggling shortcut;
- closure-key shortcut;
- class-marker shortcut.

## Success Criteria

- T399's measurement facts are preserved exactly.
- The T399-style optional boundary menu fails the forced-task gate.
- A synthetic task whose declared output is the `R:B` parity relation passes
  the formal forced-task gate but remains marked as control-only.
- Hidden-datum, closure-key, and class-marker shortcuts fail with explicit
  absorber labels.
- The result says no claim-ledger movement is earned.

## Failure Criteria

The artifact fails if:

- it changes the T399 substrate facts;
- optional enlarged-state access passes the forced-task gate;
- the synthetic positive control is treated as a claim promotion;
- any shortcut case is allowed through the gate;
- the result is framed as new physics, a public posture change, or a top-line
  claim update.

## Known Physics Constraints

This is a finite task-gate artifact only. It does not supply a domain-native
physical or finality task. It does not claim that the Bell-pair parity control
is itself the desired Direction-A discriminator.

## Contribution Needed

Replace the synthetic relational control with a domain-native physical or
finality setup where the declared task forces the boundary crossing before the
state pair is selected.

