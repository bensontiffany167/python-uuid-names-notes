# Create deterministic namespaced identifiers: implementation

## What the example does

UUID5 hashes a namespace and name so the same pair produces the same identifier. It is not random and should not be used as an unpredictable access token.

The public function is `solve(value)`. The JSON input contract can be seen in this concrete example:

```json
"https://example.com/a"
```

Expected result:

```json
"6639460f-3425-5329-8097-a58f06127860"
```

Run `python3 example.py` for the Python representation of the result. `solution.py` contains the full implementation and can also be imported by another script.

## Scope

The function implements exactly the behavior described above. It does not perform network or filesystem access. Python exceptions indicate unsupported input; the next lesson turns them into a command-line error response. Review the limitations before reusing it in an application.
