# Technical Report: Detector Challenge-Window Freeze Screen v0.1

## Claim Under Test

T175 left Q1B with one narrow live governance shape: a pre-data quorum map in
which archive custody, escrow, and trust are mandatory guardians of the
critical challenge-window actions.

T176 asks whether that static map is enough.

## Result

The finite answer is no:

```text
if guardian identity or critical challenge-window rights can be changed after
data collection begins, the static T175 quorum map is scaffold-only
```

The only live profile in the current fixture family is a fully frozen
challenge-window policy.

## Why This Matters

Without T176, Q1B still has a practical escape hatch. A collaboration can
publish an admissible initial quorum map, then reserve break-glass override,
temporary trust suspension, or guardian replacement for the exact period when
review rights are supposed to protect outside scrutiny.

That would leave the repo talking as if rights were fixed when they are really
contingent on later policy moves.

## Finite Screen Shape

Start from a T175-valid static guardian map and ask whether any of the
following can change during the challenge window:

- row-release quorums;
- revocation quorums;
- audit quorums; or
- guardian identity itself.

If yes, the current finite audit treats the route as null for Q1B.

## Audited Cases

### 1. Fully Frozen Challenge-Window Policy

No challenge-window mutation is allowed.

Result:

```text
live finite control
```

This is the only surviving profile.

### 2. Governance Break-Glass Release Override

Governance can temporarily authorize release outside the predeclared guardian
path.

Result:

```text
null mutable challenge-window rights
```

The initial T175 map no longer determines who actually controls row review.

### 3. Mid-Window Escrow Replacement

The named escrow authority can be replaced after collection but before review
closes.

Result:

```text
null mutable guardian identity
```

Independent escrow becomes a revocable label, not a fixed guardian.

### 4. Trust Suspension Before Revocation

The trust auditor can be suspended during a dispute and then bypassed.

Result:

```text
null mutable revocation rights
```

### 5. Post-Dispute Guardian Addition

A new substitute guardian can be inserted after challenge begins.

Result:

```text
null mutable audit rights
```

The pre-data guardian map no longer fixes who controls review.

## What T176 Improves

T176 converts "publish the quorum map" into a stronger and more realistic ask:

```text
publish the quorum map and freeze it for the whole challenge window
```

That makes the remaining Q1B route easier to falsify operationally.

## What T176 Weakens

It weakens the last surviving Q1B governance story.

A workflow no longer counts just because it starts with the right guardians.
If it keeps emergency policy mutation or guardian rotation available during the
review period, the rights are conditional and Q1B stays blocked.

## Boundary Of The Result

This is a finite governance screen, not a universal statement about all real
laboratory security operations.

The current result says only that, within the repo's surviving Q1B route, a
mutable challenge-window policy does not support the kind of outside review
rights the branch now requires.

This should not be read as a claim that emergency, legal, or safety procedures
are illegitimate in real detector collaborations. The narrower red-team point
is that any such procedure exits the current Q1B claim-review route unless it
is predeclared and audited as a preserved-rights successor policy. In
particular, the successor policy must still show that archive custody, escrow,
and trust cannot be bypassed on the critical release, revocation, and audit
actions.

## Falsification Condition

T176 fails if a workflow should still count for Q1B even though it can change
guardian identity or critical challenge-window release, revocation, or audit
rules after data collection begins.

## Open Blocker

The repo has no named detector workflow that exposes a signed pre-data freeze
policy proving that challenge-window guardians and critical rights cannot be
changed after collection.

## Claim Ledger Update

Q1B remains `externally_blocked`.

Add this sharpening:

```text
Static guardian quorums are scaffold-only if release, revocation, audit, or
guardian-identity rules can be rewritten during the challenge window.
```

## Recommended Next Move

Update the Q1B handoff to require a signed challenge-window freeze policy in
addition to the T175 quorum map. If realistic groups need break-glass
override or mid-window guardian rotation, demote Q1B below the active
frontier.
