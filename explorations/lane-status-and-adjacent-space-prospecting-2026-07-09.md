# Lane status ledger + adjacent-space prospecting

2026-07-09. Reframes the session's outcomes under one principle, and maps the adjacent space the
distributed-systems <-> quantum-finality correspondence opens.

## Principle (governs this ledger)

**Only actual falsification closes a lane.** "Not worth it right now" is a *prioritization* judgment, not
a *closure* judgment, and belongs to the prioritizing system (CapacityOS/JoeOps dispatch/review), not to a
kill in the analysis layer. So below, `SHUT` means *refuted as stated*; everything else is
`OPEN (deprioritized)` with a wake condition. Prior swings over-used "dead" for lanes that were merely
absorbed, not-novel-as-stated, or not-worth-now; those are re-opened here.

## Reclassification of session verdicts

### Actually SHUT (falsified as stated -- terminal for that exact claim only)

| claim (as stated) | why shut |
|---|---|
| no-signaling is the *defining* invariant of the band | flat across all scenarios (computation); separates nothing. (No-signaling as a *background property* is still true.) |
| CRDT commutativity coincides with band-exit (#15) | measured *anti*-correlated; band-exit makes recoveries MORE non-commutative |
| swap is an *empirical* discriminator vs decoherence (P3) | both ledgers reproduce identical observable statistics -- proven non-discriminating |
| "smallest irreversible quorum" is *the scalar* order parameter (P5) | T17 scalar-insufficiency; the cardinality reading is non-monotone across BFT/Shamir |
| correlation-without-control is a *necessary defining face* | flat everywhere (measurement) |

Each is shut only *as precisely worded*; the broader idea it came from may live below.

### OPEN (deprioritized) -- NOT shut; parked with a wake condition

| lane | prior (wrong) label | actual status | wake condition |
|---|---|---|---|
| finality dual to no-cloning (copy-law, B) | "dead" | the specific J+R conservation is falsified; the framing is not | a different conserved/priced quantity; the quantum->DS transfer |
| arrow / time-as-finality (D) | "dead" | the ABL pre/post-swap probe is shut; the North Star is manifestly open | a non-ABL asymmetry; a constructor-theoretic time asymmetry; a new fixture |
| graded interior (E) | "dead" | not shut -- grading is real but lives on the *algebra-widening* axis, not intrinsic | define grading over an admissible-algebra family (F's axis) |
| band relativity / gauge-over-algebra (F) | "dead" | CRDT mechanism shut; "band depends on the admissible algebra" (Bohr/Rovelli) is unrefuted and supported by E | a mechanism other than commutativity |
| CAP/FLP <-> Bell no-go | "conditional/thin" | OPEN frontier (see prospecting) | the non-healable-asynchrony FLP test; read arXiv 2602.18723 |
| DS <-> quantum bridge (generative) | (deflated) | OPEN -- a discriminating map that correctly found the one deep bridge | pick a new question it generates; attempt a transfer |

## Adjacent-space prospecting (literature check, run as prospecting not gatekeeping)

Four corners of the correspondence, with what the literature actually shows:

1. **Quantum Darwinism (redundancy R) <-> replication / eventual consistency -- OPEN, strongest lead.**
   Zurek's own framing already speaks in distributed-systems terms: redundant *copies* proliferate, the
   environment is a *communication channel*, and many observers *independently* access fragments and *reach
   consensus*. But the searched literature does **not** draw the formal/quantitative correspondence
   (redundancy plateau <-> replication factor / eventual-consistency convergence). The vocabulary is aligned
   and the bridge is unbuilt -- a genuine open adjacent space. Sources: Zurek quantum Darwinism reviews
   (arXiv quant-ph/0308163; PMC9689795); redundancy quantification (arXiv 1703.10096).

2. **CAP / FLP <-> Bell / no-signaling -- OPEN but an ACTIVE frontier (significant, not insignificant).**
   A 2026 paper draws exactly this: FLP, Halpern-Moses, and CAP framed as *conditional* impossibilities on a
   shared "unilateral-message / locality" primitive, structurally paralleled with Bell's theorem ("What
   Distributed Computing Got Wrong", arXiv 2602.18723). And monogamy of Bell violations is derivable from
   no-signaling (arXiv 0810.1175). So the bridge is live and being published *right now* -- which is
   evidence it is significant. Our finality/monogamy angle may differ from the causality-primitive angle;
   read 2602.18723 before investing.

3. **Monogamy / shareability <-> access structures / secret sharing -- ESTABLISHED (known bridge).**
   Quantum secret sharing (Cleve-Gottesman-Lo) and access structures already are this correspondence. Real
   and useful; not novel. This is the strut that survived our stress tests -- and it survived *because* it
   is a genuine deep bridge.

4. **Monogamy bounds <-> Byzantine fault-tolerance thresholds -- LIKELY OPEN (as a correspondence).**
   "Quantum-aided Byzantine agreement" is an established field, but it *uses* entanglement as a tool to
   solve consensus; the searched literature does **not** address monogamy-of-entanglement as a structural
   *explanation* of fault-tolerance bounds. The reverse/structural direction we care about looks unoccupied.
   Tantalizing-but-suspect datum: the qubit 2-shareability wall is 2/3 and classical BFT needs >2/3 honest
   nodes -- possibly shared monogamy structure, possibly a parametrization coincidence (the qutrit wall did
   not land on 2/3). Worth one check. Sources: Quantum Byzantine agreement (Wikipedia; arXiv 2207.04939).

## Handoff

None of the OPEN lanes above are closed; they are deprioritized with wake conditions for the prioritizing
system to weigh. The two highest-prospect new questions the map generates: (1) build the redundancy <->
replication correspondence quantitatively (corner 1, apparently unbuilt); (2) attempt a *reverse transfer* --
use a monogamy bound to derive a distributed fault-tolerance limit (corner 4). Either, if it transfers,
converts the bridge from analogy to discovery.
