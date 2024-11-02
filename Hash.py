import os
import hashlib
my_first_sha = "d6539d5b43e4923900eb6208315ee1542b2a32ce9aed4cf458131220d3aa2f76"
def generate_sha256(file_path):
    """Generate SHA-256 hash for a file."""
    with open(file_path, "rb") as f:
        return hashlib.sha256(f.read()).hexdigest()  
# List of files to check
files_to_check = ["9JA TOP 10 WEEZYWYN.txt"]

for file_path in files_to_check:
    if os.path.isfile(file_path):
        print(f"{file_path}: {generate_sha256(file_path)}")
        if my_first_sha== generate_sha256(file_path):
             print("file is okay")
        else:
            print("file tampared")
    else:
        print(f"{file_path} does not exist.")