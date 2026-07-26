# Barandes Stochastic-Quantum Comparison Note

## Status

Open-problem note. This is not a Time as Finality claim upgrade.

## Purpose

Preserve the current judgment on Jacob Barandes' stochastic-quantum
correspondence as a comparison theorem for Time as Finality's quantum-facing
lines.

## Main Relevance To TaF

This is currently the strongest repo-level fit of the three.

TaF already carries pressure on the question:

```text
which parts of quantum-looking behavior require genuinely new finality
structure, and which parts can already be reconstructed inside ordinary
Hilbert-space / channel formalisms?
```

Barandes matters because it gives a precise route:

```text
stochastic process -> CPTP map -> Kraus form -> unitary dilation
```

### 2026-07-26 scope correction

The shorthand must not be read as a dilation of an interventionally complete
multi-time process. In the revised
[Stochastic-Quantum Theorem](https://arxiv.org/html/2309.03085v2), the proof
singles out \(\Gamma(t\leftarrow0)\), and the constructed enlarged process has
\(\widetilde{\mathcal T}_0=\{0\}\). It recovers the distinguished
initial-time transition family after marginalization. It does not show that
one dilation preserves every original conditioning-time kernel, full
trajectory distribution, or held-out intervention.

The exact TaF null-model reading is therefore:

```text
base-time stochastic transition family
    -> nonunique amplitude/Kraus representation
    -> Stinespring/unitary dilation
```

When the target is multi-time history, provenance, memory, or continuation,
the comparator must additionally supply a full process tensor, quantum comb,
or consistent finite-dimensional distribution. Otherwise same base-time data
can hide different intermediate temporal facts.

So it is a good benchmark for:

- `claims/Q1-quantum-under-finalization.md`
- `tests/T10-finality-superselection-rule.md`
- `tests/T131-bell-test-h1-mapping.md`
- `papers/records-finality-readout-separation-v0.1.md`

## Best Use

The best use is as a comparator:

```text
if a TaF quantum-facing proposal is already reproducible by stochastic-unitary
dilation, then TaF has not yet shown distinct finality-side structure.
```

That does not make the proposal false. It means the novelty burden remains open.

## Where It Can Help

### 1. Q1 narrowing

Q1 should not ask TaF to re-derive all of quantum mechanics. A narrower,
cleaner question is:

```text
what extra record/finality/access structure survives after the strongest
stochastic/CPTP/unitary null model has already been granted?
```

### 2. Bell / Hilbert import discipline

`T131-bell-test-h1-mapping.md` already notes that Tsirelson-type bounds require
imported Hilbert-space structure. Barandes gives a disciplined import path.

That is useful in two ways:

- it shows what exactly is being imported,
- it clarifies what TaF would still need to contribute beyond that import.

### 3. Record / readout separation

Barandes cleanly separates stochastic evolution from final subsystem readout.
That supports TaF's existing instinct to keep apart:

- record generation,
- finality or stabilization,
- scalar or semantic readout.

The scope correction adds a fourth separation:

- base-time transition representation versus complete multi-time process.

## What It Does Not Yet Do For TaF

It does not by itself establish:

- finality as a primitive physical relation,
- record-bearing observer constraints,
- domain-relative no-global-commit structure,
- source/readout separation,
- colimit or descent conditions for multi-observer aggregation.

Those are still TaF-side burdens.

## TaF Verdict

The right posture is:

```text
use Barandes as a strong null model and comparison theorem for Q1/T10/T131.
```

The wrong posture is:

```text
treat the theorem as evidence that Time as Finality has already been proved.
```

## Best Next TaF-Side Question

For any future Q1 or Bell-facing note, require this split:

1. what is explained by stochastic/CPTP/unitary dilation alone,
2. what requires record/finality/access structure that survives that absorber.
