import sys

try:
    f = open("marks.txt", "rt")
except:
    print("Sorry! File cannot be opened!")
    sys.exit(1)

for line in f.readlines():
    parts = line.strip("\n").split(",")
    name = parts[0]
    total = 0
    for m in parts[1:]:
        total += int(m)

    print(f"{name:20s}  {total}")

f.close()

