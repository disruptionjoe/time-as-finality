---
document_type: persona_panel_cluster_output
cluster: C-distributed-consensus
primary_reader: agents
read_pattern: current_state
write_pattern: append_only
authority: exploratory
created: 2026-07-02
status: exploratory
personas: [9, 34, 35, 36, 55, 56]
note: Persona output is METHOD, NOT EVIDENCE. Convergence here is one process wearing masks (single-process ceiling). No claim moves; no ledger/TESTS edit.
---

# Cluster C — Distributed Systems / Consensus

Personas: 9 Distributed Systems Researcher · 34 Git Version Control Expert ·
35 Database Systems Architect · 36 Access-Control Systems Expert ·
55 Hashgraph / Gossip-Provenance Researcher · 56 Avalanche-Class Consensus Researcher.

Cluster edge: finality, reachability, "who can DO what." Native turf. All physics
attributions flagged from-memory-unverified. Terse fields per brief structure.

---

## 9. Distributed Systems Researcher

### U1 — meaning of "physical rather than declared"

- **Steelman.** A boundary is physical iff it is a *safety property forced by an
  impossibility bound*, not a *configuration constant*. In consensus this is
  exact: FLP says no deterministic protocol achieves agreement under one crash
  in an asynchronous network — the impossibility is forced by the model's timing
  assumptions, not declared. Map: R→R+ is physical iff *no R-supported protocol
  whatsoever* (all interventions, unbounded work) can complete the task, and
  that failure is a theorem about the interaction structure, not a stipulated
  trace. "Declared bookkeeping" = a liveness knob (partition config). "Physical"
  = a safety impossibility over the model's own dynamics.
- **Supporting argument.** FLP/CAP are the cleanest existing examples of a
  boundary that is provably not relabelable: you cannot buy your way across with
  more messages or more time under async. That is exactly the "work cannot buy
  reach" shape the program wants, and it is a *derived* wall.
- **Hidden assumptions.** That the finite closed model HAS a partition-like
  asynchrony parameter to make the impossibility bite; that "all R-supported
  protocols" is a closed quantifier the model can actually range over.
- **Vindication.** A finite fixture where the R→R+ separation is a corollary of
  an FLP/CAP-style impossibility over the interaction graph — reach-failure as
  theorem, not partial trace.
- **Kill.** Show any single R-supported protocol that completes the task after
  finite retries → boundary was a liveness knob (wait-longer), not safety.
- **Confidence.** 5.

**Hegelian.**
- Thesis: physical = impossibility-forced safety bound (FLP/CAP-shaped).
- Antithesis (finite-closed-model objection): FLP's teeth come from *unbounded
  asynchrony* — an infinite/open timing model. A finite closed model has a
  bounded state space; every "impossibility" over it is decidable and, being
  decidable, reduces to a property of a stipulated partition of co-present state.
  Joint-record completion is the finite shadow of "CAP with the partition
  healed": once you admit both records are physically co-present (retained tier-1
  at I=1.97 bits), there is no partition, so no CAP wall — only a declared cut.
  FLP does not survive finitization into a closed model.
- Synthesis (SHRINKS): survives only as a *requirement on the model*, not a
  repair. The physical-boundary criterion is well-posed ONLY if the model carries
  a genuine asynchrony/partition parameter that is not healable by admitting
  co-present state. In every fixture to date the partition WAS healable (retained
  carriers co-present) → wall was declared. Net: FLP tells you what property the
  model must have; it does not certify any fixture built so far. Non-empty but
  thin.

### U2 — transport rung

- **Steelman.** The transport rung is the right move because it imports a real
  asynchronous-network bound: if records propagate by actual dynamics on an
  interaction graph with finite couplings and a time budget T, then reach(T) is
  the causal-influence set — a *derived* horizon. Joint-record completion is
  blocked by construction: departed records are not co-present within T, so R
  cannot be a declared subset of anything reachable.
- **Supporting argument.** CAP: under a partition you provably cannot have both
  consistency and availability. A time budget that cannot reach the departed
  register IS a partition the agent cannot heal → the separator is forced.
- **Hidden assumptions.** That "departed within T" is not just "co-present but I
  declined to trace it in." That the graph's reach is temperature/dynamics-forced
  and not re-openable by waiting.
- **Vindication.** Fixture where reach(T) is a graph-theoretic causal set and the
  separator lives strictly outside reach(T) for a T that is itself pinned by an
  energy/work budget — not a free parameter.
- **Kill.** joint-record completion (below) or wait-longer.
- **Confidence.** 4.

**Hegelian.**
- Thesis: transport rung escapes joint-record completion via a dynamics-derived
  partition.
- Antithesis (MUST face joint-record completion): "reachable within timeout =
  co-present" is precisely the rename joint-record completion feeds on. A finite
  budget T does not make the departed register non-existent — it makes it
  *currently unreached*. The record is still physically co-present in the global
  state; the agent simply hasn't gossiped with it yet. Once you admit the global
  state (which the ALL-interventions quantifier's environment-side channel lemma
  effectively does), the departed carrier is a declared subset of co-present
  state again. CAP's partition is a *network* fact; here the "partition" is an
  agent's budget — a resource threshold, i.e. wait-longer wearing a CAP mask.
  This is the THIRD design to hit this wall.
- Synthesis (near-EMPTY): the rung escapes joint-record completion ONLY if
  "departure" is irreversible co-presence-destruction (the record is not merely
  unreached but *gone from the global state within T and not recoverable at any
  R++*). If departure is partial-trace-into-a-still-co-present-reservoir, it is
  the declared subset again. Distributed-systems lens cannot supply that
  irreversibility — CAP/FLP give unreachability, not non-existence. Verdict:
  REDESIGN, not GO. The rung must carry a global-state-destruction argument the
  network bound cannot provide.

### U3 — literature adjacency

- **Steelman.** Recovery-after-departure IS the distributed-systems reorg/finality
  problem. Probabilistic finality (confirmation depth k) is the native language:
  a record is "final" not when declared but when the cost to reverse exceeds a
  threshold. Borrow: k-deep confirmation, long-range-attack bounds, and
  data-availability sampling — all quantify "recoverable vs gone" as a resource
  threshold on adversary power.
- **Supporting argument.** DA sampling: a client can verify data is recoverable by
  sampling erasure-coded chunks; below a threshold of withheld shares recovery is
  possible, above it provably not. That is a clean threshold-crossing recovery
  theorem to borrow for U3's "when and at what cost."
- **Hidden assumptions.** That the fixture's recovery has an erasure-code /
  threshold structure at all (it may be all-or-nothing per the φ-independence
  certificate). Threshold theorems need redundancy; a single departed carrier has
  none.
- **Vindication.** Fixture where restoration-at-R++ obeys a threshold-recovery law
  (recover iff ≥ t shares reachable) matching DA-sampling math.
- **Kill.** Recovery is exactly all-or-nothing (φ-independence against all
  channels) with no threshold structure → DA/erasure math does not apply; it's a
  binary reachability fact, closer to a horizon than a reorg.
- **Confidence.** 4. GU firewall resonance noted, NOT support.

