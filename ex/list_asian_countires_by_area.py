import requests


def select_country(c):
    return c['region'] == 'Asia' and c['area'] is not None


resp = requests.get("https://restcountries.eu/rest/v2/all")
countries = resp.json()

for c in sorted(filter(select_country, countries),
                key=lambda c: c['area'], reverse=True)[:10]:
    print(f"{c['name']:30}  - {c['area']}")
