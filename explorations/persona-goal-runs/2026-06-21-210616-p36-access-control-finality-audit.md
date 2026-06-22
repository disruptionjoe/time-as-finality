# P36 - Access-Control Systems Expert

## Goal

Model finality under permission inheritance, revocation, audit-log tampering,
and security-lattice access boundaries.

## Status

Done. This was a bounded exploratory run only. It does not update claims,
ROADMAP, TESTS, or CLAIM-LEDGER.

## Repo Context Read

- `Vision - North Star.md`
- `Method - Research Program Guidelines.md`
- `Lead Research Line - Time as Finality.md`
- `explorations/persona-future-run-goals-2026-06-20.md`
- `claims/Q1A-access-boundary-record-accounting.md`
- `claims/Q1B-detector-provenance-admissibility.md`
- `tests/T100-detector-authority-domain-bound.md`
- `tests/T121-real-detector-packet-schema-audit.md`
- `tests/T123-same-payload-packet-foa-witness.md`
- `tests/T161-detector-control-root-independence.md`
- `technical-reports/TECHNICAL-REPORT-future-capability-preservation-audit-v0.1.md`
- `results/physical-record-deletion-fixed-accounting-v0.1-results.md`

## Work Performed

1. Checked the first queued persona entry and selected `P36`.
2. Mapped existing repo machinery touching access boundaries, authority,
   revocation, auditability, and future operation availability.
3. Compared the access-control framing against the repo's strongest existing
   detector and admissibility artifacts.
4. Pressured the idea against mature absorbers already acknowledged in the repo:
   access-control systems, provenance systems, mechanism design, and enriched
   future-capability state.

## Result

The access-control lens is useful, but it does not currently produce a new TaF
primitive.

The strongest bounded conclusion is:

```text
finality-under-access-control = future evidence operation availability under
an authorization/provenance state, not raw record visibility alone
```

The smallest useful repo-facing object appears to be:

```text
Authorization-Admissibility State
  = nominal roles
  + permission inheritance map
  + effective authority partition
  + critical control-root map
  + revocation / key / publication state
  + audit-log integrity / provenance state
  + task-indexed future evidence operations
```

This is not a new physics-facing object. It is an enriched authorization state.

## What Survives The Audit

- `T100` already gives a lower bound on nominal authority separation.
- `T161` sharpens that to an effective authority partition after quotienting by
  shared manifest, archive, audit, publication, and revocation roots.
- `T121` and `T123` already show the key access-control fact: same raw payload
  and same immediate result can still differ in admissibility and future
  operation rights.
- `T145` cleanly separates access revocation and authority/provenance
  revocation from physical record deletion.

Taken together, these already model most of what P36 asked for, only in
detector-admissibility language rather than explicit authorization-lattice
language.

## Access-Control Translation

| P36 target | Closest current repo object | Bounded verdict |
| --- | --- | --- |
| permission inheritance | nominal authority roles before T161 quotient | useful but standard; must be checked against shared control roots |
| revocation | `revocation_status`, key state, authority/provenance revocation | already load-bearing and already non-physical |
| audit-log tampering | provenance-chain failure, archive/audit root collapse | already covered as admissibility/provenance failure |
| security-lattice boundary | observer access boundary plus effective authority partition plus allowed operations | not yet written as a lattice, but structurally present |

## Main Decision

P36 should currently be treated as **translation residue**:

- strong as a hostile review lens on Q1B and admissibility work;
- weak as evidence for a new mathematical object;
- absorbed by standard authorization/provenance/capability-state machinery once
  the hidden control-root and revocation state are admitted honestly.

The clean survivor is not "access control explains finality." The clean
survivor is narrower:

```text
coarse record equality is insufficient whenever authorization/provenance state
changes which future evidence operations remain legal, auditable, or trusted
```

## Proposed Next Action

If Joe wants to continue this line later, the next honest step is not a claim
update. It is one finite hostile formalization:

1. define an explicit authorization state with inherited grants, separation of
   duty, revocation, and audit-log integrity labels;
2. state a monotonicity/non-monotonicity question for future evidence
   operations under that state; and
3. test whether it adds anything beyond the existing `T100` + `T121` + `T123`
   + `T161` detector infrastructure.

The best fit is probably as groundwork for the later authority-boundary persona
goals, especially `P87`, rather than as a standalone new branch.

## Claim-Status Posture

- No claim status changes recommended.
- No ROADMAP or TESTS changes recommended.
- No CLAIM-LEDGER update recommended.
- Best current posture: exploratory translation over existing admissibility and
  future-operation machinery.
