# Technical Report: Loss Relocation v0.1

## Claim Under Test

The motivating sentence is:

```text
Emergence may be the relocation of lost information into a stable new
constraint surface.
```

T107 weakens and formalizes that sentence. The testable version is:

```text
When a projection forgets source structure, the loss relocates only if a
target-side judgment remains dependent on source lifts, or if every source lift
stably forbids a target action.
```

This is not an information-conservation law. It is a finite accounting rule for
where the operational effect of forgotten structure appears.

## Artifact

T107 builds six finite projection scenarios:

| Scenario | Lost axis | Relocation |
| --- | --- | --- |
| `charge_neutrality_debt` | charge | admissibility condition |
| `spin_orientation_debt` | spin | orientation debt |
| `mass_persistence_debt` | mass | persistence debt |
| `phase_history_debt` | phase | path memory |
| `gauge_representative_absorbed` | gauge | absorbed freedom |
| `lorentz_access_constraint` | Lorentz/frame | stable access constraint |

For each target pair, the model computes all source-lift judgments. The
relocation class is derived as follows:

```text
mixed allowed/forbidden lifts -> reconstruction debt
all forbidden lifts           -> stable constraint surface
all allowed, hidden variation -> absorbed freedom
```

The witness obligation is source-anchored: it is the set of source-lift pairs
whose judgments disagree after projection.

## Result

The finite audit supports the weak relocation principle and rejects the strong
conservation slogan.

Lost charge, spin, mass, and phase produce reconstruction debt in the tested
fixtures because target-visible judgments vary across hidden source lifts.
Lost Lorentz/frame data produces a stable constraint surface in the tested
fixture because every source lift denies causal access. Lost gauge
representative data is absorbed because every source lift gives the same
invariant judgment.

## Current Strongest Claim

Loss relocation is source-fiber dependence:

```text
lost structure matters at the target exactly when target judgments are not
well-defined over the projection fiber, or when all lifts impose the same
stable constraint.
```

This gives `LossKernel` a better candidate semantics than label union:
source-fiber analysis can derive witness obligations instead of declaring them.

## What This Improved

T107 turns a powerful intuition into a finite audit:

- it preserves the "track where lost structure goes" idea;
- it avoids false conservation language;
- it gives a derivation path for T99-style witness obligations;
- it bridges the GU six-axis protocol into TaF as a specification discipline.

The GU protocol requires proposals to specify substrate, observer, pairing,
causal order, emergence class, and coordination loop. T107 says that when any
such axis is projected away, the first question is not "what label was lost?"
but:

```text
which target judgments become lift-dependent over the forgotten axis?
```

## What This Weakened Or Falsified

T107 weakens the strongest version of "conservation of lost information."
Some loss is absorbed. Gauge representative loss is the control: hidden
variation exists, but it creates no debt because the judged rule is invariant
over every lift.

This blocks overclaiming. The project should say "relocation of operational
effect under projection," not "conservation of lost information."

## Falsification Condition

Reject loss relocation as independent TF1 content if source-fiber analysis
does not survive comparison with ordinary why-not provenance, abstract
interpretation, lenses, CSP explanations, or effect annotations.

Reject the specific finite rule if a projected judgment has mixed source-lift
verdicts but no admissibility or reconstruction obligation is needed, or if a
uniform invariant fiber is forced to create debt.

## Claim Ledger Update

Add T107 to TF1:

```text
Loss relocation is modeled by source-fiber lift analysis. Mixed lift verdicts
produce reconstruction debt, uniform forbidden lifts produce a stable
constraint surface, and uniform invariant lifts show absorbed freedom. This
supports a source-anchored derivation path while rejecting conservation-style
language.
```

## Open Blocker

T107 supplies candidate semantics, not prior-art separation. The next blocker
is to compare the source-fiber rule against why-not provenance, abstract
interpretation, lenses, and CSP explanation machinery.

## Next Work

Re-express T99's typed witness obligations using source-fiber analysis and test
whether the quotient separation still survives. If it does, `LossKernel` has a
cleaner non-tautological core:

```text
typed loss = source-fiber witness needed to make a projected judgment
well-defined.
```

## Reproduction

```bash
python -m unittest tests.test_loss_relocation -v
python -m models.run_t107
```
