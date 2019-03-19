data "external" "zip_file" {
  program = ["python3", "${path.module}/archive.py"]

  query = {
    source_dir  = "${path.module}/test_files/"
    output_path = "${path.module}/zipfile.zip"
  }
}

output "zipped_file_md5" {
  value = "${data.external.zip_file.result.output_md5}"
}

output "zipped_file_output_absolute_path" {
  value = "${data.external.zip_file.result.output_absolute_path}"
}

output "zipped_file_output_path" {
  value = "${data.external.zip_file.result.output_path}"
}

output "zipped_file_output_size" {
  value = "${data.external.zip_file.result.output_size}"
}
