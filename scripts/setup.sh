#!/usr/bin/env bash

set -euo pipefail

source "$(cd "$(dirname "$0")" && pwd)/common.sh"

install_ai=false

while [[ $# -gt 0 ]]; do
  case "$1" in
    --ai)
      install_ai=true
      ;;
    -h|--help)
      cat <<'EOF'
Usage: scripts/setup.sh [--ai]

Options:
  --ai    Install optional AI dependencies in addition to the base game runtime.
EOF
      exit 0
      ;;
    *)
      error "Unknown option: $1"
      exit 1
      ;;
  esac
  shift
done

info "Preparing local virtual environment"

if [[ ! -d "${VENV_DIR}" ]]; then
  python3 -m venv "${VENV_DIR}"
  info "Created virtual environment at ${VENV_DIR}"
else
  info "Using existing virtual environment at ${VENV_DIR}"
fi

"${PYTHON_BIN}" -m pip install --upgrade pip setuptools wheel
"${PIP_BIN}" install -e .
"${PIP_BIN}" install -r "${ROOT_DIR}/requirements-dev.txt"

if [[ "${install_ai}" == true ]]; then
  info "Installing optional AI dependencies"
  "${PIP_BIN}" install -r "${ROOT_DIR}/requirements-ai.txt"
fi

info "Setup finished. Activate it with: source ${VENV_DIR}/bin/activate"