# T376 Results: Fixed-Admissibility Absorber Harness

## Current strongest claim

Fixed admissibility is a reusable absorber. Parity-style coherence,
latent-source access, and projector-style mode selection are not source-side
residue unless fixed predicate/projector/access models fail.

## Fixture verdicts

| fixture | fixed predicate | fixed latent access | fixed projector | nonfixed needed | residue |
|---|---:|---:|---:|---:|---|
| `parity_clock_free_trace` | `true` | `true` | `true` | `false` | `fixed_admissibility_absorbed` |
| `latent_access_trace` | `true` | `true` | `true` | `false` | `fixed_admissibility_absorbed` |
| `projector_zero_mode_trace` | `true` | `true` | `true` | `false` | `fixed_admissibility_absorbed` |
| `nonfixed_threshold_positive_control` | `false` | `false` | `false` | `true` | `nonfixed_admissibility_residue` |

## Plain-English reading

The harness catches the recurring false positive:

```text
records cohere or get filtered
therefore source-side finality may be active
```

The result says: not yet. If a fixed predicate, fixed projector, fixed latent
source, schema constraint, or causal-order-plus-value rule reproduces the
trace, the witness is reconstruction-layer discipline.

The positive control matters because it shows the harness is not vacuous. When
the same visible proposal flips verdict only because the admissibility law
changes, the fixed absorbers fail and the trace is labeled:

```text
nonfixed_admissibility_residue
```

## Claim ledger update

Register T376 as a guardrail harness only. It demotes witnesses that are
reproduced by fixed admissibility plus changing access and preserves only
traces requiring a genuinely nonfixed admissibility law.

## Not claimed

This result does not prove source-side finality, does not promote D1/PO1/MTI/S1,
and does not claim fixed admissibility explains all record behavior. It is a
pre-promotion absorber.
