import requests
import json

# Set the repository name and the Personal Access Token
repository = "your_repository_name"
pat = "DefaultEndpointsProtocol=https;AccountName=gabrielunique;AccountKey=Q0cuA+qoaj2+9gRu2dIMtoug21qEDvwY0vTV5SeMKehlGNhF59sn8BNjU2dqltach10hA4PQwgcC+AStsEcQBw=="

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
