#!/usr/bin/env bash

set -euo pipefail

source "$(cd "$(dirname "$0")" && pwd)/common.sh"

quiet=0
if [[ "${1:-}" == "--quiet" ]]; then
  quiet=1
fi

pid="$(read_pid || true)"

if ! pid_is_running "${pid:-}"; then
  [[ -f "${PID_FILE}" ]] && rm -f "${PID_FILE}"
  if [[ "${quiet}" -eq 0 ]]; then
    warn "No managed Block-Bricks process is running."
  fi
  exit 0
fi

if [[ "${quiet}" -eq 0 ]]; then
  info "Stopping Block-Bricks PID ${pid}"
fi

kill "${pid}"

for _ in $(seq 1 20); do
  if ! pid_is_running "${pid}"; then
    rm -f "${PID_FILE}"
    [[ "${quiet}" -eq 0 ]] && info "Process stopped"
    exit 0
  fi
  sleep 0.2
done

warn "Process did not stop after SIGTERM, sending SIGKILL"
kill -9 "${pid}"
rm -f "${PID_FILE}"
[[ "${quiet}" -eq 0 ]] && info "Process stopped"