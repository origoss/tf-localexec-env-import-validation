#!/usr/bin/env sh
python3 -m venv ../scripts/venv
source ../scripts/venv/bin/activate
pip install -r ../scripts/requirements.txt
python3 ../scripts/validate_runtime.py
deactivate