#!/usr/bin/env bash

set -euo pipefail

ROOT_DIR="${ROOT_DIR:-$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)}"
VENV_DIR="${VENV_DIR:-${ROOT_DIR}/.venv}"
PYTHON_BIN="${PYTHON:-${VENV_DIR}/bin/python}"
PIP_BIN="${PIP:-${VENV_DIR}/bin/pip}"
APP_ENTRY="${APP_ENTRY:-${ROOT_DIR}/main.py}"
RUNTIME_DIR="${RUNTIME_DIR:-${ROOT_DIR}/.local/runtime}"
PID_FILE="${PID_FILE:-${RUNTIME_DIR}/block-bricks.pid}"
LOG_FILE="${LOG_FILE:-${RUNTIME_DIR}/block-bricks.log}"

info() {
  printf '\033[1;34m[info]\033[0m %s\n' "$*"
}

warn() {
  printf '\033[1;33m[warn]\033[0m %s\n' "$*"
}

error() {
  printf '\033[1;31m[error]\033[0m %s\n' "$*" >&2
}

ensure_runtime_dir() {
  mkdir -p "${RUNTIME_DIR}"
}

require_venv() {
  if [[ ! -x "${PYTHON_BIN}" ]]; then
    error "Virtual environment not found at ${VENV_DIR}. Run 'make setup' first."
    exit 1
  fi
}

pid_is_running() {
  local pid="$1"
  [[ -n "${pid}" ]] && kill -0 "${pid}" 2>/dev/null
}

read_pid() {
  if [[ -f "${PID_FILE}" ]]; then
    tr -d '[:space:]' < "${PID_FILE}"
  fi
}

check_display_hint() {
  if [[ -z "${DISPLAY:-}" && -z "${SDL_VIDEODRIVER:-}" ]]; then
    warn "DISPLAY is not set. Foreground gameplay needs a graphical session. Use 'make smoke' for headless validation."
  fi
}