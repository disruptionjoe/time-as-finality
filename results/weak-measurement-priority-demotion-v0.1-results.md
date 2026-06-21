# T94 Results: Weak-Measurement Priority Demotion

## Route states

| Route | Real platform | Pre-registered raw-log protocol | Survives current null criterion | Independent axis named before analysis | Source-anchored candidate | Empirical deployment present |
| --- | --- | --- | --- | --- | --- | --- |
| detector provenance | True | True | True | True | True | False |
| weak measurement | False | False | False | False | False | False |

## Priority verdict

Preferred route: `detector_provenance`

Weak-measurement status: `demoted_below_detector_provenance`

Detector status: `active_but_not_empirically_upgraded`

Detector provenance retains a source-anchored, pre-registered, raw-log admissibility route that survives current null tests, while weak measurement has no named independent axis on a real platform.

## Strongest claim

Weak measurement should be demoted below detector provenance in the active Q1 roadmap. The detector route still has a source-anchored, pre-registered raw-log path that survives the current null criteria; the weak-measurement route has no real platform with an independent branch, provenance, or undo-cost axis.

## What this improved

T94 converts repeated prose demotion warnings into an explicit route-selection rule. Future runs can stop reopening null weak-measurement platforms unless they first satisfy the independent-axis gate.

## What this weakened

This weakens T12 strategically, not just locally. Weak measurement is no longer the default lead experimental route on the basis of promise alone.

## Falsification condition

T94 fails if a concrete weak-measurement platform names a pre-registered independent branch/provenance/undo-cost observable, not derived from the standard monitored record and not postselected, and that axis changes the TaF verdict while standard monitored statistics stay fixed.

## Q1 update

Keep Q1 partially supported, but demote T12 below detector provenance in the active roadmap until a monitored weak-measurement platform clears T90 and T93 with a real independent axis.

## Blocker

The repo still lacks the single object weak measurement needs most: a named platform with a pre-registered independent axis that survives same-record and postselection collapse.

## Recommended next

Advance detector provenance toward one real T78-style deployment, or reinstate weak measurement only after naming a concrete independent-axis platform with a raw-log schema.
