from itertools import *
t = {i + j for i in '0246' for j in '0246'}
t1 = {i + j for i in '1357' for j in '1357'}
print(t)
print(t1)
c = 0
a = permutations('01234567')
for i in a:
    s = ''.join(i)
    # print([k not in s for k in list(t)])
    if all(k not in s for k in list(t)) and (s[0] != '0') and all(k not in s for k in list(t1)):
        c += 1
        print(s)
print(c)
