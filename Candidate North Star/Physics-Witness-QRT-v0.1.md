# Physics Witness: Quantum Resource Theory v0.1

## Status

This is a companion artifact to `Candidate North Star v0.4.md`.

It is not canon. It does not promote the Candidate North Star. It does not
claim new physics. It does not claim canonical residue.

Purpose:

```text
Produce one filled no-free-physics template for quantum resource theory,
run it through the v0.4 absorption protocol, assign an honest residue label,
and confirm whether this domain can bear the weight v0.4 assigns it in the
Physics Witness Posture section.
```

Gate settled here: whether v0.4's physics templates have at least one real
filled instantiation before v0.5 drafts.

---

## The Witness

### Filled No-Free-Physics Template

```text
Known theory:
  Quantum resource theory (QRT) — specifically the resource theory of
  entanglement under LOCC, and more generally any resource theory defined
  by a free-state set F and a free-operation class R.

  Standard references: Chitambar and Gour 2019 "Quantum resource theories"
  (Rev. Mod. Phys. 91, 025001). Horodecki et al. 2009 entanglement review.
  Winter and Streltsov 2016 operationally motivated coherence resource theory.

Y:
  Global bipartite (or multipartite) quantum state rho_AB in H_A tensor H_B,
  together with the full purification rho_ABE in H_A tensor H_B tensor H_E.
  In the general resource-theory framing: the full quantum state rho on the
  composite system, which may include environment/purifier access E.

X:
  Reduced density matrix rho_A = Tr_B(rho_AB) on subsystem A only, as
  accessible to a strictly local observer O_A who can measure A but has no
  physical access to B or E.
  More precisely: the image of the partial-trace map restricted to local
  measurements on A with no classical side-channel from B.

pi:
  pi : Y -> X is the partial trace / local restriction map.
  pi(rho_AB) = Tr_B(rho_AB) = rho_A.
  This is a completely positive trace-preserving (CPTP) map and a standard
  projection in the quantum information sense.

Cap:
  Cap_R(rho_AB) = the set of resource states reachable from rho_AB under the
  declared allowed operation class R, where R is one of:
    - LOCC: local operations and classical communication between A and B.
    - Local-only: local operations on A alone, no communication.
    - LOCC + shared randomness.
    - Global unitaries (reference ceiling for convertibility).
  In the entanglement resource theory: Cap_LOCC(rho_AB) is the downset of
  states convertible from rho_AB under LOCC, including the entanglement
  distillation envelope (asymptotic rate E_D) and the dilution cost (E_C).
  In the coherence resource theory: Cap_R(rho) is the set reachable under
  incoherent operations from a given state in a fixed basis.

K:
  The capability object K is the convertibility preorder on states induced by R:
    sigma <=_R rho iff there exists a free operation Lambda in R such that
    Lambda(rho) = sigma (exact case) or Lambda(rho) approx sigma (approx case).
  K is equivalently encoded by the resource monotone family: any function
  M : States -> R such that M(Lambda(rho)) <= M(rho) for all Lambda in R.
  Canonical choice for entanglement: the entanglement entropy E(rho_AB) =
  S(rho_A) for pure states; E_D and E_C for mixed states.

Equivalence on K:
  Two states rho, sigma are K-equivalent (rho ~=_K sigma) when they are
  mutually interconvertible under R: rho <=_R sigma and sigma <=_R rho.
  For pure bipartite states under LOCC, this is equivalent to equal
  Schmidt coefficients (up to permutation). For mixed states, mutual
  interconvertibility is more subtle and theory-dependent.
  In the approximate/asymptotic case: rho ~=_K sigma iff E_D(rho) = E_D(sigma)
  and E_C(rho) = E_C(sigma), which defines the equivalence used for quotienting.

Allowed operations:
  R = LOCC: local quantum operations on A and B independently, plus any
  finite number of rounds of classical communication between A and B.
  This is the physically motivated free operation class for entanglement theory:
  it cannot create entanglement and is closed under composition.
  Alternative: R_A = local operations on A only (no communication). This is the
  strictly local class for the observer who owns only subsystem A.
  The witness uses both: R_A for the local observer, LOCC for the two-party
  cooperative case. The access profile declares which class is active.

Observer/access profile:
  O_A: Observer holding subsystem A. Physical access = local measurements on A
  (POVMs on H_A), local unitary operations on A, and local state preparation on
  A. No physical access to B, no joint operations on AB, no access to purifier E.
  O_AB: Two-party cooperative observer. Physical access = all the above on A and
  B, plus classical communication between A and B (unlimited rounds). No access
  to environment E.
  O_full: Reference observer with full access to ABE including purifier. This
  is the access profile under which the full state rho_ABE determines all
  resource properties and Cap factors through pi trivially (rho_ABE is the
  full state, no projection loss).
  The witness is indexed to O_A and O_AB. Statements about O_full are the
  trivial enrichment control (see below).

Horizon/resource boundary:
  The resource boundary is the access boundary between A and B. Classical
  communication across this boundary is free; quantum communication and
  entanglement creation are not free.
  The horizon in the entanglement sense: LOCC cannot increase entanglement,
  so the entanglement horizon of rho_AB under LOCC is the set of states with
  E_D(sigma) <= E_D(rho). Convertibility decreases or is flat monotonically.
  For the strictly local observer O_A: the horizon is tighter; without classical
  communication, local operations alone cannot change global resource values.

Factorization question:
  Does Cap_R factor through pi?
  That is: does rho_A = Tr_B(rho_AB) determine Cap_R(rho_AB) up to ~=_K?
  Answer (known theorem):
    Under R_A (local operations on A only, no communication): NO.
    Same rho_A can coexist with different global entanglement values,
    different E_D, different E_C, different LOCC-convertibility structure.
    pi-fiber {rho_AB : Tr_B(rho_AB) = rho_A} contains states at every
    entanglement level from zero (product states with the given marginal)
    up to states with rho_A as marginal and high global entanglement.
    Under LOCC (O_AB): also NO for mixed states. Same rho_AB can have
    the same local spectra but different entanglement properties (bound
    entanglement vs. distillable entanglement). Local spectra do not determine
    LOCC-convertibility for mixed states.
    For pure states under LOCC: YES for the Schmidt decomposition.
    rho_A = Tr_B(|psi><psi|) determines the Schmidt coefficients which
    determine the full entanglement structure under LOCC. This is the
    PRESERVATION CONTROL (see below).

Native absorber:
  Quantum resource theory fully owns this witness.
  The non-factorization is a theorem in QRT: the reduced density matrix does
  not determine global resource properties for mixed states.
  The minimal sufficient enrichment is the global state rho_AB (or its
  purification rho_ABE). This enrichment is domain-standard: QRT always
  works with global states.
  The HJW (Hurvits-Josza-Wouters) theorem and purification results give
  the absorber in explicit form: the purification ambiguity (non-uniqueness
  of purification up to unitaries on E) shows that rho_A determines rho_ABE
  only up to local unitaries on E, which is a resource-theory equivalence
  not a resource-level equivalence. Different purifiers can give different
  multipartite resource values.
  Bound entanglement literature (Horodecki et al.) explicitly studies states
  where rho_AB has positive partial transpose (PPT, entangled but not
  distillable under LOCC) versus states with same local spectra but non-zero
  distillable entanglement. This is exactly the non-factorization fixture
  the audit needs.

Not claimed:
  1. This witness does not claim that QRT "proves" the Candidate North Star.
     The projection-sufficiency failure is a known theorem, not new.
  2. This witness does not claim that rho_A being insufficient for global
     resource properties is surprising to physicists. It is not.
  3. This witness does not claim that the audit schema adds mathematical content
     beyond what QRT already provides.
  4. This witness does not claim that Cap can be defined independently of the
     declared operation class R. Cap is indexed to R throughout.
  5. This witness does not claim that the entanglement resource theory is the
     only or canonical K for quantum systems.
  6. This witness does not claim gauge-invariance complications are resolved.
     Phase conventions and basis choices for coherence resource theories
     require an invariance audit before the coherence case is used.
```

