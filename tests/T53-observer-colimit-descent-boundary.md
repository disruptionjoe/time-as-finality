# T53: Observer-Colimit Descent Boundary Audit

## Target Claims

- [C1: Experienced Time As Record Finality](../claims/C1-experienced-time-as-record-finality.md)
- [D1-Field: Multiscale Observer Finality](../claims/D1-field-multiscale-observer-finality.md)
- [T47: PO1 DAG Theorem](T47-po1-dag-theorem.md)
- [T48: FinaliEvent Structure](T48-finali-event-structure.md)
- [T50: Axis Monotonicity Theorem](T50-axis-monotonicity-theorem.md)
- [T51: Multi-Observer Apparent Finality Colimit](T51-multi-observer-apparent-finality-colimit.md)

## Central Question

After T51-style observer colimits restore phantom incomparabilities, what can
still fail?

T53 distinguishes:

```text
valid partial order
  !=
unique global event-finality completion
  !=
axis-reconstructable temporal order
```

The test asks whether bounded observer views determine a canonical
event-finality structure, or whether additional descent data are required.

## Competing Hypotheses

H0: T51/T52-style positive colimits cover all meaningful multi-observer merges.

H1: Every compatible observer merge has a unique canonical event-finality
completion.

H2: Partial-order validity can hold while uniqueness requires extra descent
data.

H3: Record-order colimits can remain valid while finality-axis reconstruction
fails.

H4: Some boundary failures are hidden-record repairable; others remain
noncanonical.

H5: A stronger descent-style formalism is required beyond pointwise record
union.

## Executable Witnesses

1. `t51_positive_control`
   - Inherited T51-style witness.
   - One bounded observer misses a predecessor record.
   - The unique completion restores the hidden ordering and satisfies AM.

2. `ambiguous_event_identity`
   - Two observers see locally identical two-event chains.
   - The data do not decide whether these are the same chain or two disjoint
     chains.
   - Multiple compatible completions remain.

3. `axis_failing_valid_colimit`
   - Record containment gives a valid partial order.
   - The causal finality axis decreases along a record dependency.
   - AM fails while the record-order colimit remains valid.

4. `hidden_record_repair`
   - Apparent records and axis profiles disagree.
   - Adding one hidden predecessor record restores AM.
   - The case separates repairable incompleteness from arbitrary completion.

5. `nondefinable_overlap_boundary`
   - A proposed completion lacks an event map for one observer.
   - Projection is not definable, so no colimit verdict is meaningful.

## Success Criteria

T53 succeeds if it produces:

- at least one inherited positive T51-style case;
- at least one underdetermined observer merge;
- at least one axis-valid colimit;
- at least one axis-failing colimit;
- at least one hidden-record repair case;
- at least one nondefinable overlap boundary;
- a clear statement of what descent data are required.

## Failure Criteria

T53 fails if:

- every compatible observer merge is automatically unique;
- axis reconstruction never fails independently of partial-order validity;
- hidden-record repair cannot be distinguished from arbitrary noncanonical
  completion;
- nondefinable overlap maps are incorrectly treated as ordinary colimits.

## Non-Goals

- Do not redo a symmetric positive T52-style witness.
- Do not claim that T47-style partial-order consistency fails for well-formed
  PO1-admissible event structures.
- Do not treat observer disagreement as evidence for subjective reality.
- Do not require full sheaf or descent machinery unless the finite witnesses
  force it.

## Expected Scientific Value

T51 showed that apparent incomparability can be a bounded-access artifact.
T53 asks whether the repaired global structure is canonical.

The expected result is a finite boundary theorem:

```text
T47 acyclicity can protect partial-order consistency,
but canonical observer-relative temporal reconstruction also requires
event identity maps, sufficient overlap data, and AM-compatible axis profiles.
```
