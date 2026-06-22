# P35 Run - Database Systems Architect

- timestamp: 2026-06-21T20:05:43-05:00
- goal_id: P35
- selected_persona: Database Systems Architect
- selected_goal: Translate a core typed-forgetting example into relational algebra, projection, joins, provenance semirings, and why-not provenance.
- bounded_question: Does one core typed-forgetting witness still look nonstandard after translation into relational algebra and provenance machinery, or does the database reading absorb it?
- posture: bounded exploratory run only; no claim-status update, roadmap change, or ledger edit.

## Repo Context Read

- `explorations/persona-future-run-goals-2026-06-20.md`
- `Vision - North Star.md`
- `Method - Research Program Guidelines.md`
- `Lead Research Line - Time as Finality.md`
- `claims/TF1-typed-forgetting-attribution.md`
- `tests/T99-losskernel-quotient-separation.md`
- `models/losskernel_quotient_separation.py`
- `tests/T108-loss-relocation-prior-art.md`
- `models/loss_relocation_prior_art.py`
- `tests/T127-same-neighbor-data-losskernel-audit.md`
- `explorations/persona-goal-runs/2026-06-20-194724-p11-programming-languages-typed-effects.md`
- `explorations/persona-goal-runs/2026-06-21-110150-p26-philosophy-of-mathematics-losskernel-classification.md`
- `explorations/research-constellation-orchestrator-2026-06-20.md`

## Work Performed

1. Chose `T99` as the core typed-forgetting example because it already fixes
   the hostile quotient conditions:

```text
same source
same target
same ordinary composite map
same endpoint behavior
same naive lost-label set
```

2. Read `T108` and `T127` first so the translation would be an absorber pass,
   not a novelty exercise.
3. Recast the `T99` collision pair as a small relational schema plus three
   query layers:
   - visible projection;
   - witness-bearing join;
   - attribution query.
4. Checked whether the typed distinction survives once ordinary database
   provenance and why-not explanations are allowed the same witness relation.

## Database Translation Of T99

### Source schema

Use the `T99` branch fixture as two source tables.

```text
BranchMap(branch_id, visible_branch)
Witness(branch_id, label, witness_id, witness_type,
        source_anchor, resolves_obstruction, obstruction_id)
```

Fix the visible branch map in both cases as:

```text
BranchMap =
  { (left_source_branch,  lumped_branch),
    (right_source_branch, lumped_branch) }
```

This is the `T99` ordinary composite map:

```text
left_source_branch  -> lumped_branch
right_source_branch -> lumped_branch
```

Now translate the two `T99` collision cases.

### Case A: relevant witness

```text
Witness_A =
  { (left_source_branch,  branch_selector,
     signed_preimage_selector,
     source_global_section_resolver,
     source_certificate:branch-preimage-resolves-ambiguity,
     true,
     target_branch_ambiguity) }
```

### Case B: decorative label

```text
Witness_B =
  { (left_source_branch,  branch_selector,
     display_color_tag,
     decorative_metadata,
     source_annotation:display-only-color,
     false,
     none) }
```

The two cases share the same coarse visible data and the same naive lost label:

```text
branch_selector
```

They differ only in witness-bearing source attributes.

## Relational-Algebra Reading

### 1. Visible projection

```text
Q_visible := pi_visible_branch(BranchMap)
```

Both cases return exactly:

```text
{ lumped_branch }
```

So the coarse visible view is identical.

### 2. Label-only join

```text
Q_label := pi_visible_branch, label(BranchMap join Witness on branch_id)
```

Both cases return:

```text
{ (lumped_branch, branch_selector) }
```

This is the database version of the `T99` negative result:

```text
label-only LossKernel collapses
```

### 3. Witness-bearing attribution query

```text
Q_attr :=
  pi_visible_branch, witness_id, witness_type, source_anchor
  (sigma_resolves_obstruction = true
   and obstruction_id = target_branch_ambiguity
   (BranchMap join Witness on branch_id))
```

