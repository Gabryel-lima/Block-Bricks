#!/usr/bin/env bash

set -euo pipefail

source "$(cd "$(dirname "$0")" && pwd)/common.sh"

doctor_mode=0
if [[ "${1:-}" == "--doctor" ]]; then
  doctor_mode=1
fi

missing=0

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

if [[ ! -f "${ROOT_DIR}/hard_model.keras" ]]; then
  warn "Optional AI model hard_model.keras was not found. Bot mode will use fallback behavior."
fi

check_display_hint

if [[ "${doctor_mode}" -eq 1 ]]; then
  printf '\n'
  info "Root directory: ${ROOT_DIR}"
  info "Virtual environment: ${VENV_DIR}"
  info "Python runtime: ${PYTHON_BIN}"
  info "Managed log file: ${LOG_FILE}"
  info "Managed pid file: ${PID_FILE}"
  python3 --version
  make --version | sed -n '1p'
fi

if [[ "${missing}" -ne 0 ]]; then
  exit 1
fi

info "Dependency check finished successfully."