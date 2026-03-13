.PHONY: smoke test lint format check build rebuild

##@ Quality
smoke: ## Run a non-interactive smoke check against imports, assets and score files.
	@$(SYSTEM_PYTHON) scripts/smoke_check.py

test: ## Run the automated test suite.
	@$(PYTHON) -m pytest -q

lint: ## Run Ruff static checks on the main source tree and tests.
	@$(PYTHON) -m ruff check main.py src tests scripts/smoke_check.py

format: ## Format the Python source tree with Black.
	@$(PYTHON) -m black main.py src tests scripts/smoke_check.py

check: lint test smoke ## Run the main verification workflow.

##@ Build
build: ## Build source and wheel distributions.
	@$(PYTHON) -m build

rebuild: clean build ## Rebuild distributable artifacts from a clean state.