Now the cases diverge:

- Case A returns one witness-bearing tuple.
- Case B returns the empty relation.

This is exactly the `T99` verdict split:

```text
Case A -> admissible_typed_attribution
Case B -> inadmissible_label_only_metadata
```

## Provenance-Semiring Reading

For the visible query `Q_visible`, ordinary tuple provenance already says the
same thing in both cases. Using indeterminates `x_L, x_R` for the two source
tuples:

```text
Prov(Q_visible(lumped_branch)) = x_L + x_R
```

So semiring provenance on the visible projection does **not** separate the
cases. That matches the repo's warning that endpoint behavior plus naive labels
are too weak.

For the witness-bearing attribution query, provenance also behaves ordinarily.
If the witness tuple is admitted into the source schema, then:

- Case A has a derivation using the witness tuple.
- Case B has no derivation satisfying `resolves_obstruction = true`.

So the distinction is not beyond provenance machinery. It is just a different
query over a richer source schema.

## Why-Not Provenance Reading

The natural database question is:

```text
Why is there no admissible attribution answer for lumped_branch?
```

In Case B, a standard why-not explanation is:

```text
because no witness tuple satisfies
resolves_obstruction = true
and obstruction_id = target_branch_ambiguity
```

In Case A, the why-not question disappears because such a tuple exists.

This means the current typed-forgetting distinction is already legible as:

- ordinary projection loss on `Q_visible`;
- provenance over a witness-bearing join; and
- why-not provenance for the missing admissible explanation row.

## View / Complement Reading

There is also a standard view-update reading.

`Q_visible` is a non-invertible projection of `BranchMap join Witness`. The
forgotten witness relation acts like complement data needed to recover whether
the visible branch has a source-side resolution certificate.

So the database reading lands close to the same absorber family that `T108`
already identified:

- provenance / why-not provenance;
- complement-style view information;
- richer explanation schema rather than a new obstruction object.

## Result

### Main Verdict

The database translation is negative for novelty and positive for clarity.

The `T99` witness does survive translation into relational algebra, but it does
so as ordinary database machinery:

```text
projection + hidden join attributes + provenance / why-not explanation
```

not as a prior-art-separated object.

### Strongest Honest Formulation

```text
The current typed-forgetting examples can be translated into ordinary database
terms: visible projection collapses the cases, label-only provenance also
collapses them, and a witness-bearing join or why-not explanation restores the
attribution split. That supports the repo's current downgrade of LossKernel to
integration vocabulary or witness-account notation, not a distinct database-
separated theorem.
```

## Small Residual Window

The only database-facing residual target I can justify is narrower:

```text
Can witness-bearing loss data be derived canonically from the morphism as a
minimal explanation schema, rather than attached by hand as extra source
columns?
```

That would still need a same-neighbor-data pass:

```text
same relational source package
same view
same provenance semiring behavior
same why-not explanation package
but different LossKernel verdict
```

Nothing in the current fixture family earns that.

## Blocker

There is no database separation witness yet.

Once the witness relation is made explicit, the `T99` distinction becomes an
ordinary query-answer dependence on richer explanation data. That is exactly
what provenance, why-not provenance, and view-complement machinery are built
to track.

## Proposed Next Action

If this branch is continued later, the next honest bounded step is:

1. build one explicit same-neighbor-data database fixture;
2. hold fixed the relational schema, visible view, provenance semiring output,
   and why-not explanation object; then
3. test whether any `LossKernel` verdict still differs.

If that fails again, the database reading should be treated as a completed
absorber and cited as a reason to keep `LossKernel` at notation-level posture.

## Claim-Status Posture

- No claim-status changes recommended.
- No roadmap, `TESTS.md`, or `CLAIM-LEDGER.md` changes recommended.
- Positive narrow result: `T99` translates cleanly into relational algebra and
  database explanation language.
- Negative narrow result: the translation strengthens the absorber case against
  `LossKernel` novelty rather than rescuing it.
