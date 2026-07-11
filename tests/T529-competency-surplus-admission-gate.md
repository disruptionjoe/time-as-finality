# T529: Competency Surplus Admission Gate

## Target Claims

- `C(R)` capability object.
- T493 Levin competency C(R) absorber gate.
- T494 Levin/Fields primary-source competency absorber gate.
- `open-problems/region-indexed-capability-discriminator.md`.

## Setup

T493 shows that current C(R) content is absorbed when competency is granted as
the full intervention-measured task-success profile over a declared region,
menu, and task family. T494 upgrades the bounded source status for that
competency absorber warning.

T529 turns the next burden into an executable admission gate for future
region-indexed capability packets. It evaluates packet shapes against these
requirements:

1. freeze the region, menu, and task context before pair selection;
2. check T493/T494 absorber pressure;
3. use primary-source-checked competency status only inside the bounded
   calibration/absorber scope;
4. distinguish simple observed-statistics surplus from surplus over a full
   competency profile;
5. require a matched full competency profile plus an independent noncompletion
   witness for any future surplus review target;
6. block mechanism imports, claim/canon/public-posture movement, external
   publication, and cross-repo truth shortcuts.

## Success Criteria

- Current T407-style simple-statistics surplus is preserved only as review
  material, not competency surplus.
- Full-profile-equivalent packets are absorbed by competency bookkeeping.
- Weak single-statistic proxy packets are rejected or absorbed.
- A synthetic future packet shape is admitted only as a review target when it
  matches the full competency profile and supplies an independent
  noncompletion witness for a non-task-success capability.
- Source-status, external-mechanism, claim/canon/public-posture, and cross-repo
  shortcuts are blocked.

## Failure Criteria

- The gate treats flat simple statistics as surplus over full competency.
- The gate treats another task-success coordinate as escaping a full competency
  profile.
- The gate imports active-inference, free-energy, TAME, or polycomputing
  mechanisms into TaF C(R).
- The gate updates claim status, Canon Index tiers, canon verdicts, public
  posture, external-publication state, or cross-repo truth.

## Known Physics Constraints

No physics claim is made. This is a finite admission gate over internal TaF
capability-profile artifacts and the bounded Levin/Fields competency absorber
scope.

## Reproduction

```bash
python -m models.competency_surplus_admission_gate --write-results
python -m unittest tests.test_competency_surplus_admission_gate -v
```
