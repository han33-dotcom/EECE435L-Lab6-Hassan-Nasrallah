# Optional Makefile exercise

Hassan Nasrallah — EECE435L Lab 6, optional exercise.

This project combines the handout's greeting application and its later
`my_python_project` walkthrough. The application imports `greet` from
`my_module` and prints `Hello, World!`. Four unit tests verify both required
greetings, an empty name, and the application's imported function.

## Run

Create and activate a Python virtual environment, then run:

```text
make install_deps
make test
make lint
make build
make all
```

GNU Make must be installed. On Windows, use an activated PowerShell virtual
environment with make on PATH. Override executables if needed:
`make all PYTHON=python PYB=pyb`.
To run the app: `python src/main/python/app.py`.
To run tests without PyBuilder, install the package with `python -m pip install
-e .`, then use `python -m unittest discover -s src/unittest/python -v`.

## Targets and build process

| Target | Action |
| --- | --- |
| `clean` | Ask PyBuilder to remove generated target output. |
| `install_deps` | Install the pinned build tools from requirements.txt. |
| `install` | Alias for install_deps. |
| `test` | Run the four unittest cases through PyBuilder. |
| `lint` | Check the source code, tests, and descriptor with flake8. |
| `build` | Run PyBuilder publish to test and create local sdist and wheel files. |
| `package` | Alias for build. |
| `all` | Clean, install tools, test, lint, and build in that order. |

The default is `all`. `.PHONY` makes targets run even if matching filenames
exist. `.NOTPARALLEL` preserves task order even if make is invoked with `-j`,
so clean cannot race a build. Recipe lines start with real tab characters.
Build dependencies for PyBuilder's isolated environments are handled by its
install_dependencies plugin. Generated packages are below `target/dist/`.

Make provides short, repeatable commands and stops on a failed recipe.
PyBuilder manages Python source discovery, testing, dependencies, and packaging;
Make coordinates these operations. The same targets can be used locally or
in continuous integration, reducing manual steps and omitted checks.

Reference: [PyBuilder usage documentation](https://pybuilder.io/documentation/manual).
