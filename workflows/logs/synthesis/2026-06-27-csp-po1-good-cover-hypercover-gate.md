---
document_type: synthesis_protocol
queue_item: 4
status: complete
authority: non_authoritative
write_scope: workflows/logs/synthesis
claim_effect: none
---

# CSP-PO1 Continuum Good-Cover/Hypercover Gate

## Scope

This note completes queue item 4 from
`workflows/logs/best-next-move/2026-06-27-next-10-research-orchestration.md`.
It is a bounded gate for the one continuum hypothesis left open by T241. It does
not update `CLAIM-LEDGER.md`, `ROADMAP.md`, tests, results, code, or
open-problem files.

## Grounding Readout

Read surfaces used:

- `ROADMAP.md` T226/T231/T236/T241 entries: finite coefficient-aware H1 was
  built, refinement stability and finite cofinality were extended, `lim^1` was
  cleared at the tower level, and the remaining condition was named as
  good-cover/hypercover cofinality for the continuum derived-sheaf
  identification.
- `CLAIM-LEDGER.md` CSP-PO1 and H1-Sheaf rows: CSP-PO1 has finite-witness support
  and a conditional continuum row; H1-Sheaf is a partially supported finite
  byproduct, not a general continuum theorem.
- `open-problems/finite-to-smooth-shadow-bridge.md`: any bridge must type source
  and target independently, declare the preserved object, quotient-test
  redundancies, and include positive plus hostile controls.
- `open-problems/spacetime-as-finality-colimit.md`: smooth or spacetime language
  is guardrail context only. This gate does not derive spacetime, geometry,
  locality, or manifoldlikeness.

## Strictly Larger Hypothesis Left Open

T241 licenses a tower-level Cech comparison, not the continuum derived-sheaf
identification. The remaining hypothesis is:

```text
GHC: Good-cover/hypercover cofinality for the continuum orientation-sheaf object.
```

Expanded, `GHC` requires all of the following before
`continuum_derived_iso` may move off `None`:

1. A typed continuum target `X` and coefficient object `F` are declared
   independently of the finite witnesses.
2. A cover or hypercover category `Cov_good(X, F)` is declared, with covers whose
   finite intersections are contractible or at least `F`-acyclic.
3. The finite annular/triangulated systems from T226/T231/T236/T241 either form a
   cofinal subsystem of `Cov_good(X, F)` or are embedded into a larger cofinal
   good-cover/hypercover subsystem.
4. Refinement maps preserve the AC5 transition cochain and induce compatible
   cochain pullbacks.
5. A cited or proved comparison theorem identifies the Cech colimit over that
   cofinal good-cover/hypercover system with derived functor sheaf cohomology.

A countable annular tower alone does not satisfy `GHC`.

## Finite Checks Versus Continuum Claim

| Layer | What can be certified now | What remains unlicensed |
| --- | --- | --- |
| T226 finite cover | Coefficient-aware finite Z2 H1 detects the Mobius obstruction and exposes AC5-forgetting. | General continuum sheaf cohomology. |
| T231 refinement chain | Class survives uniform annular bisection. | Arbitrary cover or hypercover cofinality. |
| T236 finite poset | Staggered finite refinements and rank-2 finite cycle-space controls are stable. | Derived-functor comparison over a continuum target. |
| T241 tower | H0 inverse system is ML at the tower level; `tower_cech_iso=True`; genuine triple covers retire the thin-cover objection. | `continuum_derived_iso=True`; this still needs `GHC`. |

The gate rule is simple: finite/tower checks may set tower-level flags, but they
may not set the continuum derived-sheaf flag.

## Gate Protocol

1. Declare the target before examples.
   - Name `X` as the continuum band or structured target under test.
   - Name `F` as the coefficient/orientation sheaf or local system.
   - Name the preserved object: the AC5 transition cochain and the resulting
     H1 obstruction class.

2. Declare the cover/hypercover site.
   - Define the cover objects, refinement order, and allowed hypercovers.
   - State the acyclicity condition for intersections.
   - State whether the finite annular/triangulated covers are themselves in the
     site or only map into a larger good-cover subsystem.

