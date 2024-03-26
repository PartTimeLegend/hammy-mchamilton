output "web_url" {
  value = azurerm_linux_web_app.as.default_hostname
}

output "service_plan_name" {
  value = azurerm_service_plan.sp.name
}

output "app_name" {
  value = azurerm_linux_web_app.as.name
}

output "resource_group_name" {
  value = azurerm_resource_group.rg.name
}

output "location" {
  value = azurerm_resource_group.rg.location
}

output "environment" {
  value = var.environment
}
