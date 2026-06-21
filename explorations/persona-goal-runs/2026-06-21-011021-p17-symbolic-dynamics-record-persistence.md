# P17 - Symbolic Dynamics Expert Run

- persona: Symbolic Dynamics Expert
- goal_id: P17
- run_timestamp: 2026-06-21T01:10:21-05:00
- queue_source: `explorations/persona-future-run-goals-2026-06-20.md`
- goal: Search for symbolic invariants of record persistence using subshifts,
  forbidden words, entropy rates, and ordinal-pattern limits.
- posture: bounded exploratory run only; no claim-status update, roadmap
  change, or ledger edit.

## Repo Context Read

- `Vision - North Star.md`
- `Method - Research Program Guidelines.md`
- `Lead Research Line - Time as Finality.md`
- `explorations/persona-future-run-goals-2026-06-20.md`
- `explorations/TS-PERSONA-SPRINT-001-rafael-cortez-v0.1.md`
- `models/ts_persona_sprint.py`
- `models/local_persistence_reconciliation.py`
- `tests/test_local_persistence_reconciliation.py`
- `tests/test_local_persistence_mechanisms.py`
- `results/ts-persona-sprint-001-v0.1-results.md`

## Bounded Run

Question: do the current finite persistence traces support any symbolic-dynamics
signature stronger than the already known schedule readout?

Method:

1. Reuse the existing `TS-PERSONA-SPRINT-001` trajectories as the source
   symbolic traces.
2. Treat each level's satisfiable/obstructed trajectory as a binary word over
   `{1,0}`.
3. Compute finite block languages and forbidden words for word lengths 2-5.
4. Compare raw symbolic languages across `micro` and `holonic` for
   `canonical`, `early_stress`, `late_stress`, `large_gap`, and `zero_gap`.
5. Check whether the earlier ordinal-pattern null result was a one-metric
   accident or part of a broader symbolic collapse.

## Work Performed

I ran a finite symbolic audit over the existing trajectory generator in
`models/ts_persona_sprint.py`.

For every tested trajectory and for both `micro` and `holonic`:

- the length-2 language is identical: `{00, 01, 10, 11}`;
- the length-3 language is identical: `{000, 001, 011, 100, 110, 111}`;
- the length-3 forbidden words are identical: `{010, 101}`;
- the length-4 and length-5 languages are also identical across all tested
  levels and variants.

Observed subword complexity:

| word length `n` | distinct words `p(n)` |
| --- | --- |
| 2 | 4 |
| 3 | 6 |
| 4 | 8 |
| 5 | 10 |

This linear growth is the finite signature of a one-obstruction-block family,
so the corresponding symbolic entropy rate is zero rather than a new
persistence-bearing invariant.

The earlier ordinal-pattern null result was therefore not an accident of using
order-2 patterns. It sits inside a broader collapse:

- raw ordinal-pattern counts tie;
- raw irreversibility scores tie at zero;
- raw finite subshift languages also tie.

## Result

### Main Finding

No new symbolic invariant is earned from the current binary persistence traces.

The current traces all realize the same one-block symbolic language: a long run
of `1`, one contiguous run of `0`, then a long run of `1` again. Symbolically,
the useful finite fact is only:

```text
single obstruction interval
=> forbidden alternating return words 010 and 101
=> zero symbolic-entropy-rate family
```

That fact does not separate:

- `micro` from `holonic`;
- `canonical` from `early_stress` or `late_stress`;
- `large_gap` from `zero_gap`.

It only says the traces belong to the same coarse symbolic family.

### Smallest Discriminative Object

The smallest object that does separate the cases is not a shift-invariant
language but a position-sensitive block-length summary:

```text
(leading 1-run, 0-run, trailing 1-run)
```

Examples:

| trajectory | micro | holonic |
| --- | --- | --- |
| canonical | `(10, 15, 25)` | `(10, 25, 15)` |
| large_gap | `(10, 15, 25)` | `(10, 30, 10)` |
| zero_gap | `(10, 15, 25)` | `(10, 20, 20)` |

This summary does recover the persistence-gap information, but only because it
is a direct read-off of the hardcoded obstruction schedule. It is therefore a
derived observable, not a new symbolic-dynamics invariant.

## Interpretation

This run weakens the hope that current record-persistence traces already carry a
dynamics-native symbolic signature.

The negative result is still useful:

- it blocks over-reading ordinal-pattern language;
- it shows that raw subshift/forbidden-word language is currently too coarse;
- it localizes the issue to the fixture design rather than the analysis metric.

The present traces contain only one obstruction episode per level. With only one
episode, symbolic dynamics sees one forbidden alternating pattern family and
little else.

## Proposed Next Action

Only revisit the symbolic-dynamics lane after a fixture generates unscheduled
multi-episode obstruction/recovery behavior.

Best next gate:

1. run the already-identified `MINI-GOAL-TS-002` style test where the holonic
   persistence window is not hardcoded; and
2. only keep the symbolic lane open if non-empty `forgotten_dims` alone can
   generate multiple obstruction/recovery episodes or a persistence gap.

That would give symbolic methods something capable of producing genuinely
different block languages, entropy growth, or ordinal-pattern asymmetry.

## Claim-Status Posture

- No claim-status changes proposed.
- No roadmap or ledger changes proposed.
- Status of this run: exploratory negative result.
- Best current classification: the symbolic summaries available on the present
  traces are derived observables of the schedule, not independent invariants of
  record persistence.
