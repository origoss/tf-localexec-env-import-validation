import os
import oci
env_vars = ["CONFIG_PROFILE", "COMPARTMENT_ID", "DEPLOYMENT_ID", "CONNECTION_IDS", "GG_ADMIN_URL"]

for var in env_vars:
    value = os.environ.get(var)
    print(f"{var} = {value}")
