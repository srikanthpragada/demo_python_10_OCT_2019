import re

f = open("customers.txt", "rt")
customers = {}

for line in f.readlines():
    mobile = re.search(r'\d+', line)
    if mobile is None:
        continue

    name = re.search(r"[A-Za-z ]+", line)
    if name is None:
        continue

    # add to dict as we found both name and mobile
    customers[name.group().strip(" ")] = mobile.group()

f.close()

for name, mobile in sorted(customers.items()):
    print(f"{name:20s} {mobile}")
