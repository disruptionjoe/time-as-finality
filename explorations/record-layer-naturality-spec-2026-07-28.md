# Record-Layer Naturality of Reconciliation: Spec and First Probe

**Status:** specification + executed finite probe; review-only — no claim
movement, no T-number, no posture change. Verdict shape: **SPLIT BY
CANONICITY** (pre-registered, then confirmed on the probe fixture).
**Date:** 2026-07-28
**Registered residual:** `ROADMAP.md` 2026-07-27 routing correction — "TaF's
own remaining question is narrower and record-local: is the
record-reconciliation map natural? If it is, A and C are operationally
identical at the record layer and issuance lives strictly below records."
**Builds on:** [T584](../tests/T584-capability-invariance-morphism-gate.md)
(admissible morphism classes: representation, gauge, irrelevant
coarse-graining); [T585](../tests/T585-landauer-physical-capability-gate.md)
and [T586](../tests/T586-record-capability-order-gate.md) (the record fixture
class; clock labels shown order-inert);
[T587](../tests/T587-t586-causal-collapse-boundary-attack.md) (the stop this
work must comply with);
[T588](../tests/T588-record-issuance-contract-fork-gate.md) (contracts A and
C; the residual discriminator);
[merge-transport-dichotomy-2026-07-27](merge-transport-dichotomy-2026-07-27.md)
(scope limit 4: the naturality route survives the connection no-go).
**Carried as pointers, not rebuilt:** temporal-issuance's PP-3, D-FORK,
FUNCTOR-OBL-001, TI-C020 (TI `CLAIM-LEDGER.md`, `FORMAL-OBJECT.md`); the
withdrawal notice `system-runtime/mailboxes/temporal-issuance/
20260727-d-fork-restated-as-is-there-a-bundle.md` (the bundle/holonomy gloss
is withdrawn; "the naturality criterion is untouched" — survives explicitly).
**Model:** [../models/record_reconciliation_naturality_probe.py](../models/record_reconciliation_naturality_probe.py)
(stdlib-only, 155 lines, executed, exit 0; outcome content is data, not an
assertion)
**Tags:** `finite_witness` · spec (the probe corroborates one-line symbolic
arguments on a declared small fixture; it is not the source of the
generality, and no hardness, continuum, or physical claim is made)

---

## Reopening compliance (T587)

T587 closed with: *"Do not continue producing T-number scaffolds from T586
alone. Reopen Lane 1 only for a provenance-valid physical source packet, a
frozen capability witness, or a sharper counterexample that changes the
record-issuance contract."*

This work complies as follows.

- It is not a T-number scaffold and mints no T-number.
- It is not a comparator on the frozen T586 event system. It never touches
  T586's events, its produced-record dependency closure, or its order
  relation. T587 showed that whole move class is absorbed; nothing here
  re-enters it.
