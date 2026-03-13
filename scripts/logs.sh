#!/usr/bin/env bash

set -euo pipefail

source "$(cd "$(dirname "$0")" && pwd)/common.sh"

follow=0
if [[ "${1:-}" == "--follow" ]]; then
  follow=1
fi

if [[ ! -f "${LOG_FILE}" ]]; then
  error "Log file not found at ${LOG_FILE}. Start the managed runtime with 'make start' first."
  exit 1
fi

if [[ "${follow}" -eq 1 ]]; then
  exec tail -n "${TAIL_LINES:-50}" -f "${LOG_FILE}"
fi

tail -n "${TAIL_LINES:-50}" "${LOG_FILE}"