resource "null_resource" "runtime_validation" {
  provisioner "local-exec" {
    command = "echo 'Hello There!'"

    environment = {
    }
  }
}
