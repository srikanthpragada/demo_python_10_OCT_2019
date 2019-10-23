def swap(n1,n2):
    print(id(n1), id(n2))
    t = n1
    n1 = n2
    n2 = t
    print(id(n1), id(n2))


a = 10
b = 20
print(id(a), id(b))
swap(a,b)
print(a,b)