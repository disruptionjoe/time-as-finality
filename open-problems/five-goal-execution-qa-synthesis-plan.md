# Five-Goal Execution, QA, and Synthesis Plan

## Status

Execution handoff. This is not evidence for any claim, not a claim-ledger
update, and not permission to upgrade a route by accumulation of artifacts.

## Purpose

Track the next five ambitious goals while preserving the repo's defensive
research posture:

```text
parallelize artifact production;
serialize shared claim-status changes;
run absorber and QA passes before synthesis.
```

The plan exists to keep future runs from creating isolated artifacts that are
hard to find, mutually inconsistent, or too easy to over-read.

## Global Rule

No lane may update `CLAIM-LEDGER.md`, `TESTS.md`, or route-level claim status
until its artifact has passed a lane-local QA pass and the cross-lane synthesis
pass below. Lane work should live first in models, tests, results, literature
notes, technical reports, or open-problem handoffs.

If a lane produces only a null result, that is still a success if the null
result removes a live route, sharpens a falsification criterion, or prevents a
future overclaim.

## Shared Contract Pass

Run this first, before the five lanes diverge. The output may be a short note
or a checklist reused by each lane.

Minimum shared terms:

1. `same-neighbor-data`: the exact data granted to the best neighboring theory.
2. `fixed-H`: whether Hamiltonian, coupling, pointer observable, environment
   split, and trace-rule probabilities are held fixed.
3. `fixed-source`: whether source process, issuance order, hidden variables,
   cadence, and source/readout map are held fixed.
4. `observer-access subset`: which fragments, records, or regions are
   physically accessible to the observer.
5. `provenance partition`: which records count as independent support and why.
6. `absorber vector`: work, sink, reservoir, history export, boundary,
   authority, source-copy, and control data matched across a comparison.
7. `claim outcome`: upgrade, boundary, bookkeeping, obstruction, absorber, or
   rejection.

Exit criterion:

```text
Each lane can state exactly what data are fixed, what neighbor is granted, and
what would count as a surviving split.
```

## Goal Board

| Lane | Route | Primary artifact | Parallel-safe work | Sequential dependency | Kill condition |
| --- | --- | --- | --- | --- | --- |
| G1 | Quantum measurement / classical records | Q1A/RSPS/SBS no-go-or-split theorem | finite model, theorem sketch, SBS comparison table | requires Shared Contract Pass | all candidate splits factor through fixed decoherence/QD/SBS plus trace rule |
| G2 | Experimental discriminator | Q1B real detector packet or blocker | packet schema dry run, authority map, event-row example, outreach issue draft | requires current Q1B handoff and no ledger edits during packet work | no named deployment can satisfy pre-data manifest plus reviewable rows |
| G3 | Thermodynamic arrow | H7 constructor-impossible deletion substrate screen | substrate shortlist, absorber-vector audit, finite toy controls | requires Shared Contract Pass; should read current H7 handoff | every named substrate collapses to cost, access, boundary, hidden copy, finite barrier, or idealization |
| G4 | Spacetime reconstruction | S1 scaling discriminator | causal-set statistics, deletion-stability tests, dimension-estimator comparison | requires stable metric targets before coding | finality-colimit survivors fail scaling or manifoldlikeness screens |
| G5 | Black holes / horizons / causal access | horizon causal-access boundary discriminator | boundary taxonomy, toy model, literature absorber note | should wait for G3/G4 vocabulary drafts before final wording | horizon cases reduce to access loss, ordinary boundary records, or already-known holographic reconstruction |

## Recommended Scheduling

### Phase 0: Repo Hygiene

One run only.

1. Sync the active branch or create a clean worktree from the intended base.
2. Record dirty unrelated files, but do not revert them.
3. Decide whether each lane gets its own branch or whether one branch will
   carry a single planning/integration series.
4. Freeze a rule that only the integration pass touches shared index files.

### Phase 1: Shared Contract

One sequential run.

Deliverable:

- `open-problems/shared-neighbor-data-contract.md`, or an equivalent technical
  note if that filename is not chosen.

Required result:

- A reusable checklist for `fixed-H`, `fixed-source`, `same-neighbor-data`,
  observer access, provenance, and absorber vectors.

