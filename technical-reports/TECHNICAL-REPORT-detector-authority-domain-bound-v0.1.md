# Technical Report: Detector Authority-Domain Bound v0.1

## Claim Under Test

T98 showed that some staffing profiles preserve the locked T97 detector packet
while common small-lab merges collapse it into self-certification. The open
question is whether that was merely example-driven or whether the packet has an
exact combinatorial lower bound on the number of authority domains.

## Artifact

T100 enumerates every set partition of the five T97 authority domains:

- analysis governor;
- instrument operator;
- control designer;
- archive custodian;
- trust auditor.

It then rejects any partition that violates either of the active T98
constraints:

- trust auditor cannot share an authority with any audited domain;
- analysis governance, control design, and archive custody cannot merge with
  each other.

## Result

The lower bound is exact:

```text
minimum admissible authority domains = 4
```

No partition with three or fewer authority domains survives.

There are exactly three admissible four-domain merge classes:

```text
instrument operator + analysis governor
instrument operator + control designer
instrument operator + archive custodian
```

plus the fully separated five-domain profile.

## Current Strongest Claim

The detector-side Q1 route now carries a hard operational obstruction, not a
soft staffing preference. Under the current T97/T98 packet, no two- or
three-person authority split can avoid trust self-audit or
governance/control/archive self-certification. The route is admissible only
with at least four authority domains, and the only minimal surviving profiles
merge instrument operation with exactly one other non-auditing role.

## What This Improved

T100 upgrades T98 from example profiles to a complete finite audit. A serious
reader no longer has to trust that the selected profiles were representative.
The full search shows exactly which merges survive and which fail.

This also sharpens falsifiability. A proposed detector deployment can now be
checked against a short list of admissible merge classes before anyone argues
about data quality, provenance payloads, or D1 scoring.

## What This Weakened Or Falsified

This weakens the detector branch again. The surviving path is not just
governance-heavy; it has an exact staffing lower bound. Any future claim that a
small lab will "eventually" run the T97 packet must now answer a concrete
question: where do the four authority domains come from?

It also blocks a common ambiguity. The four-domain profile used in T98 is not
special, but the space of admissible escapes is still tiny. If a deployment
does not match one of the three minimal merge classes or full separation, it
should be demoted before data collection.

## Falsification Condition

T100 fails if either of the following occurs:

1. the T97 packet is revised so that an admissible partition with three or
   fewer authority domains exists without allowing trust self-audit or
   governance/control/archive self-certification; or
2. a real deployment shows that one of T98's current separation constraints is
   unnecessary and can be removed without reopening post hoc certification.

## Claim Ledger Update

Q1 should remain `partially_supported`, but its detector branch should be
narrowed again:

```text
Under the current T97/T98 packet, detector-side Q1 has a hard four-authority
lower bound. Any proposed deployment with fewer than four non-conflicting
authority domains should be rejected before event-level evidence is scored.
```

## Open Blocker

The repo still lacks a named real lab organization that actually fits one of
the three minimal four-domain patterns while freezing the T97 packet pre-data.

## Next Work

Map one real lab workflow onto each minimal four-domain class and ask whether
the role split is operationally realistic:

- instrument plus governance;
- instrument plus control design;
- instrument plus archive custody.

If none is realistic, demote detector provenance below the active Q1 frontier
and stop treating the route as a near-term experiment candidate.

## Reproduction

```bash
python -m unittest tests.test_detector_authority_domain_bound -v
python -m models.run_t100
```
