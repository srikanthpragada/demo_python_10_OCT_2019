# Average of positive numbers
sum = 0
count = 0

while True:
    num = int(input("Enter a number :"))
    if num == 0:
        break

    if num < 0:
        continue

    sum += num
    count += 1

print(f"Average : {sum/count}")
