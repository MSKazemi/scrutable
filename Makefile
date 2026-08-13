# Product Questionbook — convenience targets.
# Nothing here is required to use the framework. The canonical interface is the
# versioned Markdown and YAML in this repository (see decisions/ADR-0003).

PYTHON ?= python3

.DEFAULT_GOAL := help

.PHONY: help validate report install check

help: ## Show available targets
	@grep -hE '^[a-zA-Z_-]+:.*?## ' $(MAKEFILE_LIST) \
		| awk 'BEGIN {FS = ":.*?## "}; {printf "  \033[36m%-10s\033[0m %s\n", $$1, $$2}'

install: ## Install validator dependencies
	$(PYTHON) -m pip install -r tools/requirements.txt

validate: ## Run the deterministic conformance validator (same check CI runs)
	$(PYTHON) tools/validate.py

report: ## Write a machine-readable conformance report to conformance-report.json
	$(PYTHON) tools/validate.py --json > conformance-report.json
	@echo "wrote conformance-report.json"

check: ## Run the validator with warnings treated as failures
	$(PYTHON) tools/validate.py --strict
