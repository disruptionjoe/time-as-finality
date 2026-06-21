# Technical Report: Q1 Branch Adjudication v0.1

## Claim Under Test

Q1 has become an overloaded umbrella. It contains access-boundary record
accounting, detector provenance admissibility, weak-measurement discrimination,
and contextuality/no-signalling guardrails. T101 asks whether that evidence can
still support a single `partially_supported` quantum-physics claim.

## Artifact

T101 adds an executable adjudication over the current Q1 evidence set. It
assigns each branch:

- a proposed subclaim;
- a current status;
- earned content;
- not-earned content;
- a kill condition;
- a reinstatement condition;
- a next gate.

## Result

The single-claim presentation fails. Q1 should be split before paper-facing or
theorem-facing language treats it as one supported conjecture.

The branch verdicts are:

```text
Q1 umbrella: too broad for single partially-supported claim
Q1A access-boundary record accounting: survives as record accounting
Q1B detector provenance admissibility: externally blocked protocol admissibility
Q1C weak-measurement discriminator: dormant, reinstatement-only
Q1D contextuality guardrail: context only, not prediction
```

No branch currently earns new measurement dynamics or empirical quantum support.

## Current Strongest Claim

Q1 no longer behaves like one partially supported physics conjecture. Its
earned content splits into access-boundary record accounting, a blocked
detector-provenance admissibility protocol, a dormant weak-measurement
discriminator gate, and a contextuality/no-signalling guardrail. None currently
earns new measurement dynamics or empirical quantum support.

## What This Improved

T101 turns Q1 from an overloaded ledger line into a decision tree. A serious
reader can now see which parts are physics-facing, which are protocol-facing,
which are dormant, and which are only guardrails.

It also gives falsification teeth to the central quantum branch: each subclaim
now has its own kill or reinstatement gate instead of hiding behind the broad
Q1 status.

## What This Weakened Or Falsified

This weakens Q1 by rejecting the single-claim presentation. Detector provenance
remains externally blocked. Weak measurement is reinstatement-only.
Contextuality contributes discipline rather than novelty. The surviving
access-boundary content must compete directly with decoherence, Quantum
Darwinism, and ordinary causal reachability.

## Falsification Condition

T101 fails if one operational observable or theorem connects the
access-boundary, detector, and weak-measurement routes without branch-specific
rules; if a real detector packet passes T87/T97/T100 and yields a nonstandard
verdict; or if a weak-measurement platform names an independent pre-registered
axis satisfying T93.

## Claim Ledger Update

Q1 should remain only as an umbrella pointer until split:

```text
T101 shows that current Q1 evidence no longer supports treating Q1 as one
partially supported physics conjecture. Split it into Q1A access-boundary record
accounting, Q1B detector provenance admissibility, Q1C dormant weak-measurement
discriminator gate, and Q1D contextuality guardrail before paper-facing use.
No branch currently earns new measurement dynamics or empirical quantum support.
```

## Open Blocker

The project must decide whether to create separate claim files for Q1A-Q1D or
to demote Q1 to a roadmap umbrella. Without that split, the ledger hides
incompatible evidence standards inside one status label.

## Next Work

Implement the Q1 split in the claim ledger and write the Q1A literature
comparison against decoherence, Quantum Darwinism, consistent histories,
relational quantum mechanics, QBism, and many-worlds.

## Reproduction

```bash
python -m unittest tests.test_q1_branch_adjudication -v
python -m models.run_t101
```
