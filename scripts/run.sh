#!/usr/bin/env bash

set -euo pipefail

source "$(cd "$(dirname "$0")" && pwd)/common.sh"

mode="${1:-}"

require_venv
ensure_runtime_dir
check_display_hint

case "${mode}" in
  --foreground)
    info "Starting Block-Bricks in foreground"
    exec "${PYTHON_BIN}" "${APP_ENTRY}"
    ;;
  --background)
    existing_pid="$(read_pid || true)"
    if pid_is_running "${existing_pid:-}"; then
      error "Block-Bricks is already running with PID ${existing_pid}."
      exit 1
    fi

    info "Starting Block-Bricks in background"
    nohup "${PYTHON_BIN}" "${APP_ENTRY}" >>"${LOG_FILE}" 2>&1 &
    echo $! > "${PID_FILE}"
    info "PID $(cat "${PID_FILE}")"
    info "Logs: ${LOG_FILE}"
    ;;
  *)
    error "Usage: scripts/run.sh --foreground | --background"
    exit 1
    ;;
esac