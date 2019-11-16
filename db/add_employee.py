import sqlite3

# Connect to DB
con = sqlite3.connect(r"e:\classroom\python\oct10\hr.db")
cur = con.cursor()

name = input("Enter name   : ")
sal = input("Enter salary : ")
job = input("Enter job    : ")

cur.execute("insert into employees (empname,salary,job) values(?,?,?)",
            (name, sal, job))

con.commit()

con.close()
