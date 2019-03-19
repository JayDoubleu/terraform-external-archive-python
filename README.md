# terraform-archive-python
Python script to archive files to be used by terraform

archive.py overwrites operating system and creation date headers within zip file.  
This should resolve issue when zip file is created on multiple platforms.  
Running terraform apply should produce the same md5sums on every operating system and only change when file contents changed.  

Can be also tested from shell:

`echo '{"source_dir": "test_files", "output_path": "zipinfo.zip"}'|python archive.py`

Should work with python2 and 3. 
