# terraform-archive-python
Python based terraform module to create the same .zip file across operating systems.

Tested against python2/3 linux/windows.

Should resolve issues with:
- Different operating systems producing diffrent checksums
- No longer have to touch/create .zip file before running terraform

```hcl
module "archive_lambda" {                                                       
    source = "zip_file/"                                                        
    source_dir = "dummy_lambda/"                                                
    output_path = "dummy_lambda.zip"                                            
}                                                                               
                                                                                
                                                                                
resource "aws_lambda_function" "lambda_function" {                        
  filename         = "${module.archive_lambda.zip_path}"                                        
  source_code_hash = "${module.archive_lambda.base64sha256}"                                                           
}
```
