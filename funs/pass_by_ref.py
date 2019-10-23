def get_length(n):
    return len(n)


names = ['Gabby', 'Travis', 'Bill', 'Joe', 'jason']

for n in sorted(names, key=str.upper):
    print(n)

for n in sorted(names, key=lambda n: n[:3]):
    print(n)

for n in sorted(names, key=get_length):
    print(n)

for n in sorted(names, key=len):
    print(n)

d = {1: 10, 2: 5, 4: 15, 3: 2}

for t in sorted(d.items(), key=lambda t: t[1]):
    print(t)
