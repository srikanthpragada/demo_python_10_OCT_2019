from bs4 import BeautifulSoup
import requests
import sys

resp = requests.get("http://www.srikanthtechnologies.com")
if resp.status_code  != 200:
    print("Sorry! Could not get details!")
    sys.exit(1)


bs = BeautifulSoup(resp.text, 'html.parser')
for t in bs.find_all('img'):
    url = t['src']
    title = ''
    if 'title' in t.attrs:
        title = t['title']

    print(f"{url} - {title}")


