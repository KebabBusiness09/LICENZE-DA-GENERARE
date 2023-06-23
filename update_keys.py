import sys
import os
import requests

GITHUB_RAW_URL = "https://raw.githubusercontent.com/KebabBusiness09/LICENZE-DA-GENERARE/main/license_keys.txt"

# Retrieve the GitHub access token from environment variables
GITHUB_ACCESS_TOKEN = os.environ.get("GITHUB_ACCESS_TOKEN")

def update_github_raw(keys):
    keys_str = "\n".join(keys)
    headers = {"Authorization": f"token {GITHUB_ACCESS_TOKEN}"}
    response = requests.put(GITHUB_RAW_URL, data=keys_str, headers=headers)
    response.raise_for_status()

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("No keys provided. Please provide comma-separated keys as command-line arguments.")
        sys.exit(1)
        
    keys = sys.argv[1].split(",")
    update_github_raw(keys)
