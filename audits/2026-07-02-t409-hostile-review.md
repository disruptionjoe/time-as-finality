# T409 Hostile Review — Capability Restoration Frontier

Status: repo-local hostile-review record. No claim promotion; no
CLAIM-LEDGER edits; no TESTS.md edits by this pass.

Date: 2026-07-02.

Artifact under review: `T409-capability-restoration-frontier-v0.1`
(spec `tests/T409-capability-restoration-frontier.md`, model
`models/capability_restoration_frontier.py`, tests
`tests/test_capability_restoration_frontier.py`, results
`results/T409-capability-restoration-frontier-v0.1-results.md` + `.json`).

Three independent hostile lenses were run. Each reproduced the artifact
end-to-end before attacking it. Per the tri-repo three-tier vocabulary
("Coordination - Tri-Repo Division of Labor.md"): T409 entered this review
at tier 1, **recorded**.

---

## Lens 1 — Numerical reproduction from scratch

**Verdict: survives-with-corrections. Reproduced: yes.**

Evidence (condensed; full trail in the review record):

- Test suite rerun: 36 passed (5.9 s on the review machine); combined with
  neighbor suites T392/T393/T408/T142: 124 passed — matching the results
  file exactly. Model rerun reproduces `frontier_holds = True`, all three
  legs, `r_feas = r_cert = [1..7]` at `theta = pi`, the full graded table
  (`d = {7,3,1,1,0,0,0,0}`, `u_min_cert = {64,29,16,10,3,1,1,1}`).
- Independent from-scratch reproduction with the reviewer's OWN statevector
  simulator (no imports from `models/`, variable qubit count, own gate
  application / partial trace / trace norm, own seed): `vis_A = 4 sqrt(3)/7`
  re-derived by hand; `achieved = vis_A cos(theta/2)^u` verified across
  5 thetas x n in {3,5,7} x all reach sizes (max error 6.7e-16); the entire
  56-cell `r_feas` table matches `max(0, n - d)`; phi-independence verified
  over 40 RANDOM phases (not the predeclared 6) plus 300-sample random
  rank-8 Kraus channel searches on certified cells (zero violations); the
  trace-norm bound derivation re-checked algebraically (Hoelder + CPTP
  contractivity) and confirmed valid; work-invariance verified for three
  sigmas including a mixed state (stronger than the model's |0>-only
  assertion); correspondence rows, Holevo values, edges (0.273195 pi,
  0.699519 pi), Q1D teeth (3/7), contrast probes, and ledger entries all
  reproduced digit-for-digit at the structural level.

Fatal findings: none.

Non-fatal findings:

1. Sub-epsilon diagnostics are environment-specific and do not
   bit-reproduce (90 ULP-level JSON diffs). Three bolded results-md values
   fail verbatim reproduction: manufactured-coherence locked 6.9e-17
   (rerun 5.7e-17), frontier-with-work max diff 4.9e-32 (rerun 0.0), worst
   complementarity residual "<= 9.8e-15" (rerun 1.11e-14 — slightly ABOVE
   the printed worst). All 4-7 orders below the predeclared tolerances;
   no verdict affected; must be restated as noise-level.
2. The theta = pi phi-independence certificate is a finite-precision
   assertion presented with the word "exactly"; independently backed by
   the rigorous trace-norm bound, so no teeth lost — language note.
3. Suite runtime ~4 s in the md vs 5.9 s on the review machine — trivial,
   inside budget.
4. `vis_A` prose rounding (0.989743 vs 0.9897433186...) — rounding only.

## Lens 2 — Conceptual relocation (T398/T401/T404-style absorption attack)

**Verdict: survives-with-corrections. Reproduced: yes.**

Evidence (condensed): full rerun (36 + 124 passed, identical tables);
independent re-derivation with the reviewer's own simulator confirming
(A) the M=0 state at `theta = pi` is EXACTLY a two-branch GHZ-type state
(2 nonzero amplitudes, weights 4/7 and 3/7, confirmed n = 1,3,5,7);
(B) exhaustive proper-subset phi-independence; (C) the closed forms;
(D) deficit `= 1 - cos(theta/2)^(2u) = D^2` — the Englert-Greenberger-Yasin
duality identity, verified by two-line overlap algebra; (E) bound = exactly
2x achieved; (F) the leg-2 lemma mechanism; plus a three-pass prior-art
search (Gregoratti-Werner quant-ph/0504195; arXiv:1502.07030
half-environment recovery; QD redundancy literature).

Fatal findings (relocations of verdict-language; the lens verdict is
survives-with-corrections because the artifact survives ONCE RE-SCOPED —
these findings kill the framing, not the computed content):

