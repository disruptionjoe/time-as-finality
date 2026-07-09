# Plan: orchestrating starter swings across the twenty profound possibilities

Exploration-grade, 2026-07-08. Companion to
`explorations/nested-band-twenty-persona-profound-possibilities-2026-07-08.md`. How to test the twenty
possibilities for viability without wasting effort, and what "viable" has to mean given the last round's
lesson.

## Two lessons that shape the plan

1. **Cross-modal adjudication is mandatory.** Last round a full persona panel crowned no-signaling; a
   computation dethroned it. Same-modality checking (more personas) would not have caught it. So **every
   swing must terminate in an executable check or a specific in-repo model result**, not more prose. A swing
   that only argues is not done.
2. **Cluster before swinging.** The twenty are not twenty independent bets; many are one bet in different
   clothes. Testing twenty separately would waste budget and double-count. Swing the six clusters, not the
   twenty items. (Silent-cap honesty: clustering *drops* distinctions between items in a cluster; if a
   cluster passes, the second stage must recover which specific item carried it.)

## Phase 0 -- dedup to six clusters (done, inline, free)

| Cluster | Items | Core bet (one predicate to test) |
|---|---|---|
| A Access structure | 18, 19, 17, 1, 6, 10-cert | Finality = the access structure; order parameter = minimal recovering-coalition size, monotone and reproducing the nested-band table. |
| B Copy law | 8, 5, 14 | The band = the no-cloning region; a conserved/priced copy quantity flows joint->redundant. |
| C Inner-label discriminator | 10-selftest, 4, 3, 7 | Something sharper than CHSH separates inner (entangled) from outer (encrypted) band -- and it must *come apart* from CHSH on some fixture, else it is a relabel. |
| D Time / arrow / spacetime | 9, 16, 11 | The recovery statistic is time-asymmetric under pre/post swap (an arrow) and/or has a light-cone/causal structure. |
| E Graded interior / rate | 20, 12, 13 | The band interior is a genuine continuum (leakage rate / cost / basin), monotone from band to global -- supplying the graded interior the pullback demanded. |
| F Relativity of the band | 2, 6, 15 | The band moves predictably as the admissible-op algebra varies; the upper edge coincides with onset of commutativity of local recoveries. |

## Phase 1 -- one probe per cluster (parallel fan-out, 6 agents)

Each probe returns the standard swing packet `{verdict: viable|conditional|dead, strongest_reason,
sharpest_killshot, smallest_next_experiment, repo_evidence}` and **must** either run code or cite a specific
model/result. Designed kill-shots (the adversarial check each must survive):

- **A** -- dead if "minimal recovering coalition" is non-monotone or ambiguous across
  entanglement/encryption/redundancy (the exact trap that killed P5's quorum). Must be monotone AND
  reproduce the nested-band table. Reuse: `kappa_quorum_intersection_transport.py` (T239),
  `consensus_finality_crosswalk.py` (T17), `finality_band_recovery_edges.py`.
- **B** -- dead if "no-cloning" is just a restatement of the LOCC monotone (already absorbed, H7/N11-N14)
  with no new prediction. Must yield a conserved/priced quantity that the record-vs-redundancy accounting
  does not already give for free.
- **C** -- dead if every candidate discriminator (self-testing, monogamy, hardness, H^0-vs-H^1) coincides
  exactly with CHSH>2 on all fixtures (then it is a relabel). Viable only if one comes apart from CHSH in a
  physically correct way. Reuse: `t58_bell_h1_real_valued.py`, `bell_contextuality_finality.py`,
  `ab_contextuality_kappa_absorber.py`.
- **D** -- high prior of death: the H7 lineage (T80/T110/T122/T148) keeps absorbing arrows. Dead if the
  recovery statistic is time-symmetric under a pre/post-selection swap. Viable only if a finite fixture
  shows a genuine asymmetry not reducible to standard entropy accounting.
- **E** -- dead if the "rate" collapses to the same binary as readability (no genuine continuum) or is
  non-monotone band->global. Must interpolate. Reuse: `finality_records_vs_redundancy_discriminator.py`.
- **F** -- dead if commutativity-onset does not coincide with the upper edge, or varying the algebra does
  not move the band predictably. Reuse: `finality_band_recovery_edges.py` (vary the admissible algebra).

## Phase 2 -- build-and-run for survivors (pipeline, no barrier)

Any cluster that clears Phase 1 flows straight into a build stage (like the P4 model): a minimal
self-checking model that either confirms the bet numerically (exit 0, PASS checks) or kills it. Pipeline,
not parallel-with-barrier, so a cluster that clears Phase 1 starts building immediately while slower
clusters are still probing. Phase 2 output for a survivor is a committed model + writeup.

## Phase 3 -- synthesis (inline, me)

Rank survivors, correct the note (as with P4's overturn of no-signaling), and, for any cluster that passed
as a group, name which specific item(s) carried it (undo the Phase-0 clustering).

## Recommended sequence (cheap x deep first)

1. **A (access structure)** and **C (inner-label)** first -- both cheap, both plug into existing machinery
   (T239, T17; T58/T131). A is the leading candidate; C directly tests whether CHSH should be replaced.
2. **E (graded interior)** next -- it fixes a *known* gap (the pullback's demand for a continuum), so a pass
   has immediate structural value.
3. **B (copy law)** -- elegant but high absorption risk.
4. **D (arrow/spacetime)** -- do NOT run as a cheap swing. It is the most on-mission (time as finality) and
   the most likely to be absorbed; it deserves its own careful campaign, budgeted separately, not a
   30-second probe.
5. **F (relativity of band)** -- run opportunistically; partly answered already (the band already depends on
   the algebra in `finality_band_recovery_edges.py`).

## Orchestration mechanics

- Phase 1 = a single `parallel()` fan-out of 6 probe agents (one per cluster), schema-structured, each
  required to run code or cite a model.
- Phase 1->2 = a `pipeline()` so survivors build without waiting on the barrier.
- Budget guard: 6 probes is cheap. Only escalate to Phase 2 builds for clusters that clear Phase 1, so
  build cost is spent only on survivors.
- Every terminal artifact (model + writeup) is committed to this repo; dead clusters are recorded as dead
  (with the kill-shot that killed them), not silently dropped.
