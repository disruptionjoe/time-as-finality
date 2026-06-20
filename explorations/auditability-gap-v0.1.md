# Auditability Gap v0.1

## Purpose

This note reframes the T19 first-person / third-person finality result away
from consciousness-first language and toward a broader auditability principle:

```text
Internal operation can be correct while the external audit trail proving that
correctness lies outside the system.
```

Consciousness remains a motivation, not the primary claim.

## Core Pattern

T19 shows:

```text
FIRST-PERSON-FINALITY(A*(R)) = NO
THIRD-PERSON-FINALITY(G) = YES
```

The reason is not that the system lacks computation. The reason is that the
records certifying the system's own finalization are outside its accessible
region.

This is an auditability gap:

```text
operation / closure / local correctness
  !=
accessible audit trail for that correctness
```

## Why This Matters

The auditability framing is more portable than the phenomenal-bridge framing.
It applies to bounded systems whose behavior can be correct while certification
requires external logs, witnesses, reviewers, or later reconciliation.

## Comparisons

| Domain | Internal fact | External audit trail |
| --- | --- | --- |
| T19 bounded observer | R reaches closure / has self-model records | External witnesses record R_self_finality after R's horizon |
| AI agent | Agent produces a correct answer and explanation | Logs, tests, reviewers, and downstream validation outside the agent context |
| Database | Transaction appears locally committed | Replication logs, quorum certificates, or recovery records elsewhere |
| Blockchain | Node sees a valid local chain tip | Global finality depends on later consensus / checkpoint records |
| Scientific instrument | Instrument records a measurement | Calibration logs, provenance, external replication, and audit metadata |
| Court / institution | Local decision is issued | Appeals, records, chain of custody, and public docket provide auditability |

## Candidate Principle

```text
Auditability Boundary Principle:

A bounded system can satisfy an internal operation or closure predicate while
failing an internal auditability predicate when the witnesses certifying that
predicate lie outside its accessible record structure.
```

This should be treated as a theorem target, not as a settled general theorem.

## Relation To LossKernel

The auditability gap is a special case of typed loss:

```text
projection to the internal system
  forgets external audit witnesses
```

The proposed `LossKernel` for T19 should name the missing audit witnesses:

```text
LossKernel(internal_projection) includes external_self_finality_witnesses
```

If that cannot be stated cleanly, T19 may remain a separate causal-boundary
result rather than a corollary of typed forgetting.

## Guardrails

- Do not claim this solves consciousness.
- Do not claim all auditability gaps are Godelian.
- Do not blur correctness with auditability.
- Do not assume causal outside and structural outside are equivalent.

## Next Test

Construct a neutral auditability witness independent of consciousness language:

```text
bounded process P
internal success record exists inside P
external audit certificate exists outside P
P cannot access the certificate at evaluation time
third-party auditor can
```

Then test whether this witness factors through the same `LossKernel` object as
T19.
