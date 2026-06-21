# T98: Detector Operator-Handoff Audit

## Route

Quantum measurement / classical records.

## Question

After T97 reduced the detector branch to a locked dry-run packet, can a
realistic lab populate that packet without collapsing the trust audit,
preregistration, control declaration, and archive custody into self-audited
role merges?

## Motivation

The next uncertainty is operational. T97 specified schemas and hashes, but a
skeptical reviewer should also ask who is allowed to own each table and who is
allowed to audit whom. If the same authority defines controls, certifies the
archive, and signs the trust audit, the packet has not escaped post hoc
self-certification.

## Success Criteria

- The T97 packet is split into explicit authority domains.
- At least one lean but admissible staffing profile is identified.
- Common two- and three-person role merges are rejected when they create
  self-audit or governance/control/archive conflicts.
- The result states the minimal operational separation needed before any
  detector evidence can count.

## Failure Criteria

- Trust auditing is allowed to be performed by the same authority that owns the
  audited packet components.
- Governance, control design, and archive custody are merged without penalty.
- The result is described as empirical detector support rather than a
  pre-evidence admissibility filter.

## Claim Impact

If T98 passes, Q1 remains `partially_supported`, but the detector route narrows
again: the T97 packet is admissible only with enough authority separation to
avoid self-certification.

If no realistic staffing split survives the audit, detector provenance should
be demoted below the active Q1 frontier without collecting more synthetic
fixtures.

## Reproduction

```bash
python -m unittest tests.test_detector_operator_handoff_audit -v
python -m models.run_t98
```
