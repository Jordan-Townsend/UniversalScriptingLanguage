# Lua 5.4 bounded integer/control translation

`usl.lua54.bounded-int64-control.v1` translates actual Lua source to the shared
typed/effect IR and then to Python, ECMAScript BigInt or Ruby. It parses with the real
Tree-sitter Lua grammar, independently compiles the source with native Lua
`loadfile`, and probes the installed runtime for Lua 5.4 signed-64 integers.
Parsing does not execute the source.

Lua integer addition, subtraction, multiplication and negation wrap on overflow.
The admitted subset never substitutes mathematical integer semantics for a
possible wrap: an independent conservative interval interpreter rejects any
source operation whose result may leave `[-2^63, 2^63-1]`. The shared IR checker
reruns that interpreter; a stored `integer_safety` flag is not sufficient.
Division uses floor rounding; modulo has the divisor's sign. Native division
and modulo error names/messages and stdout prefixes remain observable.

The profile accepts decimal integer and boolean literals, initialized local
scalar variables, ordinary assignment, arithmetic, comparisons, strict boolean
logic, single-argument scalar `print`, lexical blocks, `if`/`elseif`/`else`, and
finite integer numeric `for`. Numeric-for bounds evaluate once; positive and
negative strides, inclusive endpoints, variable lifetimes, local shadowing and
body mutation of the visible counter are preserved. The endpoint sentinel may
be a mathematical integer just outside signed-64 range: that generated range
sentinel is explicitly distinguished from source arithmetic. Each loop has at
most 4,096 iterations; the verification pass has a 100,000-step budget.

Acyclic local functions declared before executable statements require an
independently supplied parameter/return contract. The entire parameter domain
must pass integer safety, and every admitted call must stay in that domain:

```python
source = 'local function twice(n) return n*2 end print(twice(21))'
signatures = {
    'twice': {
        'contract_version': 'usl.lua54.bounds.v1',
        'parameters': {'n': 'int'},
        'returns': 'int',
        'bounds': {'n': [-100, 100]},
    }
}
```

Integer parameters need signed-64 inclusive bounds; boolean parameters need no
numeric bounds. Accepted functions return one integer or boolean on every path,
may call already declared local functions and may produce scalar stdout.
Captured outer locals, future local function references, recursion and imports
are rejected. Function calls in numeric-for bounds are rejected while their
evaluation/effect contract remains unimplemented.

Run the qualification with the normal environment activated:

```bash
python -m unittest tests.test_v47_lua
python -m tools.qualify_semantic_lua
```

The qualification uses independently authored expected output/errors and native
original Lua versus generated Python/JavaScript/Ruby execution. It includes signed-64
extrema, precision beyond JavaScript Number, floor/modulo signs, evaluation-order
stdout traces, short circuiting, loop scope and snapshots, bounded functions,
seeded heldout arithmetic workloads and rejection cases. Its JSON records fresh
runtime/source/implementation identities and the actual generated code.

Still outside the profile are floats, `/`, tables, strings, metatables, coercion,
implicit truthiness, varargs, multiple values, globals, closures, attributes,
generic iterators, while/repeat, coroutine/concurrency APIs, modules, libraries,
native ABI and full standard conformance. Integer safety proves the declared
arithmetic model under recorded assumptions. Finite differential and intent
contracts qualify those tested inputs. Neither is a universal semantic
translation proof or proof of arbitrary original human intent.

Specification: [Lua 5.4 reference manual](https://www.lua.org/manual/5.4/manual.html),
especially arithmetic §3.4.1, numeric for §3.3.5 and function calls §3.4.10.
