# T404: Resource-Theory Absorber Audit for the T407 C(R) Object

## Route

Absorber audit (house pattern: T162's executable-obstruction form, T197's
neighbor-granted-full-legitimacy form). This is the absorber run that
T407 (`tests/T407-region-capability-no-go.md`) names as its promotion gate
("Contribution Needed", first bullet) and prices in its attack surface
("Resource theory already owns this"). It sits one level below T398
(`tests/T398-resource-profile-absorber.md`), which admitted the C(R)
PROFILES as resource states and absorbed the profile poset: here the
resource-theory FRAME itself is formalized -- fairly and strongly -- and
T407's three legs are tested against it by factorization, in code.
Honesty regime unchanged: absorption is a fully acceptable verdict, and the
audit gates the program either way.

## Question

Does a resource-theory frame

```text
(states, fixed free-operation class, induced preorder / monotone vectors)
```

absorb T407's three legs? Concretely: do T407's capability verdicts factor
through (region conditional state data, fixed free-operation class), and if
anything does not factor, WHERE exactly does it sit?

## Claim (verdict, stated up front)

**Partially absorbed; residue located.** Per leg:

1. **Anti-scalar leg (T407 Leg 2): ABSORBED as theorem-shape.** The
   standard analog is constructed explicitly -- a majorization-incomparable
   Schmidt-vector pair ((0.5, 0.25, 0.25) vs (0.4, 0.4, 0.2); partial sums
   cross) with two Vidal-style tail monotones ordering the pair strictly
   oppositely -- and its incomparability-certificate shape ((-1, +1): two
   monotones, opposite strict orders, hence no scalar by trichotomy) is
   machine-compared with T407's featured-pair certificate in monotone-axis
   coordinates (undo rank 2 vs 0; readout rank 0 vs 3). Same shape. T407's
   realized 3 x 4 grid is verified to be the monotone-vector normal form
   (exact product of two chains). Finite physical instance, not new order
   mathematics.

2. **Factorization (the real audit): the profile-from-state map FACTORS --
   absorbed content, not residue.** Fingerprinting all 24 configurations by
   their region state data (both the phi-indexed family over the imported
   T393 certificate sweep and the single unphased rho_R -- the two induced
   partitions coincide, 18 classes each) shows ZERO violations: equal
   region data implies equal capability profile and equal declared
   statistics. The six fingerprint-merged pairs are exactly the burn/none
   pairs -- T407's burn null reappears as a factorization fact. This is
   what T407/T393's phi-independence certificates say, confirmed in the
   absorber's own vocabulary. The residue is NOT here. It is located at
   two places the static frame cannot reach:

   - **(a) Causal indexing of the free class (residue located).** Along
     every escape chain none -> class -> full at fixed record writes, the
     profile drops componentwise monotonically (6/6 chains, 6/6 with strict
     drops; burn moves nothing, max profile diff exactly 0.0). The degrading
     operations are certified NON-FREE for the fixed class: all 16 menu
     protocols leave the outside marginal invariant to 4.4e-16 across all
     24 configurations, while the correlating escape writes move it by 1/3
     and 2/3 and create c-e correlation 2/9 from an exactly-uncorrelated
     start (so they are neither R-local nor product R (x) E maps; burn
     moves the marginal but creates zero correlation and zero capability
     change -- the loss tracks the correlating writes exactly). The
     fixed-frame trilemma, executable: **CPTP(R)** is sound for the no-go
     (phi-independence 2.1e-17, channel bound 3.5e-16 on the re-touched
     corner) but cannot express the loss as a conversion; **CPTP(R+E)**
     internalizes the loss but one explicit free protocol -- the
     preparation inverse -- restores locked visibility 1.0 (min
     0.999999999999999 over 24 configurations x 2 pairs) so the realized
     undo distinctions vanish and the no-go is lost; **CPTP(R) (x)
     CPTP(E)** behaves like CPTP(R). No fixed frame in the declared
     candidate set carries all three legs at once. What does is a
     causality-INDEXED family of resource theories with forced monotone
     capability loss -- T393's window pattern (recovery closes exactly at
     the escape step; boundary enlargement restores exactly), cited not
     re-derived. **Flagged honestly:** dynamical resource theories /
     resource theories of channels and processes (superchannels as free
     operations; resource theories of causal connection) are from-memory
     candidate absorbers of even this indexed-family shape. Unverified. If
     they verify, residue (a) demotes to translation.

   - **(b) Declared-record epistemics (residue located).** T407 Leg 3
     concerns bounded observers' declared readouts, not state identity;
     the frame's derived vocabulary (state identity, convertibility,
     monotone values) has no native notion of "identical declared records,
     different resources." Executable: the statistics-flat 16-class
     realizes ALL 12 resource objects across the FULL span of both
     monotone axes (3 undo levels, 4 readout levels), so any frame
     functional factoring through the declared record is constant exactly
     where the monotone vector spans its entire range; conversely the
     capability-identical converse pair (profile diff 4.4e-16) splits the
     statistics (0.083) -- a two-way non-reduction. The declared readout
     is verified to be a bona fide experiment ON the frame's states (it
     equals the computational-basis diagonal of rho_R to 5.6e-17): an
     extra primitive of Blackwell type, which the frame does not supply.
     **Flagged honestly:** comparison of statistical experiments
     (Blackwell; quantum sufficiency/deficiency) is the from-memory
     candidate absorber of that extra layer. Unverified. If it verifies,
     residue (b) also demotes.

