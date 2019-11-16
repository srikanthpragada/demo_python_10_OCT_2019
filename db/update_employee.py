import sqlite3

# Connect to DB
con = sqlite3.connect(r"e:\classroom\python\oct10\hr.db")
cur = con.cursor()

id = input("Enter id : ")
sal = input("Enter salary : ")

cur.execute("update employees set salary = ? where empid = ? ", (sal, id))
if cur.rowcount == 0:
    print("Employee id is not found!")
else:
    con.commit()
    print("Updated salary sucessfully!")

con.close()
