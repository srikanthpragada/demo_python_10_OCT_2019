from bs4 import BeautifulSoup
import requests
import sys

resp = requests.get("http://www.srikanthtechnologies.com")
if resp.status_code != 200:
    print("Sorry! Could not get details!")
    sys.exit(1)

bs = BeautifulSoup(resp.text, 'html.parser')

table = bs.find("table", {'id': 'ctl00_ContentPlaceHolder1_GridView2'})
# print(table)

rows = table.find_all("tr")[1:]

for row in rows:
    cols = row.find_all("td")
    course = cols[0].find("a").text
    stdate = cols[2].text
    print(f"{course:30s} {stdate}")
