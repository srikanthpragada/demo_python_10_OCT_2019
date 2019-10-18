# Char Frequency for a string

st = input("Enter string :")
chars = set()

for ch in st:
    if ch not in chars:
        print(ch, st.count(ch))
        chars.add(ch)



