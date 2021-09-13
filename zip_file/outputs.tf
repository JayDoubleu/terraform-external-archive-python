
output "zip_path" {
  value       = data.external.zip_file.result.output_path
  description = "path to zip file"
}

output "base64sha256" {
  value       = data.external.zip_file.result.output_base64sha256
  description = "sha256 result"
}
