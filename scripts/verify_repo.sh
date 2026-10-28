#!/usr/bin/env bash
set -euo pipefail

echo "[1/3] Setting up environment..."
# Activa el entorno virtual si existe (para ejecución local del agente)
if [ -d ".venv" ]; then
    source .venv/bin/activate
fi

echo "[2/3] Running tests and coverage..."
# Ejecuta pytest asegurando que falle el script si un test falla
pytest -q --cov=src

echo "[3/3] Running repository contract checks..."
# Ejecuta el validador determinista
python scripts/check_repo_contract.py

echo "VERIFY_REPO: PASS"