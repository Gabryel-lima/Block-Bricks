.PHONY: help doctor check-dependencies clean clean-cache clean-runtime

##@ Help
help: ## Show grouped command help with operational entrypoints.
	@printf '\033[1;36m%s\033[0m\n' 'Block-Bricks automation panel'
	@printf '\033[0;37m%s\033[0m\n' 'Use make <target> to run a workflow. Core commands are grouped below.'
	@printf '\n'
	@printf '\033[1;33m%s\033[0m\n' 'Legend: [core] daily workflow  [ops] managed runtime  [qa] quality and packaging'
	@printf '\n'
	@awk 'BEGIN {FS = ":.*## "; category = "General"; last = ""} \
		/^##@/ {category = substr($$0, 5); next} \
		/^[a-zA-Z0-9_.-]+:.*## / {if (category != last) {printf "\033[1;34m%s\033[0m\n", category; last = category} printf "  \033[1;32m%-22s\033[0m %s\n", $$1, $$2}' $(MAKEFILE_LIST)

##@ Workspace
doctor: ## Print environment diagnostics and important paths.
	@bash scripts/check_dependencies.sh --doctor

check-dependencies: ## Validate required tools, files and optional runtime hints.
	@bash scripts/check_dependencies.sh

##@ Maintenance
clean: ## Remove build artifacts, caches and managed runtime files.
	@rm -rf $(ROOT_DIR)/build $(ROOT_DIR)/dist $(ROOT_DIR)/*.egg-info $(ROOT_DIR)/.pytest_cache $(ROOT_DIR)/.ruff_cache $(ROOT_DIR)/.mypy_cache $(ROOT_DIR)/htmlcov
	@rm -rf $(ROOT_DIR)/tests/__pycache__ $(ROOT_DIR)/src/__pycache__ $(ROOT_DIR)/src/core/__pycache__ $(ROOT_DIR)/src/utils/__pycache__
	@rm -rf $(ROOT_DIR)/depreciated/src/__pycache__ $(ROOT_DIR)/depreciated/src/model/__pycache__ $(ROOT_DIR)/depreciated/src/utils/__pycache__
	@rm -f $(PID_FILE) $(LOG_FILE)
	@printf '\033[1;34m[info]\033[0m Cleaned build and runtime artifacts.\n'

clean-cache: ## Remove Python caches only.
	@find $(ROOT_DIR) -type d -name '__pycache__' -prune -exec rm -rf {} +
	@find $(ROOT_DIR) -type d \( -name '.pytest_cache' -o -name '.ruff_cache' -o -name '.mypy_cache' \) -prune -exec rm -rf {} +
	@printf '\033[1;34m[info]\033[0m Cleaned Python caches.\n'

clean-runtime: ## Remove managed PID and log files only.
	@rm -f $(PID_FILE) $(LOG_FILE)
	@printf '\033[1;34m[info]\033[0m Cleaned managed runtime files.\n'