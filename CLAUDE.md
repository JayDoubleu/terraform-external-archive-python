# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Overview

This is a Terraform module that creates consistent .zip archives across different operating systems (Linux/Windows) using Python. It solves cross-platform checksum inconsistencies by normalizing file attributes and line endings.

## Architecture

The module consists of three main components:

1. **main.tf**: Terraform configuration that uses the `external` data source to invoke the Python script and expose outputs (`zip_path` and `base64sha256`)

2. **archive.py**: Python script that:
   - Accepts JSON input via stdin with `source_dir` and `output_path`
   - Recursively walks the source directory
   - Normalizes Windows line endings to Unix (`\r\n` → `\n`)
   - Creates deterministic zip files with fixed timestamps (1980-01-01) and permissions
   - Returns JSON output with zip metadata including base64-encoded SHA256 hash

## Key Technical Details

- The Python script ensures deterministic zip creation by:
  - Setting fixed timestamps on all files
  - Using consistent file permissions (0o777)
  - Sorting files before adding to the archive
  - Converting line endings to Unix format
- Compatible with both Python 2 and Python 3
- The module is typically used with AWS Lambda deployments to ensure consistent `source_code_hash` values

## Testing

To test the archive generation:
```bash
echo '{"source_dir": "path/to/source", "output_path": "output.zip"}' | python archive.py
```