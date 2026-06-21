# Technical Report: Gap Presheaf Classification v0.1

## Scope

T113 tests whether the finite gap assignment

```text
G(U) = A(U) - F(U)
```

classifies phantom incomparability witnesses from the existing T51/T52/T53/T56/T57/T58
family.

The audit uses:

- T51 and T52 well-formed phantom incomparability witnesses via T58.
- T53 descent-boundary cases, including noncanonical hidden-record repairs.
- T56 hidden-intermediary H0 gap witness.
- T57 full record-lattice FRP and gap-restriction witnesses.
- T58 local-reversal control plus a second malformed `F(U) not subset A(U)` control.

## Definition Tested

For each observer patch `U`:

```text
A(U) = ambient global event-finality order restricted to U-accessible endpoints
F(U) = observer-local apparent order
G(U) = A(U) - F(U)
```

Raw `H0(G)` is represented in the executable audit as all computed gap sections.
The typed candidate subobject keeps only sections satisfying:

- both endpoints are accessible at `U`;
- the ambient completion is canonical;
- `F(U) subset A(U)`;
- the pair is locally incomparable, not locally reversed or conflicting.

## Result

The finite audit refutes raw `H0(G)` as a classifier and supports the typed
subobject.

```text
raw gap sections:      13
phantom sections:      10
extra raw gaps:         3

typed gap sections:    10
phantom sections:      10
extra typed gaps:       0
missing typed gaps:     0
```

The extra raw gaps are diagnostic:

- two T53 hidden-record-repair gaps that depend on a noncanonical completion;
- one T58 local-reversal gap where `F(U)` is not a suborder of `A(U)`.

## FRP Closure

The T57 restriction-closure checks remain intact:

```text
hidden_intermediary_record_lattice: holds
branching_dependency_record_lattice: holds
```

The audit also preserves the T57 non-lifting boundary: smaller patches can have
additional gaps that do not lift from larger patches.

## Negative Controls

Malformed/local-reversal controls are rejected before gap sections are called
phantom witnesses.

```text
local_reversal: invalid_local_order_control
malformed_extra_local_order: invalid_local_order_control
```

This keeps local conflict separate from phantom incomparability.

## Conservative Claim

Supported in the tested finite family:

```text
The endpoint-accessible, canonical, well-formed local-incomparability subobject
of H0(G) classifies phantom incomparability witnesses.
```

Not supported:

```text
Raw H0(G) classifies phantom incomparability.
```

## Guardrails

This result does not validate Geometric Unity, does not establish physical
torsion, does not prove that `F` sheafifies to `A`, and does not derive the
direction of finality arrows. "Torsion-like gap" remains an analogy unless it
is explicitly tied to the typed TaF-native object tested here.

## Reproduction

```bash
python -m pytest tests/test_gap_presheaf_classification.py -q
python -m pytest tests/test_gap_phantom_equivalence.py tests/test_finality_reflection_property.py tests/test_observer_colimit_descent_boundary.py -q
python -m models.run_t113
```

Artifacts:

- `results/gap-presheaf-classification-v0.1.json`
- `results/gap-presheaf-classification-v0.1-results.md`
