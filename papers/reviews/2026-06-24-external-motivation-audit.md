# Hostile External-Motivation Audit of "A Finite Typed Calculus for Local-to-Global Obstruction Under Information-Losing Morphisms" (v0.2)

**Date:** 2026-06-24
**Reviewer role:** Category theorist and combinatorialist. No knowledge of the
originating research program. I was handed the v0.2 paper cold and asked one
question: are these objects worth studying on their own terms.
**Scope:** This is not a correctness review (the prior two reviews in this folder
already did correctness, and v0.2 has absorbed their corrections honestly). This
is a *motivation* review. The question is independent interest, not whether the
proofs are right. Where I say a result is correct, I mean it; the issue is whether
a working mathematician would care.

---

## 0. The one question, answered first

**Would a mathematician with no knowledge of the originating program find these
objects worth studying?**

**Verdict: NOT EARNED, trending toward a narrow PARTIAL.**

Concretely:

- As a *paper I would referee for a journal or even a workshop*: not earned. I
  would reject or desk-decline. There is no theorem here whose statement makes me
  want to know the proof.
- As a *seed of a possibly interesting question*: a narrow partial. Exactly one
  thing in the paper is a real question rather than a definition or a known fact,
  and the paper itself has just proved that the most natural route to answering it
  is closed. That is honest and slightly interesting, but a closed route to an
  unanswered question is not yet a reason to study the objects.

I will defend this verdict component by component, then give the three objections
a referee actually raises, then say what (if anything) earns interest.

---

## 1. What the paper is actually offering, stripped of framing

The paper is candid, which makes my job easy. Its own Section 10 table grades the
components. Reproduced in my own words:

1. The obstruction is signed-graph imbalance. **Known.** (Harary, Zaslavsky.) The
   paper agrees.
2. The decorated morphisms form a category. **Routine.** The paper agrees.
3. The "loss" annotation composes by union. **Bookkeeping, true by definition.**
   The paper agrees.
4. The attribution predicate is not a Boolean functor. **Claimed small new
   result.**
5. The covariant solution-set map is not a functor; the contravariant one is.
   **Claimed clean result.**
6. Finite-to-infinite boundary verdicts. **Claimed clean small result.**
7. The loss annotation does not separate from neighbor data. **A collapse
   certificate, i.e. a negative result.**

So three components are conceded as known/routine/definitional, one is an
admitted negative result, and the load-bearing positive claims are items 4, 5, 6.
I assess those three as a hostile but fair outside reader.

---

## 2. Component-by-component motivation assessment

### 2.1 Item 4: attribution predicate is not a Boolean functor

**Mathematically correct. Motivationally inert.**

The paper's own proof tells me why I do not care: the identity law already fails,
because the predicate requires nonempty forgetting and identities forget nothing.
A predicate that is false on all identities is *never* a functor for a reason that
has nothing to do with the subject matter. This is not a structural fact about
obstruction; it is a fact about having written down a predicate that excludes
identities.

The second failure (emergent obstruction along a chain) is more honest but still
not interesting on its own terms. "A property of the endpoints of a composite is
not a property of the individual arrows" is the default expectation, not a
surprise. A category theorist's reflex on reading "X is not a functor" is to ask
"then what is the corrected functorial/lax/indexed/fibered object?" The paper does
not deliver one for this predicate. It explicitly leaves "a repaired lax or
indexed functor at infinity" open and does not build it in the finite case either.

A non-functoriality result earns interest only when the *failure* is the
phenomenon (an anomaly, an obstruction class, a genuine obstruction to a desired
structure). Here the failure is a definitional artifact. **No independent interest.**

### 2.2 Item 5: contravariant restriction of solutions is the functor

**Correct, clean, and exactly as standard as it sounds.**

