from itertools import *
a = product('КОСУФ', repeat = 5)
for k, i in enumerate(a):
    s = ''.join(i)
    if s.count('У') == 2 and s.count('Ф') == 0:
        print(k +1)