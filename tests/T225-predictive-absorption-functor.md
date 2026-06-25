# T225: Predictive Absorption Functor (orthodox face)

## Route

Mathematical machinery / absorber-map structure audit. Orthodox dual face of the
2026-06-24 breakout map: the host-selection direction of
`(residue + active AC-conditions) -> (absorbing host + canonical collapse-witness)`.

## Anchors (read for this test)

- `open-problems/typed-loss-transport-test.md` (defines the dual orthodox face)
- `tests/T220-losskernel-obligation-factorization-certificate.md`
- `tests/T221-coherent-section-functoriality-verdict.md`
- Model: `tests/test_predictive_absorption_functor.py`
- Results: `results/predictive-absorption/T225-predictive-absorption-functor-v0.1.json`

## Question

The kappa-transport test (open problem) reads the breakout map from the
heterodox side and asks for the transported obstruction *value*. T225 reads the
SAME map from the orthodox side and asks for its *domain*:

```text
Does the admissibility signature Sigma of a residue PREDICT which mature host
absorbs it, or is the host assignment recorded ad hoc after the fact?
```

If the AC-signature determines the host, the orthodox functor is predictive and
the catalogue is a theorem about the absorbers. If the host must be read off case
by case, the orthodox face fails: "everything gets absorbed" carries no
structure, only bookkeeping.

This lane is deliberately disjoint from the kappa-transport lane (T224-class). It
computes NO obstruction value anywhere; the corpus schema carries only host
labels and boolean AC-conditions. The guard
`test_distinct_from_kappa_transport` enforces this at the data-structure level.

## Setup

### The admissibility signature Sigma

For each resolved residue, Sigma is the set of independently checkable
AC-conditions that fired when the residue was set up. These are read off the
residue's resolution record, not chosen to fit the host:

```text
reads_only_nu        : the discriminating obligation factors through nu
                       (the neighbor-visible map; T220's psi.nu shape).
monotone_accum       : the state structure grows monotonically (only adds).
forward_required     : the served claim needs a covariant/forward action.
named_source_field   : the separating datum is a named source field a
                       provenance/effect/abstraction system can ingest.
solution_set_valued  : the residue object is a feasible/coherent-solution set
                       parameterised by added constraints.
search_negative      : separation sought by finite search, came back empty.
```

### Hosts in the corpus

```text
neighbor-data-collapse    : psi.nu factorization / provenance-effect-abstraction-
                            lens absorption (T108 / T127 / T220).
ordinary-category-theory  : restriction-of-solutions is contravariant; the
                            covariant solution-set map is not a functor
                            (T41 / T190 / T221).
```

### The explicit finite map

The catalogue is committed in `tests/test_predictive_absorption_functor.py`:
7 training residues + 2 held-out residues, each tagged with its fired Sigma and
(for training) its native host. `learn_rule` searches the six conditions for a
single one that perfectly separates the training hosts; that condition IS the
finite Sigma -> host map, fixed before any held-out answer is read.

## What was derived from sources

- From T220: the `reads_only_nu` condition and the
  `neighbor-data-collapse` host (the obligation factors as `psi . nu`, constant
  on every fiber of `nu`; the only escape — the hidden-source field — just
  enlarges `nu` to `nu'` and re-absorbs). T220's hidden-source escape is used as
  a held-out residue.
- From T221: the `monotone_accum` / `solution_set_valued` / `forward_required`
  conditions and the `ordinary-category-theory` host (restriction-of-solutions
  is the canonical contravariant functor; the covariant solution-set map fails
  at `Hom(1,0)=empty`). T221's covariant-`F` refutation via `e_bad` is the second
  held-out residue.
- From the open problem: the orthodox functor statement and the rule that the
  win condition is PREDICTION of the host, not post-hoc recording.

## Strongest positive result

The learned rule is a single discriminating condition:

```text
reads_only_nu  PRESENT  -> neighbor-data-collapse
reads_only_nu  ABSENT   -> ordinary-category-theory
```

It fits all 7 training residues, and on the 2 held-out residues — whose host
column was hidden during prediction — it predicts correctly both times
(`all_holdout_correct = true`, `first_separation_gate = null`). So on this
corpus the AC-signature does carry the host: residues whose discriminating
obligation reads only neighbor-visible data collapse into neighbor data;
residues whose object is a solution set under monotone constraint accumulation
are owned by ordinary category theory. The host is not random with respect to
Sigma — the orthodox map is at least locally well-typed.

## First exact obstruction / missing object

The positive result is real but its evidential weight is bounded, and the bound
is the actual finding:

1. **Binary, linearly separable, in-corpus.** There are only two hosts and they
   split on one condition. A perfect held-out score under those conditions is
   nearly forced; it demonstrates the map is *self-consistent*, not that it is
   *predictive of a surprise*.
