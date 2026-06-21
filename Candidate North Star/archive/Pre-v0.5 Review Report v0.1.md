# Pre-v0.5 Review Report v0.1

## Status

Fresh-eyes review of `Candidate North Star v0.4.md` against the v0.5 queue.

Reviewer: Claude Sonnet 4.6 (June 20, 2026)

Inputs:

- `Candidate North Star v0.4.md`
- `Candidate North Star Next Version Update Queue v0.5.md`
- `Fresh-Eyes Review Candidate North Star v0.4.md`
- `Candidate North Star Low-Hanging Dispatch Synthesis v0.1.md`

This is not canon. It does not draft v0.5. It gives verdicts on each queue
item and adds two new items.

---

## Verdicts On Queue Items Q1–Q12

### Q1. Quotient formalism — RESOLVED

v0.4 is internally consistent on this. The sufficiency definition correctly
uses `Cbar : X / ~=_X -> K` and `[pi(y)]_{~=_X}`. The fiber-constancy lemma,
minimal quotient, and capability spread all use `~=_X` and `~=_K` consistently.
The note that `~=_K` must be an equivalence relation (or the audit must name the
induced equivalence) is present in the Formal Core. No patch needed.

### Q2. Compact positive example — DECISION NEEDED

v0.4 has no worked example. The compression is successful and the audit
template is clear without one. However, Q2 is correct that the absence of a
single demoted-after-absorption mini-example makes it possible for a reader to
finish v0.4 and still not know what the audit looks like in motion.

Recommendation: add one example, explicitly walked through the checklist, with
honest demotion at the end. It should be in an appendix, not the main note.
If no natural example passes the canonicity bar, use a deliberately demoted one
to show the audit preventing overclaim. That is actually the stronger
pedagogical choice.

### Q3. Appendix map navigation — PATCH NEEDED

The current appendix map is a flat list of filenames with no description of
what each carries. Under the locked strategy of letting appendices do heavy
lifting, this is a real friction point. A reviewer cannot tell from the list
alone which report handles mathematics strengthening, which handles database
absorption, which handles prior-art humility, and which handles physics
steelmanning.

Smallest patch: replace the filename list with a two-column table:
companion report on the left, burden it carries on the right. This belongs in
the main note.

### Q4. Domain calibration framing — PATCH NEEDED (one sentence)

The domain calibration section has the correct compact pattern, but nowhere
does the main note say explicitly that domain sections are calibration gates
and not novelty evidence. A reader could read the database section and walk
away thinking strong domain absorption confirms the candidate rather than
pressure-tests it.

Smallest patch: one sentence at the top of the Domain Calibration section:

```text
Domain sections are calibration gates. Strong absorption in a domain is
expected and not a weakness; the question is whether any formal or canonical
residue survives after absorption.
```

### Q5. Physics witness mini-template — APPENDIX, NOT MAIN NOTE

The no-free-physics template is already present and correct. The decision of
whether to add a filled example follows the same logic as Q2: it belongs in a
companion report or appendix, not the main note. Confirm this placement
decision and close Q5 as a companion-report item.

### Q6. Database equality fields in checklist — APPENDIX

The database domain calibration in v0.4 lists native absorbers and K
candidates but does not carry the full database equality field checklist.
This belongs in the database companion report, not the main note. The reviewer
checklist in the main note already has `same-visible-state context fixed?` as
a gate. The detailed expansion (schema, constraints, query/view language,
isolation context, provenance, index/materialization, access policy,
consistency model, approximation tolerance, workload) should live in the
appendix. Close Q6 as confirmed appendix placement.

### Q7. Approximate equivalence — PARTIAL GAP

The Formal Core correctly notes that preorders, tolerances, metrics, and
probabilistic criteria require a named induced equivalence. The K type gate
includes `approximate retrieval envelope`. But the audit template and reviewer
checklist do not name approximate forms by type: epsilon, probabilistic, top-k,
recall@k, latency/recall envelope, workload equivalence.

For databases and ML retrieval systems this matters, because claiming exact
visible-state equality is already a known failure mode and the document should
make the approximate forms first-class alongside exact equality.

Smallest patch: one line added to the reviewer checklist:

```text
if approximate: epsilon/top-k/recall/workload equivalence declared?
```

This belongs in the main note.

### Q8. Failure label overlap — NO PATCH NEEDED

