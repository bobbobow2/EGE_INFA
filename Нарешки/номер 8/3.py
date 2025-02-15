from itertools import *

a = product('0123456789AB', repeat = 5)
c = 0
for i in a:
    s = ''.join(i)
    t = len([i for i in s if i in '9AB'])
    if (t <= 3) and (s.count("7") == 1) and s[0]:
        c += 1
print(c)
