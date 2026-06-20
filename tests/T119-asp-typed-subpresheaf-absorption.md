# T119: ASP Typed Subpresheaf And Absorption Audit v0.2

## Route

Mathematical machinery / prior-art absorption audit.

## Goal

Test the narrowed `ASP_O(U)` proposal from the persona goal run:

```text
ASP_O^T(U,h) = admissible future task/section set
```

where admissibility is indexed by observer `O`, patch `U`, task family `T`,
and horizon `h`.

This is not a claim-promotion test. It tries to preserve only the strongest
version of ASP and then kill its independence if enriched prior art absorbs it.

## Candidate Object

For a finite observer-access site `C_O`:

```text
S(U) = finite local section/task set over U
ASP_O^T(U,h) subset S(U)
```

A section is in `ASP_O^T(U,h)` only if required witnesses, operation rights,
maintenance budget, reconstruction paths, certification tokens, causal access,
and viability predicates are all satisfied.

## Required Checks

1. **Typed subpresheaf closure.**

```text
if s in ASP(V) and U subset V, then s|_U in ASP(U)
```

under stable predicate typing.

2. **Negative control.**

Restriction closure should fail when predicate typing or audit monotonicity is
violated.

3. **Relabeling invariance.**

Pure observer/record/task relabeling should preserve the ASP structure.

4. **Boundary covariance.**

Access refinement/coarsening may change ASP, but it must be recorded as a
declared boundary change, not as gauge.

5. **Absorption rerun.**

Compare ASP first against coarse entropy/information/finality/viability and
coarse reachability, then against enriched reachability/opportunity/provenance
models that include witnesses, rights, certifications, maintenance budgets, and
reconstruction paths.

## Success Criteria

- The positive finite system forms a typed subpresheaf.
- The negative control breaks closure.
- Relabeling is invariant.
- Boundary changes are covariant, not invariant.
- ASP separates from coarse baselines in at least one matched finite case.
- Enriched reachability/opportunity/provenance absorbs that separation.

## Failure Criteria

- ASP is assigned post hoc rather than by predeclared task requirements.
- The task universe changes between paired systems.
- Restriction and forward transport are conflated.
- Boundary changes are mislabeled as gauge.
- The result promotes ASP as a new primitive or GU result.

## Expected Disposition

Preserve and formalize narrowly as an observer/task-indexed audit object if the
checks pass. Do not promote ASP as independent physics. If enriched prior art
absorbs the separation cleanly, record the absorption as the main result.

## Reproduction

```bash
python -m unittest tests.test_asp_typed_subpresheaf_absorption -v
python -m models.run_t119
```