**Hegelian.**
- Thesis: borrow probabilistic-finality / DA-sampling threshold recovery.
- Antithesis: the fixture's separator is a *global correlation in no proper subset*
  and recovery is φ-independence-certified all-or-nothing. Threshold/erasure
  theorems assume recovery degrades gracefully with reachable fraction; here the
  worst proper-subset marginal diff is 0.0 until the whole set is present. There
  is no partial-recovery gradient to threshold. Blockchain finality is
  *monotone in depth*; this is *discontinuous at the whole*. Adjacency is
  cosmetic.
- Synthesis (SHRINKS): the honest adjacency is NOT blockchain finality but the
  *long-range-attack / weak-subjectivity* corner — where safety cannot be
  recovered from the protocol alone and needs an external checkpoint (a "trusted
  co-present anchor"). That maps to "you need R++ / an out-of-band anchor to
  restore." Useful framing, no borrowable theorem. Horizon literature (U3's other
  pole) is the better home; distributed-systems contributes vocabulary only.

### U4 — fallback

- **Steelman.** If the boundary is bookkeeping all the way down, the surviving
  asset is a *safety/liveness certificate toolkit*: the machinery that certifies
  "no R-supported protocol completes task X" independent of whether the cut is
  physical. That is a genuine consensus-style contribution — a reusable
  impossibility-certificate calibrated on a family.
- **Supporting argument.** Consensus made its name on impossibility *certificates*
  (FLP, CAP, lower bounds), not on any single physical partition. The value is the
  certificate, portable across models. T409's re-scoped "calibration of the
  certificate toolkit" is exactly this and it SURVIVED.
- **Hidden assumptions.** That a certificate whose premise (the cut) is declared is
  still worth publishing. It is — as conditional machinery.
- **Vindication.** Toolkit certifies reach-impossibility on ≥2 unrelated model
  families with the same certificate schema.
- **Kill.** The certificate reduces to standard data-processing/DPI + partial
  trace with no consensus-specific content → nothing new to license.
- **Confidence.** 6.

**Hegelian.**
- Thesis: fallback = portable impossibility-certificate toolkit.
- Antithesis: the decoherence-bookkeeping absorber already showed every
  load-bearing object is textbook DPI + thermodynamic accounting; a "certificate"
  over that is a relabel of DPI, not a new safety theorem.
- Synthesis (SURVIVES, modest): the certificate toolkit is a real, honest
  fallback *as calibration machinery* (candidate i in U4), matching T409's
  surviving standing. It is NOT a physical-boundary result. Worth a paper only as
  methods/toolkit, not as a no-go. Non-empty.

---

## 34. Git Version Control Expert

### U1 — meaning of "physical rather than declared"

