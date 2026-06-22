# Technical Report: Detector Preserved-Rights Successor Policy Screen v0.1

## Claim Under Test

T176 killed mutable challenge-window governance by default, but it left a
narrow realism question open:

```text
can a predeclared legal, safety, or emergency successor policy preserve the
same review rights without reopening post-data override?
```

T178 answers that question inside the surviving Q1B detector-governance route.

## Result

The finite answer is narrow:

```text
yes, but only for a predeclared preserved-rights successor policy
```

More precisely, a successor path remains live only when it:

- is fixed before data collection;
- has explicit trigger conditions;
- preserves the same mandatory archive, escrow, and trust guardians on every
  critical release, revocation, and audit action;
- preserves already-granted full row-review access during the challenge
  window;
- preserves guardian identity; and
- emits immutable transition logs.

Generic emergency or legal override language does not count.

## Why This Matters

Without T178, the repo sits in an awkward place:

- literal no-exception freeze risks making Q1B unrealistic for reasons the
  project has not actually audited;
- generic exception language simply reopens the T176 loophole.

T178 replaces that ambiguity with a typed boundary.

## Finite Screen Shape

Start from a T175-valid, T176-frozen challenge-window policy and classify
successor paths into three buckets:

1. no successor path at all;
2. preserved-rights successor path;
3. rights-reducing or undeclared successor path.

The positive case is intentionally strict. It is not enough for the successor
to be "documented" or "well intentioned." It must preserve the same rights the
freeze burden was introduced to protect.

## Audited Cases

### 1. Fully Frozen, No Successor Path

Result:

```text
live frozen control
```

This remains live for the same reason as T176.

### 2. Predeclared Preserved-Rights Legal-Hold Successor

Result:

```text
live preserved-rights successor
```

This path mirrors the same full row review into a sealed review room, keeps
the same archive, escrow, and trust guardians, keeps their identities fixed,
and writes the transition to an immutable log.

### 3. Undeclared Break-Glass Successor

Result:

```text
null undeclared override
```

The route was not frozen pre-data, so it collapses back into the T176
loophole.

### 4. Predeclared Review Pause Pending Governance Clearance

Result:

```text
null review-rights reduction
```

Even with the same guardians, a successor that pauses outside row review makes
the rights contingent rather than preserved.

### 5. Predeclared Escrow Rotation Successor

Result:

```text
null guardian-identity change
```

Independent escrow becomes a replaceable label rather than a fixed guardian.

### 6. Predeclared Revocation Override Successor

Result:

```text
null critical-action guardian bypass
```

A successor path cannot preserve Q1B while letting governance close challenge
rights without the trust-and-escrow pair.

## What T178 Improves

T178 improves Q1B in two ways:

1. It avoids overfitting to literal immutability.
2. It prevents "we have emergency procedures" from functioning as an
   untyped escape hatch.

That makes the external ask more realistic and more falsifiable at once.

## What T178 Weakens

It weakens the remaining practical stories a collaboration could tell without
showing its actual review-rights design.

After T178, the repo should not treat the following as meaningful progress:

- generic legal-hold language;
- generic safety pause language;
- escrow replacement authority;
- governance-only revocation override; or
- any successor path whose trigger and log format are not frozen pre-data.

## Boundary Of The Result

This is still a finite governance screen. It does not claim that real detector
collaborations can never operate under legal or safety constraints. It says
only that, within the surviving Q1B branch, such constraints count only when
they preserve the exact review rights Q1B now says matter.

## Falsification Condition

T178 fails if a detector workflow should still count for Q1B even though its
successor path is undeclared, rights-reducing, guardian-changing, critical-
action-bypassing, or unlogged.

## Open Blocker

The repo still has no named detector workflow that publishes either:

- a fully frozen challenge-window policy; or
- a predeclared preserved-rights successor policy package

before data collection begins.

## Claim Ledger Update

Q1B remains `externally_blocked`.

Add this sharpening:

```text
Challenge-window exception procedures count only when they are predeclared
preserved-rights successor policies with fixed triggers, fixed guardians,
preserved full row-review access, and immutable transition logs.
```

## Recommended Next Move

Update the Q1B handoff so that emergency, legal, or safety exceptions must
either be absent or arrive as a T178-valid preserved-rights successor policy
package. If realistic groups cannot meet even that narrowed exception class,
Q1B should continue to lose priority relative to non-detector routes.
