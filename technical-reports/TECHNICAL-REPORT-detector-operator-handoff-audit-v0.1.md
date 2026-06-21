# Technical Report: Detector Operator-Handoff Audit v0.1

## Claim Under Test

T97 reduced detector-side Q1 to a locked pre-data packet. The next useful
question is operational rather than physical: can a realistic lab freeze and
populate that packet without role merges that turn trust auditing and demotion
into self-certification?

## Artifact

T98 adds an executable authority-domain audit over the T97 packet. It assigns
each T97 table family to one of five roles:

- analysis governor;
- instrument operator;
- control designer;
- archive custodian;
- trust auditor.

The audit then checks four staffing profiles:

- a fully separated five-domain profile;
- a lean four-domain profile with governance merged only with instrument
  operation;
- a three-person small-lab merge;
- a two-person PI-student merge.

## Result

Two profiles survive:

- the fully separated five-domain profile;
- the lean four-domain profile.

Both failing profiles collapse for operational, not physical, reasons:

- the trust auditor is also the archive or governance owner, creating
  self-audit;
- governance, control design, and archive custody are merged, allowing the
  same authority to define controls and certify the evidence channel.

## Current Strongest Claim

The surviving detector-side Q1 route is operationally admissible only if the
T97 packet is carried by at least four non-conflicting authority domains,
including an independent trust auditor. Common two- and three-person role
merges collapse the route into self-certification before any detector evidence
exists.

## What This Improved

T98 makes the dry-run detector route easier to kill honestly. Instead of
arguing abstractly about governance, a reviewer can now ask for one named
staffing plan and check whether trust auditing and archive/control governance
are genuinely independent.

It also identifies a lean admissible target. The route is not forced to use
five people, but it cannot collapse to a small lab where the same authority
defines controls, controls the archive, and certifies the audit.

## What This Weakened Or Falsified

This weakens detector-side Q1 again. The route now depends on organizational
separation, not just packet schemas and logs.

It also falsifies a likely shortcut: a filled T97 packet from a two- or
three-person merged-authority workflow should not count as detector-side Q1
support, even if its files look complete.

## Falsification Condition

Demote the detector branch if a realistic deployment cannot name at least four
non-conflicting authority domains with an independent trust auditor before the
first event, or if merged governance/control/archive roles are allowed to
certify the packet without independent review.

## Claim Ledger Update

Q1 should remain `partially_supported`, but narrowed again:

```text
Detector-side Q1 now requires at least four non-conflicting authority domains,
including an independent trust auditor. Common two- and three-person role
merges should demote the route before any event-level evidence is scored.
```

## Open Blocker

The repo still has no named lab deployment with a concrete operator split over
the T97 packet. The blocker is organizational realism: identify a staffing
plan that survives the handoff audit and can actually be executed pre-data.

## Next Work

Map one real lab organization onto the T97 packet:

- name the operator for each authority domain;
- name the trust auditor and why that role is independent;
- fix the signed handoff points between instrument, archive, and governance;
- reject the route if the lab requires merged governance/control/archive
  ownership.

## Reproduction

```bash
python -m unittest tests.test_detector_operator_handoff_audit -v
python -m models.run_t98
```