- **Steelman.** Git already distinguishes two boundary kinds and it is the right
  distinction. Reachability (`git log`, ancestry) is a *derived* fact about the
  DAG: commit X is reachable from ref Y or it is not — the object graph forces it.
  A ref/branch/`.gitignore` is *declared* bookkeeping. "Physical boundary" =
  graph-reachability (an object either is or isn't an ancestor); "declared" = a
  ref pointer you can move. A garbage-collected/pruned object is *gone*
  (unreachable AND unrecoverable once packed away) — that is the only physical
  finality git has.
- **Supporting argument.** The distinction is operationally sharp and testable:
  `git cat-file` succeeds or fails. Reachability is not a policy; it is the hash
  DAG. That is a working model of forced-vs-declared.
- **Hidden assumptions.** That "unreachable" implies "gone." In git it does NOT
  until gc — dangling objects persist and are recoverable from reflog. That gap
  is the whole U1 problem in miniature.
- **Vindication.** A fixture where the boundary is DAG-ancestry-forced (like
  reachability) and the departed object leaves NO reflog — no co-present dangling
  copy.
- **Kill.** Show a reflog: the "gone" object is still on disk, recoverable →
  boundary was a moved ref (declared), not gc (physical). This IS the joint-record
  wound in git clothing.
- **Confidence.** 5.

**Hegelian.**
- Thesis: physical = DAG-reachability + gc-erasure; declared = ref movement.
- Antithesis (finite-closed-model objection): a finite closed model is exactly a
  git repo with gc *disabled* — every object ever created is retained and
  co-present. Reachability then is purely a function of where you point the ref,
  i.e. which subset you declare as R. The reflog always exists. In a closed model
  nothing is ever truly gc'd, so "unreachable" is always "reachable object I
  declined to name" — the joint-record completion move verbatim. Physical
  finality (gc) requires *actual deletion*, which a conservative closed model
  forbids.
- Synthesis (SHRINKS to a design requirement): git's lesson is precise — the
  physical boundary needs an *irreversible gc event* (real erasure of the
  co-present copy), not mere unreachability. Every fixture so far kept the reflog
  (retained tier-1). So U1's criterion is well-posed but UNMET: it demands
  modeling deletion/erasure as a dynamical event, which the conservative
  unitary+partial-trace house style structurally cannot do (partial trace ≠
  deletion; the traced register still exists globally). Non-empty as a sharp
  no-go on the current modeling style.

### U2 — transport rung

- **Steelman.** Transport = pushing commits to a remote you then lose network
  access to. If a commit is pushed to a remote and your local clone is pruned, the
  object has genuinely *left your reachable store*; recovering it requires
  re-fetching (a boundary-crossing task). The interaction graph (who has which
  objects) derives reach. This is a faithful transport picture.
- **Supporting argument.** Distributed git makes "who can produce object X" a real,
  location-indexed capability, not a global fact — exactly the C(R,M) shape.
- **Hidden assumptions.** That the remote copy is truly out of reach and not just
  un-fetched-yet (co-present on a reachable remote = joint record).
- **Vindication.** The departed object exists on NO node in R's reachable set
  within budget T, provably from the topology.
- **Kill.** The object sits on a remote that IS reachable (co-present in the fleet)
  → declared subset again.
- **Confidence.** 4.

**Hegelian.**
- Thesis: transport rung = push-then-lose-reach, reach derived from clone topology.
- Antithesis (joint-record completion): in a distributed VCS the whole point is
  that pushed objects are *replicated and co-present* across the fleet. "I can't
  reach it within T" is a fetch-budget statement — wait-longer / re-fetch and it
  returns. The object was never destroyed; it is a declared subset of the fleet's
  co-present object store. Joint-record completion: admit the remote's copy and
  the separator collapses. Same wall, third time.
- Synthesis (near-EMPTY): survives only if the transport is to a node that is
  *destroyed or permanently partitioned within budget* — replication turned into
  loss. Git's replication instinct actively fights the physical boundary: it is
  built to make records recoverable. Verdict: REDESIGN. Transport-by-replication
  is anti-finality; you'd need transport-by-erasure.

### U3 — literature adjacency

- **Steelman.** Recovery-after-departure maps to git's reflog / fsck / pack
  recovery: an object is recoverable exactly while a co-present trace (reflog
  entry, dangling blob) survives; after gc-expire it is gone. The threshold is the
  gc-expiry window — a cost/time boundary on recovery. This is a concrete
  recovery-window model.
- **Supporting argument.** `git fsck --lost-found` is a working recovery map with
  an explicit expiry. It quantifies "when and at what cost" concretely.
- **Hidden assumptions.** That expiry = physical erasure and not a policy timer
  (it IS a policy timer — `gc.reflogExpire`). So the boundary is declared config.
- **Vindication.** An expiry that is dynamics-forced (energy/entropy cost), not a
  settable timer.
- **Kill.** Expiry is a config knob → declared, not physical. It is.
- **Confidence.** 3. GU firewall resonance noted, NOT support.

**Hegelian.**
- Thesis: recovery-window = reflog-expiry, a cost/time recovery boundary.
- Antithesis: git's expiry is `gc.reflogExpire=90.days` — the purest possible
  *declared* bookkeeping. It is a config file. Borrowing it imports exactly the
  disease U1 is trying to cure.
- Synthesis (EMPTY): git offers a vivid metaphor and zero physical content for U3.
  The recovery boundary is always a policy timer. Record as empty for this
  persona.

### U4 — fallback

- **Steelman.** Fallback: the capability object is a *content-addressed
  provenance* claim — "which region can PRODUCE (re-derive) object X" is a real,
  location-relative invariant even if no boundary is physical. Git proves
  produce-ability (reachability + object availability) is a coherent,
  location-indexed capability ledger worth having.
- **Supporting argument.** Merkle/content-addressing gives a rigorous "who can
  reconstruct what" ledger; that is the anti-relabel global-correlation asset
  (candidate iii) in provenance form — a hash commits to the whole, no proper
  subset reproduces it.
- **Hidden assumptions.** That produce-ability adds over see-ability. It does — the
  DO-not-SEE thesis in cleanest form.
- **Vindication.** Formalize C(R,M) as an object-availability lattice with a
  Merkle-style whole-commits-not-parts separator.
- **Kill.** The ledger reduces to a plain accessibility relation with no
  DO/SEE gap → nothing new.
- **Confidence.** 5.

**Hegelian.**
- Thesis: fallback = content-addressed produce-ability ledger (DO not SEE).
- Antithesis: Merkle commitment to the whole is just a hash; "no proper subset
  reproduces the root" is the collision-resistance property, standard crypto, not
  a physics no-go — it corroborates the Lieb-Robinson-survivor (global
  correlation in no subset) as a *combinatorial* fact, weakening its physical
  reading.
- Synthesis (SURVIVES, reframed): the fallback survives as the *global-correlation
  separator* (candidate iii) with git supplying a clean model — the separator is
  whole-only, provably, and that is anti-relabel content. But it is
  combinatorial/information-theoretic, NOT physical-boundary. Aligns with the one
  surviving TaF asset. Non-empty; modest.

---

## 35. Database Systems Architect

### U1 — meaning of "physical rather than declared"

- **Steelman.** Databases separate *durability* (physical: the write hit stable
  storage; fsync'd; survives crash) from *visibility* (declared: isolation level,
  MVCC snapshot, which txn can see which row version). "Physical boundary" =
  durability/commit-point: after commit, the effect is real regardless of any
  observer's snapshot. "Declared" = an isolation-level cut over versions that are
  all physically co-present in the version store. The commit point is the one
  genuinely irreversible, mechanism-forced event (WAL flushed).
- **Supporting argument.** ACID durability is a real physical property: the commit
  LSN is fsync-forced; you cannot un-fsync. That is a mechanism-enforced finality,
  not a policy — unlike isolation, which is pure declaration over co-present MVCC
  versions.
- **Hidden assumptions.** That the model has a durability event (fsync analogue)
  distinct from a snapshot cut. The fixtures have only snapshot cuts (partial
  trace = choosing an MVCC snapshot), no fsync.
- **Vindication.** Fixture with a commit-point event that is mechanism-forced
  (entropy/work irreversible) separating states, distinct from a snapshot choice.
- **Kill.** The separator is an MVCC snapshot over co-present row versions → all
  versions physically present, cut declared. This is joint-record completion in DB
  terms — old row versions retained in the version store = retained tier-1.
- **Confidence.** 6.

**Hegelian.**
- Thesis: physical = durability/commit-point (fsync-forced); declared = MVCC
  visibility snapshot.
- Antithesis (finite-closed-model objection): a finite closed model is a database
  with *infinite version retention and no vacuum* — every row version ever written
  is co-present forever (unitary, no deletion). MVCC without vacuum means every
  "snapshot boundary" is a declared cut over fully co-present versions. The
  fsync/durability event has no analogue in a reversible closed model: there is no
  stable-storage-vs-volatile distinction because nothing is ever overwritten or
  lost. Durability requires the possibility of a crash (loss); a conservative
  closed model has no crash. So the one physical DB boundary evaporates on
  finitization — leaving only the declared snapshot, i.e. the joint-record wound.
- Synthesis (SHRINKS to requirement): DB lens sharply identifies what's missing —
  a *durability/erasure asymmetry* (crash-loss) that the model lacks. Physical
  boundary is well-posed and demands a VACUUM/crash event (irreversible version
  destruction). Current fixtures are no-vacuum MVCC → every boundary declared.
  Concrete, non-empty, but a demand on the model, not a repair of a fixture.
  Strong convergence with git-34's "gc/deletion" reading (flag: same-process).

### U2 — transport rung

- **Steelman.** Transport = replication log shipping. Reach = which replicas have
  applied the WAL up to LSN L within budget T. A row written to a replica the
  primary can't reach within T is genuinely unavailable to R. Reach is derived
  from replication topology + apply-lag — dynamics-forced, not declared.
- **Supporting argument.** CAP again, and PACELC: under a partition you trade
  consistency for availability; the unreached replica IS a partition, forcing the
  separator. Async replication makes "reachable within T" a real physical lag, not
  a choice.
- **Hidden assumptions.** That replication doesn't make the record co-present
  everywhere (it does — that's replication's job). That apply-lag = loss, not
  delay.
- **Vindication.** Departed record on a replica outside R's reach for a T pinned by
  physical apply-cost; separator forced by lag theorem.
- **Kill.** joint-record completion / wait-longer.
- **Confidence.** 4.

**Hegelian.**
- Thesis: transport rung = log-shipping, reach = applied-LSN within T.
- Antithesis (joint-record completion): replication is a *copying* protocol — the
  record is durably co-present on the source AND in the shipped log. "Not applied
  on replica within T" is apply-lag = wait-longer; the primary still holds it. The
  version is co-present in the global cluster state; admit it and the separator is
  a declared subset (the un-applied-yet replica's future state). PACELC's "else
  latency" branch says exactly this: absent a partition it's just latency you can
  wait out. Third hit on the wall.
- Synthesis (near-EMPTY): survives only under a *true partition with primary
  failure* (source destroyed before ship completes) — data actually lost, not
  lagged. Replication, like git, is built to prevent finality. Verdict: REDESIGN;
  log-shipping is anti-finality. You need an un-replicated, un-fsync'd write that
  is lost on crash — i.e. model crash-loss, which the closed model forbids (U1).

### U3 — literature adjacency

- **Steelman.** Recovery-after-departure = crash recovery / PITR
  (point-in-time-recovery) from WAL + backups, and erasure-coded storage recovery
  (RAID/Reed-Solomon). Threshold theorems apply: RS(n,k) recovers iff ≥ k of n
  shards reachable — a hard, provable threshold-crossing recovery boundary. Borrow
  RS threshold + quorum-recovery (read/write quorum W+R>N).
- **Supporting argument.** RS and quorum math are exact threshold-recovery theorems
  with proven bounds; they are the mature form of DA-sampling (55/9). Real,
  borrowable, quantifies "at what cost."
- **Hidden assumptions.** Redundancy exists to threshold over. The single departed
  carrier has k=n=1, no erasure structure → RS trivializes.
- **Vindication.** Restoration-at-R++ obeys an RS/quorum threshold matching
  W+R>N.
- **Kill.** Recovery is all-or-nothing (φ-independence), no shard structure →
  threshold theorems vacuous; it's a horizon, not a quorum.
- **Confidence.** 4. GU firewall resonance noted, NOT support.

**Hegelian.**
- Thesis: borrow RS/quorum threshold-recovery.
- Antithesis: same as 9/U3 — the separator is whole-only (global correlation in no
  proper subset), recovery is discontinuous, no graceful shard degradation.
  Quorum/RS presuppose linear redundancy; here worst-subset diff = 0.0 until the
  whole. Threshold math has nothing to grip.
- Synthesis (SHRINKS): honest adjacency is the *all-or-nothing secret-sharing*
  corner (a (n,n) threshold scheme where ALL shares are needed and any n-1 reveal
  zero) — which is the crypto reflection of the whole-only separator, NOT a
  graceful recovery theorem. Borrow the (n,n) all-shares structure as a MODEL of
  the separator, not a recovery bound. Modest, non-empty; corroborates candidate
  iii. Horizon lit remains the U3 home.

### U4 — fallback

- **Steelman.** Fallback: the capability object is a *serializability/consistency
  certificate* — a proof that a set of operations enactable from R cannot achieve
  a globally-serializable effect that R+ operations can. A safety certificate over
  what transactions R can commit. Even with declared boundaries this is a real
  isolation-frontier contribution.
- **Supporting argument.** Serializability theory (conflict graphs, acyclicity) is
  a mature safety-certificate machinery; recasting C(R,M) as "which serial
  schedules are enactable from R" is rigorous and licenses the toolkit reading
  (candidate i).
- **Hidden assumptions.** That the enactable-schedule frontier adds over plain
  reachability. Marginal.
- **Vindication.** C(R,M) as an enactable-schedule lattice with a proven R-vs-R+
  serializability gap.
- **Kill.** Reduces to standard DPI + accessibility, no isolation content →
  relabel.
- **Confidence.** 5.

**Hegelian.**
- Thesis: fallback = serializability/isolation-frontier certificate toolkit.
- Antithesis: decoherence-bookkeeping absorber — it's DPI + accounting; the
  "serializability gap" is the eraser-accessible-vs-escaped dichotomy renamed.
- Synthesis (SURVIVES, modest): lands on candidate (i) certificate-toolkit-as-
  calibration, agreeing with 9/U4 and T409's surviving standing. Real methods
  contribution, NOT a physical no-go. Non-empty.

---

## 36. Access-Control Systems Expert

### U1 — meaning of "physical rather than declared" (CLUSTER LEAD)

- **Steelman.** This is the sharpest U1 lens: access control already has a
  THREE-way distinction the program is conflating into two.
  (1) **Capability** — an unforgeable token; possession *is* the ability; holding
  it lets you DO the thing, mechanism-enforced by unforgeability (you cannot
  invoke what you cannot present).
  (2) **ACL / reference-monitor** — a mechanism (kernel, MMU) that *actively
  interposes* on every access and forces denial; physically enforced but by a
  guard, not by the subject's possession.
  (3) **Policy/stipulation** — a declared rule in a document with no mechanism
  behind it (paper policy).
  "Physical rather than declared bookkeeping" = the boundary is (1) or (2) —
  MECHANISM-enforced — versus (3) stipulated. A capability boundary is
  MECHANISM-enforced (physically forced) when *lacking the token makes the
  transformation not merely disallowed but non-enactable* — no sequence of
  R-supported operations forges it (unforgeability = a no-cloning/no-forging
  physical fact). That is exactly "physical, not declared." The fixtures'
  partial-trace boundary is category (3): the "retained" set is a stipulated
  policy tag, not a reference monitor forcing denial.
- **Supporting argument.** The capability-vs-ACL literature is precisely about
  when a boundary is enforced by the *structure of what you hold* (forced) vs *a
  lookup a guard performs* (interposed) vs *what a policy says* (declared). The
  program wants category (1): a boundary where the missing capability is
  physically unforgeable from inside R. Quantum no-cloning / no-forging is the
  physical mechanism that could make a capability boundary category-(1) forced —
  the one place "physical" has real teeth. THIS is the discriminating question the
  program should be asking.
- **Hidden assumptions.** That unforgeability in the fixture is physical
  (no-cloning) rather than declared (I labeled register i "not in R"). The current
  `prepare_retained` trace-if-not-in-retained IS a policy tag = category (3). The
  whole wound is: they built category (3) and claimed category (1).
- **Vindication.** A fixture where crossing R→R+ requires a token that is
  *physically unforgeable from R* by no-cloning/no-signaling — reach-failure =
  forging-failure, a physical impossibility, not a policy denial.
- **Kill.** Show the "capability" is a declared label with no unforgeability
  mechanism — i.e. an R-supported operation reconstructs the crossing token (the
  retained tier-1 Z-measurement P=0.4286 does exactly this: the "denied" info is
  forgeable from inside). Category collapses (1)→(3). This IS the joint-record
  kill, named precisely: the boundary was an ACL policy tag, and the retained
  correlated register is a forgeable credential.
- **Confidence.** 6.

**Hegelian.**
- Thesis: physical = capability-unforgeable-from-R (category 1, no-cloning-forced);
  declared = ACL policy tag on a co-present register (category 3).
- Antithesis (finite-closed-model objection): in a finite closed model with all
  registers co-present, is there a genuine category-(1) boundary, or does
  unforgeability always reduce to "I declared you can't read register i"? The
  reference-monitor (category 2) needs a guard *outside* the subject — but in a
  closed model there is no outside; the "guard" is just another co-present
  register, so interposition is declared. And a capability (category 1) is
  unforgeable only if no-cloning bites — but the fixtures RETAIN the tier-1
  carrier co-present (I=1.97 bits), so the crossing credential is *reconstructable*
  from R (P=0.4286 Z-measurement forges it). In a closed conservative model,
  everything co-present is in principle forgeable-from-the-whole; unforgeability
  requires something to be *physically absent*, which partial trace does not
  deliver (traced ≠ deleted). So category (1) collapses to (3) exactly when the
  boundary is declared-subset-of-co-present. Finite-closed-model objection stands.
- Synthesis (SHRINKS to a SHARP diagnostic): the access-control lens does not
  repair U1 but it *names the disease precisely and gives the well-posedness
  test*: the physical-boundary criterion IS well-posed — it is "is the crossing
  capability physically unforgeable from R (category 1) or a declared policy tag
  (category 3)?" A boundary is physical iff no R-supported operation forges the
  crossing credential. Every fixture to date FAILED this test (retained tier-1 =
  forgeable credential), which is why joint-record completion kills them. The
  criterion is meetable ONLY by a fixture where the crossing token is unforgeable
  by no-cloning/no-signaling AND the departed register is physically absent (not
  retained). This is the strongest surviving U1 REPAIR-SHAPED result in the
  cluster: not "here is a physical boundary" but "here is the exact, decidable
  test a candidate must pass, plus proof the current design class cannot pass it."
  Non-empty and load-bearing as a discriminator spec.

### U2 — transport rung

- **Steelman.** Transport rung is right because it converts a policy tag (category
  3) into a reference-monitor-forced boundary (category 2): propagation dynamics
  physically interpose — the interaction graph IS the reference monitor,
  mechanically denying reach beyond the causal set within T. The guard is the
  physics, not a label.
- **Supporting argument.** A capability that has physically left your causal reach
  is unpresentable — you cannot invoke a token you cannot causally touch. That is
  mechanism-forced denial (category 2→1).
- **Hidden assumptions.** That the token is truly gone from causal reach, not
  co-present-but-untagged. That the "monitor" (graph) isn't itself a declared
  partition of co-present state.
- **Vindication.** Crossing credential is causally unreachable within a
  work-pinned T — physically unpresentable, not policy-denied.
- **Kill.** joint-record completion.
- **Confidence.** 4.

**Hegelian.**
- Thesis: transport rung makes the boundary reference-monitor-forced (physics as
  guard).
- Antithesis (joint-record completion): "unreachable within T" is not
  "unforgeable" — the credential is causally co-present in the global state, just
  not yet fetched by R. A reference monitor that merely *delays* is not enforcing
  a boundary; it is rate-limiting (wait-longer). Once the ALL-interventions
  environment-side quantifier admits the co-present global state, the credential
  is present and forgeable → declared subset. The graph-guard denies *access
  latency*, not *possession*. Same wall.
- Synthesis (near-EMPTY): the rung upgrades category (3)→(2) ONLY if reaching the
  credential is *physically impossible within T*, not merely un-fetched — i.e. the
  monitor must be a no-signaling wall (causal past exclusion), not a lag. Access
  control cannot manufacture that; it needs the physics (U3 horizon / no-signaling)
  to supply an unforgeable-because-causally-absent credential. Verdict: REDESIGN
  toward causal-past exclusion (repair candidate (c) in U1); GO only if paired with
  a no-signaling unforgeability argument.

### U3 — literature adjacency

- **Steelman.** Recovery = credential revocation/re-issuance and key-recovery. When
  is a departed capability recoverable? In access control: iff a re-issuing
  authority (R++) exists and the revocation is soft; hard-revocation
  (key-destruction) is irrecoverable. Threshold: Shamir secret-sharing / threshold
  cryptography — a secret (credential) recoverable iff ≥ t of n shares reachable.
- **Supporting argument.** Threshold crypto is an exact recovery theorem;
  key-destruction is a clean irreversible-loss model (closer to real erasure than
  git/DB, which resist deletion). Access control natively models *hard revocation
  = destruction*.
- **Hidden assumptions.** That revocation is hard (key destroyed) not soft (policy
  flag). Soft revocation = declared = disease.
- **Vindication.** Restoration-at-R++ = threshold re-share; final-at-R+ =
  key physically destroyed within R+'s reach.
- **Kill.** Recovery is all-or-nothing whole-only → threshold (t<n) vacuous; use
  (n,n) all-shares.
- **Confidence.** 4. GU firewall resonance noted, NOT support.

**Hegelian.**
- Thesis: borrow threshold-crypto / hard-revocation-as-destruction.
- Antithesis: whole-only separator ⇒ only the (n,n) degenerate scheme fits; no
  graceful threshold. And "hard revocation" in a closed conservative model is
  again forbidden (no destruction) — soft revocation only ⇒ declared.
- Synthesis (SHRINKS): converges with 34/35 — the borrowable object is the *(n,n)
  all-shares secret-sharing scheme* as a MODEL of the whole-only separator
  (candidate iii), not a recovery bound. Access control adds the framing "the
  crossing credential is an (n,n) secret held jointly by the whole reach; no
  proper subset holds it." Clean model of the surviving asset; no physical
  boundary. Non-empty, modest.

### U4 — fallback

- **Steelman.** Fallback: C(R,M) IS a capability/authorization ledger — "what
  transformations region R is authorized-by-possession to enact." Even if the
  boundary is declared, a rigorous *capability lattice* (security-lattice /
  Bell-LaPadula-style partial order over what each region can DO) is a real
  contribution: the DO-not-SEE thesis is literally the capability-vs-information
  distinction (read ≠ execute), which access control has formalized for decades.
- **Supporting argument.** The confused-deputy / capability-vs-ACL literature is
  exactly "seeing information ≠ being able to act on it." That is the program's
  core thesis, already rigorous in access control. Strong fallback home.
- **Hidden assumptions.** That the capability lattice over C(R,M) is non-trivial
  (has incomparable elements) — the resource-theory absorber says it's a 12-object
  product preorder, which is a lattice but a mundane one.
- **Vindication.** C(R,M) as a security lattice with proven incomparabilities that
  are NOT a plain product order.
- **Kill.** Lattice = the 12-object product preorder (resource-theory absorber) →
  nothing new; ordinary monotone.
- **Confidence.** 5.

**Hegelian.**
- Thesis: fallback = capability/security-lattice formalization of DO-not-SEE.
- Antithesis: resource-theory absorber already showed the preorder is an ordinary
  product resource order; the DO-not-SEE gap is the free-ancilla monotonicity
  axiom renamed.
- Synthesis (SURVIVES, reframed): fallback lands as *the DO-not-SEE thesis given a
  rigorous access-control home* — the read≠execute distinction is genuinely the
  cleanest statement of the program's residue, but it is a KNOWN distinction, so
  the contribution is *importing* it, not discovering it. Aligns with candidate
  (iii) global-correlation-separator (the whole-holds-the-capability reading) plus
  candidate (i) toolkit. Non-empty; honestly modest — the novelty is the
  quantum-physical instantiation, not the distinction.

---

## 55. Hashgraph / Gossip-About-Gossip Provenance Researcher

### U1 — meaning of "physical rather than declared"

- **Steelman.** Hashgraph gives a physical-vs-declared distinction in provenance
  terms: an event's *causal past* (the DAG of events it gossip-references) is
  FORCED — it is cryptographically fixed the moment the event is signed; you
  cannot forge a different ancestry (hashes bind it). "Physical boundary" = the
  causal-past cut (what an event provably knew, forced by the hashgraph); the
  crossing datum is whether a witness is reachable in the gossip DAG. That is
  threshold-crossing, not declared: an event either is or isn't in the causal past,
  and that fact is signature-forced.
- **Supporting argument.** Gossip-about-gossip makes "who knew what when" a
  *derived* fact from signed event history, not a stipulated tag. Virtual voting
  computes finality from the DAG structure alone — no declared cut. This is a real
  forced-provenance boundary.
- **Hidden assumptions.** That "not in my causal past" = "physically unreachable"
  rather than "co-present event I haven't gossiped with yet." Gossip *converges* —
  everything eventually enters everyone's causal past. Delay ≠ absence.
- **Vindication.** A fixture where the crossing datum is provably outside R's causal
  past for a T pinned by gossip-propagation physics — ancestry-forced exclusion.
- **Kill.** The excluded event is co-present and will enter R's causal past by
  waiting (gossip convergence) → wait-longer; the cut was a snapshot of an evolving
  DAG, declared-at-time-t.
- **Confidence.** 4.

**Hegelian.**
- Thesis: physical = causal-past cut, signature-forced ancestry.
- Antithesis (finite-closed-model objection): hashgraph's causal past is forced
  only because events are *append-only and signed over time* — an open, growing
  DAG. A finite closed model is a *completed* gossip DAG where every event has
  already reached everyone (gossip has converged). In the converged state every
  event is in every node's causal past → no exclusion, all co-present. The "not in
  causal past" boundary exists only mid-gossip, i.e. as a time-indexed snapshot =
  declared-at-t. Signature-forcing binds *ancestry content*, not *reach exclusion*.
  So in a closed model the causal-past boundary heals (convergence) = joint-record
  completion. Stands.
- Synthesis (SHRINKS): survives as the observation that a physical boundary
  requires the DAG to be *permanently non-converged for R within budget* — a
  liveness/partition condition, not a safety fact of the completed structure.
  Reduces to the same "need a real partition" requirement as 9/35. Non-empty as
  requirement, not repair. NOTE strong overlap with 9 — single-process, not
  corroboration.

### U2 — transport rung

- **Steelman.** Transport rung is NATIVE to gossip: records propagate by actual
  gossip dynamics; reach = the causal-influence cone in the event DAG, derived from
  who-gossiped-with-whom. Joint-record completion is blocked *if* an event departs
  R's gossip neighborhood before R samples it and the DAG topology forbids
  back-flow within T. The interaction graph literally IS the gossip graph.
- **Supporting argument.** Provenance reconstruction ("who knew what when") is
  exactly reach-derived-from-dynamics; the departed record's absence from R's causal
  past is a structural DAG fact, not a declaration.
- **Hidden assumptions.** Gossip is designed to CONVERGE — anti-finality. Absence is
  temporary unless the topology permanently partitions R.
- **Vindication.** Departed event provably never enters R's causal past within
  work-pinned T by DAG topology.
- **Kill.** Gossip convergence returns it (wait-longer) / it's co-present in the
  full DAG (joint-record completion).
- **Confidence.** 4.

**Hegelian.**
- Thesis: transport rung = gossip propagation, reach = causal cone.
- Antithesis (joint-record completion): gossip-about-gossip's entire purpose is
  eventual total dissemination — every honest event reaches every node. "Departed
  before I sampled it" means it is co-present in others' causal pasts and in the
  global DAG; the ALL-interventions environment-side quantifier admits that global
  DAG, so the event is present and its provenance forgeable-from-the-whole. R is a
  declared temporal subset of the converged DAG. Gossip is the *most* anti-finality
  transport possible — it is engineered redundant dissemination. Third+ wall hit.
- Synthesis (EMPTY for finality; INVERTED insight): gossip transport actively
  DESTROYS the physical boundary because it guarantees co-presence-by-replication.
  Honest record: the gossip lens says the transport rung, if built on
  dissemination dynamics, will *reliably* reproduce joint-record completion.
  Verdict: ABANDON gossip-style transport; REDESIGN only toward dissemination-
  hostile (absorbing/erasing) dynamics. This is a useful NEGATIVE result — names a
  transport class that is guaranteed to fail.

### U3 — literature adjacency

- **Steelman.** Recovery = provenance reconstruction from signed histories +
  fork-detection. A departed record is recoverable iff enough signed
  gossip-references to it survive in reachable events (a Merkle-witness threshold).
  Adjacent to data-availability sampling (shared with 9): sample gossip witnesses;
  below a threshold of surviving references, provenance is unrecoverable.
- **Supporting argument.** Hashgraph's fork/ancestry proofs are concrete recovery-
  from-partial-history machinery; DA-sampling gives the threshold theorem.
- **Hidden assumptions.** Surviving references exist (redundant gossip). Whole-only
  separator kills the redundancy assumption.
- **Vindication.** Restoration obeys a witness-threshold matching DA-sampling.
- **Kill.** No proper subset of witnesses reconstructs it (whole-only) → threshold
  vacuous.
- **Confidence.** 3. GU firewall resonance noted, NOT support.

**Hegelian.**
- Thesis: borrow DA-sampling / witness-threshold recovery.
- Antithesis: whole-only separator ⇒ no witness subset suffices; threshold degrades
  to (n,n). Same as cluster.
- Synthesis (SHRINKS, converges): adds provenance framing "the crossing record's
  witness is an (n,n) event-set; no proper causal subset reconstructs who-knew-it."
  Model of candidate iii, not a recovery bound. Non-empty, modest, overlaps 9/35/36
  — SINGLE PROCESS, flag not corroboration.

### U4 — fallback

- **Steelman.** Fallback: C(R,M) as a *signed provenance ledger of enactable
  transformations* — "who can PRODUCE this state-change, with forced ancestry."
  Virtual-voting-style, the ledger certifies capability-provenance without a
  declared boundary. The anti-relabel asset (global correlation in no subset) is a
  provenance fact: the crossing datum's ancestry is jointly held.
- **Supporting argument.** Gossip provenance is a mature "who-can-do-what-with-proof"
  ledger; recasting C(R,M) this way gives forced (signed) provenance to the
  capability object.
- **Hidden assumptions.** That signed provenance adds physics over combinatorics. It
  is combinatorial/crypto, not physical.
- **Vindication.** C(R,M) as a virtual-voting capability ledger with whole-only
  provenance separator.
- **Kill.** Reduces to hash-commitment (combinatorial) with no physical boundary →
  corroborates the separator is combinatorial, not physical.
- **Confidence.** 4.

**Hegelian.**
- Thesis: fallback = signed provenance capability ledger.
- Antithesis: it's crypto commitment; "whole-only" = collision-resistance, weakens
  the physical reading of the surviving separator (same as git-34/U4).
- Synthesis (SURVIVES as combinatorial): fallback = candidate (iii) global-
  correlation separator, honestly reframed as an information/provenance fact, not
  physical. Non-empty; modest; reinforces that TaF's one surviving asset is
  combinatorial.

---

## 56. Avalanche-Class Consensus Researcher

### U1 — meaning of "physical rather than declared"

- **Steelman.** Avalanche gives a boundary that is a genuine *threshold-crossing*,
  not a declared cut: repeated subsampled voting drives confidence, and at a
  metastability tipping point the system commits irreversibly — a phase-transition-
  like flip. "Physical boundary" = the metastable tipping threshold: below it the
  state is reversible, above it (confidence β accumulated past k) it is
  probabilistically final and cannot practically flip. That threshold is DYNAMICS-
  forced (network sampling drives it), not a policy line — the closest consensus
  analogue to a physically-forced (threshold-crossing) boundary.
- **Supporting argument.** Probabilistic finality is precisely a *forced* boundary:
  no one declares finality; it emerges when reversal probability drops below ε
  through accumulated confidence. That is a threshold-crossing, matching the
  program's wish for "forced, not declared" — and it is a real, deployed mechanism.
- **Hidden assumptions.** That the finite closed model has a metastable dynamic
  (subsampling / confidence accumulation) at all. Unitary fixtures have no
  sampling, no metastability, no irreversible tip — the tip requires
  *effective irreversibility* the conservative model lacks.
- **Vindication.** A fixture with a confidence/metastability parameter whose
  crossing is dynamics-forced and separates A from B irreversibly-within-budget.
- **Kill.** Show the "tip" is reversible under R-supported operations (retained
  correlated register lets you flip the verdict back, P=0.4286) → not a real
  threshold, a declared snapshot.
- **Confidence.** 5.

**Hegelian.**
- Thesis: physical = metastability tipping threshold (probabilistic-finality-forced).
- Antithesis (finite-closed-model objection): Avalanche's irreversibility is
  *probabilistic and adversary-relative* — final means "reversal costs more than an
  adversary can muster," a resource threshold, NOT a safety impossibility. In a
  finite closed conservative (unitary, reversible) model there is NO true
  irreversibility: every dynamic is invertible, so no metastable tip is permanent —
  the retained tier-1 register is exactly the handle that reverses the verdict
  (B-at-R++ restorable). "Probabilistic finality" is the purest *wait-longer /
  resource-threshold* boundary: more work/depth reverses it. So Avalanche finality
  is category "resource threshold," which the kill history explicitly flags as NOT
  a physical wall (it's the wait-longer killer). Finite-closed-model + reversibility
  ⇒ the threshold is a knob.
- Synthesis (SHRINKS / near-EMPTY): probabilistic finality does NOT supply a
  physical boundary — it supplies the archetype of the boundary the program must
  AVOID (a resource/confidence threshold that more work reverses). Honest inversion:
  Avalanche clarifies that "threshold-crossing" is NOT automatically "physical"; a
  threshold you can re-cross with more resources is declared-relative-to-budget. The
  program needs a threshold that is *thermodynamically irreversible* (entropy-priced
  permanence, candidate (b) in U1), not merely confidence-high. Useful negative
  discrimination; no repair. Non-empty as a caution.

### U2 — transport rung

- **Steelman.** Transport rung with a confidence-accumulation lens: reach is the
  set the agent can *sample within T*; a record outside the subsample horizon is
  unqueryable, and repeated sampling that never reaches it makes it effectively
  final-relative-to-R. Reach derived from sampling dynamics, not declared.
- **Supporting argument.** Subsampled voting formalizes "bounded coupling + time
  budget" directly: k queries × m rounds = a bounded reach; beyond it the record is
  unsampled → separator forced by sampling bound.
- **Hidden assumptions.** Unsampled ≠ absent (co-present, just not queried).
  More rounds (wait-longer) extend reach.
- **Vindication.** Record provably unsampleable within a work-pinned query budget.
- **Kill.** joint-record completion / wait-longer (more rounds reach it).
- **Confidence.** 3.

**Hegelian.**
- Thesis: transport rung = sampling horizon, reach = subsample-reachable set.
- Antithesis (joint-record completion): "unsampled within budget" is the weakest
  possible boundary — the record is co-present and reachable with more query
  rounds; this is wait-longer BY DEFINITION (Avalanche gains confidence precisely by
  more rounds). The un-queried register is a declared subset of the co-present
  network state; admit it (ALL-interventions env-side quantifier) and the separator
  collapses. Sampling budget is a resource threshold, not a wall. Wall hit, and this
  is the WEAKEST of the cluster's transport steelmen because sampling is explicitly
  budget-extensible.
- Synthesis (EMPTY): sampling-horizon transport is a resource threshold through and
  through; it cannot escape joint-record completion or wait-longer. Honest record:
  EMPTY. Verdict: ABANDON sampling-based transport framing for the physical boundary.

### U3 — literature adjacency

- **Steelman.** Recovery = reorg-depth / probabilistic-finality reversal cost: a
  record is recoverable (reversible) while below finality depth k, final beyond it.
  The cost function is explicit (confidence vs depth). Borrow the finality-depth
  cost curve as the "at what cost is recovery possible" answer.
- **Supporting argument.** Probabilistic-finality math gives a smooth cost-of-
  reversal curve — a quantitative recovery boundary, directly answering U3's cost
  question.
- **Hidden assumptions.** Recovery is graded in depth. The fixture's recovery is
  all-or-nothing (φ-independence) — no smooth depth curve.
- **Vindication.** Restoration cost follows a confidence-depth curve.
- **Kill.** All-or-nothing whole-only separator → no smooth curve; depth math
  vacuous.
- **Confidence.** 3. GU firewall resonance noted, NOT support.

**Hegelian.**
- Thesis: borrow probabilistic-finality reversal-cost curve.
- Antithesis: recovery is discontinuous-at-the-whole (worst-subset 0.0), not smooth
  in depth. Avalanche's graded finality has nothing to grip; the fixture is a step
  function.
- Synthesis (EMPTY / near-EMPTY): probabilistic-finality's smoothness is the wrong
  shape for a whole-only step separator. No borrowable theorem. Honest record:
  EMPTY for this persona; the fixture is more horizon-like (sharp) than reorg-like
  (graded). Confirms horizon lit (U3 pole) over consensus finality.

### U4 — fallback

- **Steelman.** Fallback: the certificate toolkit as a *probabilistic safety/liveness
  certificate* — quantifying, for a family, the confidence with which "no R-supported
  protocol crosses" holds. A calibrated confidence-certificate over the capability
  frontier.
- **Supporting argument.** Avalanche's contribution was a *new certificate style*
  (confidence-based, outside quorum/BFT); recasting the toolkit as a confidence-
  calibrated frontier certificate is a real methods analogue and matches T409's
  surviving calibration standing.
- **Hidden assumptions.** That a probabilistic certificate adds over an exact one.
  The fixtures use EXACT certificates (φ-independence) — probabilism is a
  weakening, not an asset here.
- **Vindication.** Toolkit yields a calibrated confidence curve over a model family
  (the T409 calibration reading, quantified).
- **Kill.** Exact certificates dominate; probabilistic layer adds nothing → drop.
- **Confidence.** 4.

**Hegelian.**
- Thesis: fallback = probabilistic confidence-certificate toolkit.
- Antithesis: fixtures already have EXACT certificates; probabilism is strictly
  weaker; decoherence-bookkeeping absorber makes even the exact one DPI.
- Synthesis (SURVIVES only as merge into candidate (i)): the honest fallback is the
  EXACT certificate toolkit (9/35 already carry this) as calibration machinery;
  Avalanche's probabilistic flavor is NOT an asset for exact fixtures. Contribution:
  none distinct. Collapses into 9/35/36's toolkit synthesis. Near-EMPTY as a
  separate result.

---

## Cluster Synthesis

Reminder: six masks, one process. Convergences below are single-process targets,
NOT corroboration. Every "physical boundary" steelman in this cluster failed to
repair the wound; the honest yield is a set of DESIGN REQUIREMENTS and a sharp
DISCRIMINATOR SPEC, plus a modest surviving fallback.

### U1 — what "physical rather than declared" must mean

- **Strongest surviving result (36, Access-Control, cluster lead): a decidable
  discriminator SPEC, not a boundary.** Physical = the crossing capability is
  *unforgeable from R* (category-1 capability, no-cloning/no-signaling-forced) AND
  the departed register is *physically absent* (not retained); declared = an ACL
  policy tag on a co-present register (category 3). Well-posedness test: *a boundary
  is physical iff no R-supported operation forges the crossing credential.* Every
  fixture to date FAILS it (retained tier-1 = forgeable credential; the P=0.4286
  Z-measurement literally forges the "denied" datum) — which is exactly why
  joint-record completion kills them. This survives BOTH thesis and antithesis as a
  discriminator specification.
- **Convergent design requirements (9 FLP/CAP, 34 gc/deletion, 35 vacuum/crash,
  55 gossip-convergence, 56 thermodynamic-irreversibility):** all five independently
  demand the SAME missing ingredient — the model must contain a genuine
  *irreversible loss / partition-that-cannot-be-healed* event. Partial trace ≠
  deletion; the conservative unitary+partial-trace house style structurally cannot
  produce it (traced register stays globally co-present). 56 adds the sharpest
  caution: a threshold you can re-cross with more resources (probabilistic finality)
  is NOT physical — physical requires *entropy-priced permanence* (U1 candidate b),
  not confidence-high (candidate a's "permanent-within-budget" is too weak if budget
  is extensible).
- **Surviving repair candidates ranked:** (b) entropy-priced permanence and
  (c) causal-past exclusion survive as the only two the cluster can see a mechanism
  for; (a) agent-relative+permanent-within-budget is weakened by 56 (budget-
  extensible ≠ physical); (d) protocol-impossibility survives only as the 9-lens
  certificate, which is toolkit not boundary.
- **Confidence range 4–6.** Dissent/caution: 56 argues threshold-crossing ≠ physical
  (inverts the naive reading). No persona produced an actual physical boundary; U1
  yields a SPEC + requirements, honestly.

### U2 — transport rung premortem

- **Verdict: REDESIGN (5 personas) / ABANDON-as-framed (56, and 55 for gossip-class).
  No GO.** Unanimous: the transport rung as "reach = reachable-within-time-budget"
  does NOT escape joint-record completion — it RENAMES it. "Reachable within timeout
  = co-present" is the exact substitution joint-record completion feeds on; the
  departed register stays co-present in the global state (admitted by the
  ALL-interventions environment-side channel lemma) and thus a declared subset. This
  is the wall's FOURTH+ kill, now diagnosed at the transport level before build.
- **Sharp negative result (55): dissemination/gossip/replication transport is
  ANTI-finality by construction** — git push, DB log-shipping, and gossip all exist
  to make records co-present/recoverable. Building the rung on propagation dynamics
  RELIABLY reproduces joint-record completion. 56: sampling-horizon transport is the
  weakest (budget-extensible = wait-longer by definition) → EMPTY.
- **The narrow survivable redesign (36+9):** the rung escapes ONLY if "departure" is
  *irreversible co-presence-destruction within T* (causal-past exclusion +
  no-signaling unforgeability), NOT mere unreachability. The distributed-systems lens
  can supply unreachability (CAP/FLP) but NOT non-existence; the non-existence /
  irreversibility must come from physics (U3/thermo), not from the network bound. So:
  REDESIGN toward erasure/absorbing dynamics + causal-past exclusion; do not build a
  reachability-threshold rung.
- **Confidence range 3–4.** Joint-record completion faced explicitly by all six; none
  escaped it with a network bound alone.

### U3 — literature adjacency

- **Weak/cosmetic adjacency to blockchain finality & threshold recovery; EMPTY or
  near-EMPTY borrowable theorems.** Reason (unanimous 9/35/36/55/56): the fixture's
  separator is *whole-only* (global correlation in no proper subset; worst-subset
  diff 0.0 until the whole) and recovery is *all-or-nothing* (φ-independence). Every
  candidate theorem (data-availability sampling, Reed-Solomon/quorum W+R>N,
  probabilistic-finality depth curves, gossip witness-thresholds) assumes GRACEFUL
  degradation with reachable fraction. There is no gradient to threshold → theorems
  vacuous/(n,n)-degenerate.
- **The one honest borrow (34/35/36/55 converge): the (n,n) all-shares secret-sharing
  scheme** as a MODEL of the whole-only separator (any n-1 shares reveal zero) — a
  combinatorial model of candidate (iii), NOT a recovery bound. Plus the
  *weak-subjectivity / long-range-attack* corner (9): safety unrecoverable from the
  protocol alone, needs an external anchor (maps to "need R++/out-of-band anchor").
- **The natural home is horizon literature, not consensus finality** — the separator
  is sharp/step-like (horizon), not graded (reorg). 56 explicitly: fixture is
  horizon-like, not reorg-like.
- **GU firewall resonance FLAGGED by all, treated as NON-support** per the one-way
  rule. Confidence 3–4.

### U4 — fallback

- **Strongest surviving fallback (converged 9/35/36, modest): candidate (i) the
  certificate toolkit as calibration machinery**, recast in consensus terms as an
  exact impossibility/safety certificate over a model family — matching T409's
  actual surviving standing (calibration of the certificate toolkit). Real METHODS
  contribution; NOT a physical no-go. 56's probabilistic-certificate variant adds
  nothing over the exact certificates and collapses in.
- **Second surviving fallback (34/36/55): candidate (iii) the global-correlation
  separator, honestly reframed as COMBINATORIAL/information-theoretic** (Merkle
  whole-commitment / (n,n) secret / signed provenance) — the anti-relabel asset, but
  its "no proper subset" property is collision-resistance/combinatorics, which
  WEAKENS its physical reading. It corroborates the Lieb-Robinson survivor as genuine
  content while denying it is a physical boundary.
- **36's distinctive framing: candidate (iii) also = the DO-not-SEE thesis given a
  rigorous access-control home** (read ≠ execute; capability vs ACL). Cleanest
  statement of the program's residue — but a KNOWN distinction; the novelty is the
  quantum instantiation, not the distinction. Resource-theory absorber caps it (12-
  object product preorder = ordinary monotone).
- **Is it worth a paper? Cluster answer: yes, but only as (i) methods/certificate-
  toolkit + (iii) combinatorial anti-relabel separator — NOT as a physical-boundary
  no-go.** Confidence 4–6.

### Empty / shrinkage ledger (honest record)

- U1: no physical boundary produced; yields a discriminator SPEC (36) + convergent
  design requirement (irreversible-loss event the house style cannot model). SHRINK.
- U2: REDESIGN/ABANDON, no GO; joint-record completion re-killed at transport level;
  55 gossip-transport EMPTY (anti-finality); 56 sampling-transport EMPTY. SHRINK to
  a narrow physics-dependent redesign.
- U3: borrowable-theorem search largely EMPTY (whole-only ⇒ threshold math vacuous);
  34 fully EMPTY (git expiry = config); only (n,n) secret-sharing as a MODEL survives;
  horizon lit favored over consensus.
- U4: SURVIVES modest — toolkit (i) + combinatorial separator (iii); physical framing
  survives at NO tier. 56 U4 near-EMPTY (probabilism weaker than exact).
- Single-process caution: 9/35/36/55 converged on (n,n)/irreversible-loss/whole-only
  because they share a substrate, NOT because it is corroborated. Convergence here is
  a TARGET (build an erasure/causal-exclusion fixture with an unforgeability
  certificate), never evidence.
