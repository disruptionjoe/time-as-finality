<!--
TEMPLATE — save the completed durable note in this repository as
    attention/YYYYMMDD-canon-promotion-<slug>.md
Then place a pointer-only envelope naming that source path in
    ../../../repos/private/system-runtime/mailboxes/system-attention/
Awareness note for an ALREADY-EXECUTED hard promotion in time-as-finality
(a claim raised into the `theorem_backed` tier of the Canon Index, or otherwise
asserted as proven/resolved — the move an outside reader would take as
"this repo says this is definitely true").
This is NOT a request for approval. See CLAIM-LEDGER.md (Canon Index) and
CONTRIBUTING.md (Promotion gates). Delete these comment lines when filling it in.
-->

# Canon Promotion Notice: <claim id> — <short title>

- **Kind:** awareness notice — promotion already executed, not a request for approval
- **Source repo:** time-as-finality
- **Promoted by:** <agent / run id>
- **Date:** <YYYY-MM-DD>
- **Commit:** <hash>

## What was promoted
- Claim: `<ID>` — <one-line statement>
- Tier / status change: `<prior tier/status>` -> `theorem_backed` (or: asserted
  proven/resolved) in the Canon Index / `CLAIM-LEDGER.md`
- External-publication touched? <NO — in-repo tier only. Nothing entered
  `papers/published/`; external publication still pauses for Joe.>

## The case FOR
How the claim cleared the Promotion gates: the runnable artifact that earned it
(test/theorem/separation), why the result is general rather than finite-witness,
and what retired the "it's just bookkeeping / absorbed by a neighbor" objection.

## The case AGAINST (steelmanned)
The strongest honest objection: what the claim does NOT assert, what would
falsify or weaken it, the weakest load-bearing dependency (assumption, single
witness, absorber not yet run), and the reviewer who could reasonably push back.

## How the call was made
Why FOR outweighed AGAINST — what tipped the decision, and what was checked to
retire the strongest objection rather than wave it away.

## Risks
What downstream depends on this being right (other claims, essay/North Star
framing, papers, the Canon Index); what breaks or misleads if it later proves
wrong; blast radius.

## Support
Certificates (paths + result, e.g. "exit 0", "N/N PASS"), proofs, fixtures, and
independent rechecks that back the promotion. Note any absorber that was run to
clear it.

## Reversal
How to undo cleanly: revert commit <hash>, demote the Canon Index / `CLAIM-LEDGER.md`
row to <prior tier/status>, and note any downstream wording that must be re-aligned.

<!-- System Attention indexes the owner-source pointer as unread. Runtime may archive the
pointer envelope only after the pointer appears in the Attention awareness index. -->
