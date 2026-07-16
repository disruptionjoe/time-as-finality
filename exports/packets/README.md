# TaF Source-Issued Packets

Status: convention v1, adopted 2026-07-16 by the TaF steward (first instance: TAF-001).

`exports/packets/` holds **source-issued frozen packets**: outbound evidence artifacts that Time
as Finality issues to other repositories. They are neither internal test results (`results/`) nor
internal reports (`technical-reports/`); their bytes must stay frozen independently of internal
iteration.

## Rules

- One directory per packet: `TAF-<nnn>-<slug>-v<major.minor>/`.
- Contents: `packet.json` (metadata conforming to the receiving repository's frozen-packet
  contract), `blobs/` (the raw frozen artifacts: computations, captured outputs, the packet
  semantics body, and frozen copies of the TaF source documents the packet's premises cite), a
  `.gitattributes` marking everything `-text`, and an `ISSUANCE.md` recording the steward decision.
- **Frozen means frozen.** After issuance, nothing inside a packet directory is edited, ever.
  Corrections issue a new packet version directory; the old one stays.
- Two-commit issuance: commit 1 freezes the blob contents; `packet.json` then pins
  `source.revision` to commit 1's SHA and carries digests over the frozen bytes; commit 2 adds
  `packet.json` and `ISSUANCE.md`.
- Issuing a packet never changes a TaF claim status, and a receiver's conclusions built on a
  packet never flow back into TaF claims (`authority_transfer = false`).
- Issuance is a steward act on a mailbox proposal or internal decision; the adopting steward
  validates content against TaF's own formalism and evidence standards before issuing, and may
  reject or return NOT-YET-ISSUABLE.
