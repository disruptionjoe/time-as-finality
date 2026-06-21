# D1 Physical Reduction Map and Observable Audit

## Abstract

T22 audits whether D1 finality can be read as physical observable content
rather than only a useful graph formalism.

The result is mixed and intentionally conservative. T22 gives holder
redundancy a first executable physical reduction in a small
system-environment toy model: after fixing a pointer basis, fragment
partition, observer access boundary, and information threshold, D1 holder
redundancy agrees with an independence-corrected Quantum-Darwinism-style
`R_delta` count.

This does not physically derive D1. Accessible support is measurable but
observer-boundary dependent. Branch support and reversal cost remain formal
only until stronger physical independence and cost models are supplied.

## 1. Confidence Vocabulary

T22 uses four confidence levels:

| Level | Meaning |
| --- | --- |
| physically supported | The observable has a stable physical definition across the declared substrate class. |
| partially supported | The observable is measurable after explicit substrate assumptions are fixed. |
| formal only | The dimension is structurally useful, but no settled physical observable is supplied. |
| failed/rejected | A proposed reduction fails or should not be used. |

No D1 dimension reaches `physically supported` in T22 v0.1.

## 2. Reduction Map

| D1 dimension | Candidate physical observable | Substrate assumptions | Lorentz/frame status | Supporting tests | Falsification conditions | Confidence | Current verdict |
| --- | --- | --- | --- | --- | --- | --- | --- |
| accessible support | Count or measure of observer-readable record fragments carrying nonzero information about the target event inside a declared causal access boundary. | Access boundary, stable readout channels, fixed observer readout rule and threshold. | Observer-window dependent; should be stated through causal access or world-tube relations rather than coordinate simultaneity. | T1, T9, T20, T22 | If accessible support is always identical to total support, the access axis adds no content. If no local access boundary can be stated, the observable is underspecified. | partially supported | Measurable once the observer access boundary is declared. |
| holder redundancy | `R_delta`-style count of disjoint, observer-accessible environment fragments or fragment families whose mutual information with the pointer state exceeds a declared threshold. | Fragment partition, pointer basis, fixed delta, and explicit treatment of correlated duplicate fragments. | Partition and observer-access dependent, but executable once the partition and access boundary are fixed. | T20, T21, T22 | If holder redundancy never differs from raw fragment count, D1 should not claim an independence-sensitive axis. If no operational partition exists, the reduction is only formal. | partially supported | Strongest current physical traction; T22 supplies an executable check. |
| branch support | Count of causally independent record channels, branch families, or domain-cover sections supporting the same event. | Channel-independence criterion, no double-counting within one branch, explicit local domain cover or causal graph. | Covariance is open; independence should be causal or cover-theoretic, not an equal-time slice. | T13, T16, T21, T22 | If branch support always collapses to holder redundancy, it should not remain a separate D1 axis. If independence cannot be invariantly stated, the physical reduction fails. | formal only | Structurally useful, but physical observable status remains open. |
| reversal cost | Minimum intervention budget needed to erase, invert, or make unreconstructible the supporting records under a named cost model. | Declared cost model, access-level distinction, fixed reconstruction threshold. | Substrate dependent; not currently a Lorentz scalar and not identified with thermodynamic work by default. | T1, T5, T9, T18, T22 | If reversal cost always collapses to standard thermodynamic work, D1 should defer to thermodynamics. If cost models reverse the ordering with no principled choice, the axis remains formal only. | formal only | Audited but not physically reduced; universal thermodynamic-work identity is rejected. |

## 3. Executable Model

The T22 toy model is a classical readout shadow of a
system-environment measurement setup.

```text
system prior: P(S0) = 0.5, P(S1) = 0.5
system entropy: 1.0 bit
delta: 0.1
information threshold: 0.9 bits
observer access: E1, E2, E3, N1
hidden informative fragment: E4
```

Fragment information:

| Fragment | Observer accessible? | Independence class | Branch | I(S;fragment) |
| --- | --- | --- | --- | ---: |
| E1 | yes | left_channel | left | 1.0 |
| E2 | yes | right_channel | right | 1.0 |
| E3 | yes | left_channel | left | 1.0 |
| E4 | no | hidden_channel | hidden | 1.0 |
| N1 | yes | noise_channel | noise | 0.0 |

The scenario intentionally includes `E3`, a full pointer record that shares
the same independence class as `E1`. This tests whether D1 holder redundancy
tracks raw copies or independent accessible fragment families.

## 4. T22 Result

The executable D1 profile is:

```text
(accessible support, holder redundancy, branch support, reversal cost)
= (3, 2, 2, 2)
```

The Quantum-Darwinism-style comparison is:

| Quantity | Value |
| --- | ---: |
| raw accessible `R_delta` fragments | 3 |
| raw total `R_delta` fragments | 4 |
| independence-corrected accessible `R_delta` | 2 |
| D1 holder redundancy | 2 |

Interpretation:

- `E1`, `E2`, and `E3` are accessible and exceed the information threshold.
- `E4` also exceeds the threshold, but it is outside the observer access set.
- `N1` is accessible but carries zero pointer information.
- Raw accessible `R_delta` is `3`.
- Independence-corrected accessible `R_delta` is `2`.
- D1 holder redundancy agrees with the independence-corrected value.

This supports a conditional reduction:

```text
D1 holder redundancy =
independence-corrected accessible R_delta
```

but only after the pointer basis, fragment partition, access boundary, delta
threshold, and independence classes are declared.

## 5. Claim Impact

T22 strengthens [D1](claims/D1-physical-finality-definition.md) by replacing
an implicit "these four graph dimensions might be physical" posture with an
auditable reduction map. The correct current claim is:

```text
D1 is a candidate observable program, not a completed physical definition.
```

T22 strengthens [Q1](claims/Q1-quantum-under-finalization.md) only narrowly.
It gives the quantum-Darwinism comparison requested by T2 a first executable
toy check. It does not simulate decoherence, collapse, detector behavior, or
quantum amplitudes.

T22 narrows [T21](tests/T21-bell-contextuality-finality.md). Bell/CHSH
contextuality remains a physical referent for local finality without global
assignment, but it does not by itself make D1's four dimensions physical
observables.

## 6. Limits

- T22 does not prove quantum Darwinism.
- T22 does not derive D1 from quantum mechanics.
- The toy model is classical and finite.
- Holder redundancy depends on a declared fragment partition.
- Branch support remains a formal or cover-theoretic placeholder.
- Reversal cost remains a named cost-model slot, not thermodynamic work.
- No D1 dimension is currently established as a universal physical scalar.

## 7. Repo Recommendation

D1 can honestly claim the following next:

```text
D1 has a candidate physical reduction map.
Holder redundancy has the first executable physical traction.
Accessible support is physically measurable but observer-boundary dependent.
Branch support and reversal cost remain formal-only in strong claims.
```

Follow-on status: [T2](tests/T2-quantum-measurement-record-finality.md) now
tests T22 against a less hand-declared system-apparatus-environment model.
The next high-value work is to make that substrate noisy: partial scattering,
detector inefficiency, and pointer-basis selection from the coupling
structure.

## 8. Reproduction

```bash
python -m unittest tests.test_d1_physical_reduction_map -v
python -m unittest discover -s tests -p "test_*.py" -v
python -m models.run_t22
```

Machine-readable output:

- [results/d1-physical-reduction-map-v0.1.json](results/d1-physical-reduction-map-v0.1.json)

Human-readable result note:

- [results/d1-physical-reduction-map-v0.1-results.md](results/d1-physical-reduction-map-v0.1-results.md)
