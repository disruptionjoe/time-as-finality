# Technical Report: Weak-Measurement Blackwell Boundary v0.1

## Claim Under Test

Q1C already has three strong gates:

- T143: same-instrument auxiliary channels are null by default after the full
  transcript is treated as the ordinary instrument log;
- T149: a live proposal needs positive decision-risk lift at fixed full record;
- T150: that lift must target a predeclared verdict induced from an
  independently typed axis.

T155 asks whether the null class can be stated in a more general absorber form.

## Result

The finite answer is yes:

```text
if the auxiliary channel is screened off by the full ordinary monitored
transcript, then adding it cannot improve any tested predeclared finite
decision problem about the hidden axis
```

This is not a new measurement law. It is a decision-theoretic restatement of
the current Q1C null class.

## Why This Matters

Without T155, a reader could still think the repo's weak-measurement filter is
too tied to one verdict map or one scoring rule. T155 shows the point is
broader. Under the declared full-transcript reading, a screened-off auxiliary
channel is not merely unhelpful for one specially chosen decision problem. It
is redundant across the tested finite loss family because it leaves the
hidden-axis posterior unchanged once the ordinary transcript is fixed.

## Finite Absorber Shape

Declare:

```text
H = independently typed hidden axis
R = full ordinary event-level ordinary transcript
A = auxiliary channel
L = finite loss table declared before scoring
```

If:

```text
P(H | R, A) = P(H | R)
```

then the optimal Bayes action for `(R, A)` cannot beat the optimal Bayes action
for `R` alone on any loss table drawn from the tested family.

The finite code does not prove the general theorem for all possible losses.
What it does provide is the right absorber posture for this repo:

- screening-off is the real null criterion;
- zero-lift for one verdict map is just one visible consequence;
- any claimed same-instrument lift now bears the burden of showing that the
  ordinary transcript was underdeclared, or that extra structure was present,
  or that the instrument was really enlarged.

## Audited Cases

### 1. Garbled Same-Instrument Meter

The auxiliary value is only another labeling of the same record classes.

Result:

```text
screened off by R
=> equal risk with and without A for every tested loss
```

This is the clearest version of the T143/T149 null class.

### 2. Independent Noise Meter

The auxiliary channel is physically separate noise but carries no hidden-axis
content beyond the ordinary transcript.

Result:

```text
still screened off by R
=> still equal risk for every tested loss
```

This matters because "physically distinct channel" is often treated as if it
were already meaningful. T155 makes clear that physical distinctness alone does
not matter if the posterior over the hidden axis is unchanged.

### 3. Record Already Sufficient

The ordinary transcript already fixes the hidden axis.

Result:

```text
A is redundant even more strongly
```

This case shows that the absorber is not specific to weak measurement. It is a
general decision-sufficiency boundary.

### 4. Extra-Environment Candidate

The auxiliary channel changes the hidden-axis posterior at fixed record.

Result:

```text
not screened off by R
=> positive control improves the tested losses
```

This is the only kind of finite case that deserves further Q1C attention, and
even here T149 and T150 still require architecture typing and verdict honesty.

## What T155 Improves

T155 links the current Q1C gates to a recognizable absorber shape:

- T143 gives the architecture warning.
- T149 gives the conditional decision test.
- T150 prevents verdict gerrymandering.
- T155 says that, when the auxiliary channel is screened off by the full
  transcript, the whole finite decision family collapses with it.

That makes the repo easier to evaluate because the weak-measurement null class
is no longer just "our toy metric happened not to improve."

## What T155 Weakens

It weakens generic second-meter rhetoric further.

The route is not rescued by:

- a new dashboard on the same record;
- a physically distinct but posterior-redundant channel;
- a same-instrument channel whose apparent value disappears once the full
  transcript is treated as the ordinary log.

In short:

```text
screened off by the full transcript
=> not a Q1C decision resource
```

## Boundary Of The Result

This is an absorber, not a universal theorem about every laboratory protocol.

T155 depends on the declared Q1C posture:

- the ordinary record is the full event-level transcript;
- the hidden axis is typed independently of the auxiliary channel;
- the question is whether the auxiliary channel adds decision value once that
  transcript is fixed.

If a real platform can show that `A` changes the hidden-axis posterior at fixed
`R`, the absorber does not kill it. It only says that such a platform must then
be typed honestly as extra environment structure or explicit instrument
enlargement.

## Falsification Condition

T155 fails if either:

1. a screened-off auxiliary channel improves one of the tested finite decision
   problems; or
2. an auxiliary channel that changes the hidden-axis posterior at fixed record
   still fails to improve any tested loss in the positive control.

Either failure would expose a real gap in the current absorber.

## Open Blocker

The repo still has no named monitored-qubit platform where the auxiliary
channel provably changes the hidden-axis posterior at fixed full ordinary
record and can be typed as either extra environment structure or honest
instrument enlargement.

## Claim Ledger Update

Q1C remains `dormant`.

Add this sharpening:

```text
Once the full ordinary transcript screens off the auxiliary channel, that
channel is null across the tested finite decision family, not just for one
chosen verdict map.
```

## Recommended Next Move

Do not search for more same-instrument meters.

Search only for a platform that can expose event-level auxiliary content that
changes the hidden-axis posterior after the full ordinary transcript is fixed.
