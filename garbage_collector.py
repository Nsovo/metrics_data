import os
import shutil
import glob

def garbage_collect(directory, retention_mb):
    files = glob.glob(os.path.join(directory, '*'))
    total_size = sum(os.path.getsize(f) for f in files)

    while total_size > retention_mb * 1024 * 1024:
        oldest_file = min(files, key=os.path.getctime)
        os.remove(oldest_file)
        files.remove(oldest_file)
        total_size -= os.path.getsize(oldest_file)
