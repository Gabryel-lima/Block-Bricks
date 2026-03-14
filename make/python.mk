.PHONY: setup setup-ai install install-dev install-ai run dev start up serve-prod stop down restart status logs game-run game-start game-stop game-status game-logs

##@ Setup
setup: ## Prepare the project from scratch in .venv and install runtime plus dev tooling.
	@bash scripts/setup.sh

setup-ai: ## Prepare .venv with runtime, dev tooling, and optional AI dependencies.
	@bash scripts/setup.sh --ai

install: setup ## Alias for setup.

install-dev: setup ## Alias for setup with dev tooling.

install-ai: setup-ai ## Alias for setup with optional AI dependencies.

##@ Runtime
run: ## Run the game in the foreground for fast local iteration.
	@bash scripts/run.sh --foreground

dev: run ## Alias for run.

start: ## Start the managed local runtime in background and write logs to .local/runtime.
	@bash scripts/run.sh --background

up: start ## Alias for start.

serve-prod: start ## Managed operational mode for local validation.

stop: ## Stop the managed local runtime.
	@bash scripts/stop.sh

down: stop ## Alias for stop.

restart: ## Restart the managed local runtime.
	@bash scripts/stop.sh --quiet || true
	@bash scripts/run.sh --background

status: ## Show managed runtime status, PID and log location.
	@bash scripts/status.sh

logs: ## Tail managed runtime logs.
	@bash scripts/logs.sh --follow

game-run: run ## Service-scoped alias for the main game foreground run.

game-start: start ## Service-scoped alias for the managed game runtime.

game-stop: stop ## Service-scoped alias for the managed game runtime stop.

game-status: status ## Service-scoped alias for runtime status.

game-logs: logs ## Service-scoped alias for runtime logs.