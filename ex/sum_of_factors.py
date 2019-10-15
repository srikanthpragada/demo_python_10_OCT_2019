
num = int(input("Enter a number :"))
sum = 0

for i in range(2, num//2  + 1):
    if num % i == 0:
        sum += i

print(f"Sum of factors = {sum}")
