MAKEFLAGS += --warn-undefined-variables
MAKEFLAGS += --no-builtin-rules
SHELL := bash
.ONESHELL:
.SHELLFLAGS := -eu -o pipefail -c
.DEFAULT_GOAL := all
.DELETE_ON_ERROR:
.SUFFIXES:

TESTS = .

.PHONY: update-requirements
update-requirements:
	pip install --upgrade pip setuptools pip-tools
	pip-compile --upgrade --build-isolation --output-file requirements/main.txt requirements/main.in
	pip-compile --upgrade --build-isolation --output-file requirements/dev.txt requirements/dev.in

.PHONY: install-requirements
install-requirements:
	pip install -r requirements/main.txt -r requirements/dev.txt

.PHONY: sync-requirements
sync-requirements:
	pip-sync requirements/main.txt requirements/dev.txt

.PHONY: pytest
pytest:
	pytest -v -p no:warnings $(TESTS)

.PHONY: black
black:
	black --line-length 128 src
	black --line-length 128 tests
