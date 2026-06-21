# Technical Report: Spin-Observerse Holonomy Step 2 v0.1

**Date:** 2026-06-20
**Test:** T112
**Model:** `models/t112_spin_observerse_holonomy.py`
**Unit tests:** `tests/test_t112_spin_observerse_holonomy.py`
**Results:** `results/spin-observerse-holonomy-step2-v0.1-results.md`

## Abstract

T112 formalizes a bounded finite/proxy audit for the T63 proposal that the CHSH
Cech holonomy can be realized as spin holonomy in the spin-observerse
`Y_spin`. The result is conditional: under H3 and a declared positive-generator
spin-lift convention, the CHSH majority-representative Cech holonomy `-1`
matches a `Z/2` spin-lift phase `-1`. The naive observerse `Y` remains a
negative control, T65's non-biconditional correction is preserved, and
representative dependence is explicit.

The audit does not validate Geometric Unity physics, does not derive quantum
probabilities, and does not prove a continuous bipartite Berry/solid-angle
theorem.

## Setup

The CHSH context loop is:

```text
A0B0 -> A0B1 -> A1B1 -> A1B0 -> A0B0
```

The declared angle convention is:

```text
A0 = 0
A1 = pi/2
B0 = pi/4
B1 = -pi/4
Eij = -cos(Ai - Bj)
S = E00 + E01 + E10 - E11
```

This gives:

```text
S = -2*sqrt(2)
abs(S) = 2*sqrt(2)
```

The implemented Cech transition function compares the shared setting outcome
on each adjacent edge of the CHSH cover. The holonomy is the product of the
four transition signs.

## H3 Identification Hypothesis

H3 remains the load-bearing hypothesis:

```text
finite CHSH Cech transition cochain
=
spin holonomy of the declared loop in Y_spin
```

T112 checks that both sides match as `Z/2` data under a declared finite proxy.
It does not prove that a general continuous GU field configuration realizes the
same loop.

## Topology Control

The audit encodes the T63 topology correction:

```text
pi1(naive Y) order: 1
nontrivial Z/2 holonomy available in naive Y: False
pi1(Y_spin) proxy order: 2
Z/2 spin-lift candidate available: True
```

Therefore the naive observerse `Y` cannot host the claimed nontrivial loop in
this fixture. The spin lift supplies only a candidate host, not a validation of
GU physics.

## Phase Control

The positive-generator spin-lift proxy maps each detector-setting change to a
positive `pi/2` spin-frame generator step:

```text
B0 -> B1: pi/2
A0 -> A1: pi/2
B1 -> B0: pi/2
A1 -> A0: pi/2
```

The total is `2*pi`, so:

```text
exp(i * 2*pi / 2) = -1
```

The signed closed-angle control is different. Using signed principal angle
changes, the total is `0`, giving phase `+1`. This is the key diligence result:
the sign `-1` depends on the declared spin-lift convention and H3.

## CHSH Representative Result

For the declared angles, all maximum-probability local representatives have
holonomy `-1`. The canonical representative is:

```text
A0B0: (+1, -1)
A0B1: (+1, -1)
A1B1: (+1, +1)
A1B0: (+1, -1)
```

Its transition pattern is:

```text
(+1, -1, +1, +1)
```

The product is `-1`, matching the spin-lift proxy sign under H3.

## T65 Causal Control

The exhaustive deterministic audit over all CHSH sections preserves T65:

```text
total deterministic sections: 256
locally causal sections: 16
all locally causal sections have holonomy +1: True
holonomy +1 sections: 128
non-LC holonomy +1 sections: 112
false biconditional restored: False
```

Thus T112 keeps the valid causal reading:

```text
holonomy -1 => not locally causal
```

and does not restore:

```text
locally causal <=> holonomy +1
```

## Representative Dependence

The full nonzero support of the probabilistic CHSH model contains both
holonomy classes:

```text
holonomy -1 support sections: 128
holonomy +1 support sections: 128
```

The majority-representative family is stable at holonomy `-1`, but arbitrary
support representatives are not. Therefore the CHSH holonomy claim must remain
representative-qualified.

## Verdict

The finite/proxy audit passes:

```text
naive Y negative control: pass
Y_spin Z/2 candidate: pass
declared spin-lift phase -1: pass
CHSH majority Cech holonomy -1: pass
T65 non-biconditional control: pass
representative-dependence control: pass
```

## Strongest Conditional Claim

Under H3 and the declared positive-generator spin-loop embedding, the CHSH Cech
obstruction is realized as `Z/2` spin holonomy.

## Not Claimed

- GU physics is validated.
- TaF derives quantum probabilities.
- TaF derives the Tsirelson bound.
- All contextuality is spin holonomy.
- Holonomy `+1` is equivalent to local causality.
- The signed closed detector path has phase `-1` without the declared lift.

## Open Blocker

The continuous bipartite Berry/solid-angle theorem is still open. A stronger
version of T112 would need to replace the positive-generator finite proxy with
an invariant continuous spin-frame path theorem whose solid angle and
orientation are specified without convention leakage.