---

## Absorption Protocol Run

### State-Enrichment Absorption Test

The natural sufficient enrichment for the local observer case is rho_AB itself
(the global bipartite state). This is domain-standard. QRT always begins with
the global state and asks what operations are free.

The enrichment pi'(rho_AB) = (rho_A, rho_AB) trivially restores factorization,
but rho_AB is not artificial or gerrymandered: it is the actual object of study.

The enrichment by rho_ABE (purification) is also domain-standard: purification
is a standard tool in quantum information and gives the maximal state, from which
all resource quantities can be computed.

Verdict on state-enrichment absorption: ABSORBED.

The non-factorization is real but absorbed by the domain-standard enrichment.
The enrichment is natural (rho_AB is not exotic). This does not make the witness
worthless; it confirms that QRT already has the right enriched state and the
audit just names what is happening.

### Native-Theory Absorption Test

Quantum resource theory provides:

- the convertibility preorder as K (already done);
- the LOCC monotone proof that entanglement entropy E is a resource monotone
  (already proven, not new);
- the pure-state uniqueness theorem (Schmidt decomposition argument) showing
  when rho_A does determine global capability (the preservation control);
- the bound entanglement family showing when it does not (non-factorization
  fixtures are known);
- the HJW purification theorem giving the absorption of the purifier ambiguity;
- the mixed-state entanglement theory showing the gap between E_D and E_C and
  between PPT and non-PPT entangled states.

