# Define project variables
PYTHON := python3
VENV := venv
PIP := $(VENV)/bin/pip

.PHONY: help install test lint clean

# Help command to list available tasks
help: ## Show this help message
	@echo "Usage: make [task]"
	@echo ""
	@echo "Tasks:"
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-15s\033[0m %s\n", $$1, $$2}'

install: ## Create virtual environment and install dependencies
	$(PYTHON) -m venv $(VENV)
	$(PIP) install --upgrade pip
	$(PIP) install -e .

test: ## Run unit and integration tests using pytest
	$(VENV)/bin/pytest tests/

lint: ## Check code quality with flake8 and black
	$(VENV)/bin/flake8 src/
	$(VENV)/bin/black --check src/

clean: ## Remove temporary files, caches, and venv
	rm -rf __pycache__ .pytest_cache .venv venv dist build *.egg-info