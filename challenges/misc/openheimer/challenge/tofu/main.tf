terraform {
  required_version = ">= 1.6.2"
}

variable "SECRET" {
  type = string
  sensitive = true
  description = "i keep my secrets safe here :))"
}