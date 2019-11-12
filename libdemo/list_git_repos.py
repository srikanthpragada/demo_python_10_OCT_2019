
# Lists repos of the given github user

import requests
import sys

user = input("Enter github username : ")
URL = f"https://api.github.com/users/{user}/repos"

resp = requests.get(URL)
if resp.status_code != 200:
    print("Sorry! Username is invalid!")
    sys.exit(1)

repos = resp.json()

if len(repos) == 0:
    print("Sorry! No repos found!")
    sys.exit(2)
    
for repo in repos:
    print(repo['name'])


