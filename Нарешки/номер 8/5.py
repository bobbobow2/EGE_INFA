from itertools import *
c = 0
for j in range(4, 7):
    a = product('ЧОАНИМЕ', repeat = j)
    for i in a:
        s = ''.join(i)
        if s.count('М') == 3:
            c += 1
print(c)
