# T376: Fixed-Admissibility Absorber Harness

## Target Claims

D1, PO1, MTI, S1, and any future record-coherence or source-side finality
witness that risks confusing fixed compatibility with nonfixed admissibility.

## Setup

Build a finite harness that compares a candidate accept/reject trace against
five fixed absorber families:

```text
fixed compatibility predicate
fixed projector / fixed-H state space
fixed latent source plus changing observer access
ordinary schema constraint checking
causal order plus a declared value predicate
```

## Success Criteria

- Absorb a temporal-issuance-style parity trace.
- Absorb a fixed latent-source/changing-access trace.
- Absorb a fixed-projector/zero-mode selection trace.
- Refuse to absorb a positive control whose accept/reject behavior requires a
  genuinely changing admissibility threshold.
- Emit explicit residue labels.

## Failure Criteria

- The harness promotes fixed predicate behavior as source-side residue.
- The harness absorbs the nonfixed positive control.
- The harness lacks a plain demotion boundary.

## Known Physics Constraints

No physics claim is made. This is an absorber guardrail for finite witness
discipline.

## Contribution Needed

Extend the harness to future TaF witnesses before claim promotion. A witness
that fails this absorber can be considered for stronger domain-native tests; a
witness absorbed here should be demoted to reconstruction-layer discipline.
