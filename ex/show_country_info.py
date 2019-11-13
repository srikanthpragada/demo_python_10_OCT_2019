import requests
import sys

code = input("Enter country code : ")
resp = requests.get(f"https://restcountries.eu/rest/v2/alpha/{code}")
if resp.status_code != 200:
    print("Sorry! Could not get country details.")
    sys.exit(1)

country = resp.json()
print(f"Name        : ", country['name'])
print(f"Borders     : ", ",".join(country['borders']))

names = []
for c in country['currencies']:
    names.append(c['name'])

print(f"Currencies  : ", ",".join(names))
