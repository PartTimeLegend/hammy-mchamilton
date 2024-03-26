variable "environment" {
  type = string
  description = "The environment to deploy this app service to e.g., dev, test, staging, prod."
}

variable "location" {
  type    = string
  default = "UK South"
  description = "The Azure location for deploying this this application to."
}

variable "discord_token" {
  type      = string
  sensitive = true
  default = "Discord oauth2 token. SENSITIVE."
}

variable "app_name" {
  type    = string
  default = "hammy"
  description = "The app name to use."
}

variable "container" {
  type    = string
  default = "parttimelegend/hammy-mchamilton:latest"
  description = "Container name"
}

variable "container_registry" {
  type    = string
  default = "https://ghcr.io"
  description = "Container registry URL"
}

variable "os_type" {
  type    = string
  default = "Linux"
  description = "OS Type (Windows / Linux)"
}

variable "app_service_sku_name" {
  type    = string
  default = "P1v2"
  description = "The sku to use for the app service"
}

variable "keyvault_sku_name" {
  type    = string
  default = "standard"
  description = "The SKU to use for the KeyVault"
}
