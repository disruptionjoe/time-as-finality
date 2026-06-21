# Technical Report: Future Operation Availability Residue Audit v0.1

## Claim Under Test

Multiple recent branches have repeatedly collapsed to a similar residue:
something like "what can still be done?" T119 tests whether that residue is a
genuine cross-branch organizing object, a useful bookkeeping object, or only a
perspective illusion.

The candidate object is Future Operation Availability (FOA):

```text
FOA(O, T, h) = the set of future operations in task universe T that remain
available to observer/system O over horizon h under witness, right,
reconstruction, certification, and maintenance constraints.
```

## Branch Audit

| Branch | What collapsed | What survived | FOA relation |
| --- | --- | --- | --- |
| Q1A | Branch support, reversal cost, and external novelty versus provenance-aware Darwinism. | Audited accessible provenance-class support plus partition visibility. | Weak: becomes FOA only after adding certification or task-use language. |
| ASP | Scalar/replacement primitive readings. | Observer/task-indexed admissible future task set. | Strong: ASP is effectively FOA. |
| Reconstruction debt | Conservation-of-lost-information language. | Missing witnesses matter when later reconstruction or judgment depends on them. | Strong, but expressible as provenance, abstraction, or why-not debt. |
| Maintenance cost | Independent maintenance theory. | Maintained witnesses, rights, and repair paths preserving future operations. | Strong, but absorbed by enriched viability/control/provenance. |
| Provenance | First-class event-finality primitive for colimits and AM. | Audit, identity, custody, attribution, and admissibility evidence. | Strong when future certification, challenge, or repair depends on it. |
| LossKernel | Label-only loss and novelty over rich effects/provenance/lenses. | Source-anchored witness obligations. | Strong when projected targets lose future judgments or repair operations. |
| Admissibility | Seven independent empirical gates. | Smaller structural checklist plus semantic forgotten-structure condition. | Strong at the evidence-protocol layer. |

## Finite Examples

### Example A: FOA differs, existing measures do not

Two repositories have the same endpoint tree and matched entropy,
information, finality, viability, coarse reachability, control rank, and
persistence. One retains merge base, branch history, and signed-history
witnesses; the other is a squashed snapshot.

```text
history-preserved repo: {build, merge, revert, bisect}
squashed snapshot:      {build}
```

This is the strongest finite separation against coarse measures.

### Example B: existing measures differ, FOA does not

Two record archives differ in entropy, information, finality score, viability
score, reachability count, control rank, and persistence. Both retain the same
record/checksum witnesses and read/repair rights.

```text
compressed archive: {read, repair}
redundant archive:  {read, repair}
```

This prevents identifying FOA with ordinary scalar measures.

### Example C: FOA collapses into existing framework

A consensus state with checkpoint, validator signatures, fraud proof, challenge
window, and rollback rights has:

```text
{accept, challenge, rollback}
```

The same checkpoint after challenge witnesses expire has:

```text
{accept}
```

But if reachability analysis includes witnesses, rights, certifications, and
reconstruction paths in the state, it computes exactly the same sets. This is
the strongest absorption control.

## Prior-Art Pressure

| Target | Verdict |
| --- | --- |
| Viability kernels | Absorb FOA when the viability set is future task availability. |
| Reachability analysis | Absorbs FOA when state includes witnesses, rights, certificates, and reconstruction paths. |
| Affordance landscapes | Partial: captures available actions but often omits certification and admissibility tokens. |
| Active inference policy spaces | Absorb FOA if policies range over witness/right-bearing states. |
| Reinforcement-learning action spaces | Partial: executable actions are captured, but reconstruction and certification are usually absent. |
| Opportunity-set economics | Directly absorbs FOA as feasible opportunity set. |
| Capability theory | Partial: close conceptual neighbor, weaker on formal witness debt and certification. |
| Mechanism design | Absorbs rights, incentives, challenge rules, admissible moves, and authority. |
| Commons governance | Absorbs monitoring, sanctioning, repair, public rules, and challenge authority. |
| Control theory | Absorbs FOA when controlled state and admissible controls include record and authority variables. |

## Strongest Version

FOA is not a scalar and not a primitive. The strongest defensible version is a
typed availability set:

```text
FOA = feasible future operation set after witness, right, reconstruction,
certification, maintenance, observer, task, and horizon parameters are fixed.
```

## Weakest Point

FOA is almost entirely absorbed by enriched reachability, opportunity-set,
viability, control, mechanism-design, commons-governance, and provenance
frameworks. It only separates from coarse versions of those frameworks.
Separation from intentionally impoverished prior art is not enough to promote
it.

## Closest Prior Art

The closest formal homes are enriched reachability analysis and
opportunity-set economics. Provenance and mechanism design are closest for the
certification, authority, challenge, and admissibility pieces.

## Strongest Separation Argument

Against coarse measures, FOA separates finite cases where entropy,
information, finality, viability, persistence, coarse reachability, and
control rank all match but future admissible operations differ.

## Strongest Absorption Argument

Once witnesses, rights, certificates, maintenance budgets, and reconstruction
paths are included in the state, FOA is just the feasible
action/reachability/opportunity set. Rich prior art absorbs it.

## Chain Test

The proposed chain:

```text
lost structure
-> reconstruction debt
-> reduced operation rights
-> reduced future operation availability
```

is structurally present in ASP, reconstruction debt, maintenance,
provenance, and LossKernel. Q1A only weakly joins: accessible record support
can support future certification/use, but the current Q1A fixed-data family is
not itself an action-space theory.

## Recommendation

Preserve and formalize narrowly. Do not promote.

FOA is useful as a cross-branch audit normal form because it names the residue
that keeps surviving after scalar or primitive ambitions collapse. It should
not be advertised as a new physical primitive, a replacement for viability or
reachability, or a Nobel-level organizing law. The honest formulation is:

```text
Several branches converge on task-indexed future operation availability once
witnesses, rights, reconstruction paths, certifications, maintenance, observer,
and horizon are made explicit. This convergence is structural but mostly
absorbed by enriched existing frameworks.
```

## Claim Ledger Update

No core claim upgrade. Add T119 as a synthesis audit:

```text
Multiple branches converge on observer/task-indexed future operation
availability as a useful normal form, but the object is absorbed by enriched
reachability, opportunity-set, viability/control, provenance, commons
governance, and mechanism-design frameworks. Preserve narrowly; do not
promote.
```

## Open Blocker

To promote FOA, construct a same-enriched-prior-art quotient witness: same
reachability state, same opportunity set, same control state, same provenance,
same mechanism rights, and same commons-governance variables, but different
FOA verdict. T119 provides no such witness.

## Reproduction

```bash
python -m unittest tests.test_future_operation_availability_residue -v
python -m models.run_t119
```