3. **Overall: `partially_absorbed_residue_located`,** with the predeclared
   demotion clause asserted verbatim in the tests: if BOTH flagged
   candidate absorbers verify against the literature, T407 demotes to
   "resource theory with extra bookkeeping" and no promotion may cite this
   audit as support.

## Class

**Absorber audit, capability-object lineage.** NOT registered in
CLAIM-LEDGER. This artifact can only demote or gate; it promotes nothing.
All decisions pause for Joe per AGENTS.md.

## Status

Implemented; all checks pass as stated. 21 tests green; T407 and T398
suites re-run alongside, still green. Everything that carries a verdict is
exact statevector arithmetic on T407's imported model; nothing sampled.

## Target Claims

- [T407: Region-Indexed Capability No-Go](T407-region-capability-no-go.md)
  (the object under audit; its named promotion gate)
- [T398: Resource-Profile Absorber](T398-resource-profile-absorber.md)
  (the profile-level absorber this audit extends one level down)
- [T393: Causal Forcing of the Access Asymmetry](T393-causal-forcing-of-access-asymmetry.md)
  (the window result residue (a) rests on; certificate sweep imported)
- [T394: Axis-Count Reconstruction Hierarchy](T394-axis-count-reconstruction-hierarchy.md)
  (via T407's imported grid/poset machinery)
- [T395: Record-Order Trade-off Probe](T395-record-order-tradeoff-probe.md)
  (primitives imported through T407)

## The Absorber Frame (declared once, before numbers)

```text
states           : region conditional state data per configuration --
                   the single unphased rho_R AND the phi-indexed family
                   {rho_R(phi)} over the imported T393 certificate sweep
                   (both carried; induced partitions compared)
free operations  : all CPTP maps supported on R = (c, r1, r2, t), FIXED
                   ONCE (strongest natural in-region class); CPTP(R+E) and
                   CPTP(R) (x) CPTP(E) enumerated as alternative fixed
                   frames, never mixed in
preorder         : reachability under the fixed free class
monotone vector  : the two T407 axes (undo level, readout level),
                   certified against the whole class by T407's imported
                   all-channel certificates
```

Fairness note: the frame is granted everything it can natively own --
state-level objects (not just profiles), the strongest in-region free
class, and complete monotone coordinates. The audit looks for what fails
to factor AFTER that grant.

## Setup

`models/resource_theory_absorber_audit.py`. Imports T407's model wholesale
(`models.region_capability_no_go`: configurations, profiles, menu,
certificates, statistics partition, poset/grid checkers), T393's
certificate phase sweep (`PHI_CERT`), and T395's statevector primitives.
The only new operator constructed is the preparation-circuit unitary
(from T407's own gate constructors), used as the boundary-crossing
restoration protocol; the only new data are the Leg-A Schmidt vectors.
Fingerprints round to 10 decimals; floors predeclared (restore 1 - 1e-9;
outside-move 0.25; correlation 0.15; converse stats split 0.05).

## Gates / Guardrails

- **No fake citations:** every literature attribution (Nielsen
  majorization, Chitambar-Gour review, dynamical/channel resource
  theories, resource theories of causal connection, Blackwell comparison
  of experiments) is FROM MEMORY, flagged as such in module constants and
  asserted flagged in the tests; nothing enters `literature/`.
- **Verdict vocabulary predeclared** as module constants, asserted
  verbatim; inflation terms banned by test.
- **Q1D / R1:** untouched -- inherited from T407 unchanged; this audit
  adds no physical claims, only factorization checks on T407's family.
- **T398 consistency:** the audit confirms T398's absorption of the order
  content and refines (does not contradict) its "region indexing absorbed
  as context parameter" line: as a STATIC context parameter the region is
  absorbed; the executable point is that the parameter is causality-
  indexed and no fixed choice carries all three legs at once.

## Neighbors / Prior Art

In-repo: T407 (object under audit), T398 (profile-level absorber), T162 /
T197 (the absorber-audit pattern), T393 (window result; certificates),
T399-T403 (the other lane's discriminator screens -- complementary: they
strengthen the boundary-crossing task side, this audit prices the
resource-theory side).

Candidate prior art (ALL from memory -- flagged, unverified, none cited as
fact): Nielsen's majorization theorem and LOCC-incomparable states
(~1999); Vidal-style entanglement monotones; the Chitambar-Gour
resource-theory review; dynamical resource theories / resource theories of
channels and processes (superchannels as free operations); resource
theories of causal connection / process matrices; Blackwell comparison of
statistical experiments and quantum sufficiency/deficiency orderings.

## Honest Reviewer Attack Surface

- **"The frame enumeration is a strawman -- only three fixed classes."**
  The three are the natural ones definable from the declared region
  geometry (in-region, everything, no-communication product); the residue
  claim is relative to that declared candidate set, stated as such, and
  the from-memory dynamical-RT flag names exactly the framework that
  could beat it. The verdict is conditional on that flag by construction.
- **"CPTP(R+E) trivializing is obvious -- global purity."** Yes, and
  that is the point made executable: obviousness is the absorber's own
  argument that no SINGLE fixed frame does both jobs. The explicit free
  protocol (preparation inverse, restored visibility 1.0, outside-marginal
  move up to 1.0) turns the observation into a certificate.
- **"Residue (b) is just 'RT doesn't talk about observers' -- not a
  residue."** Agreed in part, and priced: the audit does not claim the
  frame is WRONG, only that Leg 3 is not a statement in it, and that the
  extra primitive it needs (the experiment map) is verified to be
  Blackwell-type structure with its own named candidate absorber. If that
  absorber verifies, (b) demotes -- predeclared.
- **"T398 already ruled statistics-flatness absorbed; this contradicts
  it."** No: T398 absorbed it as an incomplete observer shadow GIVEN the
  admitted profile; this audit locates precisely the extra structure that
  admission smuggles in (the record map is two-way non-reducing against
  the resource objects) and hands it to its proper owner.
- **"The escape chain is configuration-indexed, not time-indexed --
  where is the causality?"** Disclosed: the time-indexing (window closing
  at the escape step) is T393's Tier-1 result, cited not re-derived; the
  executable stand-ins here are escape-extent monotonicity and
  boundary-crossing restoration.

## Failure Conditions

- Any tuning of the fingerprint decimals, floors, or candidate-frame set
  after inspecting numbers (all predeclared; the Schmidt pair was chosen
  for its textbook partial-sum crossing before any comparison ran).
- Leg A fails if the majorization pair is comparable or the certificate
  shapes differ. Reportable verdict: "no shape identity -- anti-scalar leg
  not absorbed as stated" (did not occur).
- Leg B1 fails if any fingerprint class splits on profile or statistics.
  Reportable verdict: "capability does NOT factor through the region
  state -- T407's certificates are wrong somewhere" (did not occur; this
  would have been the headline).
