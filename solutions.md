# Solutions

## 1. Installation
Install pylint, mypy and flake8 using `pip`.

## 2. Output of pylint, flake8 and mypy

```
% pylint fibonacci.py 
************* Module fibonacci
fibonacci.py:26:30: E1121: Too many positional arguments for function call (too-many-function-args)

------------------------------------------------------------------
Your code has been rated at 6.43/10 (previous run: 6.43/10, +0.00)
```

```
% pylint fibonacci_unformatted.py 
************* Module fibonacci_unformatted
fibonacci_unformatted.py:9:0: C0304: Final newline missing (missing-final-newline)
fibonacci_unformatted.py:1:0: C0114: Missing module docstring (missing-module-docstring)
fibonacci_unformatted.py:1:0: W0401: Wildcard import fib (wildcard-import)
fibonacci_unformatted.py:3:0: C0116: Missing function or method docstring (missing-function-docstring)
fibonacci_unformatted.py:4:4: C0103: Variable name "integerInput" doesn't conform to snake_case naming style (invalid-name)
fibonacci_unformatted.py:5:4: W0612: Unused variable 'string_input' (unused-variable)
fibonacci_unformatted.py:2:0: W0611: Unused ceil imported from math (unused-import)
fibonacci_unformatted.py:2:0: C0411: standard import "from math import ceil" should be placed before "from fib import *" (wrong-import-order)

------------------------------------------------------------------
Your code has been rated at 0.00/10 (previous run: 0.00/10, +0.00)
```

```
 % flake8 fibonacci_unformatted.py 
fibonacci_unformatted.py:1:1: F403 'from fib import *' used; unable to detect undefined names
fibonacci_unformatted.py:2:1: F401 'math.ceil' imported but unused
fibonacci_unformatted.py:3:1: E302 expected 2 blank lines, found 0
fibonacci_unformatted.py:4:17: E225 missing whitespace around operator
fibonacci_unformatted.py:5:5: F841 local variable 'string_input' is assigned to but never used
fibonacci_unformatted.py:5:17: E225 missing whitespace around operator
fibonacci_unformatted.py:7:23: E225 missing whitespace around operator
fibonacci_unformatted.py:7:29: E201 whitespace after '('
fibonacci_unformatted.py:7:30: F405 'fib' may be undefined, or defined from star imports: fib
fibonacci_unformatted.py:7:47: E202 whitespace before ')'
fibonacci_unformatted.py:8:11: E201 whitespace after '('
fibonacci_unformatted.py:8:30: E202 whitespace before ')'
fibonacci_unformatted.py:9:1: E305 expected 2 blank lines after class or function definition, found 0
fibonacci_unformatted.py:9:7: W292 no newline at end of file
```

```
% mypy fibonacci_typed.py 
fibonacci_typed.py:20: error: Argument 1 to "fib" has incompatible type "str"; expected "int"
fibonacci_typed.py:23: error: Argument 1 to "fib" has incompatible type "float"; expected "int"
fibonacci_typed.py:26: error: Too many arguments for "fib"
Found 3 errors in 1 file (checked 1 source file)
```

## 3. IDE Configuration

### PyCharm
1. In Settings / Editor / Inspections / Python disable all.
2. Install the pylint and mypy extensions.
3. Configure pylint and mypy in *Other Settings*: you can set a different path to the executables (by default it will use the pylint / mypy installed in the current python environment) and the arguments to the commands.

### Visual Studio Code
1. Install the Python extension, *but not the Pylance extension* (Pylance is another linter, similar to pylint).
2. In Preferences set *Linting: Pylint Enabled*. 
3. In Preferences set *Linting: Mypy Enabled*.
4. By default, VSCode will use pylint / mypy from the configured python environment. You can also set absolute paths to the pylint / mypy executables. You can set arguments to the pylint / mypy commands by configuring *Linting: Pylint args* and *Linting: Mypy args*.

## 4. Options
**Disable no new line at the end of file**: `pylint fibonacci_unformatted.py --disable=C0304`

**Disable missing docstring**: `pylint fibonacci_unformatted.py --disable=C0114`

**Warn about missing typing annotations**:
```
% mypy add_two.py --disallow-untyped-defs 
add_two.py:5: error: Function is missing a type annotation
add_two.py:15: error: Function is missing a return type annotation
add_two.py:15: note: Use "-> None" if function does not return a value
```
