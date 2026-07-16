# TAF-001 Issuance Record

- **Decision:** ADOPTED-AND-ISSUED by the Time as Finality steward, 2026-07-16.
- **Origin:** mailbox proposal `system/mailboxes/time-as-finality/20260716-taf001-paired-intervention-packet-draft-for-issuance.md`
  (archived with processing receipt), pointing at the firewalled lane-B draft
  `possibility-to-capability/explorations/2026-07-16-northstar-unblock/lane-B-taf-source-packet.md`
  and its governing adversarial referee report (verdict SOUND-WITH-CORRECTIONS, firewall INDEPENDENT).
- **Content revision (commit 1, pinned as `source.revision`):** `e0414d6497e8344df811ce594648649ee1480ba4`
- **Semantics source revision (FORMALISM.md, T46 frozen from):** `8df3cf138855571538768d57e94ca36320f3830b`
- **Digests (ptc-frozen-bundle-v1):**
  - `manifest_digest`: `b9a06ac273acd4fe3294267572a480eab45c8b096b7dac2da108f07b751e9d1f`
  - `packet_digest`: `baf974fc92875774511428935327beec3ea8b4288d594a1f2e75c290a5562f9a`
  - `bundle_digest` (= `integrity.digest`): `0b0085419670a619c9574cd2accf1c4347e68ab6f249762372d8626bd8256a94`
- **Schema:** validated against the receiver's `frozen-packet-v0.2.schema.json` semantics via
  `possibility-to-capability/tests/validate_frozen_packet_v0_2_contract.py::validate_packet`
  with this bundle as `bundle_root`: zero errors.

## Steward verification performed before adoption

1. Blob identity: `taf001_paired_intervention.py` SHA-256
   `e945cd89fc59e4ab644ec49d4513742ca17911edf760d239eabaebb2e1c8b34c` (8181 bytes) and
   `taf001_output.txt` SHA-256
   `c3ada0d8367f76638f1ffba7889a748bd355b8fcd4c67262236b08a496f060d0` (2038 bytes) confirmed
   against the draft's claims.
2. Reproduction: computation re-run (Python 3, stdlib only), exit 0, output byte-identical.
3. Referee probes independently re-implemented and confirmed: P1 (a formation-only edit under
   fixed access reproduces ALPHA's delta), P1b (exhaustive sweep of all 16 access subsets of
   {h1,h2,h3,h4}: none reproduces BETA's vector), P2 (the embedded invariance assert is
   tautological).
4. Semantics audited against TaF's own `FORMALISM.md` (record token tuple, availability
   conditions 1-2, reconstruction rule, D1 profile and componentwise preorder, reconciler level,
   T22 "formal only" vocabulary) and `tests/T46-...md` (vocabulary-only use).
5. Referee corrections applied in the frozen semantics body: D1 (invariance guard demoted to
   by-construction property), D2 (fact 3 one-directional; R-1 rescoped), D5 (FORMALISM citation
   narrowed), Section 9 grade note. D3 discharged by this steward issuance; D4 discharged by the
   complete validating `packet.json`.

## What issuance commits TaF to

Only the machine-checked computed facts in `blobs/taf001_semantics.md` Section 7, at exploration
tier, formal-only grade, on designed finite witnesses. No TaF claim status changes (R1, A1, PO1,
CS1, D1, T46 verdicts untouched). No receiver-side classification is endorsed
(`authority_transfer = false`).