1. **"Reach" is a declared bookkeeping boundary, graded — not yet
   physical.** In the closed 10-qubit unitary model nothing dynamical
   prevents access to the "unreached" bath qubits; the menu restriction is
   stipulated per r — the same status as T407's declared boundary. The
   completed-description kill applies: at `theta = pi` every
   phi-independence certificate is the textbook fact that a proper
   subsystem of a GHZ state carries no phase information. The
   verdict-language "the bounded-region premise ... made physical" and
   "Tier-2 forcing earned" must be dropped: T407's standing objection
   (declared vs physical boundary) is NOT discharged; the physical-escape
   mechanism is exactly the named-unbuilt Hamiltonian rung. What survives
   redescription: the FUNCTION dynamics -> r (cnot n, swap 1,
   uncorrelated 0) is dynamics-indexed and partition-covariant, so the
   frontier's dependence on the interaction family is real content; the
   boundary axis itself is not.
2. **Leg 2's predeclared failure leg was mathematically unfireable**
   (phi-independent input + any CPTP map + any phi-independent ancilla =
   phi-independent output is provable before any code runs) —
   predeclaration theater, not an experiment. "Work does not substitute
   for reach" holds only because the menu forbids work buying reach by
   fiat; in any Hamiltonian/transport model the physically interesting
   substitution is that work BUYS reach. Leg 2 is unitarity/data-processing
   in Tier-2 costume; its promotion to "the sharp form of priced in reach,
   not work" must be downgraded.
3. **The physics content of all three legs is standard**, triggering the
   spec's own re-scope clause. Leg 1 at `theta = pi` is GHZ subsystem
   counting; the graded surface is the standard decoherence-factor
   product (one closed form); Leg 3's headline correspondence is EXACTLY
   the Englert-Greenberger-Yasin duality `V^2 + D^2 = 1` in this family —
   and duality is NOT in the artifact's flagged prior-art list; the
   Holevo plateau is the quantum-Darwinism redundancy plateau (flagged,
   correctly); environment-access recovery is worked territory
   (Gregoratti-Werner; arXiv:1502.07030). The assembly (certificate-
   wrapped, banded, ledgered) has no located literature twin, but every
   physical fact assembled is textbook — the correct standing is
   **repo-internal calibration of the certificate toolkit on a QD-type
   family**, not a new physical frontier result.

Non-fatal findings: environment-dependent noise floors presented as exact
(as lens 1); the 6-phase certificate's sufficiency silently relies on the
degree-1 trigonometric structure of rho(phi) (true, verified, unstated —
one sentence needed); "unlimited work registers" numerically asserted with
exactly two ancillas, the unlimited claim carried by the lemma; "certified
against ALL channels" is scoped to the fixed phase-locked figure of merit
on the M=0 branch; the swap-probe `r_feas_by_n` is hardcoded rather than
derived (supporting facts computed — presentation, not error); the three
contrast probes (broadcast/swap/uncorrelated) are the genuinely valuable
residue and deserve to be the headline of the re-scoped calibration.

## Lens 3 — Predeclaration and statistics integrity

**Verdict: survives-with-corrections. Reproduced: yes.**

Evidence (condensed): git log/status (T409 quartet fully untracked; last
commit predates T409); file creation times (model 07:49:43 < test
07:53:04 < JSON 07:53:43 < spec 07:55:49 < results-md 07:56:53); `git
show HEAD` confirms V_STAR = 0.9, THETA = pi/3, PHI_CERT, PHI_LOCK_GRID
byte-identical to the committed T392/T393 batch (d4f47c7) with empty
working-tree diff; full re-execution (124 passed); adversarial certificate
probes (flatness on the exact lock grid 1.7e-16, 200 random phases
2.8e-16, degree-1 trig fit residual 5.6e-16 with genuinely nonzero B at
partial strength); trace-norm bound re-derived by hand and confirmed
airtight for any CPTP map on the declared reach.

Fatal findings: none.

Non-fatal findings (first is a MANDATORY correction):

1. **Predeclaration trail does not exist as claimed.** The spec file was
   CREATED after the model, the test file, and the results JSON; all five
   quartet files are untracked; no steward/runs record covers T409; the
   spec contains outcome-dependent prose and run-specific noise values.
   The results heading "Predeclarations (fixed before inspecting numbers)"
   is an unaudited assertion that file metadata disfavors. Mitigations
   keeping this non-fatal: (a) every load-bearing threshold is
   byte-identical to code committed in the T392-T395 batch; (b) no verdict
   is threshold-marginal (certificates 2.2e-16 vs 1e-12; achieved 0.98974
   vs v* = 0.9; closed forms analytically forced — no tuning opportunity);
   (c) the predeclared failure legs (saturations) actually fired in the
   contrast probes and were reported. Required fix: disclose that only the
   imported T392/T393 constants are auditably prior; T409-specific sweep
   and scenario parameters were fixed in-session without an independent
   record.
