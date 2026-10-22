# Calculator build with PyBuilder

Hassan Nasrallah — EECE435L Lab 6, graded exercise.

The package implements add, subtract, multiply, divide, modulus, power,
and square_root. There are 32 unit tests covering ordinary arithmetic,
negative and fractional inputs, and invalid operations.

## Reproduce the build

From this directory, with Python 3.10 or later:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
python -m pip install -e .
pyb run_unit_tests
python -m unittest tests.unittest.calculator_Hassan_Nasrallah.test_calculator_Hassan_Nasrallah -v
pyb clean install_build_dependencies run_unit_tests publish
```

On Linux/macOS activate with `source .venv/bin/activate` instead.
The direct unittest command needs the editable install so the src package is
importable. PyBuilder sets its source path automatically.

`build.py` enables source management, unittest execution, dependency management,
and setuptools packaging. Test discovery explicitly uses `test_*` and points
at the handout's test directory. This ensures the build executes the test suite.
The default `pyb` task is `publish`, which tests and creates local source and
wheel distributions. In PyBuilder, publish builds local artifacts; it does not
upload them to PyPI. Generated packages are under `target/dist/` and reports
are under `target/reports/`.

Division and modulus with a zero divisor raise ValueError. Square root only
accepts nonnegative real numbers and raises ValueError for a negative input.
Modulus follows Python's divisor-sign convention. Power follows Python's `**`
semantics, including ZeroDivisionError for zero to a negative exponent.

The submission's `evidence/` folder contains the actual execution logs, test
reports, package smoke test, and terminal screenshot.

Reference: [PyBuilder plugin documentation](https://pybuilder.io/documentation/plugins).
