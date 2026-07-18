#!/bin/bash

set -e

PROJECT_DIR="/root/wom-discord"

cd "$PROJECT_DIR"

echo "===== $(date) ====="

echo "[1/4] Pulling latest code..."
git pull origin main

echo "[2/4] Activating virtual environment..."
source venv/bin/activate

echo "[3/4] Running Wise Old Man notifier..."
python3 main.py

echo "[4/4] Finished."
