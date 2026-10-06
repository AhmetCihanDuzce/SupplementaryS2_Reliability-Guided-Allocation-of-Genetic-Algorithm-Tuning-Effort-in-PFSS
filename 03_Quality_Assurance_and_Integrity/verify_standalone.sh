#!/usr/bin/env bash
set -euo pipefail
ROOT="$(cd "$(dirname "$0")" && pwd)"
PKG="$(cd "$ROOT/.." && pwd)"
python3 "$ROOT/scripts/verify_all.py"
python3 "$ROOT/scripts/verify_prospective_matrices_exact.py"
python3 "$ROOT/scripts/verify_recommended_operational_policy_validation.py" --s2 "$PKG"
