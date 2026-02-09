import os
import oci
import requests
import time
import sys
import logging

ENV_VARS = [
    "CONFIG_PROFILE",
    "COMPARTMENT_ID",
    "DEPLOYMENT_ID",
    "CONNECTION_IDS",
    "GG_ADMIN_URL",
]


def prove_imports():
    logging.debug(f"Time is loaded:{'time' in sys.modules}")
    logging.debug(f"oci version: {oci.__version__}")
    logging.debug(f"requests version: {requests.__version__}")

def prove_env_variables():
    for var in ENV_VARS:
        try:
            value = os.environ.pop(var)
            print(f"{var} = {value}")
        except KeyError:
            print(f"Environment variable '{var}' is not set")
        

def main():
    logging.basicConfig(level=logging.DEBUG)
    prove_imports()
    prove_env_variables()


if __name__ == "__main__":
    main()
