from fnmatch import *

def dels(num):
    d = set()
    for j in range(2, int(num ** 0.5) + 1):
        if num % j == 0:
            d.add(j)
            d.add(num // j)
    return list(d)
def prost(num):
    d = set()
    for j in range(2, int(num ** 0.5) + 1):
        if num % j == 0:
            return False
    return True * num != 1


for i in range(1, 10**5):
    d = dels(i)
    if fnmatch(str(i), '1*77') and len(d) == 2:
        if prost(d[0]) and prost(d[1]):
            print(i)