### Phase 2: First Parallel Pair

Run G1 and G2 in parallel.

Why these first:

- G1 can kill or sharply limit the most tempting internal quantum route.
- G2 is the only live experimental route and should not wait on more internal
  toy models.

G1 output options:

- proof sketch;
- finite counterexample search;
- no-go theorem draft;
- updated RSPS/Q1A absorber note if the no-go succeeds.

G2 output options:

- minimal reviewable packet example;
- exact blocker table;
- outreach-ready issue draft for a detector group;
- null report if the governance burden is unrealistic.

### Phase 3: Second Parallel Pair

Run G3 and G4 in parallel after the shared contract exists.

Why these together:

- They stress different routes and should not block each other.
- Both require precise matching conditions and can reuse the absorber-vector
  language from Phase 1.

G3 output options:

- one named substrate audit;
- finite deletion/impossibility model;
- H7 demotion note if all named substrates collapse.

G4 output options:

- executable scaling discriminator;
- causal-set/manifoldlikeness comparison table;
- S1 demotion note if finite witnesses fail scaling.

### Phase 4: Horizon Lane

Run G5 after G3 and G4 have draft vocabularies.

Reason:

Horizon claims are easy to confuse with deletion, inaccessible records,
observer boundary, and spacetime reconstruction. G5 should reuse the sharpest
terms from G3 and G4 instead of inventing parallel language.

G5 output options:

- boundary taxonomy;
- toy causal-access discriminator;
- absorber note against standard horizon, algebraic-QFT, holographic, or
  reconstruction accounts;
- demotion rule for horizon-style H7 or B1 claims.

### Phase 5: QA and Synthesis

One sequential integration run after at least two lane artifacts exist, or
after any lane claims a positive result.

This pass decides what should enter shared repo surfaces.

## Lane QA Checklist

Every lane must answer these before integration:

1. What is the strongest claim after the artifact?
2. What existing theory or repo absorber explains the same result better?
3. What data are fixed across the comparison?
4. What would falsify or demote the lane?
5. Does the artifact create a new prediction, a theorem target, a boundary
   rule, or only bookkeeping?
6. Did the implementation regenerate its result artifacts?
7. Were relevant checks run?
8. Does the claim ledger need an update, or should the result stay local?

Minimum checks:

```text
python <changed model or runner>
python -m py_compile <changed python files>
git diff --check
```

If unit tests exist for touched modules, run those instead of only
`py_compile`.

## Cross-Lane Synthesis Checklist

The synthesis pass must produce a short report with:

1. The live status of G1-G5: active, blocked, null, demoted, or ready for
   integration.
2. The strongest surviving TaF claim after all lane outputs.
3. The strongest killed or weakened claim.
4. Any shared definitions that should become repo-wide contract language.
5. Conflicts between lanes, especially:
   - Q1A/RSPS basis-objectivity language versus horizon/objectivity language;
   - H7 deletion language versus horizon access-loss language;
   - S1 reconstruction language versus causal-access boundary language.
6. A claim-ledger update proposal, not an automatic claim-ledger edit.
7. A next-run queue ordered by expected value, not by route rotation.

## Integration Rules

Only after synthesis:

1. Update `CLAIM-LEDGER.md` if a claim status, boundary, or primary evidence
   changed.
2. Update `TESTS.md` if an executable test or model exists.
3. Add cross-links from claim pages, literature absorber notes, open-problem
   handoffs, and result artifacts.
4. Commit the integration separately from lane-local work when practical.

Do not merge lane outputs by enthusiasm. Merge only what survives QA.

## Current Recommended Queue

1. Shared neighbor-data contract.
2. G1 Q1A/RSPS/SBS no-go-or-split theorem.
3. G2 Q1B real detector packet or exact blocker.
4. G3 H7 constructor-impossible deletion substrate screen.
5. G4 S1 scaling discriminator.
6. G5 horizon causal-access boundary discriminator.
7. Cross-lane QA and synthesis report.

## Follow-up Trigger

Run the QA/synthesis pass when either condition is met:

- two lane artifacts have landed; or
- any single lane claims a positive, route-upgrading result.

If neither condition is met after five more runs, synthesize anyway and demote
or pause the lanes that produced only vague setup.
