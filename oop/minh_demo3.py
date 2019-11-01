class A:
    def __init__(self):
        print("A", type(self))


class B:
    def __init__(self):
        print("B")


class C(A, B):
    def __init__(self):
        A.__init__(self)
        B.__init__(self)


obj = C()
