# terraform-archive-python

> **Note: This repository has been archived.** It was created to accommodate the consistent creation of Lambda zips when using multiple operating systems. The Terraform Go module for archiving was producing different checksums depending on the operating system it was executed on, resulting in false zip changes when running `terraform apply`. This module ensured that the zip file always had consistent checksums regardless of the operating system used. This repository is now archived as it's likely that the issue has been fixed in the source Terraform Go module.

Python based terraform module to create the same .zip file across operating systems.

Tested against python2/3 linux/windows.

Should resolve issues with:
- Different operating systems producing diffrent checksums
- No longer have to touch/create .zip file before running terraform

```hcl
module "archive_lambda" {
    source = "./"
    source_dir = "dummy_lambda/"
    output_path = "dummy_lambda.zip"
}


resource "aws_lambda_function" "lambda_function" {
  filename         = "${module.archive_lambda.zip_path}"
  source_code_hash = "${module.archive_lambda.base64sha256}"
}
```
