# papers/

Everything paper-related, organized by **publication stage**. A paper lives in
exactly one of the three subfolders at a time, so its location always tells the
truth about where it stands. Mirrors the `gu-formalization` paper lifecycle so the
two sibling repos share one publication discipline.

## The three-stage lifecycle

1. **[`drafts/`](drafts/)** — work in progress. All drafts, notes, deep-research
   prompts, review passes, and **previous/superseded versions**. Nothing here is a
   public claim; agents edit freely and version liberally (changelogs, vN files).
2. **[`candidates/`](candidates/)** — staged for publication. A paper graduates
   here **only when Joe has explicitly said he wants to publish it**; its earlier
   versions stay in `drafts/`. Near-final, not yet public. Each carries a
   `STAGING-NOTES.md` and has passed the light staging gate. See
   [`candidates/README.md`](candidates/README.md).
3. **[`published/`](published/)** — the public record. A paper moves up here
   **only after Joe confirms it has actually been published** (arXiv id / DOI /
   live URL recorded). Empty until then; append-mostly.

A paper moves rightward as its status advances. Direction of travel is
`drafts/ → candidates/ → published/`, and never skips a stage.

## What belongs here (and what never moves in)

`papers/` holds **fresh, purpose-written publishable drafts** — a clean writeup
authored *for* an audience. It is **not** a home for research workings.

The research itself stays where it lives: `open-problems/`, `results/`,
`technical-reports/`, `explorations/`, `tests/`, `models/`. Those are the
**source** a paper draft is written **from**; they are never moved into `papers/`.
So when a result looks like a potential paper, you **write a new document** here —
you do not relocate the working artifacts. This is by design: because nothing is
ever migrated in, cross-repo and in-repo links to the workings never break.

One line: *workings stay put; a paper is a fresh draft written from them.*

## How this maps to the verification tiers

The repo's cross-repo tiers (recorded → internally established → externally
established, per `Coordination - Tri-Repo Division of Labor.md`) line up with the
lifecycle:

- **`drafts/`** may hold anything down to *recorded* or exploratory.
- **`candidates/`** should carry a result at least **internally established** (or
  honestly graded lower, in-text) — survived the repo's own hostile review,
  reproducible from the tree. A candidate is capped at *internally established* by
  the single-process ceiling until it is actually published/externally read.
- **`published/`** is the external step: physical publication is what makes an
  outside record exist. That, plus any peer/specialist read it draws, is the only
  route to *externally established*.

**Publishing is Joe's action, not an agent's.** Agents draft, version, review, and
stage; they never publish, submit, or post. Every graduation (`drafts → candidates`
and `candidates → published`) requires Joe's explicit say-so.

## Legacy flat papers (pre-lifecycle, kept in place)

Older paper writeups that predate the lifecycle. They are **cited as point-in-time
provenance** from `CLAIM-LEDGER.md`, `ROADMAP.md`,
`MATHEMATICAL-INDEPENDENCE-AUDIT.md`, several `tests/`, and audits, so they **stay
exactly where they are** — never relocated. New papers use the lifecycle folders;
these remain at the `papers/` root:

- `typed-forgetting-local-global-obstruction-v0.1.md`, `...-v0.2.md`
- `typed-loss-kernels-obstruction-attribution-v0.1.md`
- `records-finality-readout-separation-v0.1.md`
- `reviews/` — associated skeptical/external review passes.

## Currently

- **Candidates:** none yet.
- **Published:** none yet.
- **In drafts:** the scope-theorem adversarial-hardening deep-research prompt
  (pairs with `open-problems/finite-closed-capability-boundary-scope-theorem.md`).
