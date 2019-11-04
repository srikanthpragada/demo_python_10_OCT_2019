
sum = 0
count = 0
for i in range(5):
    try:
        num = int(input("Enter a number:"))
        sum += num
        count += 1
    except ValueError:
        print("Invalid Number!")


print("Average= ", sum / count)
