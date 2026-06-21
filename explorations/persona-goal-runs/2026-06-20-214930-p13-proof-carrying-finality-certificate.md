# P13 Bounded Run - Proof-Carrying Finality Certificate Schema

- Run timestamp: 2026-06-20T21:49:30-05:00
- Persona: P13 - Zero-Knowledge / Cryptography Researcher
- Goal id: P13
- Queue goal: Specify proof-carrying finality for bounded observers: witness, statement, commitment, verification predicate, leakage model, and failure mode.
- Bounded scope: repo-only synthesis across existing witness-obligation, detector-manifest, and bounded-observer-gap surfaces. No claim-status, roadmap, workflow, automation, or executable-model edits.

## Repo Context Read

- `open-problems/proof-carrying-record-finality.md`
- `ROADMAP.md`
- `CLAIM-LEDGER.md`
- `tests/T99-losskernel-quotient-separation.md`
- `technical-reports/TECHNICAL-REPORT-losskernel-quotient-separation-v0.1.md`
- `tests/T136-detector-preregistration-manifest.md`
- `technical-reports/TECHNICAL-REPORT-detector-preregistration-manifest-v0.1.md`
- `tests/T19-phenomenal-bridge-complexity-separation.md`
- `tests/T92-accessible-witness-gap-restriction.md`
- `explorations/all-persona-last-24h-review-2026-06-20.md`

## Work Performed

1. Read the existing open problem to see whether proof-carrying finality was already defined as a strong theorem target or only as an analogy import.
2. Compared the two strongest repo-local "certificate-like" structures:
   - `T136` detector pre-event manifests, which already freeze commitments before data;
   - `T99` typed witness obligations, which separate same-endpoint cases only when hidden source-side obligations are carried.
3. Cross-checked both against the bounded-observer gap discipline from `T19/T92` to see what a downstream observer can and cannot verify without full witness disclosure.
4. Reduced the cryptography analogy to the smallest object that fits current repo results without pretending physical records are already zero-knowledge proofs.

## Result

### Smallest honest repo-native object

The useful object is not "proof-carrying finality" in the broad sense. It is a
bounded, observer-indexed certificate for a specific admissibility or
attribution judgment:

```text
ProofCarryingFinalityPacket_O = (
  statement,
  commitment,
  hidden_witness_type,
  verifier_access_profile,
  verification_predicate,
  leakage_profile,
  failure_modes
)
```

with:

- `statement`: a bounded claim such as "this detector packet qualifies for tier
  X under predeclared rules" or "this projection verdict is admissible because a
  named source witness exists";
- `commitment`: a hash, manifest binding, or typed obligation token that fixes
  what is being claimed before later reinterpretation;
- `hidden_witness_type`: the witness is not fully disclosed to the verifier, but
  its role is typed in advance;
- `verifier_access_profile`: the observer and access boundary under which the
  claim is being checked;
- `verification_predicate`: the finite rule that returns `accept`, `reject`, or
  `underdetermined`;
- `leakage_profile`: exactly what the verifier learns beyond the verdict;
- `failure_modes`: the ways the packet can fail or overclaim.

### Two current instantiations already exist in the repo

1. `T136` is a commitment-carrying admissibility packet.
   - strongest fit for `commitment`;
   - the verifier checks pre-event manifest bindings, declared tier, wrapper
     commitments, and authority separation;
   - the verifier does not need the future detector outcomes at verification
     time;
   - this is close to proof-carrying protocol admission, not proof of detector
     physics.

2. `T99` is a witness-typed attribution packet.
   - strongest fit for `hidden_witness_type`;
   - same endpoints and naive lost-label sets can still require opposite
     verdicts because one case carries an obstruction-resolving source witness
     obligation and the other does not;
   - this is close to proof-carrying attribution, but only if those witness
     obligations are derivable rather than fixture-declared.

### Minimal verification rule

The repo-compatible verifier should be read as:

```text
verify_O(packet, local_data) in {accept, reject, underdetermined}
```

where `accept` means:

1. the packet's commitment was frozen before the later dispute point;
2. the verification predicate references only the verifier's declared access
   profile plus the committed digest/typed obligation surface;
3. the packet's hidden witness type is sufficient for the specific judgment
   being claimed;
4. no known failure mode is triggered.

`underdetermined` is essential. It captures the repo's existing bounded-observer
discipline more honestly than forcing every case into accept/reject.

### Why zero-knowledge language only partially fits

The analogy helps only when three restrictions are enforced:

1. The packet certifies a bounded relation, not the whole physical state.
2. The verifier's access boundary is explicit.
3. The hidden witness is a typed role inside an existing finite protocol or
   attribution judgment, not a mystical "the universe contains the proof."

Without those restrictions, the analogy misleads in exactly the way the roadmap
warns about:

- it can make entanglement sound like encrypted message passing;
- it can blur physical records with engineered proof systems;
- it can imply a bounded observer can certify facts whose witness lies outside
  the accessible region.

### Hard boundary from `T19/T92`

`T19/T92` supply the main cryptographic guardrail:

- a bounded observer may fail to verify a true external finality fact because
  the witness is outside its accessible region;
- a certificate cannot erase that boundary unless the repo explicitly grants a
  trusted transfer channel carrying the needed witness commitment into the
  observer's admissible access set;
- therefore "proof-carrying finality" should not be used to claim that bounded
  observers can verify self-finality or hidden global structure merely by
  rhetoric.

So the strongest honest statement from this run is:

```text
TaF currently supports proof-carrying bounded judgments, not proof-carrying
physical finality in general.
```

### Leakage model and failure modes

The minimal leakage model is:

- reveal the claimed judgment type;
- reveal the verifier identity/access profile;
- reveal the commitment digest and witness type;
- do not reveal full raw witness payload unless the protocol already requires
  it.

The bounded failure modes are:

1. `posthoc_commitment_upgrade`
   - the tier or typed obligation is bound only after data or dispute.
2. `label_only_no_source_anchor`
   - a decorative label is presented as if it were a witness obligation.
3. `access_boundary_mismatch`
   - the verifier is asked to certify a fact whose witness is outside its
     admissible access profile.
4. `physics_as_crypto_overreach`
   - the analogy is used to imply physical proof-system semantics that the repo
     has not earned.
5. `leakage_undisciplined`
   - the packet leaks the full witness or raw outcome when only a bounded
     relation was supposed to be certified.

## Main Finding

The repo does not need a general zero-knowledge story first. It already has two
partial certificate components:

- `T136`: commitment-before-data;
- `T99`: typed hidden witness burden.

The missing middle is an explicit verifier contract that says which bounded
judgment is being certified, for which observer, with what leakage, and when
`underdetermined` is the only honest verdict.

## Blocker

No current executable object unifies:

- `T136`-style precommitted manifests;
- `T99`-style source-anchored hidden witness obligations;
- `T19/T92`-style access-boundary failure;
- one shared `verify_O(...)` predicate.

Also, `T99` still depends on fixture-declared witness obligations rather than a
canonical derivation rule, so the witness half of the packet is not yet earned.

## Proposed Next Action

Take one bounded follow-up:

1. Draft `T137` or a nearby exploration note defining a shared
   `ProofCarryingFinalityPacket` schema with one `T136` detector instance and
   one `T99` attribution instance.
2. Require every such packet to return `accept`, `reject`, or
   `underdetermined`, with `access_boundary_mismatch` as a first-class reject
   reason.
3. Refuse entanglement or self-finality examples until a trusted commitment
   channel is named that does not violate the `T19/T92` access-gap discipline.

## Claim-Status Posture

- No claim promotion is warranted.
- `open-problems/proof-carrying-record-finality.md` remains exploratory.
- `Q1B` stays an externally blocked admissibility protocol; this run only gives
  it cleaner certificate language.
- `TF1` stays an open formal target; this run only identifies the witness side
  of a possible certificate object.
- `T19/T92` remain the main anti-overreach boundary: true facts need not be
  verifier-accessible facts.
