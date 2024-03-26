locals {
  region = module.region-abbreviation-mapping.az_region_abbr_map[var.location]
}
