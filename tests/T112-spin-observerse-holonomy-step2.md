# T112: Spin-Observerse Holonomy Step 2

**Status:** implemented as finite/proxy audit
**Route:** GU holonomy dictionary / contextuality and causal-boundary obstruction
**Artifacts:** `models/t112_spin_observerse_holonomy.py`,
`tests/test_t112_spin_observerse_holonomy.py`,
`results/spin-observerse-holonomy-step2-v0.1.json`,
`results/spin-observerse-holonomy-step2-v0.1-results.md`,
`TECHNICAL-REPORT-spin-observerse-holonomy-step2-v0.1.md`

## Question

Can the provisional T63 holonomy theorem be sharpened by formalizing the
bipartite Berry/solid-angle embedding of the CHSH context loop into the
spin-observerse `Y_spin`, while preserving the negative controls identified by
T63 and T65?

## Answer

Yes, but only as a conditional finite/proxy theorem.

Under H3 and the declared positive-generator spin-lift convention, the CHSH
majority-representative Cech holonomy `-1` is realized by a `Z/2` spin-lift
candidate phase `-1`. The naive observerse `Y` remains a negative control:
inside this fixture it has no nontrivial `Z/2` loop available for the same
claim.

This does not validate GU physics, derive quantum probabilities, derive the
Tsirelson bound, or prove an unconstrained continuous Berry/solid-angle
theorem. It sharpens the dictionary only.

## Declared Angle Convention

The implemented convention is:

```text
A0 = 0
A1 = pi/2
B0 = pi/4
B1 = -pi/4
S = E00 + E01 + E10 - E11
Eij = -cos(Ai - Bj)
```

The CHSH value is:

```text
S = -2*sqrt(2)
abs(S) = 2*sqrt(2)
```

The context loop is:

```text
A0B0 -> A0B1 -> A1B1 -> A1B0 -> A0B0
```

The spin-lift proxy declares each detector-setting change to be lifted as a
positive `pi/2` generator step in the spin frame. Four such changes give total
angle `2*pi`, so the spinor phase is:

```text
exp(i * 2*pi / 2) = exp(i*pi) = -1
```

## Load-Bearing Control

The signed closed-angle control gives total signed angle `0`, hence phase
`+1`. Therefore the positive-generator spin-lift convention is load-bearing.
This is why the result remains conditional under H3 rather than becoming a
free-standing continuous Berry-phase theorem.

## H3 Statement

H3 is the identification hypothesis:

```text
Cech transition cochain on the CHSH 4-cycle
=
spin holonomy of the declared Y_spin loop
```

T112 verifies that the two sides match as finite `Z/2` data under the declared
proxy. It does not prove that every continuous GU realization must implement
that proxy.

## T65 Controls Preserved

The finite exhaustive audit over all deterministic CHSH sections preserves the
T65 correction:

```text
locally_causal(s) => holonomy(s) = +1
holonomy(s) = +1 does not imply locally_causal(s)
```

Counts:

```text
total deterministic sections: 256
locally causal sections: 16
holonomy +1 sections: 128
non-LC holonomy +1 sections: 112
false biconditional restored: False
```

Thus T112 does not restore the false biconditional
`locally_causal <=> holonomy +1`.

## Representative-Dependence Control

For the declared CHSH angles:

- all maximum-probability local representatives have holonomy `-1`;
- the full nonzero support contains both holonomy classes;
- arbitrary support representatives split evenly: 128 with holonomy `-1` and
  128 with holonomy `+1`.

So the probabilistic CHSH holonomy statement is representative-qualified. The
strong claim applies to the declared majority-representative family, not to all
local section choices.

## Result

The finite/proxy audit passes:

```text
naive Y negative control: pass
Y_spin Z/2 candidate: pass
declared spin-lift phase -1: pass
CHSH majority Cech holonomy -1: pass
T65 non-biconditional control: pass
representative-dependence control: pass
```

## Claim Impact

T112 supports this conditional statement:

```text
Under H3 and the declared positive-generator spin-loop embedding,
the CHSH Cech obstruction is realized as Z/2 spin holonomy.
```

The continuous bipartite Berry/solid-angle theorem remains open. Before any
stronger promotion, the proxy should be replaced by an invariant continuous
spin-frame path theorem with explicit solid angle and orientation data.

## Guardrails

- GU is used as mathematical scaffolding, not validated physics.
- The finite CHSH Cech computation remains valid even if the GU embedding
  fails.
- T65's one-way causal reduction is the allowed physical reading.
- `holonomy +1` remains necessary but not sufficient for local causality.