2. Certificate documentation gap (substance verified sound): the 6-point
   phi-cert needs the one-sentence degree-1 trig-interpolation argument;
   the trace-norm bound carries the all-channel verdict with no
   finite-proxy gap.
3. Run-unstable machine-noise values quoted as bolded results (as lens 1);
   the "<= 9.8e-15" phrasing should quote the tolerance, not the run.
4. Results-md leg-2 sentence drops a load-bearing qualifier: must read
   "work registers in any (necessarily phi-independent) state"; the lemma
   is false for phi-correlated ancillas.
5. Haar spot check labeled "reach + work" actually samples reach plus only
   ONE work register; work-invariance numerics assert only sigma = |0><0|,
   with "any state" carried by the (correct) lemma. Disclosed; sampling
   never carries an impossibility verdict — house rule respected.
6. TESTS.md contains a full uncommitted T409 registration row embedding
   run-specific noise digits; CLAIM-LEDGER.md is clean. Whether the T409
   lane was authorized to edit TESTS.md is a **governance question that
   pauses for Joe**; this review pass did not touch TESTS.md.
7. COMPLEXITY-LEDGER compliance verified clean ("exhaustive" only for
   literal all-2^n blocks; no hardness/scalability rhetoric; no ledger
   edit).

---

## Aggregate verdict

**survives-with-corrections** (all three lenses; unanimous). All three
lenses independently reproduced the numerics, two of them with fully
independent from-scratch simulators. No lens returned a fatal verdict.
The relocation lens's fatal findings kill the artifact's FRAMING — the
"physical boundary" and "Tier-2 forcing earned" verdict-language and the
new-physics standing — not its computed content; per the spec's own
re-scope clause the artifact stands as a **repo-internal calibration of
the certificate toolkit (all-channel certificates, graded bands, T142
ledger) on a quantum-Darwinism-type collision family**, with the three
contrast probes (broadcast forces r(n) = n; swap saturates at r = 1;
uncorrelated stream at r = 0) as the headline residue showing the declared
reach axis reads off real dynamical structure.

Consequences for the open problem
(`open-problems/region-indexed-capability-discriminator.md`): the
physical-boundary discriminator remains OPEN. T409 does not discharge
T407's standing objection (declared vs physical boundary). The
physical-escape mechanism is exactly T409's own named-unbuilt next rung:
the genuine open-system bound (Hamiltonian bath; work/entropy scaling
with bath contact), where work buying reach becomes a live, fireable
failure leg rather than one excluded by fiat.

## Corrections applied

Applied 2026-07-02 as a dated addendum section in
`results/T409-capability-restoration-frontier-v0.1-results.md`
(history preserved; original text untouched):

1. Verdict downgrade: "Tier-2 forcing earned" and "bounded-region premise
   made physical" withdrawn; standing re-scoped to repo-internal
   calibration per the spec's own clause; T407's objection recorded as
   NOT discharged.
2. Leg-2 downgrade: failure leg acknowledged as unfireable; "priced in
   reach, not work" scoped to a model where work is given no channel to
   buy reach; the "(necessarily phi-independent)" qualifier restored.
3. Prior-art completion: the leg-3 correspondence identified as the
   Englert-Greenberger-Yasin duality (previously unflagged); environment-
   access-recovery prior art named (Gregoratti-Werner quant-ph/0504195;
   arXiv:1502.07030).
4. Reproducibility relabeling: the three bolded noise-level values
   (6.9e-17 / 4.9e-32 / <= 9.8e-15) restated as run-specific machine
   noise below the predeclared tolerances; "exactly" language for the
   finite-precision certificate qualified; the missing degree-1
   trig-interpolation sentence added.
5. Predeclaration disclosure (mandatory): only imported T392/T393
   constants are auditably prior; T409-specific parameters fixed
   in-session without an independent record; spec file postdates the
   first numbers.
6. Scope notes: "unlimited work registers" and "certified against ALL
   channels" scoped to what was computed/lemma-carried; swap-probe
   hardcoding disclosed.

Not touched: CLAIM-LEDGER.md (clean of T409), TESTS.md (pre-existing
uncommitted T409 row flagged above for Joe — governance, not edited
here), the spec/model/test files, the archived JSON.

## Verification-tier consequence

Per the tri-repo three-tier vocabulary: no lens is fatal (three
unanimous survives-with-corrections verdicts) and the numerics were
independently reproduced from scratch by all three lenses. **T409 moves
from recorded to internally established** — in its corrected, re-scoped
standing (repo-internal calibration on a QD-type family; contrast probes
as headline; no physical-boundary claim). The Tier-2/"made physical"
framing did NOT survive review and is not internally established at any
tier. Externally established remains untouched (single-process ceiling
applies; internal reviewers are spawned by the same process).

No claim promotion. No ledger edits. All promotion decisions pause for
Joe.
