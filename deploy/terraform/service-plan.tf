resource "azurerm_service_plan" "sp" {
  name                = "plan-${var.app_name}-${var.environment}-${local.region}-${random_string.random.result}"
  resource_group_name = azurerm_resource_group.rg.name
  location            = azurerm_resource_group.rg.location
  os_type             = var.os_type
  sku_name            = var.app_service_sku_name
}
