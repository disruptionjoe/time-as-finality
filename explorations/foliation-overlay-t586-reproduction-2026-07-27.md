# Foliation Overlay Against the T586 Record Order: In-Repo Reproduction

**Status:** reproduction-and-corroboration — in-repo re-derivation of the
2026-07-27 out-of-repo swing-2 computation; corroborates the T587 downgrade
context; no new claim, no new T-number
**Graded:** 2026-07-28 — **GRADED-CONFIRMED at fixture tier**, with the
independence-scope caveat binding (see the 2026-07-28 correction below for
exactly what the 17/17 certifies); findings' citation classes settled by the
fixture-family sweep (finding 1 → typing-theorem, finding 3 →
regime-dependent). Closes the "grading remains a separate, unblocked step"
flag. Grading note, rider section:
[goal2-charter-verdict-grading-2026-07-28.md](goal2-charter-verdict-grading-2026-07-28.md)
**Date:** 2026-07-27
**Reproduces:** the swing-2 result reported in the private system-runtime
mailbox note
`mailboxes/time-as-finality/20260727-swing2-result-foliation-against-t586-order.md`,
which was computed in a scratch directory outside this repository and
explicitly requested in-repo reproduction before grading
**Builds on:** [T586](../tests/T586-record-capability-order-gate.md)
([model](../models/t586_record_capability_order_gate.py)) and
[T587](../tests/T587-t586-causal-collapse-boundary-attack.md)
([model](../models/t587_t586_causal_collapse_boundary_attack.py), verdict
`T586_DOWNGRADED_TO_TYPED_RECORD_PREREQUISITE_FILTER_REVIEW_ONLY`)
**Model:**
[../models/foliation_overlay_t586_reproduction.py](../models/foliation_overlay_t586_reproduction.py)
(pure stdlib, deterministic, byte-identical across repeat runs; prints a JSON
expected/actual/match table; exit 0 — all 17 checks match the mailbox note's
reported values)

---

## Why this is an exploration and not a test

Two constraints meet here and are reconciled deliberately:

1. The mailbox note asks for its numbers to be reproduced inside TaF, under
   the repository's own conventions, before anything is graded or enters a
   ledger.
2. T587's closing stop controls what those conventions currently permit:
   *"Do not continue producing T-number scaffolds from T586 alone. Reopen
   Lane 1 only for a provenance-valid physical source packet, a frozen
   capability witness, or a sharper counterexample that changes the
   record-issuance contract."*

A foliation is formally an injective global time assignment, so it induces a
total order — which puts a foliation overlay squarely in the comparator class
T587 already adjudicated: T587 found the T586 record order **absorbed** by its
strongest-dependency and causal comparators and returned a downgrade to a
typed record-prerequisite filter. Running a fresh total-order comparator
against T586 therefore cannot open a new T-number and does not constitute a
new claim. It lands as this: a reproduction of the out-of-repo numbers, filed
as corroborating context for the T587 downgrade. The mailbox note frames
itself the same way.

## Method

Everything was re-derived from scratch against the T586 module's own
machinery — the `_landauer_record_events` fixture (reused unchanged, not
copied) and the `build_order_report`, `causal_relation`, `transitive_closure`,
and `clock_label_relation` helpers. The original out-of-repo scratch script
was deliberately not consulted or imported, preserving the mailbox note's own
hygiene rule that an unblessed artifact should not enter the repository by the
back door; agreement between two independently written derivations is part of
the reproduction's value.

Run from the repository root:

```sh
python3 -m models.foliation_overlay_t586_reproduction
```

## Reproduced result — every value matches the mailbox note

| Quantity | Note value | Reproduced | Match |
|---|---|---|---|
| Baseline record order is a strict partial order | yes | yes | yes |
| Ordered pairs in record closure | 6 | 6 | yes |
| Incomparable unordered pairs | 4, all involving `prepare_biased_reference` | 4, all involving `prepare_biased_reference` | yes |
| Ordered pairs in causal closure | 8 | 8 | yes |
| Record closure strictly contained in causal closure | true | true | yes |
| Candidate foliations (all orderings of 5 events) | 120 | 120 | yes |
| Foliations respecting record order | 5 | 5 | yes |
| Foliations respecting causal order | 3 | 3 | yes |
| Record-admissible but causally inadmissible | 2 | 2 | yes |
| Comparabilities an admissible foliation adds | 4 | 4 | yes |
| ...of which have no record basis | 4 (all) | 4 (all) | yes |
| Record order recomputed with a foliation label present | identical to baseline | identical to baseline | yes |

No discrepancy was found. Had any number differed, that discrepancy — not a
smoothed agreement — would be the headline of this note.

## The four findings, with reproduced numbers

