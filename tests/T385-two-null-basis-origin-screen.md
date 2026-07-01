# T385: Two-Null Basis Origin Screen

## Target Claims

D1, R1, S1, PO1, and the T384 `basis_origin` open object:

```text
Can exactly two primitive null compatibility-signal directions be derived from
compatibility alone, or are they better understood as the minimal shape of a
round-trip adapter?
```

## Setup

Compare targeted origin principles:

- absolute/global clock origin,
- scalar source-action origin,
- one-way signal origin,
- minimal round-trip handshake origin,
- overcomplete broadcast origin,
- signed cancellation origin,
- gauge/relabel origin.

## Success Criteria

- Reject origins that import global time.
- Reject scalar origins with no signal geometry.
- Reject one-way origins with no round-trip closure.
- Demote overcomplete origins that add extra primitive directions.
- Reject signed origins that require negative source counts.
- Identify whether the minimal handshake origin is only a motivation or a full
  compatibility-alone derivation.

## Failure Criteria

- Claim that compatibility alone has derived the two-null basis when the
  handshake premise is still imported.
- Treat a scalar source action as equivalent to signal geometry.
- Hide the round-trip acknowledgment premise.
- Let extra primitive directions pass as equally clean.

## Known Constraints

This is a finite origin-principle screen. It is not a completeness theorem over
all possible mathematical origins of the basis.

## Contribution Needed

If the minimal handshake origin survives, the next target is:

```text
derive or falsify why compatibility should require bidirectional
acknowledgment / round-trip closure in the first place.
```
