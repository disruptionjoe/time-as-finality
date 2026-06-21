# P08 Bounded Run - Quantum-Information Operational Crosswalk

- Run timestamp: 2026-06-20T16:44:48-05:00
- Persona: P08 - Quantum Information Theorist
- Goal id: P08
- Queue goal: Define branch support, provenance, and reversal cost using quantum channels, instruments, distinguishability, entropy, recovery maps, or resource monotones.
- Bounded scope: repo-only audit of the current D1/Q1 weak-measurement and provenance branches, with no new physics claim and no claim-status changes.

## Repo Context Read

- `personas/EXPERT-PANEL.md`
- `claims/D1-physical-finality-definition.md`
- `claims/Q1-quantum-under-finalization.md`
- `claims/Q1A-access-boundary-record-accounting.md`
- `claims/Q1C-weak-measurement-discriminator-gate.md`
- `tests/T132-weak-measurement-nonnull-criterion.md`
- `tests/T90-weak-measurement-reparameterization-obstruction.md`
- `tests/T91-weak-measurement-platform-audit.md`
- `tests/T93-weak-measurement-undo-cost-independence.md`
- `explorations/persona-goal-runs/2026-06-20-154418-p07-quantum-foundations-q1-neighbor-audit.md`

## Work Performed

1. Read the current D1 physical-reduction status to separate already operational dimensions from formal-only ones.
2. Read the Q1 umbrella and Q1A/Q1C branch files to avoid upgrading dormant weak-measurement language into a live information-theoretic claim.
3. Read T132/T90/T91/T93 to identify exactly what would count as a non-null quantum-information observable rather than a relabeled standard trajectory statistic.
4. Recast the current repo vocabulary into channel/instrument language and asked which quantities are already earned, which are blocked, and what the smallest next operational object should be.

## Operational Recast

The useful quantum-information translation is not yet a full resource theory.
The smallest honest object is an audited instrument packet:

```text
(I, A, Z, B, G)
```

where:

- `I` is the measured instrument or monitored channel family;
- `A` is the observer access map that determines which outputs are visible;
- `Z` is provenance side-information that certifies copied versus independent record routes;
- `B` is a pre-registered branch witness distinguishing live instrument-history alternatives;
- `G` is a recovery / erasure task used to define reversal cost.

Under that packet, the current D1-adjacent quantities translate as follows.

| TaF quantity | Quantum-information recast | Current repo status |
| --- | --- | --- |
| accessible support | support of observer-accessible instrument outcomes after applying `A` | partially operational |
| holder redundancy | count of provenance-distinct accessible fragments or channels carrying the same recoverable record content | partially operational |
| provenance | classical side-information `Z` needed to decide whether two record carriers are independent, copied, ambiguous, or withheld | operational only as audited side-channel evidence, not semantic labeling |
| branch support | number of pairwise distinguishable live branch hypotheses consistent with the same standard monitored summaries | formal-only / blocked |
| reversal cost | minimum admissible external resource required by a recovery or erasure task `G` while standard monitored summaries are held fixed | formal-only / blocked |

## Main Findings

### 1. Provenance already has a natural channel-side role

The detector branch has effectively identified provenance as side information
about instrument implementation, not as a fifth metaphysical axis. In
quantum-information terms, `Z` is the classical witness that tells us whether
two apparent record carriers came from independent subchannels, delayed copies,
or an ambiguous shared route. Without `Z`, the repo's current honest move is to
withhold D1 rather than infer independence from outcome statistics alone.

That means provenance is presently best treated as an admissibility condition
for redundancy and branch claims, not as an extra dynamical prediction.

### 2. Holder redundancy can be expressed with standard machinery

The strongest earned translation is still the T22/T104 style one:
independence-corrected record support behaves like a provenance-aware count of
accessible fragments or channels that carry the same recoverable content.

This is close to standard information-theoretic bookkeeping. The repo does not
currently justify a stronger claim than "redundancy must be computed over
audited provenance classes rather than raw fragment count."

### 3. Branch support needs distinguishability of hidden histories, not more counting

The blocked D1 quantity is not ordinary support size. A quantum-information
version would need a pre-registered witness that two trajectories have the same
coherence/redundancy/access summaries yet leave different numbers of live,
mutually distinguishable branch hypotheses for the observer.

That is stricter than current Q1A and current weak-measurement examples. The
repo explicitly says branch support collapses in the present fixed-data family
and remains null in current monitored-platform proposals when it is reconstructed
from the same record stream.

So the relevant object is not "how many branches exist in the model?" but
"how many branch alternatives remain operationally distinguishable under
`(I, A, Z)` before post hoc labeling?"

### 4. Reversal cost must be task-based

The repo's strongest guardrail is correct: control-pulse energy, schedule
bookkeeping, or reversal-success labels are not yet admissible reversal-cost
observables. In channel language, reversal cost should be tied to a task:

- specify a target recovery or erasure goal `G`;
- specify the allowed recovery map family;
- ask for the minimum independent resource needed to complete `G` while the
  standard monitored summaries stay fixed.

Until a platform names that task and an independent meter, reversal cost is
only a formal placeholder, not an earned thermodynamic or operational monotone.

## Result

The bounded P08 conclusion is conservative:

1. The current repo already supports a clean instrument/provenance/accounting
   reading for accessible support, audited redundancy, and withhold rules.
2. It does not yet support a genuine quantum-information observable for branch
   support or reversal cost.
3. The smallest useful next object is an audited instrument packet
   `(I, A, Z, B, G)`, not a full quantum resource theory and not a new
   weak-measurement prediction.

This is enough to sharpen language:

- provenance = audited side information for independence claims;
- branch support = distinguishable live branch hypotheses, not post hoc labels;
- reversal cost = minimum resource for a named recovery task, not control effort.

## Blocker

No current repo witness supplies two trajectories with identical standard
monitored summaries and an independently measured difference in either:

- branch distinguishability under a fixed instrument/access/provenance packet; or
- task-based reversal cost under a calibrated independent meter.

Without one of those, the quantum-information recast stays bookkeeping-plus-
guardrails rather than a new operational theorem.

## Proposed Next Action

Build one finite monitored-instrument witness with explicit packet data
`(I, A, Z, B, G)` and require all of the following before any upgrade:

1. `I` fixed before analysis and shared across the comparison cases.
2. Standard summaries fixed across the cases: coherence proxy, redundancy
   summary, observer access summary, and reversal-success summary where relevant.
3. `Z` distinguishes copied versus independent record routes by measured or
   intervention-defined evidence, not semantic labels.
4. `B` changes the number of live distinguishable branch hypotheses, or `G`
   changes the minimum independent recovery resource.
5. The TaF verdict changes only because of `B` or `G`.

If no such finite witness can be specified, the honest conclusion is that the
current D1/Q1 quantum branch collapses to provenance-disciplined information
accounting over already formed records.

## Claim-Status Posture

- No claim promotion.
- D1 accessible support and holder redundancy remain the only partially
  operational quantum-facing dimensions in the current repo.
- D1 branch support and reversal cost remain formal-only in strong physical
  language.
- Q1A remains bookkeeping-only.
- Q1C remains dormant until a real platform supplies the missing packet data.
