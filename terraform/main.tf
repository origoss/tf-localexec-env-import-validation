resource "null_resource" "runtime_validation" {
  provisioner "local-exec" {
    command =  "../scripts/run_validate_runtime.sh"
    
    environment = {
        CONFIG_PROFILE = "test config profile"
        COMPARTMENT_ID = "test compartment id"
        DEPLOYMENT_ID = "test deployment id"
        CONNECTION_IDS = "test connection ids"
        GG_ADMIN_URL = "test gg admin url"
    }
  }
}
