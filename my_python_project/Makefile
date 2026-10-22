.DEFAULT_GOAL := all
.NOTPARALLEL:
.PHONY: all clean install install_deps test lint build package

PYTHON ?= python
PYB ?= pyb

all: clean install_deps test lint build

clean:
	$(PYB) clean

install: install_deps

install_deps:
	$(PYTHON) -m pip install -r requirements.txt

test:
	$(PYB) run_unit_tests

lint:
	$(PYTHON) -m flake8 src build.py

build:
	$(PYB) publish

package: build
