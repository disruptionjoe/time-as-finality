# Causal Outside vs Structural Outside v0.1

## Purpose

This note prevents sloppy analogies between causal access limits and
Godel/Rice-style structural limits.

The repo currently has both kinds of "outside" in view. They must be kept
distinct until a theorem connects them.

## Two Kinds Of Outside

### Causal Outside

A witness is causally outside a system when it exists at an event, location, or
record holder that the system cannot access at the evaluation point.

T19 is primarily causal:

```text
R_self_finality witnesses exist after R's observation horizon.
```

T65 is also causal in the spatial sense:

```text
the joint information needed for a locally causal CHSH assignment is outside
Alice's and Bob's individual causal regions.
```

### Structural Outside

A fact is structurally outside a system when it cannot be expressed, proved, or
decided inside the system's own language, rules, or semantic resources.

Godel, Rice, and related self-reference results live here.

## Why The Distinction Matters

Causal outside does not automatically imply structural outside.

A record can be inaccessible now but decidable later. A fact can be structurally
inexpressible even if all relevant data are locally present. These are different
failure modes.

## Questions To Answer

1. When is a witness causally inaccessible?
2. When is a fact structurally inexpressible?
3. When can causal inaccessibility induce a Godel-like verification gap?
4. When are causal and structural outside unrelated?

## Candidate Theorem Target

```text
Causal-to-Structural Gap Theorem:

Under specified closure, self-reference, and language-completeness assumptions,
a causal record boundary induces a structural self-verification gap.
```

This is not currently proved. T19 supports only the causal-boundary side.

## Failure Modes For The Theorem

- The system can later access the missing witness, so the gap is temporal but
  not structural.
- The system can represent the proposition but lacks evidence, so the problem
  is epistemic rather than semantic.
- The system cannot represent the proposition even with all evidence, so the
  problem is structural but not caused by a causal boundary.
- Adding a meta-record inside the access region collapses the gap.

## Relation To Auditability

Auditability gaps are usually causal first:

```text
audit witness outside local access
```

They become structural only if the system lacks a way, even in principle, to
represent or certify the audit predicate from inside its own language.

## Relation To LossKernel

LossKernel can help state the distinction:

```text
causal loss kernel:
  removes reachable witness records

structural loss kernel:
  removes expressive or proof resources
```

The repo should not identify these kernels without a theorem.

## Guardrail Language

Avoid:

```text
T19 is Godel.
```

Use:

```text
T19 is a causal-boundary auditability result. A Godel-like structural theorem
would require additional assumptions about the system's internal language and
self-verification rules.
```
