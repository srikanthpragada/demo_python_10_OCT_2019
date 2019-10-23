def divby3(n):
    return n % 3 == 0


def iseven(n):
    return n % 2 == 0


nums = [10, 11, 15, 60, 70]

for n in filter(lambda n: n % 2 == 0, nums):
    print(n)

for n in filter(divby3, nums):
    print(n)
