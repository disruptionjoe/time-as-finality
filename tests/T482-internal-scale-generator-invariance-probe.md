# T482: Internal Scale Generator Invariance Probe

## Target Claims

- [RG Flow as a Multiscale-Transport Analogy](../open-problems/rg-flow-as-multiscale-transport-analogy.md)
- [T24: D1 Multiscale Observer Field](T24-d1-multiscale-observer-field.md)
- [T38: Minimal Multiscale Transport Formalization](T38-minimal-multiscale-transport.md)
- [T480: Scale-Label Operation Gate](T480-scale-label-operation-gate.md)
- [T481: Internal Scale Structure Admission Gate](T481-internal-scale-structure-admission-gate.md)

## Setup

T481 admits a synthetic future internal-scale packet only as a review target
when the packet predeclares a TaF-native internal generating rule, comparison
domain, positive and negative controls, and relabel-invariance checks.

T482 makes that review target concrete with one finite attempt:

```text
support_depth =
  accessible_support
  + holder_redundancy
  + branch_support
  + reversal_cost
```

The predeclared bands are:

```text
low_support    <= 4
middle_support <= 8
high_support   > 8
```

The comparison domain is the declared T24 observer sites and T38/T480
transport edges. The probe then attacks this candidate with relabeling,
uniform-null, posthoc-threshold, observer-label-order, hidden-time, finality,
RG/conformal, and promotion-shortcut controls.

## Success Criteria

- T481 remains passed and review-only.
- The D1-support-gradient packet is admitted only as review-grade D1
  bookkeeping.
- The stratified T24 packet produces nontrivial bands, while the uniform T24
  null control collapses to one band.
- Observer-label relabeling preserves the generated support-band multiset.
- Label-only, posthoc-threshold, observer-order, hidden-time, duration/arrow,
  finality, RG/conformal, physics, and promotion shortcuts are blocked.
- The result earns no independent internal scale structure, record clock,
  duration, temporal arrow, record-finality change, scale-genesis theorem,
  physics claim, D1 promotion, RG/TaF equivalence theorem, claim-ledger
  movement, roadmap movement, North Star movement, public-posture movement, or
  cross-repo movement.

## Failure Criteria

- A D1 support-depth band is treated as independent internal scale structure.
- Observer label order survives as a generator.
- Thresholds are selected after the separator is known.
- Hidden time/order metadata creates scale, duration, or arrow evidence.
- A support band changes record-finality status.
- RG or conformal fixed-point machinery becomes a TaF internal generator.
- The result promotes D1, scale genesis, physics posture, public posture,
  claim status, or cross-repo truth.

## Known Physics Constraints

RG scale and conformal symmetry remain external analogy material. T482 does not
evaluate RG beta functions, conformal-gravity phenomenology, unitarity,
rotation curves, asymptotic freedom, or quantum gravity.

## Result

Implemented as T482 v0.1.

Expected verdict:

```text
D1_SUPPORT_GRADIENT_PROBE_BUILT_BOOKKEEPING_ONLY_NO_SCALE_STRUCTURE
```

The probe admits a concrete D1-support-gradient review packet, but only as
D1-support bookkeeping because the bands factor entirely through the existing
D1 profile tuple. It earns no independent internal scale structure, record
clock, duration, temporal arrow, finality change, scale-genesis theorem,
physics claim, claim-ledger movement, roadmap movement, North Star movement,
public-posture movement, or cross-repo movement.

## Reproduction

```bash
python -m pytest tests/test_internal_scale_generator_invariance_probe.py -q
python -m models.internal_scale_generator_invariance_probe --write-results
```

Artifacts:

- `models/internal_scale_generator_invariance_probe.py`
- `tests/test_internal_scale_generator_invariance_probe.py`
- `results/T482-internal-scale-generator-invariance-probe-v0.1.json`
- `results/T482-internal-scale-generator-invariance-probe-v0.1-results.md`

## Contribution Needed

Future internal-scale packets should not treat D1 support-gradient bands as
independent scale structure. They must either stay labeled as D1 bookkeeping or
supply an independent TaF-native generator that does not merely factor through
the existing D1 profile tuple, while preserving predeclared comparison domains,
controls, and relabel-invariance checks.
