# Technical Report: LossKernel Quotient Separation v0.1

## Claim Under Test

The LossKernel program needs more than T73's union law. The hard question is
whether the object survives a quotient by same endpoints, same ordinary
composite map, same endpoint behavior, and same naive lost-label set.

## Artifact

T99 adds an executable quotient audit. It constructs a same-naive-quotient
collision:

- `collision_path_relevant_witness`;
- `collision_path_decorative_label`.

Both cases share:

- source id;
- target id;
- ordinary composite map;
- target obstruction behavior;
- naive lost-label set `{branch_selector}`.

They differ only in the typed witness obligation carried by the loss. One lost
`branch_selector` is a source-side certificate resolving the target ambiguity.
The other is a display-only annotation.

Controls check that identical typed witnesses collapse and that endpoint
differences are not counted as quotient survival.

## Result

The label-only LossKernel fails the quotient gate. It cannot distinguish the
two collision paths even though the admissibility verdicts differ:

```text
admissible_typed_attribution
inadmissible_label_only_metadata
```

A typed witness kernel separates them, but only by adding source-anchored
witness obligations. That is an additional semantic burden, not a theorem
already supplied by T73.

## Current Strongest Claim

LossKernel can survive this finite quotient only if it is upgraded from a set
of lost labels to a source-anchored witness-obligation object. Without that,
it remains a provenance/effect-style annotation and should not be advertised as
a novel mathematical invariant.

## What This Improved

T99 makes the quotient/prior-art gate executable. It identifies the precise
payload needed for a non-tautological TF1: a lost item must name the source
witness whose presence resolves a target obstruction.

## What This Weakened Or Falsified

This falsifies label-only LossKernel as a sufficient object for TF1. The T73
union law remains useful bookkeeping, but it does not by itself separate
attribution from ordinary provenance or effect annotations.

## Falsification Condition

Reject theorem-level TF1 language if source-anchored witness obligations cannot
be canonically derived from finite morphism data, or if those obligations
collapse to ordinary provenance labels under the same quotient.

## Claim Ledger Update

TF1 should remain `open_formal_target`:

```text
T99 shows that naive label-union LossKernel fails quotient survival. A
witness-carrying version separates the fixture only by adding source-anchored
obligations, so TF1 cannot be promoted from T73 until those obligations are
derived rather than declared.
```

## Open Blocker

The witness obligations in T99 are fixture-declared. The live blocker is
canonical derivation from explicit source sections, target obstruction
certificates, and the restriction map.

## Next Work

Rebuild one T34 or T37 fixture with explicit source sections and target
obstruction certificates, then derive the T99 witness obligation mechanically
from the morphism.

## Reproduction

```bash
python -m unittest tests.test_losskernel_quotient_separation -v
python -m models.run_t99
```
