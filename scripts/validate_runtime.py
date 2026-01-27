import os
import oci
import requests
import time
import sys

ENV_VARS = [
    "CONFIG_PROFILE",
    "COMPARTMENT_ID",
    "DEPLOYMENT_ID",
    "CONNECTION_IDS",
    "GG_ADMIN_URL",
]


def prove_imports():
    print("Time is loaded:", 'time' in sys.modules)
    print("oci version: ", oci.__version__)
    print("requests version: ", requests.__version__)

def prove_env_variables():
    for var in ENV_VARS:
        try:
            value = os.environ.pop(var)
            print(f"{var} = {value}")
        except KeyError:
            print(f"Environment variable '{var}' is not set")
        

if __name__ == "__main__":
    prove_imports()
    prove_env_variables()