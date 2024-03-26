resource "azurerm_linux_web_app" "as" {
  name                = "app-${var.app_name}-${var.environment}-${local.region}-${random_string.random.result}"
  location            = azurerm_resource_group.rg.location
  resource_group_name = azurerm_resource_group.rg.name
  service_plan_id     = azurerm_service_plan.sp.id

  site_config {
    always_on = true
    application_stack {
      docker_image_name   = var.container
      docker_registry_url = var.container_registry
    }
  }

  app_settings = {
    TOKEN = azurerm_key_vault_secret.token.value
  }
}
