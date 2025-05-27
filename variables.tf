variable "name" {
  description = "Prefix to use for resources name"
  default     = "ec2-scheduler"
}

variable "stopstart_tags" {
  description = "Enable STOP/START for EC2 Instances with the following tag"
  default = {
    TagKEY   = "stopstart"
    TagVALUE = "enabled"
  }
}

variable "stop_cron_schedule" {
  description = "Cron Expression when to STOP Servers in UTC Time zone"
  default     = "cron(15 15 ? * MON-FRI *)" # UTC+3 = 18:15, workdays only
}

variable "start_cron_schedule" {
  description = "Cron Expression when to START Servers in UTC Time zone"
  default     = "cron(45 05 ? * MON-FRI *)" # UTC+3 = 08:45, workdays only
}

variable "tags" {
  description = "Tags to apply to resources"
  default = {
    Developer = "ADV-IT"
    Author    = "Denis Astahov"
  }
}
