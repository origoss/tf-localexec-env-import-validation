# tf-localexec-env-import-validation
This repository contains scripts and Terraform configuration used to validate environment variables and python module imports.

## Usage
Apply the terraform configuration. The results are printed during apply.
```sh
cd terraform
terraform init
terraform apply
```
## How It Works
- during apply, a terraform `local-exec` provisioner runs a wrapper script `run_validate_runtime`
- the wrapper script  sets up the python virtual environment
- and runs the `validate_runtime` to test reachability of environment variables and python module imports
