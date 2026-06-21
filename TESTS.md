# Tests

The project is useful only if claims can be formalized, stressed, or broken.

## Test Index

| ID | Test | Target claims | Status |
| --- | --- | --- | --- |
| [T1](tests/T1-record-graph-temporal-reconstruction.md) | Record graph temporal reconstruction | C1, D1, D2 | implemented: partial success |
| [T2](tests/T2-quantum-measurement-record-finality.md) | Quantum measurement record finality | Q1, D1, G2 | implemented: dynamical measurement finality lab |
| [T3](tests/T3-spacelike-events-no-global-commit-order.md) | Spacelike events and no global commit order | R1, G2 | open |
| [T4](tests/T4-black-hole-causal-access-boundary.md) | Black-hole causal access boundary | B1, G2 | open |
| [T5](tests/T5-thermodynamic-record-support.md) | Thermodynamic record support | D1, C1 | structural benchmark implemented |
| [T6](tests/T6-snowball-record-finality.md) | Snowball record finality | A1, D1, Q1 | open |
| [T7](tests/T7-overlapping-causal-domains.md) | Overlapping causal domains | R1, B1, S1 | open |
| [T8](tests/T8-observer-renderer-toy-model.md) | Observer renderer toy model | D2, G3 | open |
| [T9](tests/T9-emergence-laboratory.md) | Emergent records across reversible and irreversible local dynamics | D1, C1, T5 | implemented: comparative success |
| [T16](tests/T16-spacetime-aggregation.md) | Spacetime aggregation toy model | S1, H5, R1 | implemented: finite gluing and obstruction witnesses |
| [T17](tests/T17-consensus-finality-crosswalk.md) | Consensus finality crosswalk | A1, D1 | implemented: collapse maps and bounded theorem check |
| [T18](tests/T18-finality-direction-theorem.md) | Finality direction theorem | H7, D1 | implemented: constructor-style finite theorem check |
| [T80](tests/T80-reversible-finality-nonmonotonicity.md) | Reversible finality nonmonotonicity | H7, T9, T18 | implemented: reversible Rule 30 lift violates raw D1 monotonicity, weakening H7 to a conditional constructor theorem |
| [T82](tests/T82-persistent-reconciler-cost-boundary.md) | Persistent reconciler cost boundary | H7, T9, T80 | implemented: persistent memory restores monotone retained support only through irreversible OR memory or resource-accounted append-only ledger capacity |
| [T84](tests/T84-cyclic-reconciler-entropy-export.md) | Cyclic reconciler entropy export | H7, T80, T82 | implemented: fixed cyclic reconciliation restores monotone accounting only by exporting overwritten records or paying erasure cost |
| [T106](tests/T106-bounded-sink-reversible-compression.md) | Bounded-sink reversible compression | H7, T80, T82, T84 | implemented: reversible compression does not rescue H7 once the bounded sink and closed return path are included |
| [T110](tests/T110-finite-permutation-monotone-obstruction.md) | Finite-permutation monotone obstruction | H7, T80, T82, T84, T106 | implemented: finite closed reversible dynamics admit no strict scalar finality monotone unless the score is constant on each orbit |
| [T116](tests/T116-open-markov-record-entropy.md) | Open Markov record-entropy comparison | H7, T110 | implemented: open stochastic record arrows are absorbed by path irreversibility, exported history, or fresh blank capacity in the tested fixtures |
| [T122](tests/T122-stationary-markov-monotone-obstruction.md) | Stationary Markov monotone obstruction | H7, T110, T116 | implemented: finite stationary Markov dynamics admit no strict scalar expected-finality monotone on stationary support |
| [T124](tests/T124-constructor-admissibility-grounding-audit.md) | Constructor-admissibility grounding audit | H7, T18, T80, T84, T106, T110, T116, T122, T128 | implemented: reverse-edge ledger permits only constructor-only or resource-accounting readings; no current H7 witness grounds an unqualified physical arrow |
| [T125](tests/T125-d1-boundary-connection-transport.md) | D1 boundary connection transport | D1, R1, S1, T111, T112, T113 | open: specification-only transport audit for boundary-indexed D1 profiles, identity, composition, closed loops, provenance deltas, and hostile controls |
| [T126](tests/T126-finality-colimit-causal-set-embeddability.md) | Finality-colimit causal-set embeddability audit | S1, T16, T51, T52, T53, T54, T56, T58 | open: specification-only finite causal-set/manifoldlikeness filter for canonical finality colimits, with explicit non-embeddability modes and no spacetime derivation |
| [T127](tests/T127-same-neighbor-data-losskernel-audit.md) | Same-neighbor-data LossKernel audit | TF1, T34, T37, T39, T40, T69, T73, T99, T107, T108 | open: specification-only prior-art separation gate for source-anchored witness obligations after neighboring CSP/provenance/abstract-interpretation/lens/effect data are matched |
| [T128](tests/T128-minimal-living-arrow.md) | Minimal living arrow | H7, T80, T82, T84, T106, T110, T122 | implemented: smallest non-stipulative finite survivor is explicit resource drawdown; maintenance/open-boundary survivors reduce to resource/sink/export accounting and constructor restriction is stipulative |
| [T142](tests/T142-thermodynamic-erasure-calibration.md) | Thermodynamic erasure calibration | H7, T124, T128, T141 | implemented: T1 copy/branch-support gains are absorbed by reversible uncopy or ordinary erasure/free-energy accounting; D1 topology at fixed erasure floor is not arrow evidence |
| [T114](tests/T114-viability-filter.md) | Viability filter | North Star, D1, H7, emergence | implemented: finite geometry-to-viability filter with maintenance, record-finality, and emergence-platform gates; no core claim upgrade |
| [T115](tests/T115-maintenance-viability-split.md) | Maintenance-cost viability split | T114, H7, TF1, reconstruction debt | implemented: matched entropy/control/stability/viability/storage examples split on future operation rights, but strongest cases are absorbed by provenance, commons, and reconstruction debt |
| [T117](tests/T117-accessible-state-space-separation.md) | Accessible State Space separation audit | T115, H7, TF1, reconstruction debt | implemented: ASP separates from coarse entropy/information/finality/viability/persistence metrics, but is mostly absorbed by enriched reachable-state and opportunity-set theories |
| [T119](tests/T119-future-operation-availability-residue.md) | Future Operation Availability residue audit | Q1A, T117, T115, TF1, PO1, provenance | implemented: multiple branches converge on task-indexed future operation availability as a useful normal form, but it is absorbed by enriched reachability/opportunity/provenance/control frameworks |
| [T129](tests/T129-future-capability-preservation-audit.md) | Future capability preservation audit | T119, T121, T123, T128, ASP, FOA, LossKernel, admissibility | implemented: same-current-state/different-future-capability residue has a common audit normal form but is absorbed by enriched reachability, opportunity-set, provenance, access-control, mechanism-design, and viability frameworks |
| [T20](tests/T20-consensus-record-theorem-transfer.md) | Consensus-record theorem transfer | A1, D1, T13, T17 | implemented: theorem-transfer and boundary cases |
| [T21](tests/T21-bell-contextuality-finality.md) | Bell contextuality finality | Q1, D1, T13, T20 | implemented: CHSH contextuality and score comparison |
| [T22](tests/T22-d1-physical-reduction-map.md) | D1 physical reduction map | D1, Q1, T2, T21 | implemented: observable audit and holder-redundancy reduction |
| [T23](tests/T23-invariant-preserving-transformations.md) | Invariant-preserving transformations | IPT, D1, Q1, A1, T2, T20, T22 | implemented: typed IPT kernel, composition check, and obstruction witness |
| [T24](tests/T24-d1-multiscale-observer-field.md) | D1 multiscale observer field | D1, D1-Field, IPT, T13, T21, T23 | implemented: scalar/vector/field audit with transport and gluing counterexamples |
| [T25](tests/T25-minimal-d1-generalization.md) | Minimal D1 generalization | D1, D1-Field, IPT, T13, T21, T23, T24 | implemented: H0-H4 audit and theorem ladder |
| [T26](tests/T26-d1-restriction-system.md) | D1 restriction system | D1, D1-Field, IPT, T25 | implemented: finite graph-indexed D1 restriction object and morphism checks |
| [T27](tests/T27-class-relative-bridge-audit.md) | Class-relative bridge audit | D1RestrictionSystem, PO1 | implemented: GU bridge audit with faithful and non-definable cases |
| [T28](tests/T28-cap-theorem-bridge.md) | CAP theorem bridge | D1RestrictionSystem, PO1, T27 | implemented: CAP as finite gluing obstruction with NN structural comparison |
| [T29](tests/T29-projection-obstruction-schema.md) | Projection-Obstruction Schema | PO1, T26, T27 | implemented: finite schema with positive and boundary cases |
| [T30](tests/T30-cross-domain-projection-obstruction-validation.md) | Cross-domain projection-obstruction validation | PO1, T29 | implemented: hostile non-physics validation with Git and financial risk positives plus translator/poet boundary |
| [T31](tests/T31-po1-admissibility-conditions.md) | PO1 admissibility conditions | PO1, T29, T30 | implemented: seven-condition admissibility checklist and case reclassification |
| [T32](tests/T32-admissibility-derivation.md) | PO1 admissibility derivation | PO1, T31 | implemented: AC dependency graph, minimal basis, and generated subset counterexamples |
| [T33](tests/T33-po1-foundational-derivation.md) | PO1 foundational derivation | PO1, T32 | implemented: IPT/RMT hypothesis matrix (H0-H5); H3 best supported; AC5-naming recommended as Principle P5 |
| [T34](tests/T34-po1-chained-projection.md) | Chained projection analysis | PO1, T29, T31, T32, T33 | implemented: emergent, stepwise, and absorbed obstruction confirmed across three chain shapes |
| [T35](tests/T35-projection-obstruction-discovery-engine.md) | Projection-obstruction discovery engine | PO1, T31, T33, T34 | implemented: bounded finite exploration engine with generated positives, boundaries, and counterexamples |
| [T36](tests/T36-compression-finality-crosswalk.md) | Compression-finality crosswalk | D1, C1, T9 | implemented: finality≠compressibility confirmed; Rule 30 and Rule 0 counterexamples; correlations partial (−0.745, +0.631) |
| [T37](tests/T37-typed-transport-network.md) | Typed transport network | PO1, T26, T31, T34 | implemented: path-dependent admissibility witnessed; diamond network shows same (source, target) with different paths giving different PO1 verdicts (AC5 varies by path) |
| [T38](tests/T38-minimal-multiscale-transport.md) | Minimal multiscale transport | H1+, T26, T31, T37 | implemented: H0 covers 3/10 questions; H1 covers 8/10; H1+ (TypedTransportNetwork + CompressionRecord + EmergenceRecord) covers all 10; H2 and H3 not required |
| [T39](tests/T39-csp-satisfiability-reframing.md) | CSP / satisfiability reframing | PO1, T26, T31, T38 | implemented: PO1 gluing obstruction = binary {-1,1} parity-conflict CSP; arc consistency trivially true; typed projection (AC5, AC7) and admissibility classification are new structure not expressible in standard CSP; H_B best supported |
| [T40](tests/T40-holarchy-lab.md) | Holarchy lab — emergent holonic finality | D1, PO1, TTN, T38, T39 | implemented: holonic emergence confirmed (3-node triangle obstruction from micro-compatible nodes); cross-level AC5 necessary for holonic PO1; H_B best supported |
| [T41](tests/T41-typed-transport-category.md) | Typed transport category prototype | D1, PO1, T26, T31, T34, T37 | implemented: D1RestrictionMorphisms form a proper category (associativity 4/4, left unit 5/5, right unit 5/5); PO1 is not a Boolean functor on D1Cat (T34 restated in categorical language); H_A best supported |
| [T42](tests/T42-local-persistence-reconciliation-split.md) | Local persistence and reconciliation split audit | R1, G2, D1, T3 | implemented: LocalPersistenceReconciliationSystem separates local accumulation from reconciliation lag; four witnesses pass (delay-only, accumulation-only, both, null); H2 best supported |
| [T43](tests/T43-local-persistence-mechanisms.md) | Local persistence accumulation mechanism audit | R1, G2, D1, T42 | implemented: intrinsic rate, resource budget, and interaction density produce local differences with propagation fixed; propagation-shadow rejected; H4 best supported |
| [T44](tests/T44-local-mechanism-identifiability.md) | Local mechanism identifiability audit | R1, G2, T42, T43 | implemented: baseline traces remain ambiguous, but demand-drop plus coupling-rewire separates intrinsic rate, resource budget, and interaction density; H4 best supported |
| [T46](tests/T46-open-causal-scarcity-synchronization-boundary.md) | Open causal scarcity and closed synchronization boundary | R1, A1, PO1, T42, T44 | implemented: RecordAccessSystem distinguishes open causal-proximity scarcity from closed membership-plus-synchronization scarcity; H3 best supported; CS1 remains candidate only |
| [T47](tests/T47-po1-dag-theorem.md) | PO1 DAG theorem | PO1, D1Cat | implemented: PO1-admissible morphisms form an acyclic bipartite graph with depth <= 1 |
| [T48](tests/T48-finali-event-structure.md) | FinaliEvent structure | PO1, C1, T47 | implemented: PO1-admissible morphisms can be ordered by record containment into a partial order with incomparable events |
| [T49](tests/T49-reconstruction-without-background-time.md) | Reconstruction without background time | C1, T48 | implemented: two-axis finality dominance reconstructs the T48 record order without a scalar time variable |
| [T50](tests/T50-axis-monotonicity-theorem.md) | Axis monotonicity theorem | C1, T48, T49 | implemented: AM is the exact condition under which finality-axis dominance equals record order; counterexample and anti-scalar corollary included |
| [T51](tests/T51-multi-observer-apparent-finality-colimit.md) | Multi-observer apparent finality colimit | C1, D1-Field, T47, T48, T50 | implemented: bounded observer access creates phantom incomparability repaired by a valid colimit |
| [T52](tests/T52-symmetric-colimit-theorem.md) | Symmetric colimit theorem | C1, D1-Field, T47, T50, T51 | implemented: complementary bounded observers jointly recover the full reference order and restore AM at the colimit |
| [T53](tests/T53-observer-colimit-descent-boundary.md) | Observer-colimit descent boundary audit | C1, D1-Field, T47, T48, T50, T51 | implemented: valid colimit does not imply canonical completion or axis reconstructability; H2/H3/H4 best supported |
| [T54](tests/T54-finite-finality-descent-theorem.md) | Finite finality descent theorem | C1, D1-Field, T50, T51, T52, T53 | implemented: quotient-union descent conditions classify T51/T52 as canonical, T53 as underdetermined, and all omitted-condition counterexamples |
| [T55](tests/T55-conflict-finalievent-descent.md) | Conflict-enriched FinaliEvent descent | C1, D1-Field, T48, T50, T54 | implemented: T54 generalizes to non-empty conflict with added finite conflict checks; conflict is independent of order and AM |
| [T55B](tests/T55B-provenance-aware-reconstruction.md) | Provenance-aware reconstruction separation audit | C1, D1-Field, T51, T52, T54 | implemented: H4 confirmed (provenance variation does not change colimits, AM, or T54 descent); H1 supported (same basis, different provenances); H0 refuted; recommendation: optional audit layer |
| [T56](tests/T56-sheaf-cohomology-apparent-finality.md) | Sheaf cohomology of apparent finality — research audit | C1, D1-Field, T51, T52 | implemented: PARTIAL_SUCCESS — ambient presheaf A is well-defined (H1(A)=0); apparent-finality assignment F is not a presheaf (natural restriction overshoots F(U)); phantom incomparability is an H0-level section-mismatch, not H1; refined hypothesis: H0(G) where G=A/F is the gap presheaf; 4 open questions; 56/56 tests pass |
| [T57](tests/T57-finality-reflection-property.md) | Finality Reflection Property | C1, D1-Field, T56 | implemented: FRP holds for the T56 apparent-order model across two finite record lattices; G(U)=A(U)-F(U) is restriction-closed; generic complement counterexample refutes automatic complement closure; arrow-direction circularity remains open |
| [T58](tests/T58-gap-phantom-equivalence.md) | Gap-phantom equivalence audit | C1, D1-Field, T56 | implemented: H0(G) matches phantom incomparability witnesses for the tested T51/T52 well-formed extension cases; local reversal control shows F(U) subset A(U) is required |
| [T131](tests/T131-bell-test-h1-mapping.md) | Bell-test-to-H1 mapping | Q1, D1, R1, T13, T21 | in progress: resolves the former duplicate T58 Bell/H1 mapping track separately from T58 gap-phantom equivalence |
| [T111](tests/T111-d1-gauge-invariance-audit.md) | D1 gauge-invariance audit | D1, D1-Field, GU roadmap, finality gauge problem | implemented: pure observer/record/holder/causal relabeling preserves all four D1 dimensions; access-boundary refinement/coarsening are covariant boundary data, not gauge; hostile controls are undefined |
| [T112](tests/T112-spin-observerse-holonomy-step2.md) | Spin-observerse holonomy Step 2 | T63, T65, C1, D1, GU roadmap | implemented: finite/proxy Y_spin audit passes under H3 and a declared positive-generator spin-lift convention while preserving naive-Y, signed-angle, non-LC holonomy +1, and representative-dependence controls |
| [T113](tests/T113-gap-presheaf-classification.md) | Gap presheaf classification | C1, D1-Field, T51-T58, GU roadmap | implemented: raw H0(G) is too broad (13 raw gaps vs 10 phantoms), but the endpoint-accessible canonical well-formed local-incomparability subobject exactly matches phantom witnesses in the tested finite family |
| [T59](tests/T59-finite-to-infinite-boundary-audit.md) | Finite-to-infinite boundary audit | CSP-PO1, PO1, S1, Q1, H7, HEF | implemented: Mobius orientation witness separates transition-aware Z2 parity success from coefficient-blind scalar false global section; continuous-domain parity claims require coefficient and transition data |
| [T62](tests/T62-noisy-measurement-access-boundary.md) | Noisy measurement access-boundary discriminator | Q1, D1, T2, T22 | implemented: noisy channel-level matrix separates decoherence, Quantum-Darwinism redundancy, and observer-relative finality; Q1 weakened to access-boundary discriminator |
| [T64](tests/T64-stern-gerlach-access-window.md) | Stern-Gerlach detector access-window discriminator | Q1, D1, T2, T22, T62 | implemented: detector-fragment proxy preserves access-boundary distinction but weakens Q1 through threshold sensitivity; no-signalling guardrail passes |
| [T66](tests/T66-povm-detector-calibration-obstruction.md) | POVM detector calibration obstruction | Q1, D1, T64 | implemented: explicit POVM response matrices replace declared reliabilities, but threshold and provenance rules remain external; no-signalling guardrail passes |
| [T67](tests/T67-povm-correlation-provenance-obstruction.md) | POVM correlation provenance obstruction | Q1, D1, T66 | implemented: passive pairwise detector correlation cannot recover the D1 independence partition; copied and independent channels can be correlation-equivalent |
| [T68](tests/T68-intervention-sensitive-detector-provenance.md) | Intervention-sensitive detector provenance | Q1, D1, T67 | implemented: identical passive detector statistics separate under pre-registered intervention/provenance metadata; D1 is computed only after the partition is fixed |
| [T70](tests/T70-detector-provenance-robustness.md) | Detector provenance robustness | Q1, D1, T68 | implemented: T68 survives moderate single-channel metadata degradation but fails cleanly when trusted provenance channels are absent or threshold-dependent |
| [T72](tests/T72-physical-provenance-protocol.md) | Physical provenance protocol | Q1, D1, T70 | implemented: interval/probability protocol parameters classify robust recovery, withhold, threshold failure, false independence risk, and false dependence risk |
| [T74](tests/T74-provenance-protocol-monte-carlo.md) | Provenance protocol Monte Carlo | Q1, D1, T72 | implemented: Monte Carlo stress priors show robust detector provenance recovery is confined to a narrow engineered corner |
| [T75](tests/T75-real-detector-stack-provenance.md) | Real detector stack provenance mapping | Q1, D1, T74 | implemented: HydraHarp/White Rabbit/signed archive maps into robust recovery; unsigned-control variant withholds |
| [T76](tests/T76-measured-detector-provenance-posterior.md) | Measured detector provenance posterior | Q1, D1, T75 | implemented: deployment evidence schema preserves signed-versus-unsigned separation only for measured provenance protocols |
| [T77](tests/T77-measured-detector-policy-sensitivity.md) | Measured detector policy sensitivity | Q1, D1, T76 | implemented: signed fixture stays robust across policy corridors, but permissive policy leaks unsigned false positives |
| [T78](tests/T78-preregistered-detector-deployment-protocol.md) | Pre-registered detector deployment protocol | Q1, D1, T76, T77 | implemented: only pre-registered real-log runs are admissible for detector-branch upgrades |
| [T79](tests/T79-dashboard-summary-nonidentifiability.md) | Dashboard summary nonidentifiability | Q1, D1, T76, T78 | implemented: identical coarse dashboards can hide opposite provenance verdicts, so raw logs are load-bearing |
| [T81](tests/T81-measured-schema-ablation.md) | Measured schema ablation | Q1, D1, T76-T79 | implemented: trust boundaries and pre-registration are load-bearing in the current detector audit; other declared categories are not independently decisive yet |
| [T83](tests/T83-q1-detector-null-criterion.md) | Q1 detector null criterion | Q1, D1, T66-T81 | implemented: report-only synthesis narrowing the detector branch to a provenance-admissibility filter unless a pre-registered raw-log protocol beats passive-statistics, dashboard, and post hoc partition nulls |
| [T85](tests/T85-measured-detector-channel-dominance.md) | Measured detector channel dominance | Q1, D1, T76-T83 | implemented: spoof/unique-tag stress can still demote the signed fixture, but perturbation and DAG channels are not independently decisive once trust and pre-registration are fixed |
| [T86](tests/T86-ambiguous-tag-channel-independence.md) | Ambiguous-tag channel independence | Q1, D1, T76-T85 | implemented: clean perturbation-only and signed-DAG-only fixtures rescue ambiguous timing/tag controls, while contaminated controls withhold |
| [T87](tests/T87-real-run-raw-log-contract.md) | Real-run raw-log contract | Q1, D1, T76-T86 | implemented: event-level raw-log admission contract for future detector deployments; no D1 scoring or empirical upgrade without the required tables |
| [T95](tests/T95-detector-stack-export-map.md) | Detector stack export map | Q1, D1, T75, T87, T94 | implemented: HydraHarp/White Rabbit native timing and signed archive alone fail T87; only an augmented pre-registered export map is admissible, and only as a plan until real event rows exist |
| [T96](tests/T96-detector-feasibility-checklist.md) | Detector feasibility checklist | Q1, D1, T87, T95 | implemented: surviving detector route is a governance-heavy dry-run program carried by control manifests, ambiguity challenges, perturbation trials, trust audits, and demotion rules rather than native timing |
| [T97](tests/T97-detector-dry-run-packet-skeleton.md) | Detector dry-run packet skeleton | Q1, D1, T87, T95, T96 | implemented: schema-complete pre-data packet scaffold is executable but not evidence; placeholder scoring, schema drift, post hoc packet assembly, and missing hostile controls withhold Q1 |
| [T100](tests/T100-detector-authority-domain-bound.md) | Detector authority-domain bound | Q1, D1, T97, T98 | implemented: current detector packet requires at least four non-conflicting authority domains; no two- or three-domain profile survives |
| [T121](tests/T121-real-detector-packet-schema-audit.md) | Real detector packet schema audit | Q1, D1, T87, T97, T100 | implemented: minimal detector evidence packet separates raw payload validity from packet admissibility and future operation availability; no detector-claim promotion |
| [T123](tests/T123-same-payload-packet-foa-witness.md) | Same-payload packet FOA witness | Q1B, D1, T87, T97, T100, T121 | implemented: same raw payload, immediate result, and coarse detector summary can still differ in admissibility and future operation availability through packet wrapper fields |
| [T133](tests/T133-detector-packet-tiered-minimality.md) | Detector packet tiered minimality | Q1B, D1, T121, T123 | implemented: detector packet burden splits into provisional-admission core plus stricter claim-review extension; weakens any flat all-fields-at-once reading |
| [T134](tests/T134-detector-dry-run-tier-gate.md) | Detector dry-run tier gate | Q1B, D1, T97, T121, T123, T133 | implemented: T97 raw-log rows are necessary but not sufficient; T121/T133 wrapper fields are required before provisional admission or claim-review readiness |
| [T136](tests/T136-detector-preregistration-manifest.md) | Detector pre-registration manifest | Q1B, D1, T97, T100, T121, T133, T134 | implemented: pre-event manifest must bind table hashes, wrapper commitments, authority separation, claimed tier, no-data boundary, and top-level hash |
| [T138](tests/T138-detector-manifest-workflow-fit.md) | Detector manifest workflow fit | Q1B, D1, T100, T121, T133, T136 | implemented: common single-lab and merged-authority archive workflows are null; only a federated pre-data scaffold clears T136, still without detector evidence |
| [T132](tests/T132-weak-measurement-nonnull-criterion.md) | Weak-measurement non-null criterion | Q1, T12 | implemented: executable finite gate rejects same-record, post hoc, constant-branch, and monotone-proxy weak-measurement routes; only a verdict-changing independent measured axis survives as a candidate shape |
| [T90](tests/T90-weak-measurement-reparameterization-obstruction.md) | Weak-measurement reparameterization obstruction | Q1, T12, T83, T132 | implemented: weak-measurement route is non-null only if an independent pre-registered axis changes the TaF verdict while standard monitored statistics are held fixed |
| [T91](tests/T91-weak-measurement-platform-audit.md) | Weak-measurement platform audit | Q1, T12, T90 | implemented: superconducting homodyne, uncollapse, and quantum-jump reversal platforms fail the independent-axis gate; duplicated-record provenance or pre-metered undo cost remains blocked |
| [T93](tests/T93-weak-measurement-undo-cost-independence.md) | Weak-measurement undo-cost independence | Q1, T12, T90, T91 | implemented: undo-cost route is non-null only for a calibrated independent meter that changes the TaF verdict with standard monitored statistics fixed |
| [T130](tests/T130-weak-measurement-dual-meter-screen.md) | Weak-measurement dual-meter screen | Q1C, T12, T90, T91, T93, T132 | open: renumbered from the duplicate T115 weak-measurement dual-meter screen; screens whether any real simultaneous second meter clears the independent-axis gate |
| [T19](tests/T19-phenomenal-bridge-complexity-separation.md) | Phenomenal bridge as complexity separation | C1, D1, D2, H6 | implemented: 7-node finite graph shows FIRST-PERSON-FINALITY(A*(R)) = NO, THIRD-PERSON-FINALITY(G) = YES; causal-boundary obstruction, not computational undecidability; T60+T19 gives formal content of H6 |
| [T92](tests/T92-accessible-witness-gap-restriction.md) | Accessible-witness gap restriction | C1, T19, T58, T89 | implemented: T19 unary proposition gap and non-chain joint-witness gap satisfy restriction closure under ambient restriction, audit monotonicity, and stable proposition typing; semantic relabeling and audit-monotonicity controls fail |
| [T65](tests/T65-causal-reduction-holonomy.md) | Causal reduction of CHSH holonomy | C1, D1, H6, T63, T19 | implemented: LC => holonomy = +1 (all 16 LC sections); quantum => holonomy = -1 (Bell's theorem as holonomy); biconditional disproved (128 ≠ 16); spatial causal-boundary obstruction formally parallels T19 temporal obstruction |
| [T69](tests/T69-losskernel-failure-type.md) | LossKernel failure type monotonicity | TF1, T19, T56, T58, T63, T65 | implemented finite-fixture result: failure-type monotonicity holds only under the declared coefficient/support semantics and allowed loss morphisms; external review blocks any general Cech/sheaf theorem reading; 7/7 tests pass |
| [T73](tests/T73-losskernel-composition.md) | LossKernel composition and path-dependence biconditional | T34, T37, T69, TF1 | implemented: composition law verified as powerset-union monoid-valued annotation; path-dependence biconditional established on fixed-endpoint fixtures; quotient/prior-art gate still open; 17/17 tests pass |
| [T99](tests/T99-losskernel-quotient-separation.md) | LossKernel quotient separation | TF1, T34, T37, T73 | implemented: label-only LossKernel fails same-endpoint/same-map/same-behavior/same-label quotient survival; witness-carrying LossKernel separates only with source-anchored obligations |
| [T101](tests/T101-q1-branch-adjudication.md) | Q1 branch adjudication | Q1, D1, T2, T21, T22, T62, T66-T100 | implemented: Q1 should split before paper language; no current branch earns new measurement dynamics or empirical quantum support |
| [T102](tests/T102-q1a-neighbor-comparison.md) | Q1A neighbor comparison gate | Q1A, Q1, T2, T22, T62, T64, T101 | implemented: Q1A is only access-boundary and independence accounting unless a fixed-data witness separates it from standard neighbor frameworks |
| [T103](tests/T103-q1a-fixed-data-witness.md) | Q1A fixed-data witness | Q1A, Q1, D1, T102 | implemented: fixed standard quantum-side data can yield different D1 verdicts only through the independence partition; external distinctness remains unearned |
| [T118](tests/T118-q1a-reversal-cost-collapse.md) | Q1A reversal-cost collapse | Q1A, Q1, D1, T103, T105, T109 | implemented: in the current fixed-data family reversal cost collapses to the audited accessible-support count and adds no independent verdict content |

## Minimum Compatibility Constraints

Any formalization must:

- preserve no-signalling;
- preserve proper time and invariant interval structure;
- distinguish physical record-stability from human belief;
- distinguish local access loss from physical reversal;
- not treat decoherence as a complete measurement-problem solution;
- not derive the thermodynamic arrow by assertion;
- not require a hidden universal present;
- not treat probabilistic consensus finality as absolute truth.
- not deny remote observation as causal record access.
- not treat observer rendering as mind-created matter.

## Executable Suite

```bash
python -m unittest discover -s tests -p "test_*.py" -v
python -m models.run_t1
python -m models.run_t2
python -m models.run_emergence_lab
python -m models.run_t16
python -m models.run_t17
python -m models.run_t18
python -m models.run_t80
python -m models.run_t81
python -m models.run_t82
python -m models.run_t84
python -m models.run_t106
python -m models.run_t110
python -m models.run_t116
python -m models.run_t122
python -m models.run_t124
python -m models.run_t128
python -m models.run_t142
python -m models.run_t114
python -m models.run_t115
python -m models.run_t117
python -m models.run_t119
python -m models.run_t129
python -m models.run_t111_d1_gauge_invariance
python -m models.run_t112_spin_observerse_holonomy_step2
python -m models.run_t113
python -m models.run_t20
python -m models.run_t21
python -m models.run_t22
python -m models.run_t23
python -m models.run_t24
python -m models.run_t25
python -m models.run_t26
python -m models.run_t27
python -m models.run_t28
python -m models.run_t29
python -m models.run_t30
python -m models.run_t31
python -m models.run_t32
python -m models.run_t33
python -m models.run_t34
python -m models.run_t35
python -m models.run_t36
python -m models.run_t37
python -m models.run_t38
python -m models.run_t39
python -m models.run_t40
python -m models.run_t41
python -m models.run_t42
python -m models.run_t43
python -m models.run_t44
python -m models.run_t46
python -m models.run_t47
python -m models.run_t48
python -m models.run_t49
python -m models.run_t50
python -m models.run_t51
python -m models.run_t52
python -m models.run_t53
python -m models.run_t54
python -m models.run_t55
python -m models.run_t57
python -m models.run_t58
python -m models.run_t59
python -m models.run_t62
python -m models.run_t64
python -m models.run_t70
python -m models.run_t72
python -m models.run_t74
python -m models.run_t75
python -m models.run_t76
python -m models.run_t77
python -m models.run_t78
python -m models.run_t79
python -m models.run_t85
python -m models.run_t86
python -m models.run_t87
python -m models.run_t95
python -m models.run_t96
python -m models.run_t97
python -m models.run_t100
python -m models.run_t121
python -m models.run_t123
python -m models.run_t133
python -m models.run_t134
python -m models.run_t136
python -m models.run_t138
python -m models.run_t90
python -m models.run_t91
python -m models.run_t93
python -m models.run_t101
python -m models.q1a_neighbor_comparison
python -m models.run_t103
python -m models.run_t92
python -m models.t19_phenomenal_bridge_separation
python -m models.t65_causal_reduction
```

The suites use only Python's standard library. Evidence records:

- [T1 v0.1 Results](results/T1-v0.1-results.md)
- [Quantum Measurement Finality v0.1 Results](results/quantum-measurement-finality-v0.1-results.md)
- [Emergence Laboratory v0.1 Results](results/emergence-lab-v0.1-results.md)
- [Spacetime Aggregation v0.1 Results](results/spacetime-aggregation-v0.1-results.md)
- [Consensus Finality Crosswalk v0.1 Results](results/consensus-finality-crosswalk-v0.1-results.md)
- [Finality Direction Theorem v0.1 Results](results/finality-direction-theorem-v0.1-results.md)
- [Reversible Finality Nonmonotonicity v0.1 Results](results/reversible-finality-nonmonotonicity-v0.1-results.md)
- [Persistent Reconciler Cost Boundary v0.1 Results](results/persistent-reconciler-cost-boundary-v0.1-results.md)
- [Cyclic Reconciler Entropy Export v0.1 Results](results/cyclic-reconciler-entropy-export-v0.1-results.md)
- [Bounded-Sink Reversible Compression v0.1 Results](results/bounded-sink-reversible-compression-v0.1-results.md)
- [Finite-Permutation Monotone Obstruction v0.1 Results](results/finite-permutation-monotone-obstruction-v0.1-results.md)
- [Open Markov Record-Entropy Comparison v0.1 Results](results/open-markov-record-entropy-v0.1-results.md)
- [Stationary Markov Monotone Obstruction v0.1 Results](results/stationary-markov-monotone-obstruction-v0.1-results.md)
- [Constructor-Admissibility Grounding Audit v0.1 Results](results/constructor-admissibility-grounding-audit-v0.1-results.md)
- [Minimal Living Arrow v0.1 Results](results/minimal-living-arrow-v0.1-results.md)
- [Thermodynamic Erasure Calibration v0.1 Results](results/thermodynamic-erasure-calibration-v0.1-results.md)
- [Viability Filter v0.1 Results](results/viability-filter-v0.1-results.md)
- [Maintenance-Cost Viability Split v0.1 Results](results/maintenance-viability-split-v0.1-results.md)
- [Accessible State Space Separation v0.1 Results](results/accessible-state-space-separation-v0.1-results.md)
- [Future Operation Availability Residue v0.1 Results](results/future-operation-availability-residue-v0.1-results.md)
- [Future Capability Preservation Audit v0.1 Results](results/future-capability-preservation-audit-v0.1-results.md)
- [D1 Gauge-Invariance Audit v0.1 Results](results/d1-gauge-invariance-audit-v0.1-results.md)
- [Spin-Observerse Holonomy Step 2 v0.1 Results](results/spin-observerse-holonomy-step2-v0.1-results.md)
- [Gap Presheaf Classification v0.1 Results](results/gap-presheaf-classification-v0.1-results.md)
- [Consensus-Record Theorem Transfer v0.1 Results](results/consensus-record-theorem-transfer-v0.1-results.md)
- [Bell Contextuality Finality v0.1 Results](results/bell-contextuality-finality-v0.1-results.md)
- [D1 Physical Reduction Map v0.1 Results](results/d1-physical-reduction-map-v0.1-results.md)
- [Invariant-Preserving Transformations v0.1 Results](results/invariant-preserving-transformations-v0.1-results.md)
- [D1 Multiscale Observer Field v0.1 Results](results/d1-multiscale-observer-field-v0.1-results.md)
- [Minimal D1 Generalization v0.1 Results](results/minimal-d1-generalization-v0.1-results.md)
- [D1 Restriction System v0.1 Results](results/d1-restriction-system-v0.1-results.md)
- [GU Class-Relative Bridge v0.1 Results](results/gu-class-relative-bridge-v0.1-results.md)
- [CAP Theorem Bridge v0.1 Results](results/cap-theorem-bridge-v0.1-results.md)
- [Projection-Obstruction Schema v0.1 Results](results/projection-obstruction-schema-v0.1-results.md)
- [Cross-Domain Projection-Obstruction Validation v0.1 Results](results/cross-domain-projection-obstruction-validation-v0.1-results.md)
- [PO1 Admissibility Conditions v0.1 Results](results/po1-admissibility-conditions-v0.1-results.md)
- [PO1 Admissibility Derivation v0.1 Results](results/po1-admissibility-derivation-v0.1-results.md)
- [PO1 Chained Projection v0.1 Results](results/po1-chained-projection-v0.1-results.md)
- [Compression-Finality Crosswalk v0.1 Results](results/compression-finality-crosswalk-v0.1-results.md)
- [Projection-Obstruction Discovery Engine v0.1 Results](results/projection-obstruction-discovery-engine-v0.1-results.md)
- [Typed Transport Network v0.1 Results](results/transport-network-v0.1-results.md)
- [CSP Satisfiability Reframing v0.1 Results](results/csp-satisfiability-reframing-v0.1-results.md)
- [Holarchy Lab v0.1 Results](results/holarchy-lab-v0.1-results.md)
- [Typed Transport Category v0.1 Results](results/typed-transport-category-v0.1-results.md)
- [Local Persistence and Reconciliation Split v0.1 Results](results/local-persistence-reconciliation-split-v0.1-results.md)
- [Local Persistence Mechanisms v0.1 Results](results/local-persistence-mechanisms-v0.1-results.md)
- [Local Mechanism Identifiability v0.1 Results](results/local-mechanism-identifiability-v0.1-results.md)
- [Open Causal Scarcity and Closed Synchronization Boundary v0.1 Results](results/open-causal-scarcity-synchronization-boundary-v0.1-results.md)
- [PO1 DAG Theorem v0.1 Results](results/po1-dag-theorem-v0.1-results.md)
- [FinaliEvent Structure v0.1 Results](results/finali-event-structure-v0.1-results.md)
- [Reconstruction Without Background Time v0.1 Results](results/reconstruction-without-background-time-v0.1-results.md)
- [Axis Monotonicity Theorem v0.1 Results](results/axis-monotonicity-theorem-v0.1-results.md)
- [Multi-Observer Apparent Finality Colimit v0.1 Results](results/multi-observer-apparent-finality-colimit-v0.1-results.md)
- [Symmetric Colimit Theorem v0.1 Results](results/symmetric-colimit-theorem-v0.1-results.md)
- [Observer-Colimit Descent Boundary v0.1 Results](results/observer-colimit-descent-boundary-v0.1-results.md)
- [Finite Finality Descent Theorem v0.1 Results](results/finite-finality-descent-theorem-v0.1-results.md)
- [Conflict-Enriched FinaliEvent Descent v0.1 Results](results/conflict-finalievent-descent-v0.1-results.md)
- [Finality Reflection Property v0.1 Results](results/finality-reflection-property-v0.1-results.md)
- [Gap-Phantom Equivalence v0.1 Results](results/gap-phantom-equivalence-v0.1-results.md)
- [Finite-to-Infinite Boundary Audit v0.1 Results](results/finite-to-infinite-boundary-audit-v0.1-results.md)
- [Noisy Measurement Access-Boundary v0.1 Results](results/noisy-measurement-access-boundary-v0.1-results.md)
- [Stern-Gerlach Access-Window v0.1 Results](results/stern-gerlach-access-window-v0.1-results.md)
- [Detector Provenance Robustness v0.1 Results](results/detector-provenance-robustness-v0.1-results.md)
- [Physical Provenance Protocol v0.1 Results](results/physical-provenance-protocol-v0.1-results.md)
- [Provenance Protocol Monte Carlo v0.1 Results](results/provenance-protocol-monte-carlo-v0.1-results.md)
- [Real Detector Stack Provenance v0.1 Results](results/real-detector-stack-provenance-v0.1-results.md)
- [Measured Detector Provenance Posterior v0.1 Results](results/measured-detector-provenance-posterior-v0.1-results.md)
- [Measured Detector Policy Sensitivity v0.1 Results](results/measured-detector-policy-sensitivity-v0.1-results.md)
- [Pre-Registered Detector Deployment Protocol v0.1 Results](results/preregistered-detector-deployment-protocol-v0.1-results.md)
- [Dashboard Summary Nonidentifiability v0.1 Results](results/dashboard-summary-nonidentifiability-v0.1-results.md)
- [Measured Schema Ablation v0.1 Results](results/measured-schema-ablation-v0.1-results.md)
- [Q1 Detector Null Criterion v0.1 Technical Report](TECHNICAL-REPORT-q1-detector-null-criterion-v0.1.md)
- [Measured Detector Channel Dominance v0.1 Results](results/measured-detector-channel-dominance-v0.1-results.md)
- [Ambiguous-Tag Channel Independence v0.1 Results](results/ambiguous-tag-channel-independence-v0.1-results.md)
- [Real-Run Raw-Log Contract v0.1 Results](results/real-run-raw-log-contract-v0.1-results.md)
- [Detector Stack Export Map v0.1 Results](results/detector-stack-export-map-v0.1-results.md)
- [Detector Feasibility Checklist v0.1 Results](results/detector-feasibility-checklist-v0.1-results.md)
- [Detector Dry-Run Packet Skeleton v0.1 Results](results/detector-dry-run-packet-skeleton-v0.1-results.md)
- [Detector Authority-Domain Bound v0.1 Results](results/detector-authority-domain-bound-v0.1-results.md)
- [Real Detector Packet Schema Audit v0.1 Results](results/real-detector-packet-schema-audit-v0.1-results.md)
- [Same-Payload Packet FOA Witness v0.1 Results](results/same-payload-packet-foa-witness-v0.1-results.md)
- [Detector Packet Tiered Minimality v0.1 Results](results/detector-packet-tiered-minimality-v0.1-results.md)
- [Detector Dry-Run Tier Gate v0.1 Results](results/detector-dry-run-tier-gate-v0.1-results.md)
- [Detector Pre-registration Manifest v0.1 Results](results/detector-preregistration-manifest-v0.1-results.md)
- [Detector Manifest Workflow Fit v0.1 Results](results/detector-manifest-workflow-fit-v0.1-results.md)
- [Weak-Measurement Reparameterization Obstruction v0.1 Results](results/weak-measurement-reparameterization-obstruction-v0.1-results.md)
- [Weak-Measurement Platform Audit v0.1 Results](results/weak-measurement-platform-audit-v0.1-results.md)
- [Weak-Measurement Undo-Cost Independence v0.1 Results](results/weak-measurement-undo-cost-independence-v0.1-results.md)
- [Accessible-Witness Gap Restriction v0.1 Results](results/accessible-witness-gap-restriction-v0.1-results.md)
- [T19 Phenomenal Bridge Separation Step 1 Results](tests/T19-phenomenal-bridge-complexity-separation.md)
- [T65 Causal Reduction of CHSH Holonomy Step 1 Results](tests/T65-causal-reduction-holonomy.md)
- [LossKernel Quotient Separation v0.1 Results](results/losskernel-quotient-separation-v0.1-results.md)
- [Q1 Branch Adjudication v0.1 Results](results/q1-branch-adjudication-v0.1-results.md)
- [Q1A Neighbor Comparison v0.1 Technical Report](TECHNICAL-REPORT-q1a-neighbor-comparison-v0.1.md)
- [Q1A Fixed-Data Witness v0.1 Results](results/q1a-fixed-data-witness-v0.1-results.md)

## How To Add A Test

Create a file under `tests/` with:

```md
# T#: Test Name

## Target Claims

## Setup

## Success Criteria

## Failure Criteria

## Known Physics Constraints

## Contribution Needed
```
