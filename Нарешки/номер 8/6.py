from itertools import *

c = 0
for j in range(3, 7):
    a = product('КРЫША', repeat = j)
    for i in a:
        s= ''.join(i)
        if s.count('Ы') <= 2 and (s.count('А') <= 2) and all([k not in s[1:] for k in 'КРШ']):
            print(s)
            c+=1
    print(c)