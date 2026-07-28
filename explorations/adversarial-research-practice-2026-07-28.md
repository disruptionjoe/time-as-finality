# Adversarial Research Practice: A Reusable Method for Taking a Heterodox Question to a Decision-Ready Conclusion

**Status:** practice codification — serves the charter's Practice goal
([CHARTER.md](../CHARTER.md): "Develop reusable DJC practice for investigating
consequential, unconventional possibilities and reaching honest, decision-ready
conclusions"). Review-only: no claim movement, no method-law for this
repository until promoted; **promotion to a standing surface (a method doc,
workflow, or another repository's governance) is an owner move.** Written to
transfer: every instrument is grounded in one exemplar from this program's
artifacts, cited by pointer, but stated so that a different repository — or a
different investigator with no knowledge of this program — can apply it to a
different heterodox question.
**Date:** 2026-07-28
**What this is:** the instrument set this program used to reach its Goal-2
conclusion ([goal2-charter-verdict-2026-07-28.md](goal2-charter-verdict-2026-07-28.md)),
extracted from the ~20 artifacts in which it is embodied and written down as
practice. It is not a retrospective of this program; program-specific content
appears only inside exemplar pointers.
**Not codified here (deliberately):** orchestration topology (how many agent
arms, which models), workspace plumbing (locks, session sync, versioning
defaults), and two operating disciplines already codified reusably in this
repository's `AGENTS.md` — the North-Star-vs-quick-payoff exploit note and the
construction-fork note. Those are adjacent practice; read them with this file,
do not duplicate them.

---

## The problem this practice solves

A consequential, unconventional possibility — a heterodox physics candidate, a
contrarian institutional thesis, any "probably wrong but expensive if right"
question — fails to standard research habits in two symmetric ways. Reflexive
dismissal: the question is never given a precise enough form to be tested, and
dies of vagueness attributed to falsity. Reflexive protection: the
investigator, having paid the entry cost, moves the target every time a test
bites, and the candidate survives by deformation rather than by evidence.

The practice below is a set of thirteen instruments that jointly close both
failure routes. The organizing principle: **every degree of freedom the
investigator could use to protect a conclusion is fixed in writing before the
evidence arrives, and every result — including null, negative, and
interpretation-only results — is a deliverable with a named witness.** The
instruments are grouped by when they fire in a run: gates before work, the
swing discipline during work, classification and adjudication, closers before
anything routes, ending lines and programs, and standing hygiene.

Terminology, generalized: a **swing** is one bounded investigative act with a
declared target (a calculation, a literature adjudication, a model run, a
comparison). A **wave** is a batch of swings executed together. A **candidate**
is the heterodox possibility, decomposed into rows or branches wherever its
variants differ. The **rival** is the best current account of the same
territory. An **owner** is whoever holds decision rights over a surface an
instrument touches — a person, a repository, or a standing artifact.

---

## Phase A — Gates: before any new work

### 1. The retrieval/freshness gate

**What it is.** Before a wave, two sweeps. Retrieval: enumerate what the
corpus already holds on the target question — prior swings, banked results,
standing stops, corrections already enacted. Freshness: enumerate what changed
since the plan was drafted — overnight landings, corrections to inputs the
plan cites, external results.

**When to fire it.** At the head of every wave, and again (cheaply) before any
arm cites material produced earlier in the same wave.

**The failure mode it prevents.** The corpus ahead of the conversation: the
program re-derives its own banked results, or executes swings whose premises
its own corpus already corrected. Its same-wave variant: one arm's file
carries caveats ("un-blessed, reproduce before grading") that another arm has
already discharged, so the program's artifacts disagree about their own state.
Retrieval weaker than storage is a real and recurring asymmetry; a program
that writes more than it re-reads will rediscover itself.

**Exemplar.** [goal1-model-family-classification-2026-07-27.md](goal1-model-family-classification-2026-07-27.md),
SAME-DAY CORRECTIONS item 4 ("Same-wave staleness"): the classification's
caveat on un-reproduced swing-2 numbers was already discharged in-repo
([foliation-overlay-t586-reproduction-2026-07-27.md](foliation-overlay-t586-reproduction-2026-07-27.md),
17/17) by the time the file landed; the freshness pass caught it and rewrote
the caveat the same day.

### 2. Verification tranches before new claims

**What it is.** When inherited numbers or claims are flagged for verification,
the verification arms run as their own tranche, and their flag-flips are
enacted into the artifacts that carry the flagged material **before** any new
work cites it. Order of operations: verify → correct → then build. A number in
the flagged state is not citable; it is quarantined until its flag resolves.

**When to fire it.** Whenever new work would build on material carrying an
unresolved verification flag; structurally, as a tranche between planning and
execution in every wave that inherits numbers.

**The failure mode it prevents.** Compounding error: a new claim cites a
flagged number, the flag later flips, and the correction now has to propagate
through work that never recorded the dependency. Corrections are cheap at the
tranche boundary and expensive everywhere downstream.

**Exemplar.** [goal1-model-family-classification-2026-07-27.md](goal1-model-family-classification-2026-07-27.md):
the header routes every number through a citation rule and the wave's
flag-flips; corrections 1–3 (the door relabel, the degeneration-condition
split, the margin discharge) are verification-arm results enacted under a
"Read before using any row below" instruction before downstream artifacts
(the Goal-2 verdict among them) consumed the rows.

---

## Phase B — The swing discipline: the unit of investigation

### 3. Pre-registered kills

**What it is.** Every swing declares, before execution and in writing: what
result would kill the candidate element under fire, and at what scope (which
rows, branches, or readings die; which survive regardless). The declaration is
frozen and quoted verbatim in the result. Verdicts take one of three forms:
KILL FIRES (with exact scope), KILL DOES NOT FIRE, or FIRES CONDITIONALLY
(with every exit of the fork priced). **Null results are deliverables**: a
swing that returns "null, as pre-registered" is a completed swing that
narrowed the space, not a failed one — write it up with the same care as a
positive.

**When to fire it.** At the specification of every swing — investigative,
computational, or literature-facing. A swing without a registered kill is
reading, not testing.

**The failure mode it prevents.** Outcome-shopping: deciding after the
evidence which result "counts." And its quieter twin, unfalsifiable
investigation — activity no possible outcome of which would have changed
anything, discovered only after the budget is spent.

**Exemplar.** [swing5-suppressed-percolation-adjudication-2026-07-28.md](swing5-suppressed-percolation-adjudication-2026-07-28.md)
(status header: "Registered kill: fires on the gravitational-confinement
mechanism as published… It does not fire on three successor branches" — scope
declared row by row);
[rival-symmetry-swings-2026-07-28.md](rival-symmetry-swings-2026-07-28.md)
("The three registered kills (verbatim, declared before execution)"). For the
null-as-deliverable form:
[landauer-rate-and-capability-indexed-discriminator-2026-07-27.md](landauer-rate-and-capability-indexed-discriminator-2026-07-27.md)
(NULL_REFINEMENT_AS_PREREGISTERED).

### 4. Burden symmetry

**What it is.** Before any comparative conclusion, the rival receives the same
instrument treatment as the candidate: pre-registered kills, declared before
execution, attacks steelmanned — because a rival surviving weak attacks earns
nothing. After symmetric fire, the two cost columns may honestly differ;
symmetric fire does not mean symmetric damage, and the conclusion may say so.
The output is the rival's **earned form** — the strongest statement of the
rival that survived, with its priced debts attached — which then binds every
comparative use.

**When to fire it.** Before concluding any comparison. Audit the ledger: if
the candidate carries N adversarial artifacts and the rival carries zero
registered kills, the comparison is blocked until the asymmetry is repaired.

**The failure mode it prevents.** A comparison rigged by attention: the
candidate looks weak because only the candidate was attacked. The presumption
that the incumbent is "already complete on its own terms" is exactly the kind
of claim that must be put under registered fire, not assumed.

**Exemplar.** [rival-symmetry-swings-2026-07-28.md](rival-symmetry-swings-2026-07-28.md):
a program-adversary arm ruled the ten-plus-to-zero adversarial asymmetry
blocked any comparative conclusion; three registered kills were then executed
against the rival, and the surviving rival's earned form ("GR + causal partial
order **+ a thermodynamic commit module**," with three priced debts) is the
form the conclusion artifact is bound to
([goal2-charter-verdict-2026-07-28.md](goal2-charter-verdict-2026-07-28.md) §3).

### 5. Fixture honesty

**What it is.** Any finding derived from a hand-built model (a fixture, a toy
world, a constructed dataset) is classified into one of three citation
classes: **typing-theorem** (holds for every instance expressible in the
formalism's types — provable, fixture-independent), **regime fact** (holds
under a construction discipline the fixture obeys by hand; the discipline must
be named and the boundary located), or **one-fixture artifact** (specific
values with no generality). The classifier is a **fixture-family sweep**: run
the same derivations over a pre-registered randomized family of fixtures
spanning regimes that break the hand-built fixture's implicit disciplines, and
prove as theorems whatever survives everywhere. Publish an earned-wording
table: for each headline finding, the wording it had, its class after the
sweep, and the wording it has earned. Two corollaries: a
**necessary-given-fixture** result may not be cited as contingent evidence for
the candidate; and deletion/contingency tests ("delete the candidate
structure — does the result change?") must declare their modality frame — what
class of alternatives the deletion ranges over — since necessity relative to
one fixture family is not necessity simpliciter.

**When to fire it.** Before any fixture-derived finding is cited outside the
note that produced it, and mandatorily before such a finding enters a
conclusion or a cost column.

**The failure mode it prevents.** Laundering construction choices as results:
a fact about where the author happened to draw two edges circulates as a fact
about the formalism. The sweep also catches the reverse error — a genuine
theorem timidly hedged as "in this fixture" and undersold.

**Exemplar.** [fixture-family-sweep-2026-07-28.md](fixture-family-sweep-2026-07-28.md):
600 fixtures, three regimes, predictions pre-registered before execution;
of three headline findings, one upgraded to typing-theorem
(foliation-adds-nothing, a dead-input factorization), one demoted to
regime-dependent (causal-does-more-constraining-work — an alignment
discipline, reversible in type-legal fixtures), and two revealed to be the
same fact counted twice; the "Consequences for citability" table is the
earned-wording deliverable.

### 6. Provenance-must-travel

**What it is.** Every load-bearing number, quote, and existence claim carries
its provenance class, and the classes travel with the note wherever it is
cited: **fetched-verbatim** (verified against a source obtained this run, with
extraction-layer caveats stated); **abstract/metadata-level screen** (labeled;
loads nothing alone); **in-note arithmetic** (one line from quoted formulas,
recomputable); **recalled/background** (unfetched memory — a standing debt,
listed as such); **wave-attributed** (produced by an orchestration layer,
pending recomputation in the corpus). Conditional numbers never appear without
their assumption set. Negative existence claims ("no rebuttal exists," "no
such construction is published") state their exact search bounds — queries,
databases, dates — and the evasion routes a counterexample could take.

**When to fire it.** Continuously during any swing that touches sources or
produces numbers; audit at the closer stage. The note's provenance section is
part of the deliverable, not an appendix.

**The failure mode it prevents.** Confidence leaking across the
fetch/recall boundary: a half-remembered figure hardening into a cited fact;
a bounded search circulating as a proof of absence; a conditional bound quoted
without the assumptions that make it true.

**Exemplar.** [swing5-suppressed-percolation-adjudication-2026-07-28.md](swing5-suppressed-percolation-adjudication-2026-07-28.md),
"Provenance and unverifiables (must travel with this note)": verified-verbatim
inventory with recovered-truncation flags, citers-scan bounds stated
query-by-query with the named evasion route ("a rebuttal published without
citing the paper it rebuts would evade this method"), recalled items listed as
debts. For the assumption-set rule:
[goal1-model-family-classification-2026-07-27.md](goal1-model-family-classification-2026-07-27.md) §6.

---

## Phase C — Classification and adjudication

### 7. The three-bin measure

**What it is.** Every candidate variant is classified into exactly one of
three bins: **(1) discriminable** — states an in-principle observable
difference from the rival; **(2) equivalent-but-explanatory** — empirically
equivalent to the rival but claiming explanatory gain, a claim that must then
itself be adjudicated (instrument 8); **(3) undefined-and-withdrawn** — cannot
state its commitments precisely enough to occupy either other bin, withdrawn
with named revival conditions. The bins are **precision-and-situation
classifications, never truth verdicts**: bin 1 does not mean true, bin 3 does
not mean false — it means not yet statable. Bin membership is checked against
a declared candidate schema (what a candidate must state: its posited
structure, dynamics, coupling, relation to observables, scope); bin movements
are events with witnesses, executed by the classification's owner.

**When to fire it.** At program start, to force the loose intuition into
rows; and at every kill or adjudication result, to record where each row now
sits.

**The failure mode it prevents.** Vagueness surviving as liveness — the
undefined candidate that is never wrong because it is never anything; and its
inverse, treating "empirically equivalent" as either a vindication or a
refutation when it is a situation with its own further burden.

**Exemplar.** [CHARTER.md](../CHARTER.md) Goal 1 measures (the bin definitions
and the five-element schema) as instantiated by
[goal1-model-family-classification-2026-07-27.md](goal1-model-family-classification-2026-07-27.md)
— itself scoped as "an assembly of graded-elsewhere inputs, not a grading,"
with bin movements landing as witnessed correction events (items 7 and 9).

### 8. Pre-registered adjudication gates with degeneration scoring

**What it is.** A protean candidate — a reading or interpretation that can
reshape under pressure — is never adjudicated freestyle. Before adjudication,
fix in writing: **(a)** the admissible form(s) of the candidate, with any
already-derivable convictions pre-enacted (do not re-litigate what the corpus
has proven); **(b)** could-fail commitments C1…Cn, each independently
checkable; **(c)** adversary amendments — what may NOT be counted as support
(e.g., accommodation of nulls pre-excluded as explanatory content), and the
deflationary outcome priced as live; **(d)** scoreable degeneration moves
(D-types: coupling oscillation, explanandum migration, immunization upgrades,
package retreat, rival demotion by fiat — adapt the list to the candidate)
with a numeric conviction threshold; **(e)** an exhaustive set of terminal
states, including at least one honorable one (EARNED / INTERPRETATION-ONLY /
WITHDRAWN-with-revival-conditions). Critically, the gate is fixed **before the
adjudicating arm reads the candidate's case**, is quoted verbatim in the
adjudication, and is not renegotiated. The adjudication records a
degeneration baseline (D-count and precision state) so that future drift is
mechanically convictable against today's numbers rather than against memory.

**When to fire it.** Whenever the thing under adjudication is an
interpretation, a reading, or any candidate whose content can migrate; always
before adjudicating bin-2 (equivalent-but-explanatory) claims.

**The failure mode it prevents.** Gerrymandered adjudication — the candidate
reshaping to pass whatever test is being applied, or the adjudicator reshaping
the test to reach a preferred verdict; and unconvictable future drift, where
a candidate degenerates slowly and no single step is caught.

**Exemplar.** [constitutive-reading-adjudication-2026-07-28.md](constitutive-reading-adjudication-2026-07-28.md):
gate constructed by a strategy arm, amended by a program-adversary arm, fixed
before the execution arm read the case; six commitments, three binding
adversary amendments, five D-types with conviction at D ≥ 2 across ≥ 2 types
with P = 0, three terminal states; verdict INTERPRETATION-ONLY reached by the
gate's own fork, baseline D = 0, P = 1 recorded.

---

## Phase D — Closers: before anything routes or commits

### 9. Adversary and completeness closers

**What it is.** Two passes stand between a wave's products and anything
downstream. The **adversary closer** is a hostile pass over the wave's own
output: it tries to refute the headline results, hunts category fusions and
internal contradictions, and catches same-wave staleness (instrument 1's
in-wave variant). Its findings are fixed **pre-commit** — blockers and majors
do not ride along as known issues. The **completeness closer** reconciles
three ledgers: promised-vs-delivered (every swing spec accounted for —
executed, superseded, or explicitly declined), delivered-vs-routed (every
result landed where its consumers will look), and **decided-vs-written**:
every decline and negative decision is written down with its reason. An
unwritten decline evaporates — the question will be re-opened by rediscovery
and the reasoning re-paid. Seams between same-wave artifacts that cannot be
smoothed honestly are recorded as seams.

**When to fire it.** At the close of every wave, after execution and
verification, before routing, committing, or citing the wave's products
anywhere.

**The failure mode it prevents.** Two: self-satisfied waves (the most damaging
error found in a wave is characteristically found by its own closing
adversary, when it is still cheap to fix), and silent attrition — promised
work quietly dropped, results produced but never routed, declines that exist
in no artifact.

**Exemplar.** [goal1-model-family-classification-2026-07-27.md](goal1-model-family-classification-2026-07-27.md),
SAME-DAY CORRECTIONS ("Applied per the closing adversarial pass") — item 1,
the door relabel, was the adversary's most-damaging finding, a category fusion
the file's own §6 rule forbids, fixed pre-commit;
[swing5-suppressed-percolation-adjudication-2026-07-28.md](swing5-suppressed-percolation-adjudication-2026-07-28.md),
"Series closure" (the promised-vs-delivered ledger for a five-swing series,
with a same-wave update at commit); for recorded seams,
[goal2-charter-verdict-2026-07-28.md](goal2-charter-verdict-2026-07-28.md) §6
("Cross-artifact seams (recorded, not smoothed)").

### 10. Same-day corrections blocks and enactment discipline

**What it is.** An artifact that needs correction gets a dated corrections
block at its head, with a "read this before using any row below" instruction.
A correction exists in one of two explicit states: **proposed-not-enacted**
(recorded in the block; the body unchanged; downstream users warned) or
**ENACTED** (the body updated; the block retained, with the enactment date, as
the change record). Enactment updates the tables AND keeps the block —
never one without the other. Proposed edits to artifacts owned elsewhere stay
proposed until their owner enacts them.

**When to fire it.** The same day a correction is known, whenever an already-
cited artifact turns out wrong or stale; enactment when the artifact's owner
folds the corrections in.

**The failure mode it prevents.** Both halves of the correction dilemma.
Silent retro-editing destroys the audit trail (a reader can no longer tell
what earlier work was actually citing). Correction-noting without enactment
leaves the stale body live (a hurried reader consumes the table and never
reaches the errata). The two-state discipline defeats both, and makes
"proposed" a first-class, queryable status rather than a hope.

**Exemplar.** [goal1-model-family-classification-2026-07-27.md](goal1-model-family-classification-2026-07-27.md)
("Corrections 1–9 ENACTED into the table and verdict 2026-07-28; the block
remains as the change record");
[constitutive-reading-adjudication-2026-07-28.md](constitutive-reading-adjudication-2026-07-28.md)
(§9: "classification edits proposed, not enacted" — the proposed state, held
across an ownership boundary).

---

## Phase E — Ending well: lines and programs

### 11. Stop-and-reopen packets

**What it is.** When a line of work proves sterile, it does not trail off; it
gets an explicit **stop**: a written statement naming the move that is now
forbidden (the move proven sterile) and enumerating the specific conditions
under which the line reopens. Reopening then requires a **compliance-argued
packet**: a document that quotes the stop verbatim, argues clause by clause
which reopening condition it satisfies and why, states honestly which
conditions it does **not** invoke, and leaves the reopening decision — and any
minting of new numbered scaffolds — to the stop's owner. Momentum ("we have
more ideas in this direction") is never a reopening condition.

**When to fire it.** The stop: whenever a swing or series demonstrates that a
class of follow-on work is sterile. The packet: whenever anyone — including
the stop's own author, later — wants back in.

**The failure mode it prevents.** Zombie lines: sterile directions producing
scaffold after scaffold because stopping was never made explicit; and its
overcorrection, permanent closure of a line that a genuinely new kind of input
should reopen. The named conditions make reopening mechanical rather than
rhetorical.

**Exemplar.** [../tests/T587-t586-causal-collapse-boundary-attack.md](../tests/T587-t586-causal-collapse-boundary-attack.md)
with [../results/T587-t586-causal-collapse-boundary-attack-v0.1-results.md](../results/T587-t586-causal-collapse-boundary-attack-v0.1-results.md)
("Do not continue producing T-number scaffolds from T586 alone. Reopen Lane 1
only for a provenance-valid physical source packet, a frozen capability
witness, or a sharper counterexample that changes the record-issuance
contract"); the compliant answer:
[proposed-composition-extensivity-gate-2026-07-28.md](proposed-composition-extensivity-gate-2026-07-28.md)
("Why This Packet Satisfies T587's Reopening Conditions" — clause-by-clause,
no number minted, non-invoked conditions stated, owner decides).

### 12. The conclusion form

**What it is.** A decision-ready conclusion is a single artifact with a fixed
anatomy. **What is forced:** each kill stated with its witness (a pointer to
the artifact that carries the evidence), its exact scope (which routes closed;
which survive), and its named revival conditions — with the standing caveat
that none of these is a truth verdict about nature; each is the closure of a
stated route. **What remains open:** each open question with its monitorables
routed into a standing register that future service re-verifies mechanically.
**The strongest surviving rival:** at its earned, priced form (instrument 4),
binding on comparative use. **The honest modal:** the named evidence-states
that would flip or harden the verdict, so the conclusion is supersedable by
mechanism rather than by relitigating. Two legitimacy rules frame the whole:
**interpretation-only is a legitimate terminal state** (a candidate may end as
a coherent reading with no evidential work to do, and saying so is a result),
and **a precise failure is a successful outcome** — the program succeeded if
it can say exactly where and why the candidate fails, with witnesses.

**When to fire it.** When a charter-level question is answerable at the
current evidence-state; also, in miniature, at the close of any major line.

**The failure mode it prevents.** The two degenerate endings: the triumphant
vague conclusion (a verdict with no witnesses, scope, or revival conditions —
unauditable and unfalsifiable), and the unconcluded program that never
converts its accumulated kills into a statement anyone can act on.

**Exemplar.** [goal2-charter-verdict-2026-07-28.md](goal2-charter-verdict-2026-07-28.md):
§1 what is forced (six closures, each with witness + scope + revival
conditions), §3 the rival's earned form with its cost column, §4 the verdict
("the answer is NO… and the failure locus is exact" — explicitly a success in
the charter's second mode), §5 the honest modal (seven named flip/harden
states, routed into
[standing-monitorables-2026-07-28.md](standing-monitorables-2026-07-28.md)),
§7 what the verdict does not claim.

---

## Phase F — Standing hygiene

### 13. Throughput and routing hygiene

**What it is.** Three standing rules that hold the corpus navigable and the
ownership boundaries intact. **Net-limited new notes:** prefer annotating
existing artifacts in place over minting new files; count net-new notes per
wave and keep the count small (a wave that lands a dozen results may
legitimately create one or two files). **Pointer routing across boundaries:**
a result that bears on another owner's surface routes as a pointer — naming
the source, the boundary, and the receiving owner's disposition — without
copying the owner's truth into the local corpus or rewriting local truth into
theirs; a finding that would change the status of an artifact owned elsewhere
is an **input to that owner**, never a unilateral regrade. **Owner decisions
surfaced, never taken:** anything requiring a decision by a surface's owner
(a human, a repo, a standing artifact's steward) is named, queued, and left
undecided — taking it silently is the violation even when the call is obvious.

**When to fire it.** Continuously; audited by the completeness closer
(instrument 9).

**The failure mode it prevents.** Corpus sprawl (retrieval — instrument 1 —
degrades with every redundant note, and the program starts rediscovering
itself); truth forks across repositories (two copies of one claim drifting
apart, each citable); and jurisdiction creep, where an energetic wave quietly
makes calls that were never its to make.

**Exemplar.** [swing5-suppressed-percolation-adjudication-2026-07-28.md](swing5-suppressed-percolation-adjudication-2026-07-28.md),
"What This Does Not Claim" ("The 'bin pending → bin 3' resolution is an input
to the swing-3 owner… not a unilateral regrade of that file");
[CHARTER.md](../CHARTER.md) Goal 3 measure ("Cross-repository use names the
source, boundary, and receiving-owner disposition without copying owner
truth"); [goal2-charter-verdict-2026-07-28.md](goal2-charter-verdict-2026-07-28.md)
header ("no private-surface or chat-wave citation is load-bearing anywhere in
this file").

---

## Minimum viable run

One page for applying this to a new question, in order. The full practice is a
wave-scale discipline; the minimum viable run is what a single investigator
can execute on one heterodox question without an orchestration stack.

**0. State the question and the finish line.** Write the charter-level
question in one sentence, and the two-sided success condition next to it:
what a win looks like AND what a precise failure looks like. Both are
successful outcomes; say so at the start (instrument 12's legitimacy rules,
adopted on day one). Decompose the loose intuition into rows via the candidate
schema and bin them (instrument 7) — most heterodox intuitions turn out to be
several candidates, in different bins, with different fates.

**1. GATE.** Retrieval: what already exists on this question — in your own
corpus and in the field's record (instrument 1). Verify what you inherit:
every number your plan leans on gets a provenance class now, and flagged
material is resolved before anything builds on it (instruments 2, 6). Then
write the swing specs with registered kills, scopes, and — if any candidate is
protean — the full adjudication gate, fixed before you engage the candidate's
case (instruments 3, 8). Freeze these.

**2. SWINGS.** Execute against the frozen specs. Label provenance as you go,
not retrospectively (instrument 6). Anything derived from a hand-built model
gets its citation class before it travels (instrument 5). Give the rival its
registered fire before you draft any comparison (instrument 4). Write null
results up as deliverables the day they land (instrument 3).

**3. CLOSERS.** Run the hostile pass over your own products; fix blockers and
majors before anything routes (instrument 9). Run the completeness ledger:
promised-vs-delivered, delivered-vs-routed, and every decline written with its
reason (instrument 9). Land corrections as dated blocks and enact them —
tables updated, block kept (instrument 10).

**4. ROUTE.** Annotate in place; mint net-new notes sparingly (instrument
13). Route cross-boundary results by pointer and surface — do not take —
owner decisions (instrument 13). Write explicit stops on sterile lines, with
named reopening conditions (instrument 11).

**5. CONCLUDE.** Write the conclusion in the fixed anatomy: forced (witness +
scope + revival conditions per kill), open (with monitorables in a standing
register), strongest surviving rival at its earned form, and the honest modal
of flip/harden states (instrument 12).

**The four-instrument floor.** If the question is small and the budget is
days, the irreducible core is: registered kills before execution (3),
provenance labels that travel (6), one genuinely hostile pass before anything
ships (9), and a conclusion with witnesses and revival conditions (12). A run
missing any of these four is not this practice; everything else scales with
the stakes.

---

## LIMITS

Where this practice is expensive, where it is overkill, and what it cannot
catch. A practice note that omitted this section would fail its own closers.

**Where it is expensive.** The full instrument set roughly doubles the cost of
every wave: pre-registration, verification tranches, symmetric rival fire,
fixture sweeps, and two closer passes are all work that produces no new
positive result. The spend is justified when conclusions are consequential and
the candidate or investigator has protective incentives — that is, precisely
on heterodox questions. The corrections/enactment and routing machinery also
presumes a written, versioned corpus with stable pointers; in an ephemeral
setting (conversation-only investigation) most of Phase D and F has nothing to
grip, and the practice degrades to the four-instrument floor.

**Where it is overkill.** Questions with a cheap decisive test — run the test;
the ceremony adds nothing a single well-provenance'd result does not.
Exploratory reading before any candidate exists — instruments 3 and 8 need a
statable target; firing them at a mood produces bureaucratic pre-registrations
of nothing. Mature-literature questions the field has already adjudicated —
there the work is retrieval and provenance (instruments 1, 6), not fresh
adversarial process. And low-stakes internal tooling decisions, where the
completeness closer's decline-ledger is worth keeping and the rest is not.

**What it cannot catch.**

- **Shared blind spots between adversary and author.** The hostile pass is
  drawn from the same distribution as the work it attacks — same investigator
  or same model family, same formal toolkit, same era's assumptions. It
  reliably catches internal inconsistency, staleness, and category fusion; it
  cannot see an assumption invisible to both sides. (This program's adversary
  and author arms share a substrate; the instrument's record shows it catching
  the author's errors, and shows nothing about errors of the shared frame.)
  Partial mitigation — external review, human experts, a differently-trained
  adversary — is routing work the practice can name but not perform.
- **External-literature blind spots when search is bounded.** Negative
  existence claims are only as good as their stated bounds: a rebuttal that
  does not cite the paper it rebuts evades a citers scan; terminology drift
  evades title search; unindexed or paywalled literatures evade everything.
  The practice forces the bounds to be stated (instrument 6); it cannot widen
  them.
- **Gaming at the choice-of-kill stage.** Pre-registration disciplines what
  happens after the kill is declared; it cannot force the declared kill to be
  ambitious. A program can honestly execute weak kills forever. The partial
  guard is the conclusion form's witness requirement (an unimpressive kill
  reads as unimpressive when its scope is stated exactly) — but the practice
  measures honesty, not courage.
- **Fixture families are still designed.** The sweep (instrument 5)
  randomizes within a declared type; the type itself can embed the blind
  spot. A typing-theorem is relative to the typing.
- **Degeneration scoring convicts only declared D-types.** A candidate can
  drift along a dimension nobody thought to score. The baseline makes drift
  visible in hindsight; it does not make the D-list complete.
- **A wrong charter.** The practice optimizes the path from a stated question
  to an honest conclusion. Run flawlessly on a mis-posed question, it yields
  precise, well-witnessed answers to the wrong thing. Nothing below the
  charter can catch an error in the charter.
- **Decision-readiness is indexed, not permanent.** The conclusion form's
  honest modal makes supersession mechanical, but "decision-ready" always
  means "at this evidence-state, within these bounds." The practice produces
  conclusions that are honest about their own fragility — not conclusions
  that cannot break.

---

## What This Does Not Claim

- No claim movement, no bin regrade, no guardrail edit, no method-law: this
  file describes practice; it binds nothing in this repository until an owner
  promotes it to a standing surface.
- No novelty claim: individual instruments have well-known ancestors
  (pre-registration from experimental methodology; adversarial review;
  provenance discipline from evidence law and metrology). What is codified
  here is the assembled, ordered set as this program ran it.
- No completeness claim: this is the instrument set embodied in the cited
  artifacts as of 2026-07-28; later waves may earn instruments this note does
  not contain.
- No claim that the exemplar program's conclusions are correct: the pointers
  ground the instruments, not the physics.

## Provenance (pointers only)

All exemplars are in-repo artifacts, cited by relative pointer above; none of
their content is copied here beyond short quoted phrases. Load-bearing
grounding, per instrument: 1, 2, 7, 10 —
[goal1-model-family-classification-2026-07-27.md](goal1-model-family-classification-2026-07-27.md)
(header, SAME-DAY CORRECTIONS block, §6); 3, 6, 9, 13 —
[swing5-suppressed-percolation-adjudication-2026-07-28.md](swing5-suppressed-percolation-adjudication-2026-07-28.md)
(status header, Provenance, Series closure, What This Does Not Claim), with
[landauer-rate-and-capability-indexed-discriminator-2026-07-27.md](landauer-rate-and-capability-indexed-discriminator-2026-07-27.md)
for the null-as-deliverable form; 4 —
[rival-symmetry-swings-2026-07-28.md](rival-symmetry-swings-2026-07-28.md);
5 — [fixture-family-sweep-2026-07-28.md](fixture-family-sweep-2026-07-28.md);
7 — [CHARTER.md](../CHARTER.md) (Goal 1 measures; guardrails); 8 —
[constitutive-reading-adjudication-2026-07-28.md](constitutive-reading-adjudication-2026-07-28.md);
11 — [../tests/T587-t586-causal-collapse-boundary-attack.md](../tests/T587-t586-causal-collapse-boundary-attack.md),
[../results/T587-t586-causal-collapse-boundary-attack-v0.1-results.md](../results/T587-t586-causal-collapse-boundary-attack-v0.1-results.md),
and [proposed-composition-extensivity-gate-2026-07-28.md](proposed-composition-extensivity-gate-2026-07-28.md);
12 — [goal2-charter-verdict-2026-07-28.md](goal2-charter-verdict-2026-07-28.md)
and [standing-monitorables-2026-07-28.md](standing-monitorables-2026-07-28.md).
The wave-tranche ordering (gate → execution → verification → closers) is
additionally documented on orchestration-layer memory surfaces outside this
repository; those are pattern sources only and are not load-bearing anywhere
in this file — every ordering claim above is grounded in the in-repo
artifacts' own headers and corrections blocks. Adjacent already-codified
practice referenced, not duplicated: this repository's `AGENTS.md` operating
notes (North-Star-vs-quick-payoff; the construction fork).
