import os
import oci
import requests
import time
import sys

def prove_imports():
    print("Time is loaded:", 'time' in sys.modules)
    print("oci version: ", oci.__version__)
    print("requests version: ", requests.__version__)

def prove_env_variables():
    env_vars = [
        "CONFIG_PROFILE",
        "COMPARTMENT_ID",
        "DEPLOYMENT_ID",
        "CONNECTION_IDS",
        "GG_ADMIN_URL"
    ]
    for var in env_vars:
        value = os.environ.get(var)
        print(f"{var} = {value}")

if __name__ == "__main__":
    prove_imports()
    prove_env_variables()