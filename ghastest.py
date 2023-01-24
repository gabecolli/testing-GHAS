import requests
import json

# Set the repository name and the Personal Access Token
repository = "your_repository_name"
pat = "removed secret"

# Set the headers for the API call
headers = {
    "Accept": "application/vnd.github+json",
    "Authorization": f"Token {pat}",
}

# Call the GitHub API to create a new code scanning alert
url = f"https://api.github.com/repos/{repository}/code-scanning/alerts"
data = {
    "name": "Test Alert",
    "query": "language:python AND vulnerability",
    "reason": "Testing code scanning feature",
}
response = requests.post(url, headers=headers, json=data)

# Print the response
print(response.json())

import os

def get_file_contents(file_path):
    with open(file_path, 'r') as f:
        contents = f.read()
    return contents

def main():
    file_path = os.environ.get('FILE_PATH')
    if file_path:
        contents = get_file_contents(file_path)
        print(contents)
    else:
        print("No file path provided.")