Verdict on native-theory absorption: ABSORBED.

Every part of the non-factorization is explained by existing QRT. The audit
schema organizes the known structure; it does not produce new theorems.

### Gauge/Relabeling Invariance Check

For the entanglement resource theory under LOCC:
- Local unitaries on A or B do not change entanglement (they are free operations
  in LOCC). So Cap_LOCC(U_A x U_B rho_AB) ~=_K Cap_LOCC(rho_AB). Invariance holds.
- Phase conventions on the Schmidt decomposition: Schmidt coefficients are
  invariant. Invariance holds.
- For coherence resource theories: the free incoherent operations depend on
  the chosen basis (the "pointer basis"). Different basis choices give different
  resource theories. This is NOT resolved by one invariance declaration and must
  be flagged if coherence witnesses are used. The entanglement case does not
  have this ambiguity.

Verdict: invariance holds for the entanglement witness as stated. The coherence
case requires an additional basis-declaration step before use.

---

## Preservation Control

For pure bipartite states |psi> in H_A tensor H_B:

rho_A = Tr_B(|psi><psi|) determines the Schmidt coefficients {lambda_i}
uniquely (up to permutation). Under LOCC, two pure states are convertible
iff their Schmidt coefficient vectors are related by majorization (Nielsen
1999). Since rho_A determines the Schmidt vector, Cap_LOCC factors through pi
for pure states.

This is the preservation control: the projection IS sufficient in this case.
Without it, the witness is a claim that projection always fails, which is too
strong and wrong.

The control works because: for pure states, the purification is essentially
unique up to local unitaries on E (HJW), and local unitaries on E do not change
LOCC-convertibility. So the fiber collapse is complete in this case.

---

## Non-Factorization Fixture

For mixed bipartite states:

Consider two states on 2 tensor 2 (two qubits):

State sigma_1: maximally mixed state rho_A = I/2 on A, globally a product
state: rho_AB = (I/2) tensor (I/2). No entanglement. E_D = 0.

State sigma_2: rho_A = I/2 on A (same marginal), globally the singlet state
|psi^-> = (|01> - |10>)/sqrt(2), with E = 1 ebit. E_D = 1.

Then pi(sigma_1) = I/2 = pi(sigma_2), but Cap_LOCC(sigma_1) and Cap_LOCC(sigma_2)
are not K-equivalent: sigma_2 can be used to teleport a qubit with one ebit of
entanglement consumption; sigma_1 cannot be used for any entanglement-enabled
protocol.

This is a clean non-factorization fixture: same visible state (I/2 on A), but
different resource capability under LOCC.

Known to QRT: not new, but formally satisfies the v0.4 requirement for a
non-factorization fixture in the positive (correctly placed) direction.

---

## Fiber Spread

For a fixed rho_A = sigma, the fiber {rho_AB : Tr_B(rho_AB) = sigma} contains
states with all entanglement values from 0 (product states with given marginal)
to log(min(dim H_A, dim H_B)) ebits (maximally entangled states with maximally
mixed marginal).

The spread of Cap_LOCC over this fiber is maximal: the fiber spreads over the
full range of convertibility classes. For rho_A = I/2 in 2 tensor 2, the fiber
contains both product states and the singlet, confirming non-singleton spread.

ambiguity_Cap(rho_A = I/2) = |Spread_Cap(I/2)| = uncountably many K-classes.

Cap does not factor through pi.

---

## Residue Label

**Translation Residue (with useful audit value)**

Justification:

The non-factorization is real and clean. The preservation control (pure states)
and fixture (mixed states, product vs singlet) satisfy the v0.4 checklist.
The template fills without strain.

But:

1. Native-theory absorption is complete. QRT already has all theorems,
   all vocabulary, and all proofs. The audit schema translates QRT into the
   v0.4 notation; it does not produce new results.
2. State-enrichment absorption is complete. The domain-standard enrichment
   (global state) restores factorization trivially.
3. The minimal capability-preserving quotient in this domain is the LOCC
   equivalence class on rho_AB (or equivalently the entanglement class under
   the operation class R). This is already the organizing object of QRT.
   The audit names it; QRT owns it.
4. There is no cross-domain transfer demonstrated here. The witness stays
   inside quantum information.

