g = 100  # Global


def f1():
    global g
    g = g + 1
    a = 10  # Enclosing

    def f2():
        nonlocal a
        a = a + 1
        b = 20  # Local
        print(g, a, b)

    f2()
    print(a)


f1()
