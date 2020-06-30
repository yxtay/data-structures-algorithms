MAKEFLAGS += --warn-undefined-variables
MAKEFLAGS += --no-builtin-rules
SHELL := bash
.SHELLFLAGS := -eu -o pipefail -c
.ONESHELL:
.DEFAULT_GOAL := help
.DELETE_ON_ERROR:

SOURCE_DIR := src
TEST_DIR := tests

.PHONY: help
help:  ## print help message
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}'

## dependencies

.PHONY: deps-install
deps-install:  ## install dependencies
	pip install poetry
	poetry install --no-root

.PHONY: deps-update
deps-update:
	pip install poetry
	poetry update

requirements.txt: poetry.lock
	poetry export --format requirements.txt --output requirements.txt --without-hashes

## checks

.PHONY: format
format:
	black $(SOURCE_DIR) $(TEST_DIR)

.PHONY: lint
lint:
	black $(SOURCE_DIR) $(TEST_DIR) --diff
	isort --check-only
	flake8 $(SOURCE_DIR) $(TEST_DIR)
#	mypy $(SOURCE_DIR)

.PHONY: test
test:
	pytest $(TEST_DIR) --cov $(SOURCE_DIR)

.PHONY: run-ci
run-ci: deps-install lint test  ## run ci
