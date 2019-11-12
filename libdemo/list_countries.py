import requests

resp = requests.get("https://restcountries.eu/rest/v2/all")

countries = resp.json()
for c in countries:
    print(c['name'])
