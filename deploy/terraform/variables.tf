variable "environment" {
  type = string
}

variable "location" {
  type    = string
  default = "UK South"
}

variable "discord_token" {
  type      = string
  sensitive = true
}

variable "app_name" {
  type    = string
  default = "hammy"
}

variable "container" {
  type    = string
  default = "parttimelegend/hammy-mchamilton:latest"
}

variable "container_registry" {
  type    = string
  default = "https://ghcr.io"
}
