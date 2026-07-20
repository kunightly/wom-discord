#!/bin/bash

set -e

PROJECT_DIR="/root/wom-notify"

cd "$PROJECT_DIR"

echo "===== $(date) ====="

echo "[1/5] Pulling latest code..."
git pull origin main

echo "[2/5] Activating virtual environment..."
source venv/bin/activate

echo "[3/5] Installing/updating dependencies..."
pip install -r requirements.txt

echo "[4/5] Running Wise Old Man notifier..."
python main.py

echo "[5/5] Finished."
