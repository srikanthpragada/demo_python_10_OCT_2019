class A:
    def m1(self):
        print("Method m1() in A")


class B(A):
    def m1(self):
        print("Method m1() in B")


class C(A):
    def m2(self):
        print("Method m1() in C")


class D(C, B):
    pass


print(D.mro())
