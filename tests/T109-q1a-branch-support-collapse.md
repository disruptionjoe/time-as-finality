# T109: Q1A Branch-Support Collapse

## Route

Quantum measurement / classical records.

## Question

Does branch support provide a real escape from the T105 accessible-class
reduction inside the current fixed-data Q1A witness family?

## Motivation

After T105, the strongest remaining excuse for keeping Q1A open as more than
audited bookkeeping is that another D1 dimension might still be load-bearing.
Branch support is the obvious candidate because the formalism names it
explicitly, but the current finite Q1A witnesses may not actually encode it as
an independent degree of freedom.

The highest-value move is therefore to test that directly and kill the escape
hatch if it is not real.

## Success Criteria

- Audit branch support across the current T105 visible fixed-data family.
- Check whether any admissible visible case has nontrivial branch support.
- Check whether branch support ever splits cases with the same audited
  accessible provenance support.
- Reuse the T103 branch-history control to test whether changing ordinary
  branch/history availability already leaves the fixed-data gate.
- State clearly whether branch support is a live Q1A rescue route or not.

## Failure Criteria

- It quietly changes the fixed quantum-side summaries while claiming a
  branch-support distinction.
- It treats a relabeled ordinary branch-history change as an admissible Q1A
  witness.
- It overclaims a new measurement result instead of a negative structural
  audit.

## Claim Impact

If branch support is either trivial on the admissible family or equivalent to
changing ordinary branch/history data, then Q1A loses another possible path to
paper-facing distinctness. Future branch-support work would then require a new
witness language with genuinely distinct causal record channels.

## Reproduction

```bash
python -m unittest tests.test_q1a_branch_support_collapse -v
python -m models.run_t109
```