"Feasible-solution sets are contravariant under constraint addition" is something
I would put on a qualifying exam, not in a paper. The monotone map sending a
larger constraint set to a smaller solution set, with inclusions as the functorial
action, is the canonical contravariant powerset-monotone functor. Every
mathematician who has seen Galois connections between constraints and models knows
this. The paper says so itself in Remark 6.5 ("the reader should read Theorem 6.4
as the right functor here is the obvious contravariant one, not as a novel
categorical structure").

I credit the paper for honesty. But honesty about triviality does not create
interest. The covariant-fails / contravariant-works dichotomy is the standard
content of the model-theory-of-constraints folklore (and of antitone Galois
connections generally). **No independent interest.** Its only value is internal:
it resolves a direction the originating program was confused about. An outsider
has no such confusion to resolve.

### 2.3 Item 6: the finite-to-infinite boundary

**This is the most defensible item, and it is still thin.**

The verdicts are: category laws survive, non-functor survives, cross-level
obstruction survives by compactness, and the parity characterization is
continuum-conditional because a coefficient-blind encoding fakes a global section.

The compactness lifts (de Bruijn-Erdos for the countable parity statement, Konig
for the nesting depth) are textbook applications. The one genuinely worth a
sentence is the continuum honesty guard: a scalar/coefficient-blind encoding of a
monodromy-`-1` situation reports a false global section. That is a real and
correct cautionary observation. But it is also well known in the guise "Z/2
parity / first Stiefel-Whitney-style obstruction is not seen by a coefficient-blind
real encoding," and the paper does not build the coefficient-aware obstruction
object that would make it a theorem. It flags the object as future work.

So item 6 is a correct, tidy boundary audit of known facts, with the one
non-obvious piece deferred. As a referee I would call this a good internal
hygiene exercise, not a contribution. **Marginal independent interest at best;
not a result a journal would print.**

### 2.4 Item 7: the collapse certificate

**This is the intellectually most serious part of the paper, and it is a
negative result about the paper's own proposed object.**

The certificate says: the canonical witness obligation factors through the
neighbor-visible realization map `nu`, so it is constant on `nu`-fibers, so no two
cases with the same neighbor data separate. In plain terms: the paper's candidate
new invariant is recoverable from the data that provenance, abstract
interpretation, lenses, and effect systems already carry. The thing they hoped was
new is a function of things that already exist.

I respect this. It is the rare case of a program proving its own object redundant.
But from a *motivation* standpoint it is devastating, not encouraging. The honest
reading is: "we proposed an invariant; we proved it collapses onto known data."
That removes the one candidate that could have carried independent interest.

The escape clause (Proposition 8.5: an obligation reading a hidden source field
separates, but admitting that field absorbs it back into the neighbor package) is
correctly identified as not a separation. It is a moving target that always loses.

**This component is the reason the verdict is "not earned" rather than "weakly
earned."** The paper's own strongest machinery is a proof that its candidate
object is not independent of its neighbors.

---

## 3. The independent-motivation verdict, scored

I score independent motivation on the only axis that matters to an outsider: **is
there a statement here whose truth I want to know before I know its proof?**

| Component | Want to know it? | Why / why not |
|---|---|---|
| Parity = imbalance | No | I already know it (Zaslavsky). |
| Category Res | No | Definitional closure. |
| Loss monoid law | No | True by definition. |
| Non-functor of attribution | No | Fails on identities for a non-structural reason. |
| Contravariant functor | No | Standard antitone constraint/solution Galois map. |
| Finite/infinite boundary | Slightly | Correct hygiene; the one deferred piece is the interesting one. |
| Loss collapse certificate | Somewhat, but it is negative | A program retiring its own object. Interesting as intellectual honesty, not as mathematics I would build on. |
| Open Problem 11.1 | This is the only live one | And the paper shows the natural route to it is closed. |

**Independent-motivation verdict: NOT EARNED.**

The narrow partial credit: Open Problem 11.1 ("does any attribution invariant
separate from neighbor-visible data, given that the canonical one provably does
not") is a real question and is stated precisely. A separation theorem, if it ever
arrived, would be genuinely interesting, because it would say that obstruction
attribution carries information no existing provenance/effect/AI framework
captures. That is a thesis worth wanting. But the paper does not prove it, does
not sketch a candidate construction outside the collapsed canonical one, and has
just demonstrated that the obvious attempt fails. A well-posed open question whose
only known attack is closed is not yet independent motivation. It is a lead.

---

## 4. The three objections a referee actually raises

### Objection 1 (fatal): every positive result is either known or definitional, and the paper says so.

A referee does not need to do prior-art archaeology here, because the authors have
done it against themselves. Items 1-3 are conceded. Items 4-5 are, on inspection,
a predicate that excludes identities and the standard antitone constraint-solution
functor. There is no positive theorem whose statement is both new and
non-obvious. The paper is, by its own grading, a correct re-presentation of known
mathematics plus one negative result. That is a survey paragraph, not a research
contribution. **This objection alone is a reject.**

### Objection 2 (serious): the one candidate object is proven redundant, and no replacement is offered.

The honest move would be to lead with the open separation question and present at
least one *candidate* attribution invariant that lives outside the collapsed
canonical construction, even speculatively, with evidence that it might separate.
The paper instead proves the canonical construction collapses and stops. A
program that retires its own central object without proposing a successor has, for
an outside reader, retired itself. I would tell the authors: come back when you
have a candidate invariant that is not a function of `nu`, or a proof that none
exists (which would itself be a real theorem: "obstruction attribution is
information-theoretically subsumed by existing provenance data"). Either of those
is a paper. The current state is neither.

### Objection 3 (serious): the framing of items 5 and 6 as "clean results" inflates standard facts.

Calling "feasible solution sets are contravariant" a theorem (6.4) and a
de Bruijn-Erdos lift a "survival verdict" (7.1) is grade inflation, even with the
honest remarks attached. A referee reads this as a sign that the authors do not
yet have a calibrated sense of what counts as a result in this area, which lowers
confidence in the (genuinely good) judgment shown in the collapse certificate.
Strip these to "we record the standard facts we rely on" and the paper loses
nothing and gains credibility.

---

## 5. What, if anything, earns independent interest

I will be precise about the thin slice that is not worthless.

**The single idea with independent potential** is the one the paper cannot yet
deliver: a *separation theorem* of the form

> Obstruction attribution under information-losing morphisms carries a
> well-defined invariant that is provably not a function of the data carried by
> provenance, abstract interpretation, lenses, or graded-effect annotations.

If true, that is interesting to people who work on provenance and explanation,
because it would identify a genuine gap in those frameworks. If false (i.e. every
attribution invariant collapses onto neighbor data, the strong form of the
paper's Theorem 8.3), that is *also* interesting, because it is a subsumption
theorem: "you never need a bespoke obstruction-attribution invariant; existing
provenance data determines it." The paper has proved the collapse for one
canonical construction. The interesting paper is the one that proves the collapse
*for all natural constructions* (a real theorem) or exhibits a separating one (a
real counterexample). The current draft does neither; it does the single-case
collapse and correctly declines to generalize.

**Nothing else in the paper earns independent interest.** The category, the
functor direction, and the boundary audit are all things a competent reader
produces as exercises once the setup is fixed.

---

## 6. Comparison to the two prior reviews

The earlier external review and skeptical review (this folder, dated 2026-06-20)
both reached "interesting but mostly known; not publishable as a theorem-driven
contribution," and both pointed at the same fix: a separation theorem or a
canonical loss object. v0.2 has done the right thing in response, but it is the
*pessimistic* right thing: instead of producing the separation theorem, it proved
the canonical object collapses. This is more honest than the earlier drafts and
mathematically cleaner. It also moves the independent-motivation verdict in the
*negative* direction, not the positive one, because the live novelty candidate
those reviews identified has now been shown (in its canonical form) to be
redundant. The program is more honest and less independently motivated than it was
two drafts ago. Both of those are true at once.

---

## 7. Final verdict and the single most important next step

**Independent-motivation verdict: NOT EARNED (with a narrow, clearly-bounded
partial: Open Problem 11.1 is a real question, and the strong form of the collapse
certificate is a real potential theorem).**

The paper is honest, correct, and well-calibrated about its own triviality. None
of that is the same as being worth studying from the outside. An external
mathematician handed this cold finds: known obstruction, routine category, a
non-functoriality that fails on identities, the standard contravariant
constraint-solution functor, a tidy boundary audit, and a negative result that
retires the one candidate object. There is no statement here whose truth I want to
know before its proof, except the open separation question, whose only known
attack the paper has closed.

**Single most important next step toward publishable independent motivation:**

Turn the single-case collapse certificate (Theorem 8.3) into one of two real
theorems, and lead the next paper with whichever you get:

- **(Strong subsumption.)** Prove that *every* attribution invariant on typed
  lossy morphisms factors through the neighbor-visible realization map `nu`, not
  just the canonical witness obligation. This is a theorem of the form
  "obstruction attribution is determined by existing provenance/effect/AI data,"
  which is a genuine and citable negative result that the provenance community
  would care about. It also closes the program cleanly.

- **(Separation.)** Exhibit one attribution invariant, defined outside the
  canonical witness-obligation construction and not reading an absorbable hidden
  field, that separates two morphisms with identical `nu`. This is the positive
  result the two prior reviews and this one all keep asking for, and it is the
  only thing that would flip the verdict to EARNED.

Until one of those exists, the objects are not independently motivated. They are a
correct, honest, internal scaffold around a known obstruction, with one open
question and a proof that the easy road to it is shut.
