# Fresh-Eyes Review Candidate North Star v0.4

## Status

Fresh-eye sub-agent review of:

```text
Candidate North Star v0.4.md
```

Reviewer:

```text
Descartes
```

This is not canon.
It is not a replacement draft.

## Findings

1. Mathematical alignment needs one tightening. v0.4 declares `~=_X`, but the
   sufficiency definition and fiber lemma mostly use `pi(y)` as an exact `X`
   value. If visible-state equivalence can be coarser than equality, the
   factorization should be through `X / ~=_X`, or `Cbar` must respect `~=_X`.

2. The quotient/kernel claims need the same equivalence caveat:

```text
if pi(y1) ~=_X pi(y2), then Cap(y1) ~=_K Cap(y2)
```

Also, `~=_K` must be an equivalence relation, or the audit must name the
induced equivalence used for quotienting.

3. v0.4 is not too short. The compression is successful. It keeps the locked
   posture: global absorption first, typed `Cap`, factorization/fiber
   discipline, residue honesty, and physics only after known-theory induction.

4. Status caveats are accurate but slightly over-defensive. Compress them if
   possible.

5. Physics strength improved substantially. Add one blunt local-access warning:
   strictly local observers cannot be credited with global/purifier/environment
   capability unless the access profile grants it.

6. Finite pair tests are correctly demoted.

## Final Decision

Accepted:

- equivalence/factorization cleanup;
- `~=_K` equivalence caveat;
- local-access warning;
- slight status compression.

Rejected:

- no major re-expansion of v0.4.

