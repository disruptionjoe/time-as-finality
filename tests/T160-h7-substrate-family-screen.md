# T160: H7 Substrate-Family Screen

## Route

Thermodynamic arrow of time.

## Target Claims

- [H7: Finality-Induced Direction](../claims/H7-finality-induced-direction.md)
- [Arrow of Time as Constructor Theorem](../open-problems/arrow-of-time-as-constructor-theorem.md)
- [H7 Physical-Deletion Substrate Handoff](../open-problems/h7-physical-deletion-substrate-handoff.md)

## Question

After T152 and N8, which broad substrate families should be treated as null by
default for H7's physical-arrow reinstatement gate, and what extra burden would
an exception have to clear?

## Motivation

The H7 program already has a sharp reinstatement condition:

```text
find a physically typed record substrate whose physical-deletion reverse
remains constructor-impossible after full absorber accounting
```

But the practical screening rule is still too loose. Future work can waste time
reopening the same null families under new words: protected memories, driven
steady states, gauge/superselection restrictions, or horizon-style
inaccessibility. T160 turns the existing absorber logic into a family-level
triage screen.

## Setup

T160 audits four common substrate families against the post-T145/T148/T152/N8
gate:

1. `protected_memory_family`
   Error-correcting, topological, or code-distance-protected memories.
2. `driven_dissipative_family`
   Pumped, biased, or nonequilibrium-maintained records.
3. `superselection_or_gauge_family`
   Claimed deletion impossibility from exact sector or gauge restrictions.
4. `horizon_or_access_family`
   Claimed deletion impossibility that is really observer inaccessibility or
   one-way causal separation.

Each family is judged against the same frozen burden:

```text
reverse_edge_class = physical_record_deletion
absorber vector matched
allowed control class stated
finite substrate reading supplied
future-operation split survives matching
reverse_status = constructor_impossible_after_full_accounting
```

## Success Criteria

- Protected memories are null by default unless code distance, syndrome access,
  bath/reset channels, and finite control class still leave deletion
  impossible.
- Driven dissipative records are null by default unless the claimed arrow
  survives matched pumping, bias, chemostat, or free-energy accounting.
- Superselection or gauge stories are null by default unless they produce a
  finite substrate-native impossibility rather than an exact ideal-sector ban.
- Horizon or access-loss stories are null by default because they change
  observer reachability, not record deletion.
- The result sharpens the H7 handoff without promoting any physical-arrow
  reading.

## Failure Criteria

- Treating long memory lifetime or code protection as deletion impossibility by
  itself.
- Treating maintained nonequilibrium bias as H7 residue after energy and sink
  bookkeeping are restored.
- Promoting exact gauge or superselection idealizations without a finite
  operational substrate reading.
- Confusing inaccessible records with destroyed records.

## Claim Impact

H7 remains `weakened_conditional`.

Add this screen:

```text
Protected memory, driven dissipation, exact sector restriction, and
horizon-style inaccessibility are all null H7 substrate families by default.
They reopen H7 only if a proposal freezes the reverse-edge class,
substrate-specific absorber vector, allowed controls, and future-operation
target, then still shows finite substrate-native constructor impossibility of
physical record deletion.
```

## Reproduction

This artifact is a claim-triage screen over the existing H7 obstruction stack.
There is no new executable model beyond the cited tests and absorber notes.
