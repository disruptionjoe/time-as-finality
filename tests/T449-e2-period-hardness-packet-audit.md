# T449: E2 Period-Hardness Packet Audit

## Route

D2 computational finality / E2 hardness lane, after T448 absorbed the T446 open
Rabin-lift route as chained T417/Rabin inversion.

T438 said the remaining closed public-permutation path must be a predeclared
family-level period-hardness packet. T449 makes that packet exact.

## Question

Can the D2 route be narrowed to a true closed-regime period-hardness theorem
target rather than another finite toy, point-inversion relabel, or open-chain
variant?

## Candidate

Use BBS-style public squaring on the finite group `QR_N` for a Blum integer
`N = p*q`:

```text
F_N(x) = x^2 mod N
F_N^t(x) = x^(2^t) mod N
```

For seed order `d = ord_N(x)`, the orbit period under squaring is:

```text
L = ord_d(2)
```

If `L` is known, predecessor recovery is public:

```text
predecessor(y) = F_N^(L-1)(y)
```

The proposed E2 burden is therefore hidden-order / cycle-length hardness for
the public squaring family, not point square-root inversion alone.

## Success Criteria

- The packet clears T438 only as a future theorem target, not as D2 success.
- The period formula matches public cycle discovery in the toy family.
- Known period publicly recovers predecessors.
- QR group-order completion is recorded as trapdoor completion, because `N` and
  `|QR_N|` recover `p,q` in the semiprime toy.
- Small-period seed controls are rejected as evidence.
- The result records the missing theorem obligation rather than treating finite
  arithmetic as hardness evidence.
- No D2 redesign/abandon, claim promotion, crypto theorem, physics claim, or
  public posture is asserted.

## Failure Criteria

- Treat bounded toy non-recovery as evidence.
- Treat a single fixed finite instance as a physical boundary.
- Treat point square-root inversion alone as the temporal result.
- Smuggle group order, cycle decomposition, factors, or seed selection as public
  data without recording completion.
- Omit seed-distribution or small-period controls.
- Edit `TESTS.md`, `CLAIM-LEDGER.md`, `ROADMAP.md`, North Star files, dirty
  governance files, public posture, hard policy, or T442 files.

## Claim Impact

No claim movement. T449 is a recorded-tier period-hardness packet audit only. It
sharpens the remaining D2 route to a hidden-order cycle-length theorem target.
It does not prove that target and does not decide D2 redesign/abandon.

## Reproduction

```bash
python -m pytest tests/test_e2_period_hardness_packet_audit.py -q
python -m models.e2_period_hardness_packet_audit --write-results
```
