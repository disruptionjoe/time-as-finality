# P22 Run - Information Theorist

- timestamp: 2026-06-21T06:57:29-05:00
- goal_id: P22
- selected_persona: Information Theorist
- selected_goal: Replace holder-count and support-count proxies with mutual information, directed information, redundancy/synergy, coding cost, or channel-capacity bounds where the models permit it.
- bounded_question: In the current D1 and Q1A witness family, which count-like proxies can be upgraded to information measures without reintroducing overclaiming or erasing the access/provenance discipline that the repo has already earned?

## Repo Context Read

- [`/Github Repos/time-as-finality/explorations/persona-future-run-goals-2026-06-20.md`](/Github%20Repos/time-as-finality/explorations/persona-future-run-goals-2026-06-20.md)
- [`/Github Repos/time-as-finality/claims/D1-physical-finality-definition.md`](/Github%20Repos/time-as-finality/claims/D1-physical-finality-definition.md)
- [`/Github Repos/time-as-finality/claims/Q1A-access-boundary-record-accounting.md`](/Github%20Repos/time-as-finality/claims/Q1A-access-boundary-record-accounting.md)
- [`/Github Repos/time-as-finality/literature/distinguishing-predictions.md`](/Github%20Repos/time-as-finality/literature/distinguishing-predictions.md)
- [`/Github Repos/time-as-finality/tests/T22-d1-physical-reduction-map.md`](/Github%20Repos/time-as-finality/tests/T22-d1-physical-reduction-map.md)
- [`/Github Repos/time-as-finality/tests/T62-noisy-measurement-access-boundary.md`](/Github%20Repos/time-as-finality/tests/T62-noisy-measurement-access-boundary.md)
- [`/Github Repos/time-as-finality/tests/test_d1_physical_reduction_map.py`](/Github%20Repos/time-as-finality/tests/test_d1_physical_reduction_map.py)
- [`/Github Repos/time-as-finality/tests/test_q1a_provenance_absorption.py`](/Github%20Repos/time-as-finality/tests/test_q1a_provenance_absorption.py)

## Work Performed

1. Traced where the repo still uses count-like D1 proxies:
   - `accessible support`;
   - `holder redundancy`;
   - the Q1A audited accessible provenance-support count.
2. Checked what is already information-theoretic rather than merely counted.
   T22 and T62 already compute fragment mutual information and threshold it.
3. Compared those executable surfaces with the newer Q1A closure results.
   The current family now factors through partition visibility plus audited
   accessible provenance-support count.
4. Asked a narrower question than the original persona brief:

```text
Can information measures refine the current count surfaces,
or do they actually replace them?
```

## Result

### Main Finding

The repo's count proxies are already less primitive than they look.

`holder redundancy` is not currently "just count the copies." In T22/T62 it is
already:

```text
count the accessible fragment classes
whose per-fragment mutual information clears threshold
after an audited independence partition is declared
```

So the real upgrade target is not the fragment-level observable. That part is
already mutual-information based. The upgrade target is the aggregation rule.

### Current Boundary

The strongest finite example remains:

```text
E1, E2, E3 each carry 1 bit of pointer information
raw accessible redundancy = 3
provenance-aware redundancy = 2
D1 holder redundancy = 2
```

because `E3` is a correlated duplicate under the declared independence class.

This means:

- raw mutual-information totals do not replace provenance auditing;
- raw fragment counts do not replace provenance auditing;
- any honest information upgrade must preserve the access cut and provenance
  partition as first-class inputs.

### Dimension-By-Dimension Audit