2. **The held-out residues sit inside training signature classes.** Each holdout
   shares its exact Sigma with a training residue of the same host (T221's
   covariant refutation has the same signature as T190/T41; T220's hidden-source
   escape has the same signature as T220/T127). So the test confirms
   signature-stability under the existing two hosts; it does NOT exhibit a
   residue landing in a host *not seen for that signature*.
3. **No novel-host prediction and no refusal.** The decisive event the orthodox
   face needs — a residue with signature Sigma that REFUSES its predicted host
   (the first genuine separation gate) — does not occur here, and cannot occur
   in a two-host, perfectly-separable corpus. The functor has not yet been put in
   a position where it could be wrong in an informative way.

The missing object is therefore a **third host** (or a residue whose signature
predicts host H but is absorbed by host H' != H). Until a third absorber enters
the catalogue, the AC-signature -> host map is confirmed *consistent* but not
*non-trivially predictive*.

## Constructive next object

Add at least one residue resolved by a host OTHER than the current two, with its
Sigma recorded BEFORE its host, and re-run the held-out predictor. Concrete
candidates already in the repo's absorber set:

- **`signed-graph-parity` host** (CSP-PO1 / T39): a residue whose obstruction is
  the 2-colorability gluing parity. Predicted signature: `monotone_accum` absent
  or `solution_set_valued` absent but a new condition `parity_witness` present.
- **`Cech-H1-finite-cover` host** (T21 / T131): a residue whose obstruction is a
  finite-cover cohomology class. Predicted signature: a new `cover_glued`
  condition present.

The test harness already supports this: extend `CONDITIONS`, add the residue to
`CORPUS` with `split: "holdout"`, and `learn_rule` will either find a
multi-condition splitter (functor stays predictive across three hosts) or return
`None` (no single/simple rule separates — the host assignment is ad hoc once the
host set is non-trivial). That `None` return is the built-in falsifier.

## Verdict: conditional

The orthodox face is **conditionally predictive**: on the resolved two-host
corpus the AC-signature determines the host with a single discriminating
condition and survives a genuine held-out prediction (`verdict: host` at the
fixture level). But the corpus is binary and perfectly separable, so the result
certifies *consistency of the host assignment*, not yet *non-trivial predictive
power*. The orthodox functor is not refuted (no ad-hoc host appeared) and not
promoted (no novel-host prediction and no separation gate has been tested).

```text
host-at-fixture-level  : YES  (held-out prediction correct, 2/2)
predictive-in-the-strong-sense : NOT YET (binary, in-class holdouts; no third host)
ad-hoc / orthodox-face-fails   : NOT SHOWN (no signature refused its host)
```

## Meaning for the relevant claim

- The breakout's orthodox face earns **no promotion**: its kill-switch is a
  novel-host prediction passing on an untested residue (ideally across an
  unrelated absorber), and that has not been run. T225 builds the apparatus and
  shows it is internally well-typed.
- It removes one cheap failure mode: the host assignment is *not* visibly random
  — at least two distinct hosts are cleanly predicted by orthogonal signature
  features, so the recurrence is not pure notation on this slice.
- It does not touch kappa, sheaf-H1, MTI, or the colimit lines (those files are
  not edited). It is the host-domain counterpart to the kappa-value lane and must
  stay so.

## Next proof / computation step

1. Add a third host (signed-graph-parity or Cech-H1-finite-cover) as a held-out
   residue with Sigma fixed pre-hoc; re-run. If `learn_rule` still finds a simple
   splitter and the holdout passes, upgrade `conditional -> host`. If it returns
   `None` or the holdout misses, record the residue as the **first separation
   gate** and downgrade toward `fail`.
2. Only after >=2 unrelated absorbers are predicted (not recorded) may the
   orthodox face be cited as the "independent motivation" the 2026-06-24 paper
   audit found NOT EARNED. T225 is a precondition, not that result.

## Success Criteria

- A single AC-condition separates hosts on training residues. MET.
- The learned rule fits every training residue. MET.
- Held-out hosts predicted from Sigma alone (answer hidden) match the native
  host. MET (2/2).
- Schema carries no obstruction value (distinct from kappa-transport). MET.

## Failure Criteria

- No single/simple condition separates training hosts (`learn_rule` returns
  `None`) -> host assignment is ad hoc in-sample; orthodox face fails.
- A held-out residue's predicted host differs from its native host -> that
  residue is the first genuine separation gate; record it and demote.
- The corpus stays binary forever -> verdict cannot rise above `conditional`; the
  functor remains consistent-but-not-predictive and earns nothing.

## Known Physics Constraints

None. T225 is a finite typed-machinery audit over already-resolved residues. No
time, consciousness, quantum-interpretation, curvature, gravity, or new-object
language is used. The result is tagged `finite_witness` (COMPLEXITY-LEDGER): a
finite executable fixture over a hand-built corpus, NOT a scalable classification
theorem and NOT a hardness claim.

## Reproduction

```bash
python -m unittest tests.test_predictive_absorption_functor -v
python tests/test_predictive_absorption_functor.py   # prints corpus + writes results JSON
```
