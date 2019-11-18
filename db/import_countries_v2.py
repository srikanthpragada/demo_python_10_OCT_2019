import requests
import sqlite3

con = sqlite3.connect(r"e:\classroom\python\oct10\hr.db")
cur = con.cursor()

resp = requests.get("https://restcountries.eu/rest/v2/all")
countries = resp.json()
rows = []
for c in countries:
    rows.append((c['alpha3Code'], c['name'], c['capital'], c['population'], c['area']))

cur.executemany("insert into countries values(?,?,?,?,?)", rows)
con.commit()
con.close()
print("Imported countries details!")
