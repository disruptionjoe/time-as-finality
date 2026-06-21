# Technical Report: Q1 Frontier Escape Matrix v0.1

## Claim Under Test

The Q1 branch has split into four narrowed child claims. T140 asks whether any
current child branch still offers a high-value internal quantum research route,
or whether Q1 should be treated as externally blocked until a branch-specific
escape condition is met.

## Artifact

T140 adds an executable decision matrix for:

- Q1A access-boundary record accounting;
- Q1B detector provenance admissibility;
- Q1C weak-measurement discriminator gate;
- Q1D contextuality/no-signalling guardrail.

The matrix does not score whether Time as Finality is true. It scores whether a
proposed quantum move is non-null under the gates already earned by T101,
T104, T105, T109, T118, T138, and T139.

## Result

The current frontier is:

| Branch | Current classification | Meaning |
| --- | --- | --- |
| Q1A | `bookkeeping_only` | No same-support fixed-data split survives after shared provenance partitioning, accessible-support reduction, branch-support collapse, and reversal-cost collapse. |
| Q1B | `externally_blocked_no_signed_manifest` | The only non-null detector path still lacks a named real deployment with a signed pre-event T136/T138 manifest. |
| Q1C | `null_screened_off_by_full_record` | No named platform supplies an auxiliary meter that remains verdict-changing after the full standard monitored record is fixed. |
| Q1D | `guardrail_only` | Contextuality/no-signalling constrains language but no nonredundant theorem target is named. |

Therefore:

```text
No current Q1 child branch has an active internal upgrade route.
Q1B is the only non-null experimental direction, but it is externally blocked.
```

## Current Strongest Claim

Q1 is a roadmap label, not a supported paper-facing quantum conjecture. The
strongest quantum-facing content is now procedural:

```text
Do not add another Q1 model unless it explicitly satisfies a child-branch
escape gate.
```

The useful gates are narrow:

- Q1A: same audited accessible support, shared provenance partition, fixed
  standard quantum-side summaries, and a physically justified verdict split.
- Q1B: real pre-event manifest plus real event-level packet, not scaffold
  language.
- Q1C: auxiliary axis not screened off by the full event-level ordinary record.
- Q1D: nonredundant theorem target beyond standard contextuality/no-signalling.

## What This Improved

T140 reduces route-selection ambiguity. Future quantum work can no longer
advance by citing the broad Q1 umbrella; it must declare which child gate it
targets and why the move is not already absorbed.

This also protects the long-run research program from overfitting the Q1
branch. The matrix says plainly when the highest-value move is to leave Q1 for
another route until external detector evidence or a genuine escape artifact
exists.

## What This Weakened Or Falsified

T140 weakens Q1 as an autonomous internal research line. The repo should not
present another internal Q1 finite witness as progress unless it clears one of
the escape gates.

It also weakens Q1B language: a valid workflow scaffold is not evidence. The
detector path becomes live only after a signed pre-event manifest is populated
with real rows and survives the packet and null-criterion gates.

## Falsification Condition

T140 fails if a current child branch already satisfies its listed escape gate,
or if a future branch-specific artifact satisfies an escape gate and the matrix
still classifies that branch as inactive.

## Claim Ledger Update

Add T140 to Q1:

```text
No current Q1 child branch has an active internal upgrade route. Q1B remains
the only non-null experimental path, but it is externally blocked pending a
signed pre-event manifest and real event-level packet.
```

## Open Blocker

No named detector deployment has signed the T136/T138 manifest pre-data, and
no Q1A/Q1C/Q1D escape artifact currently clears its branch gate.

## Next Work

Unless a Q1B deployment appears, the next autonomous run should leave Q1 and
attack a non-Q1 route. The best candidates are:

- thermodynamic arrow: try to derive or kill a physical free-energy/capacity
  version of H7 after T116/T122/T128/T124;
- spacetime reconstruction: test whether finite finality colimits can be tied
  to causal-set or domain-of-dependence constraints without smuggling in time.

## Reproduction

```bash
python -m unittest tests.test_q1_frontier_escape_matrix -v
python -m models.run_t140
```
