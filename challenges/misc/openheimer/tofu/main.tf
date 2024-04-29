terraform {
  required_version = ">= 1.6.2"
}

variable "SECRET" {
  type = string
}

resource "local_file" "secret" {
  content  = var.SECRET
  filename = "FLAG"
}