The eight failure labels in v0.4 are distinguishable in normal use.
`same_visible_state_underspecified` fires when visible equality is not fully
declared. `projection_underdescribed` fires when the projection omits native
domain state. These are orthogonal: a claim can fail one, both, or neither.
A distinction table is not needed unless future review sessions produce
real ambiguity. Close Q8 as no-patch.

### Q9. Canonical vs formal residue separation — ACCEPTABLE

The residue ladder is clear enough. Formal residue requires surviving immediate
absorption as a clean formal object but does not require canonicity.
Canonical requires surviving both absorption forms plus domain-natural Cap,
natural quotient, and unavoidable tradeoff. The distinction is present.

The word "immediate" in Formal Residue is the only potential confusion point:
a reader might think formal residue requires only one pass through absorption,
not two. Recommend changing "immediate" to "tested" or dropping it. One-word
patch, low priority.

### Q10. Default equality rule — PATCH NEEDED

v0.4 does not have a blunt sentence ruling out `same payload` or `same current
value` as default equality. The failure label `same_visible_state_underspecified`
handles this indirectly, but there is no positive statement that the default is
not enough.

Smallest patch: one sentence in the Formal Core, after the declaration of
`~=_X`:

```text
The default equality relation is not "same payload" or "same current value."
Equality must be declared by the audit context.
```

This belongs in the main note.

### Q11. Prior-art posture in opening — SOUND

The Executive Posture opens with "The bare idea... is old" and the second
sentence names mature fields. The Governing Sentence immediately follows with
the projection-sufficiency reframe. This is strong enough. Moving the
absorption warning earlier would require restructuring a section that already
leads with it. No patch needed.

### Q12. Falsifiability sentence — PATCH NEEDED

v0.4 has Failure Criteria (six bullets), which covers this at the program
level. But it does not have a per-witness falsifiability sentence. The
distinction matters: the program can succeed even if most witnesses are
demoted, but a reviewer needs a quick test for whether a specific witness fails.

Smallest patch: one sentence added to the Reviewer Checklist or the Residue
Ladder preamble:

```text
A proposed witness fails projection-sufficiency if a mature absorber supplies
a natural sufficient enrichment or quotient under the declared audit context.
```

This belongs in the main note.

---

## Two New Items

### N1. The "Candidate North Star" original document (root)

The root of the Candidate North Star folder contains `Candidate North Star.md`,
which appears to be a pre-v0.2 draft. Its relationship to the v0.4 line is not
stated in the folder readme. If it is superseded, mark it as archived.
If it carries something v0.4 dropped, name what. Ambiguity here creates
confusion for fresh reviewers who open the folder and see two top-level
north star files.

### N2. Physics sections in companion documents need posture alignment check

The `Candidate North Star 20 Physics Perspectives Report v0.1.md` predates the
strong physics posture in v0.4. Some personas in that report may still use
language compatible with deriving physics from Cap. Before v0.5 is drafted,
one pass through that report should confirm its physics-direction claims are
compatible with v0.4's no-free-physics rule. If they are not, add a header note
to that companion report flagging the mismatch. This is companion-report work,
not main-note work.

---

## Summary

Clear patches for the main note before v0.5:

| Item | Patch | Size |
|------|-------|------|
| Q3 | Appendix map: add two-column burden table | small |
| Q4 | Domain calibration: add calibration-gate framing sentence | one sentence |
| Q7 | Reviewer checklist: add approximate equivalence line | one line |
| Q10 | Formal Core: add default-equality-is-not-enough sentence | one sentence |
| Q12 | Residue Ladder or Checklist: add per-witness falsifiability sentence | one sentence |

Confirm as companion-report items (no main-note change):

| Item | Decision |
|------|----------|
| Q2 | Add one demoted example to appendix |
| Q5 | Add physics template filled example to appendix |
| Q6 | Database equality field checklist lives in companion report |

Close as no-patch:

| Item | Reason |
|------|--------|
| Q1 | Already resolved in v0.4 |
| Q8 | Labels distinguishable, no table needed |
| Q9 | Acceptable; optional one-word fix on "immediate" |
| Q11 | Opening posture already strong |

New items:

| Item | Action |
|------|--------|
| N1 | Clarify or archive `Candidate North Star.md` root file |
| N2 | Posture-alignment check on 20 Physics Perspectives companion |

---

## Net Assessment

v0.4 is structurally sound. The five main-note patches above are all small
and none require restructuring. The companion-report items are medium-effort
but do not block the main-note patch. v0.5 can be a tight patch release, not
a restructure.