- Its object is the **reconciliation clause of the record-issuance
  contract** — the `r` map of T588's contract C. T588 lawfully reopened Lane
  1 under T587's third condition, and its declared residual discriminator
  ("whether observers who meet end up holding a shared record structure or
  merely comparable independent ledgers... a question about what
  reconciliation does at contact") is exactly the territory this spec works. This is a
  continuation *inside* T588's opened residual, not a fresh reopening and
  not a new comparator.
- Disposition: exploration + exploration-attached probe, review-only. No
  claim-ledger movement, no revival of T586's downgraded order claim.

## The residual, restated

T588 left A (per-observer ledgers) and C (regional ledgers reconciling at
contact) standing and count-indistinguishable. The routing correction sent
the source question (PP-3 / D-FORK) to temporal-issuance and kept one
record-local question here: **is the record-reconciliation map natural with
respect to TaF's own admissible morphism classes?** If yes, A and C are
operationally identical at the record layer and issuance, if real, lives
strictly below records. If no, TaF holds a record-layer witness object.

## Construction fork declaration

Per the house discipline (identify, name, stay open): the load-bearing
objects here are **program-native record stores** in the T585/T586
construction — records as issued discrete items carrying bookkeeping labels.
No standard-physics construction is load-bearing. The twin fixture's
proper-time ratio is inherited from T588's standard special-relativistic
construction, but it enters only by fixing the two stores' cardinalities
(2 versus 1); nothing below depends on the ratio's value or origin.

## Formalization

Let **AdmCtx** be the category whose objects are declared observer contexts
and whose morphisms are T584's admissible classes: substantive representation
changes, gauge changes, and declared irrelevant coarse-graining. Let

- `Rec : AdmCtx -> Set` assign each context its record store, with admissible
  morphisms acting elementwise on records (T584's surviving content,
  instantiated at the record layer);
- `∨` be the (partial) contact operation: `C1 ∨ C2` is the joint context
  formed where the two contexts make causal contact;
- `r_{C1,C2} : Rec(C1) × Rec(C2) -> Rec(C1 ∨ C2)` be the reconciliation
  family — what contract C says happens at contact.

**Declared assumption CONTACT-FUNCTORIALITY.** Admissible `f : C1 -> C1'`
and `g : C2 -> C2'` induce an admissible `f ∨ g : C1 ∨ C2 -> C1' ∨ C2'`. Its
action is fixed on origin-tagged records by the component morphisms, and on
generated metadata by **reference consistency**: metadata that cites record
IDs must follow renames or it dangles. (For metadata carrying free-standing
values rather than references, the action would need separate declaration —
see Uncertainties.) If CONTACT-FUNCTORIALITY itself fails, that is a prior,
coarser form of contact-generated structure — call it **outcome class 0** —
and the naturality question does not typecheck. Not probed here.

**The naturality question.** With `F(C1,C2) = Rec(C1) × Rec(C2)` and
`G(C1,C2) = Rec(C1 ∨ C2)`, both functors `AdmCtx × AdmCtx -> Set`, is `r` a
natural transformation `F ⇒ G`? Concretely, for all admissible `f, g`:

```text
Rec(f ∨ g) ∘ r_{C1,C2}  =  r_{C1',C2'} ∘ (Rec f × Rec g)
```

**What YES means.** If the square commutes for all admissible `f, g`, then
`r` descends to admissible-equivalence classes: the reconciled store, up to
admissible relabeling, depends only on the component stores up to admissible
relabeling. Every piece of contact-generated structure is determined by the
components up to admissible relabeling — **disclosure-shaped**. Operationally:
no record-layer observable built from reconciled stores separates contract C
from contract A, because C's "shared record structure" is then an admissible
re-presentation of A's comparable independent ledgers. In that case issuance,
if it exists at all, lives strictly below the record layer.

**What NO means.** A witness is a pair of stores and admissible `(f, g)` with
`Rec(f ∨ g)(r(R1,R2)) ≠ r(Rec f (R1), Rec g (R2))`. The discrepancy is
structure in the joint store that componentwise admissible relabeling cannot
absorb — the record-layer shadow of the A/C fork. Two sub-cases must be kept
apart:

- **removable:** the failure reflects an arbitrary choice inside the
  reconciliation rule (an enumeration order, a label read); a canonical rule
  with the same operational content exists and is natural. This is an
  implementation artifact, not a witness of anything below records.
- **essential:** no natural family produces the operationally required
  contact content at all. Only this case is a genuine record-layer witness
  object.

## Why prior no-gos do not block this

- **Merge-transport dichotomy.** The components of `r` are merges —
  non-injective, idempotent-shaped — and the dichotomy killed every
  connection/holonomy reading of such transport. But its own scope limit 4
  states the survival verbatim: "Naturality-based criteria. Natural
  transformations require no invertibility; naturality squares with
  idempotent components are legal." This spec lives on that surviving route.
- **The Shamir caution** (ROADMAP `next_work`): a joint can exceed its parts
  informationally with no type created, and invertibility-style tests misread
  that as creation. Naturality is a commutation test, not an invertibility
  test — it compares two composites of the same maps and never forms
  `r^{-1}` — so the named failure mode does not automatically apply. Whether
  any specific threshold-scheme metadata is canonical under a declared
  admissible class is a separate question, not decided here.
- **The withdrawn bundle restatement.** The holonomy gloss on reconciliation
  metadata is withdrawn and stays withdrawn; the withdrawal notice itself
  records that the naturality criterion is untouched. This spec imports no
  bundle language.

## Admissible-class instantiation at the record layer (declared)

Records are pairs `(record_id, clock_label)`. The probe instantiates:

- **representation:** bijective record-ID relabelings (probed as
  transpositions on a declared ID universe) — T584's representation class;
  cf. T585's bit-label gauge;
- **gauge:** clock-label permutations — justified by T586, which established
  that clock labels are order-inert at the record layer (the clock-label
  comparator control fails to reproduce the record order), so permuting them
  is a within-quotient move;
- **irrelevant coarse-graining:** declared but **not exercised** by the probe
  (the fixture carries no telemetry field to drop). A probe limit, listed
  under Uncertainties.

This is a **declaration**, per T584's discipline. If clock labels were
instead declared physical, the clock-reading form below would stop being a
naturality failure and become lawful dependence on a physical quantity.
Naturality is always relative to the declared admissible class.

## Pre-registered predictions (fixed before execution)

Four reconciliation forms on the fixture (context 1: two records, context 2:
one record; T588 twin fixture at ratio 2):

| form | rule |
|---|---|
| `A_union_provenance` | origin-tagged union, no generated metadata (contract A) |
| `C_canonical_pairing` | union + full-product pairing metadata (contract C, canonical) |
| `C_lex_rank_pairing` | union + pair k-th records in lexicographic ID order (contract C, choice-dependent) |
| `C_clock_match_pairing` | union + pair records with equal clock labels (contract C, gauge-reading) |

- **P1.** The A-form is natural over the full probe sweep: pure tagged union
  commutes with elementwise relabeling.
- **P2.** The C-canonical form is natural: full-product pairing is functorial
  in the inputs.
- **P3.** The C-lex form is non-natural, with witnesses exactly under
  representation renames that flip lexicographic order, and never under pure
  clock gauge.
- **P4.** The C-clock form is non-natural under independent componentwise
  clock gauge, including one-sided cases (`f = id` with `g` a clock swap,
  and conversely).
- **P5 (localization law).** Each choice-dependent form fails precisely under
  the admissible class whose labels its metadata reads: lex-rank reads
  representation labels; clock-match reads gauge labels.
- **P6 (conditional).** If all four forms come out natural, the A/C fork is
  invisible at the record layer on this fixture class; record that as the
  sharper result and stop.
- **Interpretive pre-registration.** The residual question "is r natural?"
  is predicted to be under-determined as posed: contract C does not pin down
  one `r`. Predicted verdict shape: **natural iff the generated metadata is
  canonical (functorial in the inputs); non-natural iff choice-dependent**,
  and the failure content is exactly enumeration-order / label-alignment
  content — the vector-clock/provenance kind.

## The probe (executed)

`models/record_reconciliation_naturality_probe.py` — stdlib-only, 155 lines.
It builds the two stores, applies all pairs from a componentwise morphism
sweep (identity, ID transpositions — context 1's lex-flipping r1a↔z9 and
context 2's r2a↔w0 — clock swaps, and their compositions; 4 × 3 = 12 squares
per form), and tests
`apply_joint(f, g, r(R1,R2)) == r(f·R1, g·R2)` for each form. Sanity checks
(declared maps bijective on their universes; identity square commutes for
every form; morphism application preserves cardinality) gate the exit code;
outcome content is printed as data.

```text
python3 models/record_reconciliation_naturality_probe.py   # exit 0
```

## Outcomes

All three sanity checks pass; exit 0.

| form | squares | failing | status |
|---|---|---|---|
| `A_union_provenance` | 12 | 0 | NATURAL over probe |
| `C_canonical_pairing` | 12 | 0 | NATURAL over probe |
| `C_lex_rank_pairing` | 12 | 6 | **NON-NATURAL** |
| `C_clock_match_pairing` | 12 | 6 | **NON-NATURAL** |

- **P1 CONFIRMED. P2 CONFIRMED.** For both, the symbolic argument carries
  the generality (the probe is corroboration): elementwise relabeling
  commutes with origin-tagged union, and the full product of two stores is
  functorial in each argument, so relabel-then-pair equals pair-then-relabel.
- **P3 CONFIRMED.** Witness square: `f` = ID transposition `r1a <-> z9`
  (lex-flipping), `g = id`. Left side holds pairing `(z9, r2a)` (the old
  lex-first record, renamed); right side holds `(r1b, r2a)` (the new
  lex-first record). The 6 failing squares are exactly those whose `f`
  contains the lex-flipping rename; no failure under pure clock gauge.
- **P4 CONFIRMED.** Witness square: `f = id`, `g` = clock swap on context 2.
  Left side holds `(r1a, r2a)` (the old clock alignment); right side holds
  `(r1b, r2a)` (the new alignment). One-sided failures occur from both
  sides.
- **P5 CONFIRMED.** The failing-square sets localize exactly as predicted:
  lex-rank fails only where representation labels move enough to reorder;
  clock-match fails only where the clock gauge moves between the contexts.
- **P6 not triggered.**
- **Observed sharpening (not pre-registered, reported as observation):** the
  C-clock form's failures occur exactly where the *relative* clock
  permutation between the two contexts is non-identity. The diagonal squares
  — the same clock swap applied to both contexts — commute. Clock-match
  metadata is invariant under the diagonal gauge subgroup and non-natural
  only under independent componentwise gauge: it reads the **relative
  alignment of the two contexts' gauges**, which is precisely the
  vector-clock content the pre-registration named as the expected failure
  substance.

**Verdict (review-only): SPLIT BY CANONICITY.** On this fixture class, the
record-reconciliation map is natural exactly when its generated metadata is
canonical (functorial in the inputs), and non-natural exactly when the
metadata reads representation or gauge labels. The residual A/C bit at the
record layer is therefore **not** "which contract" but **whether the
reconciliation metadata-generation rule is canonical**. Both probed
non-natural forms are the *removable* sub-case: each has a canonical
replacement (drop the rank/alignment read, or pair by content) with the same
record payload, so neither witnesses anything below records.

## What each outcome feeds

**Natural / canonical branch (the branch the probe landed on for lawful
forms).** For reconciliation maps whose generated metadata is canonical under
T584's admissible classes, the record layer is naturality-blind to the A/C
fork: any contact-generated structure is determined by the components up to
admissible relabeling. Handoff statement for temporal-issuance, carried as a
pointer:

> TaF holds no record-layer discriminator for PP-3 in the canonical-
> reconciliation sector. If reconciliation metadata is canonical, contracts A
> and C are operationally identical at the record layer and any genuine
> issuance lives strictly below records. The discriminating power, if it
> exists, is TI's D-FORK physical branch (TI-C020; deciding fixture E042
> 6.2). TaF carries that pointer and does not open it.

