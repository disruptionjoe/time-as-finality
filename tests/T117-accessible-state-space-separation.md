# T117: Accessible State Space Separation Audit

## Route

Mathematical machinery / prior-art absorption audit.

## Question

Can two finite systems match on entropy, information, finality, viability,
persistence, and coarse reachability while differing in Accessible State Space
(ASP)?

## Candidate Definition

For this audit:

```text
ASP(observer, horizon) = admissible future task set
```

A task is accessible only when its required witnesses, rights, maintenance
budget, reconstruction paths, and certification tokens are present.

## Required Domains

- Version control.
- Provenance.
- Governance.
- Commons.
- Consensus.
- Record systems.

## Success Criteria

- Each domain supplies a finite pair matched on entropy, information,
  finality, viability, persistence, and coarse reachability.
- Each pair splits on computed ASP.
- The lost-structure chain is explicitly checked:

```text
lost structure
-> reconstruction debt
-> maintenance burden / admissibility loss
-> reduced future options
-> ASP reduction
```

## Failure Criteria

- ASP is assigned by intuition rather than task requirements.
- The task universe is changed between paired systems.
- The audit ignores reachability, opportunity sets, controllability, active
  inference, free energy, resilience, commons governance, niche construction,
  or mechanism design.
- The result promotes ASP as independent physics.

## Claim Impact

No core claim is upgraded. T117 preserves ASP only as a set-valued
observer/task-indexed audit object. It separates from coarse metrics, but is
mostly absorbed by enriched reachable-state, opportunity-set, provenance,
commons, and mechanism-design formalisms.

## Reproduction

```bash
python -m unittest tests.test_accessible_state_space_separation -v
python -m models.run_t117
```
