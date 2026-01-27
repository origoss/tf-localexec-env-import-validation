#!/usr/bin/env sh
python3 -m venv ../scripts/venv
source ../scripts/venv/bin/activate
pip install -r ../scripts/requirements.txt
. ../scripts/set_environment_variables.sh
python3 ../scripts/validate_runtime.py
deactivate