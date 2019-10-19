# Display names that have length more than avg. length of all names
names = []
total_len = 0
while True:
    name = input("Enter a name [end to stop] :")
    if name == "end":
        break

    names.append(name)
    total_len += len(name)

avglen = total_len // len(names)

for n in names:
    if len(n) > avglen:
        print(n)



