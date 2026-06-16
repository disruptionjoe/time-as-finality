# T12: Coupling-Profile Reconstruction

## Target Claims

- [M1: Coupling-Profile Reconstruction](../claims/M1-coupling-profile-reconstruction.md)
- [D2: Observer As Record-Bearing System](../claims/D2-observer-as-record-bearing-system.md)

## Question

Can two observers with different coupling profiles reconstruct different
temporal orders from the same underlying causal record graph, without
contradiction and without primitive time?

Secondary question: can constraint hardness separate unconditional physical
coupling from conditional interpretive binding?

## Setup

Extend the T1 model as a typed addition. No T1 source is modified.

- every record carries a channel tag `(channel, binding)`;
- `binding` is either `unconditional` or `conditional`;
- a coupling observer has a profile, meaning the set of channels that can
  affect it;
- an observer's coupled view contains only records on coupled channels;
- all holders are accessible to all observers, isolating coupling as the only
  varied factor;
- reconstruction runs the unmodified T1 machinery on the coupled view.

Scenario: propositions `A` and `C` use channel `grav`, proposition `B` uses
channel `em`, and proposition `D` uses channel `social`. `C` is causally
downstream of `A`, `B`, and `D`. The threshold is 2.

Definitions:

- `reach(x)` is the fraction of the population coupled to `x`'s channel.
- `hardness(x)` is the fraction of coupled observers constrained by `x`.
- `constrained` is not the same as `reconstructible`: an observer may
  reconstruct a conditional record without being bound by it.

## Success Criteria

1. At least two observers reconstruct different precedence relations from
   the same graph.
2. No observer's relation inverts the all-channel relation.
3. Observer pairs agree on propositions they can both reconstruct.
4. Matter-grade, narrow-unconditional, and idea-grade records are separated.
5. Some observer reconstructs an idea-grade proposition without being
   constrained by it.
6. No timestamps, global order, or experienced order are inputs.

## Failure Criteria

- Any reconstructed inversion versus the all-channel relation.
- All profiles yield identical relations.
- Hardness fails to separate `B` from `D`.

## Result

Status: implemented. All seven T12 unit tests pass inside the full T13 branch
suite.
