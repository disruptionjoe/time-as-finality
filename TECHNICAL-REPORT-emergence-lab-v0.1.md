# Emergent Records Across Reversible And Irreversible Local Dynamics

## Abstract

The first Time as Finality model assigned records directly. This laboratory
asks whether records and finality profiles arise from explicit dynamics.
Across all 256 elementary binary cellular-automaton rules and reversible
second-order lifts, we define a record as a counterfactual influence trace:
flipping one seed bit changes later cells. Actual Boolean sensitivity supplies
causal edges, and bounded terminal windows supply candidate observer access.

The comparison establishes a shared mathematical core: local dynamics can
generate causal record traces, and access to those traces is observer-relative
whether the global transition is reversible or irreversible. It also rejects
a stronger unification. Logical information loss, thermodynamic Landauer
cost, computational inversion, trace persistence, and observer accessibility
are distinct. Three of the proposed four finality dimensions collapse in the
simplest binary trace model. The laboratory therefore supports finality as a
comparative framework for observer-indexed records, not as one universal
mechanism of irreversibility.

## 1. What Was Made To Emerge

The original T1 graph contained hand-authored record tokens. Here the rule
generates the record.

For seed cell `s` and terminal cell `e`:

```text
record(s,e) = state(e | flip(s)) XOR state(e | baseline)
```

This is a counterfactual causal trace. It is intrinsic to the rule, initial
state, boundary condition, and chosen causal depth. It does not require an
external observer to recognize a glider or decide what pattern matters.

The same definition runs unchanged on an irreversible elementary CA and its
reversible second-order lift.

## 2. What Was Still Supplied

The laboratory does not derive everything:

- the local update rule is supplied;
- the lattice and periodic boundary are supplied;
- causal update layers are supplied, though no metric duration is;
- the seed intervention is supplied;
- the observer is a selected bounded terminal window;
- semantic propositions and conscious experience are absent.
- collective confidence formation, proof verification, and explicit
  coarse-graining are absent; these are tested separately in
  [T10](tests/T10-proof-carrying-metastable-finality.md).

The honest result is emergence of records from dynamics, not emergence of
time or observers from nothing.

## 3. Substrates

The irreversible comparison uses elementary cellular automata, with Rule 110
as the detailed example and all 256 rules in the sweep.

The reversible comparison uses:

```text
(previous, current)
  -> (current, rule(current) XOR previous)
```

The inverse is:

```text
previous = rule(current) XOR next
```

Every state of every width-five second-order lift in the 256-rule sweep was
checked for injectivity.

## 4. Causal And Observer Structure

An edge exists when changing one parent bit changes one child bit under the
actual neighborhood state. This Boolean-derivative graph is
trajectory-specific. It avoids treating every geometrically possible parent
as an actual influence.

An observer window receives only terminal trace cells inside its bounded
region. Equal-size translated windows can therefore disagree about whether a
record exists without disagreeing about the underlying dynamics.

This is the strongest cross-substrate result:

> Observer-relative record access does not require global logical
> irreversibility.

## 5. Reversal Is Not One Quantity

Four quantities were compared on shared systems.

1. **Causal trace cost:** how many accessible outputs carry the seed's
   influence.
2. **Graph intervention cost:** how many observed terminal bits must change to
   erase that trace.
3. **Computational reversal:** whether a direct inverse exists, how many
   preimages exist, and what finite enumeration requires.
4. **Thermodynamic information-loss bound:** `k_B T ln(2) H(X|Y)` for
   degenerate binary memories, a 300 K heat bath, quasistatic reset, and
   uniform input.

The reversible witness has a nonzero record trace and graph intervention cost
but zero information-loss bound. Conversely, an irreversible rule can lose
information globally while a bounded observer receives no trace of a
particular seed.

Therefore:

```text
record persistence != logical irreversibility
logical irreversibility != observer accessibility
graph intervention count != thermodynamic work
brute-force inversion != computational irreducibility
```

## 6. Rule-Sweep Result

The complete width-five sweep finds a correlation of approximately `-0.72`
between information loss and three-layer trace survival. More information
loss generally means fewer perturbation traces survive.

But explicit rule pairs break identity in both directions:

- equal loss, different survival;
- equal survival, different loss.

Finality cannot be reduced to transition-map entropy loss alone.

## 7. What Happened To D1

D1 proposed four dimensions: accessible support, redundancy, independent
branch support, and reversal cost.

The emergence test produces a mixed verdict:

- accessibility survives and remains observer-indexed;
- branch structure can vary independently;
- raw binary support, redundancy, and terminal intervention cost collapse to
  the same Hamming count;
- thermodynamic reversal cost remains separate but belongs to a physical
  implementation model, not the causal graph alone.

D1 is therefore weakened from a candidate universal physical structure to a
comparative schema whose dimensions must be justified separately for each
substrate.

## 8. Computational Irreducibility

Rule 110 is computationally universal in its established infinite
construction. The laboratory's width-five periodic system is not that
construction.

The lab measures exact finite preimages and distinguishes a direct inverse
from exhaustive enumeration. It does not prove that any trajectory lacks a
shortcut. Israeli and Goldenfeld further show why such a claim would need
care: microscopic computational irreducibility can coexist with reducible
coarse-grained behavior.

Computational irreducibility remains a possible substrate-specific source of
reversal difficulty, not a demonstrated result here.

## 9. Classification

| Candidate aspect | Verdict | Reason |
| --- | --- | --- |
| counterfactual influence trace | universal structure in this lab | same definition works on both substrate classes |
| causal sensitivity graph | universal structure in this lab | derived by Boolean dependence in both |
| observer-relative accessibility | universal structure in this lab | bounded windows differ under identical dynamics |
| trace persistence | substrate-specific | varies by rule, state, seed, and depth |
| logical information loss | substrate-specific | absent from every reversible lift |
| Landauer lower bound | substrate-specific physical mechanism | follows transition-map information loss under a memory model |
| graph reversal count | model-specific structural measure | collapses with support in the raw binary model |
| computational irreducibility | unproven | finite search is insufficient |
| experienced time | analogy / open bridge | no conscious observer or succession model |
| finality as one universal force | rejected | distinct quantities do not reduce to one mechanism |

## 10. Verdict

The Emergence Laboratory finds a real but narrower shared structure:

> Local dynamics can propagate counterfactual traces through causal
> dependency networks, and bounded systems can have different access to those
> traces.

That is enough to support a substrate-neutral science of observer-indexed
records.

It is not enough to support a universal mechanism called finality.
Thermodynamic irreversibility, computational inversion, causal propagation,
and record accessibility remain distinct mechanisms connected by a
comparative vocabulary.

## 11. Next Decisive Experiment

Make the observer dynamical. Build a persistent subsystem that:

1. receives local traces;
2. stores them across updates;
3. compares current input with retained state;
4. changes future behavior based on that comparison.

If such a reconciler can arise and preserve an internally usable record
without an externally selected terminal window, the project will have moved
from emergent traces to emergent record-bearing systems. If it cannot, the
observer-indexing remains an imposed analytical perspective.