**Non-natural branch.** The probed failures are removable and are *not* the
witness object. The genuine object, **named here and not opened**, is:

> **The non-naturalizable-reconciliation-content gate:** does there exist
> reconciliation content that is *operationally required* at causal contact
> (required by some declared record-layer task, in the T583/T585 capability
> sense) and that **no** natural family `r` can generate over the declared
> admissible class? Existence of such content would be a record-layer
> obstruction — issuance's shadow in TaF's own vocabulary. Non-existence
> would close the record layer as a PP-3 witness source entirely.

No T-number is minted for it; opening it lawfully requires T587's conditions
(it would enter as a sharper counterexample changing the record-issuance
contract, with the obstruction exhibited, or not at all).

## Known Physics Constraints

None. No physical claim is made or supported. The twin fixture's proper-time
ratio enters only as store cardinalities; differential ageing is not used,
derived, or needed here.

## What This Does Not Claim

- **No issuance verdict.** Naturality of the lawful forms does not show
  issuance is absent — it shows the record layer cannot see it. Non-
  naturality of the choice-dependent forms does not show issuance is present
  — both probed failures are removable implementation choices.
- **No PP-3 resolution and no criterion rebuilt.** PP-3, D-FORK,
  FUNCTOR-OBL-001, and TI-C020 remain temporal-issuance-owned; this spec
  applies a naturality square at TaF's record layer only and carries TI's
  results as pointers. Whether TI's non-naturality fingerprint and this
  record-layer square are one criterion at two layers is not settled here.
