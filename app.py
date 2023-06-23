from flask import Flask, render_template, request, jsonify
import requests
import os

app = Flask(__name__)

LICENSE_KEYS_FILE = "license_keys.txt"
GITHUB_RAW_URL = "https://raw.githubusercontent.com/KebabBusiness09/LICENZE-DA-GENERARE/main/license_keys.txt"
GITHUB_ACCESS_TOKEN = os.environ.get("GITHUB_ACCESS_TOKEN")  # Retrieve the access token from environment variable

@app.route("/")
def index():
    return render_template("key_management.html")

@app.route("/get_keys")
def get_keys():
    keys = fetch_keys_from_file()
    return jsonify({"keys": keys})

@app.route("/add_key", methods=["POST"])
def add_key():
    key = request.form.get("key")
    if key:
        append_key_to_file(key)
        update_github_raw()
        return jsonify({"message": "Key added successfully"})
    else:
        return jsonify({"error": "Invalid key"})

def fetch_keys_from_file():
    with open(LICENSE_KEYS_FILE, "r") as file:
        return file.read().strip().split("\n")

def append_key_to_file(key):
    with open(LICENSE_KEYS_FILE, "a") as file:
        file.write(key + "\n")

def update_github_raw():
    with open(LICENSE_KEYS_FILE, "r") as file:
        keys_str = file.read()

    headers = {
        "Authorization": f"token {GITHUB_ACCESS_TOKEN}",
        "Content-Type": "text/plain",
    }
    response = requests.put(GITHUB_RAW_URL, data=keys_str, headers=headers)
    response.raise_for_status()

if __name__ == "__main__":
    app.run()
