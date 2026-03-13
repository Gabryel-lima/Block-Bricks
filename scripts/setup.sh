#!/usr/bin/env bash

set -euo pipefail

source "$(cd "$(dirname "$0")" && pwd)/common.sh"

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

info "Setup finished. Activate it with: source ${VENV_DIR}/bin/activate"