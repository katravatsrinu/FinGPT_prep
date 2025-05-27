import requests

response = requests.get("https://api.github.com/users/octocat")

if response.status_code == 200:
    data = response.json()
    print("User:", data["login"])
    print("Bio:", data["bio"])
else:
    print("Failed to fetch user")
