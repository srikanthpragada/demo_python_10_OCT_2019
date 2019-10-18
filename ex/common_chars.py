
st1 = input("Enter first string :")
st2 = input("Enter second string :")

common_chars = set(st1) & set(st2)

for ch in common_chars:
    print(ch)

