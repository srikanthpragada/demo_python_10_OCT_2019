from bs4 import BeautifulSoup
import requests
import sys

while True:
    website = input("Enter website [end to stop]:")
    if website == 'end':
        break

    try:
        resp = requests.get(website)
    except:
        print("Sorry! Could not get details from website")
        continue

    if resp.status_code != 200:
        print("Sorry! Could not get details!")
        continue

    bs = BeautifulSoup(resp.text, 'html.parser')
    scripts = bs.find_all("script")

    for s in scripts:
        if 'src' in s.attrs:
            print(s['src'])


