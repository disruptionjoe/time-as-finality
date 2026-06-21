# Technical Report: Constructor-Admissibility Grounding Audit v0.1

## Claim Under Test

T18 proves a conditional constructor theorem: if admissible transformations are
monotone in D1, strict finalization has an impossible reverse. T124 asks whether
that admissibility rule is physically grounded in the existing H7 witness
families, or whether it imports the arrow through resource accounting,
coarse-graining, exported history, hidden environment, omitted return path, or
stipulation.

## Result

The executable audit produces a reverse-edge ledger for the current H7 stack:

- T18: valid formal theorem, but the reverse is impossible by premise.
- T80: raw reversible local dynamics can decrease D1; the inverse exists in the
  same closed state space.
- T84: monotone cyclic accounting needs exported history or erasure.
- T106: bounded-sink monotonicity is a forward-branch resource curve; the closed
  sink/unwind cycle has a return-path decrease.
- T110: finite closed reversible orbits cannot carry a strict scalar monotone.
- T116: open stochastic record arrows are paid for by path irreversibility,
  exported history, or fresh blank capacity.
- T122: stationary Markov upward moves are balanced by downward drift elsewhere.
- T128: finite resource drawdown is the strongest non-stipulative survivor, and
  constructor restriction survives only by excluding the reverse by rule.

## Strongest Claim

H7 can be used only as an audited admissibility ledger: every strict
D1-increasing edge must classify the reverse edge under the same accounting
boundary. Current witnesses permit only constructor-only or resource-accounting
readings, never an unqualified physical arrow.

## What Improved

T124 converts the phrase "admissible transformation" into a concrete review
gate. A proposed H7 upgrade must now state:

```text
forward edge
D1 delta
accounting boundary
reverse edge
reverse status
named resource, boundary, or impossibility condition
```

That makes hidden thermodynamic, memory, sink, export, and coarse-graining
assumptions explicit before H7 can be strengthened.

## What This Weakened Or Falsified

No existing H7 witness grounds a new thermodynamic arrow. The best
non-stipulative survivor is T128 resource drawdown; the formal constructor
survivor works only by excluding the reverse by rule.

## Falsification Condition

T124 is falsified, and H7 could strengthen, by a finite or physically calibrated
record substrate with a strict D1-increasing edge whose reverse is
constructor-impossible under the same full state accounting, without relying on
omitted environment, sink capacity, erasure, postselection, coarse-graining,
stationarity violation, or stipulated admissibility.

## Claim Impact Recommendation

Preserve H7 as a constructor/resource-accounting lemma. Do not present it as a
thermodynamic-arrow derivation unless a future model clears the reverse-edge
grounding gate.

## Open Blocker

The missing upgrade is a physically grounded constructor-impossibility relation
for record deletion or definalization that does not reduce to ordinary
resource, entropy, boundary, or coarse-graining accounting.

## Reproduction

```bash
python -m unittest tests.test_constructor_admissibility_grounding_audit -v
python -m models.run_t124
```
