


a = 10
d = {}
l  = [10,20,30]
try:
    v = int("abc")
    l.append(a)
    # print(l[4])
    #print(d['a'])
except ValueError as ex:
    print(ex)
except IndexError as ex:
    print(ex)
except Exception:
    print("Error")
finally:
    print("Over")

print("Goes on ")