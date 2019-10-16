
st =input("Enter a string :")

alpha = digits = others = 0

for c in st:
    if c.isalpha():
        alpha +=1
    elif c.isdigit():
        digits += 1
    else:
        others +=1


print(f"Alpha : {alpha}, Digits : {digits}, Others : {others}")

