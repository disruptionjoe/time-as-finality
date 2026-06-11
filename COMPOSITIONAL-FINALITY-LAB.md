# Compositional Finality Laboratory

## Research Question

When stable records become inputs to larger record systems, what exactly
composes?

The motivating fact-ladder is:

```text
observation -> memory -> testimony -> document -> textbook -> common fact
```

Detail can be discarded at each step while some settled content survives.
T11 asks whether that carry has a general algebra or whether it depends on the
merge, compression, observer, and inherited context.

## Typed Pipeline

The laboratory separates five stages:

```text
stored evidence
  -> inherited context and expression
  -> observer access
  -> finality profile
  -> reconstructed decision
```

Calling every stage "finality" would hide the result.

## Recursive Structure

A record system is a recursively nested tree containing:

- immutable record tokens;
- child record systems;
- local expression marks inherited by descendants.

The evaluator uses an explicit stack. Depth is a runtime parameter rather than
a fixed ontology. Tests cover every depth from zero through 1,024, but the
model makes no claim of infinitely many layers or mathematical fractality.

## Evidence Join

Visible record states merge by token identity and provenance-preserving set
union. For compatible token definitions, this operation is:

- associative;
- commutative;
- idempotent.

It is therefore a join-semilattice at the evidence-state level.

## Finality Profile

For one proposition-value pair:

```text
F = (
  unique accessible provenance,
  distinct holders,
  distinct branches,
  minimum token-erasure cost below threshold
)
```

The profile is evaluated after expression and access. It is not assumed to
inherit the evidence join.

## Checkpoint Policies

Two coarse-graining operations are compared:

1. **lossy checkpoint:** replaces a resolved bundle with one new source;
2. **provenance checkpoint:** replaces the bundle with one token carrying the
   union of hidden source identities.

Both collapse visible holder and branch structure. Only the second preserves
source support.

## Operational Epigenetic Lens

The biological analogy is restricted to three formal operations:

1. stable underlying identity;
2. inherited context-dependent expression state;
3. local reprogramming that changes later expression.

A mark can silence tagged descendant records without deleting them. A later
descendant context can reactivate the same records. This is analogous to
epigenetic regulation only at the level of inherited expression over a stable
substrate.

The model does not claim that social facts, physical records, or recursive
graphs literally use chromatin, genes, organisms, or biological generations.

## Required Counterexamples

T11 must search for:

1. two profiles whose physical merge is not their least upper bound;
2. two locally final records whose merge is unresolved;
3. duplicate tokens that inflate naive support;
4. a coarse-graining that changes finality ordering;
5. locally consistent assignments that do not form one global assignment;
6. one stored record with different inherited expression outcomes.

## Reproduction

```bash
python -m unittest discover -s tests -p "test_*.py" -v
python -m models.run_compositional_finality
```
