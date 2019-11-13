import requests

resp = requests.get("https://restcountries.eu/rest/v2/all")
countries = resp.json()

for c in sorted(countries, key= lambda d: d['population'], reverse=True):
    print(f"{c['name']:30}  - {c['population']}")