Elevation path:

The witness could reach Formal Residue if:
- a cross-domain theorem is proven that transfers the QRT convertibility
  structure to another mature field (e.g., a formal analogy between LOCC
  and database view determinacy that produces new results in one or both);
- a new typed audit criterion is derived that catches false witnesses in
  QRT-adjacent contexts where the native theory is absent.
Neither of these is demonstrated here. Translation Residue is the honest label.

---

## Reviewer Checklist (v0.4)

```text
Y declared?                                        YES — rho_AB / rho_ABE
X declared?                                        YES — rho_A = Tr_B(rho_AB)
pi declared?                                       YES — partial trace map
visible equivalence ~=_X declared?                 YES — equality of rho_A
K typed?                                           YES — convertibility preorder under R
Cap declared before the witness?                   YES — Cap_R = reachable set under R
capability equivalence ~=_K declared?              YES — mutual interconvertibility under R
observer/task/horizon/boundary fixed?              YES — O_A (local only) and O_AB (LOCC)
projection meaningful?                             YES — partial trace is physical and standard
same-visible-state context fixed?                  YES — equality of reduced density matrix
projection underdescribed?                         NO — partial trace is fully specified
Cap domain-natural?                                YES — convertibility preorder is the
                                                        canonical K in QRT
Cap non-gerrymandered?                             YES — LOCC-convertibility is operationally
                                                        motivated, not constructed for the witness
positive preservation control supplied?            YES — pure states, Schmidt decomposition
negative non-factorization fixture supplied?       YES — product vs singlet with I/2 marginal
fiber spread singleton or non-singleton?           NON-SINGLETON — maximal spread for I/2
minimal capability-preserving quotient identified? YES — LOCC equivalence class on rho_AB
trivial/native enrichment tested?                  YES — rho_AB restores factorization
state-enrichment absorption tested?                YES — ABSORBED (natural enrichment = rho_AB)
native-theory absorption tested?                   YES — ABSORBED (QRT owns all theorems)
residue label honest?                              YES — Translation Residue
```

Physics addendum:

```text
known physics induces Cap?                         YES — LOCC is physically motivated
physical access profile declared?                  YES — O_A (local), O_AB (LOCC)
allowed operations declared?                       YES — local measurements, LOCC, R_A
gauge/relabeling invariance respected?             YES for entanglement case (local unitaries
                                                       are free operations, invariance holds);
                                                   FLAG for coherence case (basis-dependent)
strictly local controls included?                  YES — O_A case is the strictly local control
not-claimed boundary explicit?                     YES — not claimed to be new, not claimed to
                                                       prove North Star, not claimed to add
                                                       content beyond QRT
```

All gates pass. The witness is honestly assembled.

---

## What This Settles

**Gate 2 settled for QRT:** quantum resource theory under an explicit LOCC /
local-only access profile can produce a real filled witness against the v0.4
no-free-physics template. The template fields are not vacuous; they constrain
what can be said.

**What it does not settle:**

- Whether other physics domains (GR, condensed matter, thermodynamics) can
  produce equally honest witnesses. Those require separate runs.
- Whether the audit schema produces any formal or canonical residue beyond
  Translation Residue in the QRT domain. It does not, currently.
- Whether v0.4's demotion of dark matter and dark energy is correct. This
  witness does not test those cases.

**Recommendation for v0.5:**

The main note's Physics Witness Posture section correctly lists quantum resource
theory as the strongest promote-as-anchor domain. This witness confirms that
listing is defensible. The anchor is real but Translation Residue only.

If v0.5 wants to make a stronger claim, the path is:
1. Run a GR causal accessibility witness (next strongest candidate per the
   20 Physics Perspectives panel).
2. Look for a cross-domain transfer theorem between QRT convertibility and
   another formal structure (database view determinacy or process semantics
   are the nearest candidates).
3. If no transfer theorem appears, the honest claim is: physics enters via
   Translation Residue witnesses that confirm the audit template is not empty
   and can be instantiated with known physics.

---

## Not Done In This Pass

The following were scoped out of this witness and should not be inferred:

- Coherence resource theory witness: requires basis-declaration step, needs
  separate treatment due to basis-dependence of the free operation class.
- Thermodynamic resource theory witness (Brandao et al.): requires declaring
  the Gibbs state as the free state and thermal operations as R; different
  template instantiation, not done here.
- Multipartite entanglement witness: different convertibility structure
  (SLOCC vs LOCC), genuinely harder, not done here.
- Any claim about time-as-finality specifically: this witness is for the
  Candidate North Star (capability projection), not for TaF's North Star.
