# ISSUANCE — TAF-002 (P2C-W1 capability adjudication, v0.1)

Issued: 2026-07-16, by the Time as Finality steward (mailbox processing run).

## Steward decision

**ADJUDICATED-AND-ISSUED.** The mailbox proposal
`CapacityOS/system/mailboxes/time-as-finality/20260716-p2cw1-superconducting-ring-witness-capability-adjudication.md`
asked TaF to adjudicate the frozen P2C-W1 witness (superconducting ring, budget-matched
counterfactual pair) as a capability-change question under TaF's own invariant standards. The
steward verified the frozen bundle independently, built a TaF-native executable adjudication
fixture at TaF's own grade discipline, and issues the split verdict recorded in
`blobs/taf002_semantics.md` section 5:

- **Clause 1:** capability change AFFIRMED, frame-indexed to the declared budget-matched
  counterfactual pair, at exploration tier.
- **Clause 2:** the factor is named — record-formation/erasure structure (TAF-001 BETA side),
  with access and resource deflations executably excluded; the factoring is non-deflationary in
  TaF semantics, so the proposal's dichotomy is non-exclusive and the honest answer is BOTH.
- **Clause 3:** the fixed-family absorber is NOT adjudicable by TaF's standards (TaF's capability
  object is frame-taking by construction); exhibited executably, endorsed in neither direction;
  P2C falsifier F1 untouched.

## Bundle verification performed before adjudication

All four P2C-W1 blob sha256s and byte lengths re-hashed against `witness.json`; freezing commit
`4c9c28bbad0bdca45377dd2265b28b1fec3cc9ef` and content revision
`850521c2fc07b277734e293cd68c0928bb0cb6de` confirmed, with originating artifacts byte-identical at
the content revision; the witness discriminator re-run from the frozen blob (exit 0, stdout
byte-identical to its frozen output).

## Two-commit freeze

- Commit 1 (blob freeze, pinned as `source.revision`):
  `0749ce51c2eb542defe4010341787f1974a56a7d`
- Commit 2 (this file plus `packet.json`): the commit introducing this file.
- Digests (`ptc-frozen-bundle-v1`):
  - `manifest_digest`: `6826fc19dfbddaaab6b2226620a41b70b0a9d936efe509ebe908142ec0255487`
  - `packet_digest`: `4bf8c8efe8ad6f9bbeb9a7b7b920bd613e2bcb4439b1c040a374992c54159c72`
  - `bundle_digest` = `integrity.digest`: `0237f93b6e075968600b065b08dbd2ee334290dd428b3821eb4c57502e17ed79`
- `packet.json` validates with zero errors against
  `possibility-to-capability/tests/validate_frozen_packet_v0_2_contract.py::validate_packet`
  with this directory as `bundle_root` (run read-only at issuance).

## Boundaries

Exploration tier; `formal only` evidence grade over literature-grade stipulated physics; no TaF
claim-status, Canon-Index, ledger, or public-posture movement; `authority_transfer = false`;
no verdict on P2C's hierarchy grades or falsifier F1; no statement about Temporal Issuance's
return. Frozen means frozen: corrections issue a v0.2 directory.