| Surface | Current executable proxy | Honest information upgrade | Status |
| --- | --- | --- | --- |
| accessible support | count of accessible informative fragments after thresholding | accessible information sidecar: per-fragment `I(S;F_i)` plus thresholded accessible set, and where operationally meaningful a rate-distortion or code-length summary for observer reconstruction | worth adding as sidecar, not a replacement |
| holder redundancy | count of distinct accessible independence classes carrying above-threshold information | audited redundancy functional over fragment families: keep the class count as the decision surface, add a redundancy/synergy sidecar so duplicates and purely joint information are exposed explicitly | worth adding as sidecar, not a replacement |
| branch support | formal count-like bookkeeping only; no stable physical reduction | do not force an information measure yet; a synergy number here would be fake precision because the current fixed-data family already collapses branch-support escape routes | not earned |
| reversal cost | named cost component without a substrate-independent physical metric | only after a real undo channel is fixed: coding cost, control description length, or channel simulation cost could be audited beside it | not earned |

### Smallest Useful Formal Object

The smallest useful upgrade is not a new D1 definition. It is an audited
information sidecar attached to the current count surfaces:

```text
InfoAudit = (
  source variable S,
  audited access set A,
  audited provenance partition Pi,
  per-fragment information vector { I(S;F_i) }_(i in A),
  threshold tau,
  accessible informative set A_tau,
  provenance-aware redundancy count R(Pi, tau),
  duplicate/synergy notes,
  optional accessible coding-cost summary
)
```

Then:

- `accessible support` stays the coarse projection `|A_tau|`;
- `holder redundancy` stays the coarse projection `R(Pi, tau)`;
- the sidecar explains why the counts take those values.

This respects the current repo posture because it sharpens bookkeeping without
pretending to derive a stronger physics theorem.

### Directed Information, Capacity, And PID Guardrails

#### Directed information

Use it only when the observer access model is genuinely sequential or
feedback-bearing, for example:

- detector streams with time-ordered release;
- control/intervention channels;
- staged reconciliation protocols.

Do not import directed information into the static T22 fragment family. There
it would be notation without extra content.

#### Channel capacity

Use capacity only as an upper bound on what an access channel could support,
not as a verdict replacement. Capacity is about potential transmission; D1 is
about audited realized records under a specific witness family.

#### Redundancy/synergy decomposition

This is the most promising next refinement for `holder redundancy`, but only in
a conservative form:

- redundancy should expose when multiple holders carry the same record content;
- synergy should expose when no single holder clears threshold but a joint
  observer could recover the source;
- neither one replaces the provenance partition.

In the current family, provenance classes remain more load-bearing than any
candidate PID quantity.

### What This Does And Does Not Buy

#### Positive

The information-theoretic upgrade can make current D1 bookkeeping more honest:

- it can show why raw redundancy overcounts;
- it can separate informative duplicates from independent support;
- it can prevent support counts from looking more primitive than they are;
- it can provide coding-cost language for future access-boundary witnesses.

#### Negative

It does not currently rescue any collapsed Q1A route.

The closure results still dominate:

- once the provenance-aware partition is shared, the fixed-data witness family
  is absorbed;
- branch support does not currently add a live same-data split;
- reversal cost does not currently add a live same-data split.

So the right conclusion is:

```text
information measures refine the audited count surfaces;
they do not reopen external distinctness by themselves
```

## Blocker

The current repo does not yet contain a canonical audited redundancy/synergy
functional for fragment families. Mutual information is executable now, but the
next aggregation step is underdetermined without choosing one conservative
redundancy notion and stating its failure cases.

## Proposed Next Action

If Joe wants a follow-on run, the next bounded step should be:

1. keep D1 counts unchanged;
2. add one `InfoAudit` sidecar to the T22/T62/T104 family;
3. report, for each witness:
   - per-fragment mutual information;
   - thresholded accessible set;
   - provenance-aware redundancy count;
   - duplicate versus independent support note;
   - any purely joint-information warning.

That would test whether the extra information language improves clarity without
quietly changing the verdict rule.

## Claim-Status Posture

- No claim-status changes recommended.
- No roadmap, test-status, or automation changes recommended.
- Positive narrow statement: the repo can justify an audited information sidecar
  for `accessible support` and `holder redundancy`.
- Negative narrow statement: the repo has not yet earned an information-theoretic
  replacement for D1 counts, and should not pretend that total mutual
  information, channel capacity, or synergy alone settles finality.
