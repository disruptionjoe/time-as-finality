# P40 - Legal Scholar

## Goal

Use legal finality to formalize authority, appeal, jurisdiction, and reversal
as a hostile analogy for observer-relative validity.

## Status

Done. This was a bounded exploratory run only. It does not update claims,
ROADMAP, TESTS, or CLAIM-LEDGER.

## Repo Context Read

- `Vision - North Star.md`
- `Method - Research Program Guidelines.md`
- `Lead Research Line - Time as Finality.md`
- `explorations/persona-future-run-goals-2026-06-20.md`
- `explorations/persona-goal-runs/2026-06-21-210616-p36-access-control-finality-audit.md`
- `technical-reports/TECHNICAL-REPORT-accessible-state-space-separation-v0.1.md`
- `technical-reports/TECHNICAL-REPORT-detector-authority-domain-bound-v0.1.md`
- `technical-reports/TECHNICAL-REPORT-detector-challenge-window-freeze-screen-v0.1.md`
- `technical-reports/TECHNICAL-REPORT-definalization-reverse-edge-taxonomy-v0.1.md`
- `results/accessible-state-space-separation-v0.1-results.md`

## Work Performed

1. Selected the first queued persona entry, `P40 - Legal Scholar`.
2. Treated legal finality narrowly as a hostile boundary case about:
   - who may certify a record;
   - where that certification applies;
   - who may challenge or appeal it;
   - what kind of reversal is being discussed.
3. Compared that lens against existing repo objects for authority partition,
   challenge-window freeze, admissible future operations, and
   authority/provenance loss.
4. Pressured the legal framing against mature absorbers already visible in the
   repo: governance, provenance, access control, reachable future operations,
   and mechanism-design style rights.

## Finite Witnesses Reviewed

### 1. Governance / appeal witness

`T117` already supplies the cleanest legal-style split:

- same archive;
- same coarse finality and reachability metrics;
- different future rights:
  `{read_archive}` versus `{appeal, challenge, read_archive, repair_rule}`.

This is exactly the kind of separation a legal scholar cares about. The record
can be present in both worlds, while validity-changing operations differ.

### 2. Authority / jurisdiction witness

`T100` shows that admissibility depends on a nontrivial authority partition.
Under the current detector packet, fewer than four authority domains collapse
into self-certification.

Legal translation:

```text
same file or verdict text
!= same authoritative standing
```

Validity depends on which body is allowed to certify within the declared
jurisdiction, not on record presence alone.

### 3. Appeal-window witness

`T176` sharpens the rights question further. A published authority map is
insufficient if guardian identity or release/revocation/audit rules can be
rewritten during the challenge window.

Legal translation:

```text
a judgment is not stably final if the appellate or review forum can be
rewritten while the appeal is still open
```

### 4. Reversal-type witness

`T144` is the key quarantine result. It separates:

- boundary access loss;
- support-copy removal;
- physical record deletion;
- authority or provenance loss.

For the legal lens, this matters because reversal of legal validity is usually
an `authority_or_provenance_loss` event, not a claim that the underlying
physical event was erased from the world.

## Result

The legal lens is useful, but only in a bounded way.

The strongest honest formulation supported by the repo is:

```text
legal finality = authority-relative admissibility of a record under declared
jurisdiction, appeal rights, and reversal rules
```

That is not the same thing as:

- truth;
- physical irreversibility;
- global observer-independent finality.

The lens is therefore good for clarifying observer-relative validity, but bad
if promoted into physics metaphor.

## Translation Table

| Legal notion | Closest repo object | Bounded verdict |
| --- | --- | --- |
| jurisdiction | observer/task/horizon/access boundary plus authority scope | useful and already structurally present |
| authority to enter judgment | authority partition, certification token, provenance state | already load-bearing in detector/admissibility work |
| appeal window | challenge rights, freeze policy, review-period controls | already present and critical in T117/T176 |
| reversal / vacatur | future operation right to challenge, revoke, repair, or downgrade | useful as governance state, not physics |
| precedent / constraint propagation | rule-bearing record that constrains later admissible moves | suggestive, but not needed as a new primitive here |

## Main Decision

`P40` should currently be treated as a disciplined translation lens, not as a
new TaF object.

What survives is narrow:

```text
record finality can be relative to a certifying authority and a review
jurisdiction, while leaving the underlying event and wider world unchanged
```

This helps the repo state more carefully that some verdicts are:

- observer-relative;
- authority-bound;
- challenge-window dependent; and
- reversible by governance/provenance action rather than by physical undo.

But once those features are typed honestly, the mathematics is mostly absorbed
by governance/provenance/admissibility and future-operation state.

## Proposed Next Action

If this lane is continued later, the next honest move is one finite legal-style
fixture, not a broader essay:

1. hold a record and its coarse content fixed;
2. vary jurisdiction, appeal rights, or certifying authority only; and
3. show which admissible future operations change:
   `certify`, `appeal`, `vacate`, `repair`, `publish`, or `treat as settled`.

That would fit naturally with later authority-boundary and challenge-event
goals such as `P84`, `P86`, or `P87`.

## Claim-Status Posture

- No claim-status changes recommended.
- No ROADMAP or TESTS changes recommended.
- No CLAIM-LEDGER update recommended.
- Best current posture: legal finality is a hostile analogy for
  authority-bound record validity and appeal/reversal discipline, while the
  underlying formal content is absorbed by existing admissibility and
  governance machinery.