- Residue (a) fails to be located if some fixed candidate frame both
  preserves the distinctions and internalizes the loss, or if an escape
  chain is non-monotone. Reportable verdict: "absorbed by a fixed frame --
  causal indexing is bookkeeping" (did not occur).
- Residue (b) fails to be located if the flat class stops spanning the
  objects or either factorization direction holds. Reportable verdict:
  "record layer reduces -- Leg 3 absorbed outright" (did not occur).
- Claiming the residues as positive novelty results rather than located
  non-absorptions conditional on unverified flags; claiming anything
  beyond T407's declared family, menu, readout convention.

## What This Does Not Earn

- **No claim promotion, no CLAIM-LEDGER entry.** An absorber audit can
  only demote or gate.
- **No literature verdict.** Both residues stand RELATIVE TO the
  formalized static frame; each carries a named from-memory candidate
  absorber that could still take it. Verifying those is the named next
  step and nothing external-facing may precede it.
- **No new mathematics, no physical-agent claim, no hardware claim.**
- The demotion clause is live: if both flags verify, T407 is "resource
  theory with extra bookkeeping" and this audit is the document that says
  so.

## Reproduction

```bash
python -m pytest tests/test_resource_theory_absorber_audit.py -v
python -m models.resource_theory_absorber_audit
```

Deterministic; ~4 s each.

## Contribution Needed

- **Verify the two flagged candidate absorbers** (dynamical/channel
  resource theories for residue (a); Blackwell/comparison-of-experiments
  for residue (b)) against actual literature -- the single decision-
  relevant follow-up. Until then both residues are conditional.
- If residue (a) survives verification: state the causality-indexed
  family {CPTP(R_s)} as an explicit object (T393's window as the index
  map) and ask what a "resource theory of remaining in the lightcone"
  would have to prove.
- If residue (b) survives verification: connect to the T399-T403
  boundary-forced-task lane, which is building the task-side version of
  the same interface.
- Pause for Joe before any re-scoping of T407 [steward note 2026-07-02:
  the remainder of this bullet was lost to a session-mount truncation
  before the 2026-07-01 stewardship pass and is unrecoverable (file was
  never committed); the pause-for-Joe directive itself is intact].
