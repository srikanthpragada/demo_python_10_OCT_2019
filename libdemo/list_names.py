f = open("names.txt", "rt")

for line in f:
    print(line.strip("\n"))

f.close()
