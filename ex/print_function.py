
def print_values(*values, **keywords):

    for v in values:
        print(v)

    for k,v in keywords.items():
        print(k,v)



print_values(10,20,30)
print_values(1,2,a = 10, b = 20)