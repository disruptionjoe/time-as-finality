# Noisy Measurement Access-Boundary Discriminator

## Abstract

T62 extends the T2/T22 quantum-measurement thread from ideal records to noisy
binary readout channels. It asks a narrow question: after noisy environmental
record formation, does Time as Finality add anything beyond decoherence and
Quantum Darwinism?

The answer is conservative. T62 does not support a new measurement-dynamics
claim. It supports an access-boundary discriminator:

```text
decohered != environmentally redundant != final for this observer
```

In the executable witness matrix, pointer decoherence, total environmental
redundancy, and observer-relative D1 finality can agree, but they can also
separate. The strongest Q1 claim is therefore weakened: Q1 adds explicit
observer-access and independence bookkeeping over classical record
availability. It does not explain decoherence itself.

## 1. Model

The model uses a uniform binary pointer variable and finite noisy readout
fragments. Each fragment has:

- readout reliability;
- pointer-coherence suppression factor;
- holder identity;
- independence class;
- branch id.

For a binary symmetric readout channel:

```text
I(S;F) = 1 - H_2(error)
error = 1 - reliability
```

A fragment contributes to raw Quantum-Darwinism-style `R_delta` when its
mutual information crosses the declared threshold. It contributes to D1 holder
redundancy only when it is inside the observer's access window and belongs to
a distinct independence class.

Pointer coherence is tracked by a simple product proxy:

```text
coherence_final = 0.5 * product(fragment.decoherence_factor)
```

This is a channel-level audit, not a Hamiltonian derivation.

## 2. Witness Matrix

| Witness | Purpose |
| --- | --- |
| `redundant_accessible_control` | Decoherence, total redundancy, and observer D1 finality agree. |
| `decohered_not_darwinist` | Many weak scatterers suppress pointer coherence, but no fragment crosses the information threshold. |
| `redundant_but_inaccessible` | Environmental records are redundant, but the observer has no access window. |
| `raw_duplicate_boundary` | Raw fragment count crosses threshold, but one fragment is a correlated duplicate. |

The result table is written by `python -m models.run_t62`.

## 3. Claim Impact

Q1 remains `partially_supported`, but the content is narrower than an
independent measurement claim. The supported statement is:

> Given a pointer basis, fragment partition, information threshold, observer
> access boundary, and independence criterion, D1 can distinguish decohered
> states, redundant environmental records, and records finalized for a specific
> observer.

This does not compete with decoherence or Quantum Darwinism. In fact, the
`decohered_not_darwinist` witness is already naturally described by standard
decoherence-versus-redundancy language. TaF's additional content appears only
when observer access or fragment independence is load-bearing.

## 4. What This Weakens

T62 weakens any broad reading of Q1 that suggests TaF predicts how noisy
decoherence happens. It does not. Decoherence dynamics and redundant record
formation remain explained, if at all, by ordinary quantum dynamics and
Quantum-Darwinism-style analysis.

T62 also forces D1 holder redundancy to inherit Quantum Darwinism's fragment
partition discipline. If the independence classes are arbitrary, D1 adds only
terminology.

## 5. Falsification Condition

Q1 loses independent measurement content if either condition holds:

1. physically justified observer access boundaries and independence classes
   cannot be specified in a detector-level model;
2. once those boundaries and classes are specified, every D1 finality predicate
   reduces to standard `R_delta` or ordinary decoherence predicates.

## 6. Limits

- No Hamiltonian is supplied.
- The pointer basis is declared, not dynamically selected.
- No Born-rule or collapse claim is made.
- Threshold sensitivity is not swept away; it is now a required next audit.
- Branch support and reversal cost remain proxy-level in this measurement
  model.

## 7. Recommended Next

Build a detector-level version: a noisy Stern-Gerlach or photon-scattering
readout with explicit fragment partition, access window, threshold sensitivity,
and no-signalling checks.

## 8. Reproduction

```bash
python -m unittest tests.test_noisy_measurement_access_boundary -v
python -m unittest discover -s tests -p "test_*.py" -v
python -m models.run_t62
```

Machine-readable output:

- [results/noisy-measurement-access-boundary-v0.1.json](results/noisy-measurement-access-boundary-v0.1.json)

Human-readable result note:

- [results/noisy-measurement-access-boundary-v0.1-results.md](results/noisy-measurement-access-boundary-v0.1-results.md)
