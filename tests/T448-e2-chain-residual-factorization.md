# T448: E2 Chain Residual Factorization

## Route

D2 computational finality / E2 hardness lane, directly following T446.

T446 produced the strongest current positive packet: an open Rabin-lift chain.
Its residual was that the hard part may still be only chained T417/Rabin static
inversion. T448 tests that residual directly.

## Question

Does the T446 open Rabin-lift chain add any theorem beyond independent per-step
Rabin inversion?

## Candidate

For the T446 chain:

```text
r_t = x_t^2 mod N_t
x_{t+1} = r_t^2 as a public integer lift into N_{t+1}
```

invert the final chain state by:

1. public integer square-root unwrap of `x_{t+1}` to expose `r_t`;
2. one Rabin square-root inversion in the current modulus `N_t`;
3. repeat for each previous step.

Also embed a one-step Rabin challenge into a length-one T446 chain by mapping
`r -> r^2`, then checking that chain inversion recovers the ordinary Rabin
predecessor.

## Success Criteria

- Full-chain inversion recovers the T446 state sequence exactly.
- The number of step-oracle calls equals the number of transitions.
- Every nontrivial oracle call is a per-step Rabin square-root inversion in the
  current modulus.
- The public lift unwrap exposes each Rabin image before the step oracle is
  called.
- A length-one T446 chain embeds the ordinary T417/Rabin inversion problem.
- Changing the next lift domain while preserving lift room does not change the
  predecessor.
- Growth debt is recorded but not treated as the E2 lock.
- No D2 redesign/abandon, claim promotion, crypto theorem, physics claim, or
  public posture is asserted.

## Failure Criteria

- Full-chain inversion needs a global coupling oracle.
- The next domain affects the recovered predecessor under matched current
  modulus and Rabin image.
- The artifact treats toy arithmetic as hardness evidence.
- The artifact treats growth as the lock.
- The artifact edits `TESTS.md`, `CLAIM-LEDGER.md`, `ROADMAP.md`, North Star
  files, dirty governance files, public posture, hard policy, or T442 files.

## Claim Impact

No claim movement. T448 is a recorded-tier residual audit only. It may close the
current T446 open-chain packet as absorbed by chained T417/Rabin inversion, but
it does not decide the broader D2 redesign/abandon question.

## Reproduction

```bash
python -m pytest tests/test_e2_chain_residual_factorization.py -q
python -m models.e2_chain_residual_factorization --write-results
```
