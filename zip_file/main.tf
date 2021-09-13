data "external" "zip_file" {
  program = ["python", "${path.module}/archive.py"]

  query = {
    source_dir  = var.source_dir
    output_path = var.output_path
  }
}
