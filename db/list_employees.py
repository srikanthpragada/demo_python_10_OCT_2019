import sqlite3

# Connect to DB
con = sqlite3.connect(r"e:\classroom\python\oct10\hr.db")
cur = con.cursor()

cur.execute("select * from employees order by salary desc")

for emp in cur.fetchall():
    print( f"{emp[0]:5d} {emp[1]:20s} {emp[2]:10d}  {emp[3]}")

con.close()