**1. The foliation changes nothing.** Assigning every event its foliation
position as the clock label and recomputing the record-capability order
returns a closure identical to baseline, still a strict partial order. This
re-exercises T586's own clock-label control, and slightly strengthens its
exhibit: T586 permuted presentation labels, while here a genuine global tick
(the foliation's positions) is present and still contributes nothing. The
foliation's induced clock-label total order (10 pairs) differs from the record
order (6 pairs), exactly as T586's control requires.

**2. Everything the foliation adds is unlicensed.** The chosen
record-admissible foliation adds exactly 4 comparabilities beyond the record
order, and they are exactly the 4 pairs the record order leaves incomparable —
all involving `prepare_biased_reference`, all with no record basis in either
direction. The foliation contributes order precisely where the record
structure says there is none.

**3. Records under-constrain the foliation.** Of 120 candidate foliations, 5
respect the record order but only 3 respect the causal order, so 2 orderings
are record-admissible yet causally inadmissible. The reproduction exhibits
them concretely: they place `prepare_biased_reference` before
`seed_known_record` (violating the causal edge seed -> prepare) or after
`certify_erased_record` (violating prepare -> certify). Notably, the
deterministic first record-admissible foliation the script selects is itself
one of these two — the record order, followed on its own, walks straight into
a causally inadmissible global ordering. Causal structure does strictly more
constraining work than record structure in this fixture.

**4. A three-fold degeneracy survives everything.** After imposing both the
record and the causal constraint, 3 foliations remain (they differ only in
where `prepare_biased_reference` sits between `seed_known_record` and
`certify_erased_record`), and nothing in the fixture selects among them. The
inaccessibility of a preferred global tick is derived by the fixture, not
posited.

## Framing

This corroborates T587's downgrade — the record order is under-constraining
relative to causal structure, and a foliation adds only unlicensed
comparabilities; the three-fold residual degeneracy means the fixture derives
the foliation's inaccessibility rather than positing it.

## Scope

Five-event toy; counts are fixture-specific; only the structure may
generalize. That any admissible time function must respect causal order is
standard and is not claimed as new; what the fixture supplies is a concrete
measure of how much less the capability-derived order constrains a foliation
than causal structure does.

## Adverse note, recorded rather than smoothed

Finding 3 cuts against a strong reading of "record/order facts are capability
facts": record structure alone does not determine temporal order even in this
fixture, and two record-admissible orderings are causally inadmissible. This
is recorded as adverse, not smoothed. The mailbox note suggests routing this
finding into the H3/R1 seam work rather than treating it as a Lane 1 result;
that routing disposition stays with the note's process and is not made here.

## What This Does Not Claim

- **No new claim.** No claim-ledger or Canon Index movement is earned or
  proposed; nothing here changes claim status in any direction.
- **No new T-number.** T587's stop stands; this is corroborating context for
  T587, not a new gate, scaffold, or attack endpoint.
- **No revival of T586's downgraded order claim.** The downgrade to a typed
  record-prerequisite filter stands; if anything, the reproduced numbers
  reinforce it.
- **No preferred-frame conclusion.** Nothing here is evidence for or against a
  preferred foliation in physics. Within the fixture, admissible global ticks
  exist, are threefold underdetermined, and add only unlicensed
  comparabilities; no conclusion about actual spacetime, a substrate tick, or
  Lorentz structure is drawn.
- **No grading.** This note reproduces; it does not grade, narrow, defer, or
  reject the swing-2 result.

## Closes

This reproduction closes the mailbox note's "reproduce before grading" flag:
the swing-2 numbers now exist inside TaF, recomputed under its own
conventions from its own fixture and helpers, with all 17 checks matching.
Grading, narrowing, deferral, or rejection of the swing-2 result is now
unblocked and remains a separate step.

## Independence scope correction (2026-07-28)

The original text above is left in place per house correction style; this
section states what its independence language actually covers, verified
against the model file by an adversarial pass.

The Status line's "in-repo re-derivation" and the Method section's
"re-derived from scratch" / "agreement between two independently written
derivations" overstate the independence scope if read broadly. Precisely:

- `models/foliation_overlay_t586_reproduction.py` imports the T586 module's
  fixture (`_landauer_record_events`) and its four helpers
  (`build_order_report`, `causal_relation`, `transitive_closure`,
  `clock_label_relation`) **wholesale** — the Method section says so
  ("reused unchanged, not copied"), but the headline framing can be read as
  claiming a fully independent pipeline.
- The independently written content is the **enumeration overlay only** —
  roughly thirty lines: the linear-extension check, the 120-permutation
  sweep, the added-comparability accounting, and the foliation-label
  re-labeling harness.
- Every expected value in the 17-check table is **carried from the mailbox
  note**, not derived blind: the script certifies agreement with reported
  values, it does not rediscover them.

What the reproduction therefore certifies is exactly: (a) determinism and
stability of the shared T586 machinery under a foliation overlay, and
(b) agreement of an independently written enumeration layer with the
out-of-repo note's reported values. Independence from the original
out-of-repo scratch script is real — it was not consulted or imported.
Independence from T586's own fixture and helpers was never achieved, and
was not the design goal; a shared-machinery error common to T586 and this
script would pass all 17 checks undetected.

The actual robustness instrument for that residual risk is the
fixture-family sweep executed this wave
([fixture-family-sweep-2026-07-28.md](fixture-family-sweep-2026-07-28.md)),
which varies the fixture rather than re-running it. Nothing in this
correction changes the reproduced numbers, the closure of the "reproduce
before grading" flag, or any claim status.
