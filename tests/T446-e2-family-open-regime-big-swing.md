# T446: E2 Family/Open-Regime Big Swing

## Route

D2 computational finality / computational arrow of time, after T438 admitted only
family-level period-hardness packets for the closed public-permutation regime and
T444 admitted changed-transition or open/nonpermutation packets only as separate
review targets.

## Question

Can an E2 computational-finality packet be made stronger than:

- T417 static relabel;
- T419/T420 finite-cycle toy reversal;
- pure ignorance of a transition;
- E1 thermodynamic or erasure cost;
- Brown-Susskind-style symmetric complexity growth?

## Candidate

Use an open Rabin-lift chain. For a public sequence of Blum moduli
`N_0, N_1, ...` with `N_{t+1} > N_t^2`, define:

```text
r_t = x_t^2 mod N_t
x_{t+1} = r_t^2 as an integer QR element in N_{t+1}
```

The transition law, moduli, domain tags, and lift inverse are public. The
factorizations of the `N_t` values are outside the reach. Reversal exists on the
image: first take the public integer square root of `x_{t+1}` to recover `r_t`,
then compute the principal square root of `r_t mod N_t`.

The forcing burden is Rabin square-root/factoring hardness at each current
modulus. The executable toy schedule is only an algebra sanity check, not
hardness evidence.

## Success Criteria

- Route the packet through T438/T444 correctly: not a closed public-permutation
  packet, but admitted for separate open-regime review.
- Exhibit public forward computation and trapdoor reversal over at least two
  chained steps.
- Preserve information on the declared image: reversal exists and is unique in
  principle.
- Avoid using toy non-recovery as evidence; record toy crackability honestly.
- Avoid pure ignorance by freezing the public transition law and audit trail.
- Avoid E1 by using injective/open dynamics, not erasure or thermodynamic cost.
- Avoid symmetric complexity growth by making Rabin inversion, not size growth,
  the named lock.
- Record the T417-chain residual rather than promoting the packet.

## Failure Criteria

- Treat a toy modulus as hardness evidence.
- Treat domain growth or state-size growth as the arrow.
- Treat unknown transition state as finality.
- Hide the transition policy, selector, or update law.
- Claim D2 is redesigned, abandoned, discharged, promoted, or public-ready.
- Edit `TESTS.md`, `CLAIM-LEDGER.md`, `ROADMAP.md`, North Star files, public
  posture, hard policy, shared context, governance files, or T442 files.

## Claim Impact

No claim movement. T446 is a recorded-tier packet swing only. It may identify a
candidate shape or a residual absorber, but it does not update the claim ledger
or decide D2 redesign/abandon.

## Reproduction

```bash
python -m pytest tests/test_e2_family_open_regime_big_swing.py -q
python -m models.e2_family_open_regime_big_swing --write-results
```
