# T91: Weak-Measurement Platform Audit

## Route

Quantum measurement / classical records.

## Question

Do the concrete weak-measurement platforms already named as likely T12 targets
actually provide an independent D1 branch-support or reversal-cost observable?

## Motivation

T90 says the weak-measurement route is non-null only if a pre-registered D1
axis changes the TaF verdict while the standard monitored record stays fixed.
T91 instantiates that gate on named experimental families rather than leaving
them as placeholders.

## Platform Family Under Audit

1. superconducting-qubit homodyne trajectories;
2. superconducting partial-measurement uncollapse protocols;
3. three-level superconducting quantum-jump warning and reversal protocols.

## Success Criteria

- At least one named platform supplies a pre-registered candidate axis that is
  not reconstructible from the same standard monitoring record.
- The candidate axis does not rely on success-conditioned postselection.
- The axis could change a TaF verdict while the standard monitored statistics
  are held fixed.

## Failure Criteria

- The candidate axis is only a refined function of the homodyne/no-click
  record already used by standard trajectory theory.
- The candidate axis depends on postselected reversal success.
- No named platform survives the T90 independent-axis gate.

## Claim Impact

Q1 remains `partially_supported`, but T12 is narrowed again if all three
platforms fail. In that case, the repo should stop treating standard
superconducting weak-measurement platforms as near-ready discriminators.

## Reproduction

```bash
python -m unittest tests.test_weak_measurement_platform_audit -v
python -m models.run_t91
```
