# Copy data from employees.txt to departments.txt
depts = {}

f = open("employees.txt","rt")

for line in f.readlines():
    parts = line.strip("\n").split(",")
    if len(parts) < 2:
        continue

    deptno = parts[0]
    empname = parts[1]

    if deptno in depts:
        depts[deptno].add(empname)  # add name to existing set
    else:
        depts[deptno] = {empname} # create an entry with set

f.close()

f = open("departments.txt","wt")
for deptno,employees in depts.items():
    emps = ','.join(sorted(employees))
    f.write(f"{deptno},{emps}\n")

f.close()


