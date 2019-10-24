# Module with number related functions
def iseven(n):
    """
    Returns true if the given number is even otherwise false

    n(int):  Number which is to be tested

    return:  True for even, False for odd
    """
    return n % 2 == 0


def isodd(n):
    return n % 2 == 1


def isprime(n):
    pass


if __name__ == '__main__':
    print("Running as script")
else:
    print("Importing numfuns")