- **Scope limit, stated prominently:** "natural" throughout means natural
  **with respect to T584's admissible morphism classes as instantiated
  above, and nothing larger.** A larger admissible class could break forms
  found natural here; a smaller one relaxes the condition. Clock-label-as-
  gauge is a declaration justified by T586's order-inertness result, not a
  theorem. The probe exercises two of T584's three classes; irrelevant
  coarse-graining is declared but untested.
- **No A-versus-C winner** and no revival of T586's downgraded order claim.
  T588's survivors both still stand; what moved is only the shape of the
  residual (canonicity of metadata, not choice of contract).
- **No claim-ledger, posture, or cross-repo movement.** Review-only; no
  T-number; no publication.
- **No generality from the enumeration.** The probe is `finite_witness`
  corroboration on one declared small fixture. The natural verdicts rest on
  the one-line symbolic arguments; the non-natural verdicts rest on exact
  exhibited witness squares. No continuum or scaling claim.

## Uncertainties

- **CONTACT-FUNCTORIALITY is assumed, not derived.** Outcome class 0 — the
  joint context itself failing to be functorial in its parts — is unprobed
  and would preempt the naturality question rather than answer it.
- **The essential sub-case is fully open.** Whether operationally required
  contact content exists that no natural family can generate (the named
  gate) is not addressed by any probe here; the probed failures are all
  removable.
- **Metadata with free-standing values** (counts, digests) has no
  reference-consistency-forced action under `f ∨ g`; the induced action
  would need separate declaration, and a poor declaration could manufacture
  or hide failures.
- **The coarse-graining leg is untested**; a telemetry-bearing fixture is
  needed to exercise T584's third class.
- **One fixture class.** Stores with richer record structure (payloads,
  entropy ranks, provenance chains as in T125-style ordered traces) could
  host canonicity failures with different content than label-reading.

## Constructive next object (named, not built)

1. **The non-naturalizable-reconciliation-content gate**, as named above —
   the only outcome of this spec that could ever earn a gate of its own.
2. **The coarse-graining leg:** re-run the square battery on a fixture with
   declared-irrelevant telemetry, exercising T584's third admissible class.
