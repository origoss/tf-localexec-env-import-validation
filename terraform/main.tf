resource "null_resource" "runtime_validation" {
  provisioner "local-exec" {
    command =  "../scripts/run_validate_runtime.sh"
  }
}
