# T112 Results: Spin-Observerse Holonomy Step 2

## Verdict

- Finite/proxy audit passed: `True`
- H3 status: conditional: H3 must identify the finite Cech transition cochain with the declared Y_spin spin-holonomy loop

## Strongest conditional claim

Under H3 and the declared positive-generator spin-lift convention, the CHSH majority-representative Cech holonomy -1 is realized by the Z/2 spin-lift candidate phase -1. The naive observerse Y control blocks the same claim without the spin lift.

## Topology controls

- Naive `Y` nontrivial Z/2 holonomy available: `False`
- `Y_spin` Z/2 candidate available: `True`
- Verdict: Naive Y is the negative control; only the spin lift supplies a Z/2 candidate host for the loop.

## Phase and CHSH sign

- Angle convention: `T112_standard_chsh_positive_generator_spin_lift`
- CHSH formula: S = E00 + E01 + E10 - E11 for singlet Eij = -cos(Ai-Bj)
- CHSH value: `-2.8284271247461903`
- `abs(CHSH) = 2*sqrt(2)`: `True`
- Positive-generator total angle: `6.283185307179586`
- Positive-generator Z/2 phase sign: `-1`
- Signed closed-angle control sign: `1`
- Convention is load-bearing: `True`
- Phase verdict: The declared positive-generator spin lift gives phase -1. The signed closed-angle control gives +1, so the lift convention and H3 identification are load-bearing.

## T65 causal controls

- Total deterministic sections: `256`
- Locally causal sections: `16`
- LC sections all have holonomy +1: `True`
- Holonomy +1 sections: `128`
- Non-LC holonomy +1 sections: `112`
- False biconditional restored: `False`

## Representative controls

- Full support sections: `256`
- Full support holonomy counts: `{'-1': 128, '1': 128}`
- Majority representatives all holonomy -1: `True`
- Representative dependence present: `True`
- Verdict: All maximum-probability representatives for the declared CHSH angles have holonomy -1, but the full nonzero support contains both holonomy classes. The probabilistic CHSH holonomy statement is therefore representative-qualified.

## Not claimed

- GU physics is validated
- quantum probabilities or Tsirelson's bound are derived from TaF
- all contextuality is spin holonomy
- holonomy +1 is equivalent to local causality
- the signed closed detector path has phase -1 without the declared lift

## Open blocker

The continuous bipartite Berry/solid-angle theorem is still not proved. This artifact only audits the finite spin-lift proxy and makes the H3/convention dependence explicit.

## Recommended next

If promoted, replace the finite positive-generator proxy with a continuous spin-frame path theorem whose solid angle and orientation are invariantly specified.

## Claim boundary

T112 sharpens the T63 dictionary conditionally. It preserves T65's one-way causal reading and leaves the false LC iff holonomy +1 biconditional false.
