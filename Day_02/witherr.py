import requests

response = requests.get("https://api.github.com/users/octocat")

if response.status_code == 200:
    print("Success")
    print(response.json())
else:
    print("Failed with status", response.status_code)
