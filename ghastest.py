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

testing = "this var is created to test code owners file. second attempt"

def test_alert_triggered():
    username = "admin"
    password = "secret"
    if username == "admin" and password == "secret":
        print("Access granted.")
    else:
        print("Access denied.")

    )
    cursor = db.cursor()
    query = "SELECT * FROM users WHERE name='" + user_input + "';"
    cursor.execute(query)
    result = cursor.fetchall()
    db.close()
    return result

