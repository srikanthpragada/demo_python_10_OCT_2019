def get_length(n):
    return len(n)


names = ['Gabby','Travis','Bill','Joe','jason']

for n in sorted(names,key=str.upper):
    print(n)


for n in sorted(names,key=get_length):
    print(n)

for n in sorted(names,key=len):
    print(n)