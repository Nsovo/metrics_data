import os
import glob
import time

def garbage_collector(path, size_limit_mb):
    # Get all files in the directory
    files = glob.glob(os.path.join(path, '*'))
    # Sort the files by modification time in reverse order (newest first)
    files.sort(key=os.path.getmtime, reverse=True)

    # Convert size limit to bytes
    size_limit_bytes = size_limit_mb * 1024 * 1024

    total_size = 0
    for file in files:
        total_size += os.path.getsize(file)

    # Delete the oldest files until the total size is under the limit
    while total_size > size_limit_bytes and files:
        oldest_file = files.pop()
        total_size -= os.path.getsize(oldest_file)
        os.remove(oldest_file)

while True:
    file_path = os.path.join(os.path.dirname(__file__), "data")
    garbage_collector(file_path, 500)  # 500 MB limit
    time.sleep(3600)