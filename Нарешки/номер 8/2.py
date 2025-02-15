from itertools import *
cnt = 0
a = permutations('КАБАЛА')
spis = set()
for i in a:
    s = "".join(i)
    if not "АА" in s:
        cnt += 1
        spis.add(s)
print(len(spis))