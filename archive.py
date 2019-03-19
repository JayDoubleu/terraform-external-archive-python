import os
import time
import sys
import json
import zipfile
import hashlib


def get_all_file_paths(directory):
    file_paths = []
    for root, directories, files in os.walk(directory):
        for filename in files:
            filepath = os.path.join(root, filename)
            file_paths.append({"filepath": filepath, "filename": filename})
    return file_paths


def main():
    data = json.load(sys.stdin)
    file_paths = get_all_file_paths(data['source_dir'])
    try:
        for file_path in file_paths:
            zf = zipfile.ZipFile(
                data['output_path'],
                mode='w',
            )
            file_bytes = open(file_path['filepath'], "rb").read()
            info = zipfile.ZipInfo(
                str(file_path['filename']),
                date_time=(1980, 1, 1, 00, 00, 00),
            )
            info.compress_type = zipfile.ZIP_DEFLATED
            info.create_system = 0
            zf.writestr(info, file_bytes)
            zf.close()
    finally:
        zip_data = {
            "output_path":
            str(data['output_path']),
            "output_absolute_path":
            str(os.path.abspath(data['output_path'])),
            "output_size":
            str(os.stat(data['output_path']).st_size),
            "output_md5":
            str(
                hashlib.md5(open(data['output_path'],
                                 'rb').read()).hexdigest())
        }
        print(json.dumps(zip_data))


if __name__ == "__main__":
    main()
