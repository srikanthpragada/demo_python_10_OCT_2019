def even_numbers(start, end):
    if start % 2 != 0:
        start += 1

    while start <= end:
        yield start
        start += 2


g = even_numbers(11, 20)
print(g.__next__())
print(g.__next__())

# for n in even_numbers(11,20):
#     print(n)
