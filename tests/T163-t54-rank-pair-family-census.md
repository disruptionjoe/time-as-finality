# T163: T54 Rank-Pair Family Census

## Route

Spacetime reconstruction.

## Target Claims

- [S1: Spacetime As Consensus Envelope](../claims/S1-spacetime-consensus-envelope.md)
- [T126: Finality-Colimit Causal-Set Embeddability Audit](T126-finality-colimit-causal-set-embeddability.md)
- [T156: Myrheim-Meyer Ordering-Fraction Screen](T156-myrheim-meyer-ordering-fraction-screen.md)
- [T157: T54 Ordering-Fraction Bridge](T157-t54-ordering-fraction-bridge.md)
- [T159: T54 Interval-Jackknife Screen](T159-t54-interval-jackknife-screen.md)

## Question

Was the T157 six-event survivor just a hand-built fragile curiosity, or does
the full six-event T54 rank-pair family contain any deletion-stable members
that survive the current finite causal-set screens?

## Motivation

T159 demoted the original T157 witness to calibration-only because a single
event deletion pushed it outside the declared flat 1+1 ordering-fraction band.
That was a valid demotion of one witness, but not yet a family-level answer.

T163 turns the next blocker into an executable census:

```text
fix causal ranks 1..6
  -> vary information ranks over all 6! permutations
  -> complete each case through T54
  -> run T126, T156, and T159
  -> count blocked, fragile, and stable cases
```

## Setup

Each family member is a canonical two-observer T54 datum with:

- six shared global events;
- fixed causal-rank axis `1..6`;
- one information-rank permutation in `S_6`;
- identical observer views so the T54 completion burden is only the induced
  partial order, not observer disagreement.

The census is intentionally small and hostile. It does not ask for spacetime.
It asks only whether the smallest nontrivial T54 rank-pair family contains any
finite members that survive the current causal-set, ordering-fraction,
interval-support, and single-deletion screens.

## Success Criteria

- The census exhausts all `6! = 720` labeled information-rank permutations.
- Every case is completed through the same T54-to-T126/T156/T159 pipeline used
  by the named controls.
- The result reports how many cases:
  - block at T126;
  - pass T126 but fail T156;
  - pass T156 but fail parent-interval support;
  - pass parent-interval support but fail jackknife stability;
  - survive all current finite screens.
- The result states explicitly whether the original T157 rank pattern is still
  fragile.
- S1 is not upgraded beyond finite control language.

## Failure Criteria

T163 fails if:

- it samples instead of exhausting the six-event family;
- it changes the T54/T126/T156/T159 audit pipeline across cases;
- it treats labeled-case counts as a continuum theorem or generic causal-set
  result;
- it treats a surviving finite family member as spacetime evidence.

## Claim Impact

S1 remains `open_formal_target`.

The expected useful outcomes are either:

1. no deletion-stable survivors exist, further weakening the current S1
   finite boundary; or
2. a small surviving subfamily exists, shifting the next burden from
   "find any stable sample" to "explain, quotient, and stress-test the
   surviving family."

Either way, the result should be better than arguing from one hand-built
example.

## Reproduction

```bash
python -m unittest tests.test_t54_rank_pair_family_census -v
python -m models.run_t163
```
