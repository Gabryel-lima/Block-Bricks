#!/usr/bin/env bash

set -euo pipefail

source "$(cd "$(dirname "$0")" && pwd)/common.sh"

pid="$(read_pid || true)"

if pid_is_running "${pid:-}"; then
  info "Status: running"
  info "PID: ${pid}"
  info "Log file: ${LOG_FILE}"
  ps -p "${pid}" -o pid=,ppid=,etime=,command=
  exit 0
fi

info "Status: stopped"
if [[ -f "${LOG_FILE}" ]]; then
  info "Last log file: ${LOG_FILE}"
fi

exit 0