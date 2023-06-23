import sys
import os
import requests

def update_github_raw(keys):
    GITHUB_RAW_URL = "https://raw.githubusercontent.com/KebabBusiness09/LICENZE-DA-GENERARE/main/license_keys.txt"
    GITHUB_ACCESS_TOKEN = os.environ["ACCESS_TOKEN"]

    keys_str = "\n".join(keys)
    headers = {"Authorization": f"token {GITHUB_ACCESS_TOKEN}"}
    response = requests.put(GITHUB_RAW_URL, data=keys_str, headers=headers)
    response.raise_for_status()

if __name__ == "__main__":
    keys = sys.argv[1].split(",")
    update_github_raw(keys)
