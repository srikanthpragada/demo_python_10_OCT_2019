def fun1():
    print("In fun1")


def fun1(msg):
    print("In fun1 with msg")

fun1()
fun1("Hello")

def multiply(n1, n2):
    return n1 * n2


def math_op(a, b, op):
    print(op(a, b))


math_op(10, 20, multiply)
# math_op(10, 20, 30)     # Invalid as 30 is not a function
