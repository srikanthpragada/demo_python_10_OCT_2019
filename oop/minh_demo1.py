
class A:
    def m1(self):
        print("Method m1() in A")


class B:
    def m1(self):
        print("Method m1() in B")


class C(A,B):
    def m2(self):
        print("Method m1() in C")


obj = C()
print(C.mro())


