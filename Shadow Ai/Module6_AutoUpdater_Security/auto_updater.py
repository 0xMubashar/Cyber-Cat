
# auto_updater.py

import requests
import os
import hashlib

UPDATE_URL = "https://yourserver.com/update/latest.zip"  # Replace with real server
UPDATE_DIR = "updates/"
HASH_FILE = "latest_hash.txt"

def download_update():
    response = requests.get(UPDATE_URL)
    if response.status_code == 200:
        os.makedirs(UPDATE_DIR, exist_ok=True)
        zip_path = os.path.join(UPDATE_DIR, "latest.zip")
        with open(zip_path, "wb") as f:
            f.write(response.content)
        return zip_path
    return None

def verify_integrity(file_path, expected_hash):
    sha256 = hashlib.sha256()
    with open(file_path, "rb") as f:
        while chunk := f.read(4096):
            sha256.update(chunk)
    return sha256.hexdigest() == expected_hash

def run_update():
    print("Checking for update...")
    zip_path = download_update()
    if zip_path:
        expected_hash = open(HASH_FILE).read().strip()
        if verify_integrity(zip_path, expected_hash):
            print("Update verified. Extracting...")
            # extract logic here (use zipfile)
        else:
            print("Hash mismatch. Update aborted.")
    else:
        print("Failed to download update.")

if __name__ == "__main__":
    run_update()
