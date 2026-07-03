# T436: Quantum E3 Resource-Lift Classifier

## Target Claims

Capability-boundary mode taxonomy, quantum E3 hinge, T435 admissible-menu gate.

## Setup

Use the T435 finite parity/superselection toy as the source gate:

```text
P = diag(1, -1)
A1 = symmetry-respecting operations, no reference/asymmetry resource
A2 = A1 plus a declared reference/asymmetry resource policy
```

T435 showed that `|+><+|` and `|-><-|` are identical under the A1
sector-population shadow while the noncommuting observable `X` separates them.
It also showed that the same datum becomes declared once A2 admits the reference
resource.

T436 classifies the resource-lift status:

```text
A1 relative obstruction
  -> A2 admits separator      => E0 declared relative to A2, not absolute E3
  -> A2 considered, still exact no-go by predeclared witness
                              => absolute E3 shape, synthetic control only here
```

## Success Criteria

- The T435 main phase pair is classified as A1-relative and A2-declared, not
  absolute E3.
- The classifier can report an absolute-after-resource shape on a synthetic
  predeclared exact no-go control.
- Large resource cost without exact impossibility is not counted as absolute E3.
- Missing A2 audit, post-hoc resource policies, hidden-resource oracles, A1-visible
  controls, and classical full-code controls do not pass.
- The artifact keeps the result recorded-tier and does not promote a claim.

## Failure Criteria

- The artifact treats T435 as an absolute E3/no-go theorem.
- The artifact treats the synthetic control as a real WAY theorem or quantum
  physics claim.
- The artifact revives T421 or uses sibling-repo content as support.
- The artifact moves `CLAIM-LEDGER.md`, `TESTS.md`, `ROADMAP.md`, North Star,
  canon, public posture, or cross-repo truth.
- Large resource cost or missing A2 policy can pass as absolute E3.

## Known Physics Constraints

This is a finite taxonomy guardrail only. It does not prove WAY, does not prove
quantum mechanics, and does not supply a physical conservation-law theorem. It
only prevents A1-relative symmetry obstruction from being read as absolute E3
without a separate exact no-go witness that survives the declared A2 resource
audit.

## Contribution Needed

Use this as a reporting rule for future quantum E3 attempts: state the A1 verdict,
state the A2 resource-lift verdict, and separately justify any absolute no-go
claim with an independently typed exact witness.
