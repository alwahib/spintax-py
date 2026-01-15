# Python vs JavaScript spintax usage

This guide shows how to use `spintaxpy` alongside the original JavaScript `spintax` library ([GitHub](https://github.com/johnhenry/spintax)). The core syntax and outputs match so you can port templates between Python and JavaScript without rewriting patterns.

## Quick parity table

| Scenario | Python (`spintaxpy`) | JavaScript (`spintax`) |
| --- | --- | --- |
| Basic parse | `list(parse("Hi {a\|b}"))` | `[...spintax.parse('Hi {a\|b}')]` |
| Count combos | `count("{a\|b\|c}")` | `spintax.count('{a\|b\|c}');` |
| Pick one | `choose("{red\|blue}")()` | `spintax.choose('{red\|blue}')();` |
| Numeric ranges | `list(parse("{1,3}"))` | `[...spintax.parse('{1,3}')]` |
| Custom delimiters | `parse("[x\|y]", pattern_start="[", pattern_end="]")` | `spintax.parse('[x\|y]', { patternStart: '[', patternEnd: ']' })` |
| Custom separators | `parse("{A;B}", separator_choices=";")` | `spintax.parse('{A;B}', { separatorChoices: ';' })` |
| Back references | `list(parse("{foo\|bar} {$0}"))` | `[...spintax.parse('{foo\|bar} {$0}')]` |
| Deterministic choice | `choose(...)(0, 1)` | `spintax.choose(...)(0, 1);` |
| Lazy iteration | generator (default) | iterator (default) |

## Usage side-by-side

### Expanding choices

```python
# Python
from spintaxpy import parse
list(parse("Hello {world|friend}"))
# ['Hello world', 'Hello friend']
```

```js
// JavaScript
import spintax from 'spintax'
[...spintax.parse('Hello {world|friend}')]
// ['Hello world', 'Hello friend']
```

### Counting combinations

```python
from spintaxpy import count
count("{small|large} {box|circle}")  # 4
```

```js
import spintax from 'spintax'
spintax.count('{small|large} {box|circle}'); // 4
```

### Choosing one combination

```python
from spintaxpy import choose
picker = choose("{red|blue} {box|circle}")
picker(0, 1)  # 'red circle' (deterministic)
picker()      # random pick
```

```js
import spintax from 'spintax'
const picker = spintax.choose('{red|blue} {box|circle}')
picker(0, 1) // 'red circle' (deterministic)
picker()     // random pick
```

### Ranges and steps

```python
list(parse("{0,10,5}"))
# ['0', '5', '10']
```

```js
[...spintax.parse('{0,10,5}')]
// ['0', '5', '10']
```

### Custom delimiters and separators

```python
parse("[A;B]", pattern_start="[", pattern_end="]", separator_choices=";")
```

```js
spintax.parse('[A;B]', { patternStart: '[', patternEnd: ']', separatorChoices: ';' })
```

## Behavioral notes

- Iteration order matches: rightmost pattern changes fastest.
- Whitespace: ranges ignore whitespace; choices preserve it, in both libraries.
- Back references use `{$n}` (0-based) in both libraries.
- Random picks: both use their language RNG. In Python, seed with `random.seed(...)`; in JS, seedable RNG is not built-in—use indices or a third-party seeded RNG if you need reproducibility.
- Python returns generators; JS returns iterators. Both are lazy; convert to list/array if you need materialized results.

## Capabilities: one vs the other

- Available in Python only: none of the core features—parity is intended. Python exposes `spintax_range` for convenience, but you can get the same numbers via `{start,end,step}` in templates.
- Available in JavaScript only: the tagged template helper `compile` exists in JS; Python intentionally omits it because tagged templates are JS-specific.
- Reproducible randomness: Python can be seeded with `random.seed`; JavaScript requires external seeding or using deterministic indices.

If you stay within the shared syntax (choices, ranges, back references, custom delimiters/separators), templates are interchangeable between the two implementations.
