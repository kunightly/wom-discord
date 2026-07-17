#!/bin/bash

cd /root/wom-discord

source venv/bin/activate

python main.py >> logs/output.log 2>&1
