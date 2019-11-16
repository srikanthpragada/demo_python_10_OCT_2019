import sqlite3

# Connect to DB
con = sqlite3.connect(r"e:\classroom\python\oct10\hr.db")
cur = con.cursor()

cur.execute("select avg(salary),count(empid) from employees")
row = cur.fetchone()
print("Average salary   : ", row[0])
print("No. of employees : ", row[1])

con.close()

