resource "azurerm_key_vault_secret" "token" {
  name         = "DISCORDTOKEN"
  value        = var.discord_token
  key_vault_id = azurerm_key_vault.kv.id
}
