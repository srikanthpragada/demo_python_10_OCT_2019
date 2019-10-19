def add(a, b):
    return a + b


print(add(10, 20))  # By position
print(add(b=10, a=5))  # By name
# print(add(b=10))


def line(size=10, char='-'):
    print(char * size)


# print(add('Abc', 20))
line()
line(20)
line(20, '*')
line(10, '.')
line(char='.', size=20)
line(char='*')
