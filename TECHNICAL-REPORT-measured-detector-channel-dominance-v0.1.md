# Technical Report: Measured Detector Channel Dominance v0.1

## Claim Under Test

T81 showed that trust boundaries and pre-registration are load-bearing in the
current measured detector audit. The next question is whether any of the
remaining measured categories can independently change the detector verdict, or
whether the schema still overstates its own breadth.

## Artifact

T85 holds the signed T76 fixture's trust and pre-registration values fixed and
builds three hostile single-category stress families:

- spoof/unique-tag stress;
- perturbation stress;
- DAG-observability stress.

Each family changes only one T81 category and reruns the T74 Monte Carlo audit.

## Result

The current detector branch narrows again.

- A hostile spoof/unique-tag family independently demotes the signed fixture
  from robust recovery to conservative withhold.
- Even hostile perturbation and DAG single-category families do not demote the
  signed fixture while authenticated tags, trust boundaries, and
  pre-registration remain intact.

The executable detector route therefore behaves more like:

```text
pre-registration gate
  + trust-boundary gate
  + authenticated-tag sufficiency
```

with perturbation and DAG channels presently auxiliary rather than independent
decision axes.

## Current Strongest Claim

The current measured detector route is narrower than the T76 schema suggests.
After trust-boundary and pre-registration gates are fixed, spoof/unique-tag
evidence can still independently demote the signed fixture, but perturbation
and DAG evidence do not become decisive on their own inside the present witness
family.

## What This Improved

T85 replaces a vague blocker with a sharper obstruction. The repo can now say
which residual detector-evidence category still matters on its own and which
ones remain unearned in the executable audit.

This also gives a clean next falsification target: either construct a family in
which perturbation or DAG evidence alone changes the verdict, or remove them
from the core detector schema.

## What This Weakened

T85 weakens any claim that the detector branch already uses perturbation
response or DAG observability as peer load-bearing channels. In the current
family they are not independently decisive once authenticated tags are strong.

That means the detector branch is not yet a broad measured-provenance schema.
It is a narrower admissibility filter anchored mostly by trust, pre-registration,
and authenticated tags.

## Falsification Condition

This report fails if either of the following happens:

1. a single-category perturbation or DAG stress family changes the signed
   fixture's verdict while trust and pre-registration stay fixed;
2. the spoof/unique-tag stress no longer changes the verdict.

The first outcome would show T85 is still too pessimistic about those channels.
The second would show the present narrowing is unstable.

## Claim Ledger Update

Q1 should remain `partially_supported`, but its detector branch should now be
stated more narrowly:

```text
The current executable detector route behaves mainly as a pre-registration
gate, a trust-boundary gate, and an authenticated-tag sufficiency test.
Perturbation and DAG evidence remain motivated but not yet independently
decisive in the witness family.
```

## Open Blocker

The current witness family leaves authenticated tag channels already strong
enough to settle provenance when perturbation or DAG evidence degrades. That
prevents those channels from becoming independently decisive.

## Next Work

Construct a hostile raw-log family in which authenticated tags are
intentionally ambiguous but one of the following still separates copied from
independent records on its own:

- perturbation response;
- signed ancestry / DAG observability.

If no such family can be built honestly, compress the detector schema again and
remove those channels from the branch's core statement.

## Reproduction

```bash
python -m unittest tests.test_measured_detector_channel_dominance -v
python -m models.run_t85
```
