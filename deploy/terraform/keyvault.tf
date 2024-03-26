resource "azurerm_key_vault" "kv" {
  name                        = "kv-${var.app_name}-${var.environment}-${local.region}-${random_string.random.result}"
  location                    = azurerm_resource_group.rg.location
  sku_name                    = var.keyvault_sku_name
  resource_group_name         = azurerm_resource_group.rg.name
  enabled_for_deployment      = true
  enabled_for_disk_encryption = true
  tenant_id                   = data.azurerm_client_config.current.tenant_id
}
