# 2026-07-02 - Computational-arrow record repair

Status: in progress. Run family: Progress.

## Context

The latest committed D2 setup created
`open-problems/computational-finality-arrow.md` and recorded the D2 swing as already
built and hostile-reviewed, but the referenced computational-arrow artifacts were
still untracked and used provisional `T418`, which collides with the registered
Schwarzschild horizon access-profile screen.

This run does not start a new claim lane. It repairs the repo-local record around
the already-created D2 swing so the negative result is coherent, rerunnable, and
non-colliding.

## Run Plan

Objective: preserve the computational-arrow negative result as a recorded-tier
artifact under a non-colliding number, while leaving North Star, claim ledger,
public posture, and cross-repo truth untouched.

Boundaries:

- Do not promote a claim.
- Do not edit `CLAIM-LEDGER.md`.
- Do not alter North Star, canon, hard policy, or public posture.
- Do not treat cryptography/number theory as physics evidence.
- Preserve the REDESIGN / K4-fired verdict.

Planned edits:

- Rename the untracked computational-arrow spec/results artifacts from `T418` to
  `T419`.
- Update the model and tests so the executable artifact records the K4 failure
  instead of asserting the failed anti-relabel guard.
- Reconcile the D2 open problem pointer to `T419`.
- Append steward memory and this run receipt.

Verification plan:

- Run focused computational-arrow tests.
- Run the model entrypoint.
- Check for stale old-number computational-arrow references.
- Run whitespace/diff checks.

## Execution Notes

- Renamed the untracked computational-arrow spec/results artifacts from `T418` to
  `T419`, preserving registered T418 as the Schwarzschild horizon access-profile
  screen.
- Updated `models/computational_arrow_of_time.py` so Leg 6 computes the actual
  trapdoor-free cycle predecessor by public forward iteration. The model now records
  K4 as fired instead of asserting an empty trapdoor-free backward set.
- Updated `tests/test_computational_arrow_of_time.py` to assert the REDESIGN
  verdict: K1 and K3 survive, but the period-4 toy orbit makes K4 fire.
- Reconciled the D2 open-problem status, the lead-line pointer, and the
  capability-boundary taxonomy note to say T419 is recorded as REDESIGN and D2
  remains open for redesign/abandon decision.
- Left `CLAIM-LEDGER.md` and `TESTS.md` untouched, matching the recorded-tier /
  no-promotion posture of the artifact.

## Verification

- `python -m pytest tests/test_computational_arrow_of_time.py -q` - 12 passed.
- `python -m models.computational_arrow_of_time | python -m json.tool > $null` -
  passed.
- `python -m pytest tests/test_computational_arrow_of_time.py tests/test_schwarzschild_horizon_access_profile_screen.py -q`
  - 20 passed.
- Stale old-number computational-arrow reference scan passed.
- `git diff --check` passed.

## Receipt

Completed. The repo now has a coherent T419 computational-arrow recorded-tier
artifact with a rerunnable negative verdict: the toy Rabin/BBS construction is
entropy-neutral and keeps the generic Rabin hardness leg, but it does not exhibit a
distinct computational arrow because public forward iteration reverses the short
cycle. No claim, North Star, canon, public-posture, or cross-repo truth movement.
D2 remains open only as a redesign/abandon decision.

Current run time: about 7 minutes.
