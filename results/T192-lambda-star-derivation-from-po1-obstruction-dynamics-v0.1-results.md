# T192 Results: `lambda*(S)` Derivation From PO1 Obstruction Dynamics

## Outcome

`PO1-NCK-001` survives only in a narrowed form.

The finite semantic repairs from T190/T191 imply:

- PO1 does **not** by itself determine a nonzero interior `lambda*(S)`;
- PO1 does give a native definition of the obstruction-risk term
  `K(lambda,S)`.

## Main Finding

The strongest honest surviving statement is:

```text
PO1 => K(lambda,S)
```

not

```text
PO1 => lambda*(S)
```

because a nontrivial optimum also requires independent gain and cost terms
`N(lambda,S)` and `C(lambda,S)`.

## Why The Stronger Claim Fails

| Route | Result |
| --- | --- |
| Original covariant `FinSets` semantics | unavailable (T190) |
| Section-preserving covariant repair | functorial but dynamically sterile (T191) |
| PO1-only objective `-K` | optimized at boundary `lambda=0` |

So PO1 alone never produces the intended interior optimum.

## What Survives

PO1 naturally types:

```text
K(lambda,S) = lambda * |F(S)| * p_obs(S)
```

where `p_obs(S)` is the PO1 obstruction probability for extension attempts at
state `S`.

This is real residue, but it is only one component of the broader issuance
dynamics.

## Repo-Safe Reading

The safe update to the formal posture is:

```text
lambda*(S) is a mixed dynamics object.
PO1 contributes the obstruction term.
It does not yet derive the whole optimum.
```

## What This Changes

- `PO1-NCK-001` should remain candidate / narrowed.
- `T197` becomes more important, because the remaining question is now whether
  the full mixed dynamics is mostly absorbed by queueing / scheduling / MSY.
- Any future promotion of `lambda*(S)` must first type `N` and `C` under the
  repaired coherent-section semantics.
