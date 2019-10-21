def print_values(*values):
    for v in values:
        print(v)


def details(**values):
    pass


details(a=10, b=20, c=30)

print_values(10, 20, 30)
print_values(10)
