<!-- BEGIN_TF_DOCS -->
## Requirements

No requirements.

## Providers

| Name | Version |
|------|---------|
| <a name="provider_azurerm"></a> [azurerm](#provider\_azurerm) | 4.14.0 |
| <a name="provider_random"></a> [random](#provider\_random) | 3.6.0 |

## Modules

| Name | Source | Version |
|------|--------|---------|
| <a name="module_region-abbreviation-mapping"></a> [region-abbreviation-mapping](#module\_region-abbreviation-mapping) | PartTimeLegend/region-abbreviation-mapping/azure | n/a |

## Resources

| Name | Type |
|------|------|
| [azurerm_key_vault.kv](https://registry.terraform.io/providers/hashicorp/azurerm/latest/docs/resources/key_vault) | resource |
| [azurerm_key_vault_secret.token](https://registry.terraform.io/providers/hashicorp/azurerm/latest/docs/resources/key_vault_secret) | resource |
| [azurerm_linux_web_app.as](https://registry.terraform.io/providers/hashicorp/azurerm/latest/docs/resources/linux_web_app) | resource |
| [azurerm_resource_group.rg](https://registry.terraform.io/providers/hashicorp/azurerm/latest/docs/resources/resource_group) | resource |
| [azurerm_service_plan.sp](https://registry.terraform.io/providers/hashicorp/azurerm/latest/docs/resources/service_plan) | resource |
| [random_string.random](https://registry.terraform.io/providers/hashicorp/random/latest/docs/resources/string) | resource |
| [azurerm_client_config.current](https://registry.terraform.io/providers/hashicorp/azurerm/latest/docs/data-sources/client_config) | data source |

## Inputs

| Name | Description | Type | Default | Required |
|------|-------------|------|---------|:--------:|
| <a name="input_app_name"></a> [app\_name](#input\_app\_name) | The app name to use. | `string` | `"hammy"` | no |
| <a name="input_app_service_sku_name"></a> [app\_service\_sku\_name](#input\_app\_service\_sku\_name) | The sku to use for the app service | `string` | `"P1v2"` | no |
| <a name="input_container"></a> [container](#input\_container) | Container name | `string` | `"HamHangOut/hammy-mchamilton:latest"` | no |
| <a name="input_container_registry"></a> [container\_registry](#input\_container\_registry) | Container registry URL | `string` | `"https://ghcr.io"` | no |
| <a name="input_discord_token"></a> [discord\_token](#input\_discord\_token) | Discord oauth2 token. SENSITIVE. | `string` | n/a | yes |
| <a name="input_environment"></a> [environment](#input\_environment) | The environment to deploy this app service to e.g., dev, test, staging, prod. | `string` | n/a | yes |
| <a name="input_keyvault_sku_name"></a> [keyvault\_sku\_name](#input\_keyvault\_sku\_name) | The SKU to use for the KeyVault | `string` | `"standard"` | no |
| <a name="input_location"></a> [location](#input\_location) | The Azure location for deploying this this application to. | `string` | `"UK South"` | no |
| <a name="input_os_type"></a> [os\_type](#input\_os\_type) | OS Type (Windows / Linux) | `string` | `"Linux"` | no |

## Outputs

| Name | Description |
|------|-------------|
| <a name="output_app_name"></a> [app\_name](#output\_app\_name) | n/a |
| <a name="output_environment"></a> [environment](#output\_environment) | n/a |
| <a name="output_location"></a> [location](#output\_location) | n/a |
| <a name="output_resource_group_name"></a> [resource\_group\_name](#output\_resource\_group\_name) | n/a |
| <a name="output_service_plan_name"></a> [service\_plan\_name](#output\_service\_plan\_name) | n/a |
| <a name="output_web_url"></a> [web\_url](#output\_web\_url) | n/a |
<!-- END_TF_DOCS -->