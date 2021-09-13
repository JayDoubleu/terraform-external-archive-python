# terraform-archive-python
Python based terraform module to create the same .zip file across operating systems.

Tested against python2/3 linux/windows.

Should resolve issues with:
- Different operating systems producing different checksums
- No longer have to touch/create .zip file before running terraform

### Usage

When sourcing this module direct, always pin your source to a specific TAG. Example syntax is shown below:

```hcl
module "archive_lambda" {
    source = "git@github.com:JSainsburyPLC/terraform-archive-python.git//zip_file?ref=1.0.1"
    source_dir = "dummy_lambda_dir/"
    output_path = "dummy_lambda.zip"
}

resource "aws_lambda_function" "lambda_function" {
  filename         = "${module.archive_lambda.zip_path}"
  source_code_hash = "${module.archive_lambda.base64sha256}"
}
```

### When updating this repo

After merging any new PR containing code changes to the 'master' branch, always create a new version tag.  e.g.
```hcl
git checkout master
git pull
git tag -a 1.0.3 -m "Release 1.0.3"
git push origin --tags
```
