
def has_ow(n):
    s1 = set("aeiouAEIOU")   # create a set
    s2 = set(n)   # creat a set for string
    return len(s1.intersection(s2)) > 0


names = ['Andy','Bill','Joe','cdf']

for n in filter(has_ow,names):
    print(n)