3. Prove or cite cofinality.
   - For every admissible open cover `U`, supply a good cover or hypercover `V`
     in the declared subsystem with `V` refining `U`.
   - If this cannot be proved, the verdict stays `finite_tower_only`.
   - A fixed countable annular bisection chain is not accepted as cofinal in all
     open covers without a separate theorem.

4. Prove or cite the comparison theorem.
   - State the theorem that Cech over the cofinal good-cover/hypercover system
     computes derived sheaf cohomology for `F`.
   - Record its hypotheses and check them against `X`, `F`, and the cover site.
   - If the theorem needs paracompactness, numerability, local acyclicity, or
     hypercover descent, those assumptions must be named.

5. Run finite controls as guards, not as promotion.
   - Reuse the T226/T231/T236/T241 finite controls to check the finite machinery.
   - Add hostile cover controls below to refute overbroad versions.
   - Keep `continuum_derived_iso=None` unless steps 3 and 4 are satisfied.

## Controls

Positive finite-cover control:

- Triangulated cylinder/Mobius covers with genuine triples, as in T241. Required
  finite behavior: cylinder has a global section, Mobius is obstructed, the
  cocycle condition is non-vacuous, and the verdict is refinement-stable.

Hostile controls:

- Coefficient-blind control: drop AC5 transition data. Required behavior: the
  Mobius obstruction can collapse to a false section, reproducing the T226 trap.
- Bad-cocycle control: introduce an unbalanced triple. Required behavior:
  `is_cocycle` fails; no H1 class is admitted.
- Loop-sign shortcut control: split a twist so the loop-sign heuristic is fooled.
  Required behavior: full coboundary cohomology, not loop sign alone, determines
  the class.
- Non-good-cover control: use a cover with a non-acyclic or disconnected
  intersection where the good-cover theorem's hypotheses fail. Required behavior:
  the continuum comparison is rejected even if a finite nerve can be computed.
- Non-cofinal-tower control: exhibit or require an open cover not refined by the
  fixed annular tower. Required behavior: a tower-only result cannot be promoted
  to all open covers.

## Verdict Taxonomy

- `finite_tower_only`: T226/T231/T236/T241-style controls pass, but `GHC` is not
  proved or cited. This is the current safe position.
- `good_cover_gate_passed`: cofinality plus the comparison theorem are both
  supplied under named hypotheses. This still authorizes only a conditional
  continuum certificate proposal, not a ledger promotion by this artifact.
- `hostile_cover_failed`: a non-good or non-cofinal control breaks the overbroad
  continuum reading.
- `inconclusive_missing_site`: `X` or `F` is too underspecified to state a
  good-cover/hypercover site.

## Acceptance-Criteria Satisfaction

- The strictly larger hypothesis left open by T241 is named as `GHC`, with its
  cofinality, acyclicity, transition-preservation, and comparison-theorem pieces.
- Finite tower-level checks are separated from continuum sheaf-cohomology claims
  in the table and gate rule.
- The positive finite-cover control is the T241 triangulated cylinder/Mobius
  witness; hostile controls include coefficient-blind, bad-cocycle, loop-sign,
  non-good-cover, and non-cofinal-tower cases.
- H1-Sheaf and CSP-PO1 remain at finite-witness/conditional tier unless a later
  authoritative pass changes them.

## No-Promotion Guardrails

- Do not set `continuum_derived_iso=True` from finite witnesses alone.
- Do not call CSP-PO1 a continuum theorem, closed theorem, or
  continuum `proto_independent` result from this gate.
- Do not promote H1-Sheaf beyond partially supported finite byproduct language.
- Do not import S1, spacetime, manifold, curvature, locality, gravity, physics, or
  geometry claims into this gate.
- Do not conflate this coefficient-sheaf continuum lane with the D1Filtered
  category-colimit lane.
- Do not edit `CLAIM-LEDGER.md`, `ROADMAP.md`, code, tests, results, or
  open-problem files from this synthesis note.
