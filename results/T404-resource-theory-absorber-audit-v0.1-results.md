# T404 Results: Resource-Theory Absorber Audit for the T407 C(R) Object

- **Artifact:** `T404-resource-theory-absorber-audit-v0.1`
- **Spec:** [tests/T404-resource-theory-absorber-audit.md](../tests/T404-resource-theory-absorber-audit.md)
- **Model:** [models/resource_theory_absorber_audit.py](../models/resource_theory_absorber_audit.py)
- **Test:** [tests/test_resource_theory_absorber_audit.py](../tests/test_resource_theory_absorber_audit.py)
- **Numbers:** [T404-resource-theory-absorber-audit-v0.1.json](T404-resource-theory-absorber-audit-v0.1.json)
- **Tags:** absorber_audit, resource_theory_frame, c_of_r,
  partially_absorbed, residue_located, no_claim_promotion

## Verdict

`partially_absorbed_residue_located`.

The absorber frame was formalized fairly and strongly -- states = region
conditional state data (single unphased rho_R AND the phi-indexed family
over the imported T393 sweep), free operations = all CPTP maps on R fixed
once, monotone vector = the two T407 axes -- and T407's three legs were
tested against it by factorization. All order-theoretic content absorbs.
Two residues survive, both at the frame's interface, each with a named
from-memory candidate absorber; if both verify, T407 demotes to resource
theory with extra bookkeeping (predeclared demotion clause).

## Per-Leg Findings

| Audit leg | Verdict | Key numbers |
| --- | --- | --- |
| Anti-scalar (T407 Leg 2) | **Absorbed as theorem-shape.** Majorization analog (0.5,0.25,0.25) vs (0.4,0.4,0.2): incomparable both ways; tail monotones E1 = (0.5, 0.6), E2 = (0.25, 0.2) order the pair oppositely; certificate shape (-1, +1) identical to T407's featured-pair shape in monotone-axis coordinates (undo rank 2 vs 0, readout rank 0 vs 3). Grid = exact 3 x 4 product order (monotone-vector normal form). | shape match exact; grid exact |
| Profile-from-state map | **Factors -- absorbed content, not residue.** 24 configs -> 18 fingerprint classes (family and single-state partitions coincide); 0 profile violations, 0 statistics violations (max 0.0); the 6 merged classes are exactly the burn/none pairs. In this family the single unphased rho_R suffices. | violations 0/0 |
| Causal indexing (residue a) | **Residue located at the static frame.** Escape chains: 6/6 componentwise monotone, 6/6 with strict drops, burn inert (0.0). Free class certified boundary-blind: menu max outside-marginal move 4.4e-16 over all 24 x 16; correlating escape writes move it 1/3 (class) / 2/3 (full) and create c-e correlation 2/9 from an exactly-uncorrelated start. Fixed-frame trilemma: CPTP(R) sound for the no-go (phi-independence 2.1e-17; channel bound 3.5e-16) but loss inexpressible as free conversion; CPTP(R+E) internalizes the loss but the preparation inverse restores locked visibility >= 0.999999999999999 for all 24 x 2, killing the distinctions; product class = same silence as CPTP(R). No fixed frame carries all three legs. | trilemma certified |
| Declared-record epistemics (residue b) | **Residue located at the frame interface.** Statistics partition (16, 8); the flat 16-class realizes all 12 resource objects with full 3-level undo and 4-level readout span. Two-way non-reduction: featured pair stats diff 0.0 with capability gaps (1.0, 2/3); converse pair profile diff 4.4e-16 with stats diff 0.083. The declared readout is verified to be an experiment on the frame's states (equals rho_R diagonal to 5.6e-17) -- Blackwell-type extra structure the frame does not supply. | two-way non-reduction certified |

## Honest Flags (all from memory, unverified)

- Residue (a) candidate absorber: **dynamical resource theories /
  resource theories of channels and processes** (superchannels as free
  operations; resource theories of causal connection). If verified to own
  causality-indexed free-class families with forced monotone loss,
  residue (a) demotes to translation.
- Residue (b) candidate absorber: **Blackwell comparison of statistical
  experiments** (quantum sufficiency/deficiency). If verified to own
  fixed-readout capability underdetermination, residue (b) demotes.
- Leg A attribution (Nielsen majorization ~1999, Vidal tails,
  Chitambar-Gour vocabulary): names unverified; numbers checked.

## Relation to T398

Confirms T398's absorption of the profile poset and refines its "region
indexing absorbed as context parameter" line: as a static context
parameter the region IS absorbed; the executable point added here is that
the parameter is causality-indexed and no fixed choice of free class
carries all three T407 legs at once. No contradiction; one level deeper.

## What This Gates

- T407 may not promote past this audit: the anti-scalar leg and the
  profile-from-state map may not be presented as resource-theory novelty
  in any form.
- The surviving presentation of T407 is the two-interface conjunction:
  one finite family in which the free class is causally indexed AND the
  declared-record layer is two-way non-reducing. Both halves are
  conditional on the unverified flags.
- Predeclared demotion clause: both flags verifying re-scopes T407 as
  "resource theory with extra bookkeeping"; this audit is the document
  that says so.

## Reproduction

```bash
python -m pytest tests/test_resource_theory_absorber_audit.py -v   # 21 passed
python -m models.resource_theory_absorber_audit
```

Deterministic, exact statevector, ~4 s; T407 (34) and T398 (10) suites
re-run green alongside.
