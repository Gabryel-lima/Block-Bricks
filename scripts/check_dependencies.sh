#!/usr/bin/env bash

set -euo pipefail

source "$(cd "$(dirname "$0")" && pwd)/common.sh"

doctor_mode=0
if [[ "${1:-}" == "--doctor" ]]; then
  doctor_mode=1
fi

missing=0

runtime_python="python3"
if [[ -x "${PYTHON_BIN}" ]]; then
  runtime_python="${PYTHON_BIN}"
fi

check_command() {
  local command_name="$1"
  if command -v "${command_name}" >/dev/null 2>&1; then
    info "Found command: ${command_name}"
  else
    error "Missing command: ${command_name}"
    missing=1
  fi
}

check_file() {
  local file_path="$1"
  if [[ -e "${file_path}" ]]; then
    info "Found file: ${file_path#${ROOT_DIR}/}"
  else
    error "Missing file: ${file_path#${ROOT_DIR}/}"
    missing=1
  fi
}

check_python_distribution() {
  local distribution_name="$1"
  if "${runtime_python}" - <<PY >/dev/null 2>&1
from importlib import metadata
metadata.version("${distribution_name}")
PY
  then
    local version
    version="$("${runtime_python}" - <<PY
from importlib import metadata
print(metadata.version("${distribution_name}"))
PY
)"
    info "Installed Python package: ${distribution_name} (${version})"
    return 0
  fi

  warn "Python package not installed: ${distribution_name}"
  return 1
}

check_command make
check_command bash
check_command python3

if python3 -m venv --help >/dev/null 2>&1; then
  info "Python venv module is available"
else
  error "python3 -m venv is unavailable"
  missing=1
fi

check_file "${ROOT_DIR}/main.py"
check_file "${ROOT_DIR}/setup.py"
check_file "${ROOT_DIR}/assets/logo.ico"
check_file "${ROOT_DIR}/assets/gear_config.png"
check_file "${ROOT_DIR}/src/json/best_score.json"
check_file "${ROOT_DIR}/src/json/best_score2.json"

if [[ -x "${PYTHON_BIN}" ]]; then
  check_python_distribution numpy >/dev/null
  check_python_distribution pygame-ce >/dev/null
else
  warn "Virtual environment not found at ${VENV_DIR}. Run 'make setup' or 'make setup-ai' for package-level diagnostics."
fi

if [[ ! -f "${ROOT_DIR}/hard_model.keras" ]]; then
  warn "Optional AI model hard_model.keras was not found. Bot mode will use fallback behavior."
fi

ai_stack_ready=0
if [[ -x "${PYTHON_BIN}" ]]; then
  if check_python_distribution keras >/dev/null && check_python_distribution tensorflow >/dev/null; then
    ai_stack_ready=1
    info "Optional AI stack is installed in the virtual environment."
  else
    warn "Optional AI stack is not fully installed. Run 'make setup-ai' if you need the Keras-backed bot."
  fi
fi

if [[ "${BLOCK_BRICKS_ENABLE_KERAS_BOT:-0}" == "1" ]]; then
  if [[ "${ai_stack_ready}" -eq 1 ]]; then
    info "Keras-backed bot loading is enabled via BLOCK_BRICKS_ENABLE_KERAS_BOT=1"
  else
    warn "BLOCK_BRICKS_ENABLE_KERAS_BOT=1 is set, but the optional AI stack is not fully installed."
  fi
else
  info "Keras-backed bot loading is disabled by default. Set BLOCK_BRICKS_ENABLE_KERAS_BOT=1 to enable it."
fi

check_display_hint

if [[ "${doctor_mode}" -eq 1 ]]; then
  printf '\n'
  info "Root directory: ${ROOT_DIR}"
  info "Virtual environment: ${VENV_DIR}"
  info "Python runtime: ${PYTHON_BIN}"
  info "Managed log file: ${LOG_FILE}"
  info "Managed pid file: ${PID_FILE}"
  info "Optional AI model: ${ROOT_DIR}/hard_model.keras"
  info "Keras bot env flag: ${BLOCK_BRICKS_ENABLE_KERAS_BOT:-0}"
  python3 --version
  make --version | sed -n '1p'
fi

if [[ "${missing}" -ne 0 ]]; then
  exit 1
fi

info "Dependency check finished successfully."