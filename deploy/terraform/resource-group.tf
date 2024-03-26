resource "azurerm_resource_group" "rg" {
  name     = "rg-${var.app_name}-${var.environment}-${local.region}-${random_string.random.result}"
  location = var.location